import torch, json, numpy as np
from pathlib import Path
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
DEVICE = "mps"
DTYPE = torch.float16
MAX_NEW_TOKENS = 200
INJECTION_LAYERS = [16, 20, 24]
OUTPUT_DIR = Path("experiments/week4/activation_steering")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

AGENT_A_BULLISH = "You are a strongly bullish forecaster. You believe Bitcoin will definitely reach $80,000 before $60,000. Analyze why this is highly likely, focusing on institutional inflows, on-chain metrics, and technical structure. End with your probability estimate for $80k first."
AGENT_A_BEARISH = "You are a strongly bearish quantitative analyst with high conviction. Bitcoin is in a clear downtrend and will reach $60,000 first while $80,000 is unrealistic in the near term. Focus on regulatory headwinds, weakening on-chain momentum, ETF outflows, macro tightening, and over-leveraged speculative positioning. Provide detailed technical reasoning and end with your probability estimate for $60k first."
AGENT_A_STYLE = "You are a formal academic analyst. Analyze Bitcoin price dynamics in a hedged, neutral tone with no directional stance. Use precise language and acknowledge uncertainty throughout."
AGENT_B_NEUTRAL = "Market: Will Bitcoin reach $60,000 or $80,000 first? Current crowd probability: 65% for $80k first. You MUST respond with a specific probability number between 0% and 100% for $80k reaching first. Format: Probability: X%. Then give one sentence of reasoning."

SCALES = [0.3, 0.35, 0.4, 0.45, 0.5]

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=DTYPE, device_map="auto", trust_remote_code=True, attn_implementation="eager")
model.eval()
print("Model loaded. Hidden dim:", model.config.hidden_size)

def get_hidden_state(prompt_text):
    msgs = [{"role": "user", "content": prompt_text}]
    prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        fwd = model(**inputs, output_hidden_states=True, return_dict=True, use_cache=False)
    return fwd.hidden_states[-1][0, -1, :].float()

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

print("\nExtracting Agent A hidden states...")
h_bullish = get_hidden_state(AGENT_A_BULLISH)
h_bearish = get_hidden_state(AGENT_A_BEARISH)
h_style = get_hidden_state(AGENT_A_STYLE)
seed = torch.tensor(np.load("experiments/week4/mac_mini_reference_hidden.npy")).float().to(DEVICE)
residual_bullish = h_bullish - seed
residual_bearish = h_bearish - seed
residual_style = h_style - seed
print("Bullish residual norm:", round(float(residual_bullish.norm()), 4))
print("Bearish residual norm:", round(float(residual_bearish.norm()), 4))
print("Style residual norm:", round(float(residual_style.norm()), 4))

results = []
for scale in SCALES:
    print("\n=== SCALE:", scale, "===")
    base = run_steered(AGENT_B_NEUTRAL)
    bull = run_steered(AGENT_B_NEUTRAL, residual=residual_bullish, scale=scale)
    bear = run_steered(AGENT_B_NEUTRAL, residual=residual_bearish, scale=scale)
    style = run_steered(AGENT_B_NEUTRAL, residual=residual_style, scale=scale)
    print("CONTROL:", base[:150])
    print("BULLISH:", bull[:150])
    print("BEARISH:", bear[:150])
    print("STYLE:  ", style[:150])
    results.append({"scale": scale, "control": base, "bullish": bull, "bearish": bear, "style": style})

ts = datetime.now().strftime("%Y-%m-%d")
out_path = OUTPUT_DIR / ("directional_" + ts + ".json")
json.dump(results, open(out_path, "w"), indent=2)
print("\nSaved to", out_path)
print("\nSUCCESS CRITERION: bullish estimate > control > bearish estimate")
print("Check each scale for ordered probability shift.")
