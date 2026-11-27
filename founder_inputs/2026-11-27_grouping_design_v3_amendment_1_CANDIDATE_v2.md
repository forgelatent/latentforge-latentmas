# Dependence grouping design v3 — amendment 1, CANDIDATE v2 (November 27, 2026)

**Status:** CANDIDATE v2. Drafted by the Systems Engine for the Founder to read. It becomes part of the agreed design only when the Founder says so in words; committing this file saves it and does not accept it. Tier 3. Nothing is implemented; no code exists for any step; no group or block count appears in this file. Amends `founder_inputs/2026-10-25_grouping_design_v3.md` (agreed October 25, 2026, commit `2e1bf84`), which is not edited; this file is read beside it. Supersedes CANDIDATE v1 (`founder_inputs/2026-11-26_grouping_design_v3_amendment_1_CANDIDATE.md`, commit `c6e48b8`), which is also not edited. The three slots v1 left open are filled here from the Founder's decisions of November 27, 2026 (`founder_inputs/2026-11-27_cold_round9_synthesis.md`, section 11). Two further points found while drafting were put to the Founder the same day and are filled in section 5. Sentences that come from the drafter and from no decision are listed in section 6. No slot is left open in this file; acceptance is still the Founder's to give.

## 1. Why an agreed design is being reopened

Unchanged from v1 section 1: design v3 is reopened before Step 1, by Founder decision of October 28, 2026, for the bridge-node finding of cold round 5. Cold round 9 (three readers, November 27) then reviewed the three points v1 left open.

## 2. What changes

**A1 — Step 5, block formation.**
v3 says: "Two events are in one sensitivity block if they share any adjudicated driver tag or are in one primary group; blocks are connected components."
Replaced by: "Each retained primary group carries at most one **group main tag** (A6), or none. Two primary groups are in one sensitivity block if and only if they carry the same group main tag. A primary group with no group main tag is a block by itself. Other driver tags, on events or groups, are recorded and reported and never link."
Under this rule every primary group lies in exactly one block and no chain through a second tag or through a group is possible. The rest of Step 5 is unchanged: the primary endpoint is recomputed with the same per-group weights and the same group means, resampling sensitivity blocks instead of primary groups; the formula is in scoring rule v0.4 §7.

**A2 — `none` is the empty tag set.**
Unchanged from v1: an event to which no driver test applies carries no driver tag. `none` is not a tag, is never stored as one, and links nothing. An empty tag set is not evidence that an event is independent of anything. **Added:** an event whose driver assignment is unresolved (A3) is never recorded as `none`.

**A3 — Step 3, what each reader records, and how the main tag is found (decisions 1a, 1b, 1c).**
v3 says each reader "(2) assigns zero or more drivers from the closed list, or 'none'."
Amended: each reader (2) applies every driver test in the frozen list to the event and records every driver whose test it passes, with the supporting text. The reader does not choose a main tag. The event's **main driver tag** is then fixed by rule: it is the passing driver that stands first in the precedence order. An event that passes no test has no main tag.
**The precedence order** is a single written ordering of the whole closed driver list, carried in the Step 0b lists file. It is chosen deliberately, shown to the Founder, approved by the Founder in words, and fixed before Step 1 like every other Step 0b list. Where a driver takes a parameter (a state, a country, a bank, a city) and an event passes that driver's test under more than one parameter, the parameter that comes first alphabetically, written exactly as the question names it, stands first (section 5, point 1). Nothing else enters the choice of main tag: not which driver seems most direct, not counts, not outcomes.
An event's driver assignment has three possible states: tagged (with a main tag), untagged (no test applies), or **unresolved** (A4).

**A4 — Step 3b, comparison, adjudication, and unsettled cases (decisions 2 and 4).**
Driver-tag agreement per event is reported twice, for the main driver tag and for the full tag set, both computed from the two readers' original independent assignments, before any adjudication or exclusion. Neither figure is a pass/fail threshold. J_human ≥ 0.80 on the group partition is unchanged and remains the only agreement threshold.
Because the main tag follows from the tag set by rule, two readers can arrive at different main tags only by disagreeing about whether a driver test passes. Every such disagreement is adjudicated with recorded evidence about the test's application. Adjudication may correct how a test was applied; it may not change the precedence order or set it aside. If the evidence does not settle it, the event's driver assignment is unresolved, the event becomes unresolved, and it is excluded with its markets at Step 4, as v3 already provides for unsettled group disagreements. Both minima are tested after these exclusions. A disagreement about a non-main tag that does not change the main tag is recorded with both readers' sets and excludes nothing.

**A5 — Step 5, "survives" covers the gates.**
Unchanged from v1: read with cold round 6 and scoring rule v0.4 §7–§8, the primary-endpoint interval must lie entirely above m, and the Gate 1 and Gate 2 intervals entirely above zero, under sensitivity-block resampling as well as primary-group resampling.

