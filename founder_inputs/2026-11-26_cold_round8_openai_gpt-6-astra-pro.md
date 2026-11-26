**Engine:** OpenAI. **Model:** GPT-6 Astra Pro (as self-reported). **Briefing:** 2026-11-26_cold_briefing_v8_margin_m.md. Tier 3. Filed verbatim.

## Decision

**Choose (a): the Founder fixes a numerical \(m\), in absolute group-averaged Brier units, as the smallest improvement worth claiming. Record it as a governance judgment and freeze it before S, T, L or D runs.** This follows the governance precedent in E1 and the smallest-worthwhile-improvement proposal in E4, while removing the discretionary hurdle identified in E4 and E7. [E1] [E2] [E4] [E6] [E7]

## Q1 — When must \(m\) be fixed?

**Running S before either the numerical margin or its complete deterministic rule has been fixed is unacceptable for the final method I recommend.** A fully specified rule may be evaluated later, but the later calculation must leave no human choice about the resulting margin. [E4] [E7]

There is a textual distinction here: **E1 says “at pre-registration”; it does not expressly say “before S.”** E2 places pre-registration after the S/BR noise estimate. Thus, the requirement to commit before every model arm is the resolution I recommend from reading E1 together with E4’s exposure objection and E7’s history—not wording already present in E1 alone. [E1] [E2] [E4] [E7]

The commitment must therefore precede **S, T, L and D**, all of which require a model run. Under a completely frozen S-dependent formula, the *numerical value* could be calculated after S; the *choice of how to obtain that value* could not. Freezing only a multiplier while leaving “spread” undefined would retain discretion. [E2] [E4] [E6] [E7]

### What can be learned before the margin is set?

| Source | What a human can learn | Can that learning determine or move \(m\)? |
|---|---|---|
| **S** | Agent B’s actual errors against the confirmatory outcomes, including its group scores and, with BR, the S−BR differences. E4 specifically identifies exposure to the exact single-agent and base-rate errors. [E2] [E4] [E6] | **It must not inform a later discretionary choice.** It may determine the numerical value only through a complete rule committed before S runs. That addresses the timing problem; it does not validate the rule’s statistical meaning. [E4] [E7] |
| **BR** | The leave-group-out constant forecast’s performance on already-known outcomes, including the scale of its Brier error. The weighting definition affects that calculation. [E2] [E4] [E6] | It can supply the input to a declared fraction-of-BR rule. The fraction and calculation must be committed, rather than adjusted after inspecting the score to obtain a preferred hurdle. Once registered, the margin cannot be reopened. [E4] [E7] |
| **C** | How the saved crowd prices scored against the resolved outcomes. This is arithmetic on existing data. [E2] [E6] | E2 assigns C a reporting role and says it is “not a target.” For a rule allowing C to determine \(m\): **no evidence in briefing**. Its score cannot justify revising the registered margin. [E2] [E7] |

**BR and C differ operationally from S:** calculating them requires no model run. I would not impose an additional requirement that their arithmetic remain unseen until registration; neither E1 nor E6 supplies that requirement, and E6 expressly says the outcomes are already known. But existing-data arithmetic does not eliminate the risk of choosing a convenient hurdle after inspecting a score. [E1] [E4] [E6] [E7]

Under the selected governance rule, BR/C may be available as context before registration, but the numerical margin is recorded as the Founder’s value judgment. Neither baseline results nor subsequent model results can reopen it. This is an explicit commitment, not a claim that the Founder is blind to the pool’s outcomes. [E1] [E4] [E6] [E7]

## Q2 — Candidate rules

### (a) A governance number — preferred

**What it protects against.** A number fixed before model runs removes the opportunity to choose the hurdle in response to observed model performance. Recording it as the smallest worthwhile improvement also separates the value of an advantage from the experiment’s measured noise. E1 item 9(b) provides the precedent for openly identifying a threshold as governance rather than evidence-derived. [E1] [E4] [E7]

**What it leaves open.** The Founder must defend why that improvement matters. Calling the number governance does not supply an empirical derivation, establish adequate power, or assure that the experiment will pass. E3 expressly permits a result that clears zero but fails to clear the required margin. [E1] [E3] [E4]

**Pre-registrability.** This is pre-registrable **as a method using the briefing alone**; no preliminary model run or noise conversion is needed. A completed registration still requires the Founder’s signed numerical choice. For that numerical value: **no evidence in briefing**. [E1] [E4] [E5]

### (b) A fixed fraction of BR’s Brier

The proposed form is:

\[
m=q\,\mathrm{Brier}_{BR},
\]

with the fraction \(q\) and the exact BR scoring calculation fixed in advance. Its input is computable from frozen data without running S or another model. [E4] [E6]

**What it protects against.** With the coefficient and calculation committed, the rule prevents discretionary selection from subsequent model results and makes the relationship between the baseline score and the hurdle explicit. [E4] [E6] [E7]

