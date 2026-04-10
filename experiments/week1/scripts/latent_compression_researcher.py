"""
LatentForge — Latent Compression Researcher Agent
Runs nightly at 2 AM. Reads today's research digest + BRAIN.md and generates
2-4 concrete compression/latent space suggestions from adjacent fields.
Output: research/suggestions/YYYY-MM-DD.md
"""

import os
import requests
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime("%Y-%m-%d")
DIGEST_DIR = Path("research/daily-digest")
SUGGESTIONS_DIR = Path("/Users/latentforge/Projects/latentforge-latentmas/research/suggestions")
SUGGESTIONS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = SUGGESTIONS_DIR / f"{TODAY}.md"
BRAIN_PATH = Path("BRAIN.md")

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

SYSTEM_PROMPT = """You are a specialist research collaborator for LatentForge, an AI startup building latent vector delta communication between agents.

Your expertise spans: information theory, compression algorithms, differential geometry, topology, neuroscience, genomics, signal processing, quantum information, and biological systems.

Your job is NOT to summarize papers. Your job is to identify techniques from any field — including nature and biology — that could improve how LatentForge compresses and transmits latent vector deltas between AI agents.

LatentForge context:
- Agents communicate by passing compressed hidden state vectors (latent deltas) instead of text
- Current compression: top-k sparsity (k=128, 24x compression, divergence holds)
- Core challenge: compress the latent space efficiently while preserving useful divergence signal
- Shared seed vector acts as common reference point between agents
- Shadow Self layer monitors drift and provides governance
- Target: injective (lossless for domain), domain-adaptive, biologically-inspired compression

For each suggestion, use EXACTLY this format:

---
SUGGESTION [N]
Technique: [name of the technique]
Field: [field it comes from]
Core idea: [one sentence — what does this technique do]
Why LatentForge: [one paragraph — how does this apply to latent delta compression specifically]
Test in one week: [concrete implementation step possible on MacBook + Anthropic API, no GPU required]
Novelty: [1-5, where 5 = nobody in latent agent communication is doing this]
Feasibility: [1-5, where 5 = can be tested on MacBook this week]
---

Generate exactly 3 suggestions. Prioritize ideas that are:
1. Novel — not already in the LatentMAS or AVP literature
2. Biologically-inspired or cross-disciplinary
3. Testable without the Mac Mini (arriving April 9-16)

Do not pad. Do not summarize. Only concrete, actionable suggestions."""


def load_latest_digest():
    files = sorted(DIGEST_DIR.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
    if not files:
        return "No digest available."
    return open(files[0]).read()[:3000]


def load_brain_summary():
    if not BRAIN_PATH.exists():
        return "BRAIN.md not found."
    content = open(BRAIN_PATH).read()
    sections = []
    for marker in ["## 1. THE THESIS", "## 4. WHAT WE ARE BUILDING", "## 11. ARCHITECTURE DECISIONS"]:
        if marker in content:
            start = content.find(marker)
            end = content.find("## ", start + 1)
            if end == -1:
                end = start + 2000
            sections.append(content[start:min(end, start+2000)])
    return "\n\n".join(sections[:3])


def call_claude(prompt):
    if not ANTHROPIC_API_KEY:
        return "ERROR: ANTHROPIC_API_KEY not set."
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
                "max_tokens": 4000,
                "system": SYSTEM_PROMPT,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=120
        )
        if r.status_code == 200:
            return r.json()["content"][0]["text"]
        else:
            return f"API Error {r.status_code}: {r.text[:200]}"
    except Exception as e:
        return f"Request failed: {e}"


def main():
    digest = load_latest_digest()
    brain = load_brain_summary()

    prompt = f"""Today's research digest (arXiv + GitHub activity):

{digest}

Current LatentForge architecture summary:

{brain}

Based on this context, generate 3 concrete compression/latent space suggestions from adjacent fields that LatentForge should explore. Focus especially on biological systems, information theory, and geometric approaches that nobody in the latent agent communication space is currently using."""

    print(f"Running Latent Compression Researcher for {TODAY}...")
    result = call_claude(prompt)

    output = f"# Latent Compression Research Suggestions — {TODAY}\n\n"
    output += f"*Generated at {datetime.now().strftime('%H:%M')} by compression researcher agent*\n\n"
    output += result

    open(OUTPUT_FILE, "w").write(output)
    print(f"Saved to {OUTPUT_FILE}")
    print("\n--- PREVIEW (first 800 chars) ---")
    print(result[:800])


if __name__ == "__main__":
    main()
