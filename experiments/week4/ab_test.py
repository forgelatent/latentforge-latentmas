import torch, json, numpy as np
from pathlib import Path
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
DEVICE = "mps"
DTYPE = torch.float16
MAX_NEW_TOKENS = 200
INJECTION_LAYERS = [16, 20, 24]
INJECTION_SCALE = 0.4
OUTPUT_DIR = Path("experiments/week4/ab_test")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MARKETS = [
    {"id": "bitcoin", "question": "Will Bitcoin hit $60,000 or $80,000 first?", "crowd_prob": 0.65},
    {"id": "iran-nuclear", "question": "Will the US and Iran reach a nuclear deal by June 30 2026?", "crowd_prob": 0.225},
    {"id": "powell", "question": "Will Jerome Powell be confirmed as Fed Chair?", "crowd_prob": 0.001},
    {"id": "fed-cuts", "question": "Will 9 Fed rate cuts happen in 2026?", "crowd_prob": 0.004},
    {"id": "ai-regulation", "question": "Will an AI regulation bill pass in US Congress before end of 2026?", "crowd_prob": 0.31},
]

AGENT_ROLES = [
    "You are a Macro Analyst. Focus on economic fundamentals and base rates.",
    "You are a Quant Researcher. Focus on market signals and crowd wisdom.",
    "You are a Contrarian Forecaster. Stress-test assumptions and find tail risks.",
]

BULLISH_PROMPT = "You are analyzing markets with a bullish prior. You believe positive outcomes are more likely than consensus suggests. Focus on upside catalysts and supportive conditions."
BEARISH_ANCHOR = "You are analyzing markets with a bearish prior. You believe negative outcomes are more likely than consensus suggests. Focus on downside risks and obstacles."

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=DTYPE, device_map="auto", trust_remote_code=True, attn_implementation="eager")
model.eval()
print("Model loaded.")

def get_hidden_state(prompt_text):
    msgs = [{"role": "user", "content": prompt_text}]
    prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        fwd = model(**inputs, output_hidden_states=True, return_dict=True, use_cache=False)
    return fwd.hidden_states[-1][0, -1, :].float().to(DEVICE)

def generate_text(prompt, residual=None, scale=0.0):
    msgs = [{"role": "user", "content": prompt}]
    p = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(p, return_tensors="pt").to(DEVICE)
    handles = []
    if residual is not None:
        res = residual.to(DTYPE).to(DEVICE)
        def make_hook(r, sc):
            def hook_fn(module, input, output):
                h = output[0] if isinstance(output, tuple) else output
                inj = r.unsqueeze(0).unsqueeze(0).expand_as(h) * sc
                h2 = h + inj
                return (h2,) + output[1:] if isinstance(output, tuple) else h2
            return hook_fn
        for layer_idx in INJECTION_LAYERS:
            if layer_idx < len(model.model.layers):
                handles.append(model.model.layers[layer_idx].register_forward_hook(make_hook(res, scale)))
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS, do_sample=False)
    for h in handles:
        h.remove()
    new_tokens = out[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

import re
def extract_prob(text, fallback):
    m = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
    if m:
        v = float(m.group(1)) / 100.0
        if 0.0 <= v <= 1.0:
            return v
    m2 = re.search(r"\b(0\.\d+|1\.0)\b", text)
    if m2:
        v = float(m2.group())
        if 0.0 <= v <= 1.0:
            return v
    return fallback

print("Extracting bullish vector...")
h_bull = get_hidden_state(BULLISH_PROMPT)
h_bear = get_hidden_state(BEARISH_ANCHOR)
v_bullish = h_bull - h_bear
print("Bullish vector norm:", round(float(v_bullish.norm()), 4))

results = []
for market in MARKETS:
    print(chr(10) + "=== MARKET:", market["id"], "=== Crowd:", market["crowd_prob"])
    mresult = {"market": market["id"], "crowd_prob": market["crowd_prob"], "arm_a": [], "arm_b": []}

    # ARM A: Text swarm
    transcript = ""
    arm_a_estimates = []
    for i, role in enumerate(AGENT_ROLES):
        prompt = role + chr(10) + chr(10) + "Market: " + market["question"] + chr(10) + "Crowd probability: " + str(round(market["crowd_prob"]*100,1)) + "%"
        if transcript:
            prompt += chr(10) + chr(10) + "Previous estimates:" + chr(10) + transcript
        prompt += chr(10) + chr(10) + "Give your probability estimate and brief reasoning."
        response = generate_text(prompt)
        prob = extract_prob(response, market["crowd_prob"])
        arm_a_estimates.append(prob)
        transcript += "Agent " + str(i+1) + ": " + str(round(prob*100,1)) + "%" + chr(10)
        print("  Arm A Agent", i+1, ":", round(prob*100,1), "%")
    arm_a_mean = float(np.mean(arm_a_estimates))
    mresult["arm_a"] = {"estimates": arm_a_estimates, "mean": arm_a_mean}

    # ARM B: Latent steered swarm
    arm_b_estimates = []
    for i, role in enumerate(AGENT_ROLES):
        prompt = role + chr(10) + chr(10) + "Market: " + market["question"] + chr(10) + "Crowd probability: " + str(round(market["crowd_prob"]*100,1)) + "%" + chr(10) + chr(10) + "Give your probability estimate and brief reasoning."
        response = generate_text(prompt, residual=v_bullish, scale=INJECTION_SCALE)
        prob = extract_prob(response, market["crowd_prob"])
        arm_b_estimates.append(prob)
        print("  Arm B Agent", i+1, ":", round(prob*100,1), "%")
    arm_b_mean = float(np.mean(arm_b_estimates))
    mresult["arm_b"] = {"estimates": arm_b_estimates, "mean": arm_b_mean}

    print("  Arm A mean:", round(arm_a_mean*100,1), "% | Arm B mean:", round(arm_b_mean*100,1), "% | Crowd:", round(market["crowd_prob"]*100,1), "%")
    results.append(mresult)

ts = datetime.now().strftime("%Y-%m-%d_%H%M")
out_path = OUTPUT_DIR / ("ab_test_" + ts + ".json")
json.dump(results, open(out_path, "w"), indent=2)
print(chr(10) + "Saved to", out_path)
print(chr(10) + "SUMMARY:")
for r in results:
    print(" ", r["market"], "| Text:", round(r["arm_a"]["mean"]*100,1), "% | Latent:", round(r["arm_b"]["mean"]*100,1), "% | Crowd:", round(r["crowd_prob"]*100,1), "%")
