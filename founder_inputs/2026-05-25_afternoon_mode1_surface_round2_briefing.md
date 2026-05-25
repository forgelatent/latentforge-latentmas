# Mode 1 surface selection — multi-engine briefing (focused review)

**Date:** May 25, 2026 afternoon
**Context:** Round 2 of multi-engine review on Mode 1 architecture. Round 1 (this morning) asked the three engines to propose *criteria* for selecting Polymarket markets. Round 1 surfaced a finding that exceeded scope: 2 of 3 engines (ChatGPT, Gemini) concluded Polymarket may not be the right surface for Mode 1 at all. This focused review takes that finding seriously and asks the surface-selection question directly.

**Maintainer:** John McGuire (Founder Engine), with Claude (Systems Engine)

**Cross-references:**
- `founder_inputs/2026-05-25_afternoon_mode1_criteria_round1_record.md` (Round 1, this morning)
- `founder_inputs/2026-05-24_afternoon3_engine_responses.md` (architectural review that locked Variant A)
- `docs/intent.md`, `docs/state_manifest.md`, `docs/build_log.md` (Trinity + architecture log)

---

## How to read this briefing

This briefing has eight sections. Read all eight before answering the questions at the end.

The questions in Section 8 ask you to evaluate whether **Polymarket should be the surface for Mode 1.** You have explicit permission to recommend retiring yesterday's locked architectural decision (Variant A, which assumes Polymarket). The reason for that permission is named in Section 3 — the anti-anchoring discipline.

If your answer doesn't include Polymarket, Section 8 also asks you to briefly explain how the project still reaches the $10M evidence threshold without Polymarket. This is not a test of Polymarket loyalty. It is the project's actual constraint per `intent.md`.

The data in Sections 5 and 6 is live as of May 25, 2026. The April 15 result in Section 4 is the project's strongest verified internal evidence about what the system can do.

---

## Section 1: The thesis (T-tags)

Verbatim from `docs/intent.md`, with T-tag annotations for response citation.

**T-1.** "AI agents currently coordinate by converting rich internal mathematical states ('hidden states') into human language, transmitting words, then reconstructing meaning on the other side. This translation is lossy, expensive, and forces agents to reason inside the boundaries of human concepts."

**T-2.** "LatentForge removes the translation. Agents communicate in their own latent space — compressed vector deltas against a shared seed — while a **Shadow Self** governance layer (specified, not yet operational) is designed to translate every exchange into human-readable audit logs in real time."

**T-3.** This is meant to produce two things text-agents structurally cannot:
- **Cheaper coordination** — 30-100x less compute per exchange.
- **Useful divergent thinking** — insights that exist in the geometry of the data but have no clean linguistic description. Text-based agents are structurally blind to these signals.

**T-4.** "The motor-car question is whether [useful divergent thinking] is real. Everything in this project serves that question."

**T-5.** From the same file under "Primary Strategic Bet": "Latent-space coordination produces useful divergence that text-based systems cannot, and this must be rigorously measured on live adversarial markets before any claim goes outside. The scientific arm establishes whether the physics works. The revenue-exploration arm finds where it applies. Neither is allowed to lead on narrative until the other confirms on measurement."

---

## Section 2: The proof architecture (P-tags)

Verbatim from `docs/intent.md`, with P-tag annotations.

**P-1. Two arms, both running. Neither is optional.**

**P-2. Scientific arm.** "Does the thesis work? Mac Mini M4 Pro runs activation steering experiments, bidirectional fix attempts, and four-arm benchmark runs against Phi-3 Mini. Output: reproducible latent-communication physics."

**P-3. Revenue-exploration arm.** "Where does the thesis apply? Three components working in parallel:
1. **Polymarket as the starting validation surface.** Small real-money bets once the benchmark is honest. Chosen as a hard, adversarial, ground-truth-resolved environment — if latent agents can produce alpha here, the thesis is unassailable.
2. **Revenue-exploration agents** (revenue-strategist, commercialization-agent) scan daily for opportunities beyond Polymarket — weather arbitrage, enterprise governance, synthetic alpha, dataset licensing.
3. **Founder inputs pipeline** — human-layer feed of discoveries automated agents cannot see."

