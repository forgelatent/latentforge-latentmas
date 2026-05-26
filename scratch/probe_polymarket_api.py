#!/usr/bin/env python3
"""
Polymarket API probe — May 26, 2026.

The daily pull returned 93 markets. Polymarket has thousands of markets.
This script asks the Gamma API directly: how many active markets exist,
total, on the unauthenticated public endpoint?
"""

import json
import urllib.request
import urllib.parse
from collections import Counter

BASE = "https://gamma-api.polymarket.com/markets"
PAGE_SIZE = 100
MAX_PAGES = 100


def fetch_page(offset):
    params = {
        "active": "true",
        "closed": "false",
        "limit": str(PAGE_SIZE),
        "offset": str(offset),
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "latentforge-probe/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())
def main():
    all_markets = []
    seen_ids = set()

    for page_num in range(MAX_PAGES):
        offset = page_num * PAGE_SIZE
        try:
            markets = fetch_page(offset)
        except Exception as e:
            print(f"Page {page_num} failed: {e}")
            break

        if not markets:
            print(f"Page {page_num}: empty, stopping.")
            break

        new_markets = []
        for m in markets:
            cid = m.get("conditionId") or m.get("id") or m.get("slug")
            if cid and cid not in seen_ids:
                seen_ids.add(cid)
                new_markets.append(m)

        all_markets.extend(new_markets)
        print(f"Page {page_num}: fetched {len(markets)}, new {len(new_markets)}, total {len(all_markets)}")

        if len(markets) < PAGE_SIZE:
            print(f"Page {page_num}: short page, stopping.")
            break

    print()
    print("=" * 70)
    print(f"TOTAL ACTIVE NON-CLOSED MARKETS: {len(all_markets)}")
    print("=" * 70)
    print()

    categories = Counter()
    for m in all_markets:
        cat = m.get("category") or m.get("groupItemTitle") or "(no category)"
        categories[cat] += 1

    print("CATEGORIES (top 30):")
    for cat, count in categories.most_common(30):
        print(f"  {count:5d}  {cat}")
    print()

    print("SAMPLE OF FIRST 20 MARKETS (question text only):")
    for m in all_markets[:20]:
        q = m.get("question", "(no question)")
        cat = m.get("category", "(no cat)")
        print(f"  [{cat}] {q[:90]}")


if __name__ == "__main__":
    main()