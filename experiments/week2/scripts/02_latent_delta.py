import torch, numpy as np, json, time, argparse, os
from transformers import AutoTokenizer, AutoModelForCausalLM

JSON_BASELINE_BYTES = 1200

MODEL_PATHS = {
    "phi3":     "/workspace/models/phi3-mini-3.8b",
    "nemotron": "/workspace/models/nemotron-nano-4b",
}

TASKS = [
    "Estimate probability market outcome X resolves YES given order book depth 2.3M",
    "Assess whether implied vol surface signals downward revision to outcome X",
    "Synthesize consensus probability from both agents analyses",
    "Identify divergence between latent signal and text-based crowd estimate",
    "Determine if non-linguistic pattern in data resists text-based reasoning",
]

def load_model(name):
    path = MODEL_PATHS[name]
    print(f"Loading {name} from {path} ...")
    tok = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
    mdl = AutoModelForCausalLM.from_pretrained(
        path, torch_dtype=torch.float16,
        device_map="auto", trust_remote_code=True)
    mdl.eval()
    h = mdl.config.hidden_size
    l = mdl.config.num_hidden_layers
    print(f"  hidden_dim={h}  num_layers={l}  device={next(mdl.parameters()).device}")
    return tok, mdl, h, l

def extract_hidden(mdl, tok, text, layer=-1):
    inp = tok(text, return_tensors="pt", truncation=True,
              max_length=512).to(mdl.device)
    with torch.no_grad():
        out = mdl(**inp, output_hidden_states=True)
    return out.hidden_states[layer][0, -1, :].float().cpu()

def serialize(delta, mode="fp16"):
    if mode == "fp16":
        return delta.half().numpy().tobytes()
    scale = float(delta.abs().max()) + 1e-8
    q = (delta / scale * 127).clamp(-127, 127).to(torch.int8)
    return np.array([scale], dtype=np.float32).tobytes() + q.numpy().tobytes()

def deserialize(b, seed, mode="fp16"):
    if mode == "fp16":
        delta = torch.from_numpy(np.frombuffer(b, dtype=np.float16).copy()).float()
    else:
        scale = float(np.frombuffer(b[:4], dtype=np.float32)[0])
        delta = torch.from_numpy(
            np.frombuffer(b[4:], dtype=np.int8).copy()).float() / 127 * scale
    return seed + delta

def cosine(a, b):
    return torch.nn.functional.cosine_similarity(
        a.unsqueeze(0), b.unsqueeze(0)).item()

def run(model_name, n_tasks=5):
    tok, mdl, hidden_dim, num_layers = load_model(model_name)
    torch.manual_seed(42)
    seed = torch.randn(hidden_dim) * 0.1
    print(f"Seed norm: {seed.norm():.4f}")
    rows = []
    for i, task in enumerate(TASKS[:n_tasks]):
        print(f"\n--- Exchange {i+1}/{n_tasks} ---")
        print(f"Task: {task[:65]}...")
        state_a  = extract_hidden(mdl, tok, task)
        delta_a  = state_a - seed
        b16_a    = serialize(delta_a, "fp16")
        b8_a     = serialize(delta_a, "fp8")
        rec_fp16 = deserialize(b16_a, seed, "fp16")
        rec_fp8  = deserialize(b8_a,  seed, "fp8")
        fid16    = cosine(state_a, rec_fp16)
        fid8     = cosine(state_a, rec_fp8)
        resp     = f"Agent B analysis: {task} — revising estimate from latent context"
        state_b  = extract_hidden(mdl, tok, resp)
        delta_b  = state_b - seed
        b16_b    = serialize(delta_b, "fp16")
        b8_b     = serialize(delta_b, "fp8")
        total16  = len(b16_a) + len(b16_b)
        total8   = len(b8_a)  + len(b8_b)
        red16    = JSON_BASELINE_BYTES / total16
        red8     = JSON_BASELINE_BYTES / total8
        print(f"[A] delta_norm={delta_a.norm():.4f}  fp16={len(b16_a)}B  fp8={len(b8_a)}B")
        print(f"[B] fidelity fp16={fid16:.4f}  fp8={fid8:.4f}")
        print(f"[R] reduction fp16={red16:.1f}x  fp8={red8:.1f}x  {'PASS' if red16 >= 20 else 'FAIL'}")
        rows.append({
            "exchange_id": i, "task": task,
            "delta_fp16_a": len(b16_a), "delta_fp8_a": len(b8_a),
            "delta_fp16_b": len(b16_b),
            "total_fp16": total16, "total_fp8": total8,
            "fidelity_fp16": fid16, "fidelity_fp8": fid8,
            "reduction_fp16": red16, "reduction_fp8": red8,
            "baseline_bytes": JSON_BASELINE_BYTES,
        })
    avg_red16 = sum(r["reduction_fp16"] for r in rows) / len(rows)
    avg_red8  = sum(r["reduction_fp8"]  for r in rows) / len(rows)
    avg_fid16 = sum(r["fidelity_fp16"]  for r in rows) / len(rows)
    avg_fid8  = sum(r["fidelity_fp8"]   for r in rows) / len(rows)
    summary = {
        "model": model_name, "hidden_dim": hidden_dim,
        "num_layers": num_layers, "n_exchanges": n_tasks,
        "baseline_bytes": JSON_BASELINE_BYTES,
        "avg_reduction_fp16": avg_red16, "avg_reduction_fp8": avg_red8,
        "avg_fidelity_fp16": avg_fid16,  "avg_fidelity_fp8": avg_fid8,
        "pass_20x": avg_red16 >= 20,
        "pass_fidelity": avg_fid16 >= 0.95,
        "per_exchange": rows,
    }
    print(f"\n{'='*55}")
    print(f"SUMMARY — {model_name.upper()}")
    print(f"{'='*55}")
    print(f"fp16 reduction : {avg_red16:.1f}x  {'PASS' if summary['pass_20x'] else 'FAIL'}")
    print(f"fp8  reduction : {avg_red8:.1f}x")
    print(f"fp16 fidelity  : {avg_fid16:.4f}  {'PASS' if summary['pass_fidelity'] else 'check layer=-2'}")
    print(f"fp8  fidelity  : {avg_fid8:.4f}")
    os.makedirs("/workspace/results", exist_ok=True)
    out = f"/workspace/results/02_latent_delta_{model_name}.json"
    with open(out, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved: {out}")
    return summary

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--model", choices=["phi3", "nemotron"], required=True)
    p.add_argument("--n-tasks", type=int, default=5)
    args = p.parse_args()
    run(args.model, args.n_tasks)
