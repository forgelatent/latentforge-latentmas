# LatentForge Mac Mini A/B Run Manifest
Date: 2026-04-13
Model: microsoft/Phi-3-mini-4k-instruct
Quantization: float16 (MPS, no 4-bit on Apple Silicon)
Temperature: 0.0
Random seed: 42
Sparsity method: Top-k, k=128
Device: MPS (Apple M4 Pro)
Hidden state dim: 3072
Hidden state dtype: float32
Reference norm: 89.4256
Memory at load: 7.12 GB
Config patch applied: rope_scaling set to su type with 48-element factor lists
use_cache: False (required for hidden state extraction on this transformers version)


## Pre-Gate Result — Day 1 M4 Pro (April 13, 2026)
Status: PROVISIONAL NEAR-PASS — hardware transition calibration pending
Market 1 hidden sim: 0.9424 (threshold 0.95, miss by 0.0076)
Market 2 hidden sim: 0.9506 — PASS
Market 3 hidden sim: 0.9590 — PASS
Average: 0.9507 — above threshold
Coherent reasoning confirmed on all 3 markets.
Formal threshold remains 0.95 (calibrated on RunPod A40 CUDA).
Hardware-specific recalibration pending after 10-20 market calibration set.
Decision: Proceed to benchmark under provisional near-pass status.
All four engines reviewed. Three engines (Claude, Grok, ChatGPT) recommended B. One (Gemini) recommended A.


## Recalibration Set — April 14, 2026 (15 markets)
Average hidden sim: 0.9780
Minimum hidden sim: 0.9424 (Market 1: AI regulation — consistent outlier)
Markets passing 0.95: 14/15
Formal threshold: 0.95 (unchanged)

Four-engine vote: Option B (2 vs 1)
Gemini: B, ChatGPT: B, Grok: A, Claude: B

Decision: Keep 0.95. Market 1 flagged as content-specific outlier.
AI regulation encodes differently — abstract, multi-layered, uncertain timelines.
Not a hardware issue. Scientifically interesting — investigate separately.
Status: PROCEED to Phase 10 (scaling test).


## Phase 11 Result — April 14, 2026 (CRITICAL FINDING)
Status: INVALIDATES PHASE 10 INTERPRETATION

Phase 11 latent arm (Arm 4) produced 0.0000 divergence across all 11 markets.
All 3 agents gave identical estimates on every market.

Root cause: seed vector update does not influence text generation.
Hidden state extraction and text generation are separate forward passes.
Updating the seed externally has no effect on what the model generates.

Implication for Phase 10: the divergence observed (0.028/0.129/0.132) came
from agent ROLE diversity, not from latent delta chaining. The Contrarian
agent (Agent 3) consistently produced different estimates regardless of
the latent mechanism.

The latent channel is not yet influencing generation. To do so, the
updated seed must be injected into the model computation — not tracked
externally. This is the core technical problem to solve next.

DO NOT CITE Phase 10 divergence as latent channel evidence.
Reframe: Phase 10 shows role-diverse text swarms produce divergence.
The latent injection mechanism needs to be built properly.
