# Useful divergence — scoring rule, CANDIDATE v0.3 (October 26, 2026)

**Status:** CANDIDATE. Drafted by the Systems Engine from v0.2 (`founder_inputs/2026-10-25_useful_divergence_scoring_rule_v0.2_CANDIDATE.md`, commit `de149a1`), the agreed grouping design v3 (`founder_inputs/2026-10-25_grouping_design_v3.md`, commit `2e1bf84`), and item 9 of the Founder decision note (`founder_inputs/2026-10-25_founder_decision_note.md`). Supersedes v0.2 only once the Founder approves. Tier 3. Nothing here is implemented. Changes from v0.2 are marked **[v0.3]**; the change log is section 12. No group count appears in this file.

**Decisions carried (Founder, October 25, item 9).** (1) The independent unit is the pre-registered outcome group; each group has equal weight in the primary score. (2) Inter-reader agreement threshold J_human ≥ 0.80, a governance choice; below it the grouping step fails. (3) The sorters' review list may be ordered by resolution source, event date, normalised title, under the written contract that order is never evidence. The Step 0b lists (driver list, normalisation words, worked examples) are in `founder_inputs/2026-10-25_grouping_step0b_lists_CANDIDATE.md`; grain at the broad end is a Founder decision still open at this draft.

## 1. The claim this rule scores
Unchanged from v0.2: given the same information, do agents communicating in latent states forecast real resolved events better than the same agents communicating in text, and is the gain concentrated where the two disagree?

## 2. The data and the units
- Data: `scratch/pool_resolutions_2026-10-25.json`: 410 resolved markets (81 YES, 329 NO). **[v0.3]** The file holds 292 events; 291 carry resolved markets and one (the Sweden PM pair) carries only STILL_OPEN markets and is never in the confirmatory sample. Both figures are correct for what they count.
- **Market:** one Polymarket question with a YES/NO settlement.
- **Event:** the API's grouping of markets. Many markets are slices of one question and only one slice wins. Per-event scores are still computed (section 7) but the event is no longer the unit of weight.
- **[v0.3] Outcome group:** a pre-declared dependence block, as defined in design v3: events linked by clause (a) same proceeding, office, legal action, instrument or event instance; (b) one resolution restricts the other's valid outcomes; or (c) the same named measurement or process over overlapping outcome windows read from the resolution conditions. Groups are the connected components of accepted links. Different group ids do not establish independence. **The outcome group is the unit of resampling and the unit of primary weight** (decision 1). The decision note's floors are tested against groups.
- **[v0.3] Sensitivity block:** the connected components of "same primary group OR shares an adjudicated driver tag" (v3, Step 5). Used only to recompute uncertainty (section 7); never a unit of weight.

## 3. [v0.3] Dependence grouping — governed by design v3, not restated here
The grouping is produced by design v3 (agreed October 25), which replaces v0.2's section 3 in full. What this rule depends on from it:
- The fixed lists of Step 0b are committed and hashed with the pool hash before Step 1 and never change after Step 1 starts.
- Two blind partitions (Founder; one cold engine session, vendor and model recorded), neither reader shown any count or any outcome; J_human ≥ 0.80 or the step fails; disagreements adjudicated with evidence; unsettled events become unresolved; no default merge, no default split, no third reader.
- Unresolved events and their markets are removed before the freeze. The groups file is committed and hashed; its hash goes into the pre-registration. Only after the freeze is anything counted.
- Both minima are tested on the retained sample after exclusions: at least 250 markets and at least 150 primary groups. Fewer is the decision note's early stop, not a reason to loosen anything.
- The `series` and `parentEventId` fields exist in the snapshots (verified October 25) and are candidate signals only; under Pattern G every API field is evidence, not definition.
- A grouping step that fails (v3 Fail conditions) stops the project before any forecast; it is not a run outcome under section 8.

