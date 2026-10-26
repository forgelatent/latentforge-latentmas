**Engine:** OpenAI. **Model:** GPT-6 Astra Pro (as self-reported). **Briefing:** 2026-10-26_cold_briefing_v5_scoring_rule_v0.3.md. Tier 3. Filed verbatim.

Q1 — Sensitivity recomputation

Yes: the proposed calculation preserves the equal-primary-group statistic while changing the resampling unit. It needs an explicit number of block draws per replicate and rules for cases where the sensitivity partition cannot support an uncertainty estimate. [E2, E4]

Let:

K = number of retained sensitivity blocks.
n_b = number of primary groups in block b.
S_b = sum of d_g over the primary groups in block b.

The original point estimate is:

Delta = sum_b S_b / sum_b n_b.

For each bootstrap replicate, draw exactly K blocks uniformly with replacement. If c_b is the number of times block b is drawn, calculate:

Delta* = sum_b(c_b × S_b) / sum_b(c_b × n_b).

This implements the stated rule: each primary group enters once per draw of its block. Do not average the sensitivity-block means equally; that would change the weights. E4 should explicitly specify K draws per replicate. [E2, E4]

The reported sensitivity point estimate must remain Delta. With unequal block sizes, the average of the bootstrap replicate ratios can differ from Delta; that does not authorize replacing the original point estimate with the bootstrap average. Changing only the resampling unit licenses no change to the reported point estimate. [E2, E4; mathematical implication]

The most important edge case is insufficient block-level information. Hypothetically, if there is one sensitivity block, every replicate reproduces the same data and returns the same value. The resulting zero-width interval would not establish perfect precision or robustness. Such a result must be “sensitivity inference not established,” not a numerical PASS; for a completed valid run, E4 therefore implies FAIL rather than VOID. This is not an estimate of how many blocks this pool will produce. [E4; mathematical implication]

More generally, very few or highly unequal blocks can make bootstrap inference unstable, while dependence remaining between blocks can understate uncertainty. Broader grouping is not guaranteed to widen an interval: the covariance of the paired score differences matters. Freeze the interval construction and an admissibility rule for inadequate block support before forecasts; no evidence in briefing supports a general numerical minimum. [E2, E4]


Q2 — What “survives” should mean

Require the sensitivity interval to lie entirely above m for the full claim in E1. That is the correct reading of “survives” for the proposed PASS. [E1, E2, E4]

For a positive m:

- An interval entirely above m supports an improvement exceeding the registered margin under the sensitivity dependence assumption.
- An interval entirely above zero, but not entirely above m, supports a positive improvement under that assumption; it does not establish the promised margin.
- An interval spanning zero establishes neither claim. It does not demonstrate that the effect is absent. [E1, E4; interpretation of the stated criteria]

If m is zero, the first two requirements coincide. Otherwise, using “excludes zero” for sensitivity would weaken the claim and should not receive the same PASS label as E1’s “beats text by more than the margin.” [E1, E4]


Q3 — Must the gates also survive sensitivity?

Yes. Require both gates to have intervals entirely above zero under both the primary and sensitivity resampling. Use the same fixed weights and resample the paired contrasts together. [E2, E4; recommendation]

For Gate 1, the failure shape permitted by not requiring sensitivity survival is a robust latent-versus-text performance result accompanied by fragile evidence that correct message pairing matters. The system could receive PASS while its content-attribution claim rests on the weaker dependence assumption. The claim supported by this gate should remain “correct pairing improves performance relative to the registered donor control.” [E4, E6]

For Gate 2, the failure shape is PASS without dependence-robust evidence that the latent system improves on silence. Beating text does not establish that separate requirement: text itself could be worse than the single receiver. [E4]

Requiring sensitivity survival can withhold PASS from a real benefit when the broader partition leaves inadequate precision. The correct interpretation is “not established under the registered sensitivity assumption,” consistent with E4’s operational FAIL definition. It must not be rewritten as “the channel carries nothing” or “latent communication cannot help.” [E2, E4]


Q4 — Donor selection

A different sensitivity block is stronger than necessary for a wrong-item swap, but it is defensible as a pre-registered screen against sharing a tagged driver. I would accept it only with a fixed, feasible donor-assignment procedure and an explicit interpretation of the comparison. Different blocks do not certify that a donor is irrelevant or otherwise comparable; that depends on the driver list and the remaining control conditions. [E2–E4]

Fix the following before the experiment:

