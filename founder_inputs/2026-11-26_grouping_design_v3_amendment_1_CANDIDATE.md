# Dependence grouping design v3 — amendment 1 (November 26, 2026)

**Status:** CANDIDATE, incomplete. Drafted by the Systems Engine. It becomes part of the agreed design only when the Founder says so in words; committing this file saves it and does not accept it. Tier 3. Nothing is implemented; no code exists for any step; no group or block count appears in this file. Amends `founder_inputs/2026-10-25_grouping_design_v3.md` (agreed October 25, 2026, commit `2e1bf84`). The original file is not edited; this file is read beside it. Three slots are marked **[to decide]** and were not filled by the drafter (section 4).

## 1. Why an agreed design is being reopened

Design v3 was agreed on October 25, 2026. It is reopened here, before Step 1 has started, by Founder decision of October 28, 2026 (decision 2 of the cold round 5 synthesis, `founder_inputs/2026-10-28_cold_round5_synthesis.md`). v3's own text allows this: its fixed lists and rules "may not change after Step 1 starts", and Step 1 has not started.

Reason: in cold round 5, two readers independently (Gemini 3.1 Pro, GPT-6 Astra Pro) showed that Step 5 as written lets multi-driver events act as bridges. Under "share any adjudicated driver tag" with connected components, one event tagged with a conflict driver and a travel driver, and another tagged with a second conflict driver and the same travel driver, join both conflict drivers and all of the travel driver into one sensitivity block. A few such events could collapse the sensitivity partition into a handful of very large blocks and make a "not established" result near-certain whatever the truth. Whether any such event exists in the pool was not estimated by anyone and may not be.

## 2. What changes

**A1 — Step 5, block formation (decision 2, "option A").**
v3 says: "Two events are in one sensitivity block if they share any adjudicated driver tag or are in one primary group; blocks are connected components."
Replaced by: "Each event carries at most one **main driver tag**, or none. Two events are in one sensitivity block if they carry the same adjudicated main driver tag or are in one primary group; blocks are connected components. Any other driver tags on an event are recorded and reported and never link."
The rest of Step 5 is unchanged: no judgment is exercised at this step; the primary endpoint is recomputed with the same per-group weights and the same group means, resampling sensitivity blocks instead of primary groups; the formula is written out in the pre-registration (scoring rule v0.4 §7 carries it).

**A2 — `none` is the empty tag set.**
An event to which no driver test applies carries no driver tag at all. `none` is not a tag, is never stored as one, and links nothing. Two untagged events are not in one block because both are untagged. An empty tag set is also not evidence that an event is independent of anything. (GPT-6 Astra Pro, round 5: if `none` were a tag, the shared-tag rule would chain every untagged event into one block.)

**A3 — Step 3, what each reader records.**
v3 says each reader "(2) assigns zero or more drivers from the closed list, or 'none'."
Amended: each reader (2) assigns zero or more drivers from the closed list, and (3) if any driver was assigned, names exactly one of them as the event's main driver tag. An event with no driver has no main tag. The log record gains the main driver tag beside the full tag list.

**A4 — Step 3b, what is compared.**
Driver-tag agreement per event is reported twice: for the main driver tag, and for the full tag set. The main-tag figure is the one that matters for block formation. Neither figure is a pass/fail threshold; J_human ≥ 0.80 on the group partition is unchanged and remains the only agreement threshold.

**A5 — Step 5, "survives" covers the gates.**
v3 says: "A PASS that does not survive is reported as not established."
Read, by cold round 6 (4 of 4) and scoring rule v0.4 §7–§8, as: the primary-endpoint interval must lie entirely above m, and Gate 1 and Gate 2 intervals entirely above zero, under sensitivity-block resampling as well as under primary-group resampling. No further change to v3 is needed for this point; this line records the reading.

## 3. What does not change

The definition and its three link clauses. Steps 0, 0b (the rule that the lists are fixed before Step 1; the lists themselves are a separate file), 1, 2, 4 and 6. The two blind partitions, their readers, and what neither reader may see. J_human ≥ 0.80. Adjudication with evidence; unsettled group disagreements make events unresolved; no default merge, no default split, no third reader. Exclusion of unresolved events. Both minima (250 markets, 150 primary groups) tested after exclusions. The written limit. Every fail condition. The split of the Iran driver (decision 3) belongs to the Step 0b lists file, not to this amendment.

## 4. Not decided — three slots the drafter did not fill

None of these was put to any reader or decided by the Founder. Each is stated with what each choice would do, and no choice is made here.

**[to decide 1] How a reader picks the main tag when more than one driver test passes.** Decision 2 says one main tag per event. Nothing written says which. One reader's phrase in round 5 ("the dominant shared cause") is a description, not a test two people would apply the same way. Without a written rule the choice is reader judgment, and its reliability is whatever A4's main-tag agreement turns out to be.

**[to decide 2] What happens when the two readers name different main tags and the evidence does not settle it.** v3 has a rule for unsettled *group* disagreements (the events become unresolved and are excluded). It has no rule for an unsettled *main tag*. The choices and their direction:
- the event carries no main tag: fewer links, so narrower sensitivity error bars; this leans toward a PASS surviving that should not;
- the event becomes unresolved and is excluded: the sample shrinks toward the 250 and 150 floors;
- the event keeps both tags as linking tags: this is the bridge A1 exists to remove.

**[to decide 3] Primary groups can still be bridges.** A1 removes bridges through a single event's several tags. But "are in one primary group" is itself a link. If two events in one primary group carry different main tags, that group joins the two drivers' blocks, exactly as a two-tag event did before. Whether this happens in the pool is unknown and may not be estimated. Forms a rule could take, none chosen: leave it (a group that truly spans two drivers arguably should join them); give each primary group one main tag instead of each event; or require events in one primary group to share a main tag and treat a mismatch as a disagreement to adjudicate. No reader saw this point; it was found while drafting this amendment.

## 5. Consequences elsewhere

- Scoring rule v0.4 §2 already describes the sensitivity block in A1's and A2's terms and says the exact rule is this amendment's to state. If any slot in section 4 is settled in a way that changes block formation, v0.4 §2 needs the matching sentence.
- The Step 0b lists CANDIDATE v2 must drop the sentence "Multiple drivers on one event are allowed and expected" as a statement about linking, or restate it: multiple tags are still allowed; only the main tag links.
- Step 1 cannot start until this amendment is accepted with its slots filled, and a Step 0b lists file is accepted, both by the Founder in words.
