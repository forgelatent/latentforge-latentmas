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