- The donor population and permitted recipient–donor relationships.
- The definition of length and format, the matching tolerance, tie-breaking and seed.
- Whether assignment is a permutation or allows reuse, and how reuse is handled.
- The number of assignments evaluated.
- What happens when no valid assignment exists.
- Which variables may enter matching. Gold outcomes, receiver results and observed gate performance must not guide donor selection or fallback choices. [E4, E6; recommended control specification]

Prefer a global constrained permutation, where feasible, so each eligible draft is used once and the intervention changes pairing without arbitrarily changing message frequencies. There is a feasibility constraint: if one block contains more than half the eligible drafts, a one-use assignment sending every recipient a donor from another block is impossible. Length and format restrictions can also make assignment impossible. This is a conditional mathematical statement, not a prediction about the pool. [E4]

If reuse or another fallback is allowed, specify it in advance. Do not respond to an inconvenient assignment by silently widening tolerances, dropping recipients, selecting especially damaging donors, or trying seeds until the gate passes. Those choices would change the control being tested. [E4, E6]

Length matching can preserve a target-derived information channel. The length of A’s correct draft may contain information about its difficulty, confidence or content. Conditioning donor selection on that length therefore means Gate 1 tests the value of correctly paired content given the retained length/format features. This is not automatically leakage of the resolved outcome, but it is narrower than removing every target-derived cue. Using outcomes or receiver performance to choose the matching rule would be a different and unacceptable selection mechanism. [E4; analysis of the proposed rule]

There is also an inference issue: using a donor from another block creates a designed link between source and recipient observations. Reusing donors makes this especially apparent, but even a permutation connects observations across the blocks otherwise resampled separately. State whether inference conditions on a fixed donor bank and assignment, averages over pre-registered assignments, or otherwise accounts for donor-source dependence. The recipient-block bootstrap alone does not establish that this added dependence is covered. [E4; implication of its donor and resampling rules]


Q5 — Driver decisions

These are prospective design recommendations. They are not findings about actual event membership or estimates of the resulting group counts. [E2–E3]

D01 — SPLIT.

The current test combines conflict and negotiations, shipping, leadership, sanctions and currency, and participation in an international event. An Iranian subject alone does not establish that all these branches represent one shared cause. [E3]

Retain a conflict/negotiation/Hormuz driver, with separate tests for a named leadership process, sanctions/economic-policy process, and international-participation decision. Apply the conflict tag additionally when the written conditions support that connection. This reduces topic-based merging while preserving a genuine conflict link when documented. The risk of splitting is losing a shared shock across branches, so the replacement tests must expressly address those cross-links before Step 1. [E2–E3; proposed revision]

D03 — ACCEPT.

Territorial control and negotiations concerning the same named war are a defensible broad sensitivity hypothesis. Splitting front-line events from that war’s peace process would remove a connection the sensitivity check is intended to stress. Acceptance means testing that shared-process assumption; it does not establish that all included outcomes are equally dependent. [E2–E3]

D09 — ACCEPT THE STATE-KEYED FORM.

Each state parameter defines a different tag. “Summed over states” in the grain note must not silently become a nationwide driver. Splitting further by office or party would remove the state-wide electoral-shock hypothesis; merging states would introduce a different national-shock hypothesis. Neither change is supported by evidence of actual dependence in this briefing. [E3]

This does not establish independence between states. It preserves the sensitivity definition actually written. [E2–E3]

D15 — ACCEPT.

The named Brazilian electoral cycle is a defensible sensitivity process across its presidential, Senate and state contests. Splitting by office or region would test a weaker shared-election-shock assumption. Keep its role as a broader sensitivity driver distinct from the primary grouping of particular resolution facts. [E2–E3]

The grain note needs correction.

The number of driver labels alone does not determine which risk increases:

- Merging existing tags adds relationships and can coarsen the partition.
- Replacing one tag with narrower subsets can remove relationships and refine it.
- Adding a previously omitted overlapping driver can coarsen the partition even though the number of labels increases. [E2–E3; consequence of the connected-component rule]

Multiple tags can also connect seemingly separate drivers transitively. Hypothetically, an event tagged D01 and D12 and another tagged D03 and D12 would connect the two war-related drivers through D12. That relationship is permitted by the tests; there is no claim here that those events occur in the pool. Evaluate the full tagging construction, not the four broad labels in isolation. [E2–E3]

Classes the list can miss

Whether any of these classes actually occurs in the retained pool: no evidence in briefing. They are gaps in the written tests. [E3]

1. Otherwise-uncovered elections in a country already mentioned elsewhere. D31 excludes countries “named above,” even when the relevant election process is not covered by their listed drivers. Change the fallback to otherwise-uncovered 2026 electoral processes, keyed by country and named cycle; mentioning a country in another driver should not by itself exclude it. [E3]

