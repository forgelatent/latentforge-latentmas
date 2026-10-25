# Cold round 4 synthesis — grouping design v2 to v3 CANDIDATE; weighting settled; three Founder decisions (October 25, 2026)

**Status:** Systems Engine synthesis of three cold readers; Tier 3. Readers (vendor, model, as self-reported): xAI Grok 4.7; Google Gemini 3.1 Pro; OpenAI GPT-6 Astra Pro. Briefing: `founder_inputs/2026-10-25_cold_briefing_v4_grouping_v2.md` (commit `aee6689`, hash `95eb2e41…`). Answers filed verbatim as `founder_inputs/2026-10-25_cold_round4_*.md` (same commit). Design under review: grouping design v2, section 5 of `founder_inputs/2026-10-25_cold_round3_synthesis.md`. The design in section 6 below (v3) is a CANDIDATE for the Founder to accept or reject. Nothing is implemented; no code was written; no model was chosen; no group count appears anywhere in the design. The Pattern D guard does not apply: the design is the Systems Engine's own and this session did not write v2's review.

**Correction to the fourth Oct 25 handoff and to the Systems Engine's in-session summary.** Both said the "merge if evidence does not settle it" rule was flagged by two readers. It was flagged by one (Grok, Optional). Gemini described the same rule as conservative and did not flag it. ChatGPT did not address it. The rule is still replaced in v3, for Grok's reason and because the replacement follows from a unanimous item (section 2, item 7); the count of readers was wrong and is corrected here.

---

## 1. Hallucination check

**None found.** Every bracketed citation in all three answers points at a block that exists (E1–E9). Every number traces to the briefing or to arithmetic from it:

- Gemini: 42,195 pairs = 291 × 290 ÷ 2 (E2). N_eff ≈ 4.1 for the E4 configuration under per-event weights: (291)² ÷ (142² + 149) = 84,681 ÷ 20,313 = 4.17. 190 pairs = 20 × 19 ÷ 2. "20 of 84" and "39 of 84" = 84 − 64 and 84 − 45 (E5). All correct. Its "0.70 or 0.80" and ChatGPT's "0.80, 0.90" are named as examples the blocks cannot justify, not as claims.
- ChatGPT: n(n−1)/2 pairs per group of n events. Correct. Every citation to E5's `end_date` warning is to the E5 note as written.
- Grok: no numbers. Every field named in its alternative ordering (`resolutionSource`, `eventDate`, `conditionId`) is in E5.

Two wording slips, neither an evidence error: Gemini lists "by " and "in " as "leading interrogatives" (they are prepositions); ChatGPT's "E4 … does not establish that A with group resampling is statistically invalid" is a correct reading of E4, which the briefing labelled a permitted configuration, not a finding.

## 2. Unanimous (3 of 3) — adopt

