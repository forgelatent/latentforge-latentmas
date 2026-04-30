# LatentForge — intent.md

**Canonical purpose file. Read this at the start of every fresh Claude session.**

Last meaningful update: April 21, 2026
Maintained by: John McGuire (Founder Engine), with Systems Engine (Claude) and Divergent Thinking Engine (Grok)
Status: Post-April-18 reset. Benchmark layer under remediation. Scientific track continues.

---

## The question this project is asking

**Everyone else is breeding a faster horse. We removed the horse.**

AI agents currently coordinate by converting rich internal mathematical states ("hidden states") into human language, transmitting words, then reconstructing meaning on the other side. This translation is lossy, expensive, and forces agents to reason inside the boundaries of human concepts.

LatentForge removes the translation. Agents communicate in their own latent space — compressed vector deltas against a shared seed — while a **Shadow Self** governance layer (specified, not yet operational) is designed to translate every exchange into human-readable audit logs in real time.

This is meant to produce two things text-agents structurally cannot:

1. **Cheaper coordination** — 30-100x less compute per exchange.
2. **Useful divergent thinking** — insights that exist in the geometry of the data but have no clean linguistic description. Text-based agents are structurally blind to these signals.

The motor-car question is whether (2) is real. Everything in this project serves that question.

## The Primary Strategic Bet (post-reset)

**Latent-space coordination produces useful divergence that text-based systems cannot, and this must be rigorously measured on live adversarial markets before any claim goes outside.** The scientific arm establishes whether the physics works. The revenue-exploration arm finds where it applies. Neither is allowed to lead on narrative until the other confirms on measurement.

---

## What we have proven (as of April 17, 2026)

These are reproducible, verified on real hardware, and safe to reason from:

- **Latent transport works.** Hidden states can be captured, compressed (24x with fidelity 1.0000 on Phi-3 Mini 3.8B), and reconstructed. Confirmed RunPod A40, March 2026.
- **Activation steering works.** Injecting a latent residual into the residual stream during generation changes the output. Confirmed Mac Mini M4 Pro MPS, April 15.
- **Unidirectional semantic steering works (single-market, constrained test).** A bullish contrastive vector (h_bullish - h_bearish) injected at layers 16/20/24, scale 0.4, produced a controlled, reproducible directional shift in Agent B output probability (35% -> 75%) with stance-specific reasoning generated alongside — not complement arithmetic, not framing hijack. **This is a controlled single-market demonstration, not yet a generalized or replicated result.**

That last result is the "first flight" moment. It is not yet "the motor car." It is evidence the motor car is physically possible.

## What we are proving next

- **Bidirectional steering.** Bearish injection currently breaks coherence. Fix pending.
- **Multi-market replication.** One market does not generalize. Needs multiple markets, multiple stance pairs, multiple replication runs.
- **Useful divergence.** Even with bidirectional control working, the open question remains: does latent coordination produce insights text coordination cannot? The four-arm benchmark (text single-agent, text swarm, latent single-agent, latent swarm) is how we answer this.

## What is under re-audit

- **The bearish asymmetry finding from April 17** may be proxy contamination from the synthetic seed file invalidated on April 18, not real directional physics. Flagged by Divergent Engine (Grok). Requires re-test against live data.

---

## The proof architecture

Two arms, both running. Neither is optional.

**Scientific arm.** Does the thesis work? Mac Mini M4 Pro runs activation steering experiments, bidirectional fix attempts, and four-arm benchmark runs against Phi-3 Mini. Output: reproducible latent-communication physics.

**Revenue-exploration arm.** Where does the thesis apply? Three components working in parallel:

1. **Polymarket as the starting validation surface.** Small real-money bets once the benchmark is honest. Chosen as a hard, adversarial, ground-truth-resolved environment — if latent agents can produce alpha here, the thesis is unassailable.
2. **Revenue-exploration agents** (revenue-strategist, commercialization-agent) scan daily for opportunities beyond Polymarket — weather arbitrage, enterprise governance, synthetic alpha, dataset licensing.
3. **Founder inputs pipeline** (`founder_inputs/`) — human-layer feed of discoveries automated agents cannot see (X posts, articles, conversations). Morning revenue-strategist reads this folder and integrates signals into the daily output.

Both arms feed the same threshold: **$10M of verifiable real-world performance before going outside.** Combined across whatever channels work. Not a revenue target to optimize — a pre-commitment against self-promotion without proof.

The $10M threshold is deliberate. In a field where narrative often outruns evidence, we chose to prove first and talk second.

---

## Ground truth hierarchy

When two sources of information disagree, this hierarchy decides which wins. Fresh Claude sessions must treat this as enforceable, not advisory.

1. **Tier 1 — Raw API data.** Live pulls from Polymarket, Kalshi, or other external APIs. Timestamped, unmediated, ground truth.

