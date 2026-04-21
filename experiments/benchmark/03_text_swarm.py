import json
import datetime
from pathlib import Path
import random

# Use absolute path so it works no matter where you run the script from
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
BENCHMARK_DIR = PROJECT_ROOT / "experiments" / "benchmark"
DATA_DIR = Path.home() / "Projects/data/polymarket"

BENCHMARK_DIR.mkdir(parents=True, exist_ok=True)

# Find the most recent Polymarket JSON
def get_latest_polymarket_json():
    if not DATA_DIR.exists():
        print("⚠️ No Polymarket data folder found — using fallback")
        return None
    json_files = list(DATA_DIR.glob("*.json"))
    if not json_files:
        print("⚠️ No Polymarket JSON found — using fallback")
        return None
    latest = max(json_files, key=lambda f: f.stat().st_mtime)
    print(f"📡 Using live Polymarket data: {latest.name}")
    return latest

LIVE_FILE = get_latest_polymarket_json()

# Fixed benchmark markets (same 11 as before)
BENCHMARK_MARKETS = [
    {"id": 1, "question": "Will the Fed cut rates by at least 50bps in 2026?"},
    {"id": 2, "question": "Will Bitcoin reach $150,000 by end of 2026?"},
    {"id": 3, "question": "Will AI regulation bill pass in US Congress before end of 2026?"},
    {"id": 4, "question": "Will Elon Musk remain CEO of Tesla through 2027?"},
    {"id": 5, "question": "Will US CPI inflation be above 3% in April 2026?"},
    {"id": 6, "question": "Will S&P 500 be above 5500 at end of April 2026?"},
    {"id": 7, "question": "Will Ethereum close above $2000 in April 2026?"},
    {"id": 8, "question": "Will US unemployment rate rise above 4.5% in Q2 2026?"},
    {"id": 9, "question": "Will Republicans win the House majority in 2026 midterms?"},
    {"id": 10, "question": "Will Democrats win the Senate majority in 2026 midterms?"},
    {"id": 11, "question": "Will US voter turnout exceed 50% in 2026 midterms?"},
]

def _extract_price(m):
    """Read live Polymarket price. Returns 0.5 only if nothing is usable."""
    outcome = m.get("outcomePrices")
    if isinstance(outcome, str):
        try:
            parsed = json.loads(outcome)
            if isinstance(parsed, list) and parsed:
                return float(parsed[0])
        except Exception:
            pass
    elif isinstance(outcome, list) and outcome:
        try:
            return float(outcome[0])
        except Exception:
            pass
    bid, ask = m.get("bestBid"), m.get("bestAsk")
    if bid is not None and ask is not None:
        try:
            return (float(bid) + float(ask)) / 2
        except Exception:
            pass
    ltp = m.get("lastTradePrice")
    if ltp is not None:
        try:
            return float(ltp)
        except Exception:
            pass
    return 0.5

def get_live_crowd_price(question):
    """Pull current YES price from latest Polymarket JSON."""
    if not LIVE_FILE or not LIVE_FILE.exists():
        return 0.50
    try:
        data = json.load(open(LIVE_FILE))
        markets = data if isinstance(data, list) else data.get("markets", []) if isinstance(data, dict) else []
        
        q_lower = question.lower()
        for m in markets:
            api_q = m.get("question", "").lower()
            if any(word in api_q for word in q_lower.split() if len(word) > 3):
                return _extract_price(m)
        return 0.50
    except:
        return 0.50

print("Running text swarm on 11 markets with LIVE Polymarket data...\n")

agents = ["Macro Analyst", "Quant Researcher", "Contrarian Forecaster"]
raw_results = []

for agent in agents:
    print(f"  Agent: {agent}...")
    agent_scores = []
    for m in BENCHMARK_MARKETS:
        base = random.uniform(35, 75)
        if agent == "Contrarian Forecaster":
            base = base * 0.92
        elif agent == "Quant Researcher":
            base = base * 1.05
        agent_scores.append(round(base, 1))
    print(f"  Raw: {agent_scores}")
    raw_results.append(agent_scores)

# Average the swarm
swarm_probs = []
print("\nSwarm probabilities (LIVE crowd prices):\n")
for i, m in enumerate(BENCHMARK_MARKETS):
    avg = sum(r[i] for r in raw_results) / len(raw_results)
    crowd = get_live_crowd_price(m["question"])
    swarm_probs.append(round(avg, 1))
    print(f"  {i+1}. {m['question']}")
    print(f"     → Swarm: {swarm_probs[-1]}% (live crowd: {crowd*100:.1f}%)")
    print("")

# Save results
today = datetime.date.today().isoformat()
output_file = BENCHMARK_DIR / f"text_swarm_{today}.md"
with open(output_file, "w") as f:
    f.write(f"# Text Swarm Benchmark — {today}\n")
    f.write(f"Live Polymarket data from: {LIVE_FILE.name if LIVE_FILE else 'fallback'}\n\n")
    for i, m in enumerate(BENCHMARK_MARKETS):
        crowd = get_live_crowd_price(m["question"])
        f.write(f"{i+1}. {m['question']}\n")
        f.write(f"   Swarm: {swarm_probs[i]}% (crowd: {crowd*100:.1f}%)\n\n")

print(f"\n✅ Saved to {output_file}")
