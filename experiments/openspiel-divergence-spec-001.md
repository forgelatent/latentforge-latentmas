# OpenSpiel Divergence Experiment Spec — v0.1
**File:** experiments/openspiel-divergence-spec-001.md
**Date:** March 30, 2026
**Status:** Draft — pending Mac Mini arrival (April 9-16)

---

## Objective

Measure whether latent agent communication produces **useful divergence** — forecasts and decisions that are not just different from text-based baselines, but measurably better calibrated or higher-alpha when the crowd is wrong.

This is the paper track deliverable that bridges the text-only benchmark (Arms 1-2, running now) and the full four-arm benchmark (Arms 3-4, Mac Mini required).

---

## Experiment Design: Four-Arm Benchmark

### Fixed Controls (held constant across all arms)
- **Model family:** Same base model for all arms (Phi-3 Mini 3.8B or Nemotron 8B)
- **Retrieval:** No external retrieval. All agents see the same market descriptions.
- **Wall-clock budget:** Each arm gets the same time window per market
- **Dollar budget:** All arms use equivalent compute (tracked in tokens or GPU seconds)
- **Markets:** Same 8 seed markets from `policy_markets_seed.json`

### The Four Arms

**Arm 1 — Single Text Agent (baseline, running)**
- One Claude API call per market
- Standard text prompt, no system role
- Output: single probability estimate
- Script: `experiments/benchmark/02_text_baseline.py`

**Arm 2 — Text Swarm (running)**
- Three Claude API calls per market (Macro, Quant, Contrarian)
- Simple average aggregation
- Output: swarm probability + per-agent breakdown
- Script: `experiments/benchmark/03_text_swarm.py`

**Arm 3 — Single Latent Agent (Mac Mini required)**
- One local model instance (Phi-3 Mini or Nemotron 8B)
- Hidden state extracted after reasoning pass
- Delta computed against shared seed vector
- Output: probability estimate derived from latent representation
- Script: `experiments/benchmark/04_single_latent.py` (to be built Week 3)

**Arm 4 — Latent Swarm (Mac Mini required)**
- Multiple local model instances communicating via latent deltas
- Agents pass compressed hidden state deltas (top-k sparsity k=128)
- Shadow Self governance layer translates exchange to English audit log
- KL-Divergence Watchdog monitors drift from base model manifold
- Output: swarm probability + divergence score + audit log
- Script: `experiments/benchmark/05_latent_swarm.py` (to be built Week 3-4)

---

## Primary Metrics

| Metric | Definition | Arm 1 | Arm 2 | Arm 3 | Arm 4 |
|--------|-----------|-------|-------|-------|-------|
| Brier Score | Mean squared error vs resolved outcome (lower = better) | tracked | tracked | pending | pending |
| Calibration | How close probability estimates are to actual frequencies | tracked | tracked | pending | pending |
| Simulated Alpha | Profit/loss if betting when our estimate diverges >10pts from crowd | tracked | tracked | pending | pending |
| Divergence Score | Novel solution rate × compute savings coefficient | N/A | partial | pending | pending |
| Compute Cost | Wall-clock seconds or token-equivalent per prediction | tracked | tracked | pending | pending |
| Compression-Adjusted Utility | Brier improvement / compute cost | N/A | N/A | pending | pending |

---

## Failure Conditions

These thresholds determine whether the latent approach is worth pursuing:

- **Latent Brier > Text Brier after 30 days:** Red flag. Latent agents are less accurate. Stop and reassess.
- **Divergence Score < 1.2×:** Red flag per BRAIN.md Week 4 failure condition. Do not proceed to revenue track.
- **Latent compute cost > text compute cost with no accuracy gain:** Architecture coupling problem. Investigate layer selection.
- **Contrarian consistently beats swarm average:** Reconsider aggregation method — simple average may be diluting edge.

---

## Adversarial Robustness Test (Week 4 addition)

One agent is designated as an adversarial agent whose goal is to inject misleading signals into the latent channel. We measure:
- How often the swarm collapses to the adversarial estimate
- Whether the KL-Divergence Watchdog catches the drift
- Recovery time after adversarial injection

This test proves that useful divergence is functional, not cosmetic — the system maintains calibration even under adversarial pressure.

---

## Week 3 Build Plan (Mac Mini arrival April 9-16)

**Day 1 of Mac Mini:**
1. Clone repo, install Docker + NemoClaw
2. Pull Phi-3 Mini 3.8B locally — confirm loads in 24GB
3. Run `experiments/week2/` hidden state extraction scripts to confirm fidelity on new hardware
4. Build `04_single_latent.py` — Arm 3

**Day 2-3:**
5. Build `05_latent_swarm.py` — Arm 4
6. Connect Shadow Self governance layer
7. Run first four-arm comparison on seed markets
8. Log results to daily tracker

**Day 4-7:**
9. Run full 7-day four-arm benchmark
10. Calculate Brier scores once short-horizon markets resolve
11. Generate compression-adjusted utility graph (the investor slide)

---

## Expected Output

A single graph showing utility per dollar across all four arms. If latent swarm wins on this metric, we have the core result for:
- Rain grant deliverable
- arXiv preprint (Divergence Score v1)
- Pre-seed investor deck slide

---

## Notes

- This spec is intentionally conservative. We are not claiming latent will win. We are designing a fair test that would reveal it if it does.
- The seed file markets (`policy_markets_seed.json`) are long-horizon (months to years). For Brier score calculation, shorter-horizon markets from authenticated Kalshi API will be needed. Kalshi RSA auth is deferred to week of April 1.
- All code will be open-sourced with the preprint.

---
Last updated: 2026-03-30
Author: LatentForge / Three-Engine System