1. **Q1: Option B.** Each outcome group has weight 1; a group's score is the mean of its events' per-event Brier (markets still averaged within events). Option A is reported beside it on the identical sample as a companion result, never as a second chance to PASS (ChatGPT's wording). Group-size distribution and the largest groups' share are reported.
2. **Q3(ii): no number for the agreement threshold can be justified from the evidence.** The number is a governance choice, fixed before Step 3, recorded as a choice. → Founder decision 1 (section 7).
3. **Q3(iii): below the threshold the grouping step FAILS and the early stop applies.** No adjudication-anyway; no third reader introduced after seeing the disagreement. (ChatGPT: a third blind reader is admissible only as a policy written into the design before review begins.)
4. **Q3(i): agreement is computed over joined pairs only**, on the two original partitions, with transitive closure (every pair inside a group counts, not only recorded edges). Gemini and ChatGPT both write it as Jaccard: |J_A ∩ J_B| ÷ |J_A ∪ J_B|; Grok's "fraction of those pairs on which both agreed to join" is the same quantity.
5. **Q4: v2 is not yet pre-registrable** (threshold unset; weighting unwritten; Step 5 unspecified; clause (c) unverified).
6. **Step 5 (the sensitivity grouping) as written is insufficient.** Grok: one broader partition does not remove residual dependence. Gemini: its clauses are not written, it is built after the primary count is unblinded, and it has no blind protocol, so it can be made to produce a false FAIL (broad drivers) or a false PASS (minimal drivers). ChatGPT: it must keep the primary weights and change only what moves together in resampling, and the design must say which count is tested against 150.
7. **Unresolved events need an explicit fate.** Grok (Optional, v3 reading): nothing forces the step to say its independence claim failed. Gemini: adjudication must not become a rescue. ChatGPT: every unresolved event is excluded from the confirmatory sample, and both minima (250 markets, 150 groups) are re-checked after all exclusions.

## 3. Splits, and the resolution proposed for v3

- **Q2 (title ordering): 2 to 1.** Gemini and ChatGPT: safe under a written contract (Gemini: deterministic normalisation; adjacency never a reason; every singleton decision names the rows inspected. ChatGPT: display order only; never an edge, score or presumption; keys and tie-breaks fixed before review; readers may merge non-adjacent events; plus a written cross-list procedure so "neighbours considered" is not just the rows above and below). Grok: unsafe; no contract binds it once titles are visible; order by `resolutionSource`, then `eventDate`, then a hash of `conditionId`. **Observation:** titles must be visible in the packet in any design, because a reviewer cannot apply clauses (a)–(c) without knowing what the event is; Grok's objection therefore reduces to the sort key. **Resolution offered:** adopt ChatGPT's cross-list procedure in either case, so the sort order is no longer load-bearing; then the sort key is a Founder choice between two written options (section 7, decision 2). Not resolved here.
- **N_eff: what it is for.** Gemini: floor it, or adopt B (under which N_eff equals the group count). ChatGPT: under B it equals the group count and validates nothing; interpreting it as a statistical sample size needs assumptions not in the briefing. Grok: report it. **Resolution:** under B, no N_eff floor (it would be the 150 floor restated). Report instead the group-size distribution, the number of groups with two or more events, the largest group's share of *events*, and, beside the companion A result, the N_eff that A's weights imply. No second numerical floor: the readers gave none.
- **Q4 (biggest remaining hole): three different, all adopted.** Grok: residual shared drivers → answered by the rewritten Step 5 plus the written limit. Gemini: Step 5 discretion → Step 5 clauses and driver list written and committed before Step 1; driver tags assigned blind during Step 3 by both readers; the sensitivity partition is then mechanical. ChatGPT: clause (c) joins on listing-date overlap → replaced with outcome-window overlap from the written resolution conditions; `first_seen`/`endDate` demoted to supporting metadata; unresolved when the window cannot be determined.
- **"Merge if evidence does not settle it" (Grok only, see correction above).** Replaced: an unsettled disagreement makes the events involved *unresolved*, and unresolved events are excluded (item 7). No default merge, no default split. Cost accepted: exclusion shrinks the sample toward the floors, which is the honest direction.

## 4. Caught by one reader only, adopted

- ChatGPT: sensitivity resampling keeps the primary weights; only the resampling blocks change. The resampling and normalisation formula is written out before forecasts.
- ChatGPT: the count tested against 150 is the primary-partition count after all exclusions; the sensitivity count is reported, never substituted.
- ChatGPT: Q3 edge cases: a pair one reader joined and the other left unresolved is in the denominator only; a zero denominator reports "undefined", not 100%; numerator, denominator and unresolved counts published; agreement also reported per component of the union of the two partitions.
- ChatGPT: amend the decision note so "independent events" reads as outcome groups with equal primary weight. → Founder decision 3.
- Gemini: a second agreement figure on human-modified links only (pairs joined by at least one reader that Step 2 did not link, plus Step 2 pairs at least one reader split), so mechanical links cannot mask human disagreement.
- Gemini: a title normalisation rule restricted to lower-casing, punctuation and whitespace stripping, and removal of a fixed list of leading words; no stemming, no keyword extraction, no similarity scoring. (Used only if decision 2 keeps title in the sort key.)
- Gemini: the row status starts `UNLINKED`; adjacency may never be cited as a reason.
- Grok: alternative sort key without title. (Decision 2, option 2b.)

## 5. Not adopted, with reason

- Gemini's suggestion that a PASS additionally require the Option A point estimate to point the same way. It would make the primary endpoint depend on both weightings; A is reported, not gated. (ChatGPT's "companion, not a second chance to PASS" is the mirror of the same concern and is adopted.)
- ChatGPT's "a third blind reader as a pre-written policy." Admissible, but not adopted: the readers were unanimous that the number is a governance choice and the step fails below it; a third-reader policy would soften a floor the Founder has not yet set.

## 6. Grouping design v3 (CANDIDATE — Founder to accept or reject; three slots marked [DECISION n] await section 7)

