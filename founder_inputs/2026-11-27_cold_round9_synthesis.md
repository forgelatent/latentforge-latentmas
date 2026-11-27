# Cold round 9 synthesis — three unsettled points in the amended sensitivity step (November 27, 2026)

**Status:** Systems Engine synthesis of three cold readers; Tier 3. Readers (vendor, model, as self-reported): Google Gemini 3.1 Pro; xAI Grok 4.7; OpenAI GPT-6 Astra Pro. Briefing: `founder_inputs/2026-11-26_cold_briefing_v9_main_driver_tag.md` (commit `f51e616`). Answers filed verbatim as `founder_inputs/2026-11-27_cold_round9_*.md` (same commit). Under review: design v3 amendment 1 CANDIDATE (`c6e48b8`), saved and not accepted. Written in a fresh session that drafted neither the amendment nor the briefing; the Pattern D separation held. HEAD at the start of writing: `fbc2027`, level with origin. Nothing is implemented; no event has been tagged or grouped; no group or block count appears in this file. Nothing in any other file was edited.

**What this session had in front of it.** The five bundle files and eleven `founder_inputs/` files (decision note; design v3; Step 0b lists CANDIDATE; round 5 synthesis; scoring rule v0.4; amendment 1; briefing v9; the three answers; the November 27 handoff). **Not read:** the round 6, 7 and 8 syntheses and the November 3 and November 26 handoffs. Where this file touches them it relies on v0.4's and the handoff's account of them.

---

## 0. Plain-language page

The experiment draws its error bars twice. The second time, events are sorted into big piles by shared cause ("driver"). Each event gets one main label, and events with the same main label go in one pile. Three things were never written down. The readers were asked about each.

| Question | What the readers said | Settled? |
|---|---|---|
| When two labels fit one event, how is the main one picked? | A written rule is needed. All three would make "the war" the main label for a Trump meeting about the war. They wrote three different rules. | Rule needed: yes, 3 of 3. Which rule: no. |
| What if the two sorters pick different main labels and the evidence cannot settle it? | Take the event out of the test, with its markets. | Yes, 3 of 3. |
| Should sorter agreement on main labels have its own pass mark? | One says yes (gives no number). Two say no: report it, do not gate on it. | No. Split 1 to 2. |
| Two events tied together as one fact carry different main labels. Does that glue two piles into one? | Yes. Two readers say forbid it: one fact, one main label. One says keep it if both labels survive checking. | Glue exists: yes, 3 of 3. Repair: split 2 to 1. |

One more finding concerns something the Systems Engine wrote. Amendment 1 section 4 says which way each choice moves the error bars. One reader says no direction is established, and a small worked check (section 5) shows that reader is right. Those sentences need rewording whichever way the decisions go.

## 1. Hallucination check

**No fabricated finding, no invented citation, no number that changes a conclusion.** Every reader cited blocks and stated vendor and model. Five defects recorded:

- Gemini cites "[Intro, E5]" once. The introduction is not an evidence block; the content it cites (primary groups are events resolving on the same fact) is in the introduction as written. Citation defect.
- Gemini labels a floor failure "False FAIL / VOID". No block defines VOID as covering a sample-size failure; under scoring rule v0.4 §8 a grouping fail is the early stop, not a VOID. Label defect; the point (exclusion shrinks the sample toward the minima) stands.
- Gemini's Optional says a "near-zero-width" distribution forces a FAIL under E6. E6 says degenerate (zero width). Overstatement.
- Grok, Q2(a): removing an event's main tag "reduces the number or size of sensitivity blocks". Removing links leaves the number of blocks the same or higher, never lower. Wording slip; Gemini and GPT-6 have it the right way round.
- Gemini and Grok both read E3 as a Founder decision to *eliminate bridge nodes*. E3's text records a mechanism ("one main driver tag per event for block formation"), prompted by the bridge-node finding. Whether the decision meant "remove this one bridge" or "no bridges at all" is not in the block. This is the hinge of the Q3 split (section 4) and only the Founder can say which was meant.

Word counts of the three proposed rules (machine-counted): Gemini 68; Grok 69 for the rule, 86 if its example sentence is counted; GPT-6 66. All within the limit as rules.

## 2. Unanimous (3 of 3) — adopt unless the Founder overrules

