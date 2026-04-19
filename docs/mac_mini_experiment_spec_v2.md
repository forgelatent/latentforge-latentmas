🚨 OLD DATA — see docs/INCIDENT_2026-04-18.md for details
LatentForge Mac Mini A/B Experiment Spec — v2.0
Pre-registered April 11, 2026. Revised after Grok independent review.
Lock date: before Mac Mini first boot. No amendments after first run.

---

Governing Principle

Every arm runs Phi-3 Mini 3.8B, same checkpoint, same quantization level, same temperature. No mixing model families. No post-hoc market selection. No threshold adjustments after results are seen. Results scored against this spec exactly as written.

---

Reproducibility Block
Lock these values before first run. Log in experiments/week4/run_manifest.md.

Model: Phi-3 Mini 3.8B
Checkpoint hash: [record before first run]
Quantization: 4-bit (confirm on Mac Mini load)
Temperature: 0.0 (deterministic)
Random seed: 42 (all arms)
Sparsity method: Top-k, k=128
Sparsity commit hash: [record before first run]
Shadow Self model: TinyLlama 1.1B
Shadow Self checkpoint hash: [record before first run]
Prompt version hash: [md5 of prompt files before first run]

Any deviation from these values during a run must be logged immediately. That run is labeled as a variant, not a primary result.

---

The Four Arms

Arm 1 — Text Single-Agent: Single Phi-3 Mini, text prompt, no swarm
Arm 2 — Text Swarm: 3-agent text swarm (Macro, Quant, Contrarian)
Arm 3 — Latent Single-Agent: Single Phi-3 Mini via latent delta
Arm 4 — Latent Swarm: 3-agent latent swarm, same roles

Markets: The same 11 policy/macro/geopolitical markets in the current Shadow Match baseline. No substitutions. If a market resolves before all arms run, it is scored and logged — not removed.

Timing: All four arms run on the same day against the same market snapshot. Crowd probability pulled once per session at run start, used identically across all four arms. No arm gets fresher data.

Statistical analysis: For every Brier and BSS delta reported, compute 95% confidence intervals and p-values using paired bootstrap resampling (10,000 iterations). Report exact N (markets scored) alongside every number. No delta is cited as meaningful without p<0.05. Multiple-testing correction (Bonferroni) applied when comparing across all five tests simultaneously.

Note on prior exposure: The 11 markets have been tracked by the text swarm for 8+ days. This is acknowledged. These runs are therefore labeled as validation (known market set, internal benchmark) not out-of-sample generalization. Out-of-sample generalization claims require a fresh market set added after pre-registration — target this for Week 5 extension if primary benchmark passes.

---

Pre-Run Gate: Latent Echo Test

Run before any benchmark data is collected. If it fails, stop. Fix W_a alignment before proceeding.

Protocol:
1. Agent A receives a market description as a text prompt
2. Agent A generates a latent delta
3. Shadow Self decodes the delta to English
4. Score semantic similarity (cosine similarity on sentence embeddings) between Agent A's original reasoning and Shadow Self's reconstruction
5. Repeat for 3 test markets drawn from the 11 Shadow Match markets

Pass threshold: >=0.95 similarity on 3 of 3 test markets

Failure response: Stop. Debug alignment matrix. Do not proceed until Echo test passes. Log failure and fix in experiments/week4/echo_log.md.

Continuous monitoring (added v2.0): The Echo test does not stop here. During the full benchmark run, log fidelity score on every inter-agent exchange across all latent arms (Arms 3 and 4). Report average fidelity per arm, minimum fidelity observed, and number of exchanges falling below 0.90. This is the continuous governability record — not just the pre-run gate.

---

The Five Motor-Car Tests

TEST 1 — PERFORMANCE

Measure: Brier score and BSS vs crowd per arm on all 11 markets. BSS = 1 - (arm Brier / crowd Brier). Primary comparison: Arm 4 (latent swarm) vs Arm 2 (text swarm). Secondary: Arm 3 vs Arm 1.

Statistical requirement: Report 95% CI and bootstrap p-value for every delta. A result is only cited if p<0.05.

