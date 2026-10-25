# LatentForge — cold review briefing v2: the "useful divergence" scoring rule (October 25, 2026)

**To the reviewing engine: read this first.** You have no terminal, repository or file access. Everything you may rely on is in a labeled block below (E1 to E6) or in the candidate rule pasted verbatim after them. Cite the block or the rule's section number for every claim. If a claim has no block, write "no evidence in briefing". In May 2026 an engine reviewing this project described code that did not exist, with line numbers; the operator caught it by running the engine's own commands. That is why this format exists. The Founder's and the Systems Engine's views on the open questions are withheld; do not infer them from question wording. Nothing is attached; the rule is inline.

## Context in one paragraph
LatentForge (solo non-technical founder; Claude as Systems Engine; Grok, Gemini and ChatGPT as cold reviewers) is testing whether agents that pass latent states instead of text forecast better. On Oct 25 the Founder decided to continue with one pre-registered test on resolved Polymarket markets (E1), outer kill date Dec 31, 2026. The document under review is the CANDIDATE scoring rule for that test. It is not implemented. No experiment is designed yet. A budget rule (how to match compute between arms) is a separate, unwritten precondition and is out of scope here.

## Evidence (Tier 1 = operator-verified on the host; Tier 3 = read from papers)
**E1 (Tier 1).** Candidate pool: 412 policy, geopolitics and macro markets from daily Polymarket snapshots (138 files, Mar 23 to Oct 25, 2026), excluding sports (by API flags) and crypto, each first seen at least 7 days before its end date, "will X say Y" markets removed. Resolutions looked up from the Gamma API on Oct 25: 410 resolved (81 YES, 329 NO), 2 still open, 0 not found, 0 ambiguous; 291 distinct events. Resolution read from settlement prices (one side >= 0.99, the other <= 0.01). 223 markets were first seen 30+ days before their end date; 112 had over $10K traded.
**E2 (Tier 1).** Many markets are slices of one event (party rankings, seat bands, date windows) and only one slice wins; hence the 19.8% YES rate. The API's `umaResolutionStatuses` field is not a reliable resolution flag (220 of 410 settled markets show only "proposed").
**E3 (Tier 1).** The project has no matched latent-vs-text experiment on record. Its April 17 "A/B test" gave the two arms different information. Its earlier benchmark scored against a hand-typed seed file for 20 days (April 18 incident); every claim from it is retracted.
**E4 (Tier 3, read directly Oct 25).** Draft-KV (arXiv 2609.34754): in prior latent interfaces (LatentMAS, C2C), swapping the message for one from an unrelated question changes accuracy by at most 0.60 points while total gain reaches 15.44, i.e. gains that do not depend on content. Their method passes draft-position states through a trained 1.05M-parameter bridge and beats the identical draft given as text in 33 of 35 shared-input settings, mean +5.85 points; on the only strong-receiver row (Qwen3-8B to Qwen3-4B) the gap runs -0.1 to +3.8, mean about +2.1, at about 2x the sharer compute (13.745 vs 7.187 TFLOPs). No error bars on the medium gap.
**E5 (Tier 3).** arXiv 2608.04893 (Aug 2026): the pairing effect is at ceiling when the receiver needs the sender's private information and within +-2.8 points when it could solve alone; its direct-text arm is, in its own words, a validity calibration, not a text baseline.
**E6 (Founder decision note, Oct 25).** "Proven" means: at least 250 resolved markets on at least 150 independent events, latent beats text by more than the pre-registered margin, with error bars. Spend: Mac Mini first, then up to $500 of GPU rental. Early stops include: no latent method passes the swap test on this task.

=== THE CANDIDATE RULE, VERBATIM. File: founder_inputs/2026-10-25_useful_divergence_scoring_rule_CANDIDATE.md, sha256 first 12: 4b3b37bb9ab4 ===

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

## Questions
Answer each separately. Cite E-blocks or rule section numbers. Write "no evidence in briefing" where that is the honest answer.
**Q1 (one reason, argued).** The single biggest way this rule could declare a PASS that is not real, or a FAIL that is not real. One, not a list.
**Q2.** Section 8 proposes a 41-event calibration slice and a 250-event confirmatory set. Keep, drop, or replace with what? Reason in three sentences.
**Q3.** Section 2 and open question 2: should slices of one event be scored as a set (probabilities constrained to sum to 1 across the event) or independently? Which choice can be gamed, and how?
**Q4.** Section 6, validity gate: is "mean Brier_D minus Brier_L above zero with an interval excluding zero" a sufficient swap test, or must the gate use the accuracy-style pairing gain from E4? If insufficient, state the gate you would require.
**Q5.** Given E1, E2 and E4, propose a margin m with units and a one-line justification, or write "no evidence in briefing".
**Optional.** Anything in the rule that makes it unable to fail.
**Filing.** Reply as plain text. Your answer is filed with your vendor AND model name; state the model if you can.
