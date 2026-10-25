# Cold briefing v4 — grouping design v2 and three open questions (October 25, 2026)

**To the reader:** you have no terminal and no file access. Everything you may rely on is in the evidence blocks E1–E9 below, copied verbatim from committed project files or from the operator's terminal. Cite the block for every claim you make ("[E3]"). If the blocks do not support a claim, write "no evidence in briefing" rather than filling the gap. The Founder's view and the Systems Engine's view on each question are deliberately withheld. Do not assume you have seen earlier rounds; nothing outside these blocks counts. At the end, state your vendor AND your exact model name.

**What is being reviewed.** A revised CANDIDATE design (v2) for sorting 291 prediction-market events into "outcome groups": sets of events that depend on the same real-world fact. The groups become the independent unit for the experiment's error bars and for a minimum-size floor. v2 was written after a cold round on v1. Three questions were left open by that round because the readers gave no answer or split, and the project's rule is that the people who wrote the design do not settle them alone. The design is not implemented. Nothing in it is canon.

---

## E1 — The floors and the early stop (Founder decision note, October 25, 2026, committed)
> 2. On at least 250 resolved markets across at least 150 independent events from the collected Polymarket data, the latent arm beats the text arm by more than the pre-registered margin, with error bars.
> 5. What stops me early. Fewer than 150 independent events survive resolution lookup. [...]

## E2 — The pool (from the resolution lookup, committed)
410 of 412 pool markets resolved (81 YES, 329 NO) across 291 events; 2 still open. Many pool markets are slices of one event (party rankings, seat bands, date windows); only one slice wins. YES rate 19.8%.

## E3 — What the scoring rule v0.2 currently says about units and weights (committed `de149a1`, sections 2, 3 and 7)
> **Outcome group:** a set of events that depend on the same underlying real-world outcome [...]. The outcome group, not the event, is the independent unit: uncertainty is computed by resampling groups, and the decision note's 150-independent-events floor is tested against the number of groups.
> Scoring is per event: each event counts once, however many markets it has.
> Per event: mean Brier over its markets. [...] The market list, outcome definitions and weights (each market weight 1 within its event, each event weight 1) are frozen before forecasts and never changed [...]. Per arm: mean of per-event Brier.
> **Primary endpoint:** paired difference per event, d_e = Brier_T(e) − Brier_L(e). Positive favors latent. Report the mean of d_e with a 95% bootstrap interval. The bootstrap resamples outcome groups (10,000 resamples), so all events in a group move together.

## E4 — A shape the counts allow (from a round-3 reader, committed verbatim `03310fc`)
> 291 events can form exactly 150 groups consisting of one group with 142 events and 149 singleton groups. If the primary score gives equal weight to each event, that one group receives 142/291, or 48.8%, of the total weight despite the nominal count of 150 groups. This is a configuration permitted by the counts, not a description of the actual grouping.

## E5 — What the data holds (operator terminal, October 25; newest snapshot, 84 markets; one snapshot only)
```
POOL market keys: ['conditionId', 'endDate', 'event_id', 'first_seen', 'outcome', 'outcomePrices_raw', 'question', 'slug', 'status', 'umaResolutionStatuses_raw', 'updatedAt', 'volumeNum_snapshot']
SNAP markets with an event object: 84 of 84 | markets with more than one event: 0
SNAP events[0] keys include: description, endDate, eventDate, id, negRisk, parentEventId, resolutionSource, series, seriesSlug, slug, startDate, ticker, title
series non-empty: 64 | value types: ['list']
series[0] element keys include: id, recurrence, seriesType, slug, ticker, title
seriesSlug non-empty: 64 | distinct: 46
parentEventId non-null: 45
negRisk true: 33 | distinct event ids: 64
```
Coverage of these fields on snapshots from March 23 to October 24 has not been measured. The meaning of `parentEventId`, `series`, `recurrence` and `seriesType` in Polymarket's data model has not been verified; the project treats API fields as evidence, not definition (two prior findings: `end_date` did not mean settlement date; `liquidity` did not mean crowd participation).

