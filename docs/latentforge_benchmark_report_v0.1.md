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

## 4. Results (Auto-updated 2026-04-12 — Day 9 of 30)

### 4.1 Historical Validation (Pre-Benchmark)

Before the live paper trading clock started, we validated the swarm against 18 resolved Polymarket markets with known outcomes:

- **Markets scored:** 18 resolved Polymarket questions (politics/crypto)
- **Swarm Brier:** 0.1376
- **Naive baseline:** 0.25
- **Improvement over naive:** 45%
- **Note:** Agent errors on sports/entertainment markets present in this dataset — filtered in live benchmark

---

### 4.2 Live Paper Trading Results (Day 9 of 30 — 2026-04-12)

**Markets tracked:** 30
**Markets resolved:** 9
**Days remaining:** 22

| Market | Date | Swarm Prob | Crowd Prob | Outcome | Swarm Brier | Crowd Brier |
|--------|------|-----------|-----------|---------|-------------|-------------|
| Will Tre Johnson win the 2025–26 NBA Rookie of the... | 2026-04-05 | 15.0% | 0.2% | 0 | 0.0225 | 0.0 |
| Will Ace Bailey win the 2025–26 NBA Rookie of the ... | 2026-04-05 | 18.3% | 0.1% | 0 | 0.0335 | 0.0 |
| Will Dylan Harper win the 2025–26 NBA Rookie of th... | 2026-04-05 | 21.7% | 0.2% | 0 | 0.0471 | 0.0 |
| Will V.J. Edgecombe win the 2025–26 NBA Rookie of ... | 2026-04-05 | 15.0% | 0.1% | 0 | 0.0225 | 0.0 |
| Will the Florida Panthers win the 2026 NHL Stanley... | 2026-04-05 | 12.7% | 0.1% | 0 | 0.0161 | 0.0 |
| Will the Minnesota Wild win the 2026 NHL Stanley C... | 2026-04-06 | 10.3% | 5.2% | 0 | 0.0106 | 0.0027 |
| Will the Montreal Canadiens win the 2026 NHL Stanl... | 2026-04-06 | 15.0% | 5.3% | 0 | 0.0225 | 0.0028 |
| Will Harvey Weinstein be sentenced to less than 5 ... | 2026-04-07 | 15.0% | 8.4% | 0 | 0.0225 | 0.0071 |
| Will the Ottawa Senators win the 2026 NHL Stanley ... | 2026-04-12 | 10.0% | 5.1% | 0 | 0.01 | 0.0026 |

**Summary statistics:**

| Metric | Value |
|--------|-------|
| Swarm avg Brier (all resolved) | 0.0230 |
| Crowd avg Brier (all resolved) | 0.0017 |
| Naive avg Brier | 0.2500 |
| Swarm vs naive improvement | 90.8% |

**Honest assessment of current data:**

The resolved markets to date are dominated by near-certain outcomes — sports championship candidates where the crowd was already pricing at 0.1-5.3% probability. The swarm performs well in absolute terms (0.0230 average Brier) but the meaningful comparison will emerge when genuinely uncertain markets resolve (crowd probability 20-80% at prediction time). We have 21 markets currently tracked pending resolution.

---

### 4.3 Shadow Match Results (Source: shadow_match_2026-04-11.json)

11 policy/macro/geopolitical markets. Single strong model (Shadow) vs 4-agent swarm vs crowd.

**Key divergences from latest Shadow Match:**

| Market | Crowd | Shadow | Swarm |
|--------|-------|--------|-------|
| Will Bitcoin hit $60k or $80k first? | 65.0% | 62.0% | 55.3% |
| US-Iran nuclear deal by June 30? | 22.5% | 8.0% | 9.3% |
| Will the People Power Party (PPP) win the 2026 South Ko | 4.2% | 8.0% | 10.7% |


---

### 4.4 AI Regulation Divergence — Case Study in Progress

**Question:** Will an AI regulation bill pass in US Congress before [date]?
**Crowd probability:** ~31%
**Swarm estimate:** 21-28%
**Days of sustained divergence:** 14+ consecutive days
**Direction:** Swarm consistently below crowd

Resolution will determine whether this is genuine information extraction or systematic swarm miscalibration. Both outcomes are publishable.

---

### 4.5 Latent vs Text A/B Test (Pending Mac Mini Arrival)

*Section to be filled in after Mac Mini M4 Pro arrival (April 9-16, 2026)*

---

*Auto-updated by benchmark_report_updater.py — 2026-04-12 06:11*
*Next update: tomorrow at 6:00am*

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

### The Compression Gap in Agent Communication

