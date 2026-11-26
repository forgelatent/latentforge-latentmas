# Useful divergence — scoring rule, CANDIDATE v0.4 (November 26, 2026)

**Status:** CANDIDATE. Drafted by the Systems Engine from v0.3 (`founder_inputs/2026-10-26_useful_divergence_scoring_rule_v0.3_CANDIDATE.md`, commit `a6c2de8`) by applying four edit lists and nothing else: cold round 5 synthesis §6 (`founder_inputs/2026-10-28_cold_round5_synthesis.md`), cold round 6 synthesis §3, cold round 7 synthesis §5 (both `founder_inputs/2026-11-03_*`), and cold round 8 synthesis §5 (`founder_inputs/2026-11-26_cold_round8_synthesis.md`), plus the Founder's value for m (decision note item 10, commit `54c1bf3`). Supersedes v0.3 only once the Founder approves. Tier 3. Nothing here is implemented; no arm has run; no model is chosen. Changes from v0.3 are marked **[v0.4]**; the change log is section 12. Where an edit list named a requirement without fixing its content, the slot is marked **[v0.4, to write]** and listed in section 11; nothing was filled in by the drafter. No group or block count appears in this file.

**Decisions carried.** From October 25 (decision note item 9): the outcome group is the independent unit with equal weight; J_human ≥ 0.80; review-list order under the written contract. From the round 5 synthesis's six decisions: (1) the Step 0b lists are a draft, saved not accepted; (2) design v3 Step 5 is reopened before Step 1: one main driver tag per event for block formation; (3) the Iran driver is split in two; (4) "survives" means the sensitivity interval is entirely above m, and both gates must hold under both resamplings (cold round 6, 4 of 4); (5) the divergence secondary endpoint is dropped (cold round 7; Founder); (6) m is a governance number fixed before any arm runs (cold round 8, 2 of 2), and the Founder chose m = 0.01 on November 26, 2026. **This rule depends on two documents not yet written:** the design v3 amendment for decision 2, and the Step 0b lists CANDIDATE v2.

