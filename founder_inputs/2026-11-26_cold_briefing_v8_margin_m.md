# Cold briefing v8 — how the margin m is fixed (decision 6; first asking) (November 26, 2026)

**To the reader:** you have no terminal and no file access. Everything you may rely on is in the evidence blocks E1–E7 below, copied verbatim from committed project files and from two filed cold-round answers. Cite the block for every claim ("[E2]"). If the blocks do not support a claim, write "no evidence in briefing" rather than filling the gap. The Founder's view and the Systems Engine's view are deliberately withheld. Do not propose a model. Do not estimate how many markets, groups or blocks the pool will produce, or what the latent-versus-text effect will be. At the end, state your vendor AND model name.

**What is being reviewed.** One open point: how the pre-registered margin m — the amount by which the latent arm must beat the text arm for the experiment to PASS — is fixed. The current draft sets m *after* two baseline arms have been run on the real pool. Two readers flagged that in round 5 as a side remark; it has never been put as a question. This round asks it. **This round's answer is final for the method; the number itself, if the method is a governance choice, is the Founder's.** Nothing is implemented; no arm has run; no forecast exists.

---

## E1 — Founder decision note, items 2 and 5 (committed, amended October 25)
> 2. [...] the latent arm beats the text arm by more than the pre-registered margin, with error bars. **The margin and the budget rule are set at pre-registration, not after.**
> 5. **What stops me early.** Fewer than 150 independent events survive resolution lookup. No latent method passes the swap test on this task. The Mac Mini cannot run the chosen setup and $500 of GPU time cannot either. The budget rule cannot be written in a form a cold round accepts.
> 9 (b). Inter-reader agreement threshold for the dependence grouping: J_human >= 0.80, chosen by me as a governance rule, not derived from evidence (readers 3 of 3 that no evidence can set it); below it the grouping step fails and this note's early stop applies.

## E2 — Scoring rule CANDIDATE v0.3, §4 (arms), §7 ("beats"), §9 (margin), as written (committed `a6c2de8`)
> **S (single):** agent B alone, no message. The floor.
> **BR (base rate):** a constant forecast equal to the pool's YES rate computed leaving out the group being scored. Leave-one-out is by group, not by event, so no information from the scored group's siblings leaks in.
> **C (crowd):** the last saved Polymarket price before resolution. Recorded and reported; never shown to any agent; not a target.
> **"Beats"** means the 95% group-bootstrap interval of the difference excludes zero in the favorable direction.
> **§9. Margin and power.** m is an absolute reduction in group-averaged Brier under section 7's definition, set at pre-registration after the noise estimate below and before any T or L forecast. Not derived from accuracy points on QA; Draft-KV's ~+2 points under shared input is recorded so that m is chosen knowing the expected effect is small. No calibration slice; the full eligible pool is the confirmatory set. **Noise estimate:** the spread of per-group Brier differences from arms that do not involve the channel, S and BR, on the full pool, under the same group weights.

## E3 — The PASS rule as decided in cold round 6 (November 3; 4 of 4; committed `701fe1d`)
> Pass: primary-endpoint interval entirely above the pre-registered margin m under both primary-group and sensitivity-block resampling, AND Gate 1 and Gate 2 each met (95% interval entirely above zero under both resamplings), AND L beats BR. FAIL means "did not establish the required advantage," not "the advantage is absent." A primary interval that clears zero but not m under either resampling is a FAIL with its own label.

## E4 — Cold round 5, Optional: the two remarks on m, verbatim (committed `a6c2de8`)
**Gemini 3.1 Pro:** "Setting the margin m AFTER seeing S and BR on the confirmatory pool [...]: Running Agent B alone (S) on the full confirmatory pool and comparing it to the resolved ground-truth outcomes to compute Brier_S(g) − Brier_BR(g) *before* setting m means the operator and Systems Engine observe the exact base-rate Brier score and single-agent Brier error on the confirmatory test set before choosing the hurdle m. Worse, if the mapping from 'spread of Brier_S(g) − Brier_BR(g)' to m is not a rigid deterministic formula (e.g., m = k · SE(Brier_S − Brier_BR) with k fixed *before* running S), a human can choose a small m after seeing the noise number. **Fix:** Pre-register the exact multiplier formula for m *before* computing the noise estimate (or set m directly as a fixed fraction of Brier_BR)."

