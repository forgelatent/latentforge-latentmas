# LatentForge Calibration Benchmark Report
## Latent Vector Multi-Agent Communication: A 30-Day Adversarial Forecasting Benchmark

**Version:** 0.1 — Skeleton (Started April 6, 2026)
**Status:** In progress — fill in as data accumulates
**Target completion:** May 7, 2026 (Day 30 of paper trading clock)
**Authors:** John McGuire, LatentForge

---

## Abstract

*(Fill in on Day 30)*

We present a 30-day benchmark of a latent vector multi-agent forecasting system against text-based baselines and crowd consensus on real-money prediction markets. Our system achieves [FINAL BRIER SCORE] average Brier score across [N] resolved markets, representing a [X]% improvement over naive baseline and [Y]% improvement over single-model shadow. The 5-market calibration subset achieves an average Brier of [0.0250 or updated], approaching superforecaster-level performance in adversarial liquid market conditions. We further present the first hardware-validated latency and fidelity comparison between latent vector and text-based agent communication, demonstrating [RESULT] on [MODEL] running on Apple M4 Pro silicon.

---

## 1. Introduction

### 1.1 Motivation

Current multi-agent AI systems communicate via natural language — converting rich internal mathematical representations into tokens, transmitting them, and reconverting. This translation is lossy, computationally expensive, and constrains agents to reason within human conceptual boundaries.

LatentForge proposes an alternative: agents communicate via compressed latent vector deltas against a shared seed vector, preserving signal fidelity while reducing inter-agent bandwidth. A Shadow Self governance layer translates all machine communication to human-readable audit logs in real time.

This report presents the first external validation of this approach on a measurable, adversarial task with ground truth resolution: real-money prediction markets.

### 1.2 Related Work

- LatentMAS (Zou et al., arXiv:2511.20639v2): Pure latent collaboration via shared KV-cache. Demonstrates 14.6% accuracy improvement and 70-83% token reduction over text-based MAS on reasoning benchmarks. LatentForge extends this to real-world forecasting with governance.
- ColdMath (Polymarket, 2025-2026): $101K profit on weather prediction markets using METAR aviation data vs consumer forecast prices. Demonstrates that systematic information processing asymmetry produces monetizable edge in prediction markets.
- Superforecasting literature (Tetlock et al.): Elite human forecasters achieve Brier scores of 0.15-0.20 on geopolitical questions. Our calibration subset at 0.0250 operates in a different regime — shorter-horizon markets with higher liquidity.

### 1.3 Contributions

1. First 30-day benchmark of latent vector multi-agent communication on real-money prediction markets
2. First hardware-validated latency/fidelity comparison between latent and text-based agent communication (Apple M4 Pro)
3. Documentation of a sustained 7+ day directional divergence from crowd consensus on AI regulation markets
4. Open methodology for reproducing the benchmark on any prediction market platform

---

## 2. System Architecture

### 2.1 Text-Based Swarm (Phase 1 — Control)

Four agents with differentiated reasoning roles:
- **Macro Analyst:** Economic fundamentals, base rates, central bank policy
- **Quant Researcher:** Market signals, momentum, crowd wisdom
- **Contrarian Forecaster:** Stress-tests assumptions, finds tail risks crowd underweights
- **Bayesian Updater:** Neutral prior, updates only on concrete evidence (added April 5, 2026)

Each agent independently estimates probability for YES outcome. Final swarm estimate = average of four agent estimates.

### 2.2 Shadow Model (Single Agent Baseline)

Single claude-sonnet-4-6 instance with no role differentiation. Provides clean single-model baseline against which swarm coordination value is measured.

### 2.3 Crowd Baseline

Polymarket last-trade price at time of prediction. Represents aggregated crowd consensus of incentivized human forecasters.

### 2.4 Naive Baseline

0.50 probability for all markets. Represents zero-information baseline.

### 2.5 Latent Vector Swarm (Phase 2 — Mac Mini A/B Test)

*(Fill in after Mac Mini arrival April 9-16)*

Model: [MODEL NAME]
Hardware: Mac Mini M4 Pro, 32GB unified memory
Compression: [K] top-k sparsity, [X]x compression ratio
Fidelity: [SCORE]
Communication protocol: Hidden state delta against shared seed vector

### 2.6 Shadow Self Governance Layer

Every agent exchange translated to human-readable audit log in real time. Drift detection via cosine distance threshold. Safe Mode triggers at threshold [X].

---

## 3. Benchmark Design

### 3.1 Market Selection Criteria

- Crowd probability between 5% and 95% (genuine uncertainty)
- Resolution within 90 days of prediction date
- Substantive policy, macro, or geopolitical content (no sports, entertainment)
- Minimum volume threshold: [X] on Polymarket

### 3.2 Scoring Methodology

**Brier Score:** (probability - outcome)² where outcome ∈ {0, 1}
Lower is better. Perfect calibration = 0. Naive baseline = 0.25.

**Metrics reported:**
- Swarm avg Brier (all markets)
- Shadow avg Brier (all markets)
- Crowd avg Brier (all markets)
- Naive baseline (0.25)
- Calibration subset Brier (markets with crowd 10-90%)
- Swarm vs naive improvement %
- Swarm vs shadow improvement %
- Swarm vs crowd improvement %

### 3.3 Timeline

