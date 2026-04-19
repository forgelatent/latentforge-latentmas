#!/usr/bin/env python3
# ===============================================================================
# [INVALIDATED 2026-04-18] This file contains claims derived from pre-live
# synthetic baseline data. See docs/INCIDENT_2026-04-18.md for full audit trail.
# ===============================================================================

"""
LatentForge Commercialization Agent
Runs nightly. Reads all data sources + previous thesis and updates
a running commercialization_thesis.md that compounds over time.
"""

import os
import json
from datetime import datetime
from pathlib import Path
import anthropic

CLIENT = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"], timeout=120)
MODEL = "claude-sonnet-4-6"

BASE = Path.home() / "Projects/latentforge-latentmas"
REVENUE_DIR = BASE / "revenue_ideas"
DIGEST_DIR = BASE / "research/daily-digest"
SUGGESTIONS_DIR = BASE / "research/suggestions"
FOUNDER_INPUTS_DIR = BASE / "founder_inputs"
CALIBRATION_DIR = BASE / "experiments/benchmark/calibration"
THESIS_FILE = BASE / "commercialization_thesis.md"
OUTPUT_DIR = BASE / "revenue_ideas"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_latest(directory, suffix=".md"):
    directory = Path(directory)
    files = sorted(directory.glob(f"*{suffix}"), reverse=True)
    if not files:
        return None, ""
    try:
        return files[0].name, files[0].read_text(encoding="utf-8")[:2000]
    except Exception:
        return None, ""

def load_thesis():
    if THESIS_FILE.exists():
        return THESIS_FILE.read_text(encoding="utf-8")[:3000]
    return "No prior thesis yet. This is Day 1."

def load_founder_inputs():
    notes = ""
    for f in sorted(FOUNDER_INPUTS_DIR.glob("*.md")):
        try:
            notes += f.read_text(encoding="utf-8")[:500] + "\n\n"
        except Exception:
            pass
    return notes[:2000] if notes else "None today."

def load_calibration():
    log = CALIBRATION_DIR / "brier_running.json"
    if not log.exists():
        return "No calibration data yet."
    try:
        data = json.loads(log.read_text())
        if not data:
            return "Calibration tracker running but no resolved markets yet."
        resolved = [m for m in data if m.get("outcome") is not None]
        if not resolved:
            return f"{len(data)} markets tracked. No resolutions yet."
        swarm_briers = [m["swarm_brier"] for m in resolved if m.get("swarm_brier") is not None]
        avg = sum(swarm_briers) / len(swarm_briers) if swarm_briers else None
        return f"{len(resolved)} resolved markets. Avg swarm Brier: {avg:.4f}" if avg else "Resolved but no scores yet."
    except Exception as e:
        return f"Error reading calibration: {e}"

def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = OUTPUT_DIR / f"commercialization_{date_str}.md"

    print(f"Running Commercialization Agent for {date_str}...")

    _, digest = load_latest(DIGEST_DIR)
    _, suggestions = load_latest(SUGGESTIONS_DIR)
    _, prev_revenue = load_latest(REVENUE_DIR)
    prior_thesis = load_thesis()
    founder_inputs = load_founder_inputs()
    calibration = load_calibration()

    prompt = f"""You are the Commercialization Intelligence for LatentForge.

LatentForge is building the first latent vector communication protocol for multi-agent AI systems.
Agents communicate via compressed hidden state deltas instead of text — dramatically cheaper and 
capable of producing insights text-based systems cannot express. A Shadow Self governance layer 
translates all machine communication to human-readable audit logs in real time.

Current proven results:
- Fidelity 1.0000 at 24x compression on Phi-3 Mini 3.8B
- Divergence score 2.0/2 on all exchanges
- 45% Brier score improvement vs naive baseline on 18 resolved Polymarket markets (0.1376 vs 0.25)
- 7+ consecutive days of AI regulation divergence (swarm 21-28% vs crowd 31%)
- 30-day paper trading clock running (Day 3)
- Mac Mini M4 Pro arriving April 9-16 for first latent vs text A/B test
- M5 Mac Studio 128GB arriving June/July for full 4-arm benchmark

Calibration status: {calibration}

Prior commercialization thesis:
{prior_thesis}

Today's research digest highlights:
{digest}

Compression researcher suggestions:
{suggestions}

Founder Engine inputs (signals from X, GitHub, articles):
{founder_inputs}

---

LOCKED DECISIONS - DO NOT REVISIT THESE:
- Rain grant: PARKED until Mac Mini latent vs text A/B results exist. Do not recommend submitting it.
- Public dashboard: Target is May 7 (Day 30). Do not recommend building it earlier.
- Bayesian Updater: Dropped April 12. Swarm is now 3 agents (Macro, Quant, Contrarian).

---

Your job: Think like a co-founder focused entirely on how LatentForge becomes a real business.

Produce:

1. PRIMARY STRATEGIC BET (one paragraph)
The single highest-conviction commercialization path right now. Be specific. Reference our actual results.

2. THESIS UPDATE (one paragraph)
How has your conviction changed since the prior thesis? What's stronger, what's weaker, what's new?

3. BUSINESS MODEL OPTIONS (3 options, ranked)
For each: name, how it works, why it fits LatentForge specifically, earliest possible revenue date.
Consider: protocol licensing, dataset moat sales, synthetic alpha fund, prediction market API, 
enterprise agent governance layer, research partnerships, PLG developer tools, etc.

4. PARTNERSHIP TARGETS (2-3 specific targets)
Who specifically should John be talking to right now? Name organizations or types of organizations.
What's the pitch to each? What do we offer them?

5. PRODUCT-LED GROWTH ANGLE
What's the smallest possible thing we could ship publicly that demonstrates value and pulls people in?
Must be achievable before Mac Studio arrives in June.

6. THIS WEEK'S ONE ACTION
The single highest-leverage commercialization action John can take in the next 7 days.

Be grounded in our actual results. No generic startup advice. Every recommendation must connect 
to something specific about latent communication, our Brier scores, or our governance layer."""

    response = CLIENT.messages.create(
        model=MODEL,
        max_tokens=4000,
        timeout=120,
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.content[0].text

    output = f"# LatentForge Commercialization Briefing — {date_str}\n\n"
    output += f"*Generated at {datetime.now().strftime('%H:%M')}*\n\n"
    output += result

    output_path.write_text(output, encoding="utf-8")
    print(f"Saved to {output_path}")

    # Update running thesis
    thesis_update = f"\n\n---\n## {date_str} Update\n\n{result[:1500]}"
    with open(THESIS_FILE, "a", encoding="utf-8") as f:
        f.write(thesis_update)
    print(f"Thesis updated at {THESIS_FILE}")

    print("\n--- PREVIEW ---")
    print(result[:800])

if __name__ == "__main__":
    main()