# experiments/week1/scripts/kalshi_pull.py
"""
Kalshi Pull — Simple and robust version
Fetches active markets and saves them cleanly as a list.
"""

import requests
import json
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime("%Y-%m-%d")
OUTPUT_DIR = Path("~/Projects/data/kalshi").expanduser()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / f"markets_{TODAY}.json"

def main():
    # Kalshi public API for markets
    url = "https://api.elections.kalshi.com/trade-api/v2/markets"
    params = {
        "limit": 1000,
        "status": "open"
    }

    try:
        import os
        api_key = os.environ.get('KALSHI_API_KEY', '')
        headers = {'Authorization': 'Bearer ' + api_key} if api_key else {}
        response = requests.get(url, params=params, headers=headers, timeout=20)
        response.raise_for_status()
        data = response.json()

        # Kalshi API usually returns {"markets": [...] } or direct list
        if isinstance(data, dict) and "markets" in data:
            markets = data["markets"]
        else:
            markets = data if isinstance(data, list) else []

        print(f"Total markets received: {len(markets)}")

        # Save raw markets
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(markets, f, indent=2)

        print(f"✅ Saved {len(markets)} markets to {OUTPUT_FILE}")

        if markets and len(markets) > 0:
            first = markets[0]
            print("\nFirst market sample keys:", list(first.keys()))
            print("First question:", first.get("title") or first.get("question") or "N/A")

    except Exception as e:
        print(f"Error fetching Kalshi data: {e}")

if __name__ == "__main__":
    main()