1. **A written main-tag selection rule is required before Step 3.** Agreement reporting (A4) does not replace it; a judgment step without a written test is a known failure shape [E7].
2. **In the example, D03 is main and D12 is recorded and does not link.** Common ground of all three rules: a personal-activity driver yields to the driver that is the meeting's stated subject.
3. **Unsettled main tag: option (b).** The event becomes unresolved and is excluded with its markets before the freeze, as v3 already does for unsettled group disagreements. Option (a) (no main tag) and option (c) (both tags link) are rejected by all three; (c) restores the bridge that option A removed.
4. **Primary groups do bridge.** Under A1, two events in one primary group with different main tags join the two drivers' blocks.
5. **Step 5 stays mechanical once its inputs are frozen.** All judgment sits in Steps 3 and 3b. (Grok answers "No" to the question as asked because it reads it as covering the whole process; in substance it agrees.)

## 3. The three selection rules, side by side

| | Gemini 3.1 Pro | Grok 4.7 | GPT-6 Astra Pro |
|---|---|---|---|
| First test | Substantive domain or conflict driver over personal-activity or procedural drivers (D11, D12) | The driver whose test "most directly matches" the stated dependence; geopolitical or institutional over personal-activity when the stated subject is the former | One written precedence only: D03 over D12 for a meeting explicitly about the war |
| Second test | "Direct causal determinant" | — | — |
| If still tied | Lowest driver id | Lower-numbered driver | **Unresolved**, then excluded under Q2(b) |
| Judgment words left in | "substantive", "direct causal determinant" | "most directly" (Grok names this as its own failure shape and as the biggest remaining risk) | none; adjudication "may never invent priorities" |
| Failure shape the reader names | An arbitrary cut when two real causes co-determine an outcome | Residual reader judgment | A valid shared cause left in the non-linking tags; exclusions change the sample |

What the table shows, without choosing:

- **Two parts are separable.** (i) Which drivers yield to which: all three want this written. Gemini and Grok write it as a class ("personal-activity"); GPT-6 writes it as one named pair. Neither class is defined against the driver list, which the readers saw four rows of. Either way the content belongs in the Step 0b lists as a closed, written list of ids, not as an adjective. (ii) What happens when the written precedence does not settle it: lowest id (2 readers) or unresolved and excluded (1 reader).
- **Lowest id never excludes anything, and it is arbitrary.** Driver ids were assigned in drafting order by the Systems Engine and carry no meaning. Under this tie-break the numbering becomes a rule with consequences, and the list is about to be renumbered in CANDIDATE v2 by a drafter who has read the pool's questions. If chosen, the numbering must be fixed and stated as a rule before Step 1.
- **Unresolved-then-excluded has no arbitrary cut, and it costs sample.** Every event that passes two tests with no written precedence leaves the test with its markets. How many such events exist was not estimated by anyone and may not be. The floors are 250 markets and 150 primary groups; falling below them is the decision note's early stop.
- **The judgment phrases are optional.** Gemini's step 2 and Grok's first sentence can be dropped without losing determinism in either rule; what remains is written precedence, then the tie-break.

## 4. Splits

**Own pass mark for main-tag agreement: Gemini yes; Grok and GPT-6 no.**
- Gemini: without one, low agreement still proceeds and the sensitivity check runs on noisy tags, "a control that cannot fail". It gives no number ("no evidence in briefing").
- GPT-6: the binding control is the treatment of each case (written rule, adjudicate or exclude, minima, admissibility). The agreement figure is a diagnostic; nothing supports borrowing 0.80 from a different quantity. It concedes the cost: low original agreement followed by enough adjudications can continue, and that must stay visible.
- Grok: no, because A4 sets none. This restates the amendment and is not an argument; the "no" side rests on GPT-6.
- Resolution proposed, Founder decides: no threshold (2 of 3); both agreement figures reported on the original independent assignments, before adjudication and exclusions (GPT-6). If the Founder wants one, it is a governance number chosen the way 0.80 was, with what happens below it written first.

**Group bridges: Gemini and Grok repair with option (c); GPT-6 keeps them, option (a).**
- (c): events in one primary group must share a main tag. Checked in Step 3b after the group partition is adjudicated; a mismatch is adjudicated; an unsettled one makes the events unresolved and excluded. In effect, one main tag per primary group. Costs: more adjudication, more exclusions, and a rule is needed for which tag the group takes (Gemini reuses the Q1 rule; Grok states none).
- (a): if the group and both events' main tags survive adjudication, the join stands. GPT-6: differing main tags are not evidence that the grouping or the tagging is wrong, and making blocks finer is not by that fact a correction. Cost: blocks can chain through groups; a construction that then fails admissibility is "a limitation of that analysis", and a finer one that would pass does not show the failure was mistaken.
- The hinge is section 1's last item: what the October 28 decision meant. If it meant "no chaining of drivers through any single link", (c) follows. If it meant "one event may not link through several tags", (a) is consistent with it.
- No resolution proposed. This one turns on the Founder's intent, which no reader can supply.

