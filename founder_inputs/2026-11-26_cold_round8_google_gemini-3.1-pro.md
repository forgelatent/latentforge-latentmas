**Engine:** Google. **Model:** Gemini 3.1 Pro (as self-reported). **Briefing:** 2026-11-26_cold_briefing_v8_margin_m.md. Tier 3. Filed verbatim.

**Q1 — When must m be fixed?**

* **Running S before fixing m:** Running S (a model arm) before $m$ or a deterministic formula for it is fixed is not acceptable. E1 explicitly mandates that "[t]he margin and the budget rule are set at pre-registration, not after" [E1], and E7 treats any hurdle that can be chosen or moved after results are visible as a known failure shape [E7]. While E2 §9 attempts to define pre-registration as occurring after the S and BR noise estimate and before T or L [E2], running S on the confirmatory pool exposes the exact single-agent Brier error on resolved ground truth, allowing a human to choose a small $m$ after seeing the number [E4]. Therefore, $m$ (or a rigid deterministic formula for it) must be fixed before *any* model arm (S, T, L, or D) runs [E1, E4, E6].
* **BR and C:** The answer differs for BR and C because neither involves running a model; their Brier scores are static arithmetic on frozen pool data and settlement prices that already exist [E6]. However, because outcomes are already known on the frozen pool [E6], any rule relying on BR or C must still be frozen before computing or inspecting those scores to prevent post-hoc threshold tuning [E4, E7].
* **What a human learns and how it can move m:**
* **From S:** The human learns the exact single-agent Brier score and per-group error spread on the confirmatory test set [E4]. Without a frozen deterministic formula, a human can pick a low $m$ tailored to look achievable relative to S's baseline performance or variance [E4].
* **From BR:** The human learns the group-weighted base-rate Brier score on the frozen pool [E4, E6]. If $m$ is set after seeing BR without a pre-committed fraction, the human can scale $m$ downward to make clearing the hurdle easier [E4, E7].
* **From C:** The human learns the Brier score of the final pre-resolution Polymarket crowd price on the frozen pool [E2, E6]. Seeing how hard the market crowd is to beat—or the gap between BR and C—could tempt a human to lower $m$ if $m$ is not already locked [E7].



**Q2 — Candidate rules**

* **(a) Governance number:**
* *Protects against:* Eliminates all dependence on confirmatory pool results, model runs (S), or invalid noise proxies, completely preventing post-hoc threshold manipulation [E4, E7].
* *Leaves open:* Requires an arbitrary human value judgment with no empirical Brier calibration on this task [E1, E5].
* *Pre-registrability:* **Pre-registrable as written in the blocks**, following the exact governance precedent established in E1 item 9(b) [E1].


* **(b) Fixed fraction of BR's Brier:**
* *Protects against:* Prevents any model arm (S, T, L, D) from influencing $m$ and scales the hurdle proportionally to the pool's baseline uncertainty before models run [E4, E6].
* *Leaves open:* Because BR's Brier is already computable on the frozen pool [E6], inspecting BR before locking the fraction allows a human to tune the fraction to yield a desired $m$ [E4, E7]. Furthermore, E2 §4's definition of BR ("pool's YES rate") is currently ambiguous regarding group/event weights [E4].
* *Pre-registrability:* **Needs something the blocks do not contain**—specifically, the chosen fraction itself and an amended, group-weighted definition of BR [E4].


* **(c) Fixed multiplier of the S − BR spread:**
* *Protects against:* Prevents post-hoc discretionary selection of $m$ *after* S runs, provided the multiplier $k$ is locked beforehand [E4].
* *Leaves open:* Measures the wrong noise—the spread of single-agent minus base-rate errors has different forecasts and covariance structures than the primary T-minus-L contrast, so it cannot verify statistical power [E4].
* *Pre-registrability:* **Needs something the blocks do not contain**—the numerical multiplier $k$ is missing from the blocks [E2, E4].


* **(d) Preferred alternative:** No other rule is ahead of (a); using a direct governance number in Brier units is the cleanest pre-registrable choice because no external Brier effect size exists [E5] and proxy noise spreads are structurally mismatched to the T-minus-L contrast [E4].

**Q3 — What m is for**

* **Purpose of m:** $m$ is the *smallest effect worth claiming* (a value/governance choice), not an empirical forecast of expected effect [E1, E4]. E5 explicitly states that the expected effect size in Brier on this pool is unknown [E5].
* **Bearing of E5:** E5 cannot validly set or derive $m$ because Draft-KV reports accuracy points (+2.1 mean, −0.1 to +3.8 range without error bars) on a QA benchmark under shared input, which has no conversion to Brier score reductions on Polymarket events [E2, E4, E5]. At most, E5 serves as contextual background confirming that channel gains in prior literature are modest [E2, E5].
* **Failure shape invited:** Saying "$m$ should be small because the expected effect is small" invites the **"Pro-Thesis Optimization Loop"** from E7 [E7]. Designing the hurdle around an assumed small effect tailors the pass criterion to guarantee a favorable verdict regardless of practical significance, echoing the prior benchmark failure where hurdles were shaped so no result could be unfavorable [E7].

**Q4 — Text**

> **§9. Margin and power.** $m$ is an absolute reduction in group-averaged Brier under section 7's definition, fixed at pre-registration before any model arm (S, T, L, or D) runs and before computing or inspecting BR or C scores on the frozen pool. No calibration slice is used; the full eligible pool is the confirmatory set. Arms S and BR are used strictly as baseline and feasibility checks, not to set $m$ or estimate statistical power for the T-minus-L contrast.
> *Governance record:* The pre-registered margin is $m = \text{[Founder value]}$ Brier units, chosen by the Founder as a governance rule representing the smallest improvement worth claiming, not derived from pool data or E5.

**Optional**

* In **E2 §9**, the phrase *"set at pre-registration after the noise estimate below and before any T or L forecast"* allows $m$ to be chosen after running S and BR on the confirmatory pool, creating a window to set a low $m$ after seeing baseline error spreads [E2, E4].
* In **E3**, nothing permits revising $m$ or the noise estimate after T or L has been seen; E3 explicitly locks the verdict categories so that a primary interval clearing zero but not $m$ is a FAIL with its own label [E3].

**Filing.** Vendor: Google Model: Gemini 3.1 Pro