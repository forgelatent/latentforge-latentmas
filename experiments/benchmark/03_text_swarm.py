# experiments/benchmark/03_text_swarm.py
"""
Arm 2: Text Swarm Estimator
Calls Claude 3 times with different reasoning angles on the same markets.
Aggregates probabilities to produce a swarm estimate.
Compares against Arm 1 (single text agent) baseline.
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime("%Y-%m-%d")
BENCHMARK_DIR = Path("experiments/benchmark")
SEED_FILE = BENCHMARK_DIR / "policy_markets_seed.json"
OUTPUT_FILE = BENCHMARK_DIR / f"text_swarm_{TODAY}.md"

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

AGENT_PROMPTS = [
    "You are a macroeconomic analyst. Estimate probabilities based on economic fundamentals, central bank policy, and historical base rates. Be calibrated and conservative.",
    "You are a quantitative researcher who specializes in prediction markets. Estimate probabilities based on current market signals, momentum, and crowd wisdom. Weight recent data heavily.",
    "You are a contrarian forecaster. Your job is to identify where the consensus is likely wrong. Estimate probabilities by stress-testing assumptions and looking for tail risks the market underweights.",
]

def call_claude(system_prompt, markets_text):
    if not ANTHROPIC_API_KEY:
        return None
    prompt = f"""Here are today's prediction markets:

{markets_text}

For each market, give your probability estimate for the YES outcome as a percentage.

Format exactly like this for each market:
Market N: XX%

Only output the market numbers and percentages, nothing else."""

    try:
        r = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 300,
                "system": system_prompt,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )
        if r.status_code == 200:
            return r.json()["content"][0]["text"]
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def parse_probabilities(text, n_markets):
    probs = []
    if not text:
        return [None] * n_markets
    for i in range(1, n_markets + 1):
        for line in text.split("\n"):
            if line.strip().startswith(f"Market {i}:"):
                try:
                    pct = line.split(":")[1].strip().replace("%", "")
                    probs.append(float(pct))
                    break
                except:
                    probs.append(None)
                    break
        else:
            probs.append(None)
    return probs

def main():
    if not SEED_FILE.exists():
        print("Seed file not found.")
        return

    markets = json.load(open(SEED_FILE))
    n = len(markets)

    markets_text = ""
    for i, m in enumerate(markets, 1):
        markets_text += f"Market {i}: {m.get('question', '')}\n"
        markets_text += f"Current crowd probability: {m.get('current_price', 'N/A')}\n\n"

    print(f"Running text swarm on {n} markets...")

    all_probs = []
    agent_names = ["Macro Analyst", "Quant Researcher", "Contrarian Forecaster"]

    for i, (name, prompt) in enumerate(zip(agent_names, AGENT_PROMPTS)):
        print(f"  Agent {i+1}: {name}...")
        result = call_claude(prompt, markets_text)
        probs = parse_probabilities(result, n)
        all_probs.append(probs)
        print(f"  Raw: {probs}")

    # Aggregate: simple average, skip None
    swarm_probs = []
    for j in range(n):
        valid = [all_probs[i][j] for i in range(3) if all_probs[i][j] is not None]
        swarm_probs.append(round(sum(valid) / len(valid), 1) if valid else None)

    # Write output
    out = open(OUTPUT_FILE, "w")
    out.write(f"# Text Swarm Estimates - {TODAY}\n\n")
    out.write("Three agents (Macro, Quant, Contrarian) averaged into swarm estimate.\n\n")
    out.write(f"| # | Market | Macro | Quant | Contrarian | Swarm Avg | Crowd |\n")
    out.write(f"|---|--------|-------|-------|------------|-----------|-------|\n")

    for j, m in enumerate(markets):
        q = m.get("question", "")[:60] + "..."
        crowd = m.get("current_price", "N/A")
        macro = f"{all_probs[0][j]}%" if all_probs[0][j] else "-"
        quant = f"{all_probs[1][j]}%" if all_probs[1][j] else "-"
        contra = f"{all_probs[2][j]}%" if all_probs[2][j] else "-"
        swarm = f"{swarm_probs[j]}%" if swarm_probs[j] else "-"
        crowd_pct = f"{int(float(crowd)*100)}%" if crowd not in ["N/A", None] else str(crowd)
        out.write(f"| {j+1} | {q} | {macro} | {quant} | {contra} | {swarm} | {crowd_pct} |\n")

    out.write("\n## Divergence from Single Agent (Arm 1 vs Arm 2)\n\n")
    out.write("Compare this file against text_baseline_{TODAY}.md to see if swarm moves estimates.\n")
    out.close()

    print(f"\nSaved to {OUTPUT_FILE}")
    print("\nSwarm probabilities:")
    for j, m in enumerate(markets):
        print(f"  {j+1}. {m.get('question','')[:50]}... -> {swarm_probs[j]}% (crowd: {m.get('current_price','?')})")

if __name__ == "__main__":
    main()