**Definition.** An outcome group is a pre-declared dependence block, used for resampling and, under Option B, as the unit of primary weight. Two events are linked when (a) they resolve on the same proceeding, office, legal action, legislative instrument, or event instance; or (b) one event's resolution mathematically or legally restricts the valid outcomes of the other; or (c) they track the same named underlying measurement or process over overlapping *outcome windows*, where an outcome window is the period that the event's written resolution conditions say the outcome is measured over, with the boundary text recorded. Collection dates, listing dates (`first_seen`, `endDate`) and a shared actor or asset name do not establish a link by themselves. Every accepted link names the shared fact or process, the outcome window, and the source text. Shared topic words, a shared API identifier, or a shared resolution source alone are not links. Final groups are the connected components of all accepted links. Different group ids do not establish independence.

**Step 0 — fix the input.** Hash the pool file. Count distinct `event_id` among resolved markets by a search over the whole file. The count is written in the record and shown to no reader.

**Step 0b — write the fixed lists, before Step 1.** (i) The driver list for Step 5: a closed list of named shared drivers (for example "US 2026 midterm cycle", "Federal Reserve rate path 2026", "BTC/USD price path"), each with a one-line test for membership. (ii) The sort keys, normalisation rule, missing-value placement and tie-break for the review list ([DECISION 2]). (iii) The agreement threshold ([DECISION 1]). (iv) The split conditions for Step 3. All four committed and hashed with the pool hash. None may be changed after Step 1 starts.

**Step 1 — build the review packet (no API calls).** For each resolved market, open the local snapshot dated `first_seen` and the newest local snapshot that contains the market; copy from the event object: id, slug, title, description, resolutionSource, startDate, endDate, eventDate, parentEventId, negRisk, ticker, every `series` element (id, slug, ticker, title, recurrence, seriesType), and seriesSlug. Identity check: pool `event_id` equals snapshot `events[0].id`; mismatches are marked unresolved, not skipped. Where the two snapshots disagree, keep both values and flag the conflict. Report per-field coverage over all 410 markets by snapshot month. Outcomes are **not** in the packet. For each event, the packet carries the resolution-condition text (from `description`) from which reviewers read the outcome window.

**Step 2 — mechanical candidates.** Two signals only: (a) any shared `seriesSlug` or series id across all memberships; (b) same `parentEventId`, or one event's id is another's parent. Connected components of these form candidate groups. A missing or empty field never links and never implies independence. `negRisk`, `ticker`, `resolutionSource` and `title` never link. Row status starts `UNLINKED`. Review-list order: candidate groups first, members adjacent; then singletons in the order fixed at Step 0b. Order is a reading aid; adjacency may never be cited as a reason for a link, and non-adjacency is never evidence of independence.

**Step 3 — two blind partitions plus driver tags.** Reader A: the Founder. Reader B: a fresh cold engine session, vendor and model recorded. Each receives the Step 1 packet, the Step 2 list, the definition, the driver list, and worked examples (mandatory join, justified separation, unresolved case). Neither receives the other's work, any count of groups or candidates, or any outcome. Each reader, for every event: (1) assigns it to a group or marks it unresolved; (2) assigns zero or more drivers from the closed list, or "none". Allowed actions: keep a candidate group; split it, only under the Step 0b conditions (the mechanical link joins events whose named facts differ and none of (a)–(c) holds; or the link is an API tagging error); merge two candidate groups; merge a singleton into a group; mark unresolved. **Cross-list procedure (required):** for every singleton and every candidate group, the reader must examine, and list in the log, every event that shares its `resolutionSource` and every event whose outcome window overlaps its own; "neighbours considered" means that list, not the rows above and below. One record per decision with: event ids and market ids; resulting group id; the link accepted or rejected; snapshot date and file hash used; each event's resolution fact (subject, outcome or measurement, proceeding, outcome window with boundary text); the clause applied; for a split, why the mechanical link was rejected; for a singleton, the cross-list events considered and why each was not joined; driver tags; reader identity; rule version; open questions.

**Step 3b — compare and adjudicate.** On the two original partitions, with transitive closure, compute: J_all = |J_A ∩ J_B| ÷ |J_A ∪ J_B| over joined pairs; J_human, the same over pairs where at least one reader departed from Step 2; agreement per component of the union of the two partitions; and driver-tag agreement per event. A pair one reader joined and the other left unresolved is in the denominator only. A zero denominator is reported as undefined. Numerator, denominator and unresolved counts are published. **If J_human is below the Step 0b threshold, the step fails** (section 6.1). Otherwise adjudicate every material disagreement with recorded evidence. If the evidence does not settle it, every event in the disputed pair or component becomes unresolved. No default merge; no default split. Both original partitions are kept in the record.

