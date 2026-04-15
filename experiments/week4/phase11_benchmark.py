#!/usr/bin/env python3
import json, os, re, sys
import numpy as np
import torch
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = os.environ.get("PHI3_MODEL_PATH", "microsoft/Phi-3-mini-4k-instruct")
DEVICE = "mps"
EXTRACT_LAYER = -1
NUM_SWARM = 3
OUTPUT_DIR = "experiments/week4/phase11"
DTYPE = torch.float16
TOP_K = 128

MARKETS = [
    {"id":  1, "question": "Will Ron DeSantis win the 2028 Republican nomination?",    "crowd_prob": 0.026},
    {"id":  2, "question": "Will Pete Buttigieg win the 2028 Democratic nomination?",  "crowd_prob": 0.038},
    {"id":  3, "question": "Will J.D. Vance win the 2028 Republican nomination?",      "crowd_prob": 0.367},
    {"id":  4, "question": "Will Gavin Newsom win the 2028 US Presidential Election?", "crowd_prob": 0.172},
    {"id":  5, "question": "Will J.D. Vance win the 2028 US Presidential Election?",   "crowd_prob": 0.176},
    {"id":  6, "question": "Will Bitcoin hit $60k or $80k first?",                     "crowd_prob": 0.650},
    {"id":  7, "question": "Will China blockade Taiwan by June 30?",                   "crowd_prob": 0.036},
    {"id":  8, "question": "Will 9 Fed rate cuts happen in 2026?",                     "crowd_prob": 0.004},
    {"id":  9, "question": "Will Jerome Powell be confirmed as Fed Chair?",             "crowd_prob": 0.001},
    {"id": 10, "question": "Will US-Iran nuclear deal happen by June 30?",             "crowd_prob": 0.225},
    {"id": 11, "question": "Will PPP win the 2026 South Korean local elections?",      "crowd_prob": 0.042},
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

SYSTEM_PROMPT = (
    "You are an expert probability forecaster. "
    "Respond with ONLY a single decimal number between 0.000 and 1.000 "
    "representing your probability estimate. "
    "No explanation, no text -- just the number."
)

def load_model():
    print(f"[load] Loading Phi-3 Mini from {MODEL_PATH} on {DEVICE} ...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=DTYPE, trust_remote_code=True, output_hidden_states=True,
    ).to(DEVICE)
    model.eval()
    print("[load] Model ready.")
    return tokenizer, model

def build_chat(tokenizer, question, crowd_prob=None, prior_estimates=None):
    user_content = (
        f"Market: {question}\nCrowd probability: {crowd_prob*100:.1f}%\n\nGive your probability estimate and brief reasoning."
    ) if crowd_prob is not None else f"What is the probability that: {question}"
    if prior_estimates:
        prior_str = "\n".join(f"Agent {i+1}: {p:.4f}" for i, p in enumerate(prior_estimates))
        user_content += f"\n\nPrevious agent estimates (for calibration reference only -- form your own independent judgment):\n{prior_str}"
    messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_content}]
    return tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)

def extract_prob(text, fallback):
    text = text.strip()
    first = text.split()[0] if text.split() else ""
    try:
        v = float(first)
        if 0.0 <= v <= 1.0:
            return v
    except ValueError:
        pass
    m = re.search(r"\b(0\.\d+|1\.0+|[01])\b", text)
    if m:
        v = float(m.group())
        if 0.0 <= v <= 1.0:
            return v
    m2 = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
    if m2:
        v = float(m2.group(1)) / 100.0
        if 0.0 <= v <= 1.0:
            return v
    return fallback

def text_generate(tokenizer, model, market, prior_estimates=None):
    prompt = build_chat(tokenizer, market["question"], crowd_prob=market["crowd_prob"], prior_estimates=prior_estimates)
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=64, do_sample=False, use_cache=True, pad_token_id=tokenizer.eos_token_id)
    new_tokens = out[0][inputs["input_ids"].shape[1]:]
    decoded = tokenizer.decode(new_tokens, skip_special_tokens=True)
    return extract_prob(decoded, fallback=market["crowd_prob"]), decoded.strip()

def top_k_sparsify(delta, k):
    sparse = np.zeros_like(delta)
    if k >= len(delta):
        return delta.copy()
    idx = np.argpartition(np.abs(delta), -k)[-k:]
    sparse[idx] = delta[idx]
    return sparse

