# LatentForge Steering Results — April 17, 2026
## Private Internal Document — Day 14 of 30
## Classification: Internal Only — Do Not Share Externally

---

## 1. PURPOSE

This document records the honest results of activation steering experiments
conducted on Mac Mini M4 Pro (Phi-3 Mini 3.8B, MPS) on April 15-17, 2026.
It is a factual internal record, not a marketing document.
Nothing in this document should be shared externally until we have
demonstrated real revenue generation.

---

## 2. WHAT WE TESTED

Method: Contrastive activation steering
Vector: h_bull - h_bear (bullish hidden state minus bearish hidden state)
Injection: Residual stream at layers [16, 20, 24], scale 0.4
Decoding: Greedy (do_sample=False) — any output difference is from injection only
Model: Phi-3 Mini 3.8B on Apple Silicon M4 Pro MPS
Markets: All 11 Shadow Match markets

---

## 3. FULL 11-MARKET SCORECARD

| Market | Crowd | Control | Steered | Delta | Result |
|--------|-------|---------|---------|-------|--------|
| Bitcoin 60k vs 80k first | 65% | 45% | 75% | +30pts | WORKS |
| US-Iran nuclear deal | 22.5% | 15% | 35% | +20pts | WORKS |
| Jerome Powell Fed Chair | 0.1% | 10% | 25% | +15pts | WORKS |
| 9 Fed rate cuts 2026 | 0.4% | 1.2% | 15% | +13.8pts | WORKS |
| China blockade Taiwan | 3.6% | 1.5% | 1.5% | 0pts | FLAT |
| AI regulation bill 2026 | 31% | 45% | 45% | 0pts | FLAT |
| PPP South Korea 2026 | 4.2% | refusal | refusal | — | REFUSAL |
| Ron DeSantis 2028 GOP | 2.6% | refusal | refusal | — | REFUSAL |
| Pete Buttigieg 2028 Dem | 3.8% | refusal | refusal | — | REFUSAL |
| JD Vance 2028 President | 17.6% | refusal | refusal | — | REFUSAL |
| Gavin Newsom 2028 | 17.2% | refusal | refusal | — | REFUSAL |

Summary: 4 of 11 markets show genuine directional steering.
7 of 11 do not respond (5 refusals, 2 flat).

---

## 4. WHAT IS HONESTLY CONFIRMED

### Confirmed
1. Latent transport — fidelity 1.0000 at 24x compression (Phi-3 Mini, RunPod A40)
2. Activation steering — injection deterministically changes output
3. Bullish directional steering — confirmed on 4 markets with genuine reasoning change
   - Bitcoin: reasoning shifted to institutional inflows, positive momentum
   - Iran-nuclear: reasoning shifted to mutual interests, stabilization
   - Powell: reasoning shifted to Senate support, experience alignment
   - Fed cuts: reasoning shifted to economic indicators supporting cuts
4. Pattern identified: works on financial and monetary policy probability questions
   with numeric crowd anchors. Fails on elections and extreme geopolitical events.

### Not Confirmed
- Bearish directional steering (tested exhaustively — see Section 5)
- Symmetric bidirectional control
- Latent steering superiority over text baseline (not yet A/B tested)
- Generalization beyond Phi-3 Mini on MPS

### Do Not Cite Externally
- Bearish control
- Bidirectional steering
- Results on election markets
- Taiwan result
- Phase 10 divergence as latent channel evidence

---

## 5. BEARISH CLOSURE

Bearish steering was tested exhaustively. All methods failed.

| Method | Layers | Scales Tested | Result |
|--------|--------|---------------|--------|
| h_bear - h_neutral (normalized) | [16,20,24] | 0.3 to 2.0 | Flat |
| h_bear - h_bull (normalized) | [16,20,24] | 0.3 to 0.45 | Flat |
| Raw negative injection | [16,20,24] | 0.3 to 0.45 | Word salad |
| h_bear - h_bull (normalized) | [28,29,30] | 0.5 to 1.5 | Flat |
| h_bear - h_bull (normalized) | [29,30,31] | 0.5 to 1.5 | Flat |
| h_bear - h_bull (normalized) | [30,31] | 0.5 to 1.5 | Flat |

Conclusion: Residual stream injection cannot produce downward semantic
pressure on Phi-3 Mini at any tested layer or scale. This is a model
geometry constraint — the bullish and bearish hidden states are 97%
similar (cosine similarity 0.9728). The 3% difference is accessible
in one direction only. This is not a protocol flaw.

---

