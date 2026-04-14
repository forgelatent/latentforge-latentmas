#!/usr/bin/env python3
"""
echo_test.py — LatentForge Latent Echo Test v2.1
Pre-registered April 11, 2026. Part of Mac Mini A/B Experiment Spec v2.0.

Architecture:
  Fidelity measurement: Phi-3 LM head projection (same-model reconstruction)
  Governance layer:     TinyLlama (human-readable audit summaries)

Two modes:
  pre-gate:    3 markets, must score >=0.95 on all 3 to PASS
  continuous:  log fidelity per exchange during full benchmark runs
"""

import os
import json
import datetime
import argparse
import sys
import torch
import numpy as np
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer, util

# ============================================================
# CONFIGURATION — locked per v2.0 spec
# ============================================================
CONFIG = {
    "agent_model":           "microsoft/Phi-3-mini-4k-instruct",
    "shadow_model":          "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "similarity_model":      "all-MiniLM-L6-v2",
    "sparsity_k":            128,
    "temperature":           0.0,
    "seed":                  42,
    "pass_threshold":        0.95,
    "safe_mode_threshold":   0.90,
    "runaway_threshold":     0.75,
    "lm_head_top_k":         50,     # tokens to decode from LM head projection
    "warmup_passes":         5,      # forward passes to initialize seed vector
    "echo_log":              "experiments/week4/echo_log.md",
    "seed_vector_path":      "experiments/week4/seed_vector.pt",
}

TEST_MARKETS = [
    {
        "id": "ai_regulation",
        "question": "Will an AI regulation bill pass in US Congress before end of 2026?",
        "crowd_prob": 0.31,
    },
    {
        "id": "us_iran_deal",
        "question": "Will the US and Iran reach a nuclear deal by June 30, 2026?",
        "crowd_prob": 0.225,
    },
    {
        "id": "bitcoin_target",
        "question": "Will Bitcoin reach $60,000 or $80,000 first?",
        "crowd_prob": 0.65,
    },
]

# ============================================================
# UTILITIES
# ============================================================
def set_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def get_device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    elif torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")

def clear_cache(device):
    if device.type == "mps":
        torch.mps.empty_cache()
    elif device.type == "cuda":
        torch.cuda.empty_cache()

def top_k_sparsity(delta, k):
    flat = delta.squeeze()
    sparse = torch.zeros_like(flat)
    k = min(k, flat.shape[-1])
    topk_indices = torch.topk(flat.abs(), k=k).indices
    sparse[topk_indices] = flat[topk_indices]
    return sparse

def compute_delta(hidden_state, seed_vector):
    return hidden_state - seed_vector

def reconstruct(delta, seed_vector):
    return seed_vector + delta

def log_append(log_path, content):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as f:
        f.write(content + "\n")

# ============================================================
# MODEL LOADING
# ============================================================
def load_agent(device):
    print("Loading Agent (Phi-3 Mini 3.8B)...")
    if device.type == "mps":
        model = AutoModelForCausalLM.from_pretrained(
            CONFIG["agent_model"],
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True,
        )
    else:
        from transformers import BitsAndBytesConfig
        bnb = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16
        )
        model = AutoModelForCausalLM.from_pretrained(
            CONFIG["agent_model"],
            quantization_config=bnb,
            device_map="auto",
            trust_remote_code=True,
        )
    tokenizer = AutoTokenizer.from_pretrained(
        CONFIG["agent_model"],
        trust_remote_code=True
    )
    print(f"Agent loaded. Hidden dim: {model.config.hidden_size}")
    return model, tokenizer