**GPT-6 Astra Pro:** "The S-minus-BR spread is not an established noise estimate for T-minus-L. The two contrasts involve different forecasts and covariance structures, and E5 supplies no conversion to Brier effect size. Use S and BR for baseline and feasibility checks, but do not treat their spread as evidence that the main contrast is adequately powered. Set m from the smallest worthwhile improvement, or freeze an explicit rule for determining it before examining S results; the present text leaves a discretionary benchmark-dependent hurdle. [...] BR also needs the primary weights. 'Pool's YES rate' could mean the pooled market fraction, which does not generally minimize the equal-group, equal-event Brier objective. For the leave-group-out constant, average each event's YES fraction within its group, then average those group rates equally over the other groups."

## E5 — The one external number on expected effect size (October 25 handoff, committed)
> Draft-KV (arXiv 2609.34754): on the only strong-receiver row the gap runs −0.1 to +3.8 accuracy points, mean about +2.1; no error bars. Accuracy points on a QA benchmark, not Brier on this pool. The size of the expected effect in Brier here is unknown.

## E6 — The pool (scoring rule v0.3 §2; the October 25 resolution lookup, committed)
> 410 resolved markets (81 YES, 329 NO) on 291 events with resolved markets. Resolutions are read from settlement prices. Outcomes are known for every market in the pool before any arm runs; the pool is frozen before forecasts.
Note: BR is a constant forecast and C is a saved price; neither involves a model. Their Brier scores on the frozen pool are arithmetic on data that already exists. S, T, L and D each require running a model.

## E7 — Project history relevant to thresholds (incident ledger, committed)
A prior benchmark script defined its winner as maximum distance from a hand-authored anchor and carried pre-written favourable prose for every verdict branch, so no result could be unfavourable; it is recorded as a "Pro-Thesis Optimization Loop." The project treats any hurdle that can be chosen or moved after results are visible as a known failure shape, and the April 18 incident as the cost of trusting a number whose provenance was not checked.

---

## Questions

**Q1 — When must m be fixed?** E1 says at pre-registration. E2 §9 sets it after S and BR have run on the real pool. Is running S (a model arm) before m is fixed acceptable under E1, or must m, or a deterministic formula for it, be fixed before *any* model arm runs? Does the answer differ for BR and C, which involve no model [E6]? State what a human can learn from each of S, BR and C before m is set, and whether that learning can move m.

**Q2 — Candidate rules.** Evaluate each, naming what it protects against and what it leaves open. (a) **A governance number:** the Founder fixes m in Brier units as the smallest improvement worth caring about, recorded as chosen, not derived — the same form as E1 item 9(b). (b) **A fixed fraction of BR's Brier** on the frozen pool (Gemini's alternative), computable before any model runs. (c) **A fixed multiplier of the S − BR spread**, with the multiplier frozen first (Gemini's first form), which GPT-6 says measures the wrong noise. (d) Any other rule you would put ahead of these three, stated in one sentence. Say which of (a)–(d) is pre-registrable *as written in the blocks* and which needs something the blocks do not contain.

**Q3 — What m is for.** Is m the *smallest effect worth claiming* (a value choice) or the *effect expected* (an empirical guess, E5)? Can E5 bear on m at all, given it is accuracy points on a different task? If a reader says "m should be small because the expected effect is small," what failure shape in E7 does that invite?

**Q4 — Text.** For the rule you choose, write the replacement for E2 §9 as it should appear in v0.4, under 150 words, including: when m is fixed relative to each arm; what S and BR may be used for; and the one sentence the pre-registration carries about how m was chosen. If you choose (a), write the sentence the Founder would sign.

**Optional.** Is there anything in E2 or E3 that lets m be revised after T or L has been seen, or lets a FAIL be converted by a change to m or to the noise estimate? If so, name the sentence to change.

**Filing.** Vendor: ____ Model: ____