## 5. Direction of effect — a correction to amendment 1 section 4

Amendment 1 section 4 states directions as fact ("fewer links, so narrower sensitivity error bars; this leans toward a PASS surviving that should not"). Gemini and Grok state the same directions. GPT-6 says deleting links makes blocks the same or finer and adding links the same or coarser, but neither fixes the direction of the interval's width, and writes "no evidence in briefing" for any verdict direction.

**Check (Systems Engine arithmetic, Tier 3).** The claim "coarser blocks always give a wider interval" was tested by running the v0.4 §7 formula on a small made-up example that uses nothing from the pool. With the point estimate held the same, merging the same values into coarser blocks made the interval narrower in one arrangement and wider in another. One failing case is enough to defeat an "always" claim. The example's numbers are deliberately not recorded in this file, by Founder decision of November 27, so that no invented figure sits in a project record; the check can be rerun by anyone with any small set of values. **GPT-6 is right: coarser does not mean wider.** The direction Gemini, Grok and the amendment state is what happens when groups inside a block move together, which is the reason for having drivers; it is an expectation, not a guarantee. The briefing shares the fault: Q2 asked "which way it moves the sensitivity interval", which presupposes a direction. Two readers supplied one; one declined.

Also from GPT-6 and correct by the formula: with the retained sample and primary groups unchanged, changing only the sensitivity partition leaves the point estimate unchanged. Excluding events does not have that protection.

## 6. Caught by one reader only

