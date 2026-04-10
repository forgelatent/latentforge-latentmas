# experiments/week1/scripts/revenue_strategist.py
"""
LATENTFORGE — Morning Revenue Strategist v0.3
Reads Kalshi data + research digest + BRAIN.md
Calls real Anthropic Claude API.
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path

# Paths
KALSHI_DIR = Path("~/Projects/data/kalshi").expanduser()
DIGEST_DIR = Path("~/Projects/latentforge-latentmas/research/daily-digest").expanduser()
BRAIN_PATH = Path("~/Projects/latentforge-latentmas/BRAIN.md").expanduser()
OUTPUT_DIR = Path("~/Projects/latentforge-latentmas/revenue_ideas").expanduser()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

def load_latest_file(directory, extension=".json"):
    if not directory.exists():
        return None, None
    files = sorted([f for f in directory.iterdir() if f.suffix == extension], key=lambda x: x.stat().st_mtime, reverse=True)
    if not files:
        return None, None
    latest = files[0]
    with open(latest, "r", encoding="utf-8") as f:
        return latest.name, f.read()

def load_brain_summary():
    if not BRAIN_PATH.exists():
        return "BRAIN.md not found."
    with open(BRAIN_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    sections = []
    for marker in ["## 1. THE THESIS", "## 3. 90-DAY GOALS", "## 4. WHAT WE ARE BUILDING"]:
        if marker in content:
            start = content.find(marker)
            end = content.find("## ", start + 1)
            if end == -1: end = len(content)
            sections.append(content[start:end].strip())
    return "\n\n".join(sections[:3])

def call_anthropic(prompt):
    if not ANTHROPIC_API_KEY:
        return "[ERROR: ANTHROPIC_API_KEY not set]"
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 4000,
                "temperature": 0.7,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["content"][0]["text"]
    except Exception as e:
        return f"[API Error: {str(e)[:200]}]"

def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = OUTPUT_DIR / f"{date_str}.md"

    kalshi_file, kalshi_data = load_latest_file(KALSHI_DIR)
    digest_file, digest_data = load_latest_file(DIGEST_DIR, ".md")
    brain_summary = load_brain_summary()

    # Read Founder Engine inputs
    FOUNDER_INPUTS_DIR = Path(os.path.expanduser("~/Projects/latentforge-latentmas/founder_inputs"))
    founder_notes = ""
    for file in sorted(FOUNDER_INPUTS_DIR.glob("*.md")):
        try:
            with open(file) as f:
                founder_notes += f.read() + "\n\n"
        except:
            pass

    print(f"Running Revenue Strategist for {date_str}...")
    print(f"Kalshi: {kalshi_file or 'None'}")
    print(f"Digest: {digest_file or 'None'}")

    prompt = f"""You are LatentForge's revenue strategist.

Our core advantage: AI agents communicate via raw latent vector deltas (hidden states) instead of lossy English/JSON. This enables lower compute and truly divergent thinking.

Today's inputs:
- Kalshi markets: {kalshi_data[:1800] if kalshi_data else "No data"}
- Research digest: {digest_data[:1200] if digest_data else "No data"}
- Thesis summary: {brain_summary}
- Founder Engine inputs: {founder_notes[:1000] if founder_notes else "None today"}

Generate 2–4 concrete, honest revenue opportunities for this week.
For each:
- Short name + realistic first-money timeline
- Specific edge from latent communication + divergence
- One actionable next step possible this week with current tools (MacBook, RunPod, OpenClaw, Anthropic API)

Be direct and grounded. Prioritize fast wins like Rain grant.

Output clean markdown."""

    result = call_anthropic(prompt)

    output = f"# LatentForge Revenue Ideas — {date_str}\n\n"
    output += f"*Generated at {datetime.now().strftime('%H:%M')} from Kalshi + research digest*\n\n"
    output += result

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\n✅ Saved to {output_path}")
    print("\n--- PREVIEW (first 700 chars) ---")
    print(result[:700])

if __name__ == "__main__":
    main()