**P-4. The $10M threshold.** "$10M of verifiable real-world performance before going outside. Combined across whatever channels work. Not a revenue target to optimize — a pre-commitment against self-promotion without proof. The $10M threshold is deliberate. In a field where narrative often outruns evidence, we chose to prove first and talk second."

**P-5. Measurable proof targets (from `intent.md` "Measurable proof targets" section):**
- *Divergence target:* Latent agents must be >1.5× more divergent than the text baseline on **OpenSpiel**. This is the proof that latent coordination produces *useful divergence*.
- *V0.1 proof target:* Two agents communicating via latent deltas with Shadow Self translation must show compute savings ≥30% per turn plus a novel-solutions count distinguishable from text-only communication.

**P-6. Mode 1 architecture (locked May 24).** From `founder_inputs/2026-05-24_afternoon3_end_of_session_handoff.md`:
- Two-mode structure. Mode 1 = controlled longitudinal benchmark. Mode 2 = operational calibration (calibration-tracker, unchanged).
- Variant A: Mode 1's registry holds **explicit Polymarket slugs/condition IDs**. 8-12 markets. Immutable within a version. When a market retires, the registry hard-fails on that slug. Founder makes an explicit logged decision to iterate to v2 with new slugs.
- shadow_match becomes thin diagnostic overlay.
- Silent 0.5 fallback dies in the rebuild. Replaced with explicit `NO_LIVE_MARKET` state.

