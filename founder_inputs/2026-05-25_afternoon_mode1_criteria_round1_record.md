# Round 1 multi-engine record — Mode 1 market-selection criteria

**Date:** May 25, 2026 afternoon
**Maintainer:** John McGuire (Founder Engine), with Claude (Systems Engine)
**Status:** Three engine responses captured verbatim. THREE-WAY COMPARISON CAPTURED. FOUNDER SYNTHESIS PENDING — DEFERRED TO FRESH SESSION.
**Cross-reference:** `founder_inputs/2026-05-25_afternoon_handoff.md` (the handoff that explains where this fits and what the next session should do); `founder_inputs/2026-05-24_afternoon3_engine_responses.md` (the architectural review that locked the Variant A registry mechanism this work selects markets for); `founder_inputs/2026-05-25_morning_engine_responses.md` (the morning elevation review).

---

## Purpose of this record

This file is the canonical record of Round 1 of the Step 7 multi-engine review on **what criteria should govern Mode 1's 8-12 market registry under Variant A**. Round 1 asked the three engines to propose *criteria*, not specific markets. Round 2 (a future session) was scoped to apply locked criteria to pick specific markets.

The review surfaced a finding that exceeds the original scope: **2 of 3 engines concluded Polymarket may not be the right surface for Mode 1 at all.** This finding made the Founder synthesis materially more consequential than originally framed. The Founder chose to defer synthesis to a fresh session rather than synthesize at the end of a long working day.

This file captures: the briefing, three engine responses verbatim, three-way comparison, convergences, divergences, discipline observations. The Founder synthesis is intentionally absent. The handoff file points the next session to this record.

---

## Source quality notes

- Briefing was constructed by Founder + Systems Engine over ~90 minutes in afternoon session, embedding live Polymarket data from May 25 04:42 pull (93 markets). Briefing is at `founder_inputs/2026-05-25_afternoon_mode1_criteria_briefing.md` (committed in same commit as this file).
- All three responses pasted from chat sessions. Direct paste, no transcription, no truncation.
- Same multi-engine discipline as the morning elevation review: Founder preferences and Systems Engine recommendations withheld, all three engines responded cold.

---

# Part 1: The briefing in summary

Question to engines: **What criteria should LatentForge use to select the 8-12 Polymarket markets that anchor Mode 1 — OR — should Polymarket be the surface for Mode 1 at all?**

Briefing structure: Part 1 thesis (T-N tags), Part 2 proof architecture (P-N tags), Part 3 $10M revenue threshold (R-N tags), Part 4 live Polymarket data (M-N tags including 93-market table), Part 5 five sub-questions, Part 6 anti-bias check, Part 7 response format.

Key framings:
- Polymarket-may-not-be-the-right-surface made a first-class option, not buried
- "Useful divergence" defined explicitly as divergence-toward-truth, not divergence-from-crowd (T-6, T-7)
- $10M threshold framed as agnostic to commercial path (R-6 through R-8): criteria must hold open both "Polymarket is the commercial proving ground" AND "Mode 1 is diagnostic-only and $10M comes from elsewhere"
- Open question on Mode 1 role surfaced (P-7): (a) primary divergence instrument, (b) real-world adversarial complement to OpenSpiel, (c) both, (d) something else

Sub-questions:
- Q1: Mode 1 role per P-7
- Q2: Is Polymarket right surface at all? If no, alternative
- Q3: Criteria shape (3-7 dimensions)
- Q4: Number of markets (closer to 8, 12, or specific)
- Q5: Failure mode if criteria applied to today's surface

---

# Part 2: ChatGPT response (verbatim)

**Position summary:** Q1 (b); Q2 not sufficient as sole surface, hybrid proposed; Q3 six criterion shapes; Q4 closer to 8; Q5 liquidity-driven noise + pooling-heterogeneous-domains failure modes.

**Q1: (b) real-world adversarial complement to OpenSpiel, with secondary calibration role.** OpenSpiel is the synthetic-domain instrument for divergence (P-6); forcing Mode 1 markets to measure abstract geometric divergence re-introduces the shadow_match failure mode (T-6, T-7).