| Phase | Dates | Markets | Status |
|-------|-------|---------|--------|
| Historical validation | Pre-April 4 | 18 resolved | Complete |
| Paper trading Phase 1 (text swarm) | April 4 — May 7 | 25+ tracked | In progress |
| Shadow Match baseline | April 4 — ongoing | 11 markets | In progress |
| Latent A/B test | April 9-16 — May 7 | TBD | Pending Mac Mini |

---

## 4. Results

### 4.1 Historical Validation (Pre-Benchmark)

- Markets scored: 18 resolved Polymarket questions (politics/crypto)
- Swarm Brier: **0.1376**
- Naive baseline: 0.25
- Improvement over naive: **45%**
- Note: agent errors on sports/entertainment markets — filtered in live benchmark

### 4.2 Live Paper Trading Results (Fill in daily)

**As of April 6, 2026 (Day 3):**

| Metric | Value |
|--------|-------|
| Markets tracked | 25 |
| Markets resolved | 5 |
| Swarm avg Brier (resolved) | 0.0283 |
| Crowd avg Brier (resolved) | 0.0 |
| Naive avg Brier | 0.25 |
| Calibration subset (5 markets) | 0.0250 |
| Days remaining | 27 |

*Note: Crowd Brier of 0.0 on early resolved markets reflects near-certain markets that slipped through the 5-95% filter. Filter tightened April 5. Future resolutions will be more informative.*

### 4.3 Shadow Match Results (Fill in as markets resolve)

*(Day 1: April 4, Day 2: April 6)*

Key divergences logged:
- **Jerome Powell confirmed as Fed Chair:** Crowd 0.1% vs Shadow 2-3% / Swarm 3% — both days, both models
- **US-Iran nuclear deal by June 30:** Crowd 22.5% vs Shadow 8% / Swarm 7-8% — strong consensus against crowd
- **Bitcoin $60k or $80k first:** Shadow 62% / Swarm 62% vs Crowd 65% — modest below-crowd

### 4.4 AI Regulation Divergence — Case Study

*(This section becomes the narrative spine of the report)*

**Question:** Will an AI regulation bill pass in US Congress before [DATE]?
**Crowd probability:** 31%
**Swarm estimate:** 21-28%
**Days of sustained divergence:** 7+ (as of April 6)
**Direction:** Swarm consistently below crowd

*(Fill in resolution outcome and analysis when market resolves)*

If swarm correct: Evidence of latent-layer information extraction advantage over crowd consensus on regulatory probability estimation.
If crowd correct: Documented case study of where latent swarm underweights crowd wisdom — equally publishable as a calibration lesson.

### 4.5 Latent vs Text A/B Test Results

*(Fill in after Mac Mini arrival)*

| Metric | Text Swarm | Latent Swarm | Delta |
|--------|-----------|--------------|-------|
| Avg Brier | TBD | TBD | TBD |
| Inference latency (ms) | TBD | TBD | TBD |
| Tokens per exchange | TBD | TBD | TBD |
| Compute cost per turn | TBD | TBD | TBD |
| Divergence score | TBD | TBD | TBD |

---

## 5. Discussion

### 5.1 What the Results Mean

*(Fill in on Day 30)*

### 5.2 Limitations

- Sample size: n=[X] resolved markets is small by academic standards
- Market selection: Polymarket skews toward political/crypto markets
- Time horizon: 30-day window may not capture long-horizon calibration
- Single model family: All agents use claude-sonnet-4-6; cross-model validation pending

### 5.3 Future Work

- Extend benchmark to 90 days with larger resolved market set
- Cross-model latent communication (Vision Wormhole)
- Weather market track (METAR data vs Polymarket weather prices)
- OpenSpiel divergence score benchmark

---

## 6. Conclusion

*(Fill in on Day 30)*

---

## 7. Appendix

### A. Market List (Full)

*(Auto-populate from calibration tracker JSON)*

### B. Daily Prediction Log

*(Link to calibration/predictions_log.json)*

### C. Shadow Match Full Results

*(Link to shadow_match JSON files)*

### D. Reproduction Instructions

```bash
# Clone the benchmark
git clone https://github.com/forgelatent/latentforge-latentmas

# Install dependencies
pip3 install anthropic requests

# Set API key
python3 -c "
import getpass, os
k = getpass.getpass('Paste key: ')
open(os.path.expanduser('~/.latentforge/.env'),'w').write(f'export ANTHROPIC_API_KEY=\"{k}\"\n')
"

# Run text swarm
source ~/.latentforge/.env
python3 experiments/benchmark/03_text_swarm.py

# Run calibration tracker
python3 experiments/benchmark/calibration_tracker.py

# Run shadow match
python3 experiments/week1/scripts/shadow_match.py
```

---

*Document maintained by: John McGuire, LatentForge*
*Started: April 6, 2026*
*Target completion: May 7, 2026*
*Repository: github.com/forgelatent/latentforge-latentmas*

### Additional Related Work

- **"The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling"** (arXiv:2604.03191): Academic validation that discrete tokenization creates information bottlenecks in scaling — directly supports LatentForge's core argument for continuous latent vector communication over token-based agent coordination.

- **VectorArc/AVP v0.6.1** (github.com/VectorArc/avp-python): Adjacent latent primitive protocol shipping `generate_on_context()`. Differentiator: no governance layer, no external calibration benchmark. LatentForge adds Shadow Self auditability and real-world prediction market validation.

- **SCRAT — Stochastic Control with Retrieval and Auditable Trajectories** (arXiv:2604.03201): Independent work on auditable agent trajectories, validating the governance/audit trail direction of Shadow Self.