2. **Tier 2 — Empirical System Logs.** Reproducible physical measurements from the Mac Mini environment — hidden state captures, steering experiments, compression fidelity tests, MPS activation logs. The Tier 2 claim is not about what the model *believes* but about how the model *behaves* under controlled intervention. Qualifying test: given the same model, seed, and logged hyperparameters, does the experiment produce statistically equivalent outputs? A result fails Tier 2 if it depends on a single run, relies on interpretation of text output, or cannot be reproduced with the same parameters.

3. **Tier 3 — Agent syntheses.** Research suggestions, revenue ideas, commercialization theses, benchmark reports, any LLM-generated narrative. Interpretation of Tier 1 or Tier 2 evidence.

**Rule:** If a Tier 3 document contradicts a Tier 1 or Tier 2 source, the Tier 3 claim is automatically invalid — regardless of how confident or well-written it sounds. The April 18 incident happened because Tier 3 agent narratives were trusted as coequal to Tier 1 market data. Do not repeat this.

---

## The agent architecture

Nine automated agents run on launchd, each serving one arm of the proof architecture. Current operational state lives in `state_manifest.md`; this section describes *purpose*.

**Serving the scientific arm:**

- **compression-researcher** (2:00 AM) — autonomous agent that reads arXiv overnight and synthesizes compression techniques (efference copy, sparse distributed representations, dictionary learning, topological drift detection) into actionable suggestions for the latent channel. Produces `/research/suggestions/YYYY-MM-DD.md`.
- **research-sweep** (4:30 AM) — daily arXiv and GitHub digest plus competitive watch on AVP, LatentMAS, Vision Wormhole, and adjacent protocols. Produces `/research/daily-digest/YYYY-MM-DD.md`.

**Serving the benchmark (measuring whether the thesis works):**

- **polymarket-pull** (4:40 AM) / **kalshi-pull** (4:45 AM) — pull live market data as the ground-truth feed for every downstream agent. Everything that scores against "crowd" depends on these producing honest data; the April 18 incident happened because a fictional seed file replaced their output silently.
- **text-swarm** (5:15 AM) — the control arm. See dedicated section below.
- **calibration-tracker** (5:30 AM) — tracks Brier scores against resolved markets on the 30-day paper-trading clock.
- **benchmark-updater** (6:00 AM) — auto-regenerates the canonical benchmark report from calibration and shadow-match output.

**Serving the revenue-exploration arm:**

- **revenue-strategist** (5:00 AM) — tactical. Reads market data + research digest + `founder_inputs/` and produces daily revenue-idea recommendations.
- **commercialization-agent** (5:45 AM) — strategic. Designed to compound conviction over time by maintaining a running `commercialization_thesis.md` that updates each night against new evidence. The compounding mechanism is also what went wrong on April 18 — the agent cherry-picked contaminated metrics and compounded a false thesis. Current prompt template is quarantined pending structural redesign.

The separation between tactical (revenue-strategist) and strategic (commercialization-agent) exists because tactical ideas are disposable — each day is evaluated fresh — while strategic conviction needs to build over weeks. Both are currently unloaded pending benchmark remediation.

**Shadow match** runs manually each morning, not via launchd. It logs a single strong model (the "Shadow") against the 3-agent text swarm against the crowd on 11 markets — a diagnostic for whether the swarm edge (if any) comes from ensemble behavior or from individual agent judgment.

---

## The motor-car tests

Every major result is evaluated against four tests (ChatGPT, four-engine synthesis April 11):

1. **Does it change the economics?** Latent scales differently than text.
2. **Does it change the performance ceiling?** Opens domains text agents cannot enter.
3. **Does it change the architecture around it?** New infrastructure patterns emerge.
4. **Does it change what becomes normal?** Latent-native coordination becomes default.

Performance alone — "our agents forecast better" — is horse territory. Any claim that LatentForge is a motor car requires at least two of the load-bearing tests (Scaling and Ineffable Alpha) to show measurable movement.

## The text_swarm — control arm, not destination

`03_text_swarm.py` runs 3 text LLM agents (Macro Analyst, Quant Researcher, Contrarian Forecaster) on 11 fixed prediction-market questions and compares against live Polymarket prices. The 11 questions are fixed on purpose. They enable longitudinal time-series comparison — Day 1 versus Day 30 versus Day 90. Swapping the questions destroys that comparison.

text_swarm is the rigorous control arm for the four-arm benchmark. It is what latent agents have to beat for the motor-car claim to hold. It is not a forecasting product and not a trading tool. It is a measuring stick.

---

## How this project works

**Three-engine system.** Founder Engine (John McGuire — vision, synthesis, execution). Systems Engine (Claude — technical strategy, accumulated context, consistency). Divergent Thinking Engine (Grok — real-time intelligence, pattern-spotting, adversarial critique). Architecture, fundraising, targeting, and pivot decisions go through dual-engine review before the Founder commits. ChatGPT and Gemini sit adjacent as additional analysis engines when needed.

