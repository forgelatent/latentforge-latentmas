**Engine:** OpenAI. **Model:** GPT-6 Astra Pro (as self-reported). **Briefing:** 2026-11-03_cold_briefing_v7_adjudication_decision5.md. Tier 3. Filed verbatim.

## Q1 — Choose **(b): retain the fixed 0.10 threshold with an explicitly conditional protocol**

**Keep the secondary endpoint, but limit its claim to whether latent forecasts improve on text forecasts among markets where their probabilities differ by at least ten percentage points.** A positive result would not, by itself, establish that the overall gain is concentrated in those markets or that the gain arises from insights without a linguistic description. Those are stronger claims than the conditional comparison specifies. [E1–E3]

### Answer to Grok: an operational threshold can be preregistered without being empirically optimal

The absence of evidence establishing 0.10 as the *right* threshold is a valid limitation. It does not make a prospectively fixed threshold and test unfalsifiable. The proposed conditional claim—positive mean Brier improvement under a specified selection and weighting rule—has an identifiable failure condition. Requiring the subset to clear the primary margin and repeat every primary gate would define a stronger secondary claim; it is not necessary merely to make the conditional claim falsifiable. [E2–E3, E5]

However, **0.10 is an operational convention**. Evidence that it is optimal, that it will select adequate support, or that the expected Brier effect makes this test well powered: **no evidence in briefing**. That limitation must remain visible in reporting. [E2–E3, E6–E7]

### Answer to Gemini: selection by forecasts limits the claim; it does not automatically invalidate it

The selected set is determined by the arms’ outputs. But both arms’ forecasts are available for the same selected markets, and both losses are evaluated against the same outcomes. A rule fixed before forecasts can therefore define a **conditional predictive-performance comparison**. Its result concerns that jointly selected set; it does not establish an effect *caused by disagreement* or an advantage in an independently defined subgroup. [E2–E3]

The distinction is between **prespecifying the conditional question** and choosing a favorable question after seeing results. The protocol must freeze the cutoff and aggregation, retain the resulting eligibility during resampling, and report inadequate or empty support without changing the threshold. Output-dependent selection alone does not prove that every interval for this conditional target is invalid. [E2–E3]

I would not replace it with option (c). A positive covariance or slope tests whether larger disagreements are associated with larger improvements under the chosen aggregation. It does not establish how much of the primary gain comes from a specified subset. Moreover, E3’s covariance expression needs an explicit group-level disagreement measure before it is executable: market-level probability gaps and group-level Brier differences are not yet a fully specified pair of group statistics. [E1–E3, E5]

**Under choice (b), E1’s concentration clause remains unestablished by this secondary test.** It must remain a research question, rather than become part of the claim licensed by a passing result. E3 already identifies the additional comparison or decomposition that a concentration claim would require. [E1, E3]

## Q2 — Retain 0.10 in probability units, and correct the earlier scaling objections

I choose fixed 0.10 because it directly defines **absolute disagreement of ten percentage points**. This is a choice about what to measure, not a finding that relative disagreement is unimportant or that either alternative is statistically inferior. [E2–E3]

| Proposed definition | What determines selection? | Uses the realized outcome? |
|---|---|---|
| \(\lvert p_L-p_T\rvert\ge0.10\) | The absolute difference between the two forecasts. | **No.** [E2] |
| \(\lvert\operatorname{logit}(p_L)-\operatorname{logit}(p_T)\rvert\ge\delta_{\text{logit}}\) | Their distance on the log-odds scale. | **No.** [E3] |
| \(\lvert p_L-p_T\rvert/\sqrt{\bar p(1-\bar p)}\ge0.25\), with \(\bar p=(p_L+p_T)/2\) | Their absolute difference scaled using their midpoint. | **No.** [E3] |

**None of these three formulas is disqualified by outcome-based selection.** Scaling by a group’s *realized YES rate* would be a different procedure: outcomes would then influence which forecasts qualify. That earlier objection does not apply to Gemini’s forecast-midpoint formula. [E2–E4]

I also correct the earlier “whose forecast?” objection: **Gemini explicitly answers that question by using both forecasts’ midpoint.** Its denominator is largest at 0.5, so its rule requires a larger absolute gap near 0.5 than near the boundaries. The previous warning about admitting very small differences near 0.5 does not describe this particular formula. [E3]

