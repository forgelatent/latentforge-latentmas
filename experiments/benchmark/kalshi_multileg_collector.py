"""
Kalshi Multi-Leg Parlay Collector v0.1
Filters existing daily Kalshi JSON files for multi-leg markets (those with mve_selected_legs).
Backfills all existing files.
"""
import json
import os
from datetime import datetime
from pathlib import Path

KALSHI_DIR = Path.home() / "Projects/data/kalshi"
MULTILEG_DIR = KALSHI_DIR / "multileg"
MULTILEG_DIR.mkdir(exist_ok=True)

def is_multileg_market(market):
    # Look for indicators of multi-leg / parlay markets
    if isinstance(market, dict):
        market_id = market.get("market_id", "")
        if "KXMVE" in market_id or market.get("mve_selected_legs") or "parlay" in str(market).lower():
            return True
    return False

def backfill_multileg():
    json_files = sorted(KALSHI_DIR.glob("*.json"))
    print(f"Found {len(json_files)} Kalshi daily files to process.")
    
    for file_path in json_files:
        date_str = file_path.stem.replace("markets_", "")
        output_path = MULTILEG_DIR / f"multileg_{date_str}.json"
        
        try:
            with open(file_path) as f:
                markets = json.load(f)
            
            multileg = [m for m in markets if is_multileg_market(m)]
            
            with open(output_path, "w") as f:
                json.dump(multileg, f, indent=2)
            
            print(f"✓ {date_str}: {len(multileg)} multi-leg markets saved")
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")

if __name__ == "__main__":
    backfill_multileg()
