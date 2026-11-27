# Cold briefing v9 — three unsettled points in the amended sensitivity step (first asking) (November 26, 2026)

**To the reader:** you have no terminal and no file access. Everything you may rely on is in the evidence blocks E1–E7 below, copied verbatim from committed project files, from two filed cold-round answers, and from one uncommitted CANDIDATE that is marked as such. Cite the block for every claim ("[E4]"). If the blocks do not support a claim, write "no evidence in briefing" rather than filling the gap. The Founder's view and the Systems Engine's view on every question are deliberately withheld. Do not propose a model. Do not estimate how many events, groups or blocks the pool will produce, or how many events will carry more than one driver. At the end, state your vendor AND your exact model name.

**What is being reviewed.** An experiment will ask whether agents communicating in latent states forecast resolved prediction markets better than the same agents communicating in text. Its error bars are computed twice: once resampling "primary groups" (sets of events that resolve on the same fact), and once resampling broader "sensitivity blocks" (primary groups joined by a shared named cause, called a driver). A result must hold under both. The step that builds the sensitivity blocks was agreed on October 25, found to have a hole in cold round 5, and reopened by the Founder before any work began. The repair ("one main driver tag per event") leaves three points unsettled. They have never been put to a reader. **This round's answer is final for the method on these three points.** Nothing is implemented; no event has been tagged or grouped; no forecast exists.

---

## E1 — Grouping design v3 as agreed October 25 (committed `2e1bf84`); excerpts

> **Definition.** [...] Final groups are the connected components of all accepted links.
> **Step 3 — two blind partitions plus driver tags.** Reader A: the Founder. Reader B: a fresh cold engine session, vendor and model recorded. [...] Neither receives the other's work, any count of groups or candidates, or any outcome. Each reader, for every event: (1) assigns it to a group or marks it unresolved; (2) assigns zero or more drivers from the closed list, or "none".
> **Step 3b — compare and adjudicate.** On the two original partitions [...]: J_all [...]; **J_human** [...]; agreement per component of the union of the two partitions; driver-tag agreement per event. [...] **If J_human < 0.80 the step fails** (Fail conditions). Otherwise adjudicate every material disagreement with recorded evidence. If the evidence does not settle it, every event in the disputed pair or component becomes unresolved. No default merge; no default split. Both original partitions are kept in the record. No third reader.
> **Step 4 — exclusions, then freeze.** Every unresolved event is removed from the confirmatory sample, with its markets. [...] Test both minima on the retained sample: at least 250 markets and at least 150 primary groups.
> **Step 5 — sensitivity partition, mechanical.** Two events are in one sensitivity block if they share any adjudicated driver tag or are in one primary group; blocks are connected components. No judgment is exercised at this step. The primary endpoint is recomputed with the same per-group weights and the same group means, resampling sensitivity blocks instead of primary groups. A PASS that does not survive is reported as not established. The resampling and normalisation formula is written out in the pre-registration.

Note: J_human is an agreement figure on the *group* partition only. v3 sets no threshold for driver-tag agreement.

## E2 — The hole found in cold round 5: two readers, verbatim (committed `a6c2de8`)

Block references inside these quotations are to the round 5 briefing, not to this one.

**Gemini 3.1 Pro:** "Because [E3] states "Multiple drivers on one event are allowed and expected," a single cross-cutting event (for example, a market on whether Trump meets Putin/Zelenskyy or imposes China tariffs while travelling, tagged with both `D12` and `D03` or `D12` and `D14` or `D12` and `D01` [E3]) acts as a **bridge node** under transitive connected components [E2, E4]. One event tagged `{D01, D12}` and another tagged `{D03, D12}` will merge the *entire* US–Iran conflict block (D01), all Trump travel/meetings (D12), and the *entire* Russia–Ukraine war block (D03) into a **single gigantic sensitivity block** [E2, E3, E4]. [...] **Fix:** Either assign each event at most **one primary macro driver** (the dominant shared cause) for Step 5 connected components, or prevent narrow personal-activity drivers (`D11`, `D12`) from transitively bridging two distinct geopolitical conflict drivers (`D01`, `D03`, `D14`, `D27`, `D28`)."

**GPT-6 Astra Pro:** "Multiple tags can also connect seemingly separate drivers transitively. Hypothetically, an event tagged D01 and D12 and another tagged D03 and D12 would connect the two war-related drivers through D12. That relationship is permitted by the tests; there is no claim here that those events occur in the pool. Evaluate the full tagging construction, not the four broad labels in isolation."

## E3 — The Founder's decision (October 28; recorded in the November 3 handoff, committed)

> **Design v3 Step 5 reopened** before Step 1 for the bridge-node finding: **option A — one main driver tag per event** for block formation; other tags recorded, never linking. An agreed design is being amended; the amendment must say so. (Oct 28)

## E4 — Amendment 1 to design v3, CANDIDATE (drafted November 26; not yet committed; not accepted); the changes as written

> **A1 — Step 5, block formation (decision 2, "option A").** [...] Replaced by: "Each event carries at most one **main driver tag**, or none. Two events are in one sensitivity block if they carry the same adjudicated main driver tag or are in one primary group; blocks are connected components. Any other driver tags on an event are recorded and reported and never link."
> **A2 — `none` is the empty tag set.** An event to which no driver test applies carries no driver tag at all. `none` is not a tag, is never stored as one, and links nothing. Two untagged events are not in one block because both are untagged. An empty tag set is also not evidence that an event is independent of anything.
> **A3 — Step 3, what each reader records.** [...] Amended: each reader (2) assigns zero or more drivers from the closed list, and (3) if any driver was assigned, names exactly one of them as the event's main driver tag. An event with no driver has no main tag. The log record gains the main driver tag beside the full tag list.
> **A4 — Step 3b, what is compared.** Driver-tag agreement per event is reported twice: for the main driver tag, and for the full tag set. The main-tag figure is the one that matters for block formation. Neither figure is a pass/fail threshold; J_human ≥ 0.80 on the group partition is unchanged and remains the only agreement threshold.

