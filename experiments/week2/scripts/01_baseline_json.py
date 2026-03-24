import json, time, os

def run_baseline(n=10):
    results = []
    for i in range(n):
        msg_a = {
            "agent": "A", "exchange_id": i, "timestamp": time.time(),
            "task": "Estimate probability of market outcome X given liquidity Y",
            "reasoning_trace": (
                "I parse the task, activate relevant prior knowledge about market "
                "microstructure, consider order book depth, recent price action, "
                "and formulate a probability estimate with supporting rationale."
            ),
            "probability_estimate": round(0.61 + i * 0.01, 3),
            "confidence_interval": [0.54, 0.68],
            "supporting_factors": [
                "Order book imbalance signals upward pressure",
                "Historical base rate for this outcome type: 0.58",
                "Recent resolution trend: 3 of last 5 similar markets resolved YES"
            ],
            "query_to_b": (
                "Do you see contradictory signals in the volatility surface "
                "that would revise this estimate downward?"
            )
        }
        ser_a = json.dumps(msg_a)
        msg_b = {
            "agent": "B", "exchange_id": i, "timestamp": time.time(),
            "received_bytes": len(ser_a.encode()),
            "reasoning_trace": (
                "Parsing Agent A estimate. Cross-referencing with implied vol surface. "
                "Slight downward revision warranted based on IV skew."
            ),
            "revised_estimate": round(0.58 + i * 0.01, 3),
            "revision_reason": "IV skew suggests more downside than A point estimate reflects",
            "consensus_ready": True
        }
        ser_b = json.dumps(msg_b)
        total = len(ser_a.encode()) + len(ser_b.encode())
        results.append({"exchange_id": i, "bytes_a": len(ser_a.encode()),
                        "bytes_b": len(ser_b.encode()), "total": total,
                        "tokens_approx": len(ser_a.split()) + len(ser_b.split())})
    avg_bytes  = sum(r["total"] for r in results) / len(results)
    avg_tokens = sum(r["tokens_approx"] for r in results) / len(results)
    print("=" * 55)
    print("LATENTFORGE — JSON BASELINE")
    print("=" * 55)
    print(f"Avg bytes/exchange:  {avg_bytes:.0f}")
    print(f"Avg tokens/exchange: {avg_tokens:.0f}")
    print(f"\n*** PASTE INTO 02_latent_delta.py line 22: ***")
    print(f"JSON_BASELINE_BYTES = {avg_bytes:.0f}")
    os.makedirs("/workspace/results", exist_ok=True)
    with open("/workspace/results/01_baseline.json", "w") as f:
        json.dump({"avg_bytes": avg_bytes, "avg_tokens": avg_tokens,
                   "per_exchange": results}, f, indent=2)
    print("\nSaved: /workspace/results/01_baseline.json")

if __name__ == "__main__":
    run_baseline()