## E6 — The project's history with text matching (incident ledger, committed)
Two prior components matched questions to markets by shared words. Both produced structured-looking false matches: one mapped every benchmark question to one of two unrelated markets because of tokens like "2026" and "April"; the other matched an astrophysics paper on a star cluster to the term "AI population forecasting". Both are recorded as a matching-without-a-contract failure. No keyword or token matching is in force anywhere in the pipeline.

## E7 — What the three round-3 readers said on the floor and on weighting (filed verbatim `03310fc`; positions only)
- Reader 1: "If groups turn out very uneven in size, 'at least 150 groups' no longer protects the error bars: a few large groups dominate the bootstrap variance while many tiny groups contribute almost nothing. The floor would need a different form (for example, a minimum number of groups each containing at least k events, or a variance-weighted effective sample size)."
- Reader 2: "'at least 150 groups' Still protects the error bars ONLY IF each outcome group receives equal weight (weight = 1 per group) in the primary endpoint and bootstrap, OR if the floor is stated in terms of Effective Sample Size ($N_{\text{eff}} = (\sum w_g)^2 / \sum w_g^2 \ge 150$)."
- Reader 3: "Retain the founder's 150-group requirement as an eligibility floor, but do not describe it as sufficient protection for the error bars. [...] Giving every group equal weight is an available design choice, but it changes the question being averaged and must be chosen explicitly before forecasts."
None of the three named a number for reader agreement. On ordering the review list by title, one reader proposed it as a reading aid, one did not address it, one allowed text-assisted candidate discovery "under an explicit contract."

## E8 — Grouping design v2 (Systems Engine CANDIDATE, October 25; not canon; from the round-3 synthesis, section 5)
**Definition.** An outcome group is a pre-declared dependence block, used for resampling. Two events are linked when (a) they resolve on the same proceeding, office, legal action, legislative instrument, or event instance; or (b) one event's resolution mathematically or legally restricts the valid outcomes of the other; or (c) they track the same recurring indicator, asset, or actor over overlapping windows (`first_seen` to `endDate`). Every accepted link names the shared fact or process, the time window, and the source material. Shared topic words, a shared API identifier, or a shared resolution source alone are not links. Final groups are the connected components of all accepted links. Different group ids do not establish independence.

**Step 0 — fix the input.** Hash the pool file. Count distinct `event_id` among resolved markets by a search over the whole file. The count is written in the record but is not shown to any reader.

**Step 1 — build the review packet (no API calls).** For each resolved market, open the local snapshot dated `first_seen` and the newest local snapshot that contains the market; copy from the event object: id, slug, title, description, resolutionSource, startDate, endDate, eventDate, parentEventId, negRisk, ticker, and every `series` element's id, slug, ticker, title, recurrence, seriesType, plus seriesSlug. Identity check: pool `event_id` equals snapshot `events[0].id`; mismatches reported as unresolved, not skipped. Where the two snapshots disagree, keep both values and flag the conflict. Report per-field coverage over all 410 markets, split by snapshot month. Outcomes are **not** in the packet.

**Step 2 — mechanical candidates.** Two signals only: (a) any shared `seriesSlug` or series id across all memberships; (b) same `parentEventId`, or one event's id is another's parent. Connected components of these form candidate groups. A missing or empty field never links. `negRisk`, `ticker`, `resolutionSource` and `title` are recorded and never link. Review-list order: candidate groups first, members adjacent; then singletons ordered by `resolutionSource`, then normalised `title`. Order is a reading aid; it proposes nothing.