**Q2: Polymarket probably NOT sufficient as sole Mode 1 surface, but useful as one component.** The live surface is dominated by noisy, short-horizon, heterogeneous contracts poorly suited for clean latent-vs-text divergence analysis. Proposed hybrid surface:
- OpenSpiel → divergence measurement
- Polymarket/Kalshi subset → calibration and adversarial grounding
- Structured non-market datasets (weather anomalies, operational forecasting, governance datasets, synthetic hidden-pattern environments) → latent reasoning stress tests

**Q3: Six criterion shapes** (priorities, not canonical text):
1. Resolution clarity must dominate liquidity — binary, externally verifiable, mechanically resolvable outcomes outrank market size (T-6, T-7)
2. Moderate uncertainty band — near-certainties (0.99/0.01) contain little informational entropy; coin-flip microcontracts measure randomness not insight; useful zone is "uncertain but structurally modellable" (P-9)
3. Mixed but bounded resolution cadence — wildly heterogeneous timelines fail the benchmark coherence (M-OBS-4)
4. Domains where language priors are weaker — if latent thesis is real, strongest signal emerges where textual narrative compression performs poorly (T-3)
5. Registry stability over optimality — longitudinal comparability matters more than chasing best current markets (P-3, P-4)
6. Separation between benchmark value and commercial value — preserve optionality (R-6 through R-8)

**Q4: Closer to 8 than 12.** Heterogeneity and weakness of live surface mean adding markets adds variance not robustness. Smaller registry is easier to audit and track longitudinally.

**Q5: Two failure modes.** (a) Liquidity-driven criteria push toward sports/crypto noise; (b) pooling heterogeneous domains under one benchmark score collapses distinct capabilities (sports microcontracts = microstatistical edge; geopolitics = interpretation; macro = structural forecasting; weather = physical systems).

**Anti-bias observations:** Volume of Part 4 anchors toward Polymarket-must-matter. Q2 and Q3 partially overlap. Commercial-vs-scientific axis deserves its own standalone question. Source insufficiency on actual latent-agent outputs — engines reasoning about benchmark surface without empirical evidence of what the system has actually done.

**Overall assessment:** Project risks conflating three different things — divergence science, calibration benchmarking, commercial alpha discovery. Registry becomes much cleaner if explicitly treated as calibration and adversarial-grounding instrument rather than canonical proof of latent cognition. Polymarket valuable for pressure-testing but current live surface does not structurally support carrying the entire thesis alone.

---

# Part 3: Gemini response (verbatim)

**Position summary:** Q1 (b); Q2 NO, pivot to Kalshi or PredictIt; Q3 four axes; Q4 exactly 8; Q5 "Surface Starvation."

**Q1: (b) real-world adversarial complement to OpenSpiel.** OpenSpiel measures geometric divergence (T-5, P-6); markets must test ground-truth calibration under adversarial pressure (R-3), satisfying outcome-based scoring (T-7) without recreating shadow_match failure.

**Q2: NO — Polymarket is the wrong primary surface for Mode 1.** Pivot Mode 1 registry to **Kalshi or PredictIt**. Use Polymarket exclusively as downstream execution target for revenue-exploration arm. Reasoning: ~35 of 93 markets are sports/microcontracts (M-OBS-1) offering no novel reasoning room; macro/policy is critically sparse with low liquidity (M-OBS-3, M-OBS-6); non-crypto regulated platforms (like Kalshi) offer cleaner systematically structured macro/climate/regulatory/demographic data matrices for multi-arm benchmark testing.

**FLAG FOR FUTURE SESSION:** Gemini's Kalshi recommendation rests on a reasoning error. Per F-4 in the morning briefing (and in `state_manifest.md`), the Kalshi May 24 pull was ~1,000 markets, 100% sports. Gemini reasoned from Kalshi's *expected* product profile (regulated election/policy markets) rather than its *actual* current data. The pivot recommendation may not survive contact with the live Kalshi surface. Gemini's broader argument (Polymarket-is-wrong-surface) does NOT depend on Kalshi being the answer, so the contamination is bounded to one option.

