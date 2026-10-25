# Dependence grouping design v3 (October 25, 2026)

**Status:** CANDIDATE with the three Founder decisions filled in; becomes the agreed design when the Founder commits this file. Source: section 6 of `founder_inputs/2026-10-25_cold_round4_synthesis.md` (commit `97d5843`), with decisions 1–3 of that file's section 7 applied as the Founder made them on October 25 (recorded in item 9 of `founder_inputs/2026-10-25_founder_decision_note.md`). Tier 3. Nothing is implemented; no code exists for any step; no group count appears anywhere in this file. Supersedes v2 (round 3 synthesis, section 5) and v1 (briefing v3, block E8).

**Decisions applied.** (1) Agreement threshold: J_human ≥ 0.80, a Founder governance choice, not derived from evidence. (2) Review-list order for untagged events: resolution source, then event date, then normalised title, under the written contract in Step 2. (3) The Founder decision note's item 2 now names the pre-registered outcome group as the independent unit with equal weight per group. Per-group weighting (Option B) is the primary endpoint on a 3-of-3 reading.

---

## Definition

An outcome group is a pre-declared dependence block, used for resampling and as the unit of primary weight. Two events are linked when (a) they resolve on the same proceeding, office, legal action, legislative instrument, or event instance; or (b) one event's resolution mathematically or legally restricts the valid outcomes of the other; or (c) they track the same named underlying measurement or process over overlapping *outcome windows*, where an outcome window is the period that the event's written resolution conditions say the outcome is measured over, with the boundary text recorded. Collection dates, listing dates (`first_seen`, `endDate`) and a shared actor or asset name do not establish a link by themselves. Every accepted link names the shared fact or process, the outcome window, and the source text. Shared topic words, a shared API identifier, or a shared resolution source alone are not links. Final groups are the connected components of all accepted links. Different group ids do not establish independence.

## Step 0 — fix the input

Hash the pool file (`scratch/pool_resolutions_2026-10-25.json`). Count distinct `event_id` among resolved markets by a search over the whole file. The count is written in the record and shown to no reader.

## Step 0b — write the fixed lists, before Step 1

All four committed and hashed with the pool hash; none may change after Step 1 starts.

1. **Driver list for Step 5.** A closed list of named shared drivers (shape: "US 2026 midterm cycle", "Federal Reserve rate path 2026", "BTC/USD price path"), each with a one-line membership test. To be written in the next design session; not written here.
2. **Sort order for untagged events (decision 2).** Keys, in order: `resolutionSource`; `eventDate`; normalised `title`. Normalisation: lower-case; strip punctuation; collapse whitespace; remove a fixed list of leading words (the list itself is written and committed at Step 0b). No stemming, no keyword extraction, no similarity score. Missing values sort last within their key. Tie-break: `conditionId` of the event's first market. **Contract:** sorting changes display order only; it never creates an edge, candidate group, merge, exclusion, score, or presumption of independence; no event is hidden or filtered by its title or source; adjacency is never evidence that two events belong together and non-adjacency is never evidence that they belong apart; adjacency may never be cited as a reason in a log line; readers may inspect and merge non-adjacent events; every accepted link must independently satisfy the definition.
3. **Agreement threshold (decision 1).** J_human ≥ 0.80 (section Step 3b). Chosen by the Founder; recorded as chosen.
4. **Split conditions for Step 3.** A mechanical candidate group may be split only when the mechanical link joins events whose named facts differ and none of clauses (a)–(c) holds, or when the link is an API tagging error. Each split names which condition applies.
5. **Worked examples.** One mandatory join, one justified separation, one unresolved case, written against the definition. To be written at Step 0b; not written here.

## Step 1 — build the review packet (no API calls)

For each resolved market, open the local snapshot dated `first_seen` and the newest local snapshot that contains the market; copy from the event object: id, slug, title, description, resolutionSource, startDate, endDate, eventDate, parentEventId, negRisk, ticker, every `series` element (id, slug, ticker, title, recurrence, seriesType), and seriesSlug. Identity check: pool `event_id` equals snapshot `events[0].id`; mismatches are marked unresolved, not skipped. Where the two snapshots disagree, keep both values and flag the conflict. Report per-field coverage over all 410 markets by snapshot month. Outcomes are **not** in the packet. For each event, the packet carries the resolution-condition text (from `description`) from which reviewers read the outcome window.

## Step 2 — mechanical candidates

