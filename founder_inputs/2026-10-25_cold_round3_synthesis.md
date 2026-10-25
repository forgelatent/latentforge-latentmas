# Cold round 3 synthesis — dependence grouping design, v1 to v2 CANDIDATE (October 25, 2026)

**Status:** Systems Engine synthesis of three cold readers; Tier 3. Readers (vendor, model, as self-reported): xAI Grok 4.7; Google Gemini 3.1 Pro; OpenAI GPT-6 Astra Pro. No second model from any vendor. Briefing: `founder_inputs/2026-10-25_cold_briefing_v3_grouping_design.md` (commit `847865b`, hash `d1cc1a49…`). Answers filed verbatim as `founder_inputs/2026-10-25_cold_round3_*.md` (commit `03310fc`). Design under review: block E8 of the briefing (Systems Engine CANDIDATE, October 25). Rule it serves: scoring rule CANDIDATE v0.2 (`founder_inputs/2026-10-25_useful_divergence_scoring_rule_v0.2_CANDIDATE.md`, commit `de149a1`). The design in section 5 is a CANDIDATE for the Founder to accept or reject. Nothing here is implemented. No code was written for this synthesis. No model was chosen. No group count appears anywhere in the design, on purpose.

The Pattern D guard does not apply to this synthesis: the design under review is the Systems Engine's own, and this session did not write it.

---

## 1. Hallucination check

**None found.** Every bracketed citation in all three answers points at a block that exists (E1 to E8). Every number traces to the briefing or to arithmetic from it:

- Gemini: "20 of 84 lack `seriesSlug`" = 84 − 64 (E5: seriesSlug non-empty 64); "39 of 84 lack `parentEventId`" = 84 − 45 (E5: parentEventId non-null 45). Correct.
- ChatGPT: "one group with 142 events and 149 singleton groups" sums to 291 (E3) and makes 150 groups (E2); 142 / 291 = 48.8%. Correct, and labelled as a hypothetical.
- Grok: no numbers used.

Three small things, none a fabrication, recorded so a later reader is not misled:

1. Gemini (Q5) calls the "each event counts once" rule "the v0.1 rule." The text it leans on is E6, which quotes v0.2 section 2 ("each event counts once, however many markets it has"). The substance is in the briefing; the version label is wrong.
2. Gemini (Q3) says "`ticker` is typically event-specific" with no citation. That is general knowledge about Polymarket, not evidence from the briefing. Not relied on below.
3. Gemini (Optional) says "merging slightly more than half the events" drops the count under 150. The exact figure is 142 merges out of 291 events, which is 48.8%: just under half. The point stands; the phrasing is loose.

Readers that quoted a project document did so correctly: Gemini's "Founder plus Systems Engine" and "sorted so linked events are adjacent" are E8's words; all three readers' "conservative call is one group" is E8's words.

## 2. Unanimous (3 of 3) — adopt in design v2

- **Q4: a second, independent grouping of all 291 events before the freeze.** Grok: required; the current design has only one pass. Gemini: yes, independently, not by two people reviewing together. ChatGPT: yes; a joint Founder–Systems Engine review is not two partitions. The second reader must not see the first partition, its ordering, or any group count.
- **Q2: the E8 definition is not precise enough for two people to apply the same way.** All three gave replacement wording. Shared elements: the link must name the shared fact; it must name a time window; shared topic or a shared API label alone is not enough.
- **Q5: "at least 150 groups" is an eligibility floor, not protection for the error bars.** Uneven group sizes break it. All three asked for a second measure (minimum groups of size k, effective sample size, or an explicit weighting choice).
- **Q3: `negRisk` is not a link** (describes slices inside one event). **No script may assign a group by matching words** (E7). `seriesSlug` and `parentEventId` may only *suggest* links; they can never decide one, because their meaning is unverified and their coverage on old snapshots is unmeasured.
- **Q4: the one-line log is too thin.** "Event ids, decision, reason" cannot be audited cold. All three require, at least, the clause of the definition that was applied and the evidence looked at.

## 3. Splits, and the resolution proposed for v2