**Adopted (each follows from an agreed item or corrects the text):**
- GPT-6: A3 needs a third state, "main assignment unresolved pending adjudication", distinct from A2's "no driver applies". Option (b) cannot be written without it.
- GPT-6: an unresolved main choice must never be recorded as `none`. `none` means no test applies and is not evidence of independence.
- GPT-6: Step 5's sentence gets an operational meaning: it accepts frozen inputs and permits no new tag selection, link deletion or regrouping in response to block counts or results.
- GPT-6: the main-only rule can drop real dependence carried by a secondary driver, and a PASS could survive that should not. This is inherent in the October 28 decision and is not reopened; it goes into v3's "Written limit".
- GPT-6: any claim concerns the retained sample; nothing shows excluded events would behave the same.
- Gemini, and GPT-6 in structure (2 of 3; Grok: not from E4's text): tagging choices can push the check to either extreme, no added links (the sensitivity run equals the primary run) or fewer than two blocks (admissibility FAIL). Both follow from unwritten rules, which is why the rules are fixed before Step 3.

**Not adopted, with reason:**
- Gemini's "False FAIL / VOID" label (section 1).
- Grok's argument against a threshold (section 4); the conclusion is kept on GPT-6's reasoning.
- Any reader's statement of which wrong verdict a choice "makes more likely" (section 5).

## 7. Consequences (edit list; nothing applied)

- **Amendment 1, slot 1:** the selection rule per decision 1; its precedence content points to the Step 0b lists. A3 gains the unresolved-main state.
- **Amendment 1, slot 2:** option (b); unresolved main assignment → event unresolved, excluded with its markets at Step 4; both minima re-checked.
- **Amendment 1, A4:** both agreement figures computed on the original independent assignments; threshold per decision 2.
- **Amendment 1, slot 3:** per decision 3.
- **Amendment 1, section 4:** direction sentences reworded to what is definite (finer or coarser components; sample shrinks) with no claimed interval or verdict direction.
- **Amendment 1, new lines:** Step 5's operational meaning; the secondary-driver limit added to the Written limit.
- **Scoring rule v0.4 §2:** changes only if decision 3 is (c) (then: one main tag per primary group). §3 gains "events with an unresolved main assignment are removed before the freeze". No other section changes.
- **Step 0b lists CANDIDATE v2:** the written precedence (which driver ids yield to which); the restated "multiple drivers" sentence; if lowest id is the tie-break, the numbering fixed and declared a rule.
- One line suggested by the drafter and by no reader: when the sensitivity partition equals the primary partition, the report says so in words. The counts v3 Step 4 already reports would show it; the sentence makes it unmissable.

## 8. Founder decisions (one at a time; in the order they block each other)

1. **The selection rule.** (i) Accept the common ground: yielding is written as a closed list in the Step 0b lists. (ii) When the written precedence does not settle it: lowest driver id (2 readers), or unresolved and excluded (1 reader). (iii) Keep or drop the judgment phrases ("most directly", "direct causal determinant").
2. **Own pass mark for main-tag agreement:** no (2 readers), or yes with a number and a consequence the Founder writes (1 reader).
3. **Group bridges:** what October 28 meant, then (c) forbid mixed main tags in a primary group (2 readers) or (a) keep an adjudicated bridge (1 reader).
4. **Unanimous items in section 2 and the adopted items in section 6** stand unless overruled.
5. **Acceptance of amendment 1**, in words, only after its slots are filled per 1 to 3 and the Founder has seen the full text.

Not a decision of this round but still open and blocking any run: the kill date (decision note item 4; outer limit December 31, 2026).

## 9. Not established

Whether any event in the pool passes more than one driver test, or how many. Whether any primary group will hold events with different main tags. How many events any rule would exclude. The direction in which any choice moves the sensitivity interval or the verdict. What number a main-tag threshold should be. Whether the briefing's sentence "this round's answer is final for the method" binds: the handoff records that the Founder never accepted it in words, and two of the three points came back split.

## 10. Process notes

Fresh session; repo checks run before the task (`git log -3 --oneline`, `git status --short`, `git status -sb | head -1`): HEAD `fbc2027`, level with origin, five uncommitted pipeline files as the handoff lists. The three answers were read in full before any view was formed. Rule word counts and the section 5 check were computed, not estimated. Briefing defect recorded: Q2 presupposed a direction of effect. Systems Engine error recorded: the handoff's direction dispute is resolved here against the Systems Engine's own draft. This file proposes one resolution (the threshold) and declines to propose one for the group-bridge split.

## 11. Founder decisions made on this synthesis (November 27, 2026; added after sections 0 to 10 were written)

Each was put as one question and answered in the Founder's words, quoted. Tier 3. Nothing below is implemented and no other file was edited.

| # | Question | Founder's answer | Recorded as |
|---|---|---|---|
| 1a | Two drivers fit and the written precedence does not settle it: lowest id, or unresolved and excluded? | "A" | The driver standing first in the order wins. Nothing is excluded for this reason. |
| 1b | Should that order be chosen on purpose, shown to the Founder, approved in words and frozen before Step 1? | "Yes" | The Step 0b lists carry one deliberate precedence order. The precedence list and the order are the same thing. |
| 1c | Keep or drop the judgment phrases ("most directly", "direct causal determinant")? | "Drop it" | Dropped. The order alone decides among passing drivers. |
| 2 | Own pass mark for main-tag agreement? | "No pass amrk" | No threshold. Both agreement figures reported from the original independent assignments. |
| 3a | Primary groups whose events carry different main tags: stop the join, or keep it? | "stop at 65% confidence" | Stopped: one main tag per primary group. Recorded as a close call. |
| 3b | How the group's tag is picked: by the order, or by adjudication with exclusion if unsettled? | "use the order" | The group takes the highest-standing main tag among its events. No adjudication, no exclusion. This is Gemini's answer (reuse the selection rule) combined with decision 1; no reader wrote it in these words. |
| 4 | Six items: unsettled test-application disputes exclude the event; an "unresolved" state; unresolved is never `none`; Step 5 accepts frozen inputs only; the secondary-driver limit is written down; amendment 1 section 4's direction sentences are reworded. | "all six stand" | All six stand. |
| — | Remove the made-up example's numbers from section 5? | "yes" | Removed. |
| G1 | Found while drafting the amendment, no reader asked: one event passes the same driver under two parameters. Alphabetical, exclude, or hand-written cases? | "A" | Alphabetical by parameter as the question writes it. |
| G2 | Found while drafting, no reader asked: a leakage exclusion removes the event that supplied a group's main tag. Keep the tag or recompute? | "A" | Keep it; the tag is frozen with the groups file. |

**Anchoring, disclosed.** At 1a the Founder asked "what do you recommend". The Systems Engine recommended A at about 70%, and then gave a recommendation with every later question without being asked again. Every answer matches the recommendation given. On 3a the synthesis itself (section 4) had declined to propose a resolution; the recommendation was given in conversation, at about 65%, and the Founder repeated that figure. These are the Founder's decisions; the record shows they were made after hearing a recommendation each time.

**Not decided.** Acceptance of amendment 1 (decision 5): the Founder read the first draft of CANDIDATE v2 ("read") before G1 and G2 and has not accepted it. The precedence order itself: not written. The drafter's reporting sentence in section 7's last line. The kill date.