## 4. The arms (all use the same model checkpoint and the same prompt text)
- **T (text):** agent A reads the question and writes a draft forecast with reasoning; agent B receives the question plus A's full draft as text and states a probability.
- **L (latent):** identical, except B receives A's draft as latent states instead of text. The draft is the same draft.
- **D (deranged control):** identical to L, except B receives the latent states of a donor draft written by agent A for a market in a different primary group. **[v0.3, proposed, open]** Where sensitivity blocks exist, the donor is drawn from a different sensitivity block as well, so that no driver is shared; the donor is chosen by a seeded deterministic rule fixed at pre-registration, matched on draft length within a stated tolerance and on format. B's own input is unchanged. This substitution is the one permitted exception to section 5.
- **S (single):** agent B alone, no message. The floor.
- **BR (base rate):** a constant forecast equal to the pool's YES rate computed leaving out the group being scored. **[v0.3]** Leave-one-out is by group, not by event, so no information from the scored group's siblings leaks in.
- **C (crowd):** the last saved Polymarket price before resolution. Recorded and reported; never shown to any agent; not a target.

## 5. Information rule
Unchanged from v0.2: every arm gets question text, description, outcome names, and a "forecast as of" date; no arm gets any price, web access, other market, or the resolution date. Identical for T, L, D, S, with the registered D exception. Different information between arms voids the comparison.

Markets of the same event share one "forecast as of" date. Proposed: the latest first-seen date among the event's markets. **[v0.3]** This date is a collection date and is deliberately not the outcome window of design v3; the two serve different purposes and neither is read from the other. Still open for Founder approval (section 11).

## 6. Leakage rule
Unchanged in substance: the model's training cutoff must be earlier than every market's "forecast as of" date; markets first seen before the cutoff are excluded before any run, listed with the cutoff and its source. Eligible markets, events and groups are counted and recorded under each candidate cutoff before any model is chosen; a candidate whose cutoff leaves fewer than 250 markets or 150 groups cannot satisfy the floors.

**[v0.3]** Leakage exclusions follow v3 Step 6: every surviving event keeps its frozen group id and driver tags; empty groups are dropped; both minima are re-checked; a surviving group is never split because a bridging event was removed.

## 7. Scores
- Per market: Brier = (p − y)², y in {0, 1}. Binary, per market, on the frozen list. No sum-to-1 constraint across slices; the market list, outcome definitions and weights are frozen before forecasts.
- Per event: mean Brier over its markets (each market weight 1 within its event).
- **[v0.3] Per group:** mean of its events' per-event Brier (each event weight 1 within its group). **Each group has weight 1 in every arm-level score and in the primary endpoint** (decision 1).
- Per arm: mean over groups of the per-group Brier.
- **[v0.3] Primary endpoint:** paired difference per group, d_g = Brier_T(g) − Brier_L(g). Positive favors latent. Report the mean of d_g over groups with a 95% bootstrap interval; the bootstrap resamples primary groups (10,000 resamples, with replacement, equal probability per group).
- **[v0.3] Reported beside it, never in place of it:** the per-event form, mean over events of d_e = Brier_T(e) − Brier_L(e), with its own interval from resampling groups (all events in a group move together). This is v0.2's primary endpoint, kept so the two weightings can be compared; it is not an endpoint.
- **[v0.3] Sensitivity recomputation (v3, Step 5), written out:** the statistic is unchanged — the equal-weight mean of d_g over primary groups — and only the resampling unit changes. Each resample draws sensitivity blocks with replacement (equal probability per block); every primary group inside a drawn block enters the statistic once per draw of its block; the resample's value is the mean of d_g over the groups so entered. 10,000 resamples; 95% interval. The point estimate under sensitivity is therefore the same number as the primary point estimate; what moves is the interval. Reported beside the primary interval, never in place of it.
- Also reported: the primary endpoint on the subset of groups containing at least one YES-resolved market (the NO-skew check), with a group bootstrap.
- **Divergence:** a market is "divergent" if |p_L − p_T| ≥ delta. delta is pre-registered. Proposed 0.10; unaddressed by any cold round; still open (section 11).
- **Useful divergence (secondary endpoint):** on divergent markets only, aggregated to groups by the same means and weights: mean of (Brier_T − Brier_L) with a group-bootstrap interval, and the share of divergent markets where L is closer to the outcome than T. Both reported.
- **Gates (both required; both 95% group-bootstrap intervals; Brier, not accuracy):**
  - **Gate 1, pairing:** mean over groups of Brier_D(g) − Brier_L(g) > 0, interval excluding zero. If not met: "no positive task-relevant pairing effect was established."
  - **Gate 2, usefulness:** mean over groups of Brier_S(g) − Brier_L(g) > 0, interval excluding zero. If not met: "no advantage over a single agent was established."
  - **[v0.3]** Both gates are also recomputed under the sensitivity resampling and reported. Whether a gate must also survive sensitivity to count as met is open (section 11); the primary endpoint must (section 8).