- **Q1 (biggest hole): two shapes, same direction.** Grok and ChatGPT: dependence outside the definition (several events pushed by one shock) is resampled as if independent, so the interval is too narrow: **false PASS**. Gemini: events with missing API tags are never adjacent in the review list, stay as singletons, and inflate the group count: also **false PASS**. Both are real and both push the same way, so both get repairs. For Gemini's: event metadata is taken from the newest snapshot as well as the `first_seen` one, and untagged events are *ordered* (never linked) by resolution source and normalised title so a reviewer can see neighbours. For Grok's and ChatGPT's: a second, broader grouping by named shared driver is pre-registered as a sensitivity check that the result must survive. Grok's second mechanism, over-grouping causing a false FAIL, is accepted as the lesser risk and is answered by the written split conditions in Step 3.
- **Q2 (wording): three versions.** Grok: "one outcome is a deterministic function of the other, or both of one named fact." Gemini: three clauses (same proceeding/office/instrument; one outcome restricts the other; same recurring indicator over overlapping windows). ChatGPT: a group is a "pre-specified dependence block"; every link names the shared fact, the time window and the source; final groups are the connected components of accepted links. **Resolution:** ChatGPT's frame, with Gemini's three clauses as the link tests and ChatGPT's naming requirement on every link. Grok's deterministic-only test is **not adopted** as the whole definition: it would separate "bill passes the House" from "bill passes the Senate," which E8 meant to join; it survives as clause (b).
- **Q3 (extra signals).** Grok: none. Gemini: add `resolutionSource` and `series[0].id`/`slug` as sort and candidate signals; take the union of `first_seen` and latest snapshot metadata. ChatGPT: record all series memberships (`series` is a list, E5); add `description`, `resolutionSource` and date fields to the review packet; allow text-assisted *candidate discovery* under a contract. **Resolution:** mechanical candidate links stay at two signals (`seriesSlug` across all series memberships, and `parentEventId` in either direction). `resolutionSource` and normalised `title` are used only to **order** the review list, never to propose a link. Snapshot metadata is the union of `first_seen` and newest. The E7 rule is kept for assignment. Flag for the Founder: ordering by title is a reading aid, not a match, but it is the first use of market text in the pipeline since April; if that is unwelcome, the fallback is ordering by `resolutionSource` only.
- **Q4 (who does the second pass).** Gemini: Systems Engine and Founder independently, or a fresh cold engine session. ChatGPT: a second reader with the same packet, blind. **Resolution:** reader A is the Founder; reader B is a fresh cold engine session (any engine; model name recorded) given the Step 1 packet with outcomes stripped. The Systems Engine that wrote the design does not grade, because it is anchored on its own partition. Gemini's tie-break rule (unresolved disagreement goes to **merge**) and ChatGPT's requirement (every material disagreement adjudicated with recorded evidence) are combined: evidence first; if evidence does not settle it, merge.
- **Q5 (recurring series).** Grok: one group. Gemini: one group if windows overlap, else separate, but one group if same template. ChatGPT: one connected group for overlapping windows (transitively); no automatic rule for non-overlapping periods; coarser when in doubt. **Resolution:** overlapping windows (`first_seen` to `endDate`) form one group, chains included (A–B and B–C puts A, B, C together). Non-overlapping periods of the same series are **one group by default**; a split needs a written episode rule, recorded before the freeze, saying why the periods are separate realisations. All three readers are consistent with this.
- **Q5 (the floor).** Grok: minimum groups each with ≥ k events, or a variance-weighted effective sample size. Gemini: weight 1 per group, or N_eff ≥ 150. ChatGPT: keep 150 as eligibility; add a pre-registered feasibility report of group sizes and weights; choose the weighting explicitly. **Resolution:** 150 stays as the eligibility floor. The freeze record must report the group-size distribution, the largest groups' share of total weight, and N_eff = (Σw)² / Σw². Whether N_eff becomes a second numerical floor depends on the weighting decision in section 7, which is the Founder's.

## 4. Caught by one reader only, all adopted

