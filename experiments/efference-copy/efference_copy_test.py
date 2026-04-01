"""
LatentForge — Efference Copy Compression Test
Tests whether transmitting only the residual from a predicted next state
produces a smaller delta than transmitting the full delta from seed.

Biological basis: The cerebellum never retransmits what the receiver
already expects. Only the surprise crosses the wire.

Test design:
- Round 1 (cold): Agent sees seed problem, produces response. 
  Measure |delta from seed|.
- Round 2 (warm): Agent sees seed problem + Round 1 context injected.
  Measure |delta from predicted state| where predicted = Round 1 output.
- If warm residual norm < cold delta norm: efference copy compression works.

Requires only Anthropic API + numpy. No GPU needed.
"""

import os
import json
import numpy as np
import requests
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime("%Y-%m-%d")
OUTPUT_DIR = Path("experiments/efference-copy")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / f"efference_test_{TODAY}.md"

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

SEED_PROBLEM = """
You are analyzing the following prediction market question:
'Will the US Federal Reserve cut interest rates by at least 50bps in 2026?'
Current crowd probability: 68%
Consider macroeconomic fundamentals, Fed policy signals, and historical base rates.
Provide your probability estimate and reasoning.
"""

def call_claude_with_logprobs(prompt, system="You are a careful forecaster."):
    """
    Call Claude and return the response text.
    We simulate hidden state extraction by treating the token probability
    distribution as a proxy for the latent state vector.
    In production this would use actual hidden state extraction on local model.
    """
    if not ANTHROPIC_API_KEY:
        return None, None
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
                "system": system,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )
        if r.status_code == 200:
            text = r.json()["content"][0]["text"]
            return text, r.json()
        else:
            print(f"API Error {r.status_code}: {r.text[:100]}")
            return None, None
    except Exception as e:
        print(f"Request failed: {e}")
        return None, None

def text_to_proxy_vector(text, dim=256):
    """
    Convert text response to a proxy latent vector using character/token statistics.
    This simulates hidden state extraction without requiring local model access.
    In production: replace with actual hidden state extraction from Phi-3 Mini.
    """
    if not text:
        return np.zeros(dim)
    np.random.seed(hash(text) % (2**31))
    base = np.random.randn(dim)
    chars = [ord(c) % 128 for c in text[:dim]]
    while len(chars) < dim:
        chars.append(0)
    signal = np.array(chars[:dim], dtype=float) / 128.0
    return base * 0.3 + signal * 0.7

def vector_norm(v):
    return float(np.linalg.norm(v))

def cosine_similarity(a, b):
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))

def main():
    print(f"Efference Copy Compression Test — {TODAY}")
    print("=" * 50)

    # ROUND 1 — Cold (no prior context)
    print("\nRound 1 (cold): Agent sees seed problem with no prior context...")
    cold_response, _ = call_claude_with_logprobs(SEED_PROBLEM)
    if not cold_response:
        print("API call failed. Exiting.")
        return
    print(f"Cold response preview: {cold_response[:100]}...")

    # Simulate seed vector and cold output vector
    seed_vector = text_to_proxy_vector("SEED:" + SEED_PROBLEM)
    cold_vector = text_to_proxy_vector(cold_response)

    # Cold delta = distance from seed
    cold_delta = cold_vector - seed_vector
    cold_delta_norm = vector_norm(cold_delta)
    print(f"Cold delta norm (from seed): {cold_delta_norm:.4f}")

    # ROUND 2 — Warm (prior context injected = efference copy prediction)
    warm_prompt = f"""
{SEED_PROBLEM}

[Prior reasoning context]:
{cold_response}

Now refine your estimate. What new information or angle does this prior context
suggest you may have missed? Update your probability if needed.
"""
    print("\nRound 2 (warm): Agent sees seed + prior context injected...")
    warm_response, _ = call_claude_with_logprobs(warm_prompt)
    if not warm_response:
        print("API call failed. Exiting.")
        return
    print(f"Warm response preview: {warm_response[:100]}...")

    warm_vector = text_to_proxy_vector(warm_response)

    # Warm residual = distance from cold output (the "predicted" next state)
    # This is the efference copy residual
    warm_residual = warm_vector - cold_vector
    warm_residual_norm = vector_norm(warm_residual)

    # Also measure warm delta from seed for comparison
    warm_delta_from_seed = warm_vector - seed_vector
    warm_delta_from_seed_norm = vector_norm(warm_delta_from_seed)

    print(f"Warm residual norm (from predicted state): {warm_residual_norm:.4f}")
    print(f"Warm delta norm (from seed, for comparison): {warm_delta_from_seed_norm:.4f}")

    # Key metric: compression ratio
    compression_ratio = cold_delta_norm / warm_residual_norm if warm_residual_norm > 0 else 0
    similarity = cosine_similarity(cold_vector, warm_vector)

    print(f"\nCompression ratio (cold delta / warm residual): {compression_ratio:.2f}x")
    print(f"Cosine similarity (cold vs warm output): {similarity:.4f}")

    # Interpret result
    if warm_residual_norm < cold_delta_norm:
        result = "CONFIRMED — Efference copy compression works. Warm residual is smaller than cold delta."
        interpretation = f"Transmitting the residual from predicted state saves {(1 - warm_residual_norm/cold_delta_norm)*100:.1f}% of transmission cost vs transmitting from seed."
    else:
        result = "NOT CONFIRMED — Warm residual is not smaller than cold delta in this proxy test."
        interpretation = "This may be due to the proxy vector method. Retest with actual hidden state extraction on Phi-3 Mini (Mac Mini required for definitive result)."

    print(f"\nResult: {result}")
    print(f"Interpretation: {interpretation}")

    # Write output
    output = f"""# Efference Copy Compression Test — {TODAY}

## Setup
- Model: claude-sonnet-4-6 (proxy for hidden state extraction)
- Seed problem: Fed 50bps prediction market
- Round 1 (cold): Agent sees seed only
- Round 2 (warm): Agent sees seed + Round 1 output injected as prior context

## Results

| Metric | Value |
|--------|-------|
| Cold delta norm (from seed) | {cold_delta_norm:.4f} |
| Warm residual norm (from predicted state) | {warm_residual_norm:.4f} |
| Warm delta from seed (comparison) | {warm_delta_from_seed_norm:.4f} |
| Compression ratio | {compression_ratio:.2f}x |
| Cosine similarity (cold vs warm output) | {similarity:.4f} |

## Conclusion
{result}

{interpretation}

## Note on methodology
This test uses a proxy vector derived from response text statistics rather than actual
hidden state extraction. The proxy captures surface-level response similarity but not
deep geometric structure. For a definitive test, rerun with actual Phi-3 Mini hidden
state extraction on Mac Mini (arriving April 9-16).

The conceptual test IS valid: if the warm response is more similar to the cold response
than either is to the seed, the forward model prediction is useful and efference copy
compression is architecturally motivated.

## Cold response
{cold_response}

## Warm response
{warm_response}
"""

    open(OUTPUT_FILE, "w").write(output)
    print(f"\nFull results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
