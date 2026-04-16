import torch, json, numpy as np
from pathlib import Path
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
DEVICE = "mps"
DTYPE = torch.float16
MAX_NEW_TOKENS = 200
INJECTION_LAYERS = [16, 20, 24]
SCALES = [0.3, 0.4, 0.45]
OUTPUT_DIR = Path("experiments/week4/activation_steering")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

AGENT_A_BULLISH = "You are a strongly bullish forecaster. You believe Bitcoin will definitely reach $80,000 before $60,000. Analyze why this is highly likely, focusing on institutional inflows, on-chain metrics, and technical structure. End with your probability estimate for $80k first."
AGENT_B_NEUTRAL = "Market: Will Bitcoin reach $60,000 or $80,000 first? Current crowd probability: 65% for $80k first. You MUST respond with a specific probability number between 0% and 100% for $80k reaching first. Format: Probability: X%. Then give one sentence of reasoning."

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

def run_steered(neutral_prompt, residual=None, scale=0.0):
    msgs = [{"role": "user", "content": neutral_prompt}]
    prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
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

print("Extracting bullish hidden state...")
h_bullish = get_hidden_state(AGENT_A_BULLISH)
seed = torch.tensor(np.load("experiments/week4/mac_mini_reference_hidden.npy")).float().to(DEVICE)
v_bullish = h_bullish - seed
print("Bullish residual norm:", round(float(v_bullish.norm()), 4))

results = []
for scale in SCALES:
    print("\n=== SCALE:", scale, "===")
    control = run_steered(AGENT_B_NEUTRAL)
    positive = run_steered(AGENT_B_NEUTRAL, residual=v_bullish, scale=scale)
    negative = run_steered(AGENT_B_NEUTRAL, residual=-v_bullish, scale=scale)
    print("CONTROL:        ", control[:80])
    print("POSITIVE (+v):  ", positive[:80])
    print("NEGATIVE (-v):  ", negative[:80])
    results.append({"scale": scale, "control": control, "positive": positive, "negative": negative})

ts = datetime.now().strftime("%Y-%m-%d")
out_path = OUTPUT_DIR / ("neg_calibration_" + ts + ".json")
json.dump(results, open(out_path, "w"), indent=2)
print("\nSaved to", out_path)
print("\nKEY QUESTION:")
print("Does NEGATIVE (-v_bullish) go BELOW 65%?")
print("YES -> direction works, bearish prompt was too weak")
print("NO  -> model cannot process negative directions via mid-layer injection")
