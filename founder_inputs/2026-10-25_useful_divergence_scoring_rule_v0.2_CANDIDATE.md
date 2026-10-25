# Useful divergence — scoring rule, CANDIDATE v0.2 (October 25, 2026)

**Status:** CANDIDATE. Drafted by Systems Engine from the cold round 2 synthesis (`founder_inputs/2026-10-25_cold_round2_synthesis.md`). Supersedes v0.1 (`founder_inputs/2026-10-25_useful_divergence_scoring_rule_CANDIDATE.md`, commit `11439d8`) only once the Founder approves. Tier 3. Depends on two things that do not yet exist before any run: a budget rule, and the frozen dependence grouping of section 3. Nothing here is implemented. Changes from v0.1 are marked **[v0.2]**; the change log is section 12.

## 1. The claim this rule scores
H3/H4 as stated in `founder_inputs/2026-09-25_founder_decision_review.md`: given the same information, do agents communicating in latent states forecast real resolved events better than the same agents communicating in text, and is the gain concentrated where the two disagree?

## 2. The data and the units
- Data: `scratch/pool_resolutions_2026-10-25.json`: 410 resolved markets (81 YES, 329 NO) on 291 events, from the Polymarket snapshots.
- **Market:** one Polymarket question with a YES/NO settlement.
- **Event:** the API's grouping of markets. Many markets are slices of one question (party rankings, seat bands, date windows) and only one slice wins. Scoring is per event: each event counts once, however many markets it has.
- **[v0.2] Outcome group:** a set of events that depend on the same underlying real-world outcome (several events about the same election, the same court case, the same price path). Distinct event IDs do not establish independence. The outcome group, not the event, is the independent unit: uncertainty is computed by resampling groups, and the decision note's 150-independent-events floor is tested against the number of groups.

## 3. [v0.2] Dependence grouping — a new step before the margin, before model choice, before any forecast
- Every one of the 291 events is assigned to exactly one outcome group by a written method. The method is designed and agreed before any code is written (design pending at this draft).
- The grouping is committed and hashed before any forecast is made, and is never changed afterwards. A grouping changed after the freeze voids the run (section 8).
- The 150 floor is tested against groups after leakage exclusions (section 6). Fewer than 150 groups is the early stop in the decision note (§5), not a reason to loosen this rule.
- The API `series` field was named as a candidate aid. It is not verified to exist in the pool file or the snapshots, and under Pattern G any field used for grouping is evidence, not definition: a human check of the grouping is part of the method and is recorded.

## 4. The arms (all use the same model checkpoint and the same prompt text)
- **T (text):** agent A reads the question and writes a draft forecast with reasoning; agent B receives the question plus A's full draft as text and states a probability.
- **L (latent):** identical, except B receives A's draft as latent states (the channel under test) instead of text. The draft is the same draft.
- **D (deranged control):** **[v0.2]** identical to L, except B receives the latent states of a *donor* draft: a draft written by agent A for a market in a **different outcome group** (not merely a different question, which could be a sibling slice). The donor is chosen by a rule fixed at pre-registration, with a declared rule for matching message length and format. B's own input (question, description, outcome names, "forecast as of" date) is unchanged. This substitution is the one permitted exception to section 5 and is named there.
- **S (single):** agent B alone, no message. The floor.
- **BR (base rate):** a constant forecast equal to the pool's YES rate computed leaving out the event being scored. 1 in 5 markets resolved YES, so this floor is not trivial.
- **C (crowd):** the last saved Polymarket price before resolution. Recorded and reported; never shown to any agent; not a target.

## 5. Information rule
Every arm gets: question text, description, outcome names, and a "forecast as of" date. No arm gets: any price, any web access, any other market, the resolution date. Identical for T, L, D, S, with one registered exception: in D, agent B's message is the donor draft from section 4; B's own input is still unchanged. Different information between arms voids the comparison (the April 17 A/B test error).

**[v0.2]** Markets of the same event share one "forecast as of" date, so that siblings scored together were forecast from the same point in time. Proposed: the latest first-seen date among the event's markets, so no market is forecast before it existed in our snapshots. Open for Founder approval (section 11).

## 6. Leakage rule
The model's training cutoff must be earlier than every market's "forecast as of" date; markets first seen before the cutoff are excluded before any run. Exclusions are listed in the pre-registration with the cutoff date and its source.

**[v0.2]** The earliest "forecast as of" date in the pool is March 23, 2026. Before any model is chosen, the number of eligible markets, events and groups under each candidate cutoff is counted and recorded. A candidate whose cutoff leaves fewer than 250 markets or 150 groups cannot satisfy the decision note's floors; choosing it anyway is the early stop, not a reason to lower the floors.