What the amendment does not contain: any rule for which driver a reader names as main when several tests pass; any rule for what happens when the two readers name different main tags and adjudication does not settle it; any statement about primary groups whose events carry different main tags.

## E5 — The driver list's instructions and four of its rows (Step 0b lists, committed `1f30486`; a draft, saved and not accepted)

> How to use: for each event, a sorter assigns every driver whose test the event passes, or `none`. Tests are applied to the question text and the event description. [...] Multiple drivers on one event are allowed and expected. A driver is a *shared cause*, broader than a group; passing the same driver test never by itself puts two events in one primary group.

| Id | Driver | Membership test (one line) |
|---|---|---|
| D03 | Russia–Ukraine war: front line and peace process | The outcome depends on territorial control in Ukraine, on Russia–Ukraine negotiations, or on a meeting, call or clash whose stated subject is that war (including NATO–Russia and Trump–Putin/Zelenskyy contacts about it). |
| D05 | US Federal Reserve, 2026 | The outcome is a Federal Reserve rate decision, dissent, or sequence of decisions, or the tenure of the Fed Chair. |
| D11 | Trump's public statements and posts | The outcome is determined by what Donald Trump posts, says, praises or insults, in a stated window. |
| D12 | Trump's travel and meetings | The outcome is whether Donald Trump attends, visits, meets or speaks with a named person, event or country in a stated window. |

The full list has 31 drivers and is being revised; its other rows are not needed for these questions.

## E6 — How the blocks are used (scoring rule CANDIDATE v0.4, approved by the Founder November 26; committed `fd84f55`); excerpts

> Let K be the number of retained sensitivity blocks, n_b the number of primary groups in block b, and S_b the sum of d_g over the groups in block b. The point estimate is Δ = Σ S_b ÷ Σ n_b, which is the primary point estimate by definition. Each replicate draws exactly K blocks uniformly with replacement; with c_b the number of times block b is drawn, the replicate's value is Δ* = Σ c_b S_b ÷ Σ c_b n_b.
> **Admissibility.** If fewer than two sensitivity blocks are retained, or the resampling distribution is degenerate (zero width), the result is "sensitivity inference not established" and a completed run is a FAIL, never a PASS and never a VOID.
> **Pass:** primary-endpoint interval entirely above the pre-registered margin m under both primary-group and sensitivity-block resampling, AND Gate 1 and Gate 2 each met as defined in §7, AND L beats BR.

Note: the margin m is fixed (a Founder governance number, signed before any arm ran). A wider sensitivity interval makes PASS harder; a narrower one makes it easier.

## E7 — Project history relevant to these points (incident ledger, committed)

A prior benchmark script in this project carried pre-written favourable prose for every verdict branch, so no result could be unfavourable; it is recorded as a "Pro-Thesis Optimization Loop." Two prior components matched text by shared words without a written contract and produced structured-looking false matches. The project treats any rule that can be bent after counts or results are visible, any control that cannot fail, and any judgment step without a written test, as known failure shapes.

---

## Questions

Answer each separately. Cite blocks. Write "no evidence in briefing" where that is the honest answer.

**Q1 — Choosing the main tag.** When an event passes more than one driver test [E5], A3 requires each reader to name exactly one as main [E4]. Nothing written says which. Is a written selection rule required before Step 3, or is reader judgment with main-tag agreement reported [E4, A4] enough? If a rule is required, write it so that two readers would apply it the same way, in under 80 words, and say what it does with an event such as E2's example (a Trump meeting whose stated subject is the Russia–Ukraine war, which passes both D03 and D12 as written [E5]). Name the failure shape your answer permits.

**Q2 — Unsettled main tags.** When the two readers name different main tags for an event and adjudication with evidence does not settle it, what happens? Options on the table: (a) the event carries no main tag; (b) the event becomes unresolved and is excluded with its markets, as v3 does for unsettled group disagreements [E1]; (c) both tags link for that event; (d) another rule, stated in one sentence. For each of (a), (b) and (c), state which way it moves the sensitivity interval or the sample, and so which wrong verdict it makes more likely under E6's PASS rule. Then choose one. Separately: should main-tag agreement have a pass/fail threshold of its own, as J_human does for groups [E1], and if so what happens below it?

**Q3 — Primary groups as bridges.** Under A1 [E4], "are in one primary group" is itself a link. If two events in one primary group carry different main tags, does that group join the two drivers' blocks in the same way a two-tag event did in E2? If yes, is that a hole to repair or the correct behaviour? Options: (a) leave it; (b) one main tag per primary group instead of per event; (c) require events in one primary group to share a main tag, and treat a mismatch as a disagreement to adjudicate; (d) another rule in one sentence. Note that readers tag events blind in Step 3, before primary groups are final [E1]; say how your choice works given that order.

**Q4 — Is the amended step mechanical?** v3 Step 5 says "No judgment is exercised at this step" [E1]. With A1–A4 [E4] and your answers to Q1–Q3, is that still true? Name the single biggest remaining way the amended sensitivity step could produce a "not established" that is not real, or let a PASS survive that should not, and cite the block.

**Optional.** Is there anything in E4 that lets the sensitivity check be made toothless (blocks so fine that it equals the primary analysis) or unpassable (blocks so coarse that E6's admissibility rule or interval width decides the verdict) by choices made during tagging?

**Filing.** Vendor: ____ Model: ____