def load_shadow(device):
    print("Loading Shadow Self (TinyLlama 1.1B)...")
    model = AutoModelForCausalLM.from_pretrained(
        CONFIG["shadow_model"],
        torch_dtype=torch.float16,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(CONFIG["shadow_model"])
    print("Shadow Self loaded.")
    return model, tokenizer

def load_similarity_model():
    print("Loading similarity model...")
    model = SentenceTransformer(CONFIG["similarity_model"])
    print("Similarity model loaded.")
    return model

# ============================================================
# SEED VECTOR INITIALIZATION
# Warm start from multiple forward passes — not zeros
# ============================================================
def initialize_seed_vector(agent_model, agent_tok, device, n_passes=None):
    if n_passes is None:
        n_passes = CONFIG["warmup_passes"]

    print(f"Initializing seed vector from {n_passes} warmup passes...")
    warmup_prompts = [
        "Analyze the current state of US economic policy.",
        "What factors affect cryptocurrency prices?",
        "How does geopolitical risk affect prediction markets?",
        "Assess the probability of major legislation passing.",
        "Evaluate market consensus on regulatory outcomes.",
    ][:n_passes]

    hidden_states = []
    for prompt in warmup_prompts:
        inputs = agent_tok(prompt, return_tensors="pt").to(device)
        with torch.no_grad():
            outputs = agent_model(
                **inputs,
                output_hidden_states=True,
                return_dict=True,
            )
        last_layer = outputs.hidden_states[-1]
        last_token = last_layer[0, -1, :].float().cpu()
        hidden_states.append(last_token)
        clear_cache(device)

    seed = torch.stack(hidden_states).mean(dim=0)
    print(f"Seed vector initialized. Norm: {seed.norm().item():.4f}")
    return seed

# ============================================================
# CORE: AGENT REASONING + HIDDEN STATE EXTRACTION
# ============================================================
def agent_reason(model, tokenizer, market, device):
    msg = 'You are a careful probability forecaster. Analyze this prediction market:\n\nMarket: ' + market['question'] + '\nCurrent crowd probability: ' + f"{market['crowd_prob']*100:.1f}" + '%\n\nProvide your reasoning and probability estimate in 2-3 sentences.'
    chat = [{"role": "user", "content": msg}]
    prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=False,
            output_hidden_states=True,
            return_dict_in_generate=True,
        )

    gen_ids = outputs.sequences[0][inputs.input_ids.shape[1]:]
    reasoning = tokenizer.decode(gen_ids, skip_special_tokens=True).strip()

    # Extract hidden state via direct forward pass (use_cache=False required)
    with torch.no_grad():
        fwd = model(
            **{k: v for k,v in inputs.items()},
            output_hidden_states=True,
            return_dict=True,
            use_cache=False
        )
    last_token = fwd.hidden_states[-1][0, -1, :]
    hidden_state = last_token.float().cpu()

    return reasoning, hidden_state

# ============================================================
# FIDELITY DECODE — Phi-3 LM head projection
# Measures what Phi-3 would generate from the reconstructed state.
# This is the direct fidelity signal — no TinyLlama involved.
# ============================================================
def lm_head_decode(agent_model, agent_tok, reconstructed_state, device):
    """
    Project reconstructed hidden state through Phi-3's own LM head.
    Returns decoded text representing what the model would generate
    from this state — a direct measure of semantic preservation.
    """
    reconstructed = reconstructed_state.to(device).to(torch.float16)

    with torch.no_grad():
        logits = agent_model.lm_head(
            reconstructed.unsqueeze(0).unsqueeze(0)
        )

    probs = torch.softmax(logits[0, 0, :], dim=-1)
    top_tokens = torch.topk(probs, k=CONFIG["lm_head_top_k"])

    token_texts = [
        agent_tok.decode([idx.item()])
        for idx in top_tokens.indices
    ]
    decoded = " ".join(t.strip() for t in token_texts if t.strip())
    return decoded

