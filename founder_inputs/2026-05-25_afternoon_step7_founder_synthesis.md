# Step 7 Founder synthesis — Mode 1 surface selection (Round 2)

**Date:** May 25, 2026 afternoon
**Maintainer:** John McGuire (Founder Engine), with Claude (Systems Engine)
**Status:** All six Step 7 decisions LOCKED. Founder synthesis closed.
**Cross-references:**
- `founder_inputs/2026-05-25_afternoon_handoff.md` (this morning's deferral to fresh session)
- `founder_inputs/2026-05-25_afternoon_mode1_criteria_round1_record.md` (Round 1 — criteria review)
- `founder_inputs/2026-05-25_afternoon_mode1_surface_round2_briefing.md` (Round 2 — surface review briefing, committed `badb2dd`)
- `founder_inputs/2026-05-25_afternoon_mode1_surface_round2_responses.md` (Round 2 — three engine responses verbatim, committed `a989209`)
- `founder_inputs/2026-05-24_afternoon3_end_of_session_handoff.md` (yesterday's architectural lock — Variant A)

---

## What this document is

The canonical record of the Founder's synthesis on Step 7 — six decisions that govern Mode 1's market-selection registry under the locked Variant A architecture. This document closes the synthesis loop the afternoon handoff opened this morning.

Engine inputs (Round 1 criteria + Round 2 surface) are preserved verbatim in the record files cross-referenced above. This document captures *what was decided*, *what was overridden*, and *why*. It does not re-litigate the engine arguments.

---

## The six locked decisions

### Decision 1 — Mode 1 role

**Locked: (c) — Mode 1 does both jobs.**

Mode 1's market registry must support both:
- **Useful divergence measurement** (proving that latent agents diverge from text agents in a way that maps toward truth, per T-3/T-6 in `intent.md`)
- **Outcome-based calibration** (proving the divergence is correct, per T-7)

Engine input: ChatGPT and Gemini said (b) — Mode 1 as real-world complement to OpenSpiel's divergence proof. Grok said (c) — both jobs. Founder chose (c).

Reasoning: the dual-role framing matches the build_log.md §1.4 description of the revenue-exploration arm. Mode 1 as "real-world adversarial complement only" would underweight P-3's framing of Polymarket as the validation surface where the thesis is "unassailable" if it works. (c) preserves the dual role at the cost of demanding more from the market registry.

### Decision 2 — Surface selection

**Locked: (d) Polymarket primary. Variant A holds.**

The Variant A architecture locked May 24 stands. The Mode 1 registry will hold 8 immutable Polymarket slugs/condition IDs. No hybrid surface. No sequential staging across surfaces.

Engine input: All three engines independently recommended (ii) hybrid surface — Polymarket subset + OpenSpiel + structured non-market datasets. ChatGPT and Grok independently proposed an additional fifth option (sequential staging) not enumerated in the briefing. None of the three recommended Polymarket-primary.

**This is a Founder Engine override against triple-engine convergence.** Reasoning, captured for the audit trail:

1. The project's central question per T-4 is whether useful divergent thinking is real. Real-money adversarial markets are the only test surface that produces ground-truth resolution under adversarial pressure. Made-up games (OpenSpiel) and structured non-market datasets do not have the property that someone is actively trying to make the test wrong with their own money on the line.

2. The Founder has demonstrated override discipline before. The Rain grant pressure from automated agents persisted for weeks before April 18 surfaced the contamination that would have made the grant claims indefensible. The same instinct — "wait, this isn't ready / this isn't the real test" — is operating here.

3. The engines' shared worry (experimental identity across hybrid surfaces) is real. Each engine proposed a mechanism to address it (Gemini: cryptographic hashes for non-market dataset slots; ChatGPT: immutable benchmark objects with versioned resolution logic; Grok: hybrid registry entries with versioned identifiers). None of the three mechanisms was convincing enough to overcome the unified-surface advantage Variant A provides. Polymarket-primary preserves the experimental identity solution Variant A was designed to provide.

4. The "weak language priors" argument (A-1 in the briefing) is acknowledged as a future-audit watch item (see Decision 4 below). It is not allowed to overturn the Founder's commit to adversarial real-money testing.

**What this decision does not mean:**
- It does not retire the hybrid argument permanently. If after 30 days of operating Mode 1 the four-arm benchmark produces evidence that Polymarket is structurally the wrong surface, a future review can re-open this.
- It does not block commercial conversations on the revenue-exploration arm. Per `intent.md` P-4, the $10M threshold comes from "whatever channels work." Commercial conversations are unblocked at all times; they do not require Mode 1 to be hybrid.
- It does not invalidate the engines' inputs. Their convergence is noted in this record as a structural counter-position the Founder weighed against and overrode.

### Decision 3 — Convergent criteria

**Locked: All five Round 1 convergences.**

1. Resolution clarity must dominate liquidity — binary outcomes with verifiable external resolution sources (Fed, BLS, SEC, election results)
2. Exclude sports and tennis-microcontracts (or heavily limit)
3. Crowd uncertainty band 15-80% at selection time (excludes near-certainties)
4. Resolution source must be a trusted external official source (consequence of (1), explicit for audit trail)
5. Domain mix favoring macro/policy/geopolitics/AI-tech over noise categories

Engine input: All three engines agreed on these in Round 1. No override needed.

### Decision 4 — Divergent criteria items

**Locked items:**

- **Cadence:** Strict 14-90 days (Gemini's rule). All eight markets must resolve in that window from registry-lock date. Markets resolving in <14 days are noise-dominated; markets resolving in >90 days create longitudinal-comparison problems if a v2 has to launch before they resolve.
- **Liquidity floor:** Deferred to Round 3 (specific market selection). To be decided when looking at actual candidate markets, not in the abstract.
- **"Weak language priors" criterion:** Noted as future-audit watch item. ChatGPT's argument (A-1) — that prediction markets are heavily linguistically-mediated and possibly the worst surface for proving a latent thesis — is preserved as a known structural risk. **If, after 30 days of operating Mode 1, the latent arm fails to demonstrate edge against the text arm, this argument is the first thing to re-examine before concluding the thesis is wrong.**

Engine input: Cadence and liquidity floor were Round 1 divergences. Founder picked Gemini's cadence; deferred Grok's liquidity floor. Weak-language-priors was ChatGPT-only and was the strongest single argument against Polymarket; preserved as a documented watch item.

### Decision 5 — Number of markets

**Locked: 8 markets.**

Engine input: ChatGPT and Gemini said 8; Grok said 9-10. Founder picked 8. Smaller registry easier to audit and track longitudinally; consistent with build_log.md §1.3 four-arm benchmark statistical power.

### Decision 6 — Round 2 structure (meta-decision)

**Locked: (i) Standard — all six decisions synthesized in this session.**

Briefly considered: (ii) surface-first focused review (defer Q2), (iii) hybrid (lock convergents, defer Q1/Q2). Founder elected to synthesize all six tonight rather than defer. Validity check: the Founder's gut on Decision 2 (Polymarket primary) was clear and stable; deferral would not have changed the answer.

---

## What is now unblocked

With six decisions locked, the next work surface is:

1. **Round 3 — specific market selection.** A future multi-engine review against the locked criteria. Question: which 8 specific Polymarket markets, by slug/condition ID, best fit (14-90 day cadence, 15-80% crowd uncertainty, macro/policy/geopolitics/AI-tech domain, trusted external resolution source, exclude sports)?

2. **`benchmark_registry_v1.json` construction.** Once Round 3 closes with 8 specific slugs, write the registry file at `experiments/benchmark/benchmark_registry_v1.json` per the path proposed in the May 24 afternoon3 handoff.

3. **Loader logic.** Write the script that reads the registry, queries Polymarket for current state per slug, produces a hard-fail-visible structure (no silent 0.5 — per May 24 afternoon3 architectural lock).

4. **text-swarm rebuild against Mode 1.** Conditional on Mode 1 being deterministic per May 24 afternoon3 architectural lock. text-swarm restoration prerequisites 1-3 (matching contract, swarm architecture, audit-trail design) become re-evaluable once Mode 1 produces stable output.

---

## What is now closed (not to be re-opened lightly)

The Founder's override on Decision 2 was made cold, with three-engine input on record. The override is allowed under the operating model (Founder Engine has final authority per `intent.md`). It is not a license to re-open Decision 2 on cognitive doubt in a future session.

The legitimate triggers for re-opening Decision 2:

- After 30+ days of operating Mode 1 v1, the latent arm fails to demonstrate edge against the text arm
- The "weak language priors" worry materializes in a measurable way (latent arm wins on non-prediction-market tasks but underperforms on Polymarket)
- A structural reason emerges that Polymarket cannot serve the dual role locked in Decision 1
- Polymarket itself becomes unavailable or structurally degrades (regulatory action, surface composition shifts further)

Founder cognitive doubt about the override decision is **not** a legitimate trigger.

---

## Reproducer summary

| Claim | Reproducer |
|---|---|
| Six decisions locked | This file's "Six locked decisions" section |
| Variant A architecture remains in force | `founder_inputs/2026-05-24_afternoon3_end_of_session_handoff.md` "The architectural direction (now locked)" section |
| Round 1 convergent criteria | `founder_inputs/2026-05-25_afternoon_mode1_criteria_round1_record.md` Part 6 |
| Round 2 engine responses (verbatim) | `founder_inputs/2026-05-25_afternoon_mode1_surface_round2_responses.md`, committed `a989209` |
| Round 2 briefing (verbatim, pre-send) | `founder_inputs/2026-05-25_afternoon_mode1_surface_round2_briefing.md`, committed `badb2dd` |
| $10M threshold framing | `docs/intent.md` "The Primary Strategic Bet" + "The proof architecture" sections |
| Founder override authority | `docs/intent.md` "How this project works" section |

---

**Edit log:**
- 2026-05-26 (fresh session, John + Claude): Precision correction to Decision 2 reason #3. Original wording ("engines could not propose a clean solution") understated what the engines wrote. Replaced with wording that names each engine's proposed mechanism and the actual reason for the override (mechanisms not convincing enough to overcome unified-surface advantage). The override itself is unchanged.

*End of synthesis. Step 7 closed. Round 3 (specific market selection) blocked on this synthesis being committed.*