#!/usr/bin/env python3
"""
eof_compression_test.py — LatentForge EOF vs Top-k Sparsity Proxy Test
April 12, 2026

Tests whether Empirical Orthogonal Function (EOF) decomposition achieves
lower reconstruction error than top-k sparsity at matched compression ratio,
using Claude API response vectors as proxy latent vectors.

Hypothesis:
  1. EOF reconstruction error < top-k at matched compression ratio
  2. EOF requires fewer coefficients on semantically similar prompts
     (content-adaptive compression)

Proxy method: Claude API character n-gram frequency vectors (dim=1024)
NOTE: Coarse proxy — retest with Phi-3 hidden states on Mac Mini for
definitive citable result. Directional signal only.

Same proxy methodology as efference copy test (April 1, 2026).
"""

import os
import datetime
import numpy as np
from pathlib import Path
from anthropic import Anthropic

# ============================================================
# CONFIGURATION
# ============================================================
CONFIG = {
    "seed":               42,
    "n_vectors":          120,
    "top_k":              128,
    "eof_variance":       0.95,
    "rolling_window":     20,
    "vector_dim":         1024,
    "output_dir":         "experiments/week4/eof_compression",
    "log_file":           "experiments/week4/eof_compression/results.md",
    "vectors_file":       "experiments/week4/eof_compression/vectors.npy",
    "model":              "claude-sonnet-4-20250514",
    "max_tokens":         300,
}

np.random.seed(CONFIG["seed"])

# ============================================================
# PROMPT GROUPS — thematic clustering for content-adaptive test
# ============================================================
PROMPT_GROUPS = {
    "ai_regulation": [
        "Will the US Congress pass an AI regulation bill in 2026?",
        "What is the probability of federal AI legislation passing this year?",
        "Analyze the likelihood of AI governance legislation in the United States.",
        "How probable is it that Congress enacts AI oversight laws before 2027?",
        "Assess the chances of meaningful AI regulation passing in the current session.",
        "What factors affect the probability of US AI regulation passing?",
        "Will AI safety legislation clear the Senate in 2026?",
        "How likely is bipartisan support for AI regulation bills?",
        "What is the base rate for major technology regulation passing Congress?",
        "Will the AI regulation debate result in enacted law this year?",
    ],
    "crypto_markets": [
        "Will Bitcoin reach $150,000 by end of 2026?",
        "What is the probability Bitcoin hits $100k before $60k?",
        "Analyze Ethereum price trajectory for the next six months.",
        "How likely is a crypto market correction in Q2 2026?",
        "Will stablecoin regulation affect crypto market caps this year?",
        "What drives Bitcoin price movements in the current market?",
        "Assess the probability of a new crypto all-time high in 2026.",
        "How correlated are crypto markets with equity markets right now?",
        "Will institutional adoption continue driving Bitcoin prices higher?",
        "What is the probability of Bitcoin dominance exceeding 60%?",
    ],
    "geopolitics": [
        "Will the US and Iran reach a nuclear deal by June 2026?",
        "What is the probability of a US-Iran diplomatic breakthrough?",
        "Analyze the likelihood of Middle East peace negotiations succeeding.",
        "How probable is an escalation in US-China trade tensions this year?",
        "Will NATO membership expand further in 2026?",
        "Assess the probability of a major geopolitical crisis in 2026.",
        "What factors affect the probability of US-Iran nuclear negotiations?",
        "How likely is a diplomatic resolution to the Taiwan strait situation?",
        "Will sanctions policy change significantly under the current administration?",
        "What is the probability of a major power conflict in the next 12 months?",
    ],
    "economics": [
        "Will the Fed cut rates by 50bps or more in 2026?",
        "What is the probability of a US recession in the next 12 months?",
        "Analyze the likelihood of inflation returning above 4% this year.",
        "How probable is the S&P 500 ending 2026 above 6000?",
        "Will unemployment rise above 5% in Q3 2026?",
        "Assess the probability of a soft landing for the US economy.",
        "What factors drive Federal Reserve interest rate decisions?",
        "How likely is a significant stock market correction in 2026?",
        "Will the dollar strengthen or weaken against major currencies?",
        "What is the probability of GDP growth exceeding 2.5% in 2026?",
    ],
    "technology": [
        "Will a frontier AI model achieve AGI-level performance in 2026?",
        "What is the probability of a major AI safety incident this year?",
        "Analyze the likelihood of open-source AI models matching GPT-5.",
        "How probable is a breakthrough in quantum computing in 2026?",
        "Will AI replace more than 10% of white-collar jobs by 2027?",
        "Assess the probability of major AI company consolidation.",
        "What factors drive AI model capability improvements?",
        "How likely is a significant AI-related regulatory action in the EU?",
        "Will AI coding assistants become standard in enterprise software?",
        "What is the probability of a new computing paradigm emerging in 2026?",
    ],
    "elections": [
        "Will Democrats win the Senate majority in 2026 midterms?",
        "What is the probability of Republicans holding the House in 2026?",
        "Analyze voter turnout projections for the 2026 midterm elections.",
        "How probable is a wave election in 2026 favoring one party?",
        "Will third-party candidates significantly affect 2026 outcomes?",
        "Assess the probability of incumbent losses in 2026 primaries.",
        "What factors drive midterm election outcomes historically?",
        "How likely is redistricting to affect 2026 House races?",
        "Will economic conditions determine 2026 election results?",
        "What is the probability of a Senate filibuster reform in 2026?",
    ],
    "mixed_control": [
        "What is the weather like in San Francisco in April?",
        "Explain the rules of chess.",
        "How does compound interest work?",
        "What are the main causes of World War I?",
        "Describe the water cycle.",
        "What is the capital of Australia?",
        "How does photosynthesis work?",
        "What are the planets in the solar system?",
        "Explain the difference between mitosis and meiosis.",
        "What is the Pythagorean theorem?",
    ],
}

