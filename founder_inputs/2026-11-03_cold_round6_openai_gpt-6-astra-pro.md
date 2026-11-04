**Engine:** OpenAI. **Model:** GPT-6 Astra Pro (as self-reported). **Briefing:** 2026-11-03_cold_briefing_v6_adjudication_decision4.md. Tier 3. Filed verbatim.

## Adjudication

**Require the primary endpoint’s sensitivity interval to lie entirely above \(m\). Require Gate 2’s interval to lie entirely above zero under both primary and sensitivity resampling. E6 does not change either answer.** These choices preserve the margin claim and the separate usefulness requirement when applying the registered sensitivity analysis. [E1–E3, E5–E6]

## Q1 — What “survives” should mean

**The sensitivity analysis should retain the original threshold: above \(m\).** E1 defines the result to be established as an advantage exceeding the preregistered margin; E3 makes sensitivity survival a condition of retaining PASS. Reading “survives” as clearing that same margin preserves the substantive claim across the two resampling schemes. E1 alone does not specify the sensitivity threshold; this adjudication resolves E3’s ambiguity in favor of the explicit proposal in E2. [E1–E3]

The strongest opposing argument is that requiring the sensitivity interval to clear \(m\) can withhold PASS from a real benefit because the alternative resampling leaves insufficient precision. That is a legitimate cost of the stronger requirement. However, for the positive margin contemplated in E4, an interval entirely above zero establishes a different threshold from an interval entirely above \(m\). The additional uncertainty should change what the project claims, while preserving the positive finding it actually supports. [E2–E4]

For the specific case in the question—primary lower bound above \(m\), sensitivity lower bound above zero but at or below \(m\)—the run should report:

> **The primary-group interval establishes an improvement exceeding the preregistered margin. The sensitivity-block interval establishes a positive improvement, but does not establish that the improvement exceeds that margin. The overall result is FAIL: the required advantage was not established under the registered sensitivity analysis.** [E1–E3]

The report should show the common point estimate and both intervals. This outcome licenses the project to claim **positive superiority under both registered resampling schemes**, and **margin-exceeding superiority under primary-group resampling**. It does not license the full claim that the margin survives sensitivity, nor does it establish that the advantage is absent. This is consistent with E2’s stated meaning of FAIL. [E1–E3]

Calling the effect “true-but-small” supplies a hypothetical truth that the interval pattern itself does not determine. The actual Brier effect size, and how often this reporting pattern would occur: **no evidence in briefing**. E7 explicitly says the expected Brier effect here is unknown; its accuracy figures do not resolve this question. [E4, E7]

**E6 does not change my answer from round 5.** It removes links through an event’s secondary tags and splits the Iran driver, changing the construction behind the objection about overly broad blocks. It does not change the promised margin or the requirement that PASS survive sensitivity. Whether those changes materially narrow the resulting intervals: **no evidence in briefing**. The decision rests on maintaining the claim’s threshold, not on predicting the resulting precision. [E1–E4, E6–E7]

## Q2 — Must Gate 2 also survive sensitivity?

**Yes. The argument for retaining a separate sensitivity requirement is correct. Neither proposed substitute establishes the required interval result for \(L\) versus \(S\).** [E2–E3, E5]

The algebra explains both the appeal and the limitation of the redundancy argument. For each primary group, define:

\[
d_g=\operatorname{Brier}_T(g)-\operatorname{Brier}_L(g),
\qquad
c_g=\operatorname{Brier}_S(g)-\operatorname{Brier}_T(g).
\]

Then the Gate 2 contrast is exactly:

\[
\operatorname{Brier}_S(g)-\operatorname{Brier}_L(g)=d_g+c_g.
\]

This identity holds for the observed equal-weight means and within each bootstrap resample when the same block draws are used for the contrasts. [E2]

Consequently, requiring the **observed** mean \(\bar c\ge0\) ensures that the observed \(S-L\) advantage is at least the observed \(T-L\) advantage. It does **not** ensure the same ordering throughout the sensitivity resampling distribution. Some blocks can have negative \(S-T\) contrasts even when the overall mean is nonnegative; resampling those blocks changes their contribution. Therefore, the proposed mean condition does not guarantee that the lower bound of the sensitivity interval for \(S-L\) remains above zero. This follows from E2’s resampling rule and directly addresses the substitute proposed in E5. [E2, E5]

The strongest part of the opposing argument is its conditional algebra: **if the true mean loss of \(T\) is no greater than that of \(S\), then a true advantage of \(L\) over \(T\) implies a true advantage over \(S\).** But that conditional relationship does not make the specified sample interval gate automatically pass. The proposed observed-mean condition supplies no such interval guarantee. An established guarantee that text cannot worsen performance: **no evidence in briefing**. [E2, E5]

Moreover, E2 does not give \(T\) and \(S\) identical information. \(T\) receives A’s text draft; \(S\) receives no message. Sharing a checkpoint and prompt text therefore does not establish an ordering of their Brier losses. Text performing worse than silence remains an unclosed possibility, and aggregate non-harm in the observed means would still leave the uncertainty issue above. [E2, E5]

Keeping Gate 2 only at the primary level likewise does not close the issue: it establishes the usefulness requirement under primary-group resampling, while leaving its survival under sensitivity unresolved. E2 explicitly distinguishes those two resampling schemes and requires both gate results to be reported. [E2–E3, E5]

**What the stronger choice licenses:** a passing run can say that its advantage over the single-agent floor satisfies the registered positive-interval requirement under both resampling schemes. Under the weaker choice, it can say that usefulness passes under primary groups, but cannot necessarily say that usefulness survives the sensitivity analysis. The separate \(L-T\) endpoint cannot supply that missing result merely because its own interval clears \(m\). [E2–E3, E5]

**E6 does not change this answer.** Changing the block construction does not establish the missing relationship between the \(S-T\) and \(S-L\) resampling distributions. It can affect the eventual gate result; it does not make the gate logically redundant. [E2, E5–E6]

## Optional — Wording that leaves the weaker interpretation open

**Yes. E2 currently leaves open an overall PASS whose primary endpoint clears \(m\) under both schemes while a gate clears zero only under primary resampling.** The relevant sentence is:

> “Whether a gate must also survive sensitivity to count as met is open; the primary endpoint must.” [E2]

The later PASS definition simply says “AND Gate 1, AND Gate 2,” while E3 explicitly describes recomputation of the primary endpoint. Together, those passages leave the gate requirement unresolved. [E2–E3]

Replace the open sentence with:

> **“Each gate counts as met only if its 95% interval lies entirely above zero under both primary-group resampling and sensitivity-block resampling.”**

Also replace the gates heading’s “both 95% group-bootstrap intervals” with **“each evaluated using 95% intervals under both primary-group and sensitivity-block resampling,”** and make the PASS conjunction refer explicitly to gates meeting that definition. These edits implement the adjudication and remove the primary-only interpretation. [E2–E3, E5]

**Vendor: OpenAI**  
**Model: GPT-6 Astra Pro**
