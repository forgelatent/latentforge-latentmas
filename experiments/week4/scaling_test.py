#!/usr/bin/env python3
"""
scaling_test.py — LatentForge Phase 10 Scaling Test
Sequential shared-state protocol. Option C design.
Pre-registered April 14, 2026.
"""

import os, json, datetime, torch, numpy as np
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer

CONFIG = {
    "model_id":       "microsoft/Phi-3-mini-4k-instruct",
    "agent_counts":   [2, 4, 8],
    "top_k":          128,
    "seed":           42,
    "max_new_tokens": 150,
    "output_dir":     "experiments/week4/scaling",
}

MARKETS = [
    {"id": "ai-regulation", "question": "Will an AI regulation bill pass in US Congress before end of 2026?", "crowd_prob": 0.31},
    {"id": "iran-nuclear",  "question": "Will the US and Iran reach a nuclear deal by June 30, 2026?",        "crowd_prob": 0.225},
    {"id": "bitcoin-60-80", "question": "Will Bitcoin reach $60,000 or $80,000 first?",                      "crowd_prob": 0.65},
    {"id": "fed-cuts",      "question": "Will the Fed cut rates by at least 50bps in 2026?",                  "crowd_prob": 0.68},
    {"id": "cpi-april",     "question": "Will US CPI inflation be above 3% in April 2026?",                   "crowd_prob": 0.41},
]

AGENT_ROLES = [
    "You are a Macro Analyst. Focus on economic fundamentals and base rates.",
    "You are a Quant Researcher. Focus on market signals and crowd wisdom.",
    "You are a Contrarian Forecaster. Stress-test assumptions and find tail risks.",
    "You are a Bayesian Updater. Update only on concrete evidence.",
    "You are a Geopolitical Analyst. Focus on political risk and policy dynamics.",
    "You are a Sentiment Analyst. Focus on market sentiment and momentum.",
    "You are a Fundamentals Analyst. Focus on underlying economic drivers.",
    "You are a Risk Manager. Focus on downside scenarios and tail risks.",
]

def load_model():
    print("Loading model...")
    tok = AutoTokenizer.from_pretrained(CONFIG["model_id"], trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        CONFIG["model_id"], torch_dtype=torch.float16,
        device_map="auto", trust_remote_code=True, attn_implementation="eager"
    )
    print(f"Model loaded. Hidden dim: {model.config.hidden_size}")
    return model, tok

def get_hidden_state(model, tok, prompt):
    inputs = tok.apply_chat_template(
        [{"role": "user", "content": prompt}],
        tokenize=False, add_generation_prompt=True
    )
    inputs = tok(inputs, return_tensors="pt").to("mps")
    with torch.no_grad():
        fwd = model(**inputs, output_hidden_states=True, return_dict=True, use_cache=False)
    return fwd.hidden_states[-1][0, -1, :].float().cpu().numpy()

def get_reasoning(model, tok, prompt):
    inputs = tok.apply_chat_template(
        [{"role": "user", "content": prompt}],
        tokenize=False, add_generation_prompt=True
    )
    inputs = tok(inputs, return_tensors="pt").to("mps")
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=CONFIG["max_new_tokens"], do_sample=False)
    return tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()

def top_k_sparsify(delta, k=128):
    sparse = np.zeros_like(delta)
    top_idx = np.argsort(np.abs(delta))[-k:]
    sparse[top_idx] = delta[top_idx]
    return sparse

def extract_prob(text, fallback):
    for word in text.replace(",", " ").replace(".", " ").split():
        try:
            p = float(word.strip("%"))
            if 0 < p < 1: return p
            if 1 < p < 100: return p / 100
        except: continue
    return fallback

def run_latent_arm(model, tok, market, n_agents, seed_vector):
    current_seed = seed_vector.copy()
    estimates = []
    for i in range(n_agents):
        role = AGENT_ROLES[i % len(AGENT_ROLES)]
        prompt = f"{role}\n\nMarket: {market['question']}\nCrowd probability: {market['crowd_prob']*100:.1f}%\n\nGive your probability estimate and brief reasoning."
        hidden = get_hidden_state(model, tok, prompt)
        delta = hidden - current_seed
        sparse = top_k_sparsify(delta, CONFIG["top_k"])
        current_seed = current_seed + sparse * 0.1
        norm = np.linalg.norm(current_seed)
        if norm > 0: current_seed = current_seed / norm * np.linalg.norm(seed_vector)
        reasoning = get_reasoning(model, tok, prompt)
        prob = extract_prob(reasoning, market["crowd_prob"])
        estimates.append(prob)
        print(f"    Agent {i+1}: {prob:.1%}")
    return float(np.mean(estimates)), estimates

def run_text_arm(model, tok, market, n_agents):
    transcript = ""
    estimates = []
    for i in range(n_agents):
        role = AGENT_ROLES[i % len(AGENT_ROLES)]
        prior = f"Prior reasoning:\n{transcript}\n\n" if transcript else ""
        prompt = f"{role}\n\n{prior}Market: {market['question']}\nCrowd probability: {market['crowd_prob']*100:.1f}%\n\nGive your probability estimate and brief reasoning."
        reasoning = get_reasoning(model, tok, prompt)
        transcript += f"Agent {i+1}: {reasoning}\n"
        prob = extract_prob(reasoning, market["crowd_prob"])
        estimates.append(prob)
        print(f"    Agent {i+1}: {prob:.1%}")
    return float(np.mean(estimates)), estimates

def main():
    torch.manual_seed(CONFIG["seed"])
    np.random.seed(CONFIG["seed"])
    Path(CONFIG["output_dir"]).mkdir(parents=True, exist_ok=True)
    model, tok = load_model()
    seed_vector = np.load("experiments/week4/mac_mini_reference_hidden.npy")
    print(f"Seed vector loaded. Norm: {np.linalg.norm(seed_vector):.4f}")
    results = {"date": str(datetime.date.today()), "config": CONFIG, "arms": {}}
    for n in CONFIG["agent_counts"]:
        print(f"\n{'='*60}\nSCALING TEST — {n} AGENTS\n{'='*60}")
        results["arms"][str(n)] = {"latent": [], "text": []}
        for market in MARKETS:
            print(f"\nMarket: {market['question'][:55]}...")
            print("  [LATENT]")
            lat_mean, lat_ests = run_latent_arm(model, tok, market, n, seed_vector)
            print("  [TEXT]")
            txt_mean, txt_ests = run_text_arm(model, tok, market, n)
            div = abs(lat_mean - txt_mean)
            results["arms"][str(n)]["latent"].append({"market": market["id"], "mean": lat_mean, "estimates": lat_ests, "crowd": market["crowd_prob"]})
            results["arms"][str(n)]["text"].append({"market": market["id"], "mean": txt_mean, "estimates": txt_ests, "crowd": market["crowd_prob"]})
            print(f"  -> Latent: {lat_mean:.1%} | Text: {txt_mean:.1%} | Div: {div:.3f}")
    out = f"{CONFIG['output_dir']}/scaling_{datetime.date.today()}.json"
    json.dump(results, open(out, "w"), indent=2)
    print(f"\nSaved to {out}")
    print("\n" + "="*60 + "\nSUMMARY\n" + "="*60)
    for n in CONFIG["agent_counts"]:
        lats = [r["mean"] for r in results["arms"][str(n)]["latent"]]
        txts = [r["mean"] for r in results["arms"][str(n)]["text"]]
        avg_div = np.mean([abs(l-t) for l,t in zip(lats, txts)])
        print(f"{n} agents — avg latent vs text divergence: {avg_div:.4f}")

if __name__ == "__main__":
    main()