**Step 3 — two blind partitions.** Reader A: the Founder. Reader B: a fresh cold engine session, vendor and model recorded. Each receives the Step 1 packet, the Step 2 list, the definition, and worked examples (mandatory join, justified separation, unresolved case). Neither receives the other's partition, any count of groups or candidates, or any outcome. Each reader may: keep a candidate group; split it, only under enumerated conditions (the mechanical link joins events whose named facts are different and none of clauses (a)–(c) holds; or the link is an API tagging error); merge two candidate groups; merge a singleton into a group; mark an event unresolved. One record per decision with: event ids and market ids; resulting group id; the link accepted or rejected; snapshot date and file hash used; each event's resolution fact (subject, outcome or measurement, proceeding, time window); the clause applied; for a split, why the mechanical link was rejected; for a singleton, which neighbours were considered and why not joined; reader identity; rule version; open questions.

**Step 3b — adjudication.** Compare the two partitions. Report agreement on *joined* pairs (pairs at least one reader joined), not overall pair agreement. Adjudicate every material disagreement with recorded evidence. If the evidence does not settle it, merge. Both original partitions are kept. An event still unresolved after adjudication stays "unresolved."

**Step 4 — freeze.** Write the groups file (event_id → group_id; link reason; source snapshots per market) and a markdown record (coverage counts, both partitions, adjudication log, rejected links). Commit and hash; the hash goes into the pre-registration. Only now count groups. Test the 150 floor. Report the group-size distribution, the share of total weight carried by the largest groups, and N_eff.

**Step 5 — sensitivity grouping, pre-registered.** A second, broader partition built by named shared driver (for example, "all events whose settlement depends on the same election cycle"), written before any forecast, hashed with Step 4. The primary interval is recomputed under it. A PASS that does not survive the sensitivity grouping is reported as not established. Each sensitivity link also names its driver.

**Step 6 — leakage exclusions.** Remove excluded events; keep every surviving event's frozen group id; drop empty groups from the count; never split a surviving group because a bridging event was removed.

## E9 — Fail conditions of the grouping step (same source, section 6)
The step fails, and the decision note's early stop applies, if any of these holds after adjudication: fewer than 150 groups; unresolved events whose exclusion would take the count under 150; the two readers' joined-pair agreement is below a threshold set before Step 3 begins (number not yet chosen); or a sensitivity grouping cannot be written with named drivers. None of these may be cured by splitting, by changing the definition, or by rerunning review with the count visible.

---

## Questions

**Q1 — Weighting.** E3 gives each event weight 1 but resamples groups; E4 shows a legal configuration where one group carries 48.8% of the score at exactly 150 groups. Two options: (A) each event weight 1, groups used only for resampling; (B) each group weight 1, a group's score being the mean of its events. Which should be the primary endpoint for the claim in E1, what does the average then mean in words, and what must be reported alongside it? If you choose A, what second floor (form and number, or "no evidence to set a number") is needed? If you choose B, does the E1 claim ("250 resolved markets across 150 independent events") still describe what is being tested? Cite blocks.

**Q2 — Ordering by title.** Step 2 orders untagged singletons by `resolutionSource` then normalised `title`, as a reading aid only, and forbids any link from it [E8]. Given E6, is that a safe use of market text, or does it reopen the matching-without-a-contract failure by another door? If unsafe, what ordering would you use instead so that two events about the same fact but with no API tags can be seen next to each other by a reviewer? If safe, what written contract must bind it?

**Q3 — Agreement threshold.** E9 requires a joined-pair agreement threshold between the two blind readers, set before review, with no number chosen. State (i) how joined-pair agreement should be computed so that it is not inflated by the many unrelated pairs, (ii) what number you would require and why, or "no evidence in briefing" if the blocks cannot support one, and (iii) what should happen below the threshold: fail, a third blind reader, or adjudicate anyway with the agreement figure reported.

**Q4 — Pre-registrable?** Is design v2 [E8] plus its fail conditions [E9] something a cold auditor could follow and check later without talking to the authors? Name the single biggest remaining way it could produce a PASS or FAIL that is not real, and cite the block.

**Optional.** Is there anything in E8 or E9 that lets a thin grouping be waved through, or that makes the step unable to fail?

**Filing.** Vendor: ____ Model: ____