## 1. The claim this rule scores
**[v0.4]** Given the same information, do agents communicating in latent states forecast real resolved events better than the same agents communicating in text? How the gain is distributed across levels of disagreement between the two arms is reported, not claimed. (v0.3's second half, "and is the gain concentrated where the two disagree?", is removed: cold round 7, 3 of 3, found that no version of this test can answer it.)

## 2. The data and the units
- Data: `scratch/pool_resolutions_2026-10-25.json`: 410 resolved markets (81 YES, 329 NO). The file holds 292 events; 291 carry resolved markets and one (the Sweden PM pair) carries only STILL_OPEN markets and is never in the confirmatory sample.
- **Market:** one Polymarket question with a YES/NO settlement.
- **Event:** the API's grouping of markets. Per-event scores are computed (section 7) but the event is not the unit of weight.
- **Outcome group (primary group):** a pre-declared dependence block, as defined in design v3: events linked by clause (a) same proceeding, office, legal action, instrument or event instance; (b) one resolution restricts the other's valid outcomes; or (c) the same named measurement or process over overlapping outcome windows read from the resolution conditions. Groups are the connected components of accepted links. Different group ids do not establish independence. The outcome group is the unit of resampling and the unit of primary weight.
- **[v0.4] Sensitivity block:** the connected components of "same primary group OR same main driver tag", where each event carries at most one main driver tag for block formation (decision 2); any other driver tags on an event are recorded and never link. **`none` is the empty tag set and links nothing.** Used only to recompute uncertainty (section 7); never a unit of weight. The exact block-formation rule is the design v3 amendment's to state; this rule follows it.

## 3. Dependence grouping — governed by design v3 as amended, not restated here
Unchanged from v0.3 except as marked. What this rule depends on:
- The fixed lists of Step 0b are committed and hashed with the pool hash before Step 1 and never change after Step 1 starts. **[v0.4]** The lists are currently a draft (decision 1); Step 1 cannot start until a lists file is accepted by the Founder in words.
- Two blind partitions (Founder; one cold engine session, vendor and model recorded), neither reader shown any count or any outcome; J_human ≥ 0.80 or the step fails; disagreements adjudicated with evidence; unsettled events become unresolved; no default merge, no default split, no third reader.
- Unresolved events and their markets are removed before the freeze. The groups file is committed and hashed; its hash goes into the pre-registration. Only after the freeze is anything counted.
- Both minima are tested on the retained sample after exclusions: at least 250 markets and at least 150 primary groups.
- The `series` and `parentEventId` fields are candidate signals only; under Pattern G every API field is evidence, not definition.
- A grouping step that fails (v3 Fail conditions) stops the project before any forecast; it is not a run outcome under section 8.

## 4. The arms (all use the same model checkpoint and the same prompt text)
- **T (text):** agent A reads the question and writes a draft forecast with reasoning; agent B receives the question plus A's full draft as text and states a probability.
- **L (latent):** identical, except B receives A's draft as latent states instead of text. The draft is the same draft.
- **D (deranged control):** identical to L, except B receives the latent states of a donor draft. B's own input is unchanged. This substitution is the one permitted exception to section 5. **[v0.4] The donor rule (cold round 5):**
  - The donor draft is one written by agent A for a market in a **different primary group and a different sensitivity block** (3 of 3 readers).
  - The donor bank is the confirmatory pool only; never an excluded or open market.
  - Assignment is by a seeded deterministic rule fixed at pre-registration, either a permutation without reuse or with a stated cap on donor reuse **[v0.4, to write: which]**.
  - A fallback for a recipient with no qualifying donor is written before any forecast **[v0.4, to write]**. Feasibility statement: if one sensitivity block holds more than half the eligible drafts, a one-use cross-block assignment is impossible and the fallback applies.
  - Draft length is made **uninformative, not matched**: by a fixed generation length in the budget rule, or by padding and truncation **[v0.4, to write: which; depends on the budget rule]**. Donors are never matched on length, and never chosen using outcomes, receiver results, any arm's output on the target market, or observed gate performance.
  - The pre-registration states how inference handles donor-source dependence: conditioning on one fixed donor bank and assignment, or averaging over pre-registered assignments **[v0.4, to write: which]**. The recipient-block bootstrap alone does not cover it.
- **S (single):** agent B alone, no message. The floor.
- **BR (base rate):** **[v0.4]** the leave-one-group-out base rate under the primary weights. For the group being scored, take every other group; for each, average its events' YES fractions (an event's YES fraction is the share of its markets that resolved YES); then average those group rates equally. That one number is BR's forecast for every market in the scored group. (v0.3's "pool's YES rate" was ambiguous and could be read as the pooled market fraction.)
- **C (crowd):** the last saved Polymarket price before resolution. Recorded and reported; never shown to any agent; not a target.

## 5. Information rule
Unchanged from v0.3: every arm gets question text, description, outcome names, and a "forecast as of" date; no arm gets any price, web access, other market, or the resolution date. Identical for T, L, D, S, with the registered D exception. Different information between arms voids the comparison.

Markets of the same event share one "forecast as of" date. Proposed: the latest first-seen date among the event's markets. This is a collection date and is deliberately not the outcome window of design v3. Still open for Founder approval (section 11).

## 6. Leakage rule
Unchanged from v0.3: the model's training cutoff must be earlier than every market's "forecast as of" date; markets first seen before the cutoff are excluded before any run, listed with the cutoff and its source. Eligible markets, events and groups are counted and recorded under each candidate cutoff before any model is chosen. Leakage exclusions follow v3 Step 6: every surviving event keeps its frozen group id and driver tags; empty groups are dropped; both minima are re-checked; a surviving group is never split because a bridging event was removed.

