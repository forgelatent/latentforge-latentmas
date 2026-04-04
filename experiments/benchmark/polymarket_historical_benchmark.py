import urllib.request, json, os
from pathlib import Path
from datetime import datetime

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OUTPUT_DIR = Path("experiments/benchmark/polymarket_historical")
OUTPUT_DIR.mkdir(exist_ok=True)

def fetch_resolved_markets(limit=500):
    req = urllib.request.Request(
        "https://gamma-api.polymarket.com/markets?closed=true&limit=" + str(limit),
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    resolved = []
    for m in data:
        question = m.get("question", "")
        prices_raw = m.get("outcomePrices", "")
        try:
            p = [float(x) for x in json.loads(prices_raw)]
            if all(v == 0 for v in p):
                continue
            outcome = 1 if p[0] > 0.9 else (0 if p[0] < 0.1 else None)
            if outcome is not None and question:
                resolved.append({"question": question, "outcome": outcome})
        except:
            pass
    return resolved

def swarm_estimate(question):
    if not ANTHROPIC_API_KEY:
        return None
    agents = [
        "You are a macro analyst. Give a probability 0-100 for this market resolving YES. Reply with a single number only.",
        "You are a quantitative researcher. Give a probability 0-100 for this market resolving YES. Reply with a single number only.",
        "You are a contrarian forecaster who questions consensus. Give a probability 0-100 for this market resolving YES. Reply with a single number only.",
    ]
    probs = []
    for system in agents:
        try:
            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 10,
                "system": system,
                "messages": [{"role": "user", "content": question}]
            }).encode()
            req = urllib.request.Request(
                "https://api.anthropic.com/v1/messages",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": ANTHROPIC_API_KEY,
                    "anthropic-version": "2023-06-01"
                }
            )
            with urllib.request.urlopen(req) as r:
                resp = json.loads(r.read())
            raw = resp["content"][0]["text"].strip().replace("%", "")
            probs.append(float(raw) / 100.0)
        except Exception as e:
            print("  Agent error: " + str(e))
    return sum(probs) / len(probs) if probs else None

def run(sample_size=20):
    print("Fetching resolved Polymarket markets...")
    markets = fetch_resolved_markets(500)
    print("Total resolved: " + str(len(markets)))

    sample = markets[:sample_size]
    print("Running swarm on " + str(len(sample)) + " markets...")
    print("")

    results = []
    swarm_brier_total = 0
    naive_brier_total = 0

    for i, m in enumerate(sample):
        q = m["question"]
        actual = m["outcome"]
        swarm_prob = swarm_estimate(q)
        if swarm_prob is None:
            continue
        sb = (swarm_prob - actual) ** 2
        nb = (0.5 - actual) ** 2
        swarm_brier_total += sb
        naive_brier_total += nb
        results.append({
            "question": q[:80],
            "actual": actual,
            "swarm_prob": round(swarm_prob, 3),
            "swarm_brier": round(sb, 4),
            "naive_brier": round(nb, 4)
        })
        print("  [" + str(i+1) + "/" + str(len(sample)) + "] swarm=" + str(round(swarm_prob, 2)) + " actual=" + str(actual) + " | " + q[:55])

    n = len(results)
    if n == 0:
        print("No results. Check API key.")
        return

    avg_swarm = round(swarm_brier_total / n, 4)
    avg_naive = round(naive_brier_total / n, 4)
    improvement = round((avg_naive - avg_swarm) / avg_naive * 100, 1)

    print("")
    print("=== RESULTS ===")
    print("Markets scored: " + str(n))
    print("Swarm avg Brier score: " + str(avg_swarm) + "  (lower is better)")
    print("Naive 50/50 Brier score: " + str(avg_naive))
    print("Swarm improvement over naive: " + str(improvement) + "%")

    date_str = datetime.now().strftime("%Y-%m-%d")
    out = OUTPUT_DIR / ("historical_" + date_str + ".json")
    with open(out, "w") as f:
        json.dump({
            "summary": {
                "n": n,
                "swarm_brier": avg_swarm,
                "naive_brier": avg_naive,
                "improvement_pct": improvement
            },
            "results": results
        }, f, indent=2)
    print("Saved to " + str(out))

if __name__ == "__main__":
    run(sample_size=20)
