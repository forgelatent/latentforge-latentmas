# LatentForge Divergence vs Crowd Benchmark Tracker

**Start Date:** March 29, 2026
**Status:** Private (first 7-14 days)
**Goal:** Measure whether latent communication produces meaningfully different and better-calibrated forecasts than text-only baselines.

## Daily Summary Table

| Date | # Markets | Text Brier | Latent Brier | Crowd Brier | Divergence Rate | Notes |
|------|-----------|------------|--------------|-------------|-----------------|-------|
| 2026-03-29 | 8 | - | - | - | - | Day 1 text baseline only |

## March 29, 2026 — Day 1 (Text Baseline Only)

| # | Market | Text Prob | Crowd Prob | Latent Prob | Outcome | Divergence |
|---|--------|-----------|------------|-------------|---------|------------|
| 1 | Will the Fed cut rates by at least 50bps in 2026? | 65% | 68% | - | TBD | No |
| 2 | Will Bitcoin reach $150,000 by end of 2026? | 50% | 55% | - | TBD | No |
| 3 | Will AI regulation bill pass in US Congress before 2027? | - | 31% | - | TBD | - |
| 4 | Will Elon Musk remain CEO of Tesla through 2027? | - | 77% | - | TBD | - |
| 5 | Will US CPI inflation be above 3% in April 2026? | - | 41% | - | TBD | - |
| 6 | Will S&P 500 be above 5500 at end of April 2026? | - | 51% | - | TBD | - |
| 7 | Will Ethereum close above $2000 in April 2026? | - | 45% | - | TBD | - |
| 8 | Will US unemployment rate rise above 4.5% in Q2 2026? | - | 29% | - | TBD | - |

## Key Metrics

- **Brier Score** (lower is better) - calibration quality
- **Divergence Flag** - fires when text and latent disagree by more than 10 percentage points
- **Win Rate vs Crowd** - once latent numbers are running
- **Compute Savings** - tokens saved per exchange (Week 3+)

## Running Notes

- Day 1: Near-alignment on macro questions is expected and healthy. Text baseline is a strong model already.
- Divergence story emerges in tail events, novel correlations, and multi-agent latent swarms (Week 3+).
- Core grant framing: "We removed the lossy translation layer between agent thought and agent communication."

---
Last updated: 2026-03-29


## March 30, 2026 — Day 2 (Arms 1+2: Single Agent + Text Swarm)

| # | Market | Single | Macro | Quant | Contrarian | Swarm | Crowd | Flag |
|---|--------|--------|-------|-------|------------|-------|-------|------|
| 1 | Fed 50bps? | 65% | 72% | 65% | 55% | 64% | 68% | - |
| 2 | BTC 150K? | 50% | 48% | 52% | 45% | 48% | 55% | - |
| 3 | AI regulation? | 31% | 18% | 28% | 12% | 19% | 31% | DIVERGE |
| 4 | Musk/Tesla? | - | 71% | 74% | 62% | 69% | 77% | - |
| 5 | CPI >3%? | - | 44% | 44% | 52% | 47% | 41% | - |
| 6 | S&P >5500? | - | 54% | 53% | 58% | 55% | 51% | - |
| 7 | ETH >2K? | - | 42% | 48% | 38% | 43% | 45% | - |
| 8 | Unemployment? | - | 32% | 32% | 38% | 34% | 29% | - |

**Flag:** AI regulation swarm 19% vs crowd 31%. Contrarian at 12%.

## Contrarian Standalone Track

Contrarian is NOT a fifth arm. Logged independently to test if systematic contrarian positioning produces alpha.

| Date | Market | Contrarian | Crowd | vs Crowd |
|------|--------|------------|-------|----------|
| 2026-03-30 | Fed 50bps | 55% | 68% | -13% |
| 2026-03-30 | BTC 150K | 45% | 55% | -10% |
| 2026-03-30 | AI regulation | 12% | 31% | -19% |
| 2026-03-30 | Musk/Tesla | 62% | 77% | -15% |
| 2026-03-30 | CPI >3% | 52% | 41% | +11% |
| 2026-03-30 | S&P >5500 | 58% | 51% | +7% |
| 2026-03-30 | ETH >2K | 38% | 45% | -7% |
| 2026-03-30 | Unemployment | 38% | 29% | +9% |

Pattern: Contrarian below crowd on crypto/tech/policy. Above crowd on macro risk.