Pass (car): >=15% Brier improvement, Arm 4 vs Arm 2, p<0.05.
Ambiguous: 10-15% improvement OR p>0.05 at 15%+. Do not call it. Run fresh markets for two additional weeks before revisiting.
Fail (horse): <10% improvement, or no statistical significance at any threshold.

Load-bearing status: Necessary but not sufficient. Performance alone is horse territory. Do not proceed to external claims on Test 1 alone.

---

TEST 2 — SCALING

Measure: Run latent swarm at 2, 4, and 8 agents. Run text swarm at 2, 4, and 8 agents. Use the same 11 markets for each run. Plot Brier score vs agent count for both.

Exact protocol:
- 2-agent run: Macro + Contrarian (both arms)
- 4-agent run: Macro + Quant + Contrarian + one additional role (pre-declare role before run)
- 8-agent run: duplicate each core role x2 (pre-declare before run)
- Sequential runs on Mac Mini (memory constraint). RunPod burst approved for 8-agent run if needed (~$20-50).

Pre-declared functional form: Latent holds if 4-agent and 8-agent Brier stays within 5% of 2-agent Brier. Text plateaus or degrades if 8-agent Brier is >=5% worse than 2-agent Brier, or improvement from 2->8 agents is less than half the improvement seen in latent arm over the same range.

Pass (car): Latent holds within 5% as N scales 2->8. Text plateaus or degrades by that definition.
Fail (horse): Both curves behave identically. Latent shows no scaling advantage.

Load-bearing status: Primary car signal. If this passes alongside Test 3, that is sufficient to call the substrate change real regardless of Test 1 magnitude.

---

TEST 3 — INFORMATION DENSITY

Measure: Communication cost per correct prediction unit.
- Text arms: total tokens exchanged per session per agent pair
- Latent arms: effective vector dimensions transmitted at k=128 (non-zero elements only), converted to equivalent float16 bytes
- Efficiency ratio: (text tokens x bytes per token) / (latent effective bytes), normalized per Brier point gained

Lock before run: Sparsity implementation commit hash recorded in run manifest. k=128 fixed. No post-hoc k adjustment.

Shadow Self overhead: Measure separately — record compute time and memory consumed by TinyLlama 1.1B translation layer as % of total session compute. Report alongside efficiency ratio. If overhead >20%, note explicitly — it weakens the efficiency claim and must be disclosed.

Pass (car): >=10x efficiency ratio, Shadow Self overhead <20%.
Ambiguous: 3-10x ratio, or overhead 20-30%.
Fail (horse): <3x ratio, or overhead >30%.

Load-bearing status: Primary car signal alongside Test 2.

---

TEST 4 — INEFFABLE ALPHA

Measure: Markets where latent swarm (Arm 4) diverges from text swarm (Arm 2) by >10 percentage points AND from crowd by >10 percentage points AND later resolves correctly.

Statistical requirement (added v2.0): A single win is insufficient. Require >=2 confirmed markets. Additionally, run a non-parametric test (sign test or permutation test) on the full distribution of Arm 4 vs Arm 2 divergences to confirm the pattern is non-random (p<0.10 acceptable given small N).

Qualitative requirement: For each candidate market, a human reviewer (John) must read the Shadow Self decoded logs and confirm the latent reasoning is genuinely novel — not a rephrasing of text swarm output. Log this judgment explicitly in experiments/week4/ineffable/. It is not sufficient to report the number alone.

Pass (car): >=2 confirmed markets + non-random divergence test p<0.10 + human review confirms novelty.
Candidate tracking: Any market where Arm 4 diverges from Arm 2 by >10 points is logged in real time as a candidate. Scored on resolution.
Fail (horse): Fewer than 2 confirmed markets, or non-random test fails, or human review finds no genuine novelty.

---

TEST 5 — GOVERNABILITY

Measure:
- Echo fidelity: average and minimum semantic similarity across all inter-agent exchanges in Arms 3 and 4 during the full benchmark run (continuous, not just pre-gate)
- Drift events: number of exchanges where cosine distance exceeds threshold and triggers Safe Mode
- False positive rate: Safe Mode triggers on exchanges that human review judges as semantically stable

