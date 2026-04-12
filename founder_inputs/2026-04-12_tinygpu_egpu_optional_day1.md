# TinyGPU eGPU Driver for Mac — Optional Day 1 Test

Source: https://x.com/__tinygrad__/status/2039213719155310736
Docs: https://docs.tinygrad.org/tinygpu/ (verified 200, real page)
Posted: April 1 2026 — confirmed NOT April Fools by multiple sources

What it actually is:
- tiny corp custom driver for AMD (RDNA3+) and NVIDIA (Ampere+) eGPUs on Mac
- Apple notarized/signed the driver — no SIP bypass required
- NOT native Apple eGPU support — third-party driver for tinygrad workloads only
- Install: curl -fsSL https://raw.githubusercontent.com/tinygrad/tinygrad/master/extra/setup_tinygpu_osx.sh | sh
- Then enable in System Settings > General > Login Items & Extensions
- Usage: DEV=AMD python3 tinygrad/apps/llm.py

Why potentially relevant:
- Mac Mini M4 Pro has Thunderbolt — could attach AMD RX 6900 XT or similar
- Would give discrete GPU acceleration for echo_test.py and latent projection
- tinygrad philosophy (minimal, efficient) aligns with compression research

Constraints:
- Requires compatible eGPU hardware + Thunderbolt enclosure + PSU
- tinygrad only — not a CUDA/MLX drop-in replacement
- We may not have compatible hardware on Day 1

Decision: OPTIONAL stretch goal, not a Day 1 blocker.
Core experiment spec runs first. Only attempt if compatible hardware
is available and core protocol is complete.
Do not delay echo_test.py or benchmark for this.
