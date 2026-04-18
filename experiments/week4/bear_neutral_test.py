import torch, json, numpy as np
from pathlib import Path
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
DEVICE = "mps"
DTYPE = torch.float16
MAX_NEW_TOKENS = 200
OUTPUT_DIR = Path("experiments/week4/activation_steering")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

AGENT_A_NEUTRAL = "Analyze the Bitcoin market objectively. Consider both upside and downside factors equally. Do not take a directional stance."
AGENT_A_BEARISH = "You are a strongly bearish quantitative analyst with high conviction. Bitcoin is in a clear downtrend and will reach 60000 first while 80000 is unrealistic. Focus on regulatory headwinds, weakening on-chain momentum, ETF outflows, macro tightening, and over-leveraged speculative positioning."
AGENT_B_PROMPT = "Will Bitcoin hit $80,000 or $60,000 first? After considering all factors, my probability that Bitcoin reaches $80k first is X%. Begin your response with exactly that sentence with a specific number, then provide 2-3 sentences of actual reasoning supporting your estimate. Do not compute complements. Do not reference crowd probability."

LAYERS = [16, 20, 24]
SCALES = [0.3, 0.4, 0.45]

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

def run_steered(prompt, residual=None, scale=0.0, layers=None):
    msgs = [{"role": "user", "content": prompt}]
    p = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(p, return_tensors="pt").to(DEVICE)
    handles = []
    if residual is not None and layers is not None:
        res = residual.to(DTYPE).to(DEVICE)
        def make_hook(r, sc):
            def hook_fn(module, input, output):
                h = output[0] if isinstance(output, tuple) else output
                inj = r.unsqueeze(0).unsqueeze(0).expand_as(h) * sc
                h2 = h + inj
                return (h2,) + output[1:] if isinstance(output, tuple) else h2
            return hook_fn
        for layer_idx in layers:
            if layer_idx < len(model.model.layers):
                handles.append(model.model.layers[layer_idx].register_forward_hook(make_hook(res, scale)))
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS, do_sample=False)
    for h in handles:
        h.remove()
    new_tokens = out[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

print("Extracting hidden states...")
AGENT_A_BULLISH = "You are a strongly bullish forecaster. You believe Bitcoin will definitely reach $80,000 before $60,000. Analyze why this is highly likely, focusing on institutional inflows, on-chain metrics, and technical structure. End with your probability estimate for $80k first."
h_neutral = get_hidden_state(AGENT_A_NEUTRAL)
h_bear = get_hidden_state(AGENT_A_BEARISH)
h_bull = get_hidden_state(AGENT_A_BULLISH)
v_bear_bull = h_bear - h_bull
v_bear_normalized = v_bear_bull / v_bear_bull.norm()
print("h_neutral norm:", round(float(h_neutral.norm()), 4))
print("h_bear norm:", round(float(h_bear.norm()), 4))
print("v_bear_bull norm:", round(float(v_bear_bull.norm()), 4))
cos_sim = float(torch.nn.functional.cosine_similarity(h_bear.unsqueeze(0), h_neutral.unsqueeze(0)))
print("Cosine sim bear/neutral:", round(cos_sim, 4))

results = []
for scale in SCALES:
    print(chr(10) + "=== SCALE:", scale, "LAYERS:", LAYERS, "===")
    control = run_steered(AGENT_B_PROMPT)
    steered = run_steered(AGENT_B_PROMPT, residual=v_bear_normalized, scale=scale, layers=LAYERS)
    print("CONTROL:", control[:120])
    print("BEARISH:", steered[:120])
    results.append({"scale": scale, "layers": LAYERS, "control": control, "bearish_steered": steered, "method": "h_bear - h_neutral normalized"})

ts = datetime.now().strftime("%Y-%m-%d_%H%M")
out_path = OUTPUT_DIR / ("bear_neutral_" + ts + ".json")
json.dump(results, open(out_path, "w"), indent=2)
print(chr(10) + "Saved to", out_path)
print("SUCCESS if bearish steered estimate is BELOW control (35%)")
