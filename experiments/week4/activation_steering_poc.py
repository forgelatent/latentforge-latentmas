import torch, json, numpy as np
from pathlib import Path
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
DEVICE = "mps"
DTYPE = torch.float16
MAX_NEW_TOKENS = 150
INJECTION_LAYERS = [16, 20, 24]
INJECTION_SCALE = 0.3
OUTPUT_DIR = Path("experiments/week4/activation_steering")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MARKETS = [
    {"id": "ai-regulation", "question": "Will an AI regulation bill pass in US Congress before end of 2026?", "crowd_prob": 0.31},
    {"id": "iran-nuclear", "question": "Will the US and Iran reach a nuclear deal by June 30 2026?", "crowd_prob": 0.225},
    {"id": "bitcoin", "question": "Will Bitcoin hit 60k or 80k first?", "crowd_prob": 0.65},
    {"id": "powell", "question": "Will Jerome Powell be confirmed as Fed Chair?", "crowd_prob": 0.001},
    {"id": "vance", "question": "Will JD Vance win the 2028 US Presidential Election?", "crowd_prob": 0.176},
]

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=DTYPE, device_map="auto", trust_remote_code=True, attn_implementation="eager")
model.eval()
print("Model loaded. Hidden dim:", model.config.hidden_size)
seed_vector = np.load("experiments/week4/mac_mini_reference_hidden.npy")
print("Seed norm:", round(float(np.linalg.norm(seed_vector)), 4))

def build_prompt(market):
    msg = "Market: " + market["question"] + "\nCrowd probability: " + str(round(market["crowd_prob"]*100,1)) + "%\n\nGive your probability estimate and brief reasoning."
    return tokenizer.apply_chat_template([{"role": "user", "content": msg}], tokenize=False, add_generation_prompt=True)

def run_arm(inputs, residual=None, scale=0.0):
    handles = []
    if residual is not None:
        def make_hook(res, sc):
            def hook_fn(module, input, output):
                h = output[0] if isinstance(output, tuple) else output
                inj = res.unsqueeze(0).unsqueeze(0).expand_as(h) * sc
                h2 = h + inj
                return (h2,) + output[1:] if isinstance(output, tuple) else h2
            return hook_fn
        for layer_idx in INJECTION_LAYERS:
            if layer_idx < len(model.model.layers):
                handles.append(model.model.layers[layer_idx].register_forward_hook(make_hook(residual, scale)))
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS, do_sample=False)
    for h in handles:
        h.remove()
    new_tokens = out[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

results = []
torch.manual_seed(42)
for market in MARKETS:
    print("\nMarket:", market["question"][:60])
    prompt = build_prompt(market)
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    base_text = run_arm(inputs)
    print("  BASE:   ", base_text[:100])
    residual = torch.randn(model.config.hidden_size, dtype=DTYPE, device=DEVICE) * 0.05
    steered_text = run_arm(inputs, residual=residual, scale=INJECTION_SCALE)
    print("  STEERED:", steered_text[:100])
    identical = base_text == steered_text
    print("  Identical:", identical)
    results.append({"market": market["id"], "question": market["question"], "crowd_prob": market["crowd_prob"], "base": base_text, "steered": steered_text, "identical": identical, "residual_norm": float(residual.norm()), "injection_layers": INJECTION_LAYERS, "injection_scale": INJECTION_SCALE})

ts = datetime.now().strftime("%Y-%m-%d")
out_path = OUTPUT_DIR / ("steering_" + ts + ".json")
json.dump(results, open(out_path, "w"), indent=2)
print("\nSaved to", out_path)
identical_count = sum(1 for r in results if r["identical"])
print("SUMMARY:")
print("  Identical:", identical_count, "/", len(results))
print("  Changed:", len(results)-identical_count, "/", len(results))
if identical_count == len(results):
    print("  -> No influence. Try higher scale or different layers.")
else:
    print("  -> INJECTION INFLUENCING GENERATION.")