# ============================================================
# GOVERNANCE DECODE — TinyLlama audit summary
# Produces human-readable audit log from decoded tokens.
# Separate from fidelity measurement.
# ============================================================
def governance_decode(shadow_model, shadow_tok, decoded_tokens, market, device):
    """
    TinyLlama translates decoded token fingerprint into a human-readable
    audit summary. This is the Shadow Self governance layer.
    Fidelity is NOT measured against this output.
    """
    prompt = (
        f"You are a governance AI producing audit logs for AI agent communication.\n\n"
        f"Market being analyzed: {market['question']}\n\n"
        f"Agent signal tokens: {decoded_tokens[:200]}\n\n"
        f"Summarize what this agent is reasoning about this market in 2-3 sentences. "
        f"Include its apparent probability assessment and key factors."
    )
    inputs = shadow_tok(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = shadow_model.generate(
            **inputs,
            max_new_tokens=120,
            do_sample=False,
        )
    gen_ids = outputs[0][inputs.input_ids.shape[1]:]
    return shadow_tok.decode(gen_ids, skip_special_tokens=True).strip()

# ============================================================
# SIMILARITY
# ============================================================
def semantic_similarity(sim_model, text1, text2):
    e1 = sim_model.encode(text1, convert_to_tensor=True)
    e2 = sim_model.encode(text2, convert_to_tensor=True)
    return util.cos_sim(e1, e2).item()

def hidden_state_similarity(h1, h2):
    return torch.nn.functional.cosine_similarity(
        h1.unsqueeze(0), h2.unsqueeze(0)
    ).item()

# ============================================================
# PRE-GATE TEST
# ============================================================
def run_pre_gate(agent_model, agent_tok, shadow_model, shadow_tok,
                 sim_model, device, project_root):
    log_path  = project_root / CONFIG["echo_log"]
    seed_path = project_root / CONFIG["seed_vector_path"]
    timestamp = datetime.datetime.now().isoformat()

    print("\n" + "="*60)
    print("LATENT ECHO TEST — PRE-GATE v2.1")
    print("Fidelity: Phi-3 LM head | Governance: TinyLlama")
    print("="*60)

    log_append(log_path, f"\n## Echo Test Pre-Gate v2.1 — {timestamp}")
    log_append(log_path, f"Threshold: {CONFIG['pass_threshold']} | Markets: {len(TEST_MARKETS)}")
    log_append(log_path, f"Decode method: Phi-3 LM head projection\n")

    # Warm-start seed vector
    seed_vector = initialize_seed_vector(agent_model, agent_tok, device)
    clear_cache(device)

    results = []

    for i, market in enumerate(TEST_MARKETS):
        print(f"\nMarket {i+1}/3: {market['question'][:60]}...")

        # Agent A: reason + extract hidden state
        reasoning, hidden_state = agent_reason(agent_model, agent_tok, market, device)
        print(f"  Reasoning: {reasoning[:80]}...")
        clear_cache(device)

        # Compute delta + sparsify
        delta        = compute_delta(hidden_state, seed_vector)
        sparse_delta = top_k_sparsity(delta, CONFIG["sparsity_k"])
        sparsity     = (sparse_delta != 0).float().mean().item()

        # Reconstruct
        reconstructed = reconstruct(sparse_delta, seed_vector)

        # Hidden state fidelity (cosine)
        hs_sim = hidden_state_similarity(hidden_state, reconstructed)

        # FIDELITY: LM head decode + similarity
        decoded_tokens = lm_head_decode(agent_model, agent_tok, reconstructed, device)
        sem_sim        = semantic_similarity(sim_model, reasoning, decoded_tokens)
        clear_cache(device)

        # GOVERNANCE: TinyLlama audit summary (separate — not used for scoring)
        audit_summary = governance_decode(
            shadow_model, shadow_tok, decoded_tokens, market, device
        )
        clear_cache(device)

        passed = hs_sim >= CONFIG["pass_threshold"]
        status = "PASS" if passed else "FAIL"

        print(f"  Hidden sim:   {hs_sim:.4f}")
        print(f"  Semantic sim: {sem_sim:.4f} [{status}]")
        print(f"  Audit:        {audit_summary[:80]}...")

        results.append({
            "market_id":               market["id"],
            "reasoning":               reasoning,
            "decoded_tokens":          decoded_tokens,
            "audit_summary":           audit_summary,
            "hidden_state_similarity": hs_sim,
            "semantic_similarity":     sem_sim,
            "sparsity_ratio":          sparsity,
            "passed":                  passed,
        })

        log_append(log_path, f"### Market {i+1}: {market['id']}")
        log_append(log_path, f"- Question: {market['question']}")
        log_append(log_path, f"- Agent reasoning (truncated): {reasoning[:200]}")
        log_append(log_path, f"- LM head decoded tokens: {decoded_tokens[:200]}")
        log_append(log_path, f"- Audit summary (TinyLlama): {audit_summary[:200]}")
        log_append(log_path, f"- Hidden state similarity: {hs_sim:.4f}")
        log_append(log_path, f"- Semantic similarity (fidelity): {sem_sim:.4f}")
        log_append(log_path, f"- Sparsity ratio (k={CONFIG['sparsity_k']}): {sparsity:.4f}")
        log_append(log_path, f"- Status: {status}\n")

        # Update seed: rolling average
        seed_vector = 0.9 * seed_vector + 0.1 * hidden_state.detach()

    # Verdict
    all_passed = all(r["passed"] for r in results)
    avg_sim    = sum(r["hidden_state_similarity"] for r in results) / len(results)
    min_sim    = min(r["hidden_state_similarity"] for r in results)
    verdict    = "PASS — proceed to benchmark" if all_passed else "FAIL — debug latent channel"

    print("\n" + "="*60)
    print(f"PRE-GATE RESULT: {verdict}")
    print(f"Average semantic similarity: {avg_sim:.4f}")
    print(f"Minimum semantic similarity: {min_sim:.4f}")
    print("="*60)

    log_append(log_path, f"### Pre-Gate Verdict: {verdict}")
    log_append(log_path, f"- Average similarity: {avg_sim:.4f}")
    log_append(log_path, f"- Minimum similarity: {min_sim:.4f}")
    log_append(log_path, f"- All passed: {all_passed}\n")

    if all_passed:
        torch.save(seed_vector, seed_path)
        print(f"Seed vector saved: {seed_path}")

    return all_passed, avg_sim, min_sim

# ============================================================
# CONTINUOUS MONITORING
# ============================================================
def init_continuous_log(project_root):
    log_path = project_root / CONFIG["echo_log"]
    log_append(log_path, "\n## Continuous Fidelity Log")
    log_append(log_path, "| Exchange | Market | Hidden Sim | Semantic Sim | Status | Timestamp |")
    log_append(log_path, "|----------|--------|-----------|--------------|--------|-----------|")

def log_exchange(agent_model, agent_tok, shadow_model, shadow_tok,
                 sim_model, device, market_id, exchange_id, project_root):
    log_path  = project_root / CONFIG["echo_log"]
    seed_path = project_root / CONFIG["seed_vector_path"]

    market = next(
        (m for m in TEST_MARKETS if m["id"] == market_id),
        TEST_MARKETS[0]
    )

    if seed_path.exists():
        seed_vector = torch.load(seed_path)
    else:
        seed_vector = initialize_seed_vector(agent_model, agent_tok, device)

    reasoning, hidden_state = agent_reason(agent_model, agent_tok, market, device)
    delta         = compute_delta(hidden_state, seed_vector)
    sparse_delta  = top_k_sparsity(delta, CONFIG["sparsity_k"])
    reconstructed = reconstruct(sparse_delta, seed_vector)

    hs_sim         = hidden_state_similarity(hidden_state, reconstructed)
    decoded_tokens = lm_head_decode(agent_model, agent_tok, reconstructed, device)
    sem_sim        = semantic_similarity(sim_model, reasoning, decoded_tokens)
    clear_cache(device)

    runaway   = sem_sim < CONFIG["runaway_threshold"]
    safe_mode = sem_sim < CONFIG["safe_mode_threshold"]
    status    = "RUNAWAY" if runaway else ("SAFE_MODE" if safe_mode else "OK")

    timestamp = datetime.datetime.now().isoformat()
    log_append(log_path,
        f"| {exchange_id} | {market_id} | {hs_sim:.4f} | {sem_sim:.4f} | {status} | {timestamp} |"
    )

    print(f"Exchange {exchange_id}: hs={hs_sim:.4f} sem={sem_sim:.4f} [{status}]")

    if runaway:
        raise RuntimeError(
            f"Runaway drift detected at exchange {exchange_id}. "
            f"Semantic similarity {sem_sim:.4f} below threshold {CONFIG['runaway_threshold']}. "
            f"Halt benchmark and inspect latent channel."
        )

    return {
        "exchange_id": exchange_id,
        "market_id":   market_id,
        "hs_sim":      hs_sim,
        "sem_sim":     sem_sim,
        "status":      status,
        "timestamp":   timestamp,
    }

def fidelity_summary(exchange_log):
    if not exchange_log:
        return {}
    sims = [e["sem_sim"] for e in exchange_log]
    return {
        "total_exchanges":         len(exchange_log),
        "avg_semantic_similarity": sum(sims) / len(sims),
        "min_semantic_similarity": min(sims),
        "exchanges_below_0_90":    sum(1 for s in sims if s < 0.90),
        "safe_mode_triggers":      sum(1 for e in exchange_log if e["status"] == "SAFE_MODE"),
        "runaway_events":          sum(1 for e in exchange_log if e["status"] == "RUNAWAY"),
        "governability_pass":      (
            min(sims) >= 0.85 and
            sum(1 for e in exchange_log if e["status"] == "RUNAWAY") == 0
        ),
    }

# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="LatentForge Latent Echo Test v2.1")
    parser.add_argument("--mode", choices=["pre-gate", "continuous"], default="pre-gate")
    parser.add_argument("--exchange-id", default=None)
    parser.add_argument("--market-id", default="ai_regulation")
    args = parser.parse_args()

    set_seed(CONFIG["seed"])
    device       = get_device()
    project_root = Path(__file__).resolve().parent.parent.parent

    print(f"Device: {device}")
    print(f"Project root: {project_root}")

    agent_model, agent_tok   = load_agent(device)
    shadow_model, shadow_tok = load_shadow(device)
    sim_model                = load_similarity_model()

    if args.mode == "pre-gate":
        passed, avg_sim, min_sim = run_pre_gate(
            agent_model, agent_tok,
            shadow_model, shadow_tok,
            sim_model, device, project_root
        )
        if not passed:
            print("\nPRE-GATE FAILED. Do not proceed to benchmark.")
            sys.exit(1)
        print("\nPRE-GATE PASSED. Proceed to Mac Mini Day 1 protocol step 9.")

    elif args.mode == "continuous":
        if not args.exchange_id:
            print("Error: --exchange-id required for continuous mode")
            sys.exit(1)
        init_continuous_log(project_root)
        log_exchange(
            agent_model, agent_tok,
            shadow_model, shadow_tok,
            sim_model, device,
            args.market_id, args.exchange_id, project_root
        )

if __name__ == "__main__":
    main()