The alternatives still require complete specification. Logit distance needs a rule for forecasts equal to zero or one; midpoint scaling needs a convention when both forecasts equal the same boundary and the expression becomes \(0/0\). These are mathematical specification issues, not outcome contamination. [E3]

E4’s outcome balance does not determine which definition is preferable. It reports realized market outcomes, including multiple slices of events; it does not establish where the forecasts lie, whether they are calibrated, or the corresponding balance under equal-group weighting. Evidence for Gemini’s assertion about where most forecasts will sit: **no evidence in briefing**. Nor does the external accuracy result justify a divergence cutoff for this Brier analysis. [E3–E5, E7]

## Q3 — What a passing secondary result licenses

The exact permitted sentence is:

> **“Among markets where the latent and text forecasts differed by at least ten percentage points, latent achieved a positive mean Brier improvement under the preregistered event-and-group weighting, with nominal 95% bootstrap intervals entirely above zero under both primary-group and sensitivity-block resampling.”** [E2–E3, E5]

The sentence it does **not** license is:

> **“The overall forecasting gain is concentrated in divergent markets and demonstrates useful insights that have no clean linguistic description.”** [E1–E3]

The conditional mean neither compares the divergent subset with its complement nor measures its contribution using the original primary weights. It also does not identify the proposed mechanism. [E1–E3, E5]

**Yes, the secondary must be recomputed under sensitivity resampling.** If its primary-group interval clears zero but its sensitivity interval does not, report **“secondary claim not established under the sensitivity partition.”** Retain the estimate and both intervals; do not interpret this as proving that the conditional advantage is absent. This follows the reporting distinction adopted in E5. [E3, E5]

### Support: distinguish computability from inferential adequacy

A single eligible group or a single contributing sensitivity block cannot supply between-unit variation at that resampling level. I therefore specify **at least two eligible groups and two contributing blocks, plus finite, nondegenerate resampling distributions**, as structural requirements. This is a computability screen derived from the resampling construction—not a claim that two units provide adequate confidence-interval coverage. [E3, E5]

A validated numerical support floor, or evidence that the resulting intervals attain their nominal coverage: **no evidence in briefing**. Consequently, the permitted sentence explicitly describes **nominal bootstrap intervals**. The protocol below makes the calculation and operational success rule reproducible; it does not supply the missing validation of inferential adequacy. [E3, E6–E7]

## Q4 — Proposed v0.4 §7 text

The following paragraph implements that conditional protocol, including the structural support limitation. It is under 200 words. [E2–E7]

> Divergent markets satisfy \(|p_L-p_T|\ge0.10\), fixed before forecasts. Average T-minus-L Brier differences over divergent markets within each event, eligible events within each original group, then eligible groups equally. The claim is positive conditional improvement. Preserve original partitions. Using the primary endpoint’s interval construction, resample eligible groups and, separately, original sensitivity blocks containing eligible groups, with replacement, uniformly within each frame, drawing each frame’s observed number of units. A drawn block contributes all its eligible groups once per draw; average across entered groups. Require both nominal 95% intervals entirely above zero. Require at least two eligible groups and two contributing blocks, with finite, nondegenerate resampling distributions; this is a computability screen, not validated inferential adequacy. Otherwise report “secondary claim not established,” with the reason; never impute zero or change delta. Report selection fractions, support counts and distribution, the common estimate, both intervals, and the market-weighted share with lower L Brier, separating ties. Primary-only secondary success is “not established under sensitivity.” A secondary result never rescues primary FAIL.

## Optional — Does this add anything beyond the primary endpoint and gates?

**Yes, it adds a narrower conditional finding:** latent outperforms text within the prespecified substantial-disagreement subset. An overall improvement and overall gate results do not establish the sign of the improvement within that subset. [E2–E3, E5]

**It does not establish the motor-car mechanism in E1.** Neither this conditional mean nor the proposed covariance, on its own, demonstrates insights that lack a clean linguistic description. The project should distinguish a useful conditional performance result from proof of that stronger explanation. [E1–E3]

**Vendor: OpenAI**  
**Model: GPT-6 Astra Pro**