## 6. MAPPING TO THE 5-STEP PLAN

### Step 1 — Latent Language (BUILD THE CHANNEL)
Status: COMPLETE
- Latent transport confirmed at 24x compression with 1.0000 fidelity
- Activation steering confirmed — injection influences generation
- Bullish directional steering confirmed on 4 market types
- Bearish asymmetry documented as model geometry finding

### Step 2 — Divergent Thinking (MAKE AGENTS THINK DIFFERENTLY)
Status: PARTIAL
- Text swarm produces divergence from crowd on policy markets
  (19+ consecutive days, AI regulation swarm 21% vs crowd 31%)
- Latent steering shifts probability estimates AND reasoning paths
- Bearish pole unreachable limits full bidirectional divergence
- Full latent vs text A/B comparison not yet run

### Step 3 — Data Collection (BUILD THE MOAT)
Status: RUNNING
- 19+ days of daily shadow match and text swarm logged
- 30-day paper trading clock running (Day 14 of 30)
- All steering experiments logged with JSON outputs
- Activation steering results are Non-Human Reasoning Traces (NHRT)
  — valuable training data that does not exist elsewhere

### Step 4 — Small Bets (GENERATE REAL REVENUE)
Status: NOT STARTED
Prerequisites still needed:
- Bearish steering working OR accept one-directional system
- At least 25 days of paper trading data
- At least one policy market resolved with clear outcome
- Brier score on primary track (policy markets only)
Current blocker: 0 policy markets resolved. Clock runs until May 4.

### Step 5 — Super-Intelligence Opportunities
Status: NOT STARTED
This step requires Steps 1-4 to be substantially complete.

---

## 7. RECOMMENDED NEXT PRIVATE MILESTONES

### Immediate (Days 15-20)
1. Continue daily shadow match and text swarm — do not break the streak
2. Watch for first policy market resolution — this unlocks the primary
   Brier score and the first real calibration data point
3. Run additional bullish markets — US-Iran and Bitcoin variants
   to stress-test the 4-market pattern across different phrasings
4. Decide: accept one-directional system or attempt OBF/KV-level
   bearish approach (Phase 2, after Mac Studio arrives)

### Near-term (Days 20-30)
5. Complete 30-day paper trading clock (ends May 4)
6. Finalize internal benchmark report with calibration outcomes
7. Determine if text swarm divergence on AI regulation resolves
   correctly — this is the single most important pending data point
8. Build the Kalshi paper trading infrastructure (no real money)

### Revenue Prerequisites (Before Step 4)
- Minimum: 30 days paper trading + at least 3 policy markets resolved
- Preferred: AI regulation divergence resolves in swarm direction
- Required: honest Brier score on primary track (not sports markets)
- Optional but valuable: bearish steering working for short signals

### The M Path (Private)
Most likely near-term revenue path given current results:
1. Complete the clock. Publish honest internal benchmark.
2. If calibration data is strong: approach one quant fund or
   prediction market operator with a 60-day live pilot proposal.
3. Pilot structure: segregated paper book, full audit log access,
   swarm signals on policy markets only, no election markets.
4. If pilot shows edge: negotiate revenue share or licensing.
5. Build Shadow Self governance layer to make the system
   auditable enough for institutional use.

This path requires no external publication, no Jiaru outreach,
and no LinkedIn posts. It runs entirely in stealth.

---

## 8. HONEST RISK ASSESSMENT

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AI regulation resolves against swarm | Medium | High | Diversify markets, dont over-index on one signal |
| Bearish never works on Phi-3 Mini | High | Medium | Accept asymmetry, use bullish-only for long signals |
| Larger model needed for full steering | Medium | Low | M5 Mac Studio arriving June/July, 128GB |
| Competitor publishes similar result | Low-Medium | Medium | Stay dark, build revenue before publishing |
| Paper trading shows no edge | Low | High | Pivot to governance/NHRT dataset path |

---

## 9. WHAT WE DO NOT KNOW YET

1. Does bullish steering improve forecasting accuracy vs text baseline?
2. Does the AI regulation divergence resolve correctly?
3. Can bearish steering be achieved via KV-level injection (OBF)?
4. Does the effect generalize beyond Phi-3 Mini to larger models?
5. What is the Brier score on primary track after policy markets resolve?

These are the five open questions that will determine the path to Step 4.

---

Document prepared: April 17, 2026
Day 14 of 30-day paper trading clock
Hardware: Mac Mini M4 Pro 32GB, Phi-3 Mini 3.8B
Classification: Internal Only
