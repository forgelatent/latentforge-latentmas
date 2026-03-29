# experiments/week1/scripts/polymarket_pull.py
"""
Polymarket Pull — Simple, robust version using /markets endpoint
Saves all markets and logs stats so we can see what's coming back.
"""

import requests
import json
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime("%Y-%m-%d")
OUTPUT_DIR = Path("~/Projects/data/polymarket").expanduser()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / f"{TODAY}.json"

def main():
    url = "https://gamma-api.polymarket.com/markets"
    params = {
        "active": "true",
        "limit": 200
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        markets = response.json()

        print(f"Total raw markets received: {len(markets)}")

        closed_count = sum(1 for m in markets if isinstance(m, dict) and m.get("closed") is True)
        open_count = len(markets) - closed_count

        print(f"Closed markets: {closed_count} | Open markets: {open_count}")

        # Save everything so we have data to work with
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(markets, f, indent=2)

        print(f"✅ Saved ALL {len(markets)} markets to {OUTPUT_FILE}")

        if markets:
            first = markets[0]
            print("\nFirst market question:", first.get("question", "N/A")[:120])
            print("First market closed:", first.get("closed"))
            print("First market endDate:", first.get("endDate"))
            print("First market volume:", first.get("volume"))

    except Exception as e:
        print(f"Error fetching Polymarket data: {e}")

if __name__ == "__main__":
    main()
