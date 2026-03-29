# experiments/week1/scripts/kalshi_pull.py
"""
LATENTFORGE — Kalshi Daily Market Data Collection
Pulls active markets from Kalshi API and saves to data/kalshi/
Runs daily. Replaces broken Polymarket Gamma API.
"""

import requests
import json
import os
from datetime import datetime

OUTPUT_DIR = os.path.expanduser("~/Projects/data/kalshi")
os.makedirs(OUTPUT_DIR, exist_ok=True)

KALSHI_API_BASE = "https://api.elections.kalshi.com/trade-api/v2"

def pull_markets(api_key_id):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key_id}"
    }
    
    try:
        response = requests.get(
            f"{KALSHI_API_BASE}/markets",
            headers=headers,
            params={"limit": 100, "status": "open"},
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        markets = data.get("markets", [])
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = os.path.join(OUTPUT_DIR, f"markets_{date_str}.json")
        
        with open(filename, "w") as f:
            json.dump({
                "pulled_at": datetime.now().isoformat(),
                "market_count": len(markets),
                "markets": markets
            }, f, indent=2)
        
        print(f"Saved {len(markets)} markets to {filename}")
        return len(markets)
    
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    api_key_id = os.environ.get("KALSHI_API_KEY_ID")
    if not api_key_id:
        print("ERROR: KALSHI_API_KEY_ID not set")
        print("Run: export KALSHI_API_KEY_ID=your-key-id-here")
    else:
        count = pull_markets(api_key_id)
        print(f"Done. {count} markets at {datetime.now().isoformat()}")