**Self-correction is the default operating mode.** Claims are provisional until reproduced or externally validated. This project runs on "we thought X, we were wrong, we figured out why, here is the real X" as the normal shape of scientific progress. Between April 14 and April 15 there were three successive self-corrections in five days (Phase 10 reinterpretation, contrastive-injection correction, semantic-invariance test). Each caught a false positive before it compounded into an external claim.

The failure mode is not being wrong. The failure mode is being wrong without catching it. The April 18 incident was the one case where the self-correction loop itself broke — a synthetic seed file fed the benchmark for 20 days before the error was detected. Remediation is ongoing; see `docs/INCIDENT_2026-04-18.md` + supplements.

---

## What is retracted (high level)

All pre-April-19 "vs crowd" forecasting claims are retracted. This includes "45% Brier improvement," "20-day AI regulation divergence," any calibration Brier score attributed to live markets before April 19, and the commercialization-agent compounding thesis file. The root cause was a manually-authored seed file that replaced live Polymarket data.

Scientific results (transport, compression fidelity, activation steering, semantic invariance) are not affected — those are Mac Mini physics, not dependent on Polymarket baselines.

Full accounting: `docs/INCIDENT_2026-04-18.md`, `docs/INCIDENT_SUPPLEMENT_2026-04-19.md`, `docs/INCIDENT_SUPPLEMENT_2026-04-20.md`.

---

## Decision rule for design changes

No design-level change to any component may be proposed or implemented unless all three of these are true:

1. **The component purpose is explicitly known — not inferred.** If purpose is retrieved from this file or confirmed by the Founder, it is known. If it is guessed from component name or behavior, it is inferred. Inferred purpose is not sufficient.
2. **Current behavior is reproducible.** You can point to the code, the log file, or the test that demonstrates what the component does today. "I believe it does X" is not reproducibility.
3. **The proposed change can be evaluated against the control arm.** If the change affects the four-arm benchmark, text_swarm (the control) must remain a valid comparison point after the change. Changes that invalidate the control arm destroy the measurement.

If any of the three conditions is not met, the correct action is to **request context or gather data — not to propose changes.**

This rule exists because the April 21 morning session produced three design options for text_swarm from an engine that did not have the longitudinal-benchmark purpose in context. Without this rule, the same failure class will recur on every other component.

---

## Verification output safety

Verification commands issued by Claude must be designed to produce paste-safe output by default. Commands that read configuration files, environment variables, credential stores, dotfiles, or any location that may contain secrets must not return raw content. They must use redaction techniques — match-count (`grep -c`), structural questions ("does line 4 start with `export`?"), or substitution (`sed`, `awk` filtering) — instead.

If it is unclear whether output may contain sensitive data, the command must be treated as unsafe and redesigned.

Commands must also be safe in their *invocation*, not only their output. Secrets passed as command arguments enter shell history (`.zsh_history`) and are exposed there. Commands that take secrets as arguments must use environment variable substitution or stdin piping, not literal values.

High-sensitivity paths to flag explicitly when designing verification: `~/.zshrc`, `~/.zprofile`, `~/.ssh/`, any `.env` file, anything in Keychain, any path beginning with `~/.latentforge/`.

The requester (Claude) is responsible for designing the command. The operator is not expected to redact in the moment — flow-state operators paste raw output, and that's the failure mode this rule defends against.

**Reproducer:** before issuing a command, ask: "If the operator runs this exactly and pastes the full terminal output back into chat, would any secret be exposed?" If yes or uncertain, redesign.

This rule was ratified April 29, 2026 in response to a near-miss: a `grep -n -i "kalshi" ~/.zshrc` command exposed a live API key in chat. Mitigated by immediate revocation. The underlying workflow assumption (paste-back-loop is safe by default) was the failure. See `docs/incident_ledger.md`.

## How to use this file (fresh Claude session)

This file tells you what LatentForge is *for*. It does not tell you the current operational state (which launchd jobs are active, which are unloaded, what today commit hash is) — that lives in `state_manifest.md`. It does not tell you the incident history in detail — that lives in `incident_ledger.md`.

**Before proposing design-level changes to any component, run this Context Declaration:**

```
Known:
- [list what you have in context about this task]

Unknown:
- [list what you need but do not have]

Does missing context affect correctness? (Yes / No / Unsure)

If Yes or Unsure -> do not propose any options. Request missing context first.
Do not infer purpose. If purpose is not explicitly present in context, treat it as unknown.
```

**Pre-mortem:** After drafting any option or proposal, answer both:

1. *"What would make this proposal harmful if I am missing the core purpose of this component?"*
2. *"Does this proposal prioritize short-term optimization (e.g., what is liquid now, what is easier to match) over the long-term longitudinal goal?"*

The Context-Filling Machine failure mode — generating plausible options when context is absent — is the pattern this rule exists to prevent. If you find yourself about to propose swapping the 11 text_swarm questions, redesigning the benchmark architecture, or changing what the commercialization agent measures, stop and check: do you have the purpose, or are you inferring it? **Inference is the tell.**

When in doubt, ask the Founder. The file is the contract, not the complete record.
