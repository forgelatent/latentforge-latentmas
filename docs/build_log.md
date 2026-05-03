# LatentForge — Build Log

*Last updated: May 3, 2026 — initial draft*

# 1. The architecture

## 1.1 What this project is for

LatentForge exists to remove a specific bottleneck in multi-agent AI systems: the lossy translation between mathematical hidden states and human language. Today's autonomous agents communicate by converting rich internal thought-objects into words, transmitting tokens, and reconverting on the other side. The conversion costs compute, forces agents to think inside human conceptual boundaries, and discards information that has no clean linguistic description. The project's central claim is that agents can communicate directly via compressed vector deltas against a shared seed vector, in continuous high-dimensional space, and that doing so produces both cheaper coordination and a class of insights text-based systems cannot reach. A constitutional Shadow Self governance layer translates these machine exchanges into human-readable audit logs in real time, so the system remains interpretable and regulatorily defensible.

The project's strategic framing names this distinction sharply. Existing multi-agent systems are *faster horses*: better orchestration of agents that still talk in tokens. LatentForge's claim is to remove the horse — to build the *motor car* — by making the inter-agent channel native to the model's own representation space rather than to human language.

This framing carries a discipline as well as a thesis. The motor-car analogy can become a shield against criticism if external claims outrun measurement. The project commits explicitly to the analogy as a *measurement tool*, not a marketing narrative: a verdict requires concrete evidence across specific tests, and partial evidence does not license full claims.

*Reproducer: BRAIN.md Section 1 (Thesis) and Section 15 (one-sentence pitches), plus April 11 entry "Discipline against self-flattery (Grok): The Henry Ford analogy is dangerous if it becomes a shield against criticism."*

## 1.2 The three-engine system

The project is run by a non-technical founder. From founding (March 22, 2026), the operating model has been a deliberate three-engine system: Founder Engine (John, vision and execution and final authority), Systems Engine (Claude, accumulated reasoning across sessions, structural consistency), Divergent Thinking Engine (Grok/Supergrok, real-time intelligence and pattern-spotting). Each engine owns a distinct domain. Each has explicit constraints — the founder is non-technical, Claude has no memory between sessions, Grok has less context on accumulated project history.

The architecture is deliberate, not opportunistic. The founding rationale: no single intelligence owns complete engineering judgment. A solo non-technical founder, a sessionless Claude, and a context-poor Grok each have gaps. Three intelligences with overlapping but distinct strengths produce coverage no single one provides.

The system also pre-commits to handling disagreement. When Systems Engine and Divergent Thinking Engine substantively disagree on architecture, fundraising, customer targeting, or pivots, the disagreement itself is treated as the primary signal of high-uncertainty decisions. It escalates to the Founder Engine for resolution rather than being resolved by picking the engine that confirms an existing inclination. The named failure mode — "cherry-picking the engine that agrees with your existing bias" — is a documented anti-rationalization protocol from Day 1.

| Engine | Owns | Constraint |
|---|---|---|
| Founder (John) | Vision, market, execution, final decisions | Non-technical; must build fluency to spot suspicious results |
| Systems (Claude) | Technical strategy, architecture, structural consistency | No memory between sessions; outputs must be committed or lost |
| Divergent (Grok) | Strategic intelligence, trends, real-time pattern spotting | Less context on accumulated project history |

*Reproducer: BRAIN.md Sections 0 and 0b (Three-Engine System and Dual-Engine Review Protocol), plus Section 5 (Full Team).*

## 1.3 The four-arm benchmark

The project's central scientific claim is testable, not assumed. To make the test fair, the experimental design is a 2×2: communication channel (text vs latent) crossed with agent structure (single-agent vs swarm). This produces four arms:

| Arm | Communication | Structure |
|---|---|---|
| Arm 1 | Text | Single agent |
| Arm 2 | Text | Swarm (3 agents) |
| Arm 3 | Latent | Single agent |
| Arm 4 | Latent | Swarm (3 agents) |

The 2×2 isolates the variable being tested. A two-arm design (text vs latent) was rejected because it cannot distinguish gains from communication channel from gains from agent structure. If the latent arm wins but only the swarm versions win, the breakthrough is structured multi-agent reasoning, not the latent channel — and the project iterates harder on the latent part. If text-swarm matches latent-swarm, similar conclusion. The four-arm design forces the question to be answerable.

A second design discipline holds the base model constant across all four arms. Phi-3 Mini 3.8B is the canonical model. Different models per arm would conflate model capability with protocol effectiveness, testing model intelligence rather than communication protocol. Compute parity is non-negotiable.

A third discipline is pre-registration. The Mac Mini experiment specification (`docs/mac_mini_experiment_spec_v2.md`) was locked April 11, 2026 — markets, timing, scoring methodology, and statistical thresholds committed in writing before the Mac Mini arrived. The discipline closes off "you optimized after seeing results" objections.

Within the four-arm design, text-swarm has a specific role: rigorous *control arm*. It is not the destination, not a forecasting product, not a revenue path on its own. It exists so that when latent results arrive, the comparison is meaningful. If latent performs roughly the same as text, the breakthrough was structured reasoning, not the latent channel.

*Reproducer: BRAIN.md March 30 entries ("Four-arm benchmark design locked"), April 7 entry ("Compute parity — Phi-3 Mini across all four arms"), April 11 entry ("Mac Mini Experiment Spec Pre-Registered v2.0"), and Section 15 note on text-swarm as control arm.*

## 1.4 The proof architecture has two arms

Beyond the scientific four-arm benchmark, the project operates a parallel measurement layer: prediction markets as an adversarial validation surface. This is not the same as the four-arm benchmark. The two arms serve different functions and produce different evidence.

The **scientific arm** is the Mac Mini activation steering work. It tests whether latent vector communication can be made to influence agent generation in a controlled experiment, with stance-specific reasoning and falsifiable success criteria. The April 15, 2026 "first flight" result — a bullish contrastive vector injected at layers 16/20/24 at scale 0.4 producing a controlled directional shift in Agent B output (35% → 75%) with stance-specific reasoning generated alongside — is the canonical scientific evidence.

The **revenue-exploration arm** is the prediction-market measurement infrastructure. Polymarket and Kalshi data pulls, the text-swarm running on 11 fixed benchmark questions, the calibration-tracker scoring predictions against resolved markets. This arm produces continuous calibration evidence on real-world markets where ground truth is unavoidable. Its value is twofold: it produces a forecasting track record that can support business model paths (governance layer customers, dataset licensing, synthetic alpha fund), and it provides a real-world adversarial complement to the scientific arm's controlled experiments.