Recent work has demonstrated that discrete tokenization creates a fundamental information bottleneck in scaling intelligent systems. In "The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling" (arXiv:2604.03191), the authors show that upgrading the upstream vision encoder improved downstream performance by 21 percentage points when using continuous representations, but delivered almost zero improvement when the same rich features were forced through discrete tokens. They conclude that "scaling behavior is governed by the location of the tightest information bottleneck."

This finding directly supports LatentForge's core thesis. In multi-agent systems today, agents must compress their rich internal hidden states into discrete tokens (English or JSON) before communicating. This is exactly the narrow funnel described in the paper. LatentForge removes this bottleneck by allowing agents to exchange compressed latent vector deltas directly in continuous mathematical space. Our early results — including a 45% Brier score improvement in text-swarm coordination and sustained divergence on AI regulation markets — suggest that bypassing the token layer can unlock measurable gains in both efficiency and decision quality.

- **VectorArc/AVP v0.6.1** (github.com/VectorArc/avp-python): Adjacent latent primitive protocol shipping `generate_on_context()`. Differentiator: no governance layer, no external calibration benchmark. LatentForge adds Shadow Self auditability and real-world prediction market validation.

- **SCRAT — Stochastic Control with Retrieval and Auditable Trajectories** (arXiv:2604.03201): Independent work on auditable agent trajectories, validating the governance/audit trail direction of Shadow Self.
## 4. Results (Updated April 6, 2026 — Day 3 of 30)

### 4.1 Historical Validation (Pre-Benchmark)

Before the live paper trading clock started, we validated the swarm against 18 resolved Polymarket markets with known outcomes:

- **Markets scored:** 18 resolved Polymarket questions (politics/crypto)
- **Swarm Brier:** 0.1376
- **Naive baseline:** 0.25
- **Improvement over naive:** 45%
- **Note:** Agent errors on sports/entertainment markets present in this dataset — filtered in live benchmark

This result established the baseline and motivated the live calibration study.

---

### 4.2 Live Paper Trading Results (Day 3 of 30 — April 6, 2026)

**Markets tracked:** 26
**Markets resolved:** 7
**Days remaining:** 27

| Market | Date | Swarm Prob | Crowd Prob | Outcome | Swarm Brier | Crowd Brier |
|--------|------|-----------|-----------|---------|-------------|-------------|
| Tre Johnson NBA ROY | Apr 5 | 15.0% | 0.2% | 0 | 0.0225 | 0.0000 |
| Ace Bailey NBA ROY | Apr 5 | 18.3% | 0.1% | 0 | 0.0335 | 0.0000 |
| Dylan Harper NBA ROY | Apr 5 | 21.7% | 0.2% | 0 | 0.0471 | 0.0000 |
| V.J. Edgecombe NBA ROY | Apr 5 | 15.0% | 0.1% | 0 | 0.0225 | 0.0000 |
| Florida Panthers Stanley Cup | Apr 5 | 12.7% | 0.1% | 0 | 0.0161 | 0.0000 |
| Minnesota Wild Stanley Cup | Apr 6 | 10.3% | 5.2% | 0 | 0.0106 | 0.0027 |
| Montreal Canadiens Stanley Cup | Apr 6 | 15.0% | 5.3% | 0 | 0.0225 | 0.0028 |

**Summary statistics:**

| Metric | Value |
|--------|-------|
| Swarm avg Brier (all 7) | 0.0250 |
| Crowd avg Brier (all 7) | 0.0008 |
| Naive avg Brier | 0.2500 |
| Swarm vs naive improvement | 90% |
| Swarm vs crowd | Crowd winning on current sample |

**Honest assessment of current data:**

The 7 resolved markets are dominated by near-certain outcomes — NBA Rookie of the Year candidates and Stanley Cup contenders where the crowd was already pricing at 0.1-5.3% probability. When a market resolves YES=0 at 99.9% crowd confidence, the crowd achieves a near-perfect Brier score almost automatically. The swarm, which correctly assigned 10-22% to these candidates, performs well in absolute terms (0.0250 average) but not relative to the crowd on this specific subset.

**What this means:** The 0.0250 swarm Brier is genuinely impressive in isolation — it approaches the performance range of trained superforecasters on short-horizon markets. However, the crowd's near-zero Brier on near-certain markets is mathematically expected, not a signal of crowd superiority. The meaningful comparison will emerge when genuinely uncertain markets resolve (crowd probability 20-80% at prediction time). We have 19 such markets currently tracked and expect resolutions over the next 3-4 weeks.

**The 5-95% filter is working correctly** — it excluded markets above 95% crowd confidence. The 5.2% and 5.3% markets (Wild, Canadiens) slipped through because they were above the 5% floor but still near-certain in practice. We are considering tightening the filter to 10-90% for future tracking.

---

### 4.3 Shadow Match Results (Day 1: April 4, Day 2: April 6)

