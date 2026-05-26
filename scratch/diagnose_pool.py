#!/usr/bin/env python3
"""
Round 3 diagnostic — May 26, 2026.

Runs three filter variants against the same Polymarket pull to see how the
qualifying pool changes when we widen or remove the date window.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

PULL_FILE = Path.home() / "Projects/data/polymarket/2026-05-26.json"
TODAY = datetime(2026, 5, 26, tzinfo=timezone.utc)
MIN_PROB = 0.15
MAX_PROB = 0.80

SPORTS_KEYWORDS = [
    "nba", "nhl", "mlb", "nfl", "ncaa", "wnba", "epl", "uefa", "champions league",
    "premier league", "la liga", "serie a", "bundesliga", "mls", "f1", "formula 1",
    "nascar", "ufc", "mma", "boxing", "tennis", "atp", "wta", "golf", "pga",
    "tournament", "playoff", "championship", "world cup", "olympics", "olympic",
    "cricket", "rugby", "sox", "yankees", "lakers", "warriors", "celtics",
    "fiorentina", "match", "vs.", " v ", " vs ",
    "fifwc", "fifa", "world-cup",
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
                    "election", "primary", "governor", "midterm"],
    "ai-tech": ["openai", "anthropic", "claude", "gpt", "llama", "deepmind",
                "ai ", "agi", "apple", "nvidia", "google", "microsoft", "meta",
                "tesla", "spacex"],
    "crypto": ["bitcoin", "btc", "ethereum", "eth", "crypto", "coinbase"],
}
def load_markets():
    with open(PULL_FILE) as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return data.get("markets", [])


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


def passes_common(market):
    if market.get("closed") or market.get("archived"):
        return False
    if market.get("active") is False:
        return False
    if is_sports(market):
        return False
    yes_price = parse_yes_price(market)
    if yes_price is None:
        return False
    if yes_price < MIN_PROB or yes_price > MAX_PROB:
        return False
    outcomes = market.get("outcomes")
    if isinstance(outcomes, str):
        try:
            outcomes = json.loads(outcomes)
        except json.JSONDecodeError:
            outcomes = None
    if isinstance(outcomes, list) and len(outcomes) != 2:
        return False
    return True
def get_survivors(markets, min_days, max_days):
    out = []
    for m in markets:
        if not passes_common(m):
            continue
        end = parse_end_date(m)
        if end is None:
            continue
        days = (end - TODAY).days
        if min_days is not None and days < min_days:
            continue
        if max_days is not None and days > max_days:
            continue
        out.append({
            "market": m,
            "days": days,
            "yes_price": parse_yes_price(m),
            "tags": tag_domain(m),
            "volume": get_volume(m),
            "liquidity": get_liquidity(m),
        })
    return out


def print_market(s):
    m = s["market"]
    question = m.get("question", "(no question)")
    slug = m.get("slug", "(no slug)")
    yes_pct = int(s["yes_price"] * 100)
    days = s["days"]
    vol = s["volume"]
    liq = s["liquidity"]
    tags = ", ".join(s["tags"])
    vol_str = f"${vol:,.0f}" if vol is not None else "?"
    liq_str = f"${liq:,.0f}" if liq is not None else "?"
    print(f"  [{tags}] {question}")
    print(f"     slug: {slug}")
    print(f"     YES: {yes_pct}%  resolves in {days}d  vol {vol_str}  liq {liq_str}")
    print()


def main():
    markets = load_markets()
    print(f"Total markets in pull: {len(markets)}")
    print()

    variants = [
        ("A. 14-120 days (widen far end)", 14, 120),
        ("B. 7-90 days (widen near end)", 7, 90),
        ("C. No date filter", None, None),
    ]

    results = {}
    for name, mn, mx in variants:
        survivors = get_survivors(markets, mn, mx)
        results[name] = survivors

    print("=" * 70)
    print("COUNTS PER VARIANT")
    print("=" * 70)
    for name, _, _ in variants:
        print(f"  {name}: {len(results[name])} markets")
    print()

    for name, _, _ in variants:
        print("=" * 70)
        print(name)
        print("=" * 70)
        survivors = results[name]
        if not survivors:
            print("  (no markets survive)")
            print()
            continue
        survivors.sort(key=lambda s: s["days"])
        for s in survivors:
            print_market(s)


if __name__ == "__main__":
    main()