2. Referenda not tied to a listed election. These are explicitly assigned none. Add a driver keyed to the jurisdiction, named referendum or campaign, and period. [E3]

3. Ordinary legislative, fiscal, regulatory and judicial policy processes outside the specifically named categories. Add tests keyed to a named budget cycle, legislative package, or legal/regulatory process and its linked implementation. Avoid an unrestricted “policy” or “US politics” category. [E3]

4. Monetary policy outside the listed rate decisions and Fed Chair tenure. Widen bank-specific tests to cover explicitly named balance-sheet programmes, interventions or emergency facilities where those processes are in scope. [E3]

Finally, encode none as an empty tag set, not as a shared driver. Otherwise the mechanical shared-tag rule could connect every unclassified event merely because each carries the word “none.” “No listed test applies” must not mean either “these events share a cause” or “these events are independent.” [E2–E3; implementation clarification]


Q6 — Divergence threshold

Keep delta = 0.10 as a fixed, symmetric operational threshold: ten percentage points of probability, such as 0.30 versus 0.40. There is no evidence in briefing that this is an optimal cutoff, that it will select enough observations, or that E5’s accuracy effects justify it. It is an interpretable design choice that must be fixed before forecasts. [E4–E5]

I would not scale it by the group’s realized YES rate. That would allow outcomes to influence which forecasts enter the selected subset, while changing the question from absolute disagreement to a relative measure. A leave-group-out reference avoids using the scored group’s own labels, but still defines a different endpoint without a stated reason for doing so. [E4; methodological implication]

I would not scale it by distance from 0.5 either. Brier scoring does not give 0.5 a special decision role here. Such scaling would require another choice about whose forecast defines the distance and could make very small changes near 0.5 qualify as substantial divergence. [E4; mathematical interpretation]

The endpoint can be pre-registered, but E4 currently specifies the selection rule without a complete secondary statistic or success criterion. I would add:

- Fixed aggregation: within each event, average T-minus-L Brier differences over its divergent markets; average eligible event means within each primary group; then average equally across primary groups containing divergent markets.
- A fixed claim: for example, positive mean Brier improvement on divergent forecasts, established only if the interval lies above zero under both primary and sensitivity resampling.
- A support rule specifying when there are enough eligible groups and sensitivity blocks to estimate that conditional effect. No evidence in briefing supplies a justified numerical minimum.
- Explicit handling of no divergence or inadequate support: “secondary claim not established,” without changing delta or treating the undefined effect as zero.
- Reporting of the fraction selected, its distribution across groups and blocks, and the size and uncertainty of the effect.
- No ability for this secondary result to rescue a primary FAIL. [E1, E4, E6; proposed secondary protocol]

A positive result on divergent forecasts would establish the specified conditional claim. It would not establish that the overall gain is concentrated there. That stronger claim requires a pre-registered comparison with nondivergent forecasts or a decomposition of the primary gain using its original weights. [E4; interpretation of the proposed endpoint]


Optional — Remaining verdict risks

The S-minus-BR spread is not an established noise estimate for T-minus-L. The two contrasts involve different forecasts and covariance structures, and E5 supplies no conversion to Brier effect size. Use S and BR for baseline and feasibility checks, but do not treat their spread as evidence that the main contrast is adequately powered. Set m from the smallest worthwhile improvement, or freeze an explicit rule for determining it before examining S results; the present text leaves a discretionary benchmark-dependent hurdle. [E1, E4–E5]

BR also needs the primary weights. “Pool’s YES rate” could mean the pooled market fraction, which does not generally minimize the equal-group, equal-event Brier objective. For the leave-group-out constant, average each event’s YES fraction within its group, then average those group rates equally over the other groups. Specify this formula and what “L beats BR” means operationally; its uncertainty requirement is currently unstated. [E4; derivation from its weights]

“Run incomplete” needs fixed completion, retry and abort rules. Otherwise unfavorable partial results could be converted into an incomplete-run VOID and a fresh attempt. This is a possible loophole in the wording, not evidence that it has happened. Inadequate sensitivity information in a completed valid run should remain “not established,” not become an execution VOID. [E4, E6]

The grouping early stop itself is explicit: E2 prohibits rescuing a failed grouping by splitting, changing lists, re-including unresolved events, adding readers or rerunning with counts visible. I find no authorized escape from that stop in the supplied text. [E2]

Vendor: OpenAI
Model: GPT-6 Astra Pro