## 7. Scores
- Per market: Brier = (p − y)², y in {0, 1}. Binary, per market, on the frozen list. No sum-to-1 constraint across slices; the market list, outcome definitions and weights are frozen before forecasts.
- Per event: mean Brier over its markets (each market weight 1 within its event).
- Per group: mean of its events' per-event Brier (each event weight 1 within its group). Each group has weight 1 in every arm-level score and in the primary endpoint.
- Per arm: mean over groups of the per-group Brier.
- **Primary endpoint:** paired difference per group, d_g = Brier_T(g) − Brier_L(g). Positive favors latent. Report the mean of d_g over groups with a 95% bootstrap interval; the bootstrap resamples primary groups (10,000 resamples, with replacement, equal probability per group).
- **Reported beside it, never in place of it:** the per-event form, mean over events of d_e = Brier_T(e) − Brier_L(e), with its own interval from resampling groups. A companion result; never an endpoint and never a second chance to PASS.
- **[v0.4] Sensitivity recomputation, written out (cold round 5).** The statistic is unchanged; only the resampling unit changes. Let K be the number of retained sensitivity blocks, n_b the number of primary groups in block b, and S_b the sum of d_g over the groups in block b. The point estimate is Δ = Σ S_b ÷ Σ n_b, which is the primary point estimate by definition. Each replicate draws exactly K blocks uniformly with replacement; with c_b the number of times block b is drawn, the replicate's value is Δ* = Σ c_b S_b ÷ Σ c_b n_b. 10,000 replicates; 95% interval. Block means are never averaged equally (that would change the weights). **The reported sensitivity point estimate is Δ; the mean of the bootstrap replicates never replaces it.**
- **[v0.4] Admissibility.** If fewer than two sensitivity blocks are retained, or the resampling distribution is degenerate (zero width), the result is "sensitivity inference not established" and a completed run is a FAIL, never a PASS and never a VOID. Reported beside the block count as a diagnostic: B_eff = (Σ n_b)² ÷ Σ n_b². No numerical minimum for K or B_eff is set; no reader could support one (section 11).
- Also reported: the primary endpoint on the subset of groups containing at least one YES-resolved market (the NO-skew check), with a group bootstrap.
- **[v0.4] Gates (both required; each evaluated with 95% intervals under both primary-group and sensitivity-block resampling; Brier, not accuracy):**
  - **Gate 1, pairing:** mean over groups of Brier_D(g) − Brier_L(g) > 0. If not met: "no positive task-relevant pairing effect was established."
  - **Gate 2, usefulness:** mean over groups of Brier_S(g) − Brier_L(g) > 0. If not met: "no advantage over a single agent was established."
  - **A gate counts as met only if its 95% interval lies entirely above zero under both primary-group resampling and sensitivity-block resampling** (cold round 6, 4 of 4). The same block draws are used for all contrasts within a replicate.
