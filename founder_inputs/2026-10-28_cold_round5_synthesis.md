# Cold round 5 synthesis — scoring rule v0.3 and the Step 0b driver list (October 28, 2026)

**Status:** Systems Engine synthesis of three cold readers; Tier 3. Readers (vendor, model, as self-reported): xAI Grok 4.7; Google Gemini 3.1 Pro; OpenAI GPT-6 Astra Pro. Briefing: `founder_inputs/2026-10-26_cold_briefing_v5_scoring_rule_v0.3.md` (commit `a6c2de8`, hash `b9f3161d…`). Answers filed verbatim as `founder_inputs/2026-10-26_cold_round5_*.md` (same commit). Under review: scoring rule CANDIDATE v0.3 (`a6c2de8`, `2a4e1b4e…`) and the Step 0b lists CANDIDATE (`1f30486`). Written in a fresh session two days after the round; the Pattern D separation held. Nothing is implemented; no code was written; no model was chosen; no group count appears in this file. HEAD at the start of writing: `bba9301`.

**Correction to the seventh handoff (Oct 26, §4).** It records "3 of 3: … an admissibility rule for too few blocks is needed." Two readers said so (Gemini, ChatGPT); Grok did not raise it. The other two "3 of 3" lines in that paragraph (correct implementation; ratio estimator caveat) are right for the first and 2 of 3 for the second. Counts are corrected in sections 2 and 3 below.

---

## 1. Hallucination check

**No fabricated finding, no invented citation, no number that changes a conclusion.** Three defects recorded:

- Gemini cites "412 … markets [E3, E4]". Neither block carries 412; E4 says 410 resolved. The number happens to be the real pool size, but it is not in the briefing. Citation defect; no effect on the answer.
- Gemini calls 0.02 → 0.11 "a 5.5× change in odds". 5.5 is the ratio of probabilities; the odds ratio is about 6.1. Wording slip; the argument (a flat delta treats boundary markets and toss-ups differently) stands. Its scaled-threshold arithmetic (0.125 at p̄ = 0.50; 0.075 at p̄ = 0.10) is correct.
- Grok's Q5 "D09: split by state" reads the grain note's "summed over states" as a proposal to merge. Nothing proposed merging; D09 is already keyed by state in E3. The substance (one driver per state) agrees with the other two readers; the word "split" misreads the question, not the evidence.

ChatGPT: every formula checked — the ratio estimator, the feasibility limit (one block holding more than half the eligible drafts), the bridge-node chain. All correct as conditional statements, and each is flagged as conditional rather than as a claim about the pool.

## 2. Unanimous (3 of 3) — adopt

1. **Q1:** the written-out sensitivity recomputation correctly implements v3 Step 5: same statistic, same group weights, resampling unit changed to the block, each group entering once per draw of its block.
2. **Q3:** Gate 1 must also hold (interval above zero) under the sensitivity resampling.
3. **Q4:** a donor from a different sensitivity block is accepted (ChatGPT: "stronger than necessary but defensible"); the donor rule must be fixed before any forecast, including what happens when no donor qualifies; matching on draft length carries information from the target draft into D (Grok: if the tolerance is wide; Gemini: length tracks difficulty and confidence; ChatGPT: Gate 1 then tests paired content *given* the retained length and format cues).
4. **Q5:** D03 accept; D09 accept in its state-keyed form and never summed into a national driver; D15 accept.
5. **Q6:** nothing in evidence supports delta = 0.10, and the divergence secondary endpoint as written is not pre-registrable (Grok: drop; Gemini: descriptive only, or replace; ChatGPT: keep only with a full protocol). The common ground: v0.3 §7's divergence paragraph cannot go into a pre-registration as it stands.

## 3. Two of three — adopt, dissent or silence recorded

6. **Q1:** the recomputation is a ratio estimator because blocks hold unequal numbers of groups; the reported point estimate stays the primary number and the bootstrap mean never replaces it; an admissibility rule is needed for blocks too few or too unbalanced to support an interval (Gemini: report B_eff = (Σ|b|)² ÷ Σ|b|², warn on coverage; ChatGPT: a single block gives a zero-width interval that must read "sensitivity inference not established" — a FAIL for a completed run, never a PASS). ChatGPT supplies the formula: K blocks drawn per replicate; Δ* = Σ c_b S_b ÷ Σ c_b n_b. Grok silent on both.
7. **Optional:** the rule that turns the noise estimate into m must be frozen before S or BR is run on the pool (Gemini, ChatGPT). As v0.3 §9 stands, a person sees the S and BR Brier on the confirmatory set and then chooses the hurdle. Grok silent.
8. **Q4:** a no-reuse permutation, or a hard cap on donor reuse, and a pre-registered fallback (Gemini, ChatGPT); a feasibility limit — if one block holds more than half the eligible drafts, a one-use cross-block assignment is impossible (both, independently).
9. **Q5, D01:** split (Gemini, ChatGPT) vs accept (Grok). Both splitters draw the same line: kinetic conflict, ceasefire, negotiation and the Strait of Hormuz on one side; Iranian leadership, sanctions, the rial and international participation on the other. ChatGPT adds: the conflict tag may still be applied on the second side when the written resolution conditions support it, so a documented cross-link is kept. → Founder decision 3.
10. **Q5, missing class:** US Congress, legislation, fiscal deadlines and shutdowns, and federal courts have no driver and fall on `none` (Gemini: a D32 for Congress and the courts; ChatGPT: tests keyed to a named budget cycle, legislative package, or legal/regulatory process). Grok silent.

