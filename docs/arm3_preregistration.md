# LatentForge Arm 3 Benchmark — Pre-Registration Document
**Registered:** April 7, 2026
**Registered by:** John McGuire, LatentForge
**Purpose:** Eliminate "optimized after seeing results" objection. This document locks all benchmark parameters before Arm 3 (latent agents) runs for the first time on the Mac Mini.

---

## 1. Hypothesis

Latent-communicating agents (Arm 3) will produce measurably better probabilistic calibration and more useful divergence from crowd consensus than text-based agents (Arm 2) on identical prediction markets, using identical base models, at identical prediction timestamps.

Primary success criterion: Arm 3 Brier score < Arm 2 Brier score on the same resolved markets.
Secondary criterion: Arm 3 divergence from crowd is directionally correct more often than Arm 2.

---

## 2. Markets Included

The same 11 markets currently tracked by the text swarm (Arm 2):
1. Will the Fed cut rates by at least 50bps in 2026?
2. Will Bitcoin reach $150,000 by end of 2026?
3. Will AI regulation bill pass in US Congress before 2027?
4. Will Elon Musk remain CEO of Tesla through 2027?
5. Will US CPI inflation be above 3% in April 2026?
6. Will S&P 500 be above 5500 at end of April 2026?
7. Will Ethereum close above $2000 in April 2026?
8. Will US unemployment rate rise above 4.5% in Q2 2026?
9. Will Republicans win the House majority in 2026 midterms?
10. Will Democrats win the Senate majority in 2026 midterms?
11. Will US voter turnout exceed 50% in 2026 midterms?

No markets will be added or removed after this document is committed.

---

## 3. Base Model — Compute Parity

All four arms must use the same base model:
- **Model:** Phi-3 Mini 3.8B
- **Quantization:** 4-bit (Q4) to fit within Mac Mini 32GB
- **Version:** Document exact HuggingFace commit hash on Mac Mini Day 1 before first run
- **No mixing of model families across arms**

This ensures we are testing communication protocol, not model intelligence.

---

## 4. Prediction Timing

- All arms predict at the same time: nightly run window 5:00-6:00am SF time
- Crowd baseline (Arm 4) snapshot taken at same timestamp as agent predictions
- No predictions made after crowd price has moved significantly on breaking news
- Timestamp logged in output file for every prediction

---

## 5. Scoring Method

- **Primary metric:** Brier score per market, averaged across resolved markets
- **Secondary metric:** Brier Skill Score (BSS) relative to crowd baseline
- **Cluster weighting:** Markets grouped by theme (Macro, Crypto, AI/Tech, Politics). Results reported per cluster and overall. AI regulation does not count as multiple independent wins.
- **Statistical significance:** Confidence intervals reported at Day 30. Minimum 15 resolved markets required before claiming statistical significance.
- **No retroactive exclusions:** Once a market is included, it stays in the scoring set regardless of outcome.

---

## 6. Latent Echo Test — Must Pass Before Arm 3 Starts

Before any benchmark predictions:
1. Agent A sends a latent delta about a market to Agent B
2. Shadow Self decodes the delta to English
3. Compare decoded English to Agent A original prompt/intent
4. If semantic divergence >5%, W_a alignment matrix is failing — stop, fix, retest
5. Document Echo test result and date in this file before proceeding

**Echo test result:** [ ] PENDING — complete on Mac Mini Day 1

---

## 7. What Would Invalidate the Results

- Base model differs across arms
- Prediction timestamps differ by more than 30 minutes across arms
- Markets added or removed after this document is committed
- Fewer than 10 markets resolved by Day 30

---

## 8. Signature

This document was written and committed before Arm 3 ran a single prediction.
Commit hash of this file serves as the registration timestamp.

John McGuire — LatentForge — April 7, 2026