- **"Beats"** means the 95% group-bootstrap interval of the difference excludes zero in the favorable direction.
- **[v0.4] Disagreement reporting (descriptive only; replaces v0.3's divergence threshold and secondary endpoint; cold round 7).** For every market, record |p_L − p_T|, the paired Brier difference Brier_T − Brier_L, and whether L is closer to the realized outcome than T. Report the unconditional distribution of |p_L − p_T| across markets and groups; the decomposition of the primary group-weighted Brier gain across disagreement deciles and above a descriptive reference line of |p_L − p_T| ≥ 0.10, with the count of markets and groups above the line; both resampling intervals where any interval is shown. No secondary pass/fail gate; nothing here alters the PASS/FAIL outcome of the primary endpoint or the gates. The 0.10 line is a reading aid with no evidential basis.
- Also reported, never endpoints: mean Brier for L, T, S, BR, C per group and per event; calibration curves for L and T; the group-size distribution, the number of groups with two or more events, the largest group's share of events and of weight under both weightings, and the sensitivity-block count beside the primary group count (v3, Step 4).

## 8. Pass, fail, void, early stop
- **[v0.4] Pass:** primary-endpoint interval entirely above the pre-registered margin m under both primary-group and sensitivity-block resampling, AND Gate 1 and Gate 2 each met as defined in §7, AND L beats BR.
- **Fail:** a valid run that does not pass. FAIL means "did not establish the required advantage," not "the advantage is absent." A missed Gate 1 is the decision note's early stop for any further latent work.
- **[v0.4] The labelled FAIL (cold round 6):** "The primary-group interval establishes an improvement exceeding the pre-registered margin. The sensitivity-block interval establishes a positive improvement but does not establish that the improvement exceeds that margin. Result: FAIL — the required advantage was not established under the registered sensitivity analysis." The report shows the common point estimate and both intervals. This licenses: positive superiority under both resampling schemes, and margin-exceeding superiority under primary groups. It does not license the decision note's sentence.
- **[v0.4]** "Sensitivity inference not established" in a completed run (section 7, Admissibility) is a FAIL, not a VOID.
- **[v0.4]** No descriptive or secondary result ever rescues a primary FAIL.
- **Void:** only for execution or protocol failure: the information rule broken; the budget rule not satisfied; the market list, the groups file, the driver tags or any Step 0b list changed after the freeze; any group or candidate count shown to a reader during Step 3; the run incomplete. Void means the test did not happen; it may be rerun once the failure is fixed, under the same rule and the same frozen grouping. **[v0.4]** "Incomplete" means incomplete under completion, retry and abort rules that are written into the pre-registration before any arm runs **[v0.4, to write]**, so that an unfavourable partial run cannot be turned into a VOID afterwards.
- **Early stop (before any forecast):** the grouping step fails under v3's Fail conditions. This is the decision note's §5 stop, not a run outcome, and none of its causes may be cured by splitting, re-defining, re-including, adding a reader, or re-running with a count visible. **[v0.4]** No T, L, D or S forecast is made after a grouping fail; one made anyway is outside this rule and supports no claim.
Pass is necessary, not sufficient, for any external claim.

## 9. Margin
**[v0.4] Replaces v0.3 §9 in full (cold round 8; decision note item 10).** m is an absolute reduction in group-averaged Brier under §7's definition. The Founder fixed m at **0.01** on November 26, 2026, before any arm (S, T, L, D) ran and before BR or C was scored on the frozen pool, and signed: *"I choose m = 0.01 Brier units as the smallest improvement worth claiming. This is my governance judgment, not a value derived from any arm's result, from the pool's outcomes, or from Draft-KV's accuracy gains."* No arm result, baseline score or noise estimate may change m afterwards; a run whose primary interval clears zero but not m is a FAIL under §8. S and BR are baseline and feasibility checks only; the S − BR spread is not a noise estimate for T − L and carries no power claim. No calibration slice; the full eligible pool is the confirmatory set. Whether the experiment has enough power to detect an effect of this size is not established by anything in this rule.

## 10. What this rule does not reward
Being different from the crowd. Being different from text. Beating the crowd. Being confident. Any of these alone is "horse territory" by the motor-car tests.

## 11. Open, and to write before pre-registration
Closed since v0.3: delta and the divergence endpoint (decision 5); gates under sensitivity and the meaning of "survives" (decision 4); the donor's block constraint (round 5); how m is fixed and its value (decision 6; item 10).

Still open, each needing a Founder decision or a written text; none was decided by the drafter:
1. Shared "forecast as of" date for an event's markets: latest first-seen (proposed) or earliest.
2. Donor rule slots (§4): permutation without reuse or a stated reuse cap; the fallback text; how length is made uninformative; how inference handles donor-source dependence.
3. Completion, retry and abort rules (§8).
4. The interval construction to freeze (the edit lists say "95% bootstrap interval" and "freeze the interval construction" without naming the type), and whether any numerical minimum on blocks is wanted (§7; no reader supported a number).
5. Whether "L beats BR" must hold under sensitivity resampling as well as primary. Round 6 decided this for the primary endpoint and both gates; no round asked it for BR.
6. The budget rule (how compute is matched between arms). Unwritten; the decision note makes "cannot be written in a form a cold round accepts" an early stop.
7. Whether v0.4 goes to a cold round before pre-registration drafting.
8. The document's name: round 7 retired "useful divergence" as an endpoint; the title and file name still carry it.

## 12. Change log from v0.3
- §1: concentration clause removed; distribution of the gain reported, not claimed (round 7, 3 of 3).
- §2: sensitivity block formed from one main driver tag per event; `none` is the empty tag set (decision 2; round 5).
- §3: notes that the Step 0b lists are a draft (decision 1).
- §4 D: donor from a different sensitivity block; confirmatory-pool donor bank; seeded assignment with no reuse or a cap; fallback and feasibility statement; length uninformative, not matched; donor-source dependence to be stated (round 5). Four slots left to write.
- §4 BR: leave-one-group-out under the primary weights, formula written (round 5; round 8).
- §7: sensitivity formula with K draws and the ratio form; reported point estimate fixed as the primary one; admissibility rule and B_eff (round 5). Gates met only under both resamplings (round 6, 4 of 4). Divergence threshold and secondary endpoint replaced by descriptive disagreement reporting (round 7; decision 5).
- §8: Pass reworded; labelled FAIL added; "sensitivity inference not established" is FAIL; no rescue of a primary FAIL; completion rules required; no forecast after a grouping fail (rounds 5 and 6).
- §9: replaced in full; m = 0.01, signed November 26, 2026; S − BR spread demoted (round 8; item 10).
- §11: rewritten; four questions closed, eight listed.
- Not adopted, as the syntheses record: donor matching by the single-agent probability; a third-reader policy; Gemini's Option-A direction requirement; the slope test; a corporate driver class.
- Unchanged: §5, §6, §10; the per-market, per-event, per-group and per-arm score definitions; the primary endpoint; the NO-skew check; the early-stop causes.
