"""
Polymarket Resolved Historical Benchmark v0.2
Pulls closed markets, attempts to identify resolved ones, runs text swarm, and computes Brier score.
"""
import json
import urllib.request
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("experiments/benchmark/polymarket_historical")
OUTPUT_DIR.mkdir(exist_ok=True)

def fetch_resolved_markets(limit=20):
    url = f"https://gamma-api.polymarket.com/markets?closed=true&limit={limit}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; LatentForge-Benchmark/1.0)'})
    
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
        return data
    except Exception as e:
        print(f"Error fetching Polymarket data: {e}")
        return []

def is_resolved(market):
    # Try to detect if market has a clear resolved outcome
    if market.get("resolved") is True:
        return True
    if market.get("outcome") is not None:
        return True
    if market.get("closed") and market.get("outcomePrices"):
        # Some closed markets have outcomePrices that can indicate resolution
        return True
    return False

def get_actual_outcome(market):
    # Simple heuristic for now
    outcome = market.get("outcome")
    if outcome is not None:
        return float(outcome) if isinstance(outcome, (int, float)) else 0.0
    # Fallback: look at outcomePrices if available
    prices = market.get("outcomePrices")
    if prices and len(prices) > 0:
        try:
            return float(prices[0])  # Take first outcome as "Yes" probability at close
        except:
            pass
    return None

def simple_swarm_estimate(question):
    # TODO: Replace with real text swarm call later
    # For now, return a dummy value so the script runs
    return 0.50

def run_benchmark():
    markets = fetch_resolved_markets(limit=30)
    results = []
    
    for market in markets:
        if not is_resolved(market):
            continue
            
        question = market.get("question", "")
        actual = get_actual_outcome(market)
        if actual is None:
            continue
            
        swarm_prob = simple_swarm_estimate(question)
        brier = (swarm_prob - actual) ** 2
        
        results.append({
            "question": question[:120],
            "swarm_prob": swarm_prob,
            "actual_outcome": actual,
            "brier": brier,
            "market_id": market.get("id")
        })
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = OUTPUT_DIR / f"resolved_benchmark_{date_str}.json"
    
    with open(output_path, "w") as f:
        json.dump({
            "date": date_str,
            "total_resolved_analyzed": len(results),
            "results": results
        }, f, indent=2)
    
    print(f"✅ Analyzed {len(results)} resolved Polymarket markets.")
    print(f"Results saved to {output_path}")
    
    if results:
        avg_brier = sum(r["brier"] for r in results) / len(results)
        print(f"Average Brier score: {avg_brier:.4f} (lower is better)")

if __name__ == "__main__":
    run_benchmark()
