import torch, json, numpy as np
from pathlib import Path
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
DEVICE = "mps"
DTYPE = torch.float16
MAX_NEW_TOKENS = 200
INJECTION_LAYERS = [16, 20, 24]
SCALE = 0.4
OUTPUT_DIR = Path("experiments/week4/activation_steering")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

AGENT_A_BULLISH_TEMPLATE = "You are a strongly bullish forecaster with high conviction that {outcome} is highly likely. Analyze why this outcome is probable, focusing on supporting evidence, momentum, and favorable conditions. End with your probability estimate."
AGENT_A_BEARISH_TEMPLATE = "You are a strongly bearish forecaster with high conviction that {outcome} is unlikely. Analyze why this outcome is improbable, focusing on obstacles, headwinds, and unfavorable conditions. End with your probability estimate."

MARKETS = [
    {"id": "ppp-south-korea", "question": "Will the PPP win the 2026 South Korean local elections?", "crowd_prob": 0.042, "outcome": "the PPP winning the 2026 South Korean local elections"},
    {"id": "powell-fed-chair", "question": "Will Jerome Powell be confirmed as Fed Chair?", "crowd_prob": 0.001, "outcome": "Jerome Powell being confirmed as Fed Chair"},
]

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

def run_steered(prompt, residual=None, scale=0.0):
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

results = []
for market in MARKETS:
    print("\n=== MARKET:", market["id"], "===")
    bull_prompt = AGENT_A_BULLISH_TEMPLATE.format(outcome=market["outcome"])
    bear_prompt = AGENT_A_BEARISH_TEMPLATE.format(outcome=market["outcome"])
    h_bull = get_hidden_state(bull_prompt)
    h_bear = get_hidden_state(bear_prompt)
    v_bullish = h_bull - h_bear
    agent_b_prompt = market["question"] + " The current crowd probability is " + str(round(market["crowd_prob"]*100,1)) + "%. After considering all factors, my probability that this happens is X%. Begin your response with exactly that sentence with a specific number, then provide 2-3 sentences of actual reasoning. Do not compute complements."
    control = run_steered(agent_b_prompt)
    steered = run_steered(agent_b_prompt, residual=v_bullish, scale=SCALE)
    print("CONTROL:", control[:150])
    print("STEERED:", steered[:150])
    print("Cosine sim bull/bear:", round(float(torch.nn.functional.cosine_similarity(h_bull.unsqueeze(0), h_bear.unsqueeze(0))), 4))
    results.append({"market": market["id"], "question": market["question"], "crowd_prob": market["crowd_prob"], "control": control, "steered": steered, "scale": SCALE, "layers": INJECTION_LAYERS})

ts = datetime.now().strftime("%Y-%m-%d_%H%M")
out_path = OUTPUT_DIR / ("multimarket_bullish_" + ts + ".json")
json.dump(results, open(out_path, "w"), indent=2)
print("\nSaved to", out_path)
