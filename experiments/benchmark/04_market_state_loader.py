#!/usr/bin/env python3
"""
04_market_state_loader.py — LatentForge Mode 1 v1 market-state loader.

Reads the 8-market benchmark registry, fetches their current state from the
Polymarket Gamma API in one bulk call, normalizes it into deterministic Mode 1
semantics, and writes a single daily snapshot that all downstream consumers read.

Built against the LOCKED loader contract:
  founder_inputs/2026-06-27_loader_contract_founder_synthesis.md  (commit c0b53ce)

This file is implementation only. The contract is inherited, not re-opened.

-------------------------------------------------------------------------------
BUILD PROGRESS (6 pieces):
  [x] Piece 1: scaffolding — constants and paths
  [x] Piece 2: registry load + identity contract (reads local registry only)
  [x] Piece 3: HTTP fetch (the single bulk API call, retry, loud failure)
  [x] Piece 4: transform / normalize (the single normalization gatekeeper)
  [x] Piece 5: state decision + identity + exit codes + provenance + write
  [x] Piece 6: launchd scheduling (plist + wrapper + manual run)
Run with:  python3 04_market_state_loader.py --run        (real run; launchd uses this)
           python3 04_market_state_loader.py --selfcheck  (development self-checks)
-------------------------------------------------------------------------------
"""

import json
import time
import hashlib
import os
import sys
import uuid
from datetime import datetime, timezone
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

# ---------------------------------------------------------------------------
# Schema / version identity (feeds the Q5.3 provenance stamp later)
# ---------------------------------------------------------------------------

LOADER_SCHEMA_VERSION = "mode1-loader-v1"   # this loader's own output-schema version
EXPECTED_REGISTRY_VERSION = "v1"            # the registry version this loader is built for

# ---------------------------------------------------------------------------
# Paths — ABSOLUTE ONLY.
# launchd runs scripts from a read-only system directory; relative paths
# silently fail (documented repeat-offender trap, BRAIN.md Apr 5/6 rule).
# Every path below is anchored to the user's home directory explicitly.
# ---------------------------------------------------------------------------

HOME = Path.home()
REPO_ROOT = HOME / "Projects" / "latentforge-latentmas"

# Input: the locked 8-market registry the loader reads.
REGISTRY_PATH = REPO_ROOT / "experiments" / "benchmark" / "benchmark_registry_v1.json"

# Output: the loader's own dedicated room (Piece 1 decision).
OUTPUT_DIR = REPO_ROOT / "experiments" / "benchmark" / "mode1"

# ---------------------------------------------------------------------------
# HTTP identity
# A real User-Agent is REQUIRED. Without it the Gamma API returns 403 Forbidden
# (this was the false "endpoint is broken" premise the Q4 contract reversal fixed).
# ---------------------------------------------------------------------------

USER_AGENT = "LatentForge-mode1-loader/1.0"

GAMMA_MARKETS_ENDPOINT = "https://gamma-api.polymarket.com/markets"

# Q4 retry policy: 2 attempts on the single bulk call, waiting 10s then 30s
# before each retry, then ERROR. Lighter than polymarket-pull's 3x5min because
# this is one targeted call, not a full-surface pull.
RETRY_BACKOFF_SECONDS = [10, 30]   # len = number of retries after the first try
REQUEST_TIMEOUT_SECONDS = 30


# ---------------------------------------------------------------------------
# Piece 2: registry load + identity contract
#
# Reads the LOCAL registry file only. No network. This is where the loader
# learns "the right 8 markets" so that later (Piece 3+) it can verify the API
# handed back exactly those 8 and not a swapped/missing/extra market.
#
# Honors the contract:
#   - Q5.1 identity verification: returned conditionId set must EXACTLY match
#     the registry's 8. We build the expected set here.
#   - Q2 selection-snapshot carry-through: we keep each market's registry record
#     (slug, condition_id, question, selection_snapshot, etc.) so the loader can
#     carry the snapshot into its output later.
#   - "don't trust silently": if the registry isn't the version we expect, or
#     doesn't contain exactly 8 markets with unique condition_ids, we raise a
#     hard error instead of quietly working off the wrong list.
# ---------------------------------------------------------------------------


class RegistryError(Exception):
    """Raised when the registry is missing, malformed, wrong version, or
    fails the structural checks the loader requires before it will trust it."""


def load_registry(registry_path: Path = REGISTRY_PATH) -> dict:
    """Read and parse the registry JSON from local disk. Hard-fail if it is
    missing or not valid JSON — the loader will not proceed on a bad list."""
    if not registry_path.exists():
        raise RegistryError(f"Registry file not found: {registry_path}")
    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            registry = json.load(f)
    except json.JSONDecodeError as e:
        raise RegistryError(f"Registry file is not valid JSON: {e}")
    return registry


