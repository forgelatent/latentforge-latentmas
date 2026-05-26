#!/usr/bin/env python3
"""
Full-surface Polymarket pull + filter — May 26, 2026.

Replaces the broken daily pull (93 markets) by querying the Gamma API
directly until exhaustion. Applies the five locked criteria from the
May 25 Step 7 synthesis. Saves the qualifying pool to JSON.

Locked criteria:
  1. Resolution cadence: 14-90 days from today
  2. Crowd uncertainty: 15-80% on YES
  3. Binary outcome
  4. Exclude sports / esports / microcontracts
  5. Active, not closed, not archived
"""

import json
import sys
import urllib.request
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://gamma-api.polymarket.com/markets"
PAGE_SIZE = 100
OUTPUT_FILE = Path.home() / "Projects/latentforge-latentmas/scratch/qualifying_pool_2026-05-26.json"

TODAY = datetime(2026, 5, 26, tzinfo=timezone.utc)
MIN_DAYS = 14
MAX_DAYS = 90
MIN_PROB = 0.15
MAX_PROB = 0.80

# Aggressive sports/esports/microcontract filter
SPORTS_KEYWORDS = [
    # Major US leagues
    "nba", "nhl", "mlb", "nfl", "ncaa", "wnba", "ncaaf", "ncaab",
    # Soccer
    "epl", "uefa", "champions league", "premier league", "la liga",
    "serie a", "bundesliga", "mls", "world-cup", "world cup", "fifa", "fifwc",
    # Other sports
    "f1", "formula 1", "nascar", "ufc", "mma", "boxing",
    "tennis", "atp", "wta", "golf", "pga", "lpga",
    "cricket", "rugby", "ruprem", "rutopft", "ruabl",
    # Esports
    "dota", "dota2", "cs2", "csgo", "counter-strike", "valorant",
    "lol", "league-of-legends", "starcraft", "esports",
    # Generic sports terms
    "tournament", "playoff", "championship", "stanley cup", "super bowl",
    "world series", "finals", "olympics", "olympic",
    # Team-name patterns that show up in slugs
    "hurricanes", "avalanche", "knights", "canadiens", "thunder", "knicks",
    "spurs", "yankees", "lakers", "warriors", "celtics", "fiorentina",
    # Score/match patterns
    "kills", "odd/even", "over/under", "spread", "moneyline",
    # Spanish/European league slug prefixes
    "es2-", "es1-",
    # Microcontract crypto/price patterns
    "updown-5m", "up-or-down-on-", "intraday",
]

DOMAIN_KEYWORDS = {
    "macro": ["fed", "fomc", "cpi", "inflation", "unemployment", "gdp", "rate cut",
              "rate hike", "recession", "s&p", "spx", "treasury", "yield", "powell",
              "jobs report", "bls", "pce", "nfp"],
    "policy": ["ban", "law", "bill", "executive order", "regulation", "tariff",
               "shutdown", "senate", "house pass", "congress", "supreme court",
               "ruling", "scotus"],
    "geopolitics": ["iran", "russia", "ukraine", "china", "taiwan", "israel",
                    "gaza", "nato", "sanctions", "ceasefire", "north korea",
                    "election", "primary", "governor", "midterm", "president"],
    "ai-tech": ["openai", "anthropic", "claude", "gpt", "llama", "deepmind",
                "agi", "nvidia", "google", "microsoft", "meta", "tesla",
                "spacex", "z.ai", "xai", "apple", "amazon"],
    "crypto": ["bitcoin", "btc", "ethereum", "eth", "solana", "xrp",
               "crypto", "coinbase"],
}


def fetch_page(offset):
    params = {
        "active": "true",
        "closed": "false",
        "limit": str(PAGE_SIZE),
        "offset": str(offset),
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "latentforge-fullpull/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_all_markets():
    all_markets = []
    seen_ids = set()
    page = 0
    while True:
        offset = page * PAGE_SIZE
        try:
            markets = fetch_page(offset)
        except Exception as e:
            print(f"Page {page} failed: {e}. Stopping.")
            break
        if not markets:
            print(f"Page {page}: empty, stopping.")
            break
        new = []
        for m in markets:
            cid = m.get("conditionId") or m.get("id") or m.get("slug")
            if cid and cid not in seen_ids:
                seen_ids.add(cid)
                new.append(m)
        all_markets.extend(new)
        if page % 10 == 0:
            print(f"  page {page}: total {len(all_markets)}")
        if len(markets) < PAGE_SIZE:
            print(f"Page {page}: short page, end of results.")
            break
        page += 1
    return all_markets


def parse_end_date(market):
    for key in ("endDate", "end_date", "endDateIso", "resolutionDate"):
        if key in market and market[key]:
            raw = market[key]
            try:
                if raw.endswith("Z"):
                    raw = raw[:-1] + "+00:00"
                dt = datetime.fromisoformat(raw)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt
            except (ValueError, AttributeError):
                continue
    return None


def parse_yes_price(market):
    raw = market.get("outcomePrices")
    if raw is None:
        return None
    try:
        if isinstance(raw, str):
            prices = json.loads(raw)
        elif isinstance(raw, list):
            prices = raw
        else:
            return None
        if not prices:
            return None
        return float(prices[0])
    except (json.JSONDecodeError, ValueError, TypeError):
        return None


def is_sports(market):
    blob = " ".join([
        str(market.get("question", "")),
        str(market.get("slug", "")),
        str(market.get("category", "")),
        str(market.get("groupItemTitle", "")),
    ]).lower()
    return any(kw in blob for kw in SPORTS_KEYWORDS)


def tag_domain(market):
    blob = " ".join([
        str(market.get("question", "")),
        str(market.get("slug", "")),
    ]).lower()
    tags = []
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in blob for kw in keywords):
            tags.append(domain)
    return tags if tags else ["other"]


