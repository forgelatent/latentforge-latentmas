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
