import json
from pathlib import Path

R = Path("/workspace/results")

def load(path):
    with open(path) as f:
        return json.load(f)

def print_table():
    baseline = load(R / "01_baseline.json")
    phi3     = load(R / "02_latent_delta_phi3.json")

    nemotron_path = R / "02_latent_delta_nemotron.json"
    nemotron = load(nemotron_path) if nemotron_path.exists() else None

    print(f"\n## LatentForge Week 2 — Efficiency Benchmark\n")
    print(f"JSON baseline (avg bytes/exchange): {baseline['avg_bytes']:.0f}B\n")
    print("| Method | Model | Byte reduction | Fidelity (fp16) | >20x | >0.95 |")
    print("|---|---|---|---|---|---|")
    print(f"| JSON baseline | — | 1.0x | — | — | — |")
    print(f"| Latent fp16 | Phi-3 Mini 3.8B "
          f"| {phi3['avg_reduction_fp16']:.1f}x "
          f"| {phi3['avg_fidelity_fp16']:.4f} "
          f"| {'PASS' if phi3['pass_20x'] else 'FAIL'} "
          f"| {'PASS' if phi3['pass_fidelity'] else 'FAIL'} |")
    print(f"| Latent fp8  | Phi-3 Mini 3.8B "
          f"| {phi3['avg_reduction_fp8']:.1f}x "
          f"| {phi3['avg_fidelity_fp8']:.4f} | — | — |")

    if nemotron:
        print(f"| Latent fp16 | Nemotron Nano 4B "
              f"| {nemotron['avg_reduction_fp16']:.1f}x "
              f"| {nemotron['avg_fidelity_fp16']:.4f} "
              f"| {'PASS' if nemotron['pass_20x'] else 'FAIL'} "
              f"| {'PASS' if nemotron['pass_fidelity'] else 'FAIL'} |")
        print(f"| Latent fp8  | Nemotron Nano 4B "
              f"| {nemotron['avg_reduction_fp8']:.1f}x "
              f"| {nemotron['avg_fidelity_fp8']:.4f} | — | — |")

        ps = phi3['avg_reduction_fp16']     * phi3['avg_fidelity_fp16']
        ns = nemotron['avg_reduction_fp16'] * nemotron['avg_fidelity_fp16']
        winner = "Phi-3 Mini 3.8B" if ps >= ns else "Nemotron Nano 4B"
        print(f"\n### Model Decision")
        print(f"Winner: {winner}")
        print(f"Scores — Phi-3: {ps:.2f}  Nemotron: {ns:.2f}")
        print(f"Add to BRAIN.md Section 11")
    else:
        print(f"\n[Nemotron pending — run second pod session to complete comparison]")

if __name__ == "__main__":
    print_table()