Pass (car): Average Echo fidelity >=0.90 across full benchmark. Minimum fidelity >=0.85 on any single exchange. Drift detection triggers on genuine divergence confirmed by human review. Zero runaway drift events (fidelity dropping below 0.75 without Safe Mode triggering).
Fail (horse): Average fidelity <0.85. Safe Mode either never triggers (detection broken) or triggers constantly (system unstable). Any fidelity drop below 0.75 without Safe Mode catch.

---

Scoring and Overall Verdict

Test weights — explicit (added v2.0):

Scaling (Test 2) — Load-bearing: Primary car signal — cannot be faked by model quality
Information Density (Test 3) — Load-bearing: Primary car signal — proves substrate change
Performance (Test 1) — Supporting: Necessary but not sufficient alone
Ineffable Alpha (Test 4) — Supporting: Qualitative proof — powerful but harder to defend statistically
Governability (Test 5) — Gate: Must pass for any external claim — system must be stable

Verdict rules:

Car — proceed to revenue track and publication:
Both load-bearing tests (2 + 3) pass AND Governability (5) passes AND at least one supporting test (1 or 4) passes.

Faster horse — iterate before external claims:
Governability passes but one or both load-bearing tests fail or are ambiguous. Identify which latent channel component failed. Iterate on compression (efference copy, SDR, topological drift) before re-running.

Full dual-engine reassessment:
Governability fails OR both load-bearing tests fail. Stop. Do not proceed. Post full logs to LatentMAS Discord. Dual-engine review before any next step.

---

Output Artifacts

All output feeds directly into the benchmark report and the Day 30 conversations.

Run manifest — experiments/week4/run_manifest.md — Reproducibility, every external claim
Echo test log (pre-gate + continuous) — experiments/week4/echo_log.md — Transparency inversion proof
Brier per arm per market + CIs — experiments/week4/brier_results.md — Report Section 4, investor conversations
Scaling curve data — experiments/week4/scaling/ — Motor-car Test 2
Information density log — experiments/week4/density/ — Motor-car Test 3, efficiency claims
Shadow Self overhead log — experiments/week4/shadow_overhead/ — Test 3 disclosure, NemoClaw pitch
Ineffable alpha candidates + human review — experiments/week4/ineffable/ — Qualitative proof, pitch
Divergence distribution test results — experiments/week4/ineffable/ — Test 4 statistical defense

---

### Section 4.6 — Compression Method Tournament (Optional Day 1-2)

*Added April 12, 2026 — four-engine consensus after EOF proxy test.*

After successful pre-gate Echo Test and main four-arm benchmark, run a
small compression bake-off on the same 11 Shadow Match markets.

**Methods (all at matched effective compression ratio):**
1. Top-k sparsity k=128 — current baseline
2. EOF adaptive — 95% variance threshold, rolling-window PCA
3. EOF + sparse residual hybrid — project onto low-rank EOF basis,
   transmit sparse residual with top-k. Four-engine predicted winner.
4. Product Quantization (PQ) — sub-space quantization with codebook.
   Implement via faiss or numpy. Gold standard for vector compression.
5. Tiny learned autoencoder — 1024->64->1024 bottleneck, trained
   5-10 minutes on first batch of real hidden states.

**Evaluation per method (four layers — must use all four):**
1. Reconstruction: MSE + cosine similarity
2. Functional: KL divergence on next-token logits, top-k token agreement
3. Semantic: Shadow Self summary stability across methods
4. Efficiency: effective bits transmitted at equal functional fidelity

**Key metric:** equal functional fidelity, not just similar vector distance.

**Verdict criteria:**
- Winning method = lowest effective bits at matched functional fidelity
- If EOF + residual hybrid wins → adopt as default compression
- If PQ wins → implement codebook infrastructure before V0.1
- If top-k still wins → current architecture confirmed, no change needed

**Context:** EOF proxy test (April 12) was inconclusive — n-gram proxy
vectors are coordinate-aligned and structurally favor top-k. Real
transformer hidden states are dense and correlated — the regime where
EOF and hybrids should show advantage. This tournament is the definitive
test.

Results logged to: experiments/week4/compression_tournament/
