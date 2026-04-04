"""
Polymarket Historical Benchmark v0.1 (Fast Version)
Uses your existing historical Polymarket JSON files.
Runs the text swarm on resolved markets and compares to actual outcomes.
"""
import json
import os
from datetime import datetime
from pathlib import Path

# For now, we'll use a simple placeholder swarm estimator.
# Later we can hook in the real text swarm.
def simple_swarm_estimate(question):
    # Placeholder: return a dummy probability. Replace with real swarm call later.
    return 0.50  # 50% as starting point

def run_historical_benchmark():
    polymarket_dir = Path.home() / "Projects/data/polymarket"
    json_files = sorted(polymarket_dir.glob("*.json"))
    
    results = []
    for file_path in json_files:
        try:
            with open(file_path) as f:
                markets = json.load(f)
            
            for market in markets:
                if not isinstance(market, dict):
                    continue
                    
                question = market.get("question", "")
                resolved = market.get("resolved", False)
                actual_outcome = market.get("outcome", None)  # 0 or 1 or None if not resolved
                
                if not resolved or actual_outcome is None:
                    continue
                
                swarm_prob = simple_swarm_estimate(question)
                actual_prob = 1.0 if actual_outcome == 1 else 0.0
                
                brier = (swarm_prob - actual_prob) ** 2
                
                results.append({
                    "date": file_path.stem,
                    "question": question[:100],
                    "swarm_prob": swarm_prob,
                    "actual": actual_outcome,
                    "brier": brier
                })
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Save results
    output_dir = Path("experiments/benchmark/polymarket_historical")
    output_dir.mkdir(exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = output_dir / f"historical_benchmark_{date_str}.json"
    
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ Historical benchmark complete. {len(results)} resolved markets analyzed.")
    print(f"Results saved to {output_path}")
    
    # Quick summary
    if results:
        avg_brier = sum(r["brier"] for r in results) / len(results)
        print(f"Average Brier score: {avg_brier:.4f} (lower is better)")

if __name__ == "__main__":
    run_historical_benchmark()