**Step 4 — exclusions, then freeze.** Every unresolved event is removed from the confirmatory sample, with its markets. Write the groups file (event_id → group_id; link reason; driver tags; source snapshots per market) and the markdown record (coverage, both partitions, agreement figures, adjudication log, rejected links, exclusions). Commit and hash; the hash goes into the pre-registration. Only now count. Test both minima on the retained sample: at least 250 markets and at least 150 primary groups. Report the group-size distribution, the number of groups with two or more events, the largest group's share of events, and the sensitivity-partition count (Step 5) beside it, never in place of it.

**Step 5 — sensitivity partition, mechanical.** Two events are in one sensitivity block if they share any adjudicated driver tag, or are in one primary group; blocks are connected components. No new judgment is exercised at this step. The primary endpoint is recomputed with the same per-group weights and the same group means, resampling sensitivity blocks instead of primary groups. A PASS that does not survive is reported as not established. The resampling and normalisation formula is written out in the pre-registration.

**Step 6 — leakage exclusions.** Remove excluded events; keep every surviving event's frozen group id and driver tags; drop empty groups; re-check both minima; never split a surviving group because a bridging event was removed.

**Written limit.** Dependence that no clause, no driver tag and no reading catches is recorded as a limit of the method. Step 5 narrows it; it does not remove it.

### 6.1 Fail conditions

The grouping step fails, and the decision note's early stop applies, if after Step 4: fewer than 250 markets or fewer than 150 primary groups are retained; or J_human is below the threshold fixed at Step 0b; or the driver list cannot be written with one-line membership tests before Step 1. None of these may be cured by splitting, by changing the definition or the lists, by re-including an unresolved event, or by rerunning review with any count visible.

## 7. Founder decisions (one at a time; nothing here is decided)

1. **The agreement threshold (Step 0b iii).** A number for J_human, below which the step fails. No reader could derive one from evidence, and this synthesis cannot either. It is a governance choice. For scale, not as evidence: a Jaccard of 0.80 means that of all the pairs either reader joined by their own judgment, four in five were joined by both. The Founder picks the number; the record says it was picked, not derived.
2. **The singleton sort key (Step 0b ii).** Option 2a: `resolutionSource`, then `eventDate`, then normalised `title` under Gemini's normalisation rule and ChatGPT's contract. Option 2b (Grok): `resolutionSource`, then `eventDate`, then a hash of `conditionId`; no title in the key. Under either option the cross-list procedure in Step 3 is required, so the key is a reading aid only.
3. **Decision note wording (item 2).** Whether to add, to "at least 150 independent events," the words "where the independent unit is the pre-registered outcome group and each group has equal weight in the primary score." Grok and ChatGPT both say the current sentence no longer describes the quantity tested. Changing the note is the Founder's act, not the Systems Engine's.

Per-group weighting (Option B) is adopted on a 3-of-3 reading and stands unless the Founder overrules it.

## 8. Consequences for scoring rule v0.2 (to become v0.3 once decisions 1–3 are made)

- Section 2: replace the outcome-group definition with section 6's.
- Section 3: point at design v3; add Step 0b's fixed lists; state that 150 is the retained primary-group count after all exclusions; add the sensitivity partition.
- Section 7: "Per arm: mean of per-group d_g, where d_g is the mean of d_e over the group's events" as the primary endpoint; A reported as companion with its implied N_eff; group-size distribution reported; bootstrap resamples primary groups for the primary and sensitivity blocks for the sensitivity result, with the same weights.
- Section 8: "sensitivity partition changed after the freeze" and "an unresolved event re-included" added to void; "grouping step failed" added as an early stop.
- Section 11: decisions 1–3 recorded once made; delta still open.
- Decision note item 2 amended if decision 3 is yes.

## 9. Not established

Coverage of the event fields on snapshots before October 25 (Step 1 measures it). Whether `description` reliably contains the resolution conditions on older snapshots. Whether any pool series has non-overlapping outcome windows. The meaning of `recurrence` and `seriesType`. Whether the Founder will accept any of decisions 1–3 as framed.

## 10. Process notes

Three readers, no attachments, everything inline; every reader cited blocks and stated vendor and model. First-read checks in the fourth handoff and the full check in section 1 agree. The Systems Engine's "two readers flagged" error is corrected at the top of this file. This synthesis was written in the same evening session that ran the round, at the Founder's instruction, against the fourth handoff's recommendation of a fresh session; recorded, not defended.
