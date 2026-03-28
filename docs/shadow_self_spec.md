# Shadow Self — Technical Specification v0.1
LatentForge governance layer for latent agent communication
Written: March 28, 2026
Status: Pre-implementation — ready for Week 3 Mac Mini execution

---

## What Shadow Self Is

Shadow Self is a lightweight monitor that runs alongside a latent agent swarm and translates the vector communication stream into human-readable English in real time.

It does not control the agents. It does not modify the latent channel. It only observes, translates, and alerts.

The analogy: Shadow Self is a court reporter sitting in the room while two people speak in a foreign language. It writes down what they said in English. If they start speaking too fast or too strangely, it raises its hand and says "I can't follow this anymore."

---

## Why It Exists

Three reasons:

1. Interpretability. Investors, regulators, and enterprise customers will not trust a system they cannot read. Shadow Self makes the latent channel legible without disrupting it.

2. Safety. Latent agents can drift into regions of vector space that produce unstable or incoherent outputs. Karpathy called this "AI psychosis." Shadow Self detects drift before it compounds.

3. Audit trail. Every latent exchange gets a timestamped English translation logged to disk. One-click export for regulatory review.

---

## Architecture

Agent A sends latent delta to Agent B.
Shadow Self receives a copy of every delta as a passive tap.
Shadow Self translates, scores drift, logs everything.
If drift exceeds threshold, Safe Mode fires.

---

## Components

### 1. Delta Interceptor
Receives copy of each delta. Supports full (3072-dim) and sparse (k-dim) deltas.
Logs dims_transmitted/total_dims in every audit entry.

### 2. Translator (TinyLlama 1.1B)
Generates one English sentence per exchange describing what the latent communication appears to encode. Max 30 words. Logged with timestamp.

### 3. Drift Detector
drift_score = 1 - cosine_similarity(current_delta, rolling_mean_of_last_10)
Threshold: 0.3. If exceeded, trigger Safe Mode.

### 4. Divergence Integration
Calls score_divergence() from Script 04/05 on each exchange.
Logs divergence score (0/1/2) alongside every translation.

### 5. Safe Mode
Pauses latent exchanges. Agents fall back to text. Operator reviews and clears manually.

### 6. Audit Logger
Format per exchange:
TIMESTAMP | Exchange N | dims_transmitted/3072 | fidelity | drift_score | divergence_score | translation | REVIEW_REQUIRED | Safe Mode

Output: /workspace/logs/shadow_self_YYYY-MM-DD.log

---

## Translation Quality Gate

First 10 translations flagged REVIEW_REQUIRED.
John manually reads before system runs unattended.

---

## Benchmark Script Integration

Imports only — do not rewrite:
- apply_topk_sparsity() from Script 05
- score_divergence() from Script 04
- extract_hidden_state() from Script 04

---

## Implementation Plan — Week 3

Day 1: Boot Mac Mini. Docker + NemoClaw. Clone repo. Pull Nemotron 8B + TinyLlama 1.1B. Confirm both load in 24GB.
Day 2: Delta Interceptor. Wire into existing pipeline.
Day 3: Translator. First 5 test exchanges. Capture first translation to disk.
Day 4: Drift Detector. Trigger Safe Mode artificially. Confirm it fires.
Day 5: Audit Logger. Full end-to-end 10-exchange test. Commit everything.

---

## Success Criteria

Both models load in 24GB without swap.
First translation captured — one readable sentence per exchange.
Drift detection fires at cosine distance > 0.3.
Divergence score logged in every audit entry.
Full audit log written with every exchange timestamped.
10-exchange end-to-end run with no crashes.

---

## The Investor Pitch This Creates

Every communication between our agents is logged in human-readable English in real time, with automatic drift detection that pauses the system if communication moves outside interpretable bounds. One-click audit export for regulatory review.

---

## Open Questions for Week 3

- [ ] TinyLlama 1.1B translation quality — upgrade to Phi-3 Mini if needed
- [ ] Drift threshold of 0.3 — tune on first 20 exchanges
- [ ] Log format — plain text v0.1, migrate to JSON for Week 4 dashboard
- [ ] Safe Mode recovery — manual operator clear only in v0.1

---

Version: 0.1 — includes Divergent Engine amendments March 28 2026
Next review: Week 3 Day 5 — after first end-to-end run
