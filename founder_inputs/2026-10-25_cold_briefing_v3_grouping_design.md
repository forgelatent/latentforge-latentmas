# Cold briefing v3 — dependence grouping of the 291 events (October 25, 2026)

**To the reader:** you have no terminal and no file access. Everything you may rely on is in the evidence blocks E1–E8 below, copied verbatim from the operator's terminal or from committed project files. Cite the block for every claim you make ("[E3]"). If the blocks do not support a claim, write "no evidence in briefing" rather than filling the gap. The Founder's view and the Systems Engine's view on each question are deliberately withheld. At the end, state your vendor AND model name.

**What is being reviewed.** A CANDIDATE design for sorting 291 prediction-market events into "outcome groups" — sets of events that depend on the same real-world outcome. The groups become the independent unit for the experiment's error bars and for a minimum-size floor. The design is not implemented. Nothing in it is canon.

---

## E1 — Why grouping exists (from the cold round 2 synthesis, committed)
> **Q1 (biggest hole): three different answers, all real.** Gemini: the leakage rule can starve the sample below the 250/150 floors (false FAIL). Grok: the NO-skew and slice structure can bias mean d_e mechanically. ChatGPT: distinct event IDs are not independent units; events sharing an underlying outcome narrow the bootstrap interval (false PASS). Resolution: a new step before any forecast — group the 291 events by underlying outcome (the API `series` field is a candidate aid), freeze the grouping, resample by group, and test the 150 floor against groups.

## E2 — The floors and the early stop (Founder decision note, October 25, 2026, committed)
> 2. On at least 250 resolved markets across at least 150 independent events from the collected Polymarket data, the latent arm beats the text arm by more than the pre-registered margin, with error bars.
> 5. What stops me early. Fewer than 150 independent events survive resolution lookup. [...]

## E3 — The pool (from the October 25 handoff and the resolution lookup, committed)
410 of 412 pool markets resolved (81 YES, 329 NO) across 291 events; 2 still open. Many pool markets are slices of one event (party rankings, seat bands, date windows); only one slice wins. YES rate 19.8%.

## E4 — What the pool file holds per market (operator terminal, October 25)
```
POOL markets type: list | len: 412
POOL market keys: ['conditionId', 'endDate', 'event_id', 'first_seen', 'outcome', 'outcomePrices_raw', 'question', 'slug', 'status', 'umaResolutionStatuses_raw', 'updatedAt', 'volumeNum_snapshot']
POOL counts keys: ['RESOLVED_NO', 'RESOLVED_YES', 'STILL_OPEN']
```

## E5 — What a daily snapshot holds about events (operator terminal, October 25; snapshot file 2026-10-25, 84 markets)
```
SNAP events[0] keys: ['active', 'archived', 'automaticallyActive', 'closed', 'commentCount', 'competitive', 'createdAt', 'creationDate', 'cyom', 'deploying', 'description', 'enableNegRisk', 'enableOrderBook', 'endDate', 'eventDate', 'featured', 'gameId', 'icon', 'id', 'image', 'liquidity', 'liquidityClob', 'negRisk', 'negRiskAugmented', 'new', 'openInterest', 'parentEventId', 'pendingDeployment', 'resolutionSource', 'restricted', 'series', 'seriesSlug', 'showAllOutcomes', 'showMarketImages', 'slug', 'startDate', 'startTime', 'ticker', 'title', 'updatedAt', 'version', 'volume', 'volume1mo', 'volume1wk', 'volume1yr', 'volume24hr']
SNAP markets: 84 | series at top: 0 | series inside events[0]: 64 | markets with more than one event: 0
SNAP markets with an event object: 84 of 84
series non-empty: 64 | value types: ['list']
series[0] element keys: ['active', 'archived', 'closed', 'commentCount', 'createdAt', 'featured', 'icon', 'id', 'image', 'liquidity', 'recurrence', 'restricted', 'seriesType', 'slug', 'ticker', 'title', 'updatedAt', 'volume', 'volume24hr']
seriesSlug non-empty: 64 | distinct: 46
parentEventId non-null: 45
negRisk true: 33 | market-level negRisk true: 33
distinct event ids: 64 | distinct event slugs: 64
```
Note: these counts are from ONE snapshot (the newest). The pool spans snapshots from March 23 to October 25, 2026. Coverage of these fields on older snapshots has not been measured. The meaning of `parentEventId`, `series`, `recurrence` and `seriesType` in Polymarket's data model has not been verified; the project treats API fields as evidence, not definition (two prior findings: `end_date` did not mean settlement date; `liquidity` did not mean crowd participation).

