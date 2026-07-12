#!/usr/bin/env python3
"""
Full-surface Polymarket pull + filter, v3 — July 12, 2026.

v2's traversal (plain offset pagination) cannot complete: the Gamma API
rejects offset>2000 (HTTP 422) and the live-market universe exceeds 4000.
v3 replaces the traversal layer with EVENT-windowed pulls:

  - Walk /events (not /markets), windowed by end_date_min/end_date_max
    in half-open windows [A, B). Events carry dates even when their
    embedded markets do not, so null-endDate markets ride along.
  - One extra unfiltered ascending event walk (first 2000) catches any
    null-endDate EVENTS and doubles as completeness reference set A.
  - Harvest every embedded market from every event; dedup by conditionId.
  - Completeness check A: every event id in the unfiltered first-2000
    walk must appear in the window union. Any hole -> loud fail, no output.
  - Completeness check B: every market id in an unfiltered first-2000
    MARKET walk must appear in the harvested pool pre-filter. Any hole ->
    loud fail, no output. B validates the harvest layer itself.

Filter internals are v2's, unchanged (hash of record a96d13a9...):
prob band 0.15-0.80, MIN_DAYS=14, open-ended kept + tagged, sports
exclusion, binary check, fail-loud fetch. No server-side liquidity
filter (rule 3e allows below-floor exceptions; filter at selection).

Known limitation (documented, not hidden): completeness is proven
against the reachable reference sets. A null-endDate event with id
beyond the 2000-offset frontier, if one exists, is invisible to both
traversal and check. Evidence to date: zero null events observed in
sampling; all known null-endDate markets sit inside dated events.
"""

import json
import sys
import time
import urllib.request
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

MARKETS_BASE = "https://gamma-api.polymarket.com/markets"
EVENTS_BASE = "https://gamma-api.polymarket.com/events"
PAGE_SIZE = 100
OFFSET_CEILING = 2000  # API returns 422 above this; probe-verified 2026-07-12
PROBE_OFFSET = 1900    # window-overflow probe point
OUTPUT_FILE = Path.home() / f"Projects/latentforge-latentmas/scratch/qualifying_pool_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.json"

TODAY = datetime.now(timezone.utc)
MIN_DAYS = 14
MIN_PROB = 0.15
MAX_PROB = 0.80

# Half-open date windows [start, end) covering the live event universe.
# Sized from probe data: near-dated months are dense, far dates sparse.
# Any window that overflows fails loud with instructions to split it.
DATE_WINDOWS = [
    ("2020-01-01", "2026-07-01"),
    ("2026-07-01", "2026-07-13"),
    ("2026-07-13T00:00:00Z", "2026-07-13T12:00:00Z"),
    ("2026-07-13T12:00:00Z", "2026-07-14"),
    ("2026-07-14", "2026-07-15"),
    ("2026-07-15", "2026-07-17"),
    ("2026-07-17", "2026-07-20"),
    ("2026-07-20", "2026-08-01"),
    ("2026-08-01", "2026-09-01"),
    ("2026-09-01", "2026-10-01"),
    ("2026-10-01", "2026-11-01"),
    ("2026-11-01", "2026-12-01"),
    ("2026-12-01", "2027-01-01"),
    ("2027-01-01", "2028-01-01"),
    ("2028-01-01", "2031-01-01"),
]


def fetch_json(base, params):
    url = base + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "latentforge-fullpull/3.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_pages(base, extra_params, label):
    """Offset-paginate one query to exhaustion. Fail loud on any error,
    fail loud if we hit the offset ceiling with pages still full."""
    results = []
    page = 0
    while True:
        offset = page * PAGE_SIZE
        if offset > OFFSET_CEILING:
            raise RuntimeError(
                f"[{label}] hit offset ceiling with full pages remaining - "
                f"slice too big, must be split. Partial pool is not a pool.")
        params = {"closed": "false", "limit": str(PAGE_SIZE),
                  "offset": str(offset), "order": "id", "ascending": "true"}
        params.update(extra_params)
        batch = None
        last_err = None
        for attempt in range(1, 4):
            try:
                batch = fetch_json(base, params)
                break
            except Exception as e:
                last_err = e
                print(f"  [{label}] page {page} attempt {attempt} failed: {e}")
                time.sleep(3 * attempt)
        if batch is None:
            raise RuntimeError(
                f"[{label}] page {page} failed after 3 attempts: {last_err}. Aborting.") from last_err
        if not batch:
            break
        results.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        page += 1
    return results