## 4. Splits, and the resolution proposed

- **Q2, "survives": above m (Grok, ChatGPT) vs above zero (Gemini).** Resolution: above m. E1 item 2's claim is "beats … by more than the pre-registered margin, with error bars"; an interval that clears only zero under the sensitivity blocks does not support that sentence. Gemini's cost is real and accepted: with a fixed point estimate and a wider interval, a genuine effect can land in (0, m] and be a FAIL. That state gets its own reporting label — "positive under sensitivity; margin not established" — and is a FAIL, never a PASS. E4 already says FAIL; the label is new.
- **Q3, Gate 2 under sensitivity: required (Grok, ChatGPT) vs not needed (Gemini).** Gemini's argument: if L beats T by more than m and T is no worse than S, L beats S follows. Resolution: required. The implication needs Brier_T ≤ Brier_S, which nothing guarantees (ChatGPT: text could be worse than silence), and Gate 2 costs nothing extra to recompute. Gemini's cost (a false FAIL from block-level variance in the single-agent baseline) is recorded.
- **Q6, delta: three different answers.** Resolution proposed, Founder decides (decision 5): drop the divergence threshold as any kind of gate; keep |p_L − p_T| as a reported descriptive quantity. If a falsifiable secondary is wanted, two forms are on record: Gemini's unconditional test on the full sample (the covariance or slope of |p_L − p_T| against d, which never conditions on a post-treatment subset and cannot have zero support) and ChatGPT's conditional protocol (fixed aggregation, fixed claim, support rule, no rescue of a primary FAIL). Under neither is the threshold scaled by realized outcomes (ChatGPT). Gemini's scaling by √(p̄(1−p̄)) uses forecasts, not outcomes, so ChatGPT's outcome-scaling objection does not reach it; its "whose forecast defines distance" objection reaches it in part (Gemini uses the mean of the two).
- **Optional, early stop: Grok says E4 leaves an escape; ChatGPT finds none.** Resolution: ChatGPT is right about E2 — nothing in the text lets a failed grouping be cured. Grok's actual worry is different and valid: nothing in E4 says what a forecast made after a grouping fail is, and an incomplete or protocol-breaking run can be reclassified VOID after the fact. That is ChatGPT's "run incomplete needs fixed completion, retry and abort rules" in other words. Both go into v0.4 (section 6).

## 5. Caught by one reader only

**Adopted:**

- **ChatGPT:** `none` must be encoded as an empty tag set. If `none` is itself a tag, the shared-tag rule chains every untagged event into one block through the word "none". This is a hole in agreed design v3 Step 5 as well as in the lists.
- **ChatGPT:** D31's "a country not named above" drops any election in a country that already has a driver but whose election that driver does not cover (a US general election is the clearest case) onto `none`. Reword: "a 2026 electoral process not covered by any driver above, keyed by country and named cycle." (This matches the observation the Systems Engine withheld from the briefing; found cold.)
- **ChatGPT:** referenda not tied to a listed election are assigned `none` by the current row; add a driver keyed to jurisdiction and named referendum. Monetary policy beyond rate decisions (named balance-sheet programmes, emergency facilities) is uncovered.
- **ChatGPT:** the grain note is wrong in form. Risk does not follow the number of labels: merging tags coarsens the partition, narrowing a tag refines it, and adding a previously omitted overlapping tag can coarsen it. Replace "fewer risks missing a shock; more risks collapsing" with "what matters is which events share a tag, not how many tags there are."
- **ChatGPT:** the S − BR spread is not a noise estimate for T − L. The two contrasts involve different forecasts and different covariance; nothing converts one into the other. S and BR remain baseline and feasibility checks. → Founder decision 6.
- **ChatGPT:** BR must use the primary weights: average each event's YES fraction within its group, then average those group rates equally over the other groups; a pooled market fraction does not minimise the equal-group objective. "L beats BR" needs its interval requirement stated.
- **ChatGPT:** inference must say how donor-source dependence is handled (a fixed donor bank and assignment, or averaging over pre-registered assignments); the recipient-block bootstrap alone does not cover it.
- **Gemini:** B_eff reported as a diagnostic beside the block count.
- **Gemini and ChatGPT, independently (Optional):** multi-driver events are bridge nodes. Under connected components, one event tagged {D01, D12} and another tagged {D03, D12} join the whole US–Iran block, all of Trump's travel, and the whole Russia–Ukraine block into one sensitivity block. A handful of such events can collapse Step 5 into a few mega-blocks and make a sensitivity FAIL near-certain. This is a finding against agreed design v3, not only against v0.3. → Founder decision 2. Gemini's two candidate repairs: (i) each event carries one primary driver tag for block formation, other tags reported but not linking; (ii) personal-activity drivers (D11, D12) may not bridge two conflict or trade drivers. ChatGPT's: evaluate the whole tagging construction, not the four broad labels alone. From this reading: the Step 0b file's "multiple drivers on one event are allowed and expected" is the sentence that creates bridges; v3 Step 5's "share any adjudicated driver tag" is the sentence that lets them chain. Either can be changed; v3 permits change because Step 1 has not started.

