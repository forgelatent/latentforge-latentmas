"""
Polymarket Resolved Historical Benchmark v0.3
More robust detection of resolved markets.
"""
import json
import urllib.request
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("experiments/benchmark/polymarket_historical")
OUTPUT_DIR.mkdir(exist_ok=True)

def fetch_closed_markets(limit=50):
    url = f"https://gamma-api.polymarket.com/markets?closed=true&limit={limit}&sort=closedTime"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; LatentForge-Benchmark/1.0)'})
    
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def is_clearly_resolved(market):
    if market.get("resolved") is True:
        return True
    if market.get("finalized") is True:
        return True
    # Check if outcomePrices suggest a clear winner (one near 1.0, others near 0)
    prices = market.get("outcomePrices")
    if prices and isinstance(prices, list) and len(prices) >= 2:
        try:
            p = [float(x) for x in prices if x is not None]
            if any(abs(x - 1.0) < 0.05 for x in p) or any(abs(x - 0.0) < 0.05 for x in p):
                return True
        except:
            pass
    return False

def get_actual_outcome(market):
    prices = market.get("outcomePrices")
    if prices and isinstance(prices, list) and len(prices) > 0:
        try:
            p = [float(x) for x in prices if x is not None]
            if p:
                return p.index(max(p))  # Return index of highest probability outcome
        except:
            pass
    return market.get("outcome")

def simple_swarm_estimate(question):
    # Placeholder - replace with real swarm later
    return 0.50

def run_benchmark():
    markets = fetch_closed_markets(limit=50)
    results = []
    
    for market in markets:
        if not is_clearly_resolved(market):
            continue
            
        question = market.get("question", "")
        actual = get_actual_outcome(market)
        if actual is None:
            continue
            
        swarm_prob = simple_swarm_estimate(question)
        # Convert actual to probability (0 or 1)
        actual_prob = 1.0 if actual == 1 or actual == 0 else 0.5
        
        brier = (swarm_prob - actual_prob) ** 2
        
        results.append({
            "question": question[:100],
            "swarm_prob": swarm_prob,
            "actual_outcome": actual,
            "actual_prob": actual_prob,
            "brier": brier,
            "market_id": market.get("id")
        })
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = OUTPUT_DIR / f"resolved_benchmark_v2_{date_str}.json"
    
    with open(output_path, "w") as f:
        json.dump({
            "date": date_str,
            "total_analyzed": len(results),
            "results": results
        }, f, indent=2)
    
    print(f"✅ Analyzed {len(results)} resolved Polymarket markets.")
    print(f"Results saved to {output_path}")
    
    if results:
        avg_brier = sum(r["brier"] for r in results) / len(results)
        print(f"Average Brier score: {avg_brier:.4f} (lower is better)")

if __name__ == "__main__":
    run_benchmark()
