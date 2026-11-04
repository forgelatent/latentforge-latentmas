**Engine:** Google. **Model:** Gemini 3.1 Pro (as self-reported). **Briefing:** 2026-11-03_cold_briefing_v7_adjudication_decision5.md. Tier 3. Filed verbatim.

### Q1 — Adjudication of the Secondary Endpoint

**Verdict: Option (a) — Drop the formal inferential secondary endpoint; report disagreement descriptively only [E3].**

**Addressing the objections from (b) and (c):**

1. **Why Option (b) (GPT-6 Astra Pro's thresholded protocol) cannot stand:**
As Gemini 3.1 Pro noted in Round 5, the subset of markets where $\vert{}p_L - p_T\vert{} \ge 0.10$ is a post-treatment conditioning set determined entirely by the models' outputs [E2, E3]. Because the subset size is a random variable that can be empty or sparse, Option (b) requires inventing a pre-registered "support rule" specifying minimum eligible groups and sensitivity blocks [E3]. Yet GPT-6 Astra Pro explicitly concedes: *"No evidence in briefing supplies a justified numerical minimum"* [E3], and both Grok 4.7 and GPT-6 Astra Pro confirm that *"no evidence in briefing"* justifies $\delta = 0.10$ [E3]. Pre-registering an arbitrary cutoff paired with an arbitrary support floor creates an unprincipled hurdle that still fails to prove concentration (as GPT-6 Astra Pro admits, a conditional mean on divergent markets *"would not establish that the overall gain is concentrated there"* without a separate contrast against non-divergent forecasts or a primary-weight decomposition) [E3].
2. **Why Option (c) (Gemini 3.1 Pro's unconditional covariance/slope test) cannot stand:**
While Option (c) avoids post-treatment subset selection, it fails both algebraically and conceptually. Under the Brier score, for any single market with outcome $y \in \{0, 1\}$, the paired Brier improvement is:

$$d_m = (p_T - y)^2 - (p_L - y)^2 = (p_T - p_L)(p_T + p_L - 2y)$$



Thus, $\vert{}d_m\vert{} = \vert{}p_L - p_T\vert{} \cdot \vert{}p_T + p_L - 2y\vert{}$. Because $\vert{}p_L - p_T\vert{}$ is a direct multiplicative factor of the magnitude of $d_m$, whenever the primary endpoint is positive ($L$ is better calibrated than $T$ on average) [E5], markets with tiny $\vert{}p_L - p_T\vert{}$ are mathematically forced to have $d_m \approx 0$, while larger gains *must* come from markets with larger $\vert{}p_L - p_T\vert{}$. A positive slope or covariance $\text{Cov}_g(\vert{}p_L - p_T\vert{}, d_g) > 0$ is therefore a near-tautological mechanical consequence of a primary PASS under a quadratic scoring rule, not an independent test of "insights that exist in the geometry of the data" [E1, E3]. Furthermore, as GPT-6 Astra Pro points out, a continuous slope changes the question rather than testing whether the primary gain is concentrated in a distinct regime of disagreement [E1, E3].

**What E1's "concentrated where the two disagree" clause becomes under (a):**
Because $d_m \equiv 0$ whenever $p_L = p_T$, **100% of any non-zero Brier difference is already mathematically generated where the two arms disagree** [E2]. Under Option (a), the clause *"and is the gain concentrated where the two disagree?"* in [E1] ceases to be a separate inferential gate and becomes a **descriptive decomposition of the primary endpoint** (reporting the empirical distribution of $\vert{}p_L - p_T\vert{}$, the share of divergent markets where $L$ is closer to the outcome than $T$, and how the primary Brier gain partitions across disagreement levels) [E1, E2, E3].

---

### Q2 — The Threshold Itself

Because Option (a) is selected, **no inferential threshold is retained** [E3]. If evaluated on the merits of the Round 5 exchange for descriptive reporting:

* **Do any of the three thresholds use a realized outcome?**
**No.** Fixed $\delta = 0.10$ uses $\vert{}p_L - p_T\vert{}$; the logit threshold uses $\vert{}\text{logit}(p_L) - \text{logit}(p_T)\vert{}$; and Gemini 3.1 Pro's uncertainty scaling uses $\bar{p} = (p_L + p_T)/2$ to compute $\vert{}p_L - p_T\vert{} / \sqrt{\bar{p}(1-\bar{p})}$ [E3]. None of these three formulas inputs the realized resolution $y \in \{0,1\}$ [E3].
* **Adjudicating GPT-6 Astra Pro's two objections against E4's outcome balance:**
1. *Outcome-selection objection:* GPT-6 Astra Pro objected to scaling by *"the group's realized YES rate"* because that lets outcomes select the subset [E3]. That objection is completely valid and **disqualifies** any threshold based on realized pool or group base rates (such as the 80.2% NO / 19.8% YES rate in [E4]). However, Gemini 3.1 Pro's formula scales by the *forecast average* $\bar{p} = (p_L + p_T)/2$, not the realized outcome, so it is not disqualified by outcome leakage [E3].
2. *Whose-forecast and Brier-geometry objection:* GPT-6 Astra Pro's second objection—that Brier scoring is strictly proper in raw probability units and does not give $0.5$ or boundary log-odds a privileged role, and that scaling by $\sqrt{\bar{p}(1-\bar{p})}$ requires an arbitrary choice of whose forecast defines $\bar{p}$—is **correct** [E3]. In Brier space, a shift from $0.02$ to $0.11$ and a shift from $0.45$ to $0.54$ represent the exact same $\vert{}\Delta p\vert{} = 0.09$ linear factor in the Brier difference identity. Therefore, if a descriptive reference line is displayed alongside the continuous distribution, a fixed probability difference (such as $\vert{}p_L - p_T\vert{} \ge 0.10$) is the only scale-consistent choice in Brier space, even though its specific value ($0.10$) has no evidential basis in the briefing [E2, E3].



---

### Q3 — What Option (a) Licenses

* **What a passing run licenses the project to say:**
Because Option (a) drops the secondary pass/fail test, a run that passes the primary endpoint and both gates [E5] is licensed to state the exact descriptive facts: *"Across the pool, latent and text forecasts differed by an average of $X$ probability points (with $Y\%$ of markets showing $\vert{}p_L - p_T\vert{} \ge 0.10$, on which $L$ was closer to the outcome than $T$ in $Z\%$ of cases), accounting for $W\%$ of the primary group-weighted Brier gain"* [E2, E3].
* **What it does NOT license the project to say:**
It does **not** license the project to claim that *"useful divergence was independently established as a separate inferential endpoint"* or that *"a pre-registered threshold of $\delta = 0.10$ represents a validated boundary of non-linguistic insight"* [E1, E3].
* **Sensitivity recomputation and "not established" status:**
Under Option (a), no inferential hypothesis test is attached to the secondary summary, so there is no secondary PASS/FAIL label to become "not established" [E3, E5]. However, if any descriptive intervals are reported for disagreement slices, both the primary-group and sensitivity-block bootstrap intervals [E5, E6] should be displayed for transparency, and per [E5], no descriptive divergence summary can ever rescue a primary FAIL [E3, E5].

---

### Q4 — Pre-registration Text (for v0.4 §7)

> **Disagreement reporting (descriptive only; replaces the v0.3 secondary endpoint):** For every market, record the absolute forecast difference $\vert{}p_L - p_T\vert{}$, the paired Brier difference $\text{Brier}_T - \text{Brier}_L$, and whether $L$ is closer to the realized outcome than $T$; report the unconditional distribution of $\vert{}p_L - p_T\vert{}$ across markets and groups, the decomposition of the primary group-weighted Brier gain across disagreement deciles and above a descriptive reference line of $\vert{}p_L - p_T\vert{} \ge 0.10$, without any secondary pass/fail gate or ability to rescue a primary FAIL.

*(Word count: 84 words; single-sentence descriptive reporting line per Q4 instructions.)*

---

### Optional — Does Any Version License More About "Useful Divergence" [E1] Than Primary + Gates [E5]?

**No — none of the three versions does, and we should say so plainly.**

Here is why, grounded strictly in [E1], [E2], and [E5]:

1. **What Primary + Gate 1 + Gate 2 [E5] already establish:**
In all arms, Agents $A$ and $B$ use the exact same model checkpoint and prompt text [E2 in v6 / E1]. In arm $T$, Agent $A$ sends text; in arm $L$, Agent $A$ sends latent states; in arm $D$, the latent states are deranged; in arm $S$, Agent $B$ receives nothing [E1, E5]. If a run clears the primary endpoint ($L$ beats $T$ by more than $m$ under both primary and sensitivity resampling), clears Gate 1 ($L$ beats deranged control $D$), and clears Gate 2 ($L$ beats isolated receiver $S$) [E5], it has *already* proven that task-relevant, non-redundant predictive information was transmitted through the latent geometry that outperformed linguistic text communication ($T$) and improved upon standalone forecasting ($S$) [E1, E5].
2. **Why a divergence secondary endpoint adds zero additional proof of [E1]'s motor-car claim:**
As noted in Q1, wherever $p_L = p_T$, the paired Brier difference is identically zero ($\text{Brier}_T - \text{Brier}_L = 0$). Any positive advantage of $L$ over $T$ established by the primary endpoint **necessarily and exclusively comes from markets where $p_L \neq p_T$** [E2]. Conditioning on $\vert{}p_L - p_T\vert{} \ge \delta$ (Option b) or correlating $\vert{}p_L - p_T\vert{}$ with $d_g$ (Option c) does not inspect the *representation* to verify whether an insight lacked a "clean linguistic description" [E1]; it merely slices or re-weights the exact same probability outputs $p_L$ and $p_T$ that the primary endpoint already scored [E2, E3]. Therefore, no statistical filter on $\vert{}p_L - p_T\vert{}$ can license a substantive claim about "useful divergent thinking" [E1] beyond what a primary PASS and Gates 1–2 [E5] already prove.

---

**Filing.** Vendor: Google Model: Gemini 3.1 Pro