The arms are designed to be independent. A failure on the revenue-exploration arm (the project doesn't outpredict prediction markets) does not invalidate the scientific arm's claims about latent communication. Conversely, success in the scientific arm doesn't automatically translate to forecasting alpha. Both arms must produce evidence on their own terms.

*Reproducer: intent.md "What we have proven" and "What we are still trying to prove" sections; BRAIN.md April 14 (Phase 11) and April 15 (semantic invariance test) entries for scientific arm; BRAIN.md April 4 (calibration tracker live) and Section 9 (Track A: Polymarket Bot) for revenue-exploration arm.*

## 1.5 The motor-car tests

The motor-car analogy generates four specific tests for whether the project has actually built something new, or only built a faster horse. The tests come from external review (ChatGPT framing, April 11) and were locked into the project's evaluation framework on the same day.

| Test | Question |
|---|---|
| Economics | Does it change the economics? Does latent scale differently than text? |
| Performance ceiling | Does it open domains text agents cannot enter? |
| Architecture | Does it change the system architecture around it? Does new infrastructure emerge? |
| Norms | Does it change what becomes normal? Does latent-native coordination become the default? |

The associated discipline: **a verdict requires concrete evidence across at least two of the four tests.** Performance alone (a better Brier score, a lower compute cost) is "horse territory." External claims of having built the motor car are gated on multi-test evidence, not single-metric evidence.

This discipline was tested April 14-15 in real time. The Phase 10 scaling test produced a result that looked like motor-car evidence (latent swarms preserved more divergence than text swarms as agent count scaled). Phase 11 then revealed the divergence came from agent role diversity, not from the latent channel — the latent channel was not actually influencing generation. The Phase 10 result was relabeled "Role Diversity Scaling Result" and removed from the motor-car evidence list. The discipline held: a result that looked like multi-test evidence was retracted to single-test evidence (and not even that, since it didn't measure what was claimed) before any external claim was made.

*Reproducer: BRAIN.md April 11 entry "Strategic Framing: The Motor Car Tests (All Four Engines)" plus April 14 entries on Phase 10 and Phase 11.*

## 1.6 The Transparency Inversion

The standard objection to latent inter-agent communication is that humans cannot read it, making the system less auditable than text-based systems. The project's structural counter is that text appears transparent but is lossy: humans see the words the model chose to output, not the internal state that generated them. Words are a compression of reasoning, post-hoc, curated by the model. Latent + Shadow Self captures the full internal state, translates it systematically, and produces consistent replayable auditable logs. Both the raw mathematical exchange and the human-readable translation are preserved, and the gap between them can itself be audited.

The architecture treats this counter as a claim that must be earned, not asserted. Three proofs are required before the Transparency Inversion is used in external pitches:

1. **Deterministic reconstruction** — the same latent delta produces the same English explanation. Measured by Echo Test fidelity ≥0.90 across the full benchmark run, continuous (not just pre-gate).
2. **Drift detection** — the system reliably flags semantic divergence before it becomes uncontrolled. Measured by Safe Mode trigger accuracy in scaling runs.
3. **Fidelity metrics** — the gap between raw latent intent and decoded explanation is quantified, logged per exchange, reported per arm.

All three proofs come from the Mac Mini benchmark run. They are not theoretical claims — they are measured outputs. The discipline pre-commits the pitch to the measurement: pitch-readiness is gated on measurement-readiness. No proof, no pitch.

*Reproducer: BRAIN.md April 11 entry "Transparency Inversion — Sharpened" with the three explicit proofs.*

## 1.7 The NHRT dataset moat

The project's daily logging activity is itself part of the strategic architecture. Every latent exchange between agents, every Shadow Self translation, every calibration outcome on prediction markets, every Echo fidelity score — these accumulate into a category of data the project calls Non-Human Reasoning Traces (NHRT). High-entropy, structurally impossible to generate via text, and irreplaceable session-by-session.

The strategic argument is two-horizon. Near-term, NHRT is internal benchmark signal and training data. Long-term, as model collapse pressures frontier labs (training on low-entropy synthetic text degrades capabilities), high-entropy non-human reasoning data becomes scarce and valuable. NHRT becomes a licensing asset — the compounding moat that runs alongside the governance-layer business, not instead of it.

The operational rule that makes this strategy real: every session that runs without logging is a dataset entry lost permanently. The discipline elevates daily logging from operational hygiene to load-bearing infrastructure. It also creates a structural reason for the Mac Mini Day 1 protocol to lock checkpoint hashes, quantization levels, and run manifests before any benchmark fires — without that grounding, the logged traces lose context and value.

*Reproducer: BRAIN.md April 11 entry "Non-Human Reasoning Traces (NHRT) — Dataset Moat Framing."*

## 1.8 The $10M external-claim threshold

The architecture commits to a specific evidence threshold for any external claim that would attract serious capital, partnerships, or research collaboration. The threshold has two parts: (1) Tier 2 reproducible internal evidence on the specific claim being made, and (2) Tier 3 externally-defensible audit chain (raw data → analysis → report) for any quantitative metric cited.

The threshold means the project does not pitch claims it has only Tier 1 (observed once, not audited) or Tier 0 (intuition / hypothesis) evidence for, even when those claims are directionally promising. The cost of cited-and-retracted claims is higher than the cost of waiting. The April 18 contamination demonstrated this concretely: Tier 1 metrics that compounded across a Rain grant draft, an outreach draft, and the v0.1 benchmark report had to be retracted from all of them simultaneously when the data source was identified as contaminated. The retraction was internal-only because the claims hadn't been pitched externally yet — but the structural lesson held: claims propagate faster than they can be retracted, and external propagation of a contaminated claim is not recoverable.

The threshold operationalizes as follows: Day 30 external conversations (planned for May 7, 2026 — though the Day 30 strategic clock was decoupled from the forecasting narrative post-reset) would only cite metrics with a Tier 2 reproducer or Tier 3 audit chain. Any metric without that backing is internal-use only or do-not-cite explicitly.

*Reproducer: intent.md Tier 1/2/3 hierarchy in "Ground Truth" section; BRAIN.md April 8 entry "0.0247 Brier number clarified" and "How to cite going forward" framework; incident_ledger.md April 18 incident.*

# 2. Per-component design rationale

This section documents each automated and manual component in the system. Each subsection describes what the component is, what problem it was built to solve, what design choices were made, what failure modes were anticipated at design time, and where in the project's history the component originated.

Components are grouped by purpose: data ingestion, research, prediction generation, strategic synthesis, and reporting. The grouping reflects the system's layered shape — data flows in at the bottom, research and prediction layers process it, strategic synthesis sits above, reporting comes out at the top.

Components currently unloaded from launchd are still documented here. Their design rationale does not disappear when they are turned off, and the documentation supports future work to bring them back online with structural fixes where needed.

## 2.1 Data ingestion

The data-ingestion components are responsible for pulling external market data into the project's working set on a daily cadence. The two components in this bucket — kalshi-pull and polymarket-pull — are structurally similar in role but were built at different times under different constraints, and the gap between their designs is itself part of the project's history.

### 2.1.1 kalshi-pull

Kalshi-pull is the component responsible for pulling Kalshi market data into the project on a daily cadence. It exists because Kalshi was identified, during the founding sprint, as the US-regulated alternative to Polymarket — Polymarket blocks US residents from live trading via geofencing, which was discovered through the Dual-Engine Review Protocol on March 24-25, 2026. Kalshi-pull was designed as the first-class data-ingestion path for any future US-resident live trading, with Polymarket retained as the primary data source for benchmark and calibration work.

| Field | Value |
|---|---|
| Schedule | 4:45 AM nightly |
| Output | `~/Projects/data/kalshi/markets_YYYY-MM-DD.json` |
| Depends on | Kalshi Gamma API (no auth required for read-only market data) |
| Current status | Loaded; pulling daily |

The original design went through two iterations. The first attempt (March 29, 2026) used the legacy `trading-api.kalshi.com` endpoint and returned 401 errors — investigation revealed the endpoint had been deprecated in favor of `api.elections.kalshi.com`, which is sports-only and does not include the policy markets the project actually needed. The second iteration accepted that real policy market trading would require Kalshi's RSA signature authentication (API key + private key), which was deferred. As a workaround, the component was scoped to read-only market data from the Gamma API, which provides market existence and pricing without requiring authenticated trading access.

The output filename pattern (`markets_YYYY-MM-DD.json`, not the simpler `YYYY-MM-DD.json` used elsewhere in the project) is a deliberate disambiguation. Earlier in the project's history, multiple data sources used flat date filenames, and grep across them was producing false positives. The `markets_` prefix lets a fresh agent immediately distinguish a Kalshi pull from a research digest dated the same day.

The launchd schedule of 4:45 AM places kalshi-pull just after research-sweep (4:30 AM) so that downstream prediction-generation components running at 5:15 AM and later have fresh market data without overlapping API call windows.

The component was designed knowing that Kalshi's policy market coverage is narrower than Polymarket's, and that the Gamma API does not return resolved-market history in the same format as Polymarket's resolved-market endpoints. The decision to accept these limitations rather than block on RSA authentication was logged March 29 as a "we'll revisit when we need live trading" tradeoff. The trade has held — Kalshi-pull has run reliably as a read-only source while the project's primary calibration work has used Polymarket data.

What was anticipated to fail at design time: the Kalshi API endpoint structure was known to be in flux (the March 24-25 endpoint discovery proved this), and the design accepted that future endpoint changes might require re-authentication or schema migration work. What was not anticipated, and what later became load-bearing in the April 18 incident, was the consequence of treating policy_markets_seed.json as a workaround input to downstream agents *while* kalshi-pull was operating normally on a different code path. The seed file and the kalshi-pull output were never structurally linked, but downstream agents read both as if they were equivalently authoritative.

*Reproducer: BRAIN.md March 24 entry "Polymarket blocks US residents from live trading"; March 29 entries "Kalshi API endpoint updated + RSA auth identified" and "Use curated policy seed file for benchmark"; April 5 entry confirming kalshi-pull output path pattern; current source at `experiments/week1/scripts/kalshi_pull.py` (path verified via state_manifest.md).*

### 2.1.2 polymarket-pull

Polymarket-pull is the component responsible for pulling Polymarket market data into the project on a daily cadence. Its design history is shaped by absence: the component did not exist in the original 8-job launchd lineup. The asymmetry between *Kalshi has a pull job* and *Polymarket reads from a seed file* is the structural root of the April 18 contamination, and polymarket-pull was added during the April 19 incident response to close that gap.

| Field | Value |
|---|---|
| Schedule | 4:40 AM nightly |
| Output | `data/polymarket/YYYY-MM-DD.json` |
| Depends on | Polymarket Gamma API (no auth required for read-only market data) |
| Current status | Loaded; first fully-automated live-data pull completed April 20, 2026 |

The original design (March 22 - April 17, 2026) treated Polymarket data as something the founder pulled manually or that downstream scripts read directly from `policy_markets_seed.json`. The seed file was created on March 29, 2026, as a deliberate workaround when Kalshi's RSA authentication wasn't ready and the project needed "meaningful markets immediately" for benchmark work to begin. The decision was logged in BRAIN.md with an explicit alternative-rejected entry: *"Waiting for full auth (would delay benchmark start)."*

The seed file was designed as a temporary workaround. It was not designed as a permanent input source. Crucially, the design decision did not include an explicit removal-condition — there was no logged trigger that would retire the seed file once a real Polymarket pull was working, and there was no architectural separation between *seed-file inputs* and *live-data inputs* in downstream components. Over the next twenty days, downstream agents (text-swarm, calibration-tracker, commercialization-agent, revenue-strategist) read from the seed file as if it were live data, generating "vs crowd" comparisons, divergence claims, and Brier scores against fictional baselines.

The polymarket-pull component was added on April 19, 2026 as part of the contamination response. Its design was deliberately minimal: pull resolved markets and active markets from the Polymarket Gamma API, write to `data/polymarket/YYYY-MM-DD.json`, no transformation. The schedule of 4:40 AM was chosen to land just before kalshi-pull (4:45 AM) so that downstream prediction-generation components have fresh data from both sources before the 5:15 AM text-swarm run.

The component was designed knowing two anticipated failure modes. First, Polymarket's Gamma API has occasional rate-limiting that can produce partial pulls; the design accepts partial-pull risk and relies on downstream components to detect and handle missing data rather than retrying at the pull layer. Second, the API schema can change without notice; the design accepts schema-change risk and relies on downstream components to fail loudly rather than silently if expected fields are missing.

What was deliberately left out of the polymarket-pull design: any transformation, normalization, or scoring of the pulled data. The architectural rule "LLMs handle judgment, scripts handle everything else" applies in reverse here — pull components do *only* the pull, with no judgment about what the data means. Judgment lives in downstream prediction-generation components that consume the pull output.

The polymarket-pull component represents a structural correction to the original 8-job lineup. The corrected lineup has kalshi-pull and polymarket-pull as parallel data-ingestion components, both feeding downstream prediction generation, both producing date-stamped JSON output that downstream components read by date. The asymmetry that produced the April 18 contamination is closed at the architectural layer.

*Reproducer: incident_ledger.md April 18 incident, Section 4 root cause analysis ("com.latentforge.polymarket-pull.plist was never created, so no live Polymarket data was ever pulled automatically"); BRAIN.md March 29 seed-file decision; state_manifest.md current launchd lineup confirming polymarket-pull at 4:40 AM.*

## 2.2 Research

The research components are the project's intelligence layer. They read external sources — academic papers, GitHub repositories, competitive signals — and produce daily output that the founder reviews before opening Claude Code. The two components in this bucket — research-sweep and compression-researcher — both run autonomously, both produce dated markdown output, and both are designed to surface signals the founder would otherwise miss while heads-down on engineering work.

The research bucket reflects a specific operating philosophy from the project's founding: a non-technical solo founder cannot compete with a fast-moving research field by reading manually. Manual reading is unsustainable, and missing a competitive signal — a paper invalidating the thesis, a competitor shipping commercially, a co-author publishing something new — is a known emergency-trigger condition. The research components automate this monitoring without removing the founder's judgment, by producing structured output that the founder reads and acts on each morning.

### 2.2.1 research-sweep

Research-sweep is the project's general intelligence layer. It runs a daily sweep across arXiv (search terms specified at design time) and a curated set of GitHub repositories, scores results for relevance, and produces a markdown digest the founder reads before opening Claude Code each morning. The component exists because the relevance >0.8 threshold was specified as a design forcing function: only signals above that threshold trigger a morning strategy session before any engineering work begins.

| Field | Value |
|---|---|
| Schedule | 4:30 AM nightly |
| Output | `research/daily-digest/YYYY-MM-DD.md` |
| Depends on | arXiv API, GitHub API, Anthropic API (synthesis) |
| Current status | Loaded; arXiv match-quality drift under audit (see state_manifest.md) |

The original arXiv search terms were hand-curated at founding (BRAIN.md Section 12) and reflect the project's specific watch surface: "latent communication agents," "emergent agent language," "multi-agent hidden state," "AI governance audit trail," "prediction market agent," "vector communication LLM," "agent2agent protocol," and similar. The terms were chosen narrow enough to filter out general AI-research noise but broad enough to catch adjacent work that might validate or threaten the thesis. The GitHub watch list — LatentMAS, Vision Wormhole, OpenClaw/NemoClaw, autoresearch (Karpathy), Rain Protocol SDK, vLLM, VectorArc/AVM — is similarly curated, with each repository tied to a specific component of the project's competitive or technical landscape.

The relevance >0.8 threshold is the most load-bearing design choice in research-sweep. The threshold serves a dual purpose: it filters output volume to what the founder can actually read in five minutes, and it sets the trigger for emergency response. A signal above 0.8 doesn't just show up in the digest — it goes to the founder's morning strategy session before Claude Code work starts. The threshold mechanism was specified at design time as a binary gate, not a sorted list, because the project anticipated that without a hard threshold, daily digests would gradually expand until the founder stopped reading them.

The original 7:00 AM cron schedule (BRAIN.md Section 12, founding) was migrated to a 4:30 AM launchd job on April 4, 2026 with the rest of the cron-to-launchd migration. The earlier scheduling was chosen to ensure the digest is ready before the founder's morning routine, with WakeForJob ensuring the schedule fires regardless of laptop sleep state. The 4:30 AM placement also clears the API call window before kalshi-pull (4:45 AM) and polymarket-pull (4:40 AM) run, so research-sweep has full bandwidth for arXiv and GitHub queries.

What was anticipated to fail at design time: research-sweep's arXiv matching was known to be approximate. Search-term overlap with non-relevant papers was an acknowledged risk, and the >0.8 relevance threshold was specifically designed to filter false positives. What was not anticipated, and what the May 2, 2026 audit identified, is that the relevance scoring mechanism named in the design was never built: results pass into the digest based on search-term hits alone, with no scoring layer. The component has been producing structurally-plausible-but-content-empty matches (e.g., a paper on omega Centauri matched on "AI population forecasting") without the threshold gate ever firing. This is documented as research-sweep output drift in state_manifest.md and remains under audit. The design lesson is that a threshold mechanism specified in design but not implemented in code becomes invisible drift — the component appears to be working because it produces output, but the output's relevance has degraded in a way no scheduled check would catch.

What was deliberately left out of research-sweep at design time: any auto-action on high-relevance results. The component produces a digest. The founder reads it. The founder decides whether to escalate to a morning strategy session. The architectural rule is that research-sweep raises signals; it does not respond to them.

*Reproducer: BRAIN.md Section 12 (The Research Nervous System) for original spec including arXiv search terms and the relevance >0.8 threshold; Section 8 (Three-Engine Operating Rhythm) for the morning-digest-before-Claude-Code workflow; April 4 entry for cron-to-launchd migration; state_manifest.md research-sweep entry for current status and audit-pending classification; current source verified via `cat ~/Library/LaunchAgents/com.latentforge.research-sweep.plist` for live schedule.*

### 2.2.2 compression-researcher

Compression-researcher is the project's specialized intelligence layer for latent compression techniques. Where research-sweep is general-purpose, compression-researcher is narrowly focused on a single technical domain: methods for compressing or improving the fidelity of inter-agent latent communication. It reads from arXiv, neuroscience literature, genomics, and topology sources — domains the project identified as adjacent to its compression problem — and produces actionable suggestions the founder reviews each morning.

| Field | Value |
|---|---|
| Schedule | 2:00 AM nightly |
| Output | `research/suggestions/YYYY-MM-DD.md` |
| Depends on | Anthropic API (synthesis), curated cross-domain literature |
| Current status | Loaded; intermittent API timeouts (180s wrapper) |

The component was created on April 1, 2026, after the project recognized that the general research-sweep was missing technical signals from outside the AI/ML literature. The founding observation was that latent compression is a problem with relevant prior art in fields the project would not normally watch — neuroscience (predictive coding, efference copy, sparse distributed representations), genomics (dictionary learning), and topology (persistent homology for drift detection). The general research-sweep was structured around AI/ML search terms and would not surface these adjacent fields. A specialized agent with a different reading list was the structural fix.

The 2:00 AM schedule places compression-researcher first in the overnight job stack, before any other component runs. This ordering is deliberate. Compression-researcher's output sometimes needs to be read by other agents during the same overnight run — the founder inputs pipeline can incorporate compression suggestions into the morning revenue strategist run, and the early hour ensures the suggestions exist before downstream agents read.

The output format is structured around three fields per suggestion: technique, field-of-origin, and core idea, with priority and timing tags (HIGH/MEDIUM and Week 3/Week 4). The format was chosen to be directly actionable — a suggestion that doesn't include "when does this become work" was treated as too abstract to put into the queue. The first run on April 1 produced three suggestions in this format (efference copy compression, dictionary learning sparse coding, topological drift detection), and the format has held.

The component was designed knowing that cross-domain synthesis is harder than within-domain search. Search terms across neuroscience and AI don't map cleanly, and an agent reading Cell biology papers and looking for relevance to LatentForge was anticipated to produce some false matches. The acceptance was that occasional false matches were preferable to missing a signal from a field the general sweep wouldn't see. The compounding behavior — the agent has produced suggestions on similar themes for multiple consecutive days when a particular framing is productive — was anticipated as a feature, not a bug. The April 15 morning update notes "Compression researcher Day 4 on Predictive Coding Residuals," documenting four consecutive days where the agent sharpened the same architectural framing into progressively more actionable form.

What was anticipated to fail at design time: API timeouts during the cross-domain synthesis call were known to be a risk because the synthesis task is heavier than research-sweep's search-and-summarize task. The April 5 architectural fix added a `run_with_key.sh` wrapper with three retries on API timeout, and the timeout window was extended from 120 seconds to 180 seconds on April 17 after multiple compression-researcher and revenue-strategist failures. The current 180-second wrapper is the production state.

What was not anticipated, and what would later become structurally relevant during the April 18 contamination response, is that compression-researcher's output is consumed by the commercialization-agent as one of its compounding inputs. When the commercialization-agent's Pattern A Social Proof Loop began amplifying contaminated baselines on April 19, compression-researcher's suggestions were one of several upstream inputs being read into the loop. The component itself was not contaminated — its output was clean — but the downstream consumption pattern made compression-researcher's suggestions part of a larger compounding architecture that was not fully visible at design time.

*Reproducer: BRAIN.md April 1 entry "Latent Compression Researcher agent created" with the original three-suggestion format; April 5 entry for `run_with_key.sh` wrapper addition; April 17 entry for timeout extension to 180s; April 15 entry "Compression Researcher Day 4 on Predictive Coding Residuals" demonstrating multi-day theme persistence; state_manifest.md compression-researcher entry for current status.*

## 2.3 Prediction generation

The prediction-generation components are the system's forecasting layer. They produce probability estimates on prediction-market questions and log those estimates against eventual market resolutions. Three components occupy this bucket: text-swarm, calibration-tracker, and shadow_match. The three are structurally similar at the surface (each produces probability estimates, each uses the Anthropic API, each is connected to prediction-market data) but were built at different times for different purposes, and the relationships among them are not what a casual reading would suggest.

The most important architectural fact about this bucket: text-swarm and calibration-tracker each contain their own internal three-agent swarm using the same persona design (Macro Analyst, Quant Researcher, Contrarian Forecaster). They are *parallel implementations*, not upstream and downstream components. This was not an accident of accumulation — it was a deliberate consequence of building components for different purposes at different points in the project's timeline, with the persona design having matured by the time the second component was built. A reader who sees both components running and assumes one feeds the other is reading a structure the architecture does not have. Section 3 (Relationships between components) treats this in more detail; the per-component descriptions below establish the design rationale for each component independently.

### 2.3.1 text-swarm

Text-swarm is the project's control arm for the four-arm benchmark. It runs the project's three-persona text-based swarm against eleven fixed Polymarket benchmark questions, producing daily probability estimates that serve as the *baseline against which latent-arm results are compared*. Its purpose is not to be a forecasting product. Its purpose is to be a rigorous control — to make the eventual A/B test against latent-arm output meaningful.

| Field | Value |
|---|---|
| Schedule | 5:15 AM nightly |
| Output | `experiments/benchmark/text_swarm_YYYY-MM-DD.md` |
| Depends on | Polymarket data, Anthropic API, hardcoded benchmark question set |
| Current status | Currently unloaded as of May 2, 2026 (see state_manifest.md) |

Text-swarm was built March 30, 2026, as the implementation of Arm 2 in the four-arm benchmark architecture. The four-arm design (text vs latent × single-agent vs swarm) requires a text-swarm condition as one of the four cells, and text-swarm is that cell. The component runs eleven fixed benchmark questions on Polymarket — chosen at March 30 founding for being policy/macro/geopolitical markets with reasonable resolution timelines and crowd uncertainty — through three sequential agent personas (Macro Analyst, Quant Researcher, Contrarian Forecaster). Each agent produces an estimate on each market; the three estimates are averaged into a swarm estimate, and the daily output records all three individual estimates plus the average.

The persona design — three agents with distinct analytical lenses — emerged from the March 30 strategic sync. Macro Analyst handles economic fundamentals, base rates, central bank policy. Quant Researcher handles market signals, momentum, crowd wisdom. Contrarian Forecaster stress-tests assumptions and finds tail risks. The original design tracked the Contrarian agent as a standalone supplementary signal in addition to its inclusion in the swarm average, on the rationale that averaging the Contrarian into the swarm would dilute its directional information. The April 5 addition of a fourth agent — Bayesian Updater, recommended by Grok to anchor the swarm against narrative drift — was logged as a *trial experiment with a pre-committed evaluation date of April 12*. The trial was designed with explicit drop-criteria: if the Bayesian Updater tracks identically to the Quant Researcher on most markets, drop it. The April 8-12 trial week confirmed the prediction (the Bayesian Updater tracked identically to the Quant Researcher on 9 of 11 markets), and the agent was dropped April 11. The current swarm is three agents.

The eleven-market hardcoded set is a deliberate design choice. Live-discovery would produce a moving question set that confounds longitudinal comparison — week-3 markets would not be the same as week-1 markets, and any comparison of swarm performance across time would conflate component behavior with question-set drift. Hardcoding the eleven markets as a fixed set means longitudinal comparisons measure component behavior on a stable benchmark. The choice of eleven specifically (not ten, not twelve) was determined by the March 30 selection of policy/macro/geopolitical markets with the right uncertainty and resolution profile.

Text-swarm produces output as a markdown file named with the date pattern `text_swarm_YYYY-MM-DD.md`. The format is human-readable rather than machine-readable because the founder reads the daily output as part of the morning routine. A separate downstream agent — the calibration-tracker, with its own embedded swarm logic — handles the machine-readable scoring layer; text-swarm is not consumed by other agents in the system.

What was anticipated to fail at design time: text-swarm's eleven-market set was anticipated to underweight or miss certain market categories. The component was *not* designed to handle sports or entertainment markets, and the limitation was acknowledged at March 30. The April 8 dual-track reporting decision (primary policy track vs full all-categories track) is a related architectural response to the same concern in calibration-tracker, but text-swarm itself was always scoped to policy/macro/geopolitical questions only.

What was not anticipated: the contamination chain that connected text-swarm's output to the seed-file polymarket data source. Text-swarm reads Polymarket market data to identify the eleven benchmark markets it scores; from March 29 through April 18, that data was being read from `policy_markets_seed.json` rather than from a live API pull. Text-swarm's own logic was clean — the three personas were doing their analytical work on whatever inputs they received — but the input layer was the contaminated source, and downstream "vs crowd" claims based on text-swarm output ("swarm 21-22% vs crowd 31% for 19 days") propagated the contamination forward.

The May 2, 2026 unload of text-swarm is part of post-reset stabilization, pending decisions about what the four-arm benchmark looks like in the live-data era. The component's design rationale is preserved here for the future restoration work.

*Reproducer: BRAIN.md March 30 entry "Arm 2 text swarm built and running"; March 30 entry "Contrarian agent tracked as standalone supplementary signal"; April 5 entry "4th Agent Added to Text Swarm" with trial date pre-commitment; April 8 entry "Bayesian Updater — drop after April 12"; April 11 entry "Bayesian Updater dropped from swarm"; current source verified via `cat experiments/benchmark/03_text_swarm.py`; state_manifest.md text-swarm entry for current unloaded status.*

### 2.3.2 calibration-tracker

Calibration-tracker is the project's live calibration measurement layer. It discovers Polymarket markets that meet specific filters (5-95% crowd probability, policy/macro/geopolitics/elections category for primary track), generates probability estimates using its own internal three-agent swarm, logs predictions daily, and scores predictions against market resolutions when those resolutions occur. It is the component the project relies on for live forecasting evidence, and it produces the dual-track Brier and BSS measurements that anchor the revenue-exploration arm's calibration claims.

| Field | Value |
|---|---|
| Schedule | 5:30 AM nightly |
| Output | `experiments/benchmark/calibration/` (per-day result files) |
| Depends on | Polymarket data, Anthropic API, embedded three-persona swarm logic |
| Current status | Loaded; all forecasting claims under re-audit per intent.md |

Calibration-tracker was built April 4, 2026, as the live counterpart to the four-arm benchmark's longitudinal control. Where text-swarm runs eleven fixed questions for longitudinal comparison purposes, calibration-tracker runs against the live universe of Polymarket markets that pass its category and uncertainty filters, producing forecasts on whatever markets currently qualify. The two components serve different purposes: text-swarm is for *measuring component behavior on a stable question set*, calibration-tracker is for *measuring component behavior on the live forecasting surface*. The live surface produces calibration evidence (was the swarm well-calibrated on actually-resolved markets?), while the stable set produces longitudinal evidence (does swarm behavior change over time on the same questions?).

The most architecturally important design choice in calibration-tracker is that it contains its own internal three-agent swarm rather than reading from text-swarm's output. The `swarm_estimate` function in `calibration_tracker.py` (verified at lines 110-141) runs three Claude API calls per market, with the same three system prompts as text-swarm — Macro Analyst, Quant Researcher, Contrarian Forecaster — and averages the three estimates. The personas were already canonical by April 4 (text-swarm had been running with them since March 30), and the calibration-tracker design adopted the same persona structure for design consistency. The two implementations share persona design but are independent code paths with no data flow between them.

The choice to embed the swarm logic rather than read from text-swarm's output was a self-containment decision. Calibration-tracker's purpose required it to operate on a different question set (live-discovered, filter-qualified) than text-swarm's hardcoded eleven. If calibration-tracker had been built as a downstream consumer of text-swarm, it would have been forced to either share text-swarm's eleven-market set (defeating the live-discovery purpose) or to call text-swarm's logic separately for its own market set (which is functionally identical to having an embedded swarm with extra ceremony). The embedded design accepts code duplication of the persona logic in exchange for self-contained operation, and the architectural rule "LLMs handle judgment, scripts handle everything else" applies — the swarm logic is judgment, embedded directly into the component that needs it.

The 5-95% crowd probability filter exists to exclude markets where the crowd has already converged on near-certainty. A market trading at 99% has effectively no uncertainty for the swarm to add value to, and including such markets would inflate apparent calibration scores through trivial agreement on near-certain outcomes. The filter was added during the April 5 calibration-tracker fix sprint, alongside a `ZeroDivisionError` correction that previously caused the script to crash when no markets had resolved yet.

The category filter — primary track restricts to policy/macro/geopolitics/elections — was added April 8, 2026, after sports markets in the full track produced negative Brier Skill Scores. The negative BSS was diagnosed as a mathematical artifact of near-certain outcomes (sports markets where the crowd is at 99%+ and outcomes are 0 produce crowd Brier near 0 and any swarm uncertainty produces higher Brier; this is not a forecasting failure, it is a market-selection issue). The dual-track design — primary track (policy only) for the thesis test, full track (all categories) for transparency — was the architectural response: don't hide the sports results, but don't let them pollute the headline calibration claim either.

Four additional metrics were added to calibration-tracker on April 11, 2026: calibration curve context, entropy, swarm dispersion, and divergence vs crowd. The metrics were a ChatGPT recommendation aimed at making the benchmark report richer and the calibration evidence more defensible. The expansion is design-relevant because it confirms calibration-tracker as a self-contained statistical analysis component, not just a scoring layer — a component that only consumed text-swarm output would not need its own dispersion or entropy logic.

What was anticipated to fail at design time: calibration-tracker's filter design was known to be approximate. The 5-95% threshold and the category filter were anticipated to evolve as the project encountered more market types, and the dual-track architecture was specifically designed to surface filter issues without forcing premature commits to filter changes.

What was not anticipated: the same upstream contamination that affected text-swarm. Calibration-tracker reads Polymarket market data to identify qualifying markets and to determine crowd probabilities for filter checks; from April 4 through April 18, that data was being read from `policy_markets_seed.json`. The component's analytical logic was clean — its embedded swarm, its filters, its statistical metrics all operated correctly on whatever inputs they received — but the input layer was contaminated, and the calibration scores produced during this period are downstream of fictional baselines.

All forecasting claims from calibration-tracker before April 19, 2026 are retracted per incident_ledger.md and intent.md. The component's design is preserved here for the post-reset re-validation work.

*Reproducer: BRAIN.md April 4 entry "Live calibration tracker built & running"; April 5 entry "Two Fixes Applied" with ZeroDivisionError fix and 5-95% probability filter; April 7 entry "Brier Skill Score added to calibration tracker"; April 8 entry "Category filter added to calibration tracker" with dual-track reporting; April 11 entry "Four new metrics added to calibration tracker"; current swarm logic verified via `sed -n '105,250p' experiments/benchmark/calibration_tracker.py`; state_manifest.md calibration-tracker entry and intent.md "Under re-audit" section.*

### 2.3.3 shadow_match

Shadow_match is the project's swarm-vs-single-strong-model diagnostic. It runs eleven fixed benchmark markets through both the three-agent swarm and a single strong model (Shadow), produces side-by-side probability estimates for both, and logs the comparison alongside crowd probabilities. Its purpose is to disambiguate whether observed swarm performance comes from ensemble behavior or from individual agent judgment — a diagnostic question that calibration-tracker and text-swarm cannot answer on their own.

| Field | Value |
|---|---|
| Schedule | Manual; runs morning routine when the founder executes the script |
| Output | `~/.latentforge/shadow_match/shadow_match_YYYY-MM-DD.json` |
| Depends on | Polymarket data, Anthropic API, three-persona swarm logic, single-Shadow-agent prompt |
| Current status | Manual-by-design; runs during morning routine |

Shadow_match was built April 4, 2026, the same day as calibration-tracker, as a complementary diagnostic. Where calibration-tracker measures swarm calibration on the live forecasting surface, shadow_match measures swarm behavior *relative to a single strong model* on the same eleven-market set as text-swarm. The three-way logging — Shadow estimate, Swarm estimate, Crowd estimate — makes visible the question that calibration-tracker cannot address: when the swarm appears to outperform the crowd, is the outperformance coming from ensemble behavior (multiple agents averaging out individual errors) or from individual agent judgment (a single strong agent would have produced the same answer)?

The shadow_match output JSON includes per-market entries with five fields: market description, Shadow estimate, Swarm estimate, Crowd probability, and outcome (filled in 0 or 1 when markets resolve). The format is intentionally minimal — shadow_match is a diagnostic, not a primary measurement, and the output is meant to be readable by the founder during morning routine without further processing.

The most distinctive design choice for shadow_match is that it is *not on launchd*. It runs only when the founder executes the script during the morning routine. This is deliberate: shadow_match's purpose requires founder attention to be useful. An overnight automated run would produce the same JSON, but the diagnostic value depends on the founder reading the comparison and forming a judgment about what the divergences mean. The architectural rule that the founder owns judgment-and-interpretation, and scripts handle everything-else, is most visible here: shadow_match is a tool that produces evidence, not an agent that produces decisions. Automating it would obscure the "founder reads this each morning" workflow that makes the evidence load-bearing.

Shadow_match is referenced in BRAIN.md as the diagnostic that surfaces the *ensemble vs individual* question for any future swarm performance claim. If a benchmark report were to claim swarm outperformance, shadow_match's data is what disambiguates: a swarm whose estimates closely track the Shadow's estimates is a swarm doing nothing the Shadow couldn't have done alone; a swarm whose estimates diverge from the Shadow's in informative ways is a swarm whose ensemble behavior is doing real work. This disambiguation is not available in either text-swarm or calibration-tracker; shadow_match is the only component that produces it.

What was anticipated to fail at design time: shadow_match's manual-execution discipline was known to be a workflow risk. If the founder skips a morning routine, shadow_match doesn't run, and the time series has gaps. The acceptance was that gaps are preferable to automated runs that the founder doesn't engage with. The design rationale is that shadow_match's evidence is only useful in conjunction with founder interpretation, and the manual-trigger workflow ensures the interpretation actually happens.

What was not anticipated: the same upstream contamination as the other components in this bucket. Shadow_match reads Polymarket market data and crowd probabilities for its eleven-market set; from April 4 through April 18, those readings came from the seed file. The Shadow-vs-Swarm comparisons logged during this period are downstream of fictional crowd baselines, and the specific divergences cited in BRAIN.md (Powell at 0.1% crowd vs 3-4% Shadow/Swarm; US-Iran at 22.5% crowd vs 7-8% Shadow/Swarm; Bitcoin at 65% crowd vs 62% Shadow vs 48-52% Swarm) are retracted per incident_ledger.md.

The post-reset re-validation work (live data starting April 20, 2026) gives shadow_match its first uncontaminated baseline period. The component's design is preserved here unchanged — the manual-execution discipline, the three-way logging, the eleven-market set are all kept — and the re-audit produces new reference data on the same architecture.

*Reproducer: BRAIN.md April 4 entry "Shadow Match baseline completed"; April 6 entry "Shadow Match Day 3 logged"; April 14 entry "Shadow match is MANUAL — must run every morning"; current source verified via `cat experiments/week1/scripts/shadow_match.py`; state_manifest.md shadow_match entry confirming manual-by-design status; incident_ledger.md April 18 incident for the contaminated-baseline retraction.*

## 2.4 Strategic synthesis

The strategic-synthesis components are the system's business-thinking layer. They sit above the prediction-generation components and read from research outputs, market data, and (in the commercialization-agent's case) their own previous output, producing daily strategic recommendations the founder reviews. The two components in this bucket — revenue-strategist and commercialization-agent — were built three weeks apart, with the commercialization-agent designed explicitly as the strategic counterpart to the more tactical revenue-strategist. Both are currently unloaded for different reasons, and the design history of each matters for any future restoration work.

This bucket sits architecturally above the prediction-generation bucket. Where prediction-generation components produce probability estimates on individual markets, strategic-synthesis components produce *recommendations about what the project should do*. The output is meant for founder consumption and decision-making, not for downstream automation. The architectural rule "LLMs handle judgment, scripts handle everything else" applies in a particular way here: these components produce *advisory judgment*, with the founder retaining final-decision authority on whether to act on any given recommendation.

### 2.4.1 revenue-strategist

Revenue-strategist is the project's tactical daily ideas component. It reads from prediction-market data (Kalshi pulls, Polymarket data), the daily research digest, the founder_inputs folder, and produces a daily markdown file of revenue-related recommendations the founder reads each morning. Its design framing from the founding sprint is "tactical" — short-horizon, actionable, oriented toward week-scale revenue moves rather than quarter-scale strategic positioning.

| Field | Value |
|---|---|
| Schedule | 5:00 AM nightly (when loaded) |
| Output | `revenue_ideas/YYYY-MM-DD.md` |
| Depends on | Kalshi data, Polymarket data, research digest, founder_inputs/ folder |
| Current status | Currently unloaded as of May 2, 2026 (see state_manifest.md) |

Revenue-strategist was the project's first automated synthesis agent, built March 29, 2026, alongside the daily benchmark tracker. The original design used the Anthropic API with Kalshi market data as its primary external grounding — the founder noted the prior placeholder version was producing untethered output, and the upgrade to a real-API + real-data version was logged as a deliberate move from "placeholder" to "grounded." The original schedule was 8:00 AM; the migration to launchd on April 4 moved it to 5:00 AM as part of the unified overnight job stack, ensuring revenue-strategist's output exists before the founder's morning routine.

The component reads from four input sources: Kalshi market data (for current market state), the daily research digest (for cross-domain signals from research-sweep), the founder_inputs/ folder (for human-layer signals the automated agents can't see, dropped in by the founder via the founder_inputs pipeline), and compression-researcher's daily suggestions (for technical opportunities). The four-source design was deliberate — revenue-strategist's value depends on synthesizing signals across domains, and any single-source input would produce narrower recommendations than a cross-domain read.

The founder_inputs/ folder integration deserves specific attention. The folder was added April 5, 2026, after the founder noticed revenue-strategist was missing X/Twitter signals that the automated agents structurally couldn't see. The folder is the human layer that fills the gap: the founder drops interesting X posts, articles, or links as `.md` files with the naming convention `YYYY-MM-DD_short_description.md`, and revenue-strategist reads the folder each morning before generating its output. The pipeline is a deliberate response to the architectural reality that automated agents have limited reading surface, and the founder's serendipitous discoveries are an irreplaceable signal source.

Revenue-strategist's output format is conversational markdown — daily recommendations written for human reading, not structured for downstream consumption. The format reflects the design intent that revenue-strategist produces *advisory daily ideas*, with the founder doing the action selection. A more structured output (JSON, decision-tree) would invite downstream automation that the design specifically did not want; the conversational format makes clear that each day's output is a starting point for founder thinking, not an instruction set.

What was anticipated to fail at design time: revenue-strategist's API call duration was known to be variable. The synthesis task across four input sources is heavier than simpler prediction tasks, and the April 5 wrapper addition (`run_with_key.sh` with three retries on timeout) was a direct response to early observations of intermittent API timeouts. The April 17 timeout extension from 120s to 180s was another response to the same failure mode. The current production state uses the 180s wrapper.

What was not anticipated: the contamination chain similar to the prediction-generation components. Revenue-strategist reads Kalshi and Polymarket data as part of its synthesis, and from March through April 18, that data path included the seed-file fallback for Polymarket. Revenue-strategist's output during this period referenced contaminated baselines indirectly — through the recommendations it generated based on swarm vs crowd divergence claims that were themselves downstream of the seed file.

The May 2, 2026 unload is part of post-reset stabilization. The component's design rationale is preserved here for future restoration work; the structural question for restoration is whether revenue-strategist's input set needs adjustment now that Polymarket is pulled live and the seed-file dependency is removed.

*Reproducer: BRAIN.md March 29 entry "Revenue Strategist v0.3 with real Anthropic API"; March 29 entry "Revenue Strategist now uses real Anthropic API + Kalshi data"; April 4 entry confirming launchd migration to 5:00 AM; April 5 entry "Founder Inputs Pipeline Added"; April 5 entry on `run_with_key.sh` wrapper; April 17 entry on 180s timeout extension; state_manifest.md revenue-strategist entry for current unloaded status.*

### 2.4.2 commercialization-agent

Commercialization-agent is the project's strategic-cofounder layer. It was designed to compound conviction over time — to read its own previous output, the calibration tracker's results, the research digest, compression suggestions, and founder_inputs, and to produce a daily strategic synthesis that *builds on prior thinking* rather than starting fresh each day. Its design intent was a running thesis that deepens as evidence accumulates. Its actual failure mode was that the same compounding behavior amplified contaminated upstream evidence into increasingly confident strategic claims, ultimately producing the Pattern A Social Proof Loop documented in incident_ledger.md.

| Field | Value |
|---|---|
| Schedule | 5:45 AM nightly (when loaded) |
| Output | `revenue_ideas/commercialization_YYYY-MM-DD.md` plus `commercialization_thesis.md` (running thesis file) |
| Depends on | calibration-tracker results, research digest, compression suggestions, founder_inputs, *previous commercialization-agent output* |
| Current status | Currently unloaded since April 19, 2026 (see incident_ledger.md Pattern A) |

Commercialization-agent was built April 5, 2026, as a structural upgrade from revenue-strategist. The founder noted that revenue-strategist was producing tactical daily ideas but the project lacked a *strategic co-founder layer that compounds over time* — a component whose output depth grew as it accumulated context and revisited prior thinking. Revenue-strategist by design treats each day fresh; commercialization-agent was designed to do the opposite. Reading its own previous output was a *feature*, not an accident.

The compounding design has two outputs. The dated daily file (`commercialization_YYYY-MM-DD.md`) is the day's synthesis. The running thesis file (`commercialization_thesis.md`) is the *accumulated* strategic position — updated nightly, with each update building on the previous version's framing. The running thesis was the architectural innovation: a single canonical document whose conviction over the project's strategic direction strengthens as evidence accrues, with each night's update reading the previous version and producing a refined version.

The component's output structure was specified in design: Primary Strategic Bet, Supporting Moves, Thesis Update with conviction tracking. The Primary Strategic Bet was the headline — the single most important strategic move for the current week. Supporting Moves were the secondary actions. Thesis Update was where the running thesis evolved, with explicit conviction tracking on key positions. The format was deliberately decision-oriented: not "here are some ideas," but "here is the move, here is the supporting work, here is how my conviction changed today."

The 5:45 AM scheduling places commercialization-agent last in the overnight job stack, after all upstream components have produced their day's output. This ordering is critical to the compounding design — commercialization-agent reads from research-sweep (4:30 AM), kalshi-pull (4:45 AM), text-swarm (5:15 AM), calibration-tracker (5:30 AM), and the previous day's commercialization-agent output. Running last ensures all upstream signals are available; running first or middle would force the component to compound on stale upstream context.

The first design-discipline addition came April 11, 2026, when the commercialization-agent's daily recommendations began re-deriving already-decided positions. The agent had recommended Rain grant submission five days running despite the all-engines decision on April 5 to park the grant until Mac Mini latent results. The fix was a "LOCKED DECISIONS" block added to the agent's prompt, listing the explicit pre-committed decisions the agent should not re-derive. This was the project's first observation of the compounding failure mode — an agent designed to compound conviction was *also* compounding pressure to revisit decisions that were already made — and the prompt-level fix was the response.

What was anticipated to fail at design time: commercialization-agent's compounding behavior was understood to be a feature with attendant risk. The April 11 LOCKED DECISIONS fix was an early acknowledgment that the compounding could amplify positions the project had explicitly de-committed from. The expectation was that prompt-level discipline would be sufficient to constrain the compounding to constructive directions.

What was not anticipated, and what eventually triggered the April 19 unload, is that the prompt-level discipline could not constrain compounding when the *upstream evidence the agent was reading was contaminated*. From April 5 through April 18, commercialization-agent was reading calibration-tracker results that were themselves downstream of the seed-file contamination. The agent's compounding logic worked exactly as designed — it built increasingly confident strategic claims on accumulating evidence — but the evidence base was fictional. By April 19, the running thesis file contained Brier improvement claims, "vs crowd" performance assertions, and revenue projections all built on contaminated baselines, with conviction increasing daily because the agent read its own prior thesis as part of its input loop.

A second compounding channel was identified ten days later, during the April 29 script audit. The April 19 framing of Pattern A — accurate as far as it went — described one mechanism: the running thesis file, written nightly and read at the start of the next night's run, building conviction across days. The audit found a second mechanism that had been operating invisibly the whole time. The component reads its strategic-input directory using a "load latest file" helper that picks files by reverse-alphabetical filename order. Because the component's own output filenames sort lexicographically *after* the dated input filenames, the helper returns the component's own previous output whenever any prior commercialization output exists in the directory. The variable was named as if it held an upstream input, but the data it actually held was the component's own prior thesis. Two compounding channels were operating at once: the explicit thesis-file write-back, and the implicit input-directory collision. Both produced the same compounding-conviction effect; together they made the contamination amplification harder to dislodge than the original April 19 framing suggested. The unload decision was correct on the original framing, and a future reload requires structural fixes against both channels, not just one.

The Pattern A Social Proof Loop named in incident_ledger.md describes this failure mode in detail: the agent's input set included its own previous output, which created a self-reinforcing loop where each day's output increased conviction in claims made in previous days, while the upstream contamination remained invisible at the agent's reading layer. The agent did not have access to the raw market data; it read calibration-tracker's already-synthesized scores, which were themselves clean analytical work on contaminated input. By the time the contamination was discovered on April 18, the running thesis file had compounded fictional baselines into a comprehensive strategic narrative.

The commercialization-agent was unloaded on April 19, 2026, as part of the contamination response. The decision was explicit: a component whose designed compounding behavior amplifies contaminated upstream evidence cannot be re-loaded until the structural conditions that let contamination propagate are fixed. The structural fixes named in incident_ledger.md and state_manifest.md include split output directories, mtime-based selection of inputs, and separation of commercialization output from revenue-strategist read paths — these architectural changes are pre-conditions for any future restoration.

All three fixes target the same channel — the input-directory collision where reverse-alphabetical sort causes the agent to read its own previous output as if it were upstream input. None of the three fixes addresses the second channel, where commercialization_thesis.md is appended to nightly and read at startup; the thesis-file channel requires a separate structural decision (stop reading the thesis, truncate it nightly, version it per run, or rebuild it from clean inputs each night) not yet specified. Both channels must be closed before reload.

The deepest design lesson from commercialization-agent's history is that *compounding-conviction-over-time without contamination-resistance is dangerous in a way that is invisible from inside the component*. The agent itself behaved correctly. Its prompts were sound. Its compounding logic worked. The failure was at the architecture level: the agent's input set included contaminated upstream evidence, and the compounding amplification turned a data-source contamination into a strategic-narrative contamination that propagated faster than any single-day check could catch.

*Reproducer: BRAIN.md April 5 entry "Commercialization Agent Upgrade" with the compounding-thesis design intent; April 5 entry "Commercialization Agent Added (End of Day)" with the running-thesis architecture; April 11 entry "Rain grant locked in commercialization agent prompt" with the LOCKED DECISIONS block addition; incident_ledger.md Pattern A description of the Social Proof Loop and the April 19 unload decision; state_manifest.md commercialization-agent entry for current status and the structural-fix prerequisites for restoration.*

## 2.5 Reporting

The reporting bucket sits at the top of the system's layered shape. Where data-ingestion components feed prediction generation, prediction generation feeds calibration measurement, and strategic-synthesis components produce daily recommendations, reporting components produce *the artifacts that get read outside the system* — benchmark reports for grant applications, outreach drafts for prospective partners, narrative documentation for investor conversations. The bucket has a single component: benchmark-updater. The single-component bucket reflects the project's deliberately narrow reporting surface — there is one canonical benchmark report, automatically maintained, not a fan-out of report types.

### 2.5.1 benchmark-updater

Benchmark-updater is the project's automated report-maintenance component. It reads from calibration-tracker outputs, shadow_match results, and text-swarm logs, and regenerates the canonical benchmark report file each night with updated calibration data, divergence summaries, and timeline progression. Its design intent was to keep the benchmark report continuously current without requiring manual edits, so that any external conversation (grant draft, outreach response, investor question) could pull from a report that reflects the latest day's evidence.

| Field | Value |
|---|---|
| Schedule | 6:00 AM nightly (when loaded) |
| Output | `docs/latentforge_benchmark_report_v0.1.md` |
| Depends on | calibration-tracker outputs, shadow_match results, text-swarm logs |
| Current status | Currently unloaded since April 18, 2026 (see incident_ledger.md and state_manifest.md) |

Benchmark-updater was built April 6, 2026, the day after commercialization-agent, as the eighth and final job in the original launchd lineup. The component was added in response to a specific friction the project had encountered during the first week of April: every external-facing artifact (grant drafts, outreach drafts, founder summaries for engine sessions) required a current snapshot of the project's measurements, and producing those snapshots manually was burning founder attention on copy-paste work. The April 6 founding logged the component's purpose directly: "Benchmark report auto-updater live. Report updates itself daily."

The 6:00 AM scheduling places benchmark-updater last in the overnight job stack, after commercialization-agent (5:45 AM) and after all upstream measurement components have produced their day's output. The ordering ensures the report reflects the complete overnight cycle when the founder reads it during morning routine. The schedule also gives the report a stable update cadence — it changes at most once per day, always at 6:00 AM, which simplifies any external citation of "as of [date]" in outreach or grant material.

The output target file (`docs/latentforge_benchmark_report_v0.1.md`) was explicitly versioned. The v0.1 designation was deliberate, anticipating that the report's format and emphasis would evolve as the project matured. The component was designed to update the v0.1 file in place; a v0.2 was anticipated as a future revision when the report's underlying framing (specific Brier comparisons, "vs crowd" divergence framings, four-arm benchmark progression) needed structural redesign rather than incremental data updates.

Benchmark-updater's read paths are upstream-of-strategic-synthesis. The component reads calibration-tracker outputs, shadow_match results, and text-swarm logs — but *not* commercialization-agent output. This was a deliberate architectural choice: the benchmark report is a *measurement* artifact, not a *strategy* artifact. Strategic synthesis lives in commercialization-agent's running thesis and in revenue-strategist's daily ideas; the benchmark report is for measurements only. The separation prevents strategic narrative from contaminating measurement reports, and prevents measurement updates from triggering strategic re-derivation.

The component's update mechanism was designed to be section-targeted. The full benchmark report contains multiple sections (introduction, methodology, calibration results, divergence findings, motor-car test status, next steps), and benchmark-updater only modifies the data-driven sections — calibration results and divergence findings primarily. Methodology and framing sections are static, edited by hand when the project's framing evolves. This selectivity was a design discipline: an automated component that could rewrite methodology sections would invite drift in the document's framing, which is meant to be founder-controlled.

What was anticipated to fail at design time: benchmark-updater's update mechanism was known to depend on stable upstream output formats. If calibration-tracker's output format changed, or shadow_match's JSON schema shifted, benchmark-updater's parsing layer would need corresponding updates. The acceptance was that the project's data formats were stable enough during the v0.1 period that schema-change risk was acceptable.

What was not anticipated: the scenario in which the *content* benchmark-updater pulled from upstream sources was contaminated even though the sources themselves were running normally. From April 6 through April 18, benchmark-updater was reading calibration-tracker outputs, shadow_match results, and text-swarm logs — all of which were technically operating correctly, all of which contained measurements that were downstream of the seed-file contamination. The benchmark report's calibration sections, divergence summaries, and "vs crowd" framings accumulated over twelve days into a v0.1 report that read as a coherent measurement document but was based on fictional baselines.

The April 18 contamination discovery made the v0.1 benchmark report's contents structurally unreliable. The report contained the "45% Brier improvement" claim, the "20-day AI regulation divergence" framing, multiple "vs crowd" performance assertions, and a coherent narrative built on those measurements. Each of those elements required retraction. The benchmark-updater component was unloaded as part of the April 18-19 incident response, with the explicit rationale that an automated component continuously updating a contaminated report would propagate the contamination to any future reader of the report file. The v0.1 benchmark report itself was preserved as a quarantined draft (`latentforge_benchmark_report_v0.2_PRE_RESET_DRAFT.md` in some references) for forensic review; the v0.1 file was effectively deprecated.

The structural prerequisites for benchmark-updater's restoration are documented in state_manifest.md and incident_ledger.md. The component cannot be re-loaded against the v0.1 template — that template carries the framing assumptions ("vs crowd" comparisons, divergence-as-headline) that produced the contamination's most visible artifacts. A v0.2 template is required, designed without the framings that anchored the contaminated narrative. The April 19 incident response named benchmark-updater's restoration as gated on this template work, and the restoration is pending live-data baselines starting April 20, 2026 plus a structurally clean v0.2 template that benchmark-updater can update against.

The deepest design lesson from benchmark-updater's history is that *automated reporting components inherit whatever epistemic state their upstream sources produce*. The component itself was structurally sound — it parsed correctly, scheduled correctly, updated section-targeted as designed. But the artifact it produced was only as trustworthy as its inputs, and when its inputs were contaminated, the report became a vehicle for contamination propagation rather than a measurement record. Reporting components operate downstream of every other layer, and contamination at any upstream layer produces a contaminated report regardless of the reporting component's own correctness.

*Reproducer: BRAIN.md April 6 entry "Benchmark report auto-updater live. 8th job at 6am. Report updates itself daily"; April 6 entry "Fix 1: Job table updated to 8 jobs" with the full launchd schedule including benchmark-updater; incident_ledger.md April 18 incident for the v0.1 retraction and benchmark-updater unload rationale; state_manifest.md benchmark-updater entry for current unloaded status and v0.2 template prerequisite.*

# 3. Relationships between components

Section 2 covered each component independently — what it does, why it was built, what it depends on. This section covers the *system-level* picture: how the components connect to form an architecture, what flows where, and which connections do not exist by deliberate design choice. The relationships matter because component-level correctness does not guarantee architecture-level correctness — the April 18, 2026 contamination was an architecture-level failure assembled from components that were each individually clean.

## 3.1 The layered data flow

The system's vertical shape is layered. Data ingestion sits at the bottom; reporting sits at the top. Data flows upward through prediction generation and strategic synthesis. Research components feed in horizontally at the prediction-generation and strategic-synthesis layers.

```
┌─────────────────────────────────────────────────────────┐
│                      6:00 AM                             │
│                  benchmark-updater                       │
│         (regenerates docs/benchmark_report)              │
│                          ▲                               │
└──────────────────────────┼───────────────────────────────┘
                           │ reads measurements only
                           │
┌──────────────────────────┼───────────────────────────────┐
│                          │                               │
│  5:00 AM                 │              5:45 AM          │
│  revenue-strategist      │              commercialization│
│  (tactical daily ideas)  │              -agent           │
│                          │              (running thesis) │
│         ▲                │                  ▲            │
└─────────┼────────────────┼──────────────────┼────────────┘
          │                │                  │
          │ reads          │ reads            │ reads + reads
          │                │                  │ own previous
          │                │                  │ output
          │                │                  │
┌─────────┼────────────────┼──────────────────┼────────────┐
│         │                │                  │            │
│   5:15 AM            5:30 AM           manual            │
│   text-swarm     calibration-tracker   shadow_match      │
│   (Arm 2 control │  (live calibration  (ensemble vs      │
│   on 11 fixed     │   on filtered live  individual        │
│   markets)        │   universe)         diagnostic)      │
│         ▲                ▲                  ▲            │
│         │                │                  │            │
│         └────────────────┴──────────────────┘            │
│                          │                               │
│                          │ reads                         │
└──────────────────────────┼───────────────────────────────┘
                           │
                           │
┌──────────────────────────┼───────────────────────────────┐
│   4:40 AM                │                4:45 AM        │
│   polymarket-pull        ├────────────►   kalshi-pull    │
│   (Polymarket            │                (Kalshi        │
│   Gamma API)             │                Gamma API)     │
└──────────────────────────┼───────────────────────────────┘
                           │
                           │ feeds horizontally
                           │
┌──────────────────────────┼───────────────────────────────┐
│   4:30 AM                │                2:00 AM        │
│   research-sweep         │                compression-   │
│   (general intelligence) │                researcher     │
│                          │                (specialized   │
│                          │                research)      │
└──────────────────────────┴───────────────────────────────┘
```

The four-layer structure (ingestion → prediction → synthesis → reporting) reflects the system's actual operation, not an idealized model. Each layer's components run in a defined time window, and the schedule ordering is what makes the layering work — research and ingestion fire first, prediction generation reads the fresh data, strategic synthesis reads the fresh predictions, reporting reads the complete measurement state.

The horizontal feed from research components is structurally important. Research-sweep and compression-researcher do not fit cleanly into the ingestion-or-prediction layer — they produce content that revenue-strategist and commercialization-agent read alongside market data, so they sit horizontally at the layer where strategic synthesis begins. Compression-researcher specifically is read by revenue-strategist and (until April 19) by commercialization-agent; research-sweep is read by both strategic-synthesis components plus the founder's morning routine before any Claude Code work begins.

*Reproducer: BRAIN.md April 5 entries on revenue-strategist's input set ("Reads: Kalshi data + research digest + founder_inputs + compression suggestions"); April 5 entry on commercialization-agent's input set ("Reads: calibration tracker + research digest + compression suggestions + founder_inputs + previous output"); April 6 entry on benchmark-updater's read paths.*

## 3.2 Parallel implementations: text-swarm and calibration-tracker

The most architecturally important relationship in the system is one that does *not* exist: text-swarm and calibration-tracker do not share a data flow. They contain parallel implementations of the same three-agent swarm logic — Macro Analyst, Quant Researcher, Contrarian Forecaster — but the implementations are independent code paths with no upstream-or-downstream relationship between them.

A casual reading of the system might infer that calibration-tracker reads from text-swarm's output, since both components produce probability estimates and both run in the prediction-generation window. The inference is wrong. Calibration-tracker's `swarm_estimate` function (verified at lines 110-141 of `experiments/benchmark/calibration_tracker.py`) makes its own three Claude API calls per market, with the same three persona system prompts, and averages the results. It does not read text-swarm's output file. It does not call text-swarm's logic as a library. It is a parallel implementation.

The parallelism was deliberate, as Section 2.3.2 covered. Text-swarm runs eleven fixed benchmark questions for longitudinal comparison purposes; calibration-tracker runs the live universe of qualifying Polymarket markets for live calibration purposes. The two purposes are different enough that sharing implementation would have forced one of two bad design choices: share text-swarm's eleven-market set in calibration-tracker (defeating live-discovery), or have calibration-tracker call text-swarm's logic separately for its own market set (functionally identical to embedding with extra ceremony).

The shared persona design — three agents with the same system prompts — is not data flow. It is *design pattern reuse*. The personas were canonical by April 4, 2026 (text-swarm had been running with them since March 30), and calibration-tracker adopted them for design consistency rather than inheriting them through code. A change to the persona system prompts in one component does not propagate to the other automatically; both implementations would need to be updated independently to maintain the shared design.

The implication for system understanding is that *forecasts produced by the two components are independent observations, not the same observation reported twice*. If text-swarm and calibration-tracker happen to produce similar estimates on overlapping markets, that similarity is independent agreement, not common-source. If they produce different estimates, the difference reflects the different question sets and different Anthropic API calls, not architectural drift in a shared component.

The implication for restoration work is that any future structural change to swarm logic must be applied in both components or the parallelism breaks. Adding a fourth agent, changing a persona's system prompt, or modifying the averaging logic in one component does not affect the other. The Bayesian Updater trial-and-drop episode (April 5-12, 2026) is illustrative: the trial added a fourth agent to text-swarm only, and when the agent was dropped on April 11, the change was localized to text-swarm. Calibration-tracker's swarm logic was unaffected because the components are independent.

*Reproducer: `sed -n '105,250p' experiments/benchmark/calibration_tracker.py` shows the `swarm_estimate` function with three independent Claude API calls; `cat experiments/benchmark/03_text_swarm.py` shows text-swarm's separate implementation; BRAIN.md April 4 entry "Live calibration tracker built & running" with no reference to text-swarm consumption; BRAIN.md April 5 entry "4th Agent Added to Text Swarm" affecting only text-swarm.*

## 3.3 Independence boundaries

Several relationships that *could* exist in the system do not, and the absences are deliberate design choices documented across the project's history.

### 3.3.1 Shadow_match is not on launchd

The system's overnight job stack runs eight components on launchd schedules. Shadow_match is the ninth prediction-related component, but it does not run on launchd. The non-automation is deliberate: shadow_match's diagnostic value depends on founder interpretation, and the manual-trigger workflow ensures the interpretation actually happens. An overnight automated run would produce the same JSON output, but the founder would be less likely to engage with it during morning routine, and the diagnostic — ensemble vs individual — would degrade from active to passive.

The independence boundary is from launchd specifically, not from the data flow. Shadow_match still reads from the same data sources as the launchd-scheduled prediction components (Polymarket data, Anthropic API, the same eleven-market set as text-swarm). The boundary is in *when and how it runs*, not in *what it reads*.

### 3.3.2 Benchmark-updater does not read commercialization-agent

The reporting bucket reads from prediction generation (calibration-tracker, shadow_match, text-swarm) but explicitly does not read from strategic synthesis (commercialization-agent, revenue-strategist). This is the measurement-vs-strategy separation Section 2.5.1 covered. The benchmark report is a measurement artifact; strategic narrative lives in commercialization-agent's running thesis and revenue-strategist's daily ideas. Mixing the two would let strategic narrative contaminate measurement reports, and would also let measurement updates trigger strategic re-derivation in a way the design did not want.

The boundary is one-directional. Commercialization-agent reads calibration-tracker outputs (and did until April 19); calibration-tracker does not read commercialization-agent. Benchmark-updater reads calibration-tracker; commercialization-agent does not read benchmark-updater. The data flows from measurement upward into strategy and reporting, not in the reverse direction. Any change that introduced reverse flow — for example, an automated update to calibration-tracker's filter parameters based on commercialization-agent's strategic priorities — would break the design discipline.

### 3.3.3 Pull components do not transform data

Data-ingestion components (kalshi-pull, polymarket-pull) do not perform filtering, scoring, or interpretation on the data they pull. They pull from the API, write to a date-stamped JSON file, and exit. Any judgment about what the data means lives in downstream components. This is the architectural rule "LLMs handle judgment, scripts handle everything else" applied in reverse — pull components are scripts that do *only the pull*, with judgment intentionally pushed downstream where it can be inspected and changed without modifying the data layer.

The boundary matters for restoration: if a future change wants to add filtering at the pull layer (for example, "only pull markets with crowd probability between 5% and 95%"), that change moves judgment into a script that should not have it. The 5-95% filter belongs in calibration-tracker, not in polymarket-pull. The architectural separation preserves the pull layer's neutrality, which makes any downstream issue debuggable by reading the raw pull file directly.

### 3.3.4 Research components do not feed prediction generators

Research-sweep and compression-researcher feed strategic-synthesis components (revenue-strategist and commercialization-agent) and the founder's morning routine, but they do not feed prediction-generation components directly. Text-swarm does not read research-sweep. Calibration-tracker does not read compression-researcher's suggestions. The prediction generators operate on market data; research outputs influence strategic thinking and founder attention, not the day's forecasts.

The boundary preserves a useful property: prediction generators are deterministic in their inputs (given the same market data and the same persona prompts, they produce reproducible-modulo-API-randomness output). If research outputs fed into the prediction layer, the day's forecasts would change based on whatever papers happened to be on arXiv that morning, which would break longitudinal comparison and make swarm behavior less interpretable.

*Reproducer: BRAIN.md April 14 entry confirming shadow_match manual status; April 5-6 entries confirming benchmark-updater read paths exclude commercialization-agent; March 22 architectural rule "LLMs handle judgment, scripts handle everything else"; current source verification via `grep -E '(import|from)' experiments/benchmark/03_text_swarm.py experiments/benchmark/calibration_tracker.py` to confirm no research-component imports.*

## 3.4 The contamination chain shape

The April 18 contamination's propagation followed the system's data flow, and understanding the propagation requires the architectural picture this section has assembled. The contamination did not originate at a single component and infect downstream; it originated at a *missing component* (no live polymarket-pull) and was absorbed by every component that read Polymarket market data through the seed-file fallback.

```
        policy_markets_seed.json (Mar 29 workaround, never retired)
                          │
                          │ read as if live data by:
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   text-swarm     calibration-tracker   shadow_match
   (analytical    (analytical logic     (diagnostic
   logic clean,   clean, scoring        logic clean,
   produced       against fictional     comparing
   contaminated   crowd baselines)      against
   "vs crowd"                           fictional
   claims)                              crowd values)
        │                 │                 │
        └────────┬────────┴────────┬────────┘
                 │                 │
                 ▼                 ▼
          benchmark-updater   commercialization-agent
          (read measurements, (read calibration-tracker
          regenerated v0.1    output + own previous
          report with         output, compounded
          contaminated        contaminated baselines
          baselines)          into running thesis)
                 │                 │
                 │                 │
                 ▼                 ▼
          v0.1 benchmark      Rain grant draft,
          report file         outreach drafts,
                              Day 30 conversation
                              targets, business
                              model rankings
```

The chain shape illustrates three structural facts about the contamination.

First, every component in the chain was individually clean. Text-swarm's three personas analyzed whatever inputs they received correctly. Calibration-tracker's filters and statistical metrics operated correctly on whatever inputs they received. Shadow_match's three-way logging captured whatever values it was given. Benchmark-updater's section-targeted updates worked as designed. Commercialization-agent's compounding logic compounded whatever inputs it read. No single component was at fault.

Second, the contamination propagated *both outward and inward*. Outward propagation went through benchmark-updater into the v0.1 report file and through any external artifact that quoted it (Rain grant draft, outreach drafts). Inward propagation went through commercialization-agent's compounding loop, where each day's run read its own previous output, building increasing conviction on accumulating evidence whose base was fictional. The two directions of propagation amplify the consequences differently — outward propagation creates external retraction surface, inward propagation creates internal narrative drift that becomes harder to dislodge as it deepens.

Third, the propagation was invisible from inside any single component. A reviewer examining text-swarm's code would see correct three-persona analytical logic. A reviewer examining calibration-tracker would see correct filter design and statistical metrics. A reviewer examining benchmark-updater would see correct section-targeted updates against a stable input format. The contamination is only visible when the architecture is examined as a whole and the data-source assumption is questioned — *is the seed file actually the live data the downstream components believe it is?* That question is upstream of every component's analytical layer, and no component's design included a check for it.

The structural correction that closes the contamination chain is the polymarket-pull component added April 19, 2026 (Section 2.1.2). The component's existence breaks the chain at its source: downstream components no longer have the structural opportunity to read seed-file content as if it were live data, because there is now an explicit live-data file at `data/polymarket/YYYY-MM-DD.json` that they read instead. The seed file remains in the repository for forensic and historical purposes but is no longer in the active data flow.

The deepest architectural lesson from the contamination chain is that *defense-in-depth at the analytical and citation layers does not protect against contamination at the data-source layer*. The project's pre-April-18 disciplines — citation guides, do-not-cite lists, dual-track reporting, BSS for difficulty context, three transparency-inversion proofs gated on measurement, motor-car tests with two-of-four required for external claims — all operated on the *output* of the contaminated input. They were each rigorous and honest. They could not catch the contamination because the contamination was upstream of every analytical defense the project had built. Section 5 (Incidents that shaped the project) treats this lesson in detail; the architectural picture this section assembles is what makes Section 5's lesson load-bearing.

*Reproducer: incident_ledger.md April 18 incident with full chain analysis; BRAIN.md March 29 entry "Use curated policy seed file for benchmark" with the missing removal-condition; state_manifest.md polymarket-pull entry confirming the structural correction; the architectural picture in 3.1 above showing the data flow that the contamination followed.*

# 4. Decisions that shaped the current shape

The project's current architecture is the cumulative result of explicit decisions, each logged at the time it was made with a date, a rationale, and the alternatives that were considered and rejected. This section is the curated decision log — the load-bearing decisions that explain why the system looks the way it does. The exhaustive log lives in BRAIN.md Section 11; this section selects the decisions that are still operative in the current architecture or whose framing remains structurally important even after revision.

The decisions are organized into four eras. The era boundaries reflect the project's actual operating shifts: a founding sprint that established the core thesis and infrastructure, an early-refinement period that sharpened the experimental design, a maturation period that built the discipline layer around the upcoming Mac Mini work, and a post-reset period that responded to the April 18 contamination with structural fixes the original architecture had not anticipated.

## 4.1 Founding sprint (March 22-29, 2026)

The founding sprint established the project's core architecture in a single week. The decisions in this era set the technology stack, the team-as-three-engines operating model, the experimental-baseline strategy, and — critically — the seed-file workaround that would later become the contamination root cause. The decisions in this era are characterized by *do-now-iterate-later* shape: get a working system on the rails fast enough to start producing measurements, accept temporary workarounds where the alternative was a multi-week delay.

| Date | Decision | Why | Alternative rejected | Reproducer |
|---|---|---|---|---|
| Mar 22 2026 | LatentMAS as base, not build from scratch | Validated, MIT license, runnable today, 83% cost reduction demonstrated in paper | Build from scratch: +3 months, no advantage | BRAIN.md §11, Mar 22 entry |
| Mar 22 2026 | OpenSpiel before Minecraft | Hardware constraint + cleaner benchmark + reproducible | MineDojo: Java + GPU rendering, too many failure points | BRAIN.md §11, Mar 22 entry |
| Mar 22 2026 | NemoClaw as base runtime | NVIDIA-backed, OpenShell sandboxing, Nemotron local models, GTC announcement | OpenClaw alone: less secure, no enterprise credibility | BRAIN.md §11, Mar 22 entry |
| Mar 22 2026 | MacBook = orchestration only, never runs models | 8GB cannot handle two models. Swap = false debugging = lost days | Any local model loading: rejected unconditionally | BRAIN.md §11, Mar 22 entry; §7 Hardware section |
| Mar 22 2026 | Polymarket data collection from Day 1 | No GPU required. 4+ weeks data before bot goes live. March Madness live now. | Starting Week 5: no historical data | BRAIN.md §11, Mar 22 entry |
| Mar 22 2026 | Three-engine system (Founder + Systems + Divergent) | Covers execution + accumulated context + real-time intelligence. No single intelligence owns complete engineering judgment. | Single engine: monoculture makes confident mistakes | BRAIN.md §0 and §0b |
| Mar 22 2026 | Dual-Engine Review Protocol non-negotiable from Day 1 | Architecture/funding/targeting/pivot decisions reviewed by both Systems and Divergent before commit. Cherry-picking the agreeing engine is the named failure mode. | Review by single engine: invites confirmation bias | BRAIN.md §0b |
| Mar 24 2026 | latentforge MacBook account has no sudo/admin | Browser for GitHub operations, plain git for terminal. Cannot install Homebrew or gh CLI. | gh CLI / Homebrew: blocked by account permissions | BRAIN.md §11, Mar 24 entry |
| Mar 26 2026 | Week 2 benchmark reframed — byte reduction is wrong metric | Raw hidden state vector larger than JSON stub. Fidelity proven at 1.0000. LatentMAS gains come from compute savings not byte size. | Byte reduction metric: rejected, both engines agree | BRAIN.md §11, Mar 26 entry |
| Mar 29 2026 | Use curated policy seed file for benchmark | Kalshi trading API requires RSA auth; seed gives meaningful markets immediately | Waiting for full auth: would delay benchmark start | BRAIN.md §11, Mar 29 entry; incident_ledger.md April 18 root cause |

The seed-file decision (March 29, 2026) deserves particular attention because it is the single decision in this era that produced the architectural defect underlying the April 18 contamination. The decision itself was logged correctly — it identified the constraint (Kalshi RSA auth not ready), proposed the workaround (curated seed file), and named the alternative rejected (waiting for proper auth). What the decision did not include was an explicit *removal condition* — no logged trigger for retiring the seed file once a real Polymarket pull was working, and no architectural separation between *seed-file inputs* and *live-data inputs* in downstream components. Section 5 treats this defect in detail; the decision itself is preserved here as foundational history.

## 4.2 Early refinements (March 30 - April 7, 2026)

The early-refinement era tightened the experimental design and added the first layer of automation. The decisions in this era are characterized by *cross-engine consensus* — multiple decisions converge on the same answer when ChatGPT, Gemini, Grok, and Claude review independently, which the project treats as a signal of design soundness. This is also the era that established the architectural rule about LLMs and judgment, and the era that built out the launchd job stack from cron to a unified eight-component overnight system.

| Date | Decision | Why | Alternative rejected | Reproducer |
|---|---|---|---|---|
| Mar 30 2026 | Four-arm benchmark design locked | ChatGPT/Gemini/Grok converged on this. Falsifiable, defensible against fairness critique. | Two-arm only: not defensible against fairness critique | BRAIN.md Mar 30 entry "Four-arm benchmark design locked" |
| Mar 30 2026 | "Useful divergence" replaces "divergence" | Divergence alone not a value prop. Must be tied to calibration + PnL. | Divergence as novelty metric: too easy to dismiss | BRAIN.md Mar 30 entry |
| Mar 30 2026 | Shadow Self upgraded to KL-Divergence Watchdog | Measures drift from base model manifold, not just translates | Translator only: misses governance story | BRAIN.md Mar 30 entry |
| Mar 30 2026 | Contrarian agent tracked as standalone supplementary signal | Day 1 data shows directional divergence; averaging into swarm dilutes edge | Averaging only into swarm: dilutes the edge signal | BRAIN.md Mar 30 entry |
| Apr 4 2026 | Migrate all cron jobs to launchd with WakeForJob | Cron skipped when Mac slept. Jobs not running overnight. | Keeping cron: confirmed broken | BRAIN.md Apr 4 entry "Infrastructure Migration" |
| Apr 4 2026 | API key moved to macOS Keychain via run_with_key.sh wrapper | Eliminates plaintext key in crontab. Wraps every launchd job. | Environment variable in crontab: rejected | BRAIN.md Apr 4 entry |
| Apr 5 2026 | Founder inputs pipeline added | Automated agents can't browse X. Human layer fills the gap. | Single-source agent reads only API data | BRAIN.md Apr 5 entry "Founder Inputs Pipeline Added" |
| Apr 5 2026 | brainload alias added — every Claude session begins with full BRAIN.md paste | Claude has no memory between sessions. Truncated bootstraps cause avoidable mistakes. | Partial summaries: cause incomplete-context errors | BRAIN.md Apr 5 entry "Standing Rule — Claude Session Startup" |
| Apr 6 2026 | Architectural rule: LLMs handle judgment, scripts handle everything else | Anything deterministic lives in Python. LLM layer handles synthesis, prioritization, drafting, reasoning. Pushing deterministic work through an LLM breaks unpredictably. | Mixed-responsibility components: rejected | BRAIN.md Apr 6 entry "Fix 5: Architecture rule added" |
| Apr 6 2026 | All scripts called by launchd must use absolute paths | launchd runs scripts from a read-only system directory; relative paths silently fail | Relative paths: produce silent failures | BRAIN.md Apr 5-6 entries on launchd job fixes |
| Apr 7 2026 | Compute parity — Phi-3 Mini across all four arms | Different base models = testing model intelligence not communication protocol. | Different models per arm: rejected | BRAIN.md Apr 7 entry "External Review Decisions" |
| Apr 7 2026 | Pre-register Arm 3 benchmark before Mac Mini arrives | Eliminates "you optimized after seeing results" objection | Registering after: rejected | BRAIN.md Apr 7 entry |
| Apr 7 2026 | Brier Skill Score added to calibration tracker | Raw Brier undefendable without market difficulty context. BSS = 1 - (swarm/crowd). | Raw Brier only: rejected | BRAIN.md Apr 7 entry |
| Apr 7 2026 | Latent Echo test added to Mac Mini Day 1 protocol | Test alignment before benchmark. If divergence >5%, W_a alignment matrix is failing. | Jump straight to benchmark: rejected | BRAIN.md Apr 7 entry |
| Apr 7 2026 | Statistical significance + narrative cluster weighting added to benchmark report | Need confidence intervals and p-values by Day 30. Weight by theme cluster to prevent AI regulation counting as 3 independent wins. | Reporting raw numbers only: rejected | BRAIN.md Apr 7 entry |

The architectural rule from April 6 — *LLMs handle judgment, scripts handle everything else* — is the most consequential decision in this era. It establishes the separation between deterministic operations (file reading, API calls, timestamp comparison) that live in Python and judgment operations (synthesis, prioritization, drafting, reasoning) that live in the LLM layer. The rule appears repeatedly in subsequent decisions as the principle being applied — pull components do only the pull because pulls are deterministic; the founder owns interpretation because interpretation is judgment; benchmark-updater modifies data sections but not methodology because methodology is framing-judgment that belongs to the founder.

## 4.3 Maturation (April 8 - April 17, 2026)

The maturation era built out the discipline layer around the upcoming Mac Mini work. The decisions in this era are characterized by *pre-commitment before evidence* — pre-registered experiments, pre-decided thresholds, citation discipline, three-proofs gates on external pitches. The pattern is: anticipate where the project will be tempted to skip discipline once results arrive, write the discipline into protocol before that pressure exists. This era also includes the Phase 10/11 self-correction sequence on April 14 — the project's clearest documented example of the testing-further-than-comfortable discipline working in real time.

| Date | Decision | Why | Alternative rejected | Reproducer |
|---|---|---|---|---|
| Apr 8 2026 | Category filter added to calibration tracker | Sports/entertainment markets drag BSS negative. Primary track now policy/macro/geopolitics/elections. | Probability filter alone: still scores wrong market types | BRAIN.md Apr 8 entry "Category filter added" |
| Apr 8 2026 | Dual-track Brier reporting implemented | Policy track = thesis test. Full track = transparency. No one can accuse us of hiding results. | Single track: hides sports results or pollutes headline | BRAIN.md Apr 8 entry |
| Apr 8 2026 | 0.0247 Brier number clarified as historical-not-live | Came from April 4 historical benchmark, not live tracker. Two different datasets. Must not be conflated. | Citing without context: misleading | BRAIN.md Apr 8 entry "0.0247 Brier number clarified" |
| Apr 8 2026 | Bayesian Updater dropped from text-swarm | Trial week complete. Tracking identically to Quant Researcher on 9 of 11 markets. No added signal, adds API cost. | Keep permanently: rejected, no evidence of added value | BRAIN.md Apr 8 entry; executed Apr 11 |
| Apr 8 2026 | Rain grant parked until Mac Mini latent results | Middle path leaks too much thesis while ecosystem is converging. Resubmit late April. | Draft now: premature without latent results | BRAIN.md Apr 8 entry "Three Strategic Decisions" |
| Apr 11 2026 | Mac Mini experiment spec locked at v2.0 (pre-registered) | Grok review found two fatal flaws in v1.0 (statistical underpowering, Echo test not continuous). Both fixed. No amendments after first run. | Run on v1.0: insufficient statistical power | BRAIN.md Apr 11 entry "Mac Mini Experiment Spec Pre-Registered (v2.0)" |
| Apr 11 2026 | Motor-car tests with two-of-four threshold for external claims | Performance alone is horse territory. A verdict requires multi-test evidence. | Single-metric external claims: rejected | BRAIN.md Apr 11 entry "Strategic Framing: The Motor Car Tests" |
| Apr 11 2026 | NHRT dataset moat framing — log every latent exchange | High-entropy non-human reasoning trace data is irreplaceable session-by-session. Daily logging is asset accumulation, not optional. | Selective logging: data lost permanently | BRAIN.md Apr 11 entry "Non-Human Reasoning Traces (NHRT)" |
| Apr 11 2026 | Three proofs gate on Transparency Inversion pitch | Latent + Shadow Self is more auditable than text-only — but only with measured proofs. No proof, no pitch. | Pitch theoretical claim: rejected | BRAIN.md Apr 11 entry "Transparency Inversion — Sharpened" |
| Apr 11 2026 | LOCKED DECISIONS block added to commercialization-agent prompt | Agent recommended Rain grant 5 days running despite all-engines park decision. Compounding pressure to re-derive locked positions. | Allow agent to revisit decisions freely: triggers re-derivation | BRAIN.md Apr 11 entry "Three Decisions Executed" |
| Apr 14 2026 | Phase 10 result relabeled "Role Diversity Scaling Result" — Phase 11 retraction | Phase 11 revealed Phase 10 divergence came from agent role diversity, not latent channel. Latent channel not influencing generation. | Cite Phase 10 as latent evidence: rejected, retracted same day | BRAIN.md Apr 14 entries "Phase 10 Scaling Test Results" and "Phase 11 Critical Finding" |
| Apr 14 2026 | Activation steering as engineering frontier | Phase 11 showed external chaining doesn't influence generation. Internal injection required. | Continue external chaining work: rejected | BRAIN.md Apr 14 entry "Phase 11 Critical Finding" |
| Apr 15 2026 | Semantic invariance test required for "directional steering" claim | Contrastive injection 35% bearish result was complement arithmetic, not belief update. New test forces format to remove confound. | Cite arithmetic-confounded result as directional steering: rejected, retracted same day | BRAIN.md Apr 15 entry "Contrastive Injection Correction" |
| Apr 17 2026 | Compression-researcher and revenue-strategist timeout extended 120s → 180s | Multiple timeouts blocking overnight runs. Wrapper retry insufficient at 120s. | Continue at 120s: rejected, persistent failures | BRAIN.md Apr 17 entry "Infrastructure Fully Operational" |

The Phase 10/11 self-correction sequence on April 14 deserves particular attention. Phase 10 was logged as a milestone result — latent coordination preserved more divergence than text coordination as agent count scaled — and was almost immediately retracted when Phase 11 revealed the divergence came from agent role diversity rather than from the latent channel. The result was relabeled, the do-not-cite list was updated, and the engineering frontier shifted to activation steering. The same shape repeated April 15 with the contrastive-injection arithmetic confound: a "directional steering confirmed" milestone was retracted within hours when the result was diagnosed as complement arithmetic rather than belief update, and the semantic invariance test was designed specifically to remove the confound. The pattern is *don't stop at the first positive result; design the next test that would distinguish the result from a confound; retract scope when more rigorous testing contradicts*. The April 15 semantic invariance test that survived its own scrutiny — bullish injection 35% → 75% with stance-specific reasoning — is the project's "first flight" result.

## 4.4 Post-reset (April 18-19, 2026 onward)

The post-reset era responded to the April 18 contamination discovery with structural fixes the original architecture had not anticipated. The decisions in this era are characterized by *architecture-level interventions* — adding the missing component (polymarket-pull), formalizing the evidence hierarchy (Tier 1/2/3), establishing the Reproducer Requirement, and creating the Trinity bootstrap as the contamination-resistant successor to the brainload pattern. The era is also characterized by *unloads* — deliberately turning off components (commercialization-agent, benchmark-updater, eventually revenue-strategist) until structural conditions for safe restoration are in place.

| Date | Decision | Why | Alternative rejected | Reproducer |
|---|---|---|---|---|
| Apr 18 2026 | Benchmark-updater unloaded pending v0.2 template | v0.1 report carries "vs crowd" framings that anchor contaminated narrative. Template-level fix required, not data fix. | Continue updating v0.1: propagates contamination | incident_ledger.md April 18 incident; state_manifest.md benchmark-updater entry |
| Apr 19 2026 | Polymarket-pull added as 9th launchd job (4:40 AM) | Closes the architectural gap that produced the contamination. Live-data file at `data/polymarket/YYYY-MM-DD.json` replaces seed-file fallback. | Continue with seed-file fallback: contamination root not closed | incident_ledger.md Section 4 root cause; state_manifest.md polymarket-pull entry |
| Apr 19 2026 | Commercialization-agent unloaded | Pattern A Social Proof Loop: agent's compounding logic amplified contaminated upstream evidence. Cannot reload until structural fixes (split output dirs, mtime-based selection, separation from revenue-strategist read paths) are in place. | Reload after data fix only: compounding architecture still vulnerable | incident_ledger.md Pattern A; state_manifest.md commercialization-agent entry |
| Apr 19 2026 | Tier 1/2/3 evidence hierarchy formalized | Tier 1 = observed once, not audited. Tier 2 = reproducible internally, source verified. Tier 3 = externally defensible, raw-to-report audited. Required for grants/outreach/investor communications. | Continue with implicit evidence levels: no enforcement gate | intent.md "Ground Truth" section; BRAIN.md top-banner status block |
| Apr 19 2026 | Trinity bootstrap pattern replaces brainload-of-BRAIN.md | BRAIN.md contaminated as current-state authority. Trinity files (intent.md + state_manifest.md + incident_ledger.md) provide contamination-resistant grounding. | Continue brainload of full BRAIN.md: re-loads contamination | docs/intent.md; docs/state_manifest.md; docs/incident_ledger.md; current handoff folder |
| Apr 19 2026 | All pre-April-19 forecasting claims retracted | "45% Brier improvement," "20-day AI regulation divergence," "Shadow Match divergences," "0.0247 calibration Brier," all "vs crowd" framings — derived from fictional seed file. | Selective retraction: leaves contamination surface | incident_ledger.md April 18 incident; intent.md "Retracted / Invalidated" |
| Post-reset | Reproducer Requirement: every claim in load-bearing docs needs a verification command | Claims that compound across engines without anyone returning to raw data are the named contamination-amplification mechanism. | Trust claims by source authority: rejected | state_manifest.md Reproducer Requirement; intent.md verification discipline |
| Post-reset | Mixed-Source Synthesis Rule: claims combining multiple sources must name each source explicitly | Synthesizing across documents without source attribution loses the audit chain. | Implicit synthesis: rejected | incident_ledger.md Mixed-Source Synthesis Rule origin |
| Post-reset | Failure Escalation Protocol: silent failures must be surfaced | Pattern A's invisibility from inside the component required a protocol-level surfacing mechanism. | Trust components to fail loudly: insufficient | incident_ledger.md Failure Escalation Protocol origin |
| Post-reset | $10M external-claim threshold | External claims require Tier 2 reproducible internal evidence and Tier 3 externally-defensible audit chain. Cost of cited-and-retracted is higher than cost of waiting. | Direction-promising Tier 1 claims: rejected for external use | intent.md Tier 1/2/3; build_log.md §1.8 |
| May 2 2026 | Revenue-strategist unloaded | Part of post-reset stabilization, pending structural decisions about input set now that Polymarket is pulled live and seed-file dependency is removed. | Reload immediately: structural questions unresolved | state_manifest.md revenue-strategist entry |

The post-reset era is structurally different from the three eras that preceded it. The first three eras built the system *outward* — adding components, sharpening experimental design, layering disciplines. The post-reset era builds the system *inward* — closing architectural gaps, formalizing evidence requirements, retiring or quarantining components whose designed compounding behavior cannot be safely re-engaged without structural fixes. The era is unfinished. The structural prerequisites for restoring commercialization-agent, benchmark-updater, revenue-strategist, and the v0.2 benchmark report template are documented in state_manifest.md and incident_ledger.md, and the work to satisfy those prerequisites is ongoing.

The deepest decision in the post-reset era — the one that shapes all the others — is the Trinity bootstrap pattern. The original brainload-alias-of-full-BRAIN.md design assumed a single canonical source-of-truth file that could be re-loaded at the start of each session. The April 18 contamination invalidated that assumption: BRAIN.md itself had become contaminated as a current-state authority, and re-loading it at session start would re-load the contamination. The Trinity pattern separates clean documents (intent.md, state_manifest.md, incident_ledger.md) from the contaminated historical record (BRAIN.md), and reads only the clean documents at session start. The pattern's structural insight is that *contamination resistance requires document segregation, not document warnings* — a contaminated document with a "do not trust" banner at the top is still being read, and the contents below the banner are still entering the reader's working context. The Trinity pattern removes contaminated documents from the bootstrap entirely.

# 5. Incidents that shaped the project

This section documents incidents in the project's history. It necessarily references metrics, claims, and framings that were later retracted. Those references are preserved for context — the design lessons depend on knowing what specifically was claimed, by which mechanism, and how it was caught or how it propagated. Do not cite the contaminated metrics referenced below as current-state evidence. The canonical retraction list and the formal incident record live in `docs/incident_ledger.md`; this section's job is the *design lesson*, not the full record.

The incidents are organized chronologically because the arc matters. The discipline of testing-further-than-comfortable was working consistently throughout the project's history. The April 18 contamination was the case where that discipline could not catch the failure, because the failure was upstream of every analytical layer the discipline operated at. Reading the incidents in order makes that contrast visible. The post-reset architectural response only makes structural sense in the context of *what kind of failure the prior architecture could not detect*.

## 5.1 The Bayesian Updater trial — April 5 to April 11, 2026

The earliest documented incident-shaped event in the project's mature operating period was not a failure but a *successful pre-committed experiment*. On April 5, 2026, Grok recommended adding a fourth agent to the text-swarm — a Bayesian Updater that would anchor the swarm against narrative drift by updating only on concrete evidence and ignoring sentiment. The proposal was accepted with explicit conditions: it would run as a *trial week* with a pre-committed evaluation date of April 12, and pre-committed drop criteria. If the Bayesian Updater tracked identically to the Quant Researcher on most markets, it would be dropped.

The April 12 evaluation showed exactly the predicted pattern: the Bayesian Updater tracked identically to the Quant Researcher on 9 of 11 markets. No added signal, only added API cost. The drop criteria fired, and the agent was removed from text-swarm on April 11 (one day ahead of the formal evaluation date because the pattern was already clear).

The design lesson is the *pre-committed evaluation* shape. The trial was structured so that the project could not rationalize keeping the Bayesian Updater after observing its behavior — the drop criteria were specified in writing before any data came in, and the data either fired the criteria or did not. The same pattern recurs throughout the project's later history: Mac Mini experiment spec v2.0 pre-registration (April 11), motor-car tests with two-of-four threshold (April 11), the 30-day paper trading clock (April 4 forward). Each is a pre-committed evaluation that closes off post-hoc rationalization at the moment of evaluation.

*Reproducer: BRAIN.md April 5 entry "4th Agent Added to Text Swarm" with the pre-committed trial; April 8 entry "Bayesian Updater — drop after April 12" with confirmed criteria; April 11 entry "Bayesian Updater dropped from swarm" with execution.*

## 5.2 The Rain grant compounding pressure — April 11, 2026

The next incident-shaped event surfaced the *first observation* of what would later become recognizable as the Pattern A Social Proof Loop. The commercialization-agent had been recommending Rain grant submission for five days running, despite the all-engines decision on April 5 to park the grant until Mac Mini latent results were in hand. The agent's compounding-conviction-over-time design was working as built — it was reading its own previous output as input and accumulating conviction on its preferred strategic move — but the move it was accumulating conviction on had been explicitly de-committed at the strategy layer.

The fix on April 11 was a "LOCKED DECISIONS" block added to the agent's prompt, listing the explicit pre-committed decisions the agent should not re-derive. The fix worked for the specific case: the agent stopped recommending Rain grant submission and the running thesis no longer compounded the position.

What the fix did *not* do, and what later became architecturally consequential, is generalize. The April 11 fix operated at the prompt-engineering layer — instruct the agent which decisions are locked. It did not address the *structural* compounding mechanism: that an agent reading its own previous output as input will accumulate conviction on whatever its prior outputs claimed, and that prompt-level instructions cannot constrain the compounding when the *upstream evidence the agent reads is contaminated*. By April 19, the same architectural shape that produced the Rain grant re-derivation produced an entire compounded thesis built on contaminated baselines. The April 11 incident was a small, recoverable instance of a failure mode the project did not yet recognize as architectural.

The design lesson is that *prompt-level fixes work for prompt-level problems but cannot substitute for architectural fixes when the underlying failure is structural*. The April 11 LOCKED DECISIONS block is preserved in the architecture as a design discipline — it remains a useful tool for constraining specific re-derivation pressure on a known-locked decision — but it does not make a compounding agent contamination-resistant. That property requires architectural intervention (split output directories, mtime-based input selection, separation of read paths from compounding outputs), which the post-reset response would later implement.

*Reproducer: BRAIN.md April 11 entry "Three Decisions Executed" with the LOCKED DECISIONS block addition; incident_ledger.md Pattern A description for the architectural generalization.*

## 5.3 The Phase 10 / Phase 11 self-correction — April 14, 2026

The Phase 10 / Phase 11 sequence is the project's clearest documented example of the testing-further-than-comfortable discipline working in real time, and it is preserved in detail because the same discipline shape appears in subsequent incidents.

On the morning of April 14, the Phase 10 scaling test was completed and logged as a milestone. The result — using sequential delta chaining on Phi-3 Mini at 2/4/8 agents — showed that latent coordination preserved more divergence than text coordination as agent count increased, with the divergence holding after removing the strongest single example (CPI). The result was framed as evidence that *latent vector delta communication resists consensus collapse better than text coordination as swarms scale*. The defensible-claim formulation was logged with appropriate caveats: do not claim better forecasting, alpha generation, or replacement of text — these require resolved-outcome calibration data.

The same day, Phase 11 ran the next test. The result was 0.0000 divergence across all 11 markets in Arm 4 (latent swarm). Every agent gave identical estimates. The latent channel was not influencing generation.

The diagnosis was structural: hidden state extraction and text generation are two separate forward passes. Updating the seed vector externally has no effect on what the model generates. Each agent gets a fresh prompt and generates independently regardless of seed state. The Phase 10 divergence was real, but it was caused by *agent role diversity*, not by latent delta chaining. The Contrarian agent (Agent 3) consistently produced different estimates regardless of whether the latent mechanism was active.

The retraction was immediate and complete. Phase 10 was relabeled "Role Diversity Scaling Result." The do-not-cite list was updated to exclude Phase 10 as latent-channel evidence. The engineering frontier shifted from external chaining to activation steering — the next mechanism that could plausibly make latent state affect generation. The motor-car tests were re-evaluated against the corrected understanding.

The design lesson is the *don't-stop-at-the-first-positive-result* discipline. Phase 10 looked like motor-car evidence. The team had spent days building toward it. The temptation to publish or cite the result was real — it would have validated the thesis. Instead, the next test was run with the same rigor as the result-producing test, and the next test revealed the prior interpretation was wrong. The result was retracted within hours of being claimed, before any external citation surface existed.

This is the discipline shape that worked. Section 5.5 will name *why this discipline could not catch the contamination*, but the discipline itself, as documented here, is the project's first-line defense against premature thesis claims. It survived the contamination response unchanged and remains operative.

*Reproducer: BRAIN.md April 14 entries "Phase 10 Scaling Test Results (MILESTONE)" and "Phase 11 Critical Finding + Four-Engine Synthesis (MILESTONE)" — both entries logged the same day, with Phase 11 explicitly retracting Phase 10's framing.*

## 5.4 The contrastive arithmetic correction — April 15, 2026

April 15 produced four successive milestones in a single day, three of which were retracted or revised by the next. The discipline shape from Phase 10 / Phase 11 repeated, this time within hours rather than across phases.

The morning's activation steering proof-of-concept was the first milestone. Random residual injected at layers 16/20/24 at scale 0.3 produced different outputs on 2 of 5 markets — "INJECTION IS WORKING. Latent channel can influence generation." The framing held: greedy decoding ensured any difference was from injection effect, not sampling randomness, and the changed outputs showed different reasoning paths rather than random text drift.

The afternoon's directional steering test was the second milestone, this time framed as a *self-correction*. Bullish and bearish injections at multiple scales produced identical probability shifts. Both moved estimates up by the same amount. The conclusion was that activation steering transmits *intensity not direction* — both bullish and bearish prompts activate similar market-analysis regions of the latent space, and the residual encodes the magnitude of departure from seed, not the semantic direction of that departure.

The evening's contrastive injection test was the third milestone — and this is where the discipline pattern is most visible. Computing a contrastive vector (h_bullish minus h_bearish) and injecting it at scale 0.45, the result was a Bitcoin probability shift from 65% to 35% on bearish injection — a 30 point directional drop. This was logged as "the first evidence of directional semantic control in the latent channel."

Within the same day, the contrastive injection result was *retracted by self-correction*. The team examined the model's reasoning under the bearish injection and identified that the 35% result was not a belief update — it was complement arithmetic. The model's reasoning ran "65% for 80k, so 100% minus 65% is 35% for 60k." The injection had flipped which side of the probability was being reported, not the underlying belief. There were no bearish arguments in the reasoning. The framing was: *Current results are framing/logit hijacks, not belief updates.*

The corrective test — the semantic invariance test — was designed within hours of the retraction. Agent B's prompt was rewritten to force a specific output format ("After considering all factors, my probability that Bitcoin reaches 80k first is X%, then 2-3 sentences of actual reasoning") with explicit instruction to produce no complement arithmetic. The four evaluation criteria were specified in advance: probability moves up under bullish, reasoning contains stance-specific arguments, no complement flip language, ordered bullish > control > bearish.

The semantic invariance test ran the same evening. The result — bullish vector at scale 0.4 produced 35% → 75% with stance-specific bullish reasoning ("institutional investments, positive sentiment, strong upward trajectory") and no hedging — survived the four-criterion check. This is the project's "first flight" result, and it is preserved as Tier 2 valid in `docs/intent.md` because the test that produced it was specifically designed to remove the confound that contaminated the prior result.

The design lesson compounds Phase 10 / Phase 11. The same testing-further-than-comfortable discipline operated three times in a single day: PoC → directional test → contrastive arithmetic correction → semantic invariance test. Each iteration removed a confound from the prior interpretation. The result that survived was the result that had been tested against every confound the team could anticipate. The discipline in this incident is *iterative confound-removal*: each test asks "what alternative explanation could produce this same observation?" and the next test is designed to distinguish the genuine result from the alternative.

The asymmetry observed in this incident — bullish injection works, bearish injection breaks coherence — became the April 17 bearish asymmetry finding, which intent.md flags as under re-audit because the asymmetry may reflect proxy contamination from the synthetic seed rather than directional physics in the latent space. The first-flight bullish result is structurally clean (it was produced on Mac Mini MPS using real Phi-3 hidden states with no seed-file dependency), but the bearish-asymmetry interpretation depends on baselines that were contaminated, and the interpretation is therefore preserved provisionally rather than as confirmed.

*Reproducer: BRAIN.md April 15 entries "Activation Steering PoC RESULT," "Directional Steering Test Results," "Contrastive Injection RESULT (MAJOR MILESTONE)," "Contrastive Injection Correction (Important)," and "TRUE LATENT STEERING CONFIRMED (MAJOR MILESTONE)" — all five entries logged the same day, with the final entry surviving its own scrutiny and the prior three retracted or revised.*

## 5.5 The April 18 contamination

The April 18 contamination is the project's largest documented incident. The full incident record lives in `docs/incident_ledger.md`; this section's purpose is the *design lesson*. What follows is a compressed account of what happened, framed around the architectural insight the incident produced.

Contaminated claims that propagated and were later retracted include: an apparent "45% Brier improvement over naive baseline on 18 resolved Polymarket markets" that derived from comparison against the seed file rather than against live market data; a "20-day AI regulation divergence" framing that cited swarm probabilities against contaminated crowd baselines; a "0.0247 calibration Brier" figure that was being cited interchangeably with the historical-benchmark Brier despite operating on different datasets; multiple "Shadow Match divergence" comparisons (Powell, US-Iran, Bitcoin) where the crowd values were drawn from the seed file. None of these claims should be cited as current-state evidence; the canonical retraction list is in `docs/incident_ledger.md`.

The mechanism, in compressed form: the curated `policy_markets_seed.json` file created on March 29, 2026 as a Kalshi-RSA-auth workaround was being read by downstream prediction generators (text-swarm, calibration-tracker, shadow_match) as if it contained live Polymarket data. The text-swarm and calibration-tracker components produced apparently-meaningful "vs crowd" comparisons against the seed file's contents. Those comparisons were read by benchmark-updater into the v0.1 benchmark report, were read by commercialization-agent into the running thesis where they compounded over days, and were referenced in the Rain grant draft and outreach drafts. The contamination propagated outward through the reporting layer and inward through the strategic-synthesis compounding loop. By April 18, twenty days of accumulated claims rested on fictional baselines.

The discovery happened during routine work on the April 17 bearish asymmetry finding. Investigation into *why* the bearish injection direction was producing inconsistent results led to closer examination of the underlying market data, and the data examination revealed the seed file was being read as if it were live data. The contamination was identified, the propagation chain was mapped, and the April 18-19 incident response began.

The architectural lesson is the deepest in the project's history. *Defense-in-depth at analytical and citation layers does not protect against contamination at the data-source layer.* The project had built layers of analytical rigor: the architectural rule that LLMs handle judgment and scripts handle everything else, dual-track reporting (primary policy track vs full all-categories track), Brier Skill Score for difficulty context, citation discipline with explicit safe-citations and do-not-cite lists, three transparency-inversion proofs gated on measurement, motor-car tests with two-of-four required for external claims, pre-registration of experiment specs, statistical significance and theme-cluster weighting requirements. Each discipline was rigorous. Each was honestly applied. None could catch the contamination because the contamination was *upstream of every analytical layer the disciplines operated at*. The disciplines operated on the *output* of the contaminated input.

The Phase 10 / Phase 11 discipline that worked so cleanly on the activation steering work asks "what alternative explanation could produce this same observation?" — and that question, applied at the analytical layer, was the right question for the kind of error the project's prior incidents had been about. But it is not the right question for *data-source contamination*. The right question for that is: "is this data what I think it is?" And that question is upstream of analysis, upstream of citation, upstream of every layer where the project's disciplines operated. No component's design included a check for it, because no incident before April 18 had required one.

The structural fixes that followed are documented in Section 4.4 (Post-reset decisions) and `docs/incident_ledger.md`. The most consequential are: the addition of the polymarket-pull launchd job that closes the architectural gap allowing seed-file-as-live-data substitution; the formalization of the Tier 1/2/3 evidence hierarchy that requires explicit source-type tagging on every metric; the Trinity bootstrap pattern that segregates clean documents from contaminated documents at the session-startup layer; and the Reproducer Requirement that every claim in load-bearing documents must include a verification command that a fresh agent could rerun.

The deepest fix — the one that addresses the failure mode rather than its visible artifacts — is the Trinity bootstrap. The original `brainload` alias loaded the full BRAIN.md at the start of every Claude session. After April 18, BRAIN.md itself was contaminated as a current-state authority, and re-loading it at session start would have re-loaded the contamination. The Trinity pattern's structural insight is that *contamination resistance requires document segregation, not document warnings*. A contaminated document with a "do not trust" banner at its top is still being read; the contents below the banner still enter the reader's working context. The Trinity pattern removes contaminated documents from the bootstrap entirely. The clean documents (`intent.md`, `state_manifest.md`, `incident_ledger.md`) are the bootstrap; BRAIN.md becomes a historical-design reference accessed deliberately, not a default load.

*Reproducer: incident_ledger.md April 18 incident for the full record and the canonical retraction list; BRAIN.md March 29 seed-file decision (the contamination root); Section 4.4 of build_log.md for the post-reset structural decisions; current Trinity files at `docs/intent.md`, `docs/state_manifest.md`, `docs/incident_ledger.md`.*

## 5.6 The bearish asymmetry under re-audit — April 17, 2026 onward

The bearish asymmetry finding was logged on April 17, 2026 as a Tier 1 result requiring further investigation. The activation steering work had confirmed bullish directional control (35% → 75% with stance-specific reasoning) but bearish injection was breaking coherence — applying the negative of the contrastive vector did not produce a corresponding bearish probability shift with bearish reasoning. The asymmetry was real in the sense that the experimental result reproduced under the same conditions; what was unclear was *what kind of asymmetry it was*.

Two interpretations were live at April 17. The first: the asymmetry reflects genuine directional physics in the latent space — bullish and bearish poles are not symmetric in the model's representation, and bearish content requires a different injection mechanism than simple sign-flipping of the bullish vector. The second: the asymmetry is an artifact of how the bearish baseline was constructed, possibly involving comparison against contaminated crowd values from the seed file.

The April 18 contamination discovery moved the second interpretation from "possible alternative" to "must rule out before claiming the first interpretation." The bearish asymmetry finding was placed under re-audit. It is currently flagged in `docs/intent.md` as a finding that may reflect proxy contamination rather than directional physics, pending re-validation against live data baselines that began accumulating April 20, 2026.

The design lesson is that *Tier 1 findings cannot be promoted past the contamination boundary without re-audit*. The bullish first-flight result (Section 5.4) is structurally clean — it was produced on Mac Mini MPS using real Phi-3 hidden states with no seed-file dependency in the experimental pipeline. The bearish asymmetry finding, by contrast, rests on baselines whose construction may have included contaminated values, and the finding cannot be cited as evidence-of-directional-physics until the re-audit completes. This is the Tier 1/2/3 evidence hierarchy operating in practice: a finding that was directionally interesting at Tier 1 must clear Tier 2 (reproducible internally, source verified) before it can support any thesis claim.

The bearish asymmetry under re-audit is also the *first incident in the post-reset era* — the first case where the new evidence-tier discipline was applied to a finding the prior architecture would have promoted faster. The post-reset architecture's insistence on source-type tagging on every metric, combined with the Tier 1/2/3 hierarchy, is what surfaced the bearish-asymmetry baseline question and produced the re-audit decision rather than continued work on the directional-physics interpretation.

*Reproducer: BRAIN.md April 17 entry "Infrastructure Fully Operational (Day 14)" with the bearish asymmetry observation; intent.md "Under re-audit" section; incident_ledger.md April 18 incident for the contamination context that produced the re-audit decision.*

## 5.7 The shape of incidents this project has had

Reading the incidents in order reveals a pattern. Five of the six incidents were either *self-corrections that worked* (Bayesian Updater drop, Phase 10/11, contrastive arithmetic correction) or *small failures caught at the prompt level* (Rain grant compounding pressure) or *findings appropriately held provisionally* (bearish asymmetry under re-audit). The discipline of testing-further-than-comfortable, applied consistently, caught these incidents either before they propagated or at a propagation surface small enough to recover from.

The April 18 contamination was different in kind. It was not an analytical error caught by analytical discipline. It was a data-source error that the analytical disciplines were structurally incapable of catching, because every discipline operated downstream of the contaminated input. The contamination propagated for twenty days because the project's defense-in-depth had a missing layer at the bottom — *data integrity verification*. The post-reset architecture adds that layer through the polymarket-pull component, the Tier 1/2/3 hierarchy, the Reproducer Requirement, and the Trinity bootstrap pattern.

The deepest design lesson is that *defense-in-depth is necessary but the bottom layer must be data integrity*. Analytical rigor at the upper layers does not propagate downward to verify inputs. Citation discipline does not verify what is being cited. Pre-registration does not verify the data the registered experiment will be run against. Each upper-layer discipline assumes the layer below it is sound. When the bottom layer (data integrity) is unverified, every layer above it operates on assumed-sound input, and a failure at the bottom propagates upward through every layer's correct operation.

The post-reset architecture is the project's response to having learned this lesson concretely. The disciplines that were operating before April 18 are preserved — they remain useful at the layers they operate at — but they are now built on top of a data-integrity layer that did not exist in the original architecture. The polymarket-pull component is the most visible piece of that layer, but the architectural shift is broader: every load-bearing claim now requires source-type tagging, every metric now has Tier classification, every load-bearing document now requires reproducer commands, and every Claude session bootstrap now uses contamination-resistant document segregation rather than full-load of a single source-of-truth file.

The project's incidents shaped the project. The Phase 10/11 sequence and the contrastive arithmetic correction shaped how the project tests its own results. The Bayesian Updater trial shaped how the project conducts pre-committed experiments. The Rain grant compounding pressure shaped how the project handles strategic re-derivation. The April 18 contamination shaped the entire data-integrity layer that now sits underneath everything else. Each incident is preserved in this section because the design lesson it taught is operative in the current architecture.

*Reproducer: this section's per-incident reproducers, plus the post-reset architectural decisions in Section 4.4, plus incident_ledger.md as the canonical incident record.*