- Gemini: hide the running group count during review (the 150 cliff creates pressure to split). Also the Founder's own instruction for this synthesis.
- Gemini: enumerate in advance the only conditions under which a mechanical link may be split.
- Gemini: union of `first_seen` and newest-snapshot metadata.
- ChatGPT: Step 3 must allow merging two candidate groups, not only split/keep.
- ChatGPT: a missing or empty field never creates a link, and never counts as evidence of independence.
- ChatGPT: "reviewed singleton" and "unresolved event" are distinct states; an unresolved event is never silently an independent unit.
- ChatGPT: after leakage exclusions, keep frozen group identities, drop empty groups, and never split a surviving group to recover the floor.
- ChatGPT: record rejected links as well as accepted ones.
- ChatGPT: record every series membership, not the first.
- ChatGPT: pre-register a broader sensitivity grouping.
- Grok (Optional): nothing in v1 forces the grouping step itself to declare failure. Section 6 below adds fail conditions.

## 5. Grouping design v2 (CANDIDATE — Founder to accept or reject)

**Definition.** An outcome group is a pre-declared dependence block, used for resampling. Two events are linked when (a) they resolve on the same proceeding, office, legal action, legislative instrument, or event instance; or (b) one event's resolution mathematically or legally restricts the valid outcomes of the other; or (c) they track the same recurring indicator, asset, or actor over overlapping windows (`first_seen` to `endDate`). Every accepted link names the shared fact or process, the time window, and the source material. Shared topic words, a shared API identifier, or a shared resolution source alone are not links. Final groups are the connected components of all accepted links. Different group ids do not establish independence.

**Step 0 — fix the input.** Hash `scratch/pool_resolutions_2026-10-25.json`. Count distinct `event_id` among resolved markets by a search over the whole file, per the enumeration clause. The count is written in the record but is not shown to any reader.

**Step 1 — build the review packet (no API calls).** For each resolved market, open the local snapshot dated `first_seen` and the newest local snapshot that contains the market; copy from the event object: id, slug, title, description, resolutionSource, startDate, endDate, eventDate, parentEventId, negRisk, ticker, and every `series` element's id, slug, ticker, title, recurrence, seriesType, plus seriesSlug. Identity check: pool `event_id` equals snapshot `events[0].id`; mismatches reported as unresolved, not skipped. Where the two snapshots disagree, keep both values and flag the conflict. Report per-field coverage over all 410 markets, split by snapshot year-month, so the "one snapshot" caveat of E5 is replaced by a measurement. Outcomes (`outcome`, `outcomePrices_raw`) are **not** in the packet.

**Step 2 — mechanical candidates.** Two signals only: (a) any shared `seriesSlug` or series id across all memberships; (b) same `parentEventId`, or one event's id is another's parent. Connected components of these form candidate groups. A missing or empty field never links. `negRisk`, `ticker`, `resolutionSource` and `title` are recorded and never link. Review-list order: candidate groups first, members adjacent; then singletons ordered by `resolutionSource`, then normalised `title`. Order is a reading aid; it proposes nothing.

**Step 3 — two blind partitions.** Reader A: the Founder. Reader B: a fresh cold engine session, vendor and model recorded. Each receives the Step 1 packet, the Step 2 list, the definition, and the worked examples in the method (mandatory join, justified separation, unresolved case). Neither receives the other's partition, any count of groups or candidates, or any outcome. Each reader may: keep a candidate group; split it, only under the enumerated conditions (the mechanical link joins events whose named facts are different and neither clause (a)–(c) holds; or the link is an API tagging error); merge two candidate groups; merge a singleton into a group; mark an event unresolved. One record per decision with: event ids and market ids; resulting group id; the link accepted or rejected; snapshot date and file hash used; each event's resolution fact (subject, outcome or measurement, proceeding, time window); the clause applied; for a split, why the mechanical link was rejected; for a singleton, which neighbours were considered and why not joined; reader identity; rule version; open questions.

**Step 3b — adjudication.** Compare the two partitions. Report agreement on *joined* pairs (pairs at least one reader joined), not overall pair agreement, which looks high because most pairs are unrelated. Adjudicate every material disagreement with recorded evidence. If the evidence does not settle it, merge. Both original partitions are kept in the record. An event still unresolved after adjudication stays in the "unresolved" state (section 6).

**Step 4 — freeze.** Write `founder_inputs/<date>_outcome_groups_v1.json` (event_id → group_id; link reason; source snapshots per market) and a markdown record (coverage counts, both partitions, adjudication log, rejected links). Commit and hash; the hash goes into the pre-registration. Only now count groups. Test the 150 floor. Report the group-size distribution, the share of total weight carried by the largest groups, and N_eff.

