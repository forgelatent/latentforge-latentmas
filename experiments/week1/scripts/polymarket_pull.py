# experiments/week1/scripts/polymarket_pull.py
import requests, json
from datetime import datetime, timezone
from pathlib import Path

TODAY = datetime.now().strftime("%Y-%m-%d")
OUTPUT_DIR = Path("~/Projects/data/polymarket").expanduser()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / f"{TODAY}.json"

def main():
    url = "https://gamma-api.polymarket.com/markets"
    params = {"closed": "false", "limit": 200, "order": "volume", "ascending": "false"}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    markets = response.json()
    now = datetime.now(timezone.utc)
    open_markets = []
    for m in markets:
        if not isinstance(m, dict) or m.get("closed") is True: continue
        end = m.get("endDate") or m.get("end_date_iso")
        if end:
            try:
                if datetime.fromisoformat(end.replace("Z","+00:00")) < now: continue
            except: continue
        open_markets.append(m)
    print(f"Open markets: {len(open_markets)}")
    with open(OUTPUT_FILE, "w") as f:
        json.dump(open_markets, f, indent=2)
    print(f"Saved to {OUTPUT_FILE}")
    for m in open_markets[:5]:
        print(f"  Q: {m.get('question','?')[:100]}")
        print(f"  End: {m.get('endDate','?')[:10]} | Volume: {m.get('volume','?')}")

main()