**Q3: Four axes** (priorities, not canonical text):
1. Informational High-Dimensionality (Domain Filter) — excludes all sports, microcontracts, simple momentum tracking. Markets must require synthesis of heterogeneous data inputs
2. Mid-Horizon Resolution Cadence — strict bound 14-90 days, excludes hyper-short noise and multi-year horizons
3. Non-Trivial Crowd Uncertainty (Entropy Range) — implied probability 20-80% at registry lock
4. Unambiguous Verifiable Resolution (Audit Lock) — deterministic non-custodial or hard agency-reported resolution source (BLS, Fed, SEC); insulates Shadow Self layer from semantic legal parsing or platform-arbitrary resolution disputes

**Q4: Exactly 8 markets.** Compute parity constraints (P-2) and four-arm matrix (P-1, P-3) mean 8 hyper-curated questions maximize signal-to-noise. Expanding to 12 under sparse macro distribution would dilute quality.

**Q5: Surface Starvation.** Applying criteria cleanly: information-high-dimensionality filter eliminates 35+ sports markets; mid-horizon cadence excludes Rubio 2028; remaining macro/policy/AI surface is critically starved (only 5 macro markets, several fail timescale or entropy constraints). Live Polymarket utterly fails to support rigorous criteria. Validates M-OBS-5 — the live environment in May 2026 has diverged entirely from the foundational design assumptions.

**Anti-bias observations:** Briefing implies Mode 1 must be anchored by a single platform — a synthetic, aggregated index surface blending Kalshi + Polymarket + custom internal simulation feeds is a viable alternative not enumerated. "Small real-money bets" anchors toward programmatic order execution. Source insufficient on order-book depth and historical volume stability. Q2/Q3 overlap — better decomposed as singular "Surface Suitability & Structural Criteria Matrix."

---

# Part 4: Grok response (verbatim)

**Position summary:** Q1 (c) BOTH; Q2 yes Polymarket primary with supplements; Q3 5-6 dimensions; Q4 closer to 9-10; Q5 manageable compromises.

**Q1: (c) both — markets must support both divergence and calibration measurement.** P-6 positions markets as adversarial complement but T-6/T-7 and P-9 require outcome-based scoring for *useful* divergence; P-8 demands novel-solutions distinguishability. Pure (b) underweights the four-arm isolation (P-1 through P-4) and makes OpenSpiel carry too much divergence load; pure (a) risks shadow_match failure at scale (T-7).

**Q2: Yes, Polymarket is the right primary surface for now, with explicit supplementation path.** R-3 names it the starting hard-adversarial environment with real-money resolution discipline that synthetic alternatives lack. Live surface (M-OBS-1 through M-OBS-6) provides enough resolved outcomes despite skews. Kalshi or Manifold could supplement for cleaner macro/policy. Polymarket's liquidity and volume make it pragmatic anchor. Holds all R-7 paths open better than locking to one platform.

**Q3: 5-6 dimensions:**
- High-priority: strong binary resolvability + verifiable source; implied probability 15-80% at selection time
- Medium-high: mixed resolution cadences (max 30% ultra-short <1 week; include some 1+ year horizons); liquidity floor ~$8K-$15K
- Medium: domain balance favoring geopolitics/macro/AI-tech/equities (limit pure sports/microcontracts to ≤25%); explicit commercial neutrality (no forced paper-trade scalability but flag candidates)
- Cross-cutting: support for post-resolution comparison of latent vs text reasoning traces for novelty

**Q4: Closer to 9-10.** Balances statistical power across 4 arms (P-3) and coverage of timescale/domain mix without forcing too many marginal markets from current surface (M-OBS-6). 8 risks insufficient diversity for P-9 novelty detection; 12+ would dilute quality.

