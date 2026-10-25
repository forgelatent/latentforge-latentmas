**Engine:** OpenAI. **Model:** GPT-6 Astra Pro (as self-reported). **Briefing:** 2026-10-25_cold_briefing_v2_scoring_rule.md. Tier 3. Filed verbatim.

Vendor: OpenAI
Model: GPT-6 Astra Pro

Q1. The single biggest risk: a false PASS from overstating how many independent observations you have.

E1 establishes 291 distinct events; E6 requires at least 150 independent events. Distinct event IDs do not establish independence, and there is no evidence in briefing that this requirement has been checked. Sections 2 and 6 address multiple markets within one event, but do not specify how to handle separate events that depend on the same underlying outcome. [E1, E2, E6; rule §§2, 6]

If several such events produce correlated latent-versus-text score differences, independently resampling their event IDs can make the confidence interval too narrow. The rule could then declare PASS because repeated measurements of related outcomes were treated as separate pieces of evidence. This is a possible failure of the proposed inference, not a claim that this dependence has already been observed. [Rule §§6–7]

Before generating forecasts, define the underlying outcome groups used to assess independence, keep every related group entirely within either development or confirmation, and resample those groups together when calculating uncertainty. Preserve the intended scoring weights explicitly, and check E6's minimum against the resulting independent units rather than assuming the API's event count satisfies it. [E6; proposed repair to rule §§2, 6, 8]

Q2. Replace the fixed 41/250 split.

Replace it with a development/confirmation split made after cutoff exclusions and grouping of dependent events, because the current allocation assumes all 291 events remain eligible and provide independent evidence. [E1, E6; rule §§5, 8]

Choose the smallest worthwhile Brier improvement independently of the pilot's observed advantage, use a disjoint pilot to estimate variability and check feasibility, and reserve an untouched confirmatory set sized for a predeclared power or precision target. [Rule §§6–8]

If the eligible pool cannot meet that target while retaining at least 250 resolved markets across 150 independent events for confirmation, record that limitation rather than lowering the margin to accommodate the available data. [E6; rule §8]

Q3. Use coherent set scoring for verified complete outcome sets; otherwise retain binary scoring.

Do not impose a blanket requirement that the retained markets' YES probabilities sum to one. E2 describes different kinds of slices, but does not establish that every retained event is a complete set of mutually exclusive outcomes. [E2; rule §2]

There is also a direct arithmetic check: 81 YES resolutions across 291 events means at most 81 events contain a retained YES winner. At least 210 events therefore contain only retained NO outcomes. Requiring one of the retained YES outcomes to occur would be wrong for those events unless an appropriate residual outcome is included. [Derived from E1 and rule §2]

For a verified complete, mutually exclusive set, my recommendation is one event-level probability vector, with nonnegative probabilities summing to one, scored as:

Brier_event = 0.5 × sum over outcomes of (predicted probability − outcome indicator)².

This has a 0–1 range and reduces to the ordinary binary Brier score when there are two complementary outcomes. An incomplete exclusive set needs a "none of these" outcome; overlapping or nested questions need their actual logical constraints and generally cannot be forced to sum to one. [Proposed scoring definition based on rule §§2, 6]

For events without a defensible complete partition, independently scored binary probabilities remain legitimate. Scoring them separately does not mean treating them as independent observations for uncertainty. [Rule §§2, 6]

The gaming risk is changing the slices and their weights. Under the proposed mean-over-markets score, an event with K exclusive slices and one YES winner gives an all-zero forecast a score of 1/K. Adding more losing slices makes that incoherent forecast look closer to a perfect score, even though it still assigns zero probability to the winning outcome. This is arithmetic under the candidate rule, not an observed result. [E2; rule §6]

For a fixed market list, binary Brier scoring remains a proper score: an always-NO forecast is not a mathematical shortcut to beating honest probabilities in expectation. Freeze the outcome definitions, inclusion rules and weights before forecasts; simply imposing sum-to-one does not protect against changing the categories afterward. [Mathematical property of the score in rule §6]

Finally, coherent set forecasting requires a common information date and a defined outcome set. Section 4 currently uses each market's first-seen date and prohibits other markets, so a set-based approach requires an explicit revision before registration. Whether sibling markets already share the same first-seen date: no evidence in briefing. [Rule §4]

Q4. Keep Brier for the swap test; distinguish a pairing effect from useful improvement.

The proposed Brier difference is appropriate for a probability-forecasting task. E4's use of accuracy on question-answering tasks does not require this experiment to replace its probability score with accuracy. [E4; rule §§1, 6]

With a valid swap construction and uncertainty calculation, an interval entirely above zero for:

G_pair = mean_event(Brier_D − Brier_L)

is sufficient evidence that correct pairing improves forecasting relative to the registered mismatches. It is not sufficient by itself to show that the correct message helps compared with receiving no message. [Rule §§3, 6]

A hypothetical example shows the distinction. Suppose the outcome is NO, both L and S forecast 0.20, and D forecasts 0.80. Their Brier scores are 0.04, 0.04 and 0.64: the swap gain is +0.60, but the correct message adds no benefit over the single receiver. The entire gap comes from the mismatched message making performance worse. [Arithmetic using rule §6]

I would require:

1. For demonstrated pairing: the prespecified 95% interval for G_pair lies entirely above zero.

2. For useful communication: the prespecified 95% interval for mean_event(Brier_S − Brier_L) also lies entirely above zero.

The second condition can remain in the PASS rule rather than the swap gate. Section 7 already requires L to beat S, but "beats" needs an explicit uncertainty criterion; retain the separate comparisons with T and BR. [E6; proposed clarification to rule §§6–7]

The swap procedure also needs to be frozen. Swap across different underlying event groups, not merely different questions, because another question may be a related slice; preserve the receiver's original input and use a declared rule for compatible message format and length. Use uncertainty estimates that respect the dependence identified in Q1. [E2; proposed clarification to rule §§3, 6]

Replace "otherwise the channel carried no content" with "no positive task-relevant pairing effect was established." Content can be redundant, and an interval spanning zero does not establish its absence. [E5; rule §§3, 6]

Q5. Margin m.

No evidence in briefing: m must be an absolute reduction in the event-averaged Brier score under the final scoring definition, and E4's accuracy percentage points provide neither a conversion nor a justified minimum worthwhile Brier improvement. [E4; rule §§6, 8]

Optional. The rule misclassifies an important stopping result.

Section 7 calls failure of the swap gate VOID and says "the test did not happen," while E6 explicitly makes failure to pass the swap test an early-stop condition. A correctly executed test that fails to establish a pairing benefit did happen; its scientific result may be negative or inconclusive, but it has not met the continuation requirement. Reserve VOID for an actual protocol or execution failure, and make E6's stop condition apply to valid experiments that miss the gate. The rule has other FAIL paths, so it is not literally unable to fail, but this wording allows a central negative result to be dismissed. [E6; rule §7]

There is also a literal contradiction to fix: section 3 deliberately gives D another question's draft, while section 4 prohibits "any other market" for D as well. Explicitly permit the registered message substitution in D, otherwise a legitimate swap test could automatically violate the information rule and become VOID. [Rule §§3–4, 7]

Finally, define FAIL as "did not establish the required advantage" if that is the intended operational decision. An interval spanning m can justify stopping under the deadline, but it does not demonstrate that a worthwhile advantage is absent. [E6; rule §§7–8]