Two signals only: (a) any shared `seriesSlug` or series id across all memberships; (b) same `parentEventId`, or one event's id is another's parent. Connected components of these form candidate groups. A missing or empty field never links and never implies independence. `negRisk`, `ticker`, `resolutionSource` and `title` never link. Row status starts `UNLINKED`. Review-list order: candidate groups first, members adjacent; then untagged events in the Step 0b order, under the Step 0b contract.

## Step 3 — two blind partitions plus driver tags

Reader A: the Founder. Reader B: a fresh cold engine session, vendor and model recorded. Each receives the Step 1 packet, the Step 2 list, the definition, the driver list, the split conditions and the worked examples. Neither receives the other's work, any count of groups or candidates, or any outcome. Each reader, for every event: (1) assigns it to a group or marks it unresolved; (2) assigns zero or more drivers from the closed list, or "none". Allowed actions: keep a candidate group; split it under a Step 0b condition; merge two candidate groups; merge a singleton into a group; mark unresolved. **Cross-list procedure (required):** for every singleton and every candidate group, the reader examines, and lists in the log, every event sharing its `resolutionSource` and every event whose outcome window overlaps its own; "neighbours considered" means that list. One record per decision with: event ids and market ids; resulting group id; the link accepted or rejected; snapshot date and file hash used; each event's resolution fact (subject, outcome or measurement, proceeding, outcome window with boundary text); the clause applied; for a split, which Step 0b condition; for a singleton, the cross-list events considered and why each was not joined; driver tags; reader identity; rule version; open questions.

## Step 3b — compare and adjudicate

On the two original partitions, with transitive closure (every pair inside a group counts): J_all = |J_A ∩ J_B| ÷ |J_A ∪ J_B| over pairs at least one reader joined; **J_human**, the same quantity over pairs where at least one reader departed from Step 2 (pairs joined that Step 2 did not link, plus Step 2 pairs at least one reader split); agreement per component of the union of the two partitions; driver-tag agreement per event. A pair one reader joined and the other left unresolved is in the denominator only. A zero denominator is reported as undefined, not 100%. Numerator, denominator and unresolved counts are published. **If J_human < 0.80 the step fails** (Fail conditions). Otherwise adjudicate every material disagreement with recorded evidence. If the evidence does not settle it, every event in the disputed pair or component becomes unresolved. No default merge; no default split. Both original partitions are kept in the record. No third reader.

## Step 4 — exclusions, then freeze

Every unresolved event is removed from the confirmatory sample, with its markets. Write `founder_inputs/<date>_outcome_groups_v1.json` (event_id → group_id; link reason; driver tags; source snapshots per market) and the markdown record (coverage, both partitions, agreement figures, adjudication log, rejected links, exclusions). Commit and hash; the hash goes into the pre-registration. Only now count. Test both minima on the retained sample: at least 250 markets and at least 150 primary groups. Report the group-size distribution, the number of groups with two or more events, the largest group's share of events, and the sensitivity-partition count beside it, never in place of it.

## Step 5 — sensitivity partition, mechanical

Two events are in one sensitivity block if they share any adjudicated driver tag or are in one primary group; blocks are connected components. No judgment is exercised at this step. The primary endpoint is recomputed with the same per-group weights and the same group means, resampling sensitivity blocks instead of primary groups. A PASS that does not survive is reported as not established. The resampling and normalisation formula is written out in the pre-registration.

## Step 6 — leakage exclusions

Remove excluded events; keep every surviving event's frozen group id and driver tags; drop empty groups; re-check both minima; never split a surviving group because a bridging event was removed.

## Written limit

Dependence that no clause, no driver tag and no reading catches is recorded as a limit of the method. Step 5 narrows it; it does not remove it.

## Fail conditions

The grouping step fails, and the decision note's early stop applies, if after Step 4: fewer than 250 markets or fewer than 150 primary groups are retained; or J_human < 0.80; or the driver list cannot be written with one-line membership tests before Step 1. None of these may be cured by splitting, by changing the definition or the lists, by re-including an unresolved event, by adding a reader, or by rerunning review with any count visible.

## Still to write before Step 1 (next design session)

The driver list and its membership tests; the leading-word list for title normalisation; the worked examples. Scoring rule v0.3 (per-group weighting; sensitivity blocks with primary weights; both minima after exclusions; new definition; void and early-stop additions). Only after those: Step 0 and Step 1 as read-only data work with their own reproducers.