def get_volume(market):
    for key in ("volume", "volumeNum", "volume24hr"):
        if key in market and market[key] is not None:
            try:
                return float(market[key])
            except (ValueError, TypeError):
                continue
    return None


def get_liquidity(market):
    for key in ("liquidity", "liquidityNum"):
        if key in market and market[key] is not None:
            try:
                return float(market[key])
            except (ValueError, TypeError):
                continue
    return None
def filter_markets(markets):
    survivors = []
    rejects = Counter()
    for m in markets:
        if m.get("closed") or m.get("archived") or m.get("active") is False:
            rejects["inactive"] += 1
            continue
        if is_sports(m):
            rejects["sports"] += 1
            continue
        end = parse_end_date(m)
        if end is None:
            rejects["no_end_date"] += 1
            continue
        days = (end - TODAY).days
        if days < MIN_DAYS:
            rejects["too_soon"] += 1
            continue
        if days > MAX_DAYS:
            rejects["too_late"] += 1
            continue
        yes_price = parse_yes_price(m)
        if yes_price is None:
            rejects["no_price"] += 1
            continue
        if yes_price < MIN_PROB or yes_price > MAX_PROB:
            rejects["near_certain"] += 1
            continue
        outcomes = m.get("outcomes")
        if isinstance(outcomes, str):
            try:
                outcomes = json.loads(outcomes)
            except json.JSONDecodeError:
                outcomes = None
        if isinstance(outcomes, list) and len(outcomes) != 2:
            rejects["non_binary"] += 1
            continue
        survivors.append({
            "question": m.get("question"),
            "slug": m.get("slug"),
            "conditionId": m.get("conditionId"),
            "yes_price": yes_price,
            "days_to_resolution": days,
            "end_date": end.strftime("%Y-%m-%d"),
            "tags": tag_domain(m),
            "volume": get_volume(m),
            "liquidity": get_liquidity(m),
            "category": m.get("category"),
        })
    return survivors, rejects


def main():
    print("Fetching all active Polymarket markets...")
    all_markets = fetch_all_markets()
    print(f"\nTotal markets fetched: {len(all_markets)}\n")

    print("Applying filters...")
    survivors, rejects = filter_markets(all_markets)

    print()
    print("=" * 70)
    print(f"QUALIFYING POOL: {len(survivors)} markets")
    print("=" * 70)
    print(f"Total markets considered: {len(all_markets)}")
    print()
    print("Rejection breakdown (first failure wins):")
    for reason, count in rejects.most_common():
        print(f"  {reason:20s}  {count}")
    print()

    by_domain = {}
    for s in survivors:
        primary = s["tags"][0]
        by_domain.setdefault(primary, []).append(s)

    print("Domain breakdown:")
    for domain in ["macro", "policy", "geopolitics", "ai-tech", "crypto", "other"]:
        if domain in by_domain:
            print(f"  {domain:15s}  {len(by_domain[domain])}")
    print()

    # Sort each domain by liquidity descending (highest-quality first)
    def liq_key(s):
        return s["liquidity"] if s["liquidity"] is not None else -1

    for domain in ["macro", "policy", "geopolitics", "ai-tech", "crypto", "other"]:
        if domain not in by_domain:
            continue
        print("=" * 70)
        print(f"{domain.upper()} ({len(by_domain[domain])})")
        print("=" * 70)
        sorted_markets = sorted(by_domain[domain], key=liq_key, reverse=True)
        for s in sorted_markets:
            vol = s["volume"]
            liq = s["liquidity"]
            vol_str = f"${vol:,.0f}" if vol is not None else "?"
            liq_str = f"${liq:,.0f}" if liq is not None else "?"
            yes_pct = int(s["yes_price"] * 100)
            tags = ", ".join(s["tags"])
            print(f"\n  Q: {s['question']}")
            print(f"     slug:        {s['slug']}")
            print(f"     conditionId: {s['conditionId']}")
            print(f"     YES: {yes_pct}%  resolves: {s['end_date']} ({s['days_to_resolution']}d)")
            print(f"     vol: {vol_str}  liq: {liq_str}")
            print(f"     tags: {tags}")
        print()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(survivors, f, indent=2)
    print(f"\nSaved qualifying pool to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()