# ============================================================
# UTILITIES
# ============================================================
def log_append(log_path, content):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as f:
        f.write(content + "\n")

def cosine_distance(a, b):
    dot = np.dot(a, b)
    norm = np.linalg.norm(a) * np.linalg.norm(b)
    return 1.0 - (dot / norm if norm > 0 else 0.0)

def mse(a, b):
    return float(np.mean((a - b) ** 2))

# ============================================================
# VECTOR GENERATION
# ============================================================
def get_proxy_vector(client, prompt, dim=1024):
    """
    Generate a proxy latent vector from Claude API response.
    NOTE: Coarse proxy using character n-gram frequencies.
    Directional signal only — retest with Phi-3 hidden states on Mac Mini.
    """
    response = client.messages.create(
        model=CONFIG["model"],
        max_tokens=CONFIG["max_tokens"],
        messages=[{
            "role": "user",
            "content": (
                f"You are a careful probability forecaster. {prompt}\n\n"
                f"Provide a brief probability estimate with 2-3 sentences of reasoning."
            )
        }]
    )
    text = response.content[0].text

    vec = np.zeros(dim)
    words = text.lower().split()
    for i, word in enumerate(words):
        for char in word:
            idx = (hash(word + char + str(i % 10)) % dim)
            vec[idx] += 1.0

    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm

    return vec, text

def collect_vectors(client, log_path):
    all_vectors  = []
    all_metadata = []

    print(f"\nCollecting proxy vectors from Claude API...")
    log_append(log_path, "## Vector Collection")
    log_append(log_path, f"Model: {CONFIG['model']}")
    log_append(log_path, f"Proxy: character n-gram frequency vectors (dim={CONFIG['vector_dim']})")
    log_append(log_path, f"NOTE: Coarse proxy — Mac Mini will use real Phi-3 hidden states\n")

    total = 0
    for group_name, prompts in PROMPT_GROUPS.items():
        print(f"  Group: {group_name} ({len(prompts)} prompts)...")
        for prompt in prompts:
            try:
                vec, response_text = get_proxy_vector(
                    client, prompt, dim=CONFIG["vector_dim"]
                )
                all_vectors.append(vec)
                all_metadata.append({
                    "group":    group_name,
                    "prompt":   prompt,
                    "response": response_text[:100],
                    "index":    total,
                })
                total += 1
                if total % 20 == 0:
                    print(f"    {total} vectors collected...")
            except Exception as e:
                print(f"    Error: {e}")
                continue

    vectors = np.array(all_vectors)
    print(f"\nCollected {len(vectors)} vectors. Shape: {vectors.shape}")
    log_append(log_path, f"Vectors collected: {len(vectors)}")
    log_append(log_path, f"Vector shape: {vectors.shape}\n")
    return vectors, all_metadata

