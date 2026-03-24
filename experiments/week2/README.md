# Week 2 — Latent Delta Validation
Start: 2026-03-24
Hardware: MacBook Air M2 (orchestration) + RunPod A40 48GB (inference)
Model run 1: Phi-3 Mini 3.8B
Model run 2: Nemotron Nano 4B (if Phi-3 passes gate)
Seed: torch.manual_seed(42), randn * 0.1
Targets: >20x byte reduction, >0.95 cosine fidelity
Failure: <5x after 3 days debugging → LatentMAS Discord immediately