**What it leaves open.** The fraction remains a choice: the formula does not explain why that fraction represents an improvement worth claiming. It also makes the absolute margin depend on BR’s performance; it does not establish the expected T−L effect or adequate power. [E4] [E5]

**Pre-registrability.** It is pre-registrable in principle, but it is **not an executable specification as supplied**. It needs the fraction and an unambiguous BR calculation using the primary weights. E4 supplies a proposed clarification for the leave-group-out rate; evidence that this clarification has been incorporated into E2 is **no evidence in briefing**. The numerical fraction is also **no evidence in briefing**. [E2] [E4]

### (c) A fixed multiplier of the S−BR spread

**What it protects against.** A completely frozen function can prevent a human from selecting the margin after seeing S. The resulting number may be calculated after S without changing the earlier commitment. [E4] [E7]

**What it leaves open.** Determinism does not resolve the wrong-noise objection. E4 says that S−BR and T−L involve different forecasts and covariance structures. Consequently, fixing a multiplier does not make the S−BR spread an established measure of T−L noise or evidence of adequate power. [E4]

**Pre-registrability.** It is mechanically pre-registrable once fully specified, but **“fixed multiplier of the spread” is incomplete as supplied**. The multiplier must be chosen, and “spread” must identify an exact statistic and calculation; Gemini’s standard-error expression is presented as an example, not an adopted specification. For the chosen multiplier and final statistic: **no evidence in briefing**. For a validated conversion from S−BR noise to T−L noise: **no evidence in briefing**. [E2] [E4]

The objection is therefore not that this rule is impossible to pre-register. It is that pre-registering it would remove one source of discretion without establishing its relevance to either the worthwhile effect or the primary contrast’s uncertainty. [E4] [E7]

### (d) Another rule, in one sentence

I would put no fourth rule ahead of (a), because the briefing supports declaring a minimum worthwhile improvement but supplies no empirical conversion that could determine it. [E1] [E4] [E5]

**None of (a)–(c) is a completed numerical registration in the blocks.** Rule (a) needs the acknowledged governance choice; (b) additionally needs the exact baseline calculation; (c) needs the exact spread calculation and still lacks support for its proposed noise interpretation. [E1] [E2] [E4] [E5]

## Q3 — What is \(m\) for?

**\(m\) is the minimum advantage required for the project’s substantive claim, expressed as a value choice—not an estimate of the advantage expected.** E3 makes that distinction operational: clearing zero is insufficient; the primary interval must clear \(m\) under both resamplings, with the other PASS requirements also satisfied. E4’s “smallest worthwhile improvement” is the appropriate interpretation for the selected rule. [E3] [E4]

E5 can be recorded as limited background and as a reason to acknowledge uncertainty about transfer to this task. It cannot provide a numerical Brier margin, establish that the expected Brier effect is small, or support a power calculation. E5 explicitly says the expected effect in Brier here is unknown. For a conversion from its QA accuracy points to this pool’s Brier improvement: **no evidence in briefing**. [E4] [E5]

Saying **“\(m\) should be small because the expected effect is small”** invites the **Pro-Thesis Optimization Loop** failure shape: selecting the success criterion to accommodate the result one hopes to obtain. Fixing that criterion before running the experiment would remove later movement, but would not make the value justification sound. This identifies a risk in the reasoning, not evidence that an actual post-result adjustment has occurred. [E4] [E5] [E7]

The Founder may independently decide that a small improvement is worth claiming. The registration should identify that as the Founder’s judgment, without presenting it as an empirical consequence of Draft-KV. [E1] [E4] [E5]

## Q4 — Replacement for E2 §9

> **§9. Margin and power.** The Founder records numerical m, an absolute reduction in group-averaged Brier, at pre-registration before S, T, L or D runs. [E1] [E2] [E4] [E6] [E7]
>
> BR and C may be calculated beforehand; neither can reopen the registered choice. [E2] [E6] [E7] S and BR may support baseline and feasibility checks; L must still beat BR. [E3] [E4] The S−BR spread is not established as T−L noise or evidence of adequate power. No arm result may change m. [E4] [E7]
>
> The Founder signs: **“I choose m = [value] Brier units as the smallest improvement worth claiming; this is my governance judgment, not a value derived from arm results or Draft-KV’s accuracy gains.”** [E1] [E4] [E5]

The numerical placeholder requires the Founder’s choice; for a value to insert, **no evidence in briefing**. [E1] [E4] [E5]

## Optional — Can the margin or noise estimate rescue a FAIL?

**No.** E2 already requires the margin before any T or L forecast. E3 requires the *pre-registered* margin and explicitly labels an interval that clears zero but not \(m\) as a FAIL. Neither provision authorizes revising \(m\), or changing the noise estimate, to convert that outcome into a PASS. [E2] [E3]

The defect to replace is E2 §9’s provision that places margin selection **after the noise estimate**, together with its use of S−BR as the operative noise estimate for margin and power. E3’s PASS rule needs no change for this decision. [E2] [E3] [E4] [E7]

**Vendor: OpenAI**  
**Model: GPT-6 Astra Pro**