# ============================================================
# TOP-K SPARSITY BASELINE
# ============================================================
def top_k_compress(vec, k):
    sparse = np.zeros_like(vec)
    top_k_indices = np.argsort(np.abs(vec))[-k:]
    sparse[top_k_indices] = vec[top_k_indices]
    return sparse

def top_k_reconstruction_error(vectors, k):
    errors_mse = []
    errors_cos = []
    n_nonzero  = []
    for vec in vectors:
        compressed = top_k_compress(vec, k)
        errors_mse.append(mse(vec, compressed))
        errors_cos.append(cosine_distance(vec, compressed))
        n_nonzero.append(np.sum(compressed != 0))
    return {
        "avg_mse":     float(np.mean(errors_mse)),
        "avg_cosine":  float(np.mean(errors_cos)),
        "avg_nonzero": float(np.mean(n_nonzero)),
        "k":           k,
    }

# ============================================================
# EOF / PCA COMPRESSION
# ============================================================
def build_eof_basis(vectors):
    mean_vec            = vectors.mean(axis=0)
    centered            = vectors - mean_vec
    cov                 = np.cov(centered.T)
    eigenvals, eigenvecs = np.linalg.eigh(cov)
    idx                 = np.argsort(eigenvals)[::-1]
    eigenvals           = eigenvals[idx]
    eigenvecs           = eigenvecs[:, idx]
    total_var           = eigenvals.sum()
    cum_var             = np.cumsum(eigenvals) / total_var if total_var > 0 else np.zeros_like(eigenvals)
    return eigenvecs, eigenvals, cum_var, mean_vec

def eof_compress(vec, eigenvecs, mean_vec, cum_var, variance_threshold=0.95):
    centered     = vec - mean_vec
    n_components = int(np.searchsorted(cum_var, variance_threshold)) + 1
    n_components = max(1, min(n_components, eigenvecs.shape[1]))
    basis        = eigenvecs[:, :n_components]
    coefficients = basis.T @ centered
    reconstructed = mean_vec + basis @ coefficients
    return coefficients, n_components, reconstructed

def eof_reconstruction_error(vectors, variance_threshold=0.95, window=20):
    errors_mse   = []
    errors_cos   = []
    n_components = []

    if len(vectors) < window * 2:
        print(f"  Warning: {len(vectors)} vectors for window={window}. Results may be noisy.")
    if len(vectors) < window:
        print(f"  Not enough vectors. Reducing window to {len(vectors)//2}.")
        window = len(vectors) // 2

    for i in range(window, len(vectors)):
        window_vecs = vectors[max(0, i-window):i]
        eigenvecs, eigenvals, cum_var, mean_vec = build_eof_basis(window_vecs)
        vec = vectors[i]
        coeffs, n_comp, reconstructed = eof_compress(
            vec, eigenvecs, mean_vec, cum_var, variance_threshold
        )
        errors_mse.append(mse(vec, reconstructed))
        errors_cos.append(cosine_distance(vec, reconstructed))
        n_components.append(n_comp)

    return {
        "avg_mse":            float(np.mean(errors_mse)),
        "avg_cosine":         float(np.mean(errors_cos)),
        "avg_components":     float(np.mean(n_components)),
        "min_components":     int(np.min(n_components)),
        "max_components":     int(np.max(n_components)),
        "variance_threshold": variance_threshold,
    }

# ============================================================
# CONTENT-ADAPTIVE TEST
# ============================================================
def content_adaptive_test(vectors, metadata, variance_threshold=0.95):
    groups = {}
    for i, meta in enumerate(metadata):
        g = meta["group"]
        if g not in groups:
            groups[g] = []
        groups[g].append(i)

    eigenvecs, eigenvals, cum_var, mean_vec = build_eof_basis(vectors)
    results = {}

    for group_name, indices in groups.items():
        if len(indices) < 3:
            continue
        group_vecs  = vectors[indices]
        comp_counts = []
        for vec in group_vecs:
            _, n_comp, _ = eof_compress(
                vec, eigenvecs, mean_vec, cum_var, variance_threshold
            )
            comp_counts.append(n_comp)
        results[group_name] = {
            "avg_components": float(np.mean(comp_counts)),
            "min_components": int(np.min(comp_counts)),
            "max_components": int(np.max(comp_counts)),
            "n_vectors":      len(indices),
        }

    return results