def validate_registry(registry: dict) -> None:
    """Structural checks the loader requires before trusting the registry.
    Each failure is a loud, specific error — never a silent shrug.

      1. version must match EXPECTED_REGISTRY_VERSION ('v1').
      2. 'markets' must be a list.
      3. there must be exactly 8 markets.
      4. every market must carry a non-empty condition_id.
      5. the 8 condition_ids must be unique (no duplicates / no accidental
         double-listing of the same market).
    """
    version = registry.get("version")
    if version != EXPECTED_REGISTRY_VERSION:
        raise RegistryError(
            f"Registry version mismatch: expected '{EXPECTED_REGISTRY_VERSION}', "
            f"got '{version}'. Loader is built for the v1 registry only."
        )

    markets = registry.get("markets")
    if not isinstance(markets, list):
        raise RegistryError("Registry 'markets' is missing or not a list.")

    if len(markets) != 8:
        raise RegistryError(
            f"Registry must contain exactly 8 markets; found {len(markets)}."
        )

    condition_ids = []
    for i, m in enumerate(markets):
        cid = m.get("condition_id")
        if not cid or not isinstance(cid, str):
            slug = m.get("slug", "<no slug>")
            raise RegistryError(
                f"Market #{i + 1} ('{slug}') has a missing or invalid condition_id."
            )
        condition_ids.append(cid)

    unique = set(condition_ids)
    if len(unique) != len(condition_ids):
        raise RegistryError(
            "Registry contains duplicate condition_ids; the 8 markets must be distinct."
        )


def get_expected_condition_ids(registry: dict) -> set:
    """The set of 8 condition_ids the API must return — the Q5.1 identity anchor.
    Returns a set for exact set-equality comparison later (Piece 3+)."""
    return {m["condition_id"] for m in registry["markets"]}


def get_registry_records_by_condition_id(registry: dict) -> dict:
    """Map condition_id -> full registry record for each market, so the loader
    can carry the selection_snapshot and durable identity (slug + condition_id)
    into its output later (Q2). Keyed by condition_id because that is the field
    the API is queried and matched on."""
    return {m["condition_id"]: m for m in registry["markets"]}


# ---------------------------------------------------------------------------
# Piece 3: HTTP fetch — the single bulk call
#
# Honors the contract (Q4):
#   - urllib + explicit User-Agent (without the UA the API returns 403).
#   - ONE bulk call to /markets?condition_ids=... for all 8 markets.
#   - NO per-slug fallback. All-or-nothing is intended: a complete time-aligned
#     record, or a clean labeled gap (ERROR). We do not build a second ingestion
#     path (that would be fallback-shaped behavior — the exact thing [L-1] forbids).
#   - 2-attempt retry (waits 10s, then 30s) on the single bulk call, then ERROR.
#
# This function does ONE job: get the raw bytes back, or fail loudly. It does
# NOT parse market fields, judge liveness, or check identity — those are later
# pieces. Keeping fetch separate from interpret is the locked architecture.
# ---------------------------------------------------------------------------


class FetchError(Exception):
    """Raised when the bulk API call cannot be completed cleanly after all
    retries. This maps to the loader's ERROR state (exit code 2): transient,
    safe to retry, registry NOT invalidated."""


def build_bulk_url(condition_ids, closed: bool = False) -> str:
    """Construct the bulk endpoint URL: one condition_ids parameter per market.
    Order follows the registry; the API returns markets in its own order, so
    downstream code matches by condition_id, never by position."""
    params = [("condition_ids", cid) for cid in condition_ids]
    if closed:
        params.append(("closed", "true"))
    return GAMMA_MARKETS_ENDPOINT + "?" + urllib.parse.urlencode(params)