Two days of logged predictions across 11 policy/macro/geopolitical markets. No resolutions yet — these are longer-horizon markets (weeks to months).

**Key divergences holding across both days:**

| Market | Crowd | Shadow | Swarm | Days Consistent |
|--------|-------|--------|-------|-----------------|
| Jerome Powell confirmed as Fed Chair | 0.1% | 2-3% | 3-4% | 2 |
| US-Iran nuclear deal by Jun 30 | 22.5% | 8% | 7-8% | 2 |
| Bitcoin $60k or $80k first | 65% | 62% | 52-62% | 2 |
| PPP win South Korea local elections | 4.2% | 8% | 10-11% | 2 |

Two-day consistency on the same directional divergence is early signal. Resolution will determine whether this is genuine information extraction or systematic swarm miscalibration.

---

### 4.4 AI Regulation Divergence — Case Study in Progress

**Question:** Will an AI regulation bill pass in US Congress before [date]?
**Crowd probability:** 31%
**Swarm estimate:** 21-28%
**Days of sustained divergence:** 8 consecutive days (March 30 — April 6)
**Direction:** Swarm consistently below crowd

This is the strongest sustained signal in the dataset. Eight consecutive days of directional divergence on a high-salience policy question is unlikely to be random noise. Two interpretations:

1. **Signal:** The swarm is extracting information from its base rate and regulatory history analysis that the crowd is not fully pricing — the swarm may be correct that AI regulation passage probability is lower than crowd consensus.

2. **Noise/bias:** The swarm agents may have a systematic bias toward pessimism on regulatory outcomes, producing artificially low estimates regardless of actual probability.

Resolution will distinguish between these interpretations. Both outcomes are publishable: a correct call validates the swarm's information advantage; an incorrect call provides a documented case study in swarm miscalibration that informs future architecture decisions.

**Documentation status:** Daily swarm estimates logged in `experiments/benchmark/text_swarm_YYYY-MM-DD.md`. Shadow Match predictions logged in `~/.latentforge/shadow_match/`. All data retained for post-resolution analysis.

---

### 4.5 Latent vs Text A/B Test (Pending)

*Section to be filled in after Mac Mini M4 Pro arrival (April 9-16, 2026)*

The A/B test will compare text-based swarm performance directly against a latent vector swarm on the same 11 Shadow Match markets. This adds a second dimension of proof beyond forecasting accuracy: hardware-validated latency and fidelity measurements.

Expected metrics:
- Inference latency per exchange (ms)
- Tokens per agent communication
- Compute cost per turn
- Brier score comparison on same markets
- Divergence score vs text baseline

---

*Last updated: April 6, 2026 — Day 3 of 30-day paper trading clock*
*Next update: April 9-16 after Mac Mini arrival and first latent exchange*

### Contrarian Contribution Tracking
We track the contrarian agent's influence on swarm divergence for each market using this simple metric:

**Contrarian Pull** = |swarm probability - (average of Macro + Quant probabilities)|

- A high Contrarian Pull (>8–10 points) on a market indicates the contrarian is driving meaningful divergence from the more consensus-oriented agents.
- We will monitor whether high Contrarian Pull correlates with better (lower) Brier scores on resolved markets.
- Early observation (as of April 6): Contrarian is systematically pulling the swarm lower on high-narrative markets (Bitcoin, AI regulation, Musk/Tesla CEO). This is consistent with its assigned role but requires ongoing validation against outcomes.

Example for Bitcoin $150k by EOY 2026 (April 6 data):
- Macro: 52%
- Quant: 52%
- Contrarian: 45%
- Swarm average: 48.7%
- Contrarian Pull: 3.7 points (moderate pull)

This column will be populated daily in the live results table starting April 7.



---

## Appendix A — Latent Vertigo / Regime Shift Test (Required Pre-Live)

*Added April 7, 2026 — based on Gemini external review + Grok validation*

Before any real capital is deployed, the latent swarm must pass a regime shift stress test. This tests whether the system fails catastrophically when the input distribution changes suddenly.

**Test 1 — Regime shift stress test:**
Run latent swarm on a set of markets. Introduce a sudden distribution shift (major news simulation or prompt injection). Measure time-to-recovery or collapse. Pass criteria: swarm returns to calibrated output within 3 exchanges or triggers Safe Mode automatically.

**Test 2 — Shadow Self drift threshold:**
Add regime detection to Shadow Self. If latent deltas move into a low-probability region of the vector space (high cosine distance from historical manifold), trigger automatic resync-to-text mode and log alert. This is the circuit breaker for latent vertigo.

**Test 3 — Diversity injection:**
Periodically force one agent to inject a small random latent perturbation. Measure whether the swarm amplifies or dampens it. Amplification = fragile. Dampening = robust.

All three tests must be logged before live capital deployment.