**Q5: Surface supports with clear but manageable compromises.** Filters would yield ~8-11 viable markets (Rubio 2028, several Iran/US-Iran items, Fed rate markets, Anthropic/equities, select longer sports) from 93. Failure modes: over-weighting short-horizon or sports if liquidity is over-prioritized; sparse deep macro forcing shorter average cadence than ideal. Compromises acceptable for V0.1 but criteria must explicitly weight diagnostic value (T-6, P-9) over raw liquidity.

**Anti-bias observations:** Heavy embedding of Polymarket data and R-3 phrasing mildly anchors toward using it rather than fully exploring non-market surfaces. No major framing rules out hybrid diagnostic role. Embedded sources largely sufficient; additional data on historical Polymarket resolution accuracy rates or current Kalshi liquidity in macro would help refine timescale/domain trade-offs. Five questions well decomposed.

**Overall assessment:** Criteria make Mode 1 a strong dual-purpose surface (calibration + divergence signal) while preserving optionality for commercial paths identified by agents themselves. Polymarket works as anchor but should be monitored for replacement if liquidity patterns remain too sports/crypto-heavy.

---

# Part 5: Three-way comparison

| Question | ChatGPT | Gemini | Grok | Status |
|---|---|---|---|---|
| Q1: Mode 1 role | (b) real-world complement | (b) real-world complement | (c) both | **SPLIT 2-1: (b) vs (c)** |
| Q2: Polymarket as surface | NOT sufficient alone, hybrid (OpenSpiel + Polymarket subset + structured non-market datasets) | NO, pivot to Kalshi/PredictIt (but Kalshi is sports-dominated per F-4) | YES with supplements (Kalshi/Manifold) | **SPLIT 2-1 AGAINST Polymarket-primary** |
| Q3: Criteria shape | 6 shapes inc. "weak language priors" | 4 axes inc. 14-90 day cadence + verifiable sources | 5-6 dims with $8-15K liquidity floor + mixed cadence | **CONVERGENT on: resolution clarity, uncertainty band, exclude sports, verifiable sources. DIVERGENT on: cadence specifics, liquidity floor, weak language priors** |
| Q4: Number | ~8 | exactly 8 | 9-10 | **CONVERGENT 8-10, weighted toward 8** |
| Q5: Failure mode | Liquidity drives noise + heterogeneous pooling collapses metrics | "Surface Starvation" | Manageable compromises | **SPLIT 2-1: structural problem vs manageable** |

# Part 6: Three-engine convergences (READY FOR FOUNDER LOCK)

**Five substantive agreements survived independent review.** Future session can lock these:

1. **Number closer to 8 than 12.** All three converge tight, 8-10. Gemini and ChatGPT both 8; Grok 9-10.

2. **Domain filter required.** Exclude sports and tennis-microcontracts (or heavily limit). Sports markets don't surface useful divergence in T-3 / T-6 sense.

3. **Resolution clarity must dominate liquidity.** Binary outcomes with verifiable external resolution sources (Fed, BLS, SEC, election results) outrank market depth. Protects against shadow_match failure mode (T-7).

4. **Crowd uncertainty band 15-80%.** All three converge roughly. ChatGPT "moderate," Gemini 20-80%, Grok 15-80%. Excludes near-certainties where novel solutions cannot surface (P-9).

5. **Five briefing-design observations** (none requires Founder lock, but should inform Round 2 briefing): (a) Polymarket-anchoring bias in volume of Part 4; (b) Q2/Q3 should be merged into single "surface suitability + criteria matrix" question; (c) commercial-vs-scientific axis deserves standalone question; (d) source insufficient on actual latent-agent outputs to date; (e) source insufficient on order-book depth and historical resolution accuracy data.

# Part 7: Three-engine divergences (REQUIRE FOUNDER DECISION)

**Q1: Mode 1 role — (b) vs (c).** Real architectural disagreement. Engines reasoned to different sides of a tension in the project's stated architecture (P-3 vs P-6). Founder must decide which side of that tension is canonical.

