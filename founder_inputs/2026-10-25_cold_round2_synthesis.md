# Cold round 2 synthesis — scoring rule CANDIDATE v0.1 (October 25, 2026)

**Status:** Systems Engine synthesis of three cold readers; Tier 3. Readers (vendor, model): Google Gemini 3.1 Pro; xAI Grok 4.7; OpenAI GPT-6 Astra Pro (self-reported). A second Gemini model was not run. Briefing: `founder_inputs/2026-10-25_cold_briefing_v2_scoring_rule.md` (commit `82ae643`); answers filed verbatim as `founder_inputs/2026-10-25_cold_round2_*.md`. Rule under review: `founder_inputs/2026-10-25_useful_divergence_scoring_rule_CANDIDATE.md` (commit `11439d8`). v0.2 not yet written.

## 1. Hallucination check
None found. Every citation in all three answers lands on a real E-block or rule section. Two arithmetic claims verified: 81 YES across 291 events means at least 210 events hold no winning slice in the pool (ChatGPT); under mean-over-markets scoring, an all-zero forecast on an event with K exclusive slices scores 1/K (ChatGPT).

## 2. Unanimous (3 of 3) — adopt in v0.2
- **Q2:** drop the 41-event calibration slice. Use the full eligible pool after leakage exclusions. Estimate the noise of d_e for the margin from arms that do not involve the channel (S, BR), which cost no events.
- **Q4:** the D-vs-L gate alone is insufficient; a harmful mismatch passes it with no benefit from the correct message (ChatGPT's example: outcome NO, L = S = 0.20, D = 0.80; swap gain +0.60, benefit over S zero). Require two 95% bootstrap intervals: mean(Brier_D - Brier_L) > 0 AND mean(Brier_S - Brier_L) > 0. Keep Brier; do not convert to accuracy.
- **Optional:** "Void is not fail" is an escape hatch. Void only for execution or protocol failure (information rule broken, budget rule unmet, run incomplete). A valid run that misses a gate is FAIL, and a failed swap test is the early stop named in the decision note. "L beats S and BR" means the interval excludes zero. FAIL means "did not establish the required advantage", not "advantage absent".
- **Q5:** no reader can name m. It is an absolute reduction in event-averaged Brier, set at pre-registration after the noise estimate; not derived from E4's accuracy points.

## 3. Splits, and the resolution proposed for v0.2
- **Q1 (biggest hole): three different answers, all real.** Gemini: the leakage rule (section 5) can starve the sample below the 250/150 floors (false FAIL). Grok: the NO-skew and slice structure can bias mean d_e mechanically. ChatGPT: distinct event IDs are not independent units; events sharing an underlying outcome narrow the bootstrap interval (false PASS). Resolution: a new step before any forecast — group the 291 events by underlying outcome (the API `series` field is a candidate aid), freeze the grouping, resample by group, and test the 150 floor against groups. Report the primary endpoint also on the subset of events that contain a YES slice (addresses Grok).
- **Q3 (slices): three-way split.** Gemini: independently (set scoring breaks the information rule). Grok: as a set summing to 1. ChatGPT: set scoring only for verified complete partitions; the 210-event fact makes that the minority case. Resolution: binary Brier per market on the frozen list; per-event mean kept; no sum-to-1 constraint; the market list, outcome definitions and weights are frozen before forecasts and never changed; sibling markets scored together must share a "forecast as of" date.
- **Q4 (Grok's alternative).** An accuracy-style pairing test on a subset where B needs A's private information is a different experiment from the shared-input design and is not adopted; its intent (content, not harm) is met by the second gate.

## 4. Caught by one reader only (ChatGPT), both adopted
- Sections 3 and 4 contradict: D receives another question's draft; section 4 forbids every arm any other market. v0.2 permits the registered substitution for D explicitly; donors are drawn from a different outcome GROUP, not merely a different question; the receiver's own input is unchanged.
- Replace "otherwise the channel carried no content" with "no positive task-relevant pairing effect was established".

## 5. Consequences for the work order
- New step, before the margin and before model selection: dependence grouping of the 291 events (read-only data work, committed and hashed).
- Model search now carries a constraint from section 5: the training cutoff must precede the earliest "forecast as of" date (March 23, 2026) or events are lost; count eligible events per candidate cutoff before choosing.
- Open and unanswered: delta = 0.10 (no reader addressed it directly). Carry to v0.2 as still open.

## 6. Process notes
Three readers, not four. No attachments; the rule was inline and every reader cited its section numbers. Reader identity recorded with model name. v0.2 to be drafted in a fresh session, not at the end of Oct 25.