## 7. Scores
- Per market: Brier = (p − y)², with y in {0, 1}. Binary, per market, on the frozen list.
- Per event: mean Brier over its markets. **[v0.2]** No sum-to-1 constraint across slices. The market list, outcome definitions and weights (each market weight 1 within its event, each event weight 1) are frozen before forecasts and never changed; adding or dropping slices after the freeze voids the run. This is the defence against the slice-count arithmetic the cold round named (an all-zero forecast on an event with K exclusive slices scores 1/K).
- Per arm: mean of per-event Brier.
- **Primary endpoint:** paired difference per event, d_e = Brier_T(e) − Brier_L(e). Positive favors latent. Report the mean of d_e with a 95% bootstrap interval. **[v0.2]** The bootstrap resamples outcome groups (10,000 resamples), so all events in a group move together.
- **[v0.2] Also reported:** the primary endpoint on the subset of events that contain at least one YES-resolved market. (81 YES markets across 291 events means at most 81 such events and at least 210 events holding only NO.) This checks that a positive mean is not produced mechanically by the NO skew.
- **Divergence:** a market is "divergent" if |p_L − p_T| ≥ delta. delta is pre-registered. Proposed 0.10; no cold reader addressed it; still open (section 11).
- **Useful divergence (secondary endpoint):** on divergent markets only, grouped by event: mean of (Brier_T − Brier_L) with a group-bootstrap interval, and the share of divergent markets where L is closer to the outcome than T. Both reported.
- **[v0.2] Gates (both required; both 95% group-bootstrap intervals; Brier, not accuracy):**
  - **Gate 1, pairing:** mean over events of Brier_D(e) − Brier_L(e) > 0, interval excluding zero. If not met: "no positive task-relevant pairing effect was established." Not "the channel carried no content."
  - **Gate 2, usefulness:** mean over events of Brier_S(e) − Brier_L(e) > 0, interval excluding zero. If not met: "no advantage over a single agent was established." Gate 1 alone can be passed by a harmful mismatch (outcome NO, L = S = 0.20, D = 0.80: pairing gain +0.60, benefit over silence zero).
- **"Beats"** anywhere in this rule means the 95% group-bootstrap interval of the difference excludes zero in the favorable direction, not a raw mean difference.
- Also reported, never endpoints: mean Brier for L, T, S, BR, C; calibration curves for L and T.

## 8. Pass, fail, void **[v0.2]**
- **Pass:** primary-endpoint interval entirely above the pre-registered margin m, AND Gate 1, AND Gate 2, AND L beats BR.
- **Fail:** a valid run that does not pass: the primary interval includes or is below m, or a gate is missed, or L does not beat BR. FAIL means "did not establish the required advantage," not "the advantage is absent." A missed Gate 1 is the decision note's early stop ("no latent method passes the swap test on this task").
- **Void:** only for execution or protocol failure: the information rule broken, the budget rule not satisfied, the grouping or market list changed after the freeze, the run incomplete. Void means the test did not happen; it may be rerun once the failure is fixed, under the same rule. A valid run that misses a gate is never void.
Pass is necessary, not sufficient, for any external claim.

## 9. Margin and power **[v0.2]**
- m is an absolute reduction in event-averaged Brier under section 7's definition. It is set at pre-registration, after the noise estimate below and before any T or L forecast. It is not derived from accuracy points on QA (Draft-KV's ~+2 points under shared input, strong receiver, is recorded so that m is chosen knowing the expected effect is small; its size in Brier on this pool is unknown).
- No calibration slice. The 41/250 split is dropped; the full eligible pool is the confirmatory set.
- Noise estimate: the spread of per-event Brier differences is estimated from arms that do not involve the channel, S and BR, on the full pool. These reveal nothing about T or L and cost no events.

## 10. What this rule does not reward
Being different from the crowd. Being different from text. Beating the crowd. Being confident. Any of these alone is "horse territory" by the motor-car tests.

## 11. Open questions
1. delta = 0.10: right line? Should it scale with the event's base rate? (Carried from v0.1; unanswered by the cold round.)
2. Shared "forecast as of" date for siblings: latest first-seen (proposed) or earliest.
3. The grouping method of section 3 (design pending; Context Declaration first).
4. The donor rule for D: how a donor group is chosen, and how message length and format are matched.
5. Whether v0.2 goes to a third cold round or straight into pre-registration drafting.

## 12. Change log from v0.1
- Unit of independence is the outcome group, not the event; new section 3; bootstrap by group; 150 floor tested on groups (Q1, three readers).
- 41-event calibration slice dropped; full pool confirmatory; noise from S and BR (Q2, unanimous).
- Slices scored as independent binary markets on a frozen list; no sum-to-1; list and weights frozen (Q3 resolution; Grok's set scoring not adopted).
- Second gate added: L must beat S with an interval excluding zero; Brier kept (Q4, unanimous; Grok's accuracy-style alternative not adopted).
- Void narrowed to execution/protocol failure; valid run missing a gate is FAIL; FAIL defined; "beats" defined (Optional, unanimous).
- m defined as absolute Brier reduction, set after noise estimate (Q5, unanimous).
- Section 3/4 contradiction fixed: D's donor substitution is a registered exception; donors from a different group (ChatGPT only).
- "Channel carried no content" replaced by "no positive pairing effect established" (ChatGPT only).
- Primary endpoint also reported on YES-containing events (Grok's bias concern).
- Leakage rule gains an eligibility count per candidate cutoff before model choice (Gemini's starvation concern).
