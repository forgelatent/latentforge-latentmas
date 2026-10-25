# Useful divergence — scoring rule, CANDIDATE v0.1 (October 25, 2026)

**Status:** CANDIDATE. Drafted by Systems Engine at the end of the Oct 25 session for a cold round; not canon until a cold round and Founder approval. Tier 3. Depends on a budget rule (not yet written) before any run. Nothing here is implemented.

## 1. The claim this rule scores
H3/H4 as stated in `founder_inputs/2026-09-25_founder_decision_review.md`: given the same information, do agents communicating in latent states forecast real resolved events better than the same agents communicating in text, and is the gain concentrated where the two disagree?

## 2. The data
`scratch/pool_resolutions_2026-10-25.json`: 410 resolved markets (81 YES, 329 NO) on 291 events, from the Polymarket snapshots. The unit of analysis is the EVENT, not the market: many markets are slices of one question (party rankings, seat bands, date windows), and only one slice wins. Each event counts once, however many markets it has.

## 3. The arms (all use the same model checkpoint and the same prompt text)
- **T (text):** agent A reads the question and writes a draft forecast with reasoning; agent B receives the question plus A's full draft as text and states a probability.
- **L (latent):** identical, except B receives A's draft as latent states (the channel under test) instead of text. The draft is the same draft.
- **D (deranged control):** identical to L, except B receives the latent states from a different question's draft. If L does not beat D, the channel carried nothing (Draft-KV's swap test).
- **S (single):** agent B alone, no message. The floor.
- **BR (base rate):** a constant forecast equal to the pool's YES rate computed leaving out the event being scored. The lazy-forecaster floor; 1 in 5 markets resolved YES, so this floor is not trivial.
- **C (crowd):** the last saved Polymarket price before resolution. Recorded and reported; never shown to any agent; not a target.

## 4. What every arm gets, and does not get
Gets: question text, description, outcome names, and a "forecast as of" date equal to the day the market was first seen in our snapshots. Does not get: any price, any web access, any other market, the resolution date. Identical for T, L, D, S. Different information between arms voids the comparison (the April 17 A/B test error).

## 5. Leakage rule
The model's training cutoff must be earlier than every market's "forecast as of" date; markets first seen before the cutoff are excluded before any run. Exclusions are listed in the pre-registration with the cutoff date and its source.

## 6. Scores
- Per market: Brier = (p - y)^2, with y in {0, 1}.
- Per event: mean Brier over its markets.
- Per arm: mean of per-event Brier (each event weight 1).
- **Primary endpoint:** paired difference per event, d_e = Brier_T(e) - Brier_L(e). Positive favors latent. Report the mean of d_e with a 95% bootstrap interval over events (10,000 resamples of events).
- **Divergence:** a market is "divergent" if |p_L - p_T| >= delta. delta is pre-registered (proposed 0.10; cold round to challenge).
- **Useful divergence (secondary endpoint):** on divergent markets only, grouped by event: mean of (Brier_T - Brier_L) with a bootstrap interval over events, and the share of divergent markets where L is closer to the outcome than T. Both reported.
- **Validity gate:** mean over events of Brier_D(e) - Brier_L(e) must be above zero with an interval excluding zero; otherwise the channel carried no content and no claim is made.
- Also reported, never endpoints: mean Brier for L, T, S, BR, C; calibration curves for L and T.

## 7. Pass, fail, void
- **Pass:** primary-endpoint interval entirely above the pre-registered margin m, AND the validity gate met, AND L beats both S and BR.
- **Fail:** the primary interval includes or is below m, or L does not beat S and BR.
- **Void:** validity gate not met, or the information rule in section 4 broken, or the budget rule not satisfied. Void is not fail; it is "the test did not happen."
Pass is necessary, not sufficient, for any external claim.

## 8. Margin and power
m is set at pre-registration, not here. External evidence (Draft-KV, strong receiver, shared input) puts the latent-over-text gap near +2 accuracy points on QA; what that means in Brier on this pool is unknown. Proposal for the cold round: split the pool by event into a 41-event calibration slice (used only to estimate the spread of d_e, tuning nothing) and a 250-event confirmatory set that is not looked at until the pre-registration is committed and hashed.

## 9. What this rule does not reward
Being different from the crowd. Being different from text. Beating the crowd. Being confident. Any of these alone is "horse territory" by the motor-car tests.

## 10. Open questions for the cold round
1. Is delta = 0.10 the right line, and should it scale with the event's base rate?
2. Should slices of one event be scored as a set (probabilities summing to 1 across the event) or independently?
3. Is the 41/250 split sound, and should the calibration slice serve the budget rule instead?
4. Is a 291-event pool large enough to bound a +2-point-class effect, or only larger ones?
5. What should m be, and in what units?