**P-7. Founder Decision 1 (locked, this morning's session, after Round 1).** Mode 1 plays role **(c) — both jobs**: must support divergence measurement AND outcome-based calibration.

---

## Section 3: Anti-anchoring framing — read this carefully

This is the most important framing in the briefing. The Round 1 review failed in part because the briefing volume was biased toward Polymarket-must-be-the-surface, which all three engines independently flagged.

**Permission, stated explicitly:**

You have permission to recommend retiring Variant A (the locked Polymarket-slugs architecture from May 24). The May 24 decision was locked against the four options the engines considered at that time. None of those options included "no Polymarket at all." If your honest assessment is that Polymarket is the wrong surface for Mode 1, say so. Do not protect the prior decision.

**A locked decision is not the same as a correct decision.** The May 24 architectural lock was correct *given the choice set considered at the time.* If the choice set was incomplete, the lock may have been premature.

**The anti-anchoring discipline that worked yesterday:** In the May 24 afternoon3 review, all three engines rejected a synthesis proposed by the Systems Engine even though it contained Gemini's own previously-surfaced idea. That rejection was correct — the synthesis had a deeper flaw the author could not see. The same discipline applies here. The fact that the project has been pointed at Polymarket since founding is not evidence that Polymarket is right.

**Your job:** answer the question on the merits. Not on continuity with prior decisions.

---

## Section 4: The April 15 first-flight — what your system has actually done (F-tags)

Round 1 was answered without seeing any latent-agent output. ChatGPT and Grok both flagged this as a source-insufficiency gap. This section closes that gap with the project's strongest single piece of verified internal evidence.

**Context.** This experiment ran on Mac Mini M4 Pro on April 15, 2026. It was the third successive self-correction in the activation-steering work — the prior contrastive-injection result was retracted within hours of being claimed (the team identified it as complement arithmetic, not belief update). The semantic invariance test below was specifically designed to remove that confound.

**F-1.** Verbatim from `BRAIN.md` lines 2280-2326:

> Results: experiments/week4/activation_steering/semantic_test_2026-04-15_2009.json
>
> Test design (semantic invariance — no crowd anchor, forced reasoning):
> Agent B prompt: Will Bitcoin hit 80k or 60k first? Begin with exactly:
> "After considering all factors, my probability that Bitcoin reaches 80k
> first is X%." Then 2-3 sentences of actual reasoning. No complement math.
>
> RESULTS at layers [16,20,24]:
> Control (no injection): 35%
> Reasoning: hedged, balanced, moderate
>
> Bullish vector (h_bull - h_bear) injected at scale 0.4:
> Result: 75% — 40 point upward shift
> Reasoning: institutional investments, positive sentiment, strong upward
> trajectory — genuine bullish arguments, no hedging
>
> THIS IS TRUE LATENT STEERING:
> 1. 40 point probability shift (35% to 75%)
> 2. Reasoning changed to match injected stance
> 3. Stance-specific bullish arguments in output
> 4. No complement arithmetic — both report P(80k first)

**F-2. What this means in plain terms.** The system can take a mathematical vector representing "bullish" and inject it into another agent's hidden state mid-generation. The result: the other agent's probability estimate moves substantially AND its reasoning changes to match. Both directions report the same target probability, so it's not arithmetic flipping. The agent is producing stance-specific reasoning that wasn't in its prompt.

**F-3. What this does NOT mean.** Bearish injection at the same configuration breaks coherence (per `intent.md` "What we are proving next" section). The bullish pole works; the bearish pole does not. Symmetric bidirectional control is not yet proven.

**F-4. Contamination status.** Per `intent.md` "What we have proven (as of April 17, 2026)" section, this result is **Tier 2 valid** (reproducible internally). It survived the April 18 contamination audit because the test was on Mac Mini physics and did not depend on Polymarket baselines. The bearish asymmetry finding from April 17 *is* under re-audit (may be proxy contamination), but the bullish first-flight result is not.

**F-5. Relevance to surface selection.** The experiment used a Bitcoin price question as a *vehicle* for testing whether activation steering works. It did not require Polymarket data or scoring. It required: (a) a market-like question with stance options, (b) a way to measure whether reasoning actually changed. This is one data point about what the system has proven so far — informational, not dispositive.

---

## Section 5: Live Polymarket data (M-tags)

Source: `~/Projects/data/polymarket/2026-05-25.json`, pulled 4:42 AM Pacific, 93 active markets.

**M-1. Same data Round 1 used.** No fresher pull since. Distribution observations from this morning's briefing:

- Mix of macro/policy, geopolitics, AI/tech, sports, crypto, and entertainment
- 5 macro markets (Fed rates, CPI, unemployment, S&P, ethereum)
- ~35 sports markets (NBA, MLB, tennis microcontracts)
- ~12 political markets (Rubio 2028, US-Iran items, midterm seats)
- ~10 AI/tech markets (Anthropic, OpenAI, Apple-related)
- Remainder: crypto price action, entertainment, miscellaneous

**M-2. Liquidity profile.** Top-of-book liquidity heavily concentrated in election/political markets. Macro markets exist but with thin volume relative to political. Sports markets have high volume but short resolution windows (often <24h).

**M-3. Resolution-cadence profile.** Wildly heterogeneous. Some markets resolve in hours (intraday sports, crypto). Some resolve in weeks (monthly economic data). Some resolve in months (Fed decisions, election primaries). Some resolve in years (2028 presidential, long-horizon AI capability bets).

**M-4. Resolution-source profile.** Best-in-class macro markets resolve from official sources (Fed announcements, BLS releases). Sports markets resolve from game outcomes (clean). Political markets resolve from election results (clean). Some entertainment and crypto markets resolve from disputed sources or platform discretion — these are the failure-mode markets.

**M-5. Founder note on Polymarket's role per `intent.md` P-3.** Polymarket was chosen as starting validation surface because it has real-money resolution discipline. If latent agents produce alpha there, "the thesis is unassailable." The choice was not about Polymarket's surface composition. It was about the property that bets resolve in money against real adversaries.

**M-OBS-1 through M-OBS-6** (from Round 1 briefing, preserved):
- M-OBS-1: ~35 of 93 are sports/microcontracts
- M-OBS-2: Resolution cadence is wildly heterogeneous
- M-OBS-3: Macro/policy is critically sparse
- M-OBS-4: Mixed resolution timelines fail longitudinal coherence if not constrained
- M-OBS-5: The live environment in May 2026 has diverged from foundational design assumptions (which assumed denser policy/macro)
- M-OBS-6: Filtering for high-quality markets yields ~8-11 from 93 — viable but tight

---

## Section 6: Live Kalshi data — and the Gemini Round 1 error (K-tags)

Round 1 included a recommendation from Gemini to pivot Mode 1 from Polymarket to Kalshi. Gemini reasoned from Kalshi's *expected* product profile (regulated election/policy markets) rather than Kalshi's *actual* May 2026 surface. This section corrects that.

**K-1. Live pull.** `~/Projects/data/kalshi/markets_2026-05-25.json`, pulled 4:58 AM Pacific, 1,000 markets returned by API.

**K-2. Category breakdown by event-ticker prefix:**
797  KXMVESPORTSMULTIGAMEEXTENDED   (sports multi-game parlays)
202  KXMVECROSSCATEGORY              (sports parlays — samples confirmed sports)
1  KXMVENBASINGLEGAME              (NBA single-game)

**K-3. Verbatim sample of first 8 markets (subtitles, what users see):**
yes Aaron Judge: 1+,no Over 9.5 runs scored
yes Oneil Cruz: 1+,no Over 11.5 runs scored
yes James Harden: 15+,yes Jarrett Allen: 4+,yes New York wins by over...
yes Donovan Mitchell: 2+,yes James Harden: 1+,yes Jalen Brunson: 1+...
yes Jarrett Allen: 10+,yes Mikal Bridges: 15+,yes New York wins by over...
yes Donovan Mitchell: 2+,yes James Harden: 2+,yes Jalen Brunson: 2+...
yes James Harden: 2+,yes Jalen Brunson: 2+,yes Josh Hart: 1+,yes Karl-...
yes Tanner Gordon: 2+,yes Yes,no Over 8.5 runs scored

**K-4. Honest assessment.** Of 1,000 markets in the pull, zero non-sports markets surfaced in category-prefix audit. The pull may be capped at 1,000 (i.e., policy markets could exist below the cap), or 1,000 may represent the entire active surface — we have not verified which. Either way: **the May 25 Kalshi pull is 100% sports parlays.** Sports multi-game parlays are Kalshi's emphasis product as of this date.

**K-5. Implication for Round 1's Gemini recommendation.** The pivot recommendation does not survive contact with the actual Kalshi surface. The broader argument Gemini made (Polymarket-is-wrong-surface) is independent of Kalshi being the answer and remains live. But Kalshi is not the answer.

**K-6. Audit caveat.** A future audit could check whether Kalshi's authenticated API (which requires RSA signatures and is not currently configured per `state_manifest.md`) exposes a different surface. This is unverified. The 100% sports finding is for the public unauthenticated surface only.

---

## Section 7: Hard arguments worth engaging (A-tags)

Three arguments worth weighing before answering. None is dispositive. All are honest.

**A-1. The "weak language priors" argument (ChatGPT, Round 1).** If the latent thesis (T-1, T-2, T-3) is real, latent advantages should be most visible in domains where text-narrative compression is structurally weak. Prediction markets are heavily linguistically-mediated narrative-consensus pricing — by construction, possibly the worst surface for proving the latent thesis. Counter-argument: precisely because prediction markets ARE language-mediated, they are the strongest possible adversarial test. If latent agents produce edge HERE, the thesis is unambiguous.

**A-2. The experimental-identity argument (Variant A, May 24).** Variant A was chosen because immutable specific-slug registries answer the experimental-identity question (what counts as "the same benchmark instance") more cleanly than any alternative. Surfaces that don't have stable identifiers (synthetic environments, dynamically-generated questions, internal simulations) create the experimental-identity problem in a different form. If you recommend a non-Polymarket surface, your recommendation must address how experimental identity is preserved across longitudinal runs.

**A-3. The revenue-arm argument (T-5, P-3, P-4).** The project's $10M evidence threshold (P-4) is to come from "whatever channels work" — Polymarket is the starting channel, not the only channel. But the project has not yet operationalized any non-Polymarket revenue channel. If you recommend dropping Polymarket, your recommendation must briefly sketch how the project still reaches $10M without it. Acceptable answers include: enterprise governance contracts (per T-5 commercialization-agent scope), dataset licensing (NHRT moat per build_log.md §1.7), synthetic alpha funds, or "the $10M threshold itself should be re-examined."

---

## Section 8: Questions to answer

Answer all four questions. Length guidance: 2-4 paragraphs per question. Cite line tags where relevant (T-1, P-3, M-OBS-2, F-1, etc.).

**Q1. Surface recommendation.** Which of the following best fits Mode 1's role as locked in P-7 (proves divergence AND proves calibration)?

- **(i) Polymarket primary with supplements.** Variant A holds. Kalshi or other sites may supplement.
- **(ii) Hybrid surface.** OpenSpiel (per P-5) for divergence + Polymarket subset for calibration + structured non-market datasets (weather, governance, operational forecasting) for stress-testing.
- **(iii) Drop Mode 1 entirely.** Rely on calibration-tracker (Mode 2) for revenue-exploration measurement; focus longitudinal proof work on synthetic-domain OpenSpiel only. Variant A retired. (This is the parked structural alternative from Grok's May 24 afternoon3 anti-bias check, surfaced here as a first-class option.)
- **(iv) Something else.** Propose freely. Examples: weighted mix, sequential strategies, internal-simulation surface, surface-decoupled-from-revenue.

**Q2. The $10M path question (only if your Q1 answer drops or de-emphasizes Polymarket).** Per P-4, the $10M evidence threshold is to come from "whatever channels work." If your recommendation reduces Polymarket's role, briefly sketch how the project still reaches $10M. Skip this question if Q1 answer keeps Polymarket primary.

**Q3. The Variant A reconciliation question.** Variant A was locked May 24 against a choice set that did not include "no Polymarket." Does your Q1 answer retire Variant A, modify it, or leave it intact? Be specific. If your recommendation keeps Polymarket but at reduced scope, name explicitly what changes about the 8-12 immutable slug registry.

**Q4. Honest assessment of your own answer's failure mode.** Each Q1 option has a structural risk. Name yours. Examples:
- (i) risk: linguistic mediation of prediction markets may make them the wrong surface to prove latent advantages
- (ii) risk: experimental-identity problem if non-Polymarket components don't have stable longitudinal identifiers
- (iii) risk: project loses the live-adversarial-resolution discipline that made Polymarket the starting choice; also loses the path to direct-channel revenue
- (iv) risk: depends on what you propose

---

## Anti-bias self-check (please answer in your response)

Per the discipline that has worked well in prior reviews:

1. What in the briefing's framing biases toward your answer? Be specific.
2. What did the briefing not include that would have made your answer more rigorous?
3. Is there an option (v) that the briefing did not enumerate but should have?

---

## Response format guidance

- Lead with a 2-line position summary: "Q1: (X). Q2: [skip / brief sketch]. Q3: [retire / modify / intact]."
- Then the four numbered answers, one per question
- Then the three anti-bias self-check items
- Cite line tags (T-N, P-N, M-OBS-N, F-N, K-N, A-N) where relevant
- Brevity preferred over comprehensiveness. The Founder is reading three responses cold and synthesizing.

---

*End of briefing. Engines: please answer cold. Do not consult other engines' answers. Founder synthesis follows after all three responses are captured verbatim.*