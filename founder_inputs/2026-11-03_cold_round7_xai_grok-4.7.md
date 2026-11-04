**Engine:** xAI. **Model:** Grok 4.7. **Briefing:** 2026-11-03_cold_briefing_v7_adjudication_decision5.md. Tier 3. Filed verbatim.

**Q1.** (a) Drop the secondary endpoint; report disagreement descriptively only.

Gemini’s strongest objection [E3] is that a fixed threshold distorts the 19.8 % YES rate and that an unconditional covariance avoids post-treatment selection. That objection is correct about the fixed-threshold version, but it does not rescue the secondary claim. A positive slope of \(|p_L - p_T|\) against \(d\) over the full sample answers a different question (“larger disagreements tend to co-occur with larger Brier gains”) and does not establish that “the gain is concentrated where the two disagree” [E1]. GPT-6’s protocol makes the conditional claim pre-registrable yet still conditions on a post-treatment set whose size is unknown and can be zero [E3, E6]. Because three rounds supplied no evidential basis for any delta and the primary endpoint plus gates already decide the claim in E1 [E5], the secondary endpoint is not pre-registrable as a pass/fail item.

Under (a), E1’s “concentrated where the two disagree” clause becomes a descriptive observation that may be reported after the fact; it is no longer part of the scored claim.

**Q2.** Not applicable (option (a) keeps no threshold).  
For the record: a fixed 0.10 uses no outcome; logit difference uses no outcome; Gemini’s \(\sqrt{\bar{p}(1-\bar{p})}\) scaling uses the forecasts themselves (post-treatment) but not the realized resolution. Only scaling by a realized YES rate would let the outcome select the subset. None of the three is disqualified on outcome-leakage grounds alone; they are disqualified by the absence of any pre-registered, falsifiable success criterion that matches E1 [E3].

**Q3.** A passing secondary result is not defined.  
The project may say: “On the markets where the two arms differed by at least X in probability, the mean group-level Brier difference was Y (descriptive).” It may not say: “The gain is concentrated where the two disagree” or any sentence that treats the secondary figure as establishing the claim in E1. No recomputation under sensitivity is required because no claim is made. A descriptive number that looks different under sensitivity is simply reported as such; it is not labelled “not established.”

**Q4.**  
Descriptive reporting only: after the primary analysis, report the distribution of \(|p_L - p_T|\) across markets and the mean of \(d_g\) on the subset of markets (if any) where \(|p_L - p_T| \ge 0.10\), with the count of such markets and groups; no interval is treated as a success criterion, and the figure cannot alter the PASS/FAIL outcome of the primary endpoint or gates.

**Optional.** No version of the secondary endpoint, including the one chosen, lets a run claim something about “useful divergence” [E1] that the primary endpoint and gates [E5] do not already license. The primary result already decides whether latent beats text by more than \(m\) under both dependence structures; any statement about concentration of that gain remains descriptive.

**Filing.** Vendor: xAI Model: Grok 4.7