## E6 — The rule text the grouping serves (scoring rule CANDIDATE v0.2, sections 2–3, committed `de149a1`)
> **Outcome group:** a set of events that depend on the same underlying real-world outcome (several events about the same election, the same court case, the same price path). Distinct event IDs do not establish independence. The outcome group, not the event, is the independent unit: uncertainty is computed by resampling groups, and the decision note's 150-independent-events floor is tested against the number of groups.
> Every one of the 291 events is assigned to exactly one outcome group by a written method. [...] The grouping is committed and hashed before any forecast is made, and is never changed afterwards. [...] Fewer than 150 groups is the early stop in the decision note (§5), not a reason to loosen this rule. [...] a human check of the grouping is part of the method and is recorded.

## E7 — The project's history with text matching (incident ledger, committed)
Two prior components matched questions to markets by shared words. Both produced structured-looking false matches: one mapped every benchmark question to one of two unrelated markets because of tokens like "2026" and "April"; the other matched an astrophysics paper on a star cluster to the term "AI population forecasting". Both are recorded as a matching-without-a-contract failure. No keyword or token matching is in force anywhere in the pipeline.

## E8 — The CANDIDATE design (Systems Engine, October 25; not canon)
**Definition.** Two events are in one outcome group if they resolve on the same real-world fact, or one's resolution logically constrains the other's: the same election, the same court decision, the same bill, the same price series over overlapping windows. "Both about politics" is not a group.
**Step 0.** Hash the pool file. Count distinct `event_id` among resolved markets by a search over the whole file (expected 291).
**Step 1.** For each of the 410 resolved markets, open the local snapshot dated `first_seen`, find the market by `conditionId`, copy the event object's id, slug, title, seriesSlug, series ticker/title/recurrence/seriesType, parentEventId, negRisk, ticker. Identity check: pool `event_id` must equal snapshot `events[0].id`; mismatches reported, not skipped. Report per-field coverage over all 410. No API calls.
**Step 2.** Mechanical candidate links, two signals only: (a) same `seriesSlug`; (b) same `parentEventId`, or one event's id is another's parent. Events connected by either join one candidate group. `negRisk` recorded, not used as a link (it describes slices within one event). No keyword matching.
**Step 3.** Human review of all 291 events (Founder plus Systems Engine), reading a list sorted so linked events are adjacent. Per candidate group: split or keep. Per singleton: merge if the definition says so. One logged line per decision: event ids, decision, reason. Series that repeat over time (weekly price markets) are a review decision; the conservative call under the definition is one group.
**Step 4.** Write `founder_inputs/<date>_outcome_groups_v1.json` (event_id → group_id, link reason, source snapshot per market) plus a markdown record (coverage counts, review log). Commit and hash; the hash goes into the pre-registration. Count groups; the 150 floor is tested now and again after leakage exclusions.
**Known limit.** Dependence that no field and no reading catches (two events moved by the same macro shock but not the same fact) is outside the definition and is written down as a limit.

---

## Questions

**Q1.** What is the single biggest way this grouping could make the experiment declare a PASS or FAIL that is not real? Name the mechanism and cite the block.

**Q2.** Is the definition in E8 ("same real-world fact, or one resolution logically constrains the other") the right test for independence here, and is it precise enough for two people to apply the same way across 291 events? If not, what wording would you require?

**Q3.** Are `seriesSlug` and `parentEventId` [E5] sound as the only mechanical link signals, given that their meanings are unverified [E5 note] and coverage on older snapshots is unmeasured? Should `negRisk`, `ticker`, or anything else in E5 be a link? Is the "no keyword matching" rule [E7] right, or does it throw away a signal the review needs?

**Q4.** The human review covers all 291 events with a one-line log per decision [E8, step 3]. What must that log contain for a cold reader to audit it later? Should the design require a second, independent grouping (blind re-grouping by another reader, agreement measured) before the freeze?

**Q5.** Series that repeat over time (e.g., weekly price markets, [E5] `recurrence`): one group or several? And if groups turn out very uneven in size, does "at least 150 groups" [E2] still protect the error bars, or does the floor need a different form?

**Optional.** Is there anything in E8 that makes the grouping step unable to fail, or that lets a thin grouping be waved through?

**Filing.** Vendor: ____ Model: ____