**Step 5 — sensitivity grouping, pre-registered.** A second, broader partition built by named shared driver (for example, "all events whose settlement depends on the same election cycle" or "the same central-bank decision"), written before any forecast, hashed with Step 4. The primary interval is recomputed under it. A PASS that does not survive the sensitivity grouping is reported as not established. Merging by broad topic alone is still not allowed; each sensitivity link also names its driver.

**Step 6 — leakage exclusions.** Remove excluded events; keep every surviving event's frozen group id; drop empty groups from the count; never split a surviving group because a bridging event was removed.

**Known limit (kept, narrowed).** Dependence that neither partition nor the sensitivity grouping catches is written down as a limit. It is no longer the only answer to common shocks; Step 5 is.

## 6. Fail conditions of the grouping step

The step fails, and the decision note's early stop applies, if any of these holds after adjudication: fewer than 150 groups; unresolved events whose exclusion would take the count under 150; the two readers' joined-pair agreement is below a threshold set before Step 3 begins (number to be chosen by the Founder; the readers suggested no figure and this synthesis proposes none); or a sensitivity grouping cannot be written with named drivers. None of these may be cured by splitting, by changing the definition, or by rerunning review with the count visible.

## 7. Founder question: per-event or per-group weighting (changes scoring rule v0.2 as well)

v0.2 section 7 says each event has weight 1, and the bootstrap resamples groups (section 3). Those two statements do not fit together. ChatGPT's example (E3, E6): 291 events can form exactly 150 groups as one group of 142 events plus 149 singletons. Under per-event weighting that one group carries 48.8% of the score while the floor is still met.

- **Option A — per event.** Each event weight 1; groups used only for resampling. The average keeps its current meaning ("how well did we do on events"). A large family (one election with many events) can dominate the result and the resampled intervals become lumpy. If chosen, a second floor on N_eff or on minimum group count of size ≥ k is needed, and the largest-group weights must be reported.
- **Option B — per group.** Each group weight 1; a group's score is the mean of its events' per-event Brier. A 40-event election counts the same as one lone market. The error bars match the resampling unit. The average now means "how well did we do on independent facts," which is a different question than v0.2 currently asks.
- **Systems Engine suggestion, for acceptance or rejection:** B as the primary endpoint, A reported beside it, N_eff reported in both. Reasons: Gemini argues for B or N_eff; Grok for a size-aware floor or N_eff; ChatGPT for an explicit choice that reports the largest weights. None argued for A as primary.

The choice is the Founder's. It is not made here.

## 8. Consequences for scoring rule v0.2 and the work order

- v0.2 section 2: replace the outcome-group definition with section 5's.
- v0.2 section 3: point at design v2 (this file, once accepted); add Step 5's sensitivity grouping as a pre-registered second partition; state that 150 groups is eligibility only, with N_eff and largest-group weights reported.
- v0.2 section 7: weighting per section 7 above once decided; the bootstrap resamples groups under both the primary and the sensitivity grouping.
- v0.2 section 8: add "sensitivity grouping changed after the freeze" to the void list; add "grouping step failed" as an early stop.
- v0.2 section 11: add the weighting question and the reader-agreement threshold as open.
- Work order: grouping design v2 agreed → Step 0 and Step 1 (read-only data work, own reproducers) → Step 2 list → Step 3 blind partitions → adjudication → freeze → sensitivity grouping → then the margin, then model search under the leakage counts. No code before the design is agreed.

## 9. Not established

Coverage of `seriesSlug`, `parentEventId` and `series` on snapshots before October 25 (Step 1 measures it). What `parentEventId`, `series`, `recurrence` and `seriesType` mean in Polymarket's data model. Whether any recurring series in the pool has non-overlapping periods. Distinct `event_id` in the pool (expected 291; counted in Step 0). The reader-agreement threshold. Whether the Founder will accept title ordering as a reading aid.

## 10. Process notes

Three readers, no attachments, every claim inline; every reader cited blocks. First-read fact check in the third handoff and the full check in section 1 agree. Reader identity recorded with model name. Grok's answer was filed from the clipboard; the Gemini and ChatGPT answers went chat → Systems Engine → file (recorded in the third Oct 25 handoff). The four yes/no questions put to the Founder before the round are superseded by this synthesis and are not answered. This synthesis was written in a fresh session, not at the end of the session that produced the briefing.