**A6 — Step 4, the group main tag (decisions 3a and 3b).**
New. After Step 3b adjudication and the Step 4 exclusions, and before the freeze: each retained primary group's group main tag is the main driver tag that stands first in the precedence order among the main tags of its retained events. A group none of whose retained events has a main tag has no group main tag. This is computed, not adjudicated; no event is relabelled or excluded because of it; each event's own tags stay in the record. The groups file written at Step 4 carries the group main tag beside each group id. The group main tag is frozen with that file. Step 6 leakage exclusions do not change it: a surviving group keeps its group main tag even if the event that supplied it is removed (section 5, point 2).

**A7 — Step 5, what "no judgment" means (decision 4).**
v3 says "No judgment is exercised at this step." Operational meaning: Step 5 takes the frozen groups file as its only input and permits no new tag, no changed tag, no removed link and no regrouping, whether in response to block counts, to results, or to anything else.

**A8 — Written limit, addition (decision 4).**
Added to v3's "Written limit": because only one main tag per group forms blocks, real dependence carried by a second driver on an event, or by a different main tag on another event in the same group, is not represented in the sensitivity partition. A PASS can survive the sensitivity check when such dependence exists. The full tag sets are kept in the record so the omission can be examined; it is not removed.

## 3. What does not change

The definition and its three link clauses. Steps 0, 0b (the rule that the lists are fixed before Step 1), 1, 2 and 6. The two blind partitions, their readers, and what neither reader may see. J_human ≥ 0.80. Adjudication of group disagreements with evidence; unsettled group disagreements make events unresolved; no default merge, no default split, no third reader. Both minima (250 markets, 150 primary groups) tested after exclusions. Every fail condition. The split of the Iran driver belongs to the Step 0b lists file.

## 4. What is definite about these choices, and what is not

Replaces v1 section 4, whose statements about the direction of the interval are withdrawn (cold round 9: one reader of three disputed them, and a check confirmed that no direction is guaranteed).
- Definite: A1 with A6 gives a partition that is the same as or finer than one in which groups could join two drivers' blocks. An exclusion under A4 removes an event and its markets from the whole test, so it can change the point estimate as well as the uncertainty, and it moves the sample toward the minima. With the retained sample and primary groups unchanged, a change in the sensitivity partition alone does not change the point estimate.
- Not established: whether any of these choices makes the sensitivity interval wider or narrower, or makes any verdict more or less likely. Whether any event passes more than one driver test, or any primary group holds events with different main tags. None of this may be estimated before the freeze.

## 5. Two points found while drafting, decided by the Founder on November 27, 2026

Neither was put to any reader. Each was put to the Founder as one question after he had read this file's first draft, with a Systems Engine recommendation, and his answer matched the recommendation both times.

**Point 1 — parameterised drivers.** If one event passes the same driver's test under two parameters, which parameter's tag stands first? Options put: alphabetical; exclude the event; write each case by hand. Founder: "A" (alphabetical). Carried in A3. The alphabet carries no meaning here; it is a tie-break.

**Point 2 — the group main tag after Step 6.** If a leakage exclusion removes the event that supplied a group's main tag, does the group keep the tag or is it recomputed from the surviving events? Founder: "A" (keep it). Carried in A6. This agrees with v3 Step 6 (surviving events keep their frozen tags) and with scoring rule v0.4 §8 (a driver tag changed after the freeze voids the run). Known oddity, recorded: a group can carry a tag supplied by an event no longer in the sample.

## 6. Sentences that are the drafter's, not from a decision or a reader

So the Founder can strike any of them:
1. A1: "A primary group with no group main tag is a block by itself", and the sentence that every group lies in exactly one block. (They follow from A2 and decision 3; no one stated them.)
2. A3: "The reader does not choose a main tag." (Follows from decision 1c: with the judgment step dropped, the order fixes the main tag once the passing tests are recorded.)
3. A4: the sentence that readers can differ on a main tag only through a test's application, and the last sentence on non-main disagreements excluding nothing.
4. A6: that the group main tag is computed after the Step 4 exclusions and before the freeze, and that the groups file carries it.
5. Section 4 in full.

## 7. Consequences elsewhere (nothing applied)

- **Scoring rule v0.4 §2**, sensitivity block: "each event carries at most one main driver tag for block formation" becomes one group main tag per primary group, as A1 and A6. **§3** gains: events with an unresolved driver assignment are removed before the freeze. No other section changes.
- **Step 0b lists CANDIDATE v2** (not yet written): the precedence order over the whole closed list, with the alphabetical rule for parameters (section 5, point 1); the sentence "Multiple drivers on one event are allowed and expected" restated (all passing drivers are recorded; only the group main tag links); the items already owed from cold round 5.
- **Step 1 cannot start** until this amendment is accepted, and a Step 0b lists file is accepted, both by the Founder in words.