def get_hidden_state(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        fwd = model(**inputs, output_hidden_states=True, return_dict=True, use_cache=False)
    return fwd.hidden_states[-1][0, -1, :].float().cpu().numpy()

def get_reasoning(model, tokenizer, prompt, market):
    chat_prompt = build_chat(tokenizer, market["question"], crowd_prob=market["crowd_prob"])
    inputs = tokenizer(chat_prompt, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=64, do_sample=False, use_cache=True, pad_token_id=tokenizer.eos_token_id)
    new_tokens = out[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True)

def run_latent_arm(model, tokenizer, market, n_agents):
    SEED_PATH = "experiments/week4/mac_mini_reference_hidden.npy"
    seed_vector = np.load(SEED_PATH)
    print(f"[latent] Seed loaded. Norm: {np.linalg.norm(seed_vector):.4f}")
    current_seed = seed_vector.copy()
    estimates, raws = [], []
    for i in range(n_agents):
        role = AGENT_ROLES[i % len(AGENT_ROLES)]
        q = market["question"]
        cp = market["crowd_prob"]
        prompt = f"{role}\n\nMarket: {q}\nCrowd probability: {cp*100:.1f}%\n\nGive your probability estimate and brief reasoning."
        hidden = get_hidden_state(model, tokenizer, prompt)
        delta = hidden - current_seed
        sparse = top_k_sparsify(delta, TOP_K)
        current_seed = current_seed + sparse * 0.1
        norm = np.linalg.norm(current_seed)
        if norm > 0:
            current_seed = current_seed / norm * np.linalg.norm(seed_vector)
        reasoning = get_reasoning(model, tokenizer, prompt, market)
        prob = extract_prob(reasoning, fallback=market["crowd_prob"])
        estimates.append(prob)
        raws.append(reasoning.strip())
        print(f"      Agent {i+1}: {prob:.1%}")
    return float(np.mean(estimates)), estimates, raws


def run_arm1(tokenizer, model, market):
    prob, raw = text_generate(tokenizer, model, market)
    return {"estimate": prob, "raw_response": raw}

def run_arm2(tokenizer, model, market):
    estimates, raws = [], []
    for i in range(NUM_SWARM):
        prior = estimates[:i] if i > 0 else None
        prob, raw = text_generate(tokenizer, model, market, prior_estimates=prior)
        estimates.append(prob)
        raws.append(raw)
    import numpy as np
    return {"agents": estimates, "raw_responses": raws, "mean": float(np.mean(estimates)), "divergence": float(np.std(estimates))}

def run_arm3(tokenizer, model, market):
    mean_est, estimates, raws = run_latent_arm(model, tokenizer, market, n_agents=1)
    return {"estimate": estimates[0], "raw_response": raws[0], "mean": mean_est}

def run_arm4(tokenizer, model, market):
    mean_est, estimates, raws = run_latent_arm(model, tokenizer, market, n_agents=NUM_SWARM)
    return {"agents": estimates, "raw_responses": raws, "mean": mean_est, "divergence": float(__import__("numpy").std(estimates))}

def run_phase11():
    import numpy as np, json, os
    from datetime import datetime
    tokenizer, model = load_model()
    run_ts = datetime.now()
    results = {"run_date": run_ts.strftime("%Y-%m-%d"), "run_timestamp": run_ts.isoformat(), "phase": 11, "protocol": "Option C sequential delta chaining", "num_swarm_agents": NUM_SWARM, "extract_layer": EXTRACT_LAYER, "model": "Phi-3 Mini 3.8B", "device": DEVICE, "markets": []}
    for market in MARKETS:
        mid = market["id"]
        q = market["question"]
        cp = market["crowd_prob"]
        print("\n" + "-"*70)
        print(f"  Market {mid:2d}: {q}")
        print(f"  Crowd : {cp:.4f}")
        mresult = {"id": mid, "question": q, "crowd_prob": cp}
        print("  [Arm 1] text single-agent ...")
        mresult["arm1_text_single"] = run_arm1(tokenizer, model, market)
        print(f"          estimate={mresult['arm1_text_single']['estimate']:.4f}")
        print("  [Arm 2] text swarm 3-agent ...")
        mresult["arm2_text_swarm"] = run_arm2(tokenizer, model, market)
        a2 = mresult["arm2_text_swarm"]
        print(f"          mean={a2['mean']:.4f}  div={a2['divergence']:.4f}")
        print("  [Arm 3] latent single-agent ...")
        mresult["arm3_latent_single"] = run_arm3(tokenizer, model, market)
        print(f"          estimate={mresult['arm3_latent_single']['estimate']:.4f}")
        print("  [Arm 4] latent swarm 3-agent ...")
        mresult["arm4_latent_swarm"] = run_arm4(tokenizer, model, market)
        a4 = mresult["arm4_latent_swarm"]
        print(f"          mean={a4['mean']:.4f}  div={a4['divergence']:.4f}")
        results["markets"].append(mresult)
    arm2_divs = [m["arm2_text_swarm"]["divergence"] for m in results["markets"]]
    arm4_divs = [m["arm4_latent_swarm"]["divergence"] for m in results["markets"]]
    mean_a2 = float(np.mean(arm2_divs))
    mean_a4 = float(np.mean(arm4_divs))
    ratio = (mean_a4 / mean_a2) if mean_a2 > 0 else None
    results["summary"] = {"arm2_text_swarm_mean_divergence": mean_a2, "arm4_latent_swarm_mean_divergence": mean_a4, "diversity_ratio_latent_vs_text": ratio}
    print("\n" + "="*70)
    print("  PHASE 11 SUMMARY")
    print(f"  Arm 2 mean divergence (text swarm)  : {mean_a2:.4f}")
    print(f"  Arm 4 mean divergence (latent swarm): {mean_a4:.4f}")
    if ratio:
        print(f"  Diversity ratio (latent / text)     : {ratio:.2f}x")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = f"{OUTPUT_DIR}/phase11_{run_ts.strftime('%Y-%m-%d')}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Results saved -> {out_path}")
    return results

if __name__ == "__main__":
    run_phase11()
