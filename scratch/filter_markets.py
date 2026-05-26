#!/usr/bin/env python3
"""
Round 3 market filter — May 26, 2026.

Reads ~/Projects/data/polymarket/2026-05-26.json and applies the five locked
criteria from the May 25 Step 7 synthesis. Prints the markets that survive.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PULL_FILE = Path.home() / "Projects/data/polymarket/2026-05-26.json"
TODAY = datetime(2026, 5, 26, tzinfo=timezone.utc)
MIN_DAYS = 14
MAX_DAYS = 90
MIN_PROB = 0.15
MAX_PROB = 0.80

SPORTS_KEYWORDS = [
    "nba", "nhl", "mlb", "nfl", "ncaa", "wnba", "epl", "uefa", "champions league",
    "premier league", "la liga", "serie a", "bundesliga", "mls", "f1", "formula 1",
    "nascar", "ufc", "mma", "boxing", "tennis", "atp", "wta", "golf", "pga",
    "tournament", "playoff", "championship", "world cup", "olympics", "olympic",
    "cricket", "rugby", "sox", "yankees", "lakers", "warriors", "celtics",
    "fiorentina", "match", "vs.", " v ", " vs ",
]

DOMAIN_KEYWORDS = {
    "macro": ["fed", "fomc", "cpi", "inflation", "unemployment", "gdp", "rate cut",
              "rate hike", "recession", "s&p", "treasury", "yield", "powell",
              "jobs report", "bls", "pce"],
    "policy": ["ban", "law", "bill", "executive order", "regulation", "tariff",
               "shutdown", "senate", "house pass", "congress", "supreme court",
               "ruling"],
    "geopolitics": ["iran", "russia", "ukraine", "china", "taiwan", "israel",
                    "gaza", "nato", "sanctions", "war", "ceasefire", "north korea",
                    "election"],
    "ai-tech": ["openai", "anthropic", "claude", "gpt", "llama", "deepmind",
                "ai ", "agi", "apple", "nvidia", "google", "microsoft", "meta",
                "tesla", "spacex"],
    "crypto": ["bitcoin", "btc", "ethereum", "eth", "crypto", "coinbase"],
}
def load_markets():
    if not PULL_FILE.exists():
        print(f"ERROR: pull file not found at {PULL_FILE}", file=sys.stderr)
        sys.exit(1)
    with open(PULL_FILE) as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "markets" in data:
        return data["markets"]
    if isinstance(data, dict):
        print(f"ERROR: pull file is a dict with keys {list(data.keys())[:10]}", file=sys.stderr)
        sys.exit(1)
    print(f"ERROR: unexpected pull file shape: {type(data)}", file=sys.stderr)
    sys.exit(1)


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
    rejects = {
        "no_end_date": 0,
        "too_soon": 0,
        "too_late": 0,
        "no_price": 0,
        "near_certain": 0,
        "sports": 0,
        "inactive": 0,
        "non_binary": 0,
    }

    for m in markets:
        if m.get("closed") or m.get("archived"):
            rejects["inactive"] += 1
            continue
        if m.get("active") is False:
            rejects["inactive"] += 1
            continue

        if is_sports(m):
            rejects["sports"] += 1
            continue

        end = parse_end_date(m)
        if end is None:
            rejects["no_end_date"] += 1
            continue
        days_to_resolution = (end - TODAY).days
        if days_to_resolution < MIN_DAYS:
            rejects["too_soon"] += 1
            continue
        if days_to_resolution > MAX_DAYS:
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
            "market": m,
            "yes_price": yes_price,
            "days_to_resolution": days_to_resolution,
            "end_date": end,
            "tags": tag_domain(m),
            "volume": get_volume(m),
            "liquidity": get_liquidity(m),
        })

    return survivors, rejects
def print_summary(total, survivors, rejects):
    print("=" * 70)
    print("ROUND 3 FILTER SUMMARY — May 26, 2026")
    print("=" * 70)
    print(f"Total markets in pull:        {total}")
    print(f"Markets passing all filters:  {len(survivors)}")
    print()
    print("Rejection counts (first failure wins):")
    for reason, count in rejects.items():
        print(f"  {reason:20s}  {count}")
    print()


def print_survivors(survivors):
    print("=" * 70)
    print("SURVIVING MARKETS")
    print("=" * 70)
    print()

    by_domain = {}
    for s in survivors:
        primary = s["tags"][0]
        by_domain.setdefault(primary, []).append(s)

    domain_order = ["macro", "policy", "geopolitics", "ai-tech", "crypto", "other"]
    for domain in domain_order:
        if domain not in by_domain:
            continue
        print(f"--- {domain.upper()} ({len(by_domain[domain])}) ---")
        for s in by_domain[domain]:
            m = s["market"]
            question = m.get("question", "(no question)")
            slug = m.get("slug", "(no slug)")
            condition_id = m.get("conditionId", "(no conditionId)")
            yes_pct = int(s["yes_price"] * 100)
            days = s["days_to_resolution"]
            end_str = s["end_date"].strftime("%Y-%m-%d")
            vol = s["volume"]
            liq = s["liquidity"]
            tags = ", ".join(s["tags"])

            print(f"\n  Q: {question}")
            print(f"     slug:         {slug}")
            print(f"     conditionId:  {condition_id}")
            print(f"     YES price:    {yes_pct}%")
            print(f"     resolves:     {end_str} ({days} days)")
            print(f"     volume:       {vol if vol is None else f'${vol:,.0f}'}")
            print(f"     liquidity:    {liq if liq is None else f'${liq:,.0f}'}")
            print(f"     tags:         {tags}")
        print()


def main():
    markets = load_markets()
    survivors, rejects = filter_markets(markets)
    print_summary(len(markets), survivors, rejects)
    print_survivors(survivors)


if __name__ == "__main__":
    main()