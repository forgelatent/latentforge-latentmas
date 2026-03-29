# experiments/benchmark/02_text_baseline.py
"""
Text Baseline Estimator v2 — Fixed model name + better error handling
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime("%Y-%m-%d")
BENCHMARK_DIR = Path("experiments/benchmark").expanduser()
MARKETS_FILE = BENCHMARK_DIR / f"markets_{TODAY}.md"
OUTPUT_FILE = BENCHMARK_DIR / f"text_baseline_{TODAY}.md"

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

def load_markets():
    if not MARKETS_FILE.exists():
        print(f"Markets file not found: {MARKETS_FILE}")
        return None
    with open(MARKETS_FILE, "r", encoding="utf-8") as f:
        return f.read()

def call_claude_for_probabilities(markets_text):
    if not ANTHROPIC_API_KEY:
        return "ERROR: ANTHROPIC_API_KEY environment variable not set."

    prompt = f"""You are a well-calibrated prediction market forecaster.

Here are today's benchmark markets:

{markets_text}

For each market, provide your best probability estimate for the "Yes" outcome as a percentage (0-100).
Be concise but honest about uncertainty.

Format exactly like this for each market:

### 1. [Full Market Question]
- Text-only probability (Yes): XX%
- Reasoning: [1-2 sentence reasoning]

Do this for all markets listed."""

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-6",   # Try this first
                "max_tokens": 1000,
                "temperature": 0.5,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json()["content"][0]["text"]
        else:
            error_msg = response.json() if response.text else response.text
            return f"API Error {response.status_code}: {error_msg}"

    except Exception as e:
        return f"Request failed: {str(e)}"

def main():
    markets_text = load_markets()
    if not markets_text:
        return

    print("Calling Claude for text baseline probabilities...")

    claude_output = call_claude_for_probabilities(markets_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Text Baseline Estimates — {TODAY}\n\n")
        f.write("Text-only Claude predictions for today's benchmark markets.\n\n")
        f.write(claude_output)

    print(f"✅ Text baseline saved to {OUTPUT_FILE}")
    print("\n--- PREVIEW (first 600 characters) ---")
    print(claude_output[:600])

if __name__ == "__main__":
    main()