**Q2: Polymarket as the surface.** 2-1 against Polymarket-primary. Three different paths proposed:
- (i) Grok: Polymarket primary with supplements
- (ii) ChatGPT: hybrid (OpenSpiel + Polymarket subset + structured non-market datasets)
- (iii) Gemini: pivot to Kalshi/PredictIt — BUT Gemini's reasoning error: Kalshi is 100% sports per F-4, not the regulated macro platform Gemini imagined

This decision is the biggest single decision in Step 7. May warrant its own focused multi-engine review with both Polymarket AND Kalshi live data shown side-by-side, before locking.

**Q3 divergent items:**
- **Cadence:** Gemini strict 14-90d; ChatGPT bounded but unspecified; Grok mixed with caps on ultra-short
- **Liquidity floor:** Only Grok specified ($8-15K); others kept liquidity below-priority
- **"Weak language priors" criterion (ChatGPT only):** structurally strongest argument — if latent thesis is real, latent advantages should be most visible where text-narrative compression is weak. Polymarket markets are heavily linguistically-mediated narrative consensus pricing — by construction, possibly the worst surface for proving the latent thesis. Not surfaced by Gemini or Grok.

**Q4 number:** Lock 8, lock range 8-10, or other.

# Part 8: Discipline observations

## What worked

- **Cold-response discipline held.** Founder preferences and Systems Engine recommendations withheld; all three engines reasoned against the same starting evidence. The 2-1 splits are real disagreement, not framing artifacts.
- **The afternoon3 "critique-a-synthesis" pattern fired for the third time this week.** Multi-engine review caught a structural finding (Polymarket may be wrong surface) that the briefing did not pre-anchor toward. Three data points: architectural critique (afternoon3), elevation review (this morning), criteria review (this afternoon). The pattern is now at the threshold for light formalization that the morning elevation review record noted.
- **Hallucination resistance held under more difficult conditions.** Briefing was more generative than prior briefings (engines proposed criteria rather than evaluating fixed options). All three engines cited line tags correctly; no invented evidence. Gemini's Kalshi error is a reasoning error from outdated prior, not a hallucination.
- **Anti-bias check produced substantive observations from all three.** All three independently flagged Polymarket-anchoring bias. ChatGPT and Gemini both flagged Q2/Q3 overlap. ChatGPT and Gemini both flagged commercial-vs-scientific decomposition. Convergence on bias observations is a strong signal that the observations are real, not artifacts of any one engine's positioning.

## What did not work as well

- **The briefing's framing anchored more than intended toward Polymarket-must-be-the-surface.** All three engines flagged this. The "Polymarket may not be the right surface" framing in note 6 was insufficient against the volume of Part 4. Future briefings on surface selection should embed alternatives in equal detail.
- **The briefing's Q2/Q3 decomposition forced a binary pivot before criteria defined.** Should be a single "surface suitability + criteria matrix" question. ChatGPT and Gemini both flagged.
- **Source insufficiency on latent-agent empirical outputs.** Both ChatGPT and Grok independently flagged this — the engines are being asked to design a benchmark surface without seeing what the system has actually done so far. For Round 2 (specific markets) or for any surface-selection review, the briefing should include actual latent-agent reasoning traces or output samples if available.

## Carry-forward for the next session

1. **Founder synthesis on the six Step 7 decisions is the next action.** This file captures the engine inputs; the handoff file (`2026-05-25_afternoon_handoff.md`) captures what to do.
2. **The Polymarket-may-be-wrong-surface finding may warrant its own focused multi-engine review.** Three options: (a) Founder synthesizes on existing inputs and locks a path; (b) fresh session runs a second review specifically on surface selection with live Polymarket + Kalshi + alternative data side-by-side; (c) Founder partially locks (convergent items + number) and defers Q1/Q2 to a focused future review.
3. **Briefing-design lessons for the next surface review:** Embed alternatives in equal detail. Merge Q2/Q3. Make commercial-vs-scientific its own question. If possible, embed actual latent-agent outputs to date.

---

*End of record. Round 1 complete. Founder synthesis pending. Round 2 (specific markets) blocked on Round 1 synthesis.*