- **"Beats"** means the 95% group-bootstrap interval of the difference excludes zero in the favorable direction.
- Also reported, never endpoints: mean Brier for L, T, S, BR, C per group and per event; calibration curves for L and T; the group-size distribution, the number of groups with two or more events, the largest group's share of events and of weight under both weightings, and the sensitivity-block count beside the primary group count (v3, Step 4).

## 8. Pass, fail, void, early stop
- **Pass:** primary-endpoint interval entirely above the pre-registered margin m under primary-group resampling, **[v0.3] AND the sensitivity interval entirely above m** (proposed reading of v3's "survives"; see section 11), AND Gate 1, AND Gate 2, AND L beats BR.
- **Fail:** a valid run that does not pass. FAIL means "did not establish the required advantage," not "the advantage is absent." A missed Gate 1 is the decision note's early stop for any further latent work. **[v0.3]** A primary PASS whose sensitivity interval does not clear m is reported as "not established under the sensitivity partition" and is a FAIL.
- **Void:** only for execution or protocol failure: the information rule broken; the budget rule not satisfied; the market list, the groups file, the driver tags or any Step 0b list changed after the freeze; **[v0.3]** any group or candidate count shown to a reader during Step 3; the run incomplete. Void means the test did not happen; it may be rerun once the failure is fixed, under the same rule and the same frozen grouping.
- **[v0.3] Early stop (before any forecast):** the grouping step fails under v3's Fail conditions (fewer than 250 markets or 150 primary groups retained after Step 4 or Step 6; J_human < 0.80; the driver list cannot be written with one-line membership tests). This is the decision note's §5 stop, not a run outcome, and none of its causes may be cured by splitting, re-defining, re-including, adding a reader, or re-running with a count visible.
Pass is necessary, not sufficient, for any external claim.

## 9. Margin and power
- m is an absolute reduction in **[v0.3] group-averaged** Brier under section 7's definition, set at pre-registration after the noise estimate below and before any T or L forecast. Not derived from accuracy points on QA; Draft-KV's ~+2 points under shared input is recorded so that m is chosen knowing the expected effect is small.
- No calibration slice; the full eligible pool is the confirmatory set.
- Noise estimate: the spread of per-group Brier differences from arms that do not involve the channel, S and BR, on the full pool, under the same group weights.

## 10. What this rule does not reward
Being different from the crowd. Being different from text. Beating the crowd. Being confident. Any of these alone is "horse territory" by the motor-car tests.

## 11. Open questions
1. delta = 0.10: right line? scale with the base rate? (Carried from v0.1; no cold round has addressed it.)
2. Shared "forecast as of" date for siblings: latest first-seen (proposed) or earliest.
3. Donor rule for D: different sensitivity block as well as different group (proposed); length tolerance; seeding.
4. Whether Gates 1 and 2 must survive the sensitivity resampling, or are only reported under it.
5. What "survives" means for the primary endpoint under sensitivity: interval above m (proposed here) or interval excluding zero.
6. Driver-list grain at the broad end (D01, D03, D09, D15): a Founder decision, affects section 7's sensitivity blocks only.
7. Whether v0.3 goes to a cold round before pre-registration drafting.

## 12. Change log from v0.2
- Unit of primary weight is the outcome group, each weight 1 (decision 1; round 4, 3 of 3); per-group means and endpoint; per-event form demoted to a reported comparison.
- Section 3 replaced by a pointer to design v3; grouping failure is an early stop, not a run outcome; counts only after freeze; both minima after exclusions (v3).
- Sensitivity block defined; the Step 5 recomputation written out as a resampling rule with the primary weights unchanged; primary PASS must survive it (v3).
- Void gains: Step 0b lists or driver tags changed after freeze; a count shown during review.
- Leakage exclusions follow v3 Step 6 (keep ids, drop empty groups, never split).
- BR leave-one-out by group, not event.
- Decisions 1–3 recorded at the top; agreement threshold and sort-order contract referenced, not restated.
- 292/291 event count clarified.
- Proposed, not decided: donor from a different sensitivity block; gates reported under sensitivity; "survives" = above m.
- Unchanged: delta open; information rule; leakage rule's cutoff count; Gate definitions; FAIL and "beats" wording; section 10.
