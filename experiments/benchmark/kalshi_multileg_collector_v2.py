"""
Kalshi Multi-Leg Parlay Collector v0.2 - More Precise Filter
"""
import json
from pathlib import Path
from datetime import datetime

KALSHI_DIR = Path.home() / "Projects/data/kalshi"
MULTILEG_DIR = KALSHI_DIR / "multileg"
MULTILEG_DIR.mkdir(exist_ok=True)

def is_true_multileg(market):
    if not isinstance(market, dict):
        return False
    # Stronger filter for multi-leg parlays
    market_id = str(market.get("market_id", "")).upper()
    if "KXMVE" in market_id and "CROSSCATEGORY" in market_id:
        return True
    if market.get("mve_selected_legs") and len(market.get("mve_selected_legs", [])) > 1:
        return True
    if "parlay" in str(market.get("title", "")).lower() or "multi" in str(market.get("description", "")).lower():
        return True
    return False

def backfill_multileg():
    json_files = sorted(KALSHI_DIR.glob("markets_*.json"))
    print(f"Found {len(json_files)} Kalshi daily files.")

    for file_path in json_files:
        date_str = file_path.stem.replace("markets_", "")
        output_path = MULTILEG_DIR / f"multileg_{date_str}.json"

        try:
            with open(file_path) as f:
                markets = json.load(f)

            true_multileg = [m for m in markets if is_true_multileg(m)]

            with open(output_path, "w") as f:
                json.dump(true_multileg, f, indent=2)

            print(f"✓ {date_str}: {len(true_multileg)} true multi-leg parlays saved")
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")

if __name__ == "__main__":
    backfill_multileg()