def probe_window(start, end):
    """Ask for offset=PROBE_OFFSET inside a window. Full page there means
    the window is too big for the ceiling and must be split BEFORE pulling."""
    params = {"closed": "false", "limit": str(PAGE_SIZE),
              "offset": str(PROBE_OFFSET), "order": "id", "ascending": "true",
              "end_date_min": start, "end_date_max": end}
    batch = fetch_json(EVENTS_BASE, params)
    return len(batch)


def fetch_events_windowed():
    """Pull every live event via half-open date windows. Probe each window
    for overflow first; fail loud naming the offending window."""
    all_events = {}
    for start, end in DATE_WINDOWS:
        n = probe_window(start, end)
        if n >= PAGE_SIZE:
            raise RuntimeError(
                f"Window [{start}, {end}) overflows the offset ceiling "
                f"(probe at {PROBE_OFFSET} returned a full page). Split this "
                f"window in DATE_WINDOWS and rerun. No output written.")
        events = fetch_pages(EVENTS_BASE,
                             {"end_date_min": start, "end_date_max": end},
                             f"window {start}..{end}")
        for e in events:
            eid = e.get("id")
            if eid:
                all_events[eid] = e
        print(f"  window [{start}, {end}): {len(events)} events "
              f"(union so far: {len(all_events)})")
    return all_events