def fetch_markets_raw(condition_ids, closed: bool = False):
    """Make ONE bulk call (live-only by default; closed-only if closed=True)
    and return (raw_bytes, parsed_json).

    Returns both:
      - raw_bytes: the exact response body, used later for the api_response_sha256
        provenance fingerprint (Q5.3) — fingerprint the bytes that actually arrived.
      - parsed_json: the JSON-decoded body, for downstream transform.

    Retries per RETRY_BACKOFF_SECONDS. Any failure that survives all retries —
    HTTP error (incl. 403), network error, timeout, or a body that is not valid
    JSON — raises FetchError. No silent fallback, no partial-data path.
    """
    url = build_bulk_url(condition_ids, closed=closed)
    headers = {"User-Agent": USER_AGENT}

    attempts = 1 + len(RETRY_BACKOFF_SECONDS)   # first try + retries
    last_error = None

    for attempt_index in range(attempts):
        if attempt_index > 0:
            wait = RETRY_BACKOFF_SECONDS[attempt_index - 1]
            print(f"  [fetch] retry {attempt_index}/{len(RETRY_BACKOFF_SECONDS)} "
                  f"after {wait}s (previous error: {last_error})")
            time.sleep(wait)

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as resp:
                status = resp.status
                raw_bytes = resp.read()
            if status != 200:
                last_error = f"HTTP status {status}"
                continue
            try:
                parsed = json.loads(raw_bytes.decode("utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                last_error = f"response body was not valid JSON: {e}"
                continue
            if not isinstance(parsed, list):
                last_error = (f"expected a JSON list of markets, "
                              f"got {type(parsed).__name__}")
                continue
            # Success: clean 200 with a JSON list body.
            return raw_bytes, parsed

        except urllib.error.HTTPError as e:
            last_error = f"HTTPError {e.code}"
        except urllib.error.URLError as e:
            last_error = f"URLError {e.reason}"
        except (TimeoutError, OSError) as e:
            last_error = f"{type(e).__name__}: {e}"

    raise FetchError(
        f"Bulk market fetch failed after {attempts} attempt(s). "
        f"Last error: {last_error}"
    )


def fetch_all_markets(condition_ids):
    """Two-pass bulk fetch — 2026-07-11 fix.

    The Gamma /markets endpoint silently applies closed=false by default,
    EVEN when querying by explicit condition_ids, and closed=true is an
    EXCLUSIVE filter (returns only closed markets). Verified live 2026-07-11.
    There is no single-call way to retrieve the full registry once any
    market has resolved.

    Pass 1: bare query  -> live markets only.
    Pass 2: closed=true -> closed markets only.
    Merge by conditionId. A cid appearing in BOTH responses violates the
    observed partition and hard-fails (FetchError) — 'should be impossible'
    is what guards are for.

    Returns (raw_bytes_live, raw_bytes_closed, merged_parsed_list).
    """
    raw_live, parsed_live = fetch_markets_raw(condition_ids, closed=False)
    raw_closed, parsed_closed = fetch_markets_raw(condition_ids, closed=True)

    seen = set()
    for m in parsed_live + parsed_closed:
        cid = m.get("conditionId")
        if cid in seen:
            raise FetchError(
                f"conditionId {cid} returned by BOTH the live and closed "
                f"queries — partition assumption violated; refusing to merge.")
        seen.add(cid)
    return raw_live, raw_closed, parsed_live + parsed_closed


# ---------------------------------------------------------------------------
# Piece 4: transform / normalize — the single normalization gatekeeper
#
# Honors the contract (Q2). The loader is the ONE place where Polymarket's
# ambiguity is converted into deterministic Mode 1 semantics. Per LIVE market:
#   - durable identity: slug + condition_id
#   - parsed prices: outcomePrices decoded from its JSON-STRING form into floats,
#     HARD-FAIL if parse fails, yields ["0","0"] on an open market, or is not
#     EXACTLY 2 outcomes (the "exactly 2" check absorbs the binary-mutation concern)
#   - normalized numerics: liquidity + total volume from the *Num typed fields only
#     (string twins discarded). 24h volume is NOT recorded in v1 — see the
#     2026-06-28 volume-field-gap note: volume24hrNum does not exist, and
#     volume24hr is absent even on healthy markets; depending on it would
#     hard-fail good markets on quiet days.
#   - recorded-but-not-trusted: endDate (and active) — stored, never used to
#     judge liveness/resolution
#   - two timestamps: loader_run_at + API updatedAt
#   - selection snapshot: carried through from the registry
# NO computed mid-price / no interpretation. The loader reports what IS.
#
# This function transforms ONE market that has already been confirmed LIVE.
# Liveness judgment and identity matching are Piece 5, not here. A hard-fail
# here is a per-market data problem; Piece 5 decides what that means for the run.
# ---------------------------------------------------------------------------


class TransformError(Exception):
    """Raised when a live market's data cannot be normalized into clean Mode 1
    semantics (e.g. unparseable prices, wrong outcome count). A data-shape
    failure, surfaced loudly rather than papered over with a fallback."""


def parse_price_string(outcome_prices_raw, condition_id: str):
    """Decode outcomePrices from its JSON-string form into a list of floats.

    Polymarket returns outcomePrices as a JSON-ENCODED STRING, e.g. the literal
    text  '["0.185", "0.815"]'  — NOT a list. This is the [E-4] trap and the
    same shape behind the April 20 _extract_price silent-0.5 bug.

    Hard-fail (TransformError) if:
      - the value is missing,
      - it is not a string that JSON-decodes to a list,
      - any element is not a finite number,
      - there are not EXACTLY 2 outcomes,
      - the parsed prices are [0, 0] (an open market cannot have both sides 0).
    Returns: list of 2 floats [yes_price, no_price].
    """
    if outcome_prices_raw is None:
        raise TransformError(
            f"{condition_id}: outcomePrices is missing")

    if not isinstance(outcome_prices_raw, str):
        raise TransformError(
            f"{condition_id}: outcomePrices is {type(outcome_prices_raw).__name__}, "
            f"expected a JSON-encoded string")

    try:
        decoded = json.loads(outcome_prices_raw)
    except json.JSONDecodeError as e:
        raise TransformError(
            f"{condition_id}: outcomePrices string did not JSON-decode: {e}")

    if not isinstance(decoded, list):
        raise TransformError(
            f"{condition_id}: outcomePrices decoded to "
            f"{type(decoded).__name__}, expected a list")

    if len(decoded) != 2:
        raise TransformError(
            f"{condition_id}: outcomePrices has {len(decoded)} outcomes, "
            f"expected exactly 2 (binary market)")

    prices = []
    for elem in decoded:
        try:
            val = float(elem)
        except (TypeError, ValueError):
            raise TransformError(
                f"{condition_id}: outcomePrices element {elem!r} is not a number")
        # reject NaN / inf
        if val != val or val in (float("inf"), float("-inf")):
            raise TransformError(
                f"{condition_id}: outcomePrices element {elem!r} is not finite")
        # reject out-of-range: a probability must be in [0, 1] (Item 4)
        if val < 0.0 or val > 1.0:
            raise TransformError(
                f"{condition_id}: outcomePrices element {elem!r} is outside [0, 1] "
                f"(a probability must be between 0 and 1)")
        prices.append(val)

    if prices[0] == 0.0 and prices[1] == 0.0:
        raise TransformError(
            f"{condition_id}: outcomePrices is [0, 0] on a live market "
            f"(invalid — an open market cannot have both sides at zero)")

    return prices


def require_num_field(market: dict, field: str, condition_id: str) -> float:
    """Read a typed numeric *Num field, hard-failing if it is absent or not a
    number. Used for liquidityNum and volumeNum, which the June 28 probe
    confirmed present on all 8 markets. (24h volume is deliberately NOT read
    here — see the volume-field-gap note.)"""
    if field not in market:
        raise TransformError(
            f"{condition_id}: required numeric field '{field}' is missing")
    val = market[field]
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        raise TransformError(
            f"{condition_id}: field '{field}' is {type(val).__name__}, "
            f"expected a number")
    return float(val)


def assert_yes_first(market: dict, condition_id: str) -> None:
    """Item 1 strict-assert: position 0 of the price array must be the YES side.
    The loader maps yes_price = prices[0]; it never reads the label array. If
    Polymarket ever returns outcomes in the other order, every probability would
    invert while passing identity/price-sum/state checks clean — the silent-
    semantic-corruption shape the hard-fail architecture exists to prevent.

    Founder-locked: STRICT-ASSERT, not label-remap. If order ever flips, STOP
    loudly and look. Built defensively; outcomes arrives JSON-string-encoded
    (confirmed June 28, same [E-4] shape as outcomePrices), so decode first.
      - outcomes missing / not a list / not exactly 2 -> TransformError
      - outcomes[0] (case-insensitive) != "yes"        -> TransformError
    """
    outcomes = market.get("outcomes")
    if isinstance(outcomes, str):
        try:
            outcomes = json.loads(outcomes)
        except json.JSONDecodeError as e:
            raise TransformError(
                f"{condition_id}: outcomes string did not JSON-decode: {e}")
    if not isinstance(outcomes, list):
        raise TransformError(
            f"{condition_id}: outcomes is {type(outcomes).__name__}, expected a list")
    if len(outcomes) != 2:
        raise TransformError(
            f"{condition_id}: outcomes has {len(outcomes)} entries, expected exactly 2")
    first = outcomes[0]
    if not isinstance(first, str) or first.strip().lower() != "yes":
        raise TransformError(
            f"{condition_id}: outcomes[0] is {first!r}, expected 'Yes' "
            f"(price-array order assumption violated — STOP and inspect)")


def transform_live_market(market: dict, registry_record: dict, loader_run_at: str) -> dict:
    """Normalize ONE confirmed-live market into the deterministic Mode 1 record.

    `market` is the raw API object; `registry_record` is this market's entry
    from the registry (for snapshot carry-through and durable identity);
    `loader_run_at` is the loader's check-time stamp (ISO 8601).

    Raises TransformError on any data-shape problem.
    """
    condition_id = market.get("conditionId")
    if not condition_id:
        raise TransformError("API market object is missing conditionId")

    assert_yes_first(market, condition_id)   # Item 1: order assumption guard
    prices = parse_price_string(market.get("outcomePrices"), condition_id)
    liquidity = require_num_field(market, "liquidityNum", condition_id)
    volume_total = require_num_field(market, "volumeNum", condition_id)

    # Price-sum sanity NOTE (Option 2: surface, don't block, don't interpret).
    # A healthy binary market's two prices sum to ~1.0. If they don't, we record
    # a plain flag — we do NOT alter the prices, compute a "true" value, or change
    # the market's state. This surfaces a fact the same way end_date is recorded;
    # it is not interpretation.
    # Item 2: 24h volume — KEEP THE FIELD, write explicit null when absent.
    # Read one field only (founder decision B): volume24hrNum if present-and-
    # numeric, else None. NOT via require_num_field (absence is normal here and
    # must not alarm). Visibility without silent interpretation.
    vol_24h_raw = market.get("volume24hrNum")
    if isinstance(vol_24h_raw, bool) or not isinstance(vol_24h_raw, (int, float)):
        volume_24h = None
    else:
        volume_24h = float(vol_24h_raw)

    price_sum = prices[0] + prices[1]
    price_sum_ok = abs(price_sum - 1.0) <= 0.02   # within 2 cents of 1.0

    return {
        # durable identity (from registry — the trusted source of identity)
        "slug": registry_record.get("slug"),
        "condition_id": condition_id,
        "registry_index": registry_record.get("registry_index"),
        "question": registry_record.get("question"),

        # parsed prices (the contract's hard-fail-guarded core)
        "yes_price": prices[0],
        "no_price": prices[1],
        # price-sum sanity NOTE (surfaced fact, not a block; Option 2)
        "price_sum": price_sum,
        "price_sum_ok": price_sum_ok,

        # normalized numerics (typed *Num fields only; 24h volume omitted in v1)
        "liquidity_num": liquidity,
        "volume_num": volume_total,
        "volume_24h_num": volume_24h,   # Item 2: explicit null when API omits it

        # recorded-but-NOT-trusted (never used to judge liveness/resolution)
        "end_date_untrusted": market.get("endDate"),
        "active_untrusted": market.get("active"),

        # two timestamps: loader check-time + API last-change time
        "loader_run_at": loader_run_at,
        "api_updated_at": market.get("updatedAt"),

        # selection snapshot carried through from the registry (Q2)
        "selection_snapshot": registry_record.get("selection_snapshot"),
    }


# ---------------------------------------------------------------------------
# Piece 5: state decision + identity + exit codes + provenance + write
#
# Honors the contract:
#   Q1 — three action states. Liveness test is closed==False AND
#        acceptingOrders==True ONLY. endDate/active excluded. A non-live market
#        is RETIRED with a cause-of-death sub-field (closed vs missing).
#   Q5.1 — identity: returned conditionId set must EXACTLY match the registry's 8.
#          Any mismatch/wrong-count is a hard-fail, not a shrug.
#   Q5.2 — tiered exit codes: 0 all LIVE/validated/fresh; 1 one+ RETIRED
#          (founder v2 decision); 2 ERROR (transient, safe to retry).
#   Q5.3 — provenance stamp: loader_run_id, api_response_sha256, registry_version,
#          loader_schema_version on every output.
#   Q3 — loud failure: on any non-clean run, write the error, do NOT update the
#        production state file, exit non-zero. Clean runs write atomically.
#
# Exit code constants (Q5.2):
EXIT_ALL_LIVE = 0
EXIT_RETIRED = 1
EXIT_ERROR = 2
# ---------------------------------------------------------------------------


def utc_now_iso() -> str:
    """Loader check-time stamp, ISO 8601 UTC."""
    return datetime.now(timezone.utc).isoformat()


def is_live(market: dict) -> bool:
    """Q1 liveness test — the ONLY liveness signal the contract permits:
    closed == False AND acceptingOrders == True. endDate and active are
    explicitly NOT consulted (the Fed Dec trap: past endDate on a live market)."""
    return market.get("closed") is False and market.get("acceptingOrders") is True


def check_identity(parsed_markets, expected_condition_ids):
    """Q5.1 identity verification. Returns (ok, detail).
    The set of conditionIds the API returned must EXACTLY equal the registry's 8:
    same members, no missing, no extra, no swap. Any deviation is a hard-fail."""
    returned = set()
    for m in parsed_markets:
        cid = m.get("conditionId")
        if cid:
            returned.add(cid)

    missing = expected_condition_ids - returned       # registry ids the API didn't return
    unexpected = returned - expected_condition_ids     # ids the API returned that we didn't ask for

    if missing or unexpected or len(returned) != len(expected_condition_ids):
        detail = {
            "returned_count": len(returned),
            "expected_count": len(expected_condition_ids),
            "missing_from_response": sorted(missing),
            "unexpected_in_response": sorted(unexpected),
        }
        return False, detail
    return True, {"returned_count": len(returned),
                  "expected_count": len(expected_condition_ids)}


def decide_market_state(api_market, registry_record, loader_run_at):
    """Decide ONE market's state and build its record.
    Returns (state, record) where state is 'LIVE' or 'RETIRED'.
    - LIVE  -> record is the full normalized transform (Piece 4).
    - RETIRED -> record carries cause-of-death ('closed' vs 'missing') as data.
    A transform hard-fail on a LIVE market is re-raised: it is a genuine
    data-shape failure that the run-level handler treats as a problem, not a
    silently-dropped market.
    """
    if api_market is None:
        # Market was in the registry but NOT returned by the API at all.
        return "RETIRED", {
            "slug": registry_record.get("slug"),
            "condition_id": registry_record.get("condition_id"),
            "registry_index": registry_record.get("registry_index"),
            "question": registry_record.get("question"),
            "state": "RETIRED",
            "cause_of_death": "missing",   # not returned by the API
            "selection_snapshot": registry_record.get("selection_snapshot"),
            "loader_run_at": loader_run_at,
        }

    if is_live(api_market):
        record = transform_live_market(api_market, registry_record, loader_run_at)
        record["state"] = "LIVE"
        return "LIVE", record

    # Returned by the API but not live -> RETIRED, cause = closed.
    return "RETIRED", {
        "slug": registry_record.get("slug"),
        "condition_id": registry_record.get("condition_id"),
        "registry_index": registry_record.get("registry_index"),
        "question": registry_record.get("question"),
        "state": "RETIRED",
        "cause_of_death": "closed",   # returned, but closed/not accepting orders
        "closed_raw": api_market.get("closed"),
        "accepting_orders_raw": api_market.get("acceptingOrders"),
        "selection_snapshot": registry_record.get("selection_snapshot"),
        "loader_run_at": loader_run_at,
    }


def build_provenance(raw_bytes_live, raw_bytes_closed, registry):
    """Q5.3 provenance stamp. Fingerprints the EXACT bytes that arrived —
    one hash per pass of the two-pass fetch (2026-07-11 schema amendment)."""
    return {
        "loader_run_id": str(uuid.uuid4()),
        "api_response_sha256_live": hashlib.sha256(raw_bytes_live).hexdigest(),
        "api_response_sha256_closed": hashlib.sha256(raw_bytes_closed).hexdigest(),
        "registry_version": registry.get("version"),
        "loader_schema_version": LOADER_SCHEMA_VERSION,
    }


def assemble_run(parsed_markets, raw_bytes_live, raw_bytes_closed, registry, loader_run_at):
    """Build the full run result from a fetched+identity-checked response.
    Returns (exit_code, output_dict). Assumes identity has ALREADY passed
    (caller enforces Q5.1 before calling this). Per-market transform hard-fails
    bubble up as TransformError to the caller, which treats them as ERROR.
    """
    records_by_cid = get_registry_records_by_condition_id(registry)
    api_by_cid = {m.get("conditionId"): m for m in parsed_markets if m.get("conditionId")}

    market_records = []
    n_live = 0
    n_retired = 0
    for cid, reg_record in records_by_cid.items():
        api_market = api_by_cid.get(cid)   # None if registry market absent from response
        state, record = decide_market_state(api_market, reg_record, loader_run_at)
        if state == "LIVE":
            n_live += 1
        else:
            n_retired += 1
        market_records.append(record)

    # sort output by registry_index for stable, human-scannable order
    market_records.sort(key=lambda r: (r.get("registry_index") is None,
                                       r.get("registry_index")))

    exit_code = EXIT_ALL_LIVE if n_retired == 0 else EXIT_RETIRED
    run_state = "ALL_LIVE" if n_retired == 0 else "RETIRED_PRESENT"

    output = {
        "run_state": run_state,
        "loader_run_at": loader_run_at,
        "counts": {"live": n_live, "retired": n_retired,
                   "total": len(market_records)},
        "provenance": build_provenance(raw_bytes_live, raw_bytes_closed, registry),
        "markets": market_records,
    }
    return exit_code, output


def write_output_atomic(output_dir: Path, output: dict) -> Path:
    """Q3 clean-run write. Writes the daily snapshot atomically: write to a temp
    file in the same dir, then os.replace() into place, so a consumer never sees
    a half-written file. Creates the output dir if missing. Filename is
    market_state_YYYY-MM-DD.json (one daily snapshot, one file)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    date_str = output["loader_run_at"][:10]   # YYYY-MM-DD from the ISO stamp
    final_path = output_dir / f"market_state_{date_str}.json"
    tmp_path = output_dir / f".market_state_{date_str}.json.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, final_path)   # atomic on POSIX

    # Item 3: stable shortcut always pointing at today's dated file, created
    # atomically (symlink to temp name, then os.replace into place) so a reader
    # never catches it dangling. Dated files untouched. Clean-run-only — the
    # ERROR path never calls this, so the last good shortcut survives a failure.
    shortcut_path = output_dir / "market_state_current.json"
    tmp_link = output_dir / ".market_state_current.json.tmp"
    if tmp_link.exists() or tmp_link.is_symlink():
        tmp_link.unlink()
    os.symlink(final_path.name, tmp_link)   # relative target: just the filename
    os.replace(tmp_link, shortcut_path)     # atomic swap into final name

    return final_path


def write_error_sidecar(output_dir: Path, error_payload: dict) -> Path:
    """Q3 loud failure. On any non-clean run we do NOT touch the production
    state file. Instead we write an error sidecar the morning digest can read,
    so the failure is visible and the last good state file is preserved."""
    output_dir.mkdir(parents=True, exist_ok=True)
    date_str = error_payload.get("loader_run_at", utc_now_iso())[:10]
    err_path = output_dir / f"market_state_ERROR_{date_str}.json"
    with open(err_path, "w", encoding="utf-8") as f:
        json.dump(error_payload, f, indent=2, ensure_ascii=False)
    return err_path


def run_loader(registry_path: Path = REGISTRY_PATH,
               output_dir: Path = OUTPUT_DIR) -> int:
    """Top-level orchestration. Returns an exit code (0/1/2) per Q5.2.

    Flow:
      1. load + validate registry            (RegistryError -> ERROR/2)
      2. fetch bulk                            (FetchError    -> ERROR/2)
      3. identity check (Q5.1)                 (mismatch      -> ERROR/2)
      4. assemble run (states, provenance)     (TransformError-> ERROR/2)
      5. clean run -> atomic write, exit 0 or 1
         non-clean -> error sidecar, no production write, exit 2
    """
    loader_run_at = utc_now_iso()

    # Step 1: registry
    try:
        registry = load_registry(registry_path)
        validate_registry(registry)
    except RegistryError as e:
        payload = {"run_state": "ERROR", "error_kind": "registry",
                   "error": str(e), "loader_run_at": loader_run_at}
        write_error_sidecar(output_dir, payload)
        print(f"ERROR (registry): {e}")
        return EXIT_ERROR

    expected = get_expected_condition_ids(registry)
    condition_ids = [m["condition_id"] for m in registry["markets"]]

    # Step 2: fetch (two-pass: live + closed — see fetch_all_markets)
    try:
        raw_bytes_live, raw_bytes_closed, parsed = fetch_all_markets(condition_ids)
    except FetchError as e:
        payload = {"run_state": "ERROR", "error_kind": "fetch",
                   "error": str(e), "loader_run_at": loader_run_at}
        write_error_sidecar(output_dir, payload)
        print(f"ERROR (fetch): {e}")
        return EXIT_ERROR

    # Step 3: identity (Q5.1)
    ok, detail = check_identity(parsed, expected)
    if not ok:
        payload = {"run_state": "ERROR", "error_kind": "identity",
                   "error": "returned conditionId set does not match registry",
                   "detail": detail, "loader_run_at": loader_run_at}
        write_error_sidecar(output_dir, payload)
        print(f"ERROR (identity): conditionId set mismatch: {detail}")
        return EXIT_ERROR

    # Step 4: assemble
    try:
        exit_code, output = assemble_run(parsed, raw_bytes_live, raw_bytes_closed, registry, loader_run_at)
    except TransformError as e:
        payload = {"run_state": "ERROR", "error_kind": "transform",
                   "error": str(e), "loader_run_at": loader_run_at}
        write_error_sidecar(output_dir, payload)
        print(f"ERROR (transform): {e}")
        return EXIT_ERROR

    # Step 5: clean run -> write production file
    final_path = write_output_atomic(output_dir, output)
    c = output["counts"]
    print(f"{output['run_state']}: live={c['live']} retired={c['retired']} "
          f"-> wrote {final_path} (exit {exit_code})")
    return exit_code


# ---------------------------------------------------------------------------
# Piece 1 self-check: prove the constants load. Does NOT touch the network,
# the registry, or any output file. Safe to run.
# ---------------------------------------------------------------------------

def _piece1_selfcheck():
    print("Mode 1 loader — Piece 1 scaffolding self-check")
    print(f"  loader schema version    : {LOADER_SCHEMA_VERSION}")
    print(f"  expected registry version: {EXPECTED_REGISTRY_VERSION}")
    print(f"  registry path            : {REGISTRY_PATH}")
    print(f"  output dir               : {OUTPUT_DIR}")
    print(f"  user agent               : {USER_AGENT}")
    print(f"  endpoint                 : {GAMMA_MARKETS_ENDPOINT}")
    print(f"  registry file exists?    : {REGISTRY_PATH.exists()}")
    print(f"  output dir exists?       : {OUTPUT_DIR.exists()}")


# ---------------------------------------------------------------------------
# Piece 2 self-check: read the local registry, run the structural checks,
# and print what was found. NO network. Reads only the local registry file.
# ---------------------------------------------------------------------------

def _piece2_selfcheck():
    print("Mode 1 loader — Piece 2 registry/identity self-check")
    try:
        registry = load_registry()
    except RegistryError as e:
        print(f"  REGISTRY LOAD FAILED: {e}")
        print("  (On your Mac the registry exists; in this scratch test it does not.)")
        return

    try:
        validate_registry(registry)
        print("  structural checks       : PASSED")
    except RegistryError as e:
        print(f"  structural checks       : FAILED — {e}")
        return

    expected = get_expected_condition_ids(registry)
    records = get_registry_records_by_condition_id(registry)
    print(f"  registry version        : {registry.get('version')}")
    print(f"  market count            : {len(registry.get('markets', []))}")
    print(f"  unique condition_ids    : {len(expected)}")
    print("  markets read:")
    for m in registry["markets"]:
        snap = m.get("selection_snapshot", {})
        print(
            f"    [{m.get('registry_index')}] {m.get('slug')}"
            f"  (cid {m.get('condition_id')[:10]}…, "
            f"sel_yes={snap.get('yes_price')})"
        )


def _piece3_selfcheck():
    print("Mode 1 loader — Piece 3 fetch self-check (THIS MAKES A REAL NETWORK CALL)")
    try:
        registry = load_registry()
        validate_registry(registry)
    except RegistryError as e:
        print(f"  cannot test fetch — registry problem: {e}")
        return

    condition_ids = [m["condition_id"] for m in registry["markets"]]
    print(f"  attempting bulk call for {len(condition_ids)} markets…")
    try:
        raw_live, raw_closed, parsed = fetch_all_markets(condition_ids)
        print(f"  FETCH OK — {len(raw_live)} live-query bytes + "
              f"{len(raw_closed)} closed-query bytes, "
              f"{len(parsed)} markets in merged response")
    except FetchError as e:
        print(f"  FETCH FAILED (loud, as designed) — would become ERROR/exit 2:")
        print(f"    {e}")


def _run_selfchecks():
    _piece1_selfcheck()
    print()
    _piece2_selfcheck()
    print()
    _piece3_selfcheck()


if __name__ == "__main__":
    # Two modes:
    #   --run        : the REAL loader. Fetches, decides, writes, exits 0/1/2.
    #                  This is what launchd calls (Piece 6) and what a manual
    #                  founder run uses. Exit code is the contract's Q5.2 signal.
    #   --selfcheck  : the piece-by-piece demos (used during development).
    #   (no args)    : prints usage and exits 0, so an accidental bare run does
    #                  nothing destructive.
    arg = sys.argv[1] if len(sys.argv) > 1 else ""

    if arg == "--run":
        exit_code = run_loader()
        sys.exit(exit_code)
    elif arg == "--selfcheck":
        _run_selfchecks()
        sys.exit(0)
    else:
        print("Usage:")
        print("  python3 04_market_state_loader.py --run        # real run (launchd uses this)")
        print("  python3 04_market_state_loader.py --selfcheck  # development self-checks")
        sys.exit(0)