**Not adopted, with reason:**

- Gemini's donor matching by stratum of the single-agent probability p_S. That selects donors using an arm's output on the target market, which ChatGPT's control conditions exclude (receiver results must not guide donor selection). Gemini's other form — fix the maximum generation length in the budget rule, or pad and truncate drafts — is adopted instead: make length uninformative rather than matched.
- Grok's "split D09" (section 1) and Grok's missing class (corporate earnings, product launches, executive tenure). E3's `none` row puts "a corporate figure" on `none` by design, and the pool is policy, geopolitics, elections and macro; nothing in the briefing places a corporate class in it. Recorded, not added.
- Gemini's reading of Q2 and its Gate 2 exemption (section 4).

## 6. Consequences for v0.3 → v0.4 (edit list; nothing applied)

- §2: sensitivity-block definition gains "`none` is the empty tag set and links nothing."
- §4 D: donor from a different sensitivity block (now reader-backed; closes Oct 26 §5 item 3); seeded permutation without reuse, or a stated reuse cap; fallback written; feasibility statement (if a block holds more than half the eligible drafts the fallback applies); length made uninformative by a fixed generation budget or padding, not by matching; donor bank drawn from the confirmatory pool only; the inference statement on donor-source dependence.
- §4 BR: leave-one-group-out with the primary weights, formula as in section 5.
- §7: K draws per replicate and the ratio formula written out; the reported sensitivity point estimate is the primary estimate by definition; admissibility rule and B_eff reported; both gates recomputed under sensitivity and both required there (interval above zero); the divergence paragraph moved out of endpoints into "reported, never endpoints", pending decision 5.
- §8: "survives" = sensitivity interval entirely above m; new FAIL label "positive under sensitivity; margin not established"; "L beats BR" given its interval requirement; completion, retry and abort rules fixed so an unfavourable partial run cannot become VOID; "sensitivity inference not established in a completed run is FAIL, not VOID"; "no T, L, D or S forecast is made after a grouping fail; one made anyway is outside the rule."
- §9: the S − BR spread demoted to baseline and feasibility; m set by the rule chosen in decision 6, frozen before any arm runs.
- §11: delta question replaced by decision 5; donor-matching and gates-under-sensitivity questions closed.

## 7. Consequences for design v3 and the Step 0b lists (nothing applied; v3 is agreed and only the Founder reopens it)

- v3 Step 5, if decision 2 is yes: block-formation rule amended per the repair chosen; `none` as an empty set made explicit.
- Step 0b lists: D01 split or accept per decision 3; D31 reworded; the `none` row says "empty tag set"; new closed tests for US Congress and fiscal deadlines, federal courts, referenda by jurisdiction, and central-bank programmes beyond rate decisions — never a "US politics" bucket; grain note rewritten. Re-committed as a new CANDIDATE, since the Oct 25 file was fixed by commit and the Founder has not said whether that commit meant acceptance.

## 8. Founder decisions (one at a time; in the order they block each other)

1. Did committing `1f30486` accept the Step 0b lists, or only save them? (Asked Oct 26, twice; unanswered.) If accepted, every change in section 7 is an amendment and must be labelled one.
2. May design v3 Step 5 be amended for the bridge-node finding? Step 1 has not started, so v3 allows it. If yes: one primary driver per event for block formation (Gemini i), a no-bridging rule for D11 and D12 (Gemini ii), or another form.
3. D01: split (two readers) or accept (one).
4. "Survives" = above m, and both gates required under sensitivity: adopted on 2-of-3 readings; they stand unless overruled.
5. Divergence: drop as an endpoint and keep descriptive; keep with ChatGPT's full protocol; or replace with Gemini's unconditional test.
6. How m is set: a governance number for "smallest worthwhile improvement" (chosen the way 0.80 was), or a frozen formula from the S − BR spread accepted as a proxy that one reader says is not one. Either way frozen before any arm runs.

## 9. Not established

Whether any multi-driver event exists in the pool (no reader estimated; none may). Whether any block would hold more than half the eligible drafts. The expected effect size in Brier (E5 unchanged). Whether the Founder accepts any decision as framed.

## 10. Process notes

Fresh session, two days after the round; the writer did not draft v0.3 and did not run the round. Three readers, everything inline; every reader cited blocks and stated vendor and model. Fifth consecutive round with zero fabricated findings under the v2-defense format (rounds 2–5 plus the May 24 v2 briefing). One handoff count corrected at the top. One observation withheld from the briefing (the D31 wording) was found cold by one reader, as the seventh handoff records.