def fetch_events_unfiltered_first2000():
    """Reference set A + null-endDate-event sweep. Plain ascending walk,
    stops at the ceiling by design (short final read is expected here)."""
    results = []
    for page in range((OFFSET_CEILING // PAGE_SIZE) + 1):
        params = {"closed": "false", "limit": str(PAGE_SIZE),
                  "offset": str(page * PAGE_SIZE),
                  "order": "id", "ascending": "true"}
        try:
            batch = fetch_json(EVENTS_BASE, params)
        except Exception as e:
            raise RuntimeError(f"[ref-walk events] page {page} failed: {e}. Aborting.") from e
        if not batch:
            break
        results.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
    return results


def fetch_markets_unfiltered_first2000():
    """Reference set B: the first 2000 reachable markets, for validating
    the harvest layer end-to-end (includes known null-endDate specimens)."""
    results = []
    for page in range((OFFSET_CEILING // PAGE_SIZE) + 1):
        params = {"closed": "false", "limit": str(PAGE_SIZE),
                  "offset": str(page * PAGE_SIZE),
                  "order": "id", "ascending": "true"}
        try:
            batch = fetch_json(MARKETS_BASE, params)
        except Exception as e:
            raise RuntimeError(f"[ref-walk markets] page {page} failed: {e}. Aborting.") from e
        if not batch:
            break
        results.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
    return results


def harvest_markets(events_by_id):
    """Extract every embedded market from every event. Dedup by
    conditionId (fallback id, then slug) — a market can appear under
    multiple events."""
    markets = {}
    eventless = 0
    for e in events_by_id.values():
        for m in (e.get("markets") or []):
            key = m.get("conditionId") or m.get("id") or m.get("slug")
            if not key:
                eventless += 1
                continue
            if key not in markets:
                markets[key] = m
    if eventless:
        print(f"  WARNING: {eventless} embedded markets had no usable id key")
    return markets


# Filter internals: import from v2 (hash of record a96d13a9...) so the
# filter logic of record lives in exactly one file. Traversal is v3's own.
sys.path.insert(0, str(Path(__file__).parent))
from full_pull_and_filter_v2 import (
    parse_end_date, parse_yes_price, is_sports, tag_domain,
    get_volume, get_liquidity, filter_markets,
)


def completeness_check_a(ref_events, windowed_events_by_id):
    """Every event id reachable in the plain first-2000 walk must appear
    in the window union. A null-endDate event would fail here BY DESIGN -
    that failure is the discovery of a real hole, not a bug."""
    missing = [e.get("id") for e in ref_events
               if e.get("id") and e.get("id") not in windowed_events_by_id]
    if missing:
        nulls = [e.get("id") for e in ref_events
                 if e.get("id") in set(missing) and not e.get("endDate")]
        raise RuntimeError(
            f"COMPLETENESS CHECK A FAILED: {len(missing)} events in the "
            f"reference walk are absent from the window union. "
            f"First 10 missing: {missing[:10]}. "
            f"Of these, null-endDate: {len(nulls)} ({nulls[:10]}). "
            f"No output written.")
    print(f"  Check A PASS: all {len(ref_events)} reference events in window union.")


def completeness_check_b(ref_markets, harvested_by_key):
    """Every market id reachable in the plain first-2000 MARKET walk must
    appear in the harvested pool. Validates the harvest layer end to end,
    including that null-endDate markets rode in on their events."""
    missing = []
    for m in ref_markets:
        key = m.get("conditionId") or m.get("id") or m.get("slug")
        if key and key not in harvested_by_key:
            missing.append((m.get("id"), m.get("endDate")))
    if missing:
        nulls = sum(1 for _, ed in missing if not ed)
        raise RuntimeError(
            f"COMPLETENESS CHECK B FAILED: {len(missing)} markets in the "
            f"reference walk are absent from the harvest. "
            f"First 10 (id, endDate): {missing[:10]}. "
            f"Null-endDate among missing: {nulls}. No output written.")
    print(f"  Check B PASS: all {len(ref_markets)} reference markets harvested.")


def main():
    print("v3 event-windowed pull - " + TODAY.strftime("%Y-%m-%d"))
    print("\n[1/5] Windowed event traversal...")
    windowed = fetch_events_windowed()
    print(f"  Window union: {len(windowed)} events")

    print("\n[2/5] Reference walk A (events, first 2000)...")
    ref_events = fetch_events_unfiltered_first2000()
    print(f"  {len(ref_events)} reference events")
    null_events = [e for e in ref_events if e.get("id") and not e.get("endDate")]
    for e in null_events:
        windowed.setdefault(e["id"], e)
    print(f"  Null-endDate events merged from reference walk: {len(null_events)}")
    completeness_check_a(ref_events, windowed)

    print("\n[3/5] Harvesting embedded markets...")
    harvested = harvest_markets(windowed)
    print(f"  {len(harvested)} unique markets harvested")

    print("\n[4/5] Reference walk B (markets, first 2000)...")
    ref_markets = fetch_markets_unfiltered_first2000()
    print(f"  {len(ref_markets)} reference markets")
    backfilled = 0
    for m in ref_markets:
        key = m.get("conditionId") or m.get("id") or m.get("slug")
        if key and key not in harvested:
            harvested[key] = m
            backfilled += 1
    print(f"  Backfilled from reference walk (invisible/closed parent events): {backfilled}")
    completeness_check_b(ref_markets, harvested)

    print("\n[5/5] Applying v2 filter internals...")
    survivors, rejects = filter_markets(list(harvested.values()))
    print(f"\n{'='*70}\nQUALIFYING POOL: {len(survivors)} markets\n{'='*70}")
    print("Rejection breakdown (first failure wins):")
    for reason, count in rejects.most_common():
        print(f"  {reason:20s}  {count}")
    open_ended = sum(1 for s in survivors if s.get("open_ended"))
    print(f"\nOpen-ended (null-endDate) survivors: {open_ended}")
    by_domain = Counter(s["tags"][0] for s in survivors)
    print("Domain breakdown:", dict(by_domain))

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(survivors, f, indent=2)
    print(f"\nSaved qualifying pool to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