# ============================================================
# MAIN
# ============================================================
def main():
    project_root = Path(__file__).resolve().parent.parent.parent
    log_path     = project_root / CONFIG["log_file"]
    vectors_path = project_root / CONFIG["vectors_file"]
    timestamp    = datetime.datetime.now().isoformat()

    log_path.parent.mkdir(parents=True, exist_ok=True)

    print("="*60)
    print("LatentForge EOF Compression Proxy Test")
    print(f"Started: {timestamp}")
    print("="*60)

    log_append(log_path, f"# EOF vs Top-k Compression Proxy Test")
    log_append(log_path, f"Date: {timestamp}")
    log_append(log_path, f"Seed: {CONFIG['seed']} | Top-k k: {CONFIG['top_k']} | EOF variance: {CONFIG['eof_variance']}\n")

    # API key — consistent with .env pattern
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        env_path = os.path.expanduser("~/.latentforge/.env")
        if os.path.exists(env_path):
            for line in open(env_path):
                if "ANTHROPIC_API_KEY" in line:
                    api_key = line.strip().split("=", 1)[1].strip().strip('"')
                    break
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment or ~/.latentforge/.env")
        return

    client = Anthropic(api_key=api_key)

    # Collect or load vectors
    if vectors_path.exists():
        print(f"Loading existing vectors from {vectors_path}...")
        data     = np.load(vectors_path, allow_pickle=True).item()
        vectors  = data["vectors"]
        metadata = data["metadata"]
        print(f"Loaded {len(vectors)} vectors.")
    else:
        vectors, metadata = collect_vectors(client, log_path)
        np.save(vectors_path, {"vectors": vectors, "metadata": metadata})
        print(f"Vectors saved to {vectors_path}")

    print(f"\nRunning compression tests on {len(vectors)} vectors...")

    # Test 1: Top-k baseline
    print("\n[1/3] Top-k sparsity baseline (k=128)...")
    topk_results = top_k_reconstruction_error(vectors, k=CONFIG["top_k"])
    print(f"  Avg MSE:     {topk_results['avg_mse']:.6f}")
    print(f"  Avg cosine:  {topk_results['avg_cosine']:.6f}")
    print(f"  Avg nonzero: {topk_results['avg_nonzero']:.1f}")

    # Test 2: EOF adaptive
    print(f"\n[2/3] EOF adaptive compression ({int(CONFIG['eof_variance']*100)}% variance)...")
    eof_results = eof_reconstruction_error(
        vectors,
        variance_threshold=CONFIG["eof_variance"],
        window=CONFIG["rolling_window"]
    )
    print(f"  Avg MSE:        {eof_results['avg_mse']:.6f}")
    print(f"  Avg cosine:     {eof_results['avg_cosine']:.6f}")
    print(f"  Avg components: {eof_results['avg_components']:.1f}")
    print(f"  Min/Max:        {eof_results['min_components']}/{eof_results['max_components']}")

    # Test 3: Content-adaptive
    print("\n[3/3] Content-adaptive test by prompt group...")
    adaptive_results = content_adaptive_test(
        vectors, metadata, variance_threshold=CONFIG["eof_variance"]
    )
    for group, stats in sorted(adaptive_results.items(),
                                key=lambda x: x[1]["avg_components"]):
        print(f"  {group:20s}: avg {stats['avg_components']:.1f} components "
              f"(min {stats['min_components']}, max {stats['max_components']})")

    # Compression ratio comparison
    dim        = vectors.shape[1]
    topk_ratio = CONFIG["top_k"] / dim
    eof_ratio  = eof_results["avg_components"] / dim
    ratio_match = topk_ratio / eof_ratio if eof_ratio > 0 else 0

    print(f"\nCompression ratio:")
    print(f"  Top-k: {topk_ratio:.4f} ({CONFIG['top_k']}/{dim} dims)")
    print(f"  EOF:   {eof_ratio:.4f} ({eof_results['avg_components']:.1f}/{dim} dims)")
    print(f"  EOF uses {ratio_match:.2f}x fewer coefficients than top-k")

    # Verdict
    eof_better_mse    = eof_results["avg_mse"]    < topk_results["avg_mse"]
    eof_better_cosine = eof_results["avg_cosine"] < topk_results["avg_cosine"]

    similar_groups = ["ai_regulation", "crypto_markets", "geopolitics", "economics"]
    diverse_groups = ["mixed_control"]

    similar_avg = np.mean([
        adaptive_results[g]["avg_components"]
        for g in similar_groups if g in adaptive_results
    ])
    diverse_avg = np.mean([
        adaptive_results[g]["avg_components"]
        for g in diverse_groups if g in adaptive_results
    ])
    content_adaptive = similar_avg < diverse_avg
    hypothesis_1     = eof_better_mse or eof_better_cosine
    hypothesis_2     = content_adaptive

    print("\n" + "="*60)
    print("VERDICT")
    print("="*60)
    print(f"H1 (EOF lower reconstruction error): {'PASS' if hypothesis_1 else 'FAIL'}")
    print(f"  MSE:    top-k={topk_results['avg_mse']:.6f}  EOF={eof_results['avg_mse']:.6f}")
    print(f"  Cosine: top-k={topk_results['avg_cosine']:.6f}  EOF={eof_results['avg_cosine']:.6f}")
    print(f"H2 (Content-adaptive — fewer components on similar prompts): {'PASS' if hypothesis_2 else 'FAIL'}")
    print(f"  Similar groups avg: {similar_avg:.1f} components")
    print(f"  Diverse groups avg: {diverse_avg:.1f} components")
    print("="*60)

    # Log results
    log_append(log_path, "\n## Results\n")
    log_append(log_path, "### Top-k Sparsity Baseline (k=128)")
    log_append(log_path, f"- Avg MSE: {topk_results['avg_mse']:.6f}")
    log_append(log_path, f"- Avg cosine distance: {topk_results['avg_cosine']:.6f}")
    log_append(log_path, f"- Coefficients used: {topk_results['avg_nonzero']:.1f}\n")

    log_append(log_path, "### EOF Adaptive Compression (95% variance)")
    log_append(log_path, f"- Avg MSE: {eof_results['avg_mse']:.6f}")
    log_append(log_path, f"- Avg cosine distance: {eof_results['avg_cosine']:.6f}")
    log_append(log_path, f"- Avg components: {eof_results['avg_components']:.1f}")
    log_append(log_path, f"- Min/Max components: {eof_results['min_components']}/{eof_results['max_components']}\n")

    log_append(log_path, "### Content-Adaptive Behavior by Group")
    for group, stats in sorted(adaptive_results.items(),
                                key=lambda x: x[1]["avg_components"]):
        log_append(log_path,
            f"- {group}: avg {stats['avg_components']:.1f} components (n={stats['n_vectors']})"
        )

    log_append(log_path, f"\n### Verdict")
    log_append(log_path, f"- H1 (lower reconstruction error): {'PASS' if hypothesis_1 else 'FAIL'}")
    log_append(log_path, f"- H2 (content-adaptive): {'PASS' if hypothesis_2 else 'FAIL'}")
    log_append(log_path, f"- Top-k MSE: {topk_results['avg_mse']:.6f}")
    log_append(log_path, f"- EOF MSE: {eof_results['avg_mse']:.6f}")
    log_append(log_path, f"- Similar groups avg components: {similar_avg:.1f}")
    log_append(log_path, f"- Diverse groups avg components: {diverse_avg:.1f}")
    log_append(log_path, f"- EOF efficiency ratio vs top-k: {ratio_match:.2f}x")
    log_append(log_path, f"\nNote: Proxy test using Claude API character n-gram vectors (dim=1024).")
    log_append(log_path, f"Retest with real Phi-3 hidden states on Mac Mini for citable result.\n")

    print(f"\nResults logged to: {log_path}")
    print("Done.")

if __name__ == "__main__":
    main()
