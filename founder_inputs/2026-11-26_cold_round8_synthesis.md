# Cold round 8 synthesis — how the margin m is fixed (decision 6); 2 of 2 for a governance number set before any model runs (November 26, 2026)

**Status:** Systems Engine synthesis of two cold readers; Tier 3. Readers (vendor, model, as self-reported): Google Gemini 3.1 Pro; OpenAI GPT-6 Astra Pro. **Two readers, not three:** the Founder chose to close the round without a Grok answer (stated in session, November 26). The round is therefore thinner than rounds 2–7; the finding below is unanimous among those who answered, and both are the readers whose round 5 remarks raised the question. Briefing: `founder_inputs/2026-11-26_cold_briefing_v8_margin_m.md` (53 lines, hash `66c22ace…`). Answers filed verbatim as `founder_inputs/2026-11-26_cold_round8_*.md`. Under review: scoring rule CANDIDATE v0.3 §9. The briefing pre-committed that the method answer is final and the number is the Founder's. Nothing is implemented; no arm has run; no model chosen; no group or block count appears here.

## 1. Hallucination check

**None found.** Every citation lands on a block that exists (E1–E7). Every quoted phrase is real: E1's "set at pre-registration, not after"; E2 §9's "after the noise estimate below and before any T or L forecast"; E4's two remarks; E5's "unknown". One precision note, not a defect: GPT-6 points out that E1 says "at pre-registration" and does not literally say "before S" — its "before any model arm" is a reading of E1 together with E4 and E7, and it says so. Gemini states the same conclusion as if E1 required it directly; the conclusion is the same, the provenance is GPT-6's. Both readers write "no evidence in briefing" for the numerical value of m, which is correct: the briefing supplies none.

## 2. Unanimous (2 of 2) — adopt

1. **m must be fixed before any model arm runs** (S, T, L, D). v0.3 §9's "after the noise estimate" is the sentence that fails E1; both name it as the defect.
2. **Option (a): a governance number.** The Founder fixes m in group-averaged Brier units as the smallest improvement worth claiming, recorded as chosen, not derived — the same form as the 0.80 agreement threshold (E1 item 9(b)). Both readers put no other rule ahead of it; both say it is the only option pre-registrable from the blocks alone.
3. **The S − BR spread is not a noise estimate for T − L** and cannot carry a power argument; S and BR are baseline and feasibility checks only. (GPT-6's round 5 point, now joined by Gemini.)
4. **m is a value choice, not a forecast of the effect.** E5 (Draft-KV's accuracy points) cannot size m; it is background that says the effect may be small, nothing more.
5. **"Make m small because the expected effect is small" is the Pro-Thesis Optimization Loop shape** (E7): tailoring the bar to the hoped-for result. Fixing a small m early removes later movement but does not make the justification sound; the registration must say the number is the Founder's judgment, not a consequence of Draft-KV.
6. **Nothing in the decided PASS rule (E3) lets m or the noise estimate be revised after T or L is seen.** The only sentence to replace is v0.3 §9.
7. **BR's definition needs the primary weights** (GPT-6's round 5 formula: each event's YES fraction averaged within its group, then group rates averaged equally over the other groups); "pool's YES rate" is ambiguous. Both flag it.

## 3. One difference, and the resolution proposed

**May BR and C be computed and looked at before m is signed?** Gemini: no — their scores are arithmetic on known outcomes, so any rule touching them must be frozen before anyone inspects them. GPT-6: they may be seen as context, since neither E1 nor E6 forbids it and the outcomes are already known to everyone; what matters is that nothing seen can reopen m once signed. The difference is small because both choose option (a), under which m does not depend on BR or C at all. **Resolution proposed:** GPT-6's reading, with Gemini's caution written in: m is signed before BR, C or any arm is scored; BR and C are then computed for reporting and for the "L beats BR" condition; the record states the order. This costs nothing and removes the question. Under option (b) or (c) Gemini's stricter rule would be needed; neither is adopted.

## 4. Caught by one reader only

- **GPT-6:** under a fully frozen formula the *number* could lawfully be computed after S, but the *rule* could not be chosen after; and "freeze the multiplier" is not enough if "spread" is left undefined. Adopted as the reason (c) is incomplete as written, moot under (a).
- **GPT-6:** the Founder's signed sentence (section 5). Adopted.
- **Gemini:** the human can also learn from C how hard the crowd is to beat, and be tempted by it. Recorded; closed by the ordering in section 3.

## 5. Text for v0.4 §9 (merged from the two Q4 drafts; nothing applied)

> **§9. Margin.** m is an absolute reduction in group-averaged Brier under §7's definition. The Founder fixes m at pre-registration, before any arm (S, T, L, D) runs and before BR or C is scored on the frozen pool, and signs: *"I choose m = [value] Brier units as the smallest improvement worth claiming. This is my governance judgment, not a value derived from any arm's result, from the pool's outcomes, or from Draft-KV's accuracy gains."* No arm result, baseline score or noise estimate may change m afterwards; a run whose primary interval clears zero but not m is a FAIL under §8. S and BR are baseline and feasibility checks only; the S − BR spread is not a noise estimate for T − L and carries no power claim. BR is the leave-one-group-out base rate under the primary weights: each event's YES fraction averaged within its group, then group rates averaged equally over the other groups. No calibration slice; the full eligible pool is the confirmatory set.

## 6. Decision 6 — what is settled and what is the Founder's

Settled by the round: the method. m is a governance number, signed before anything runs, in the sentence above. Not settled, and not the readers' to settle: **the value.** Two readers wrote "no evidence in briefing" for it, and that is the correct answer — nobody has a feel for Brier units on this pool yet, and the project has decided not to borrow a number from Draft-KV. The Founder picks it the way he picked 0.80, and the record says so. That choice is the last open item in scoring rule v0.4.

## 7. Process notes

Two readers, everything inline; both cited blocks and stated vendor and model; no attachments. First asking of this question; the briefing's finality clause covers the method. Eighth consecutive round with zero fabricated findings under the v2-defense format. Round size reduced from three to two by Founder decision; recorded here and in the handoff so a future reader does not take it for a full round. Systems Engine errors this round: none caught. The Gemini file was moved to `founder_inputs/` on the third attempt (download timing), as on October 28; no content issue.
