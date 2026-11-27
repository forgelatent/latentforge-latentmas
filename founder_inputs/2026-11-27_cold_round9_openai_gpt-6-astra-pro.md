**Engine:** OpenAI. **Model:** GPT-6 Astra Pro (as self-reported). **Briefing:** 2026-11-26_cold_briefing_v9_main_driver_tag.md. Tier 3. Filed verbatim. Route: attachment → Systems Engine → file (shell cat, header prepended).

## Decisions

**Require a written main-tag selection rule; exclude events whose main tag remains unresolved; retain primary-group bridges supported by adjudicated evidence; and keep aggregate main-tag agreement as a diagnostic rather than add another numerical threshold.** Step 5 can then remain mechanical, but that does not establish that its blocks capture every relevant shared cause. These are proposed resolutions of the gaps in the unaccepted amendment. [E1] [E3] [E4] [E5] [E6] [E7]

## Q1 — Choosing the main tag

**A written selection rule is required before Step 3.** A3 requires readers to choose one main tag without telling them how; A4 reports whether they agree but does not supply the missing rule. That is the judgment-without-a-written-test failure shape identified in E7. [E4] [E7]

“Choose the dominant cause” would not resolve the supplied example: D03 and D12 both expressly apply to the stated war meeting, and neither membership test establishes priority. For an existing, accepted precedence between them: **no evidence in briefing**. [E2] [E5]

### Proposed selection rule — under 80 words

> Apply every frozen driver test; record passing tags and supporting text. No passing tag means no main tag; one means that tag. For a meeting explicitly about the Russia–Ukraine war, D03 takes precedence over D12. Select the sole remaining candidate; otherwise mark the main assignment unresolved. Adjudication may correct test application using evidence, never invent priorities. Unresolved assignments follow Q2; counts and outcomes never break ties. [E1] [E2] [E4] [E5] [E7]

Freeze this rule and the membership tests before Step 3. Given the same passing tags and stated subject, the rule produces the same selection or unresolved status; disagreement about whether a membership test passes still requires evidence-based adjudication. [E1] [E4] [E5] [E7]

For the supplied **D03+D12 war-meeting example, D03 becomes main; D12 remains in the full tag set and never links**. This is an explicit new design choice giving the stated war subject priority. It is not an empirical finding that D03 is the uniquely dominant cause. For that empirical causal ranking: **no evidence in briefing**. [E2] [E4] [E5]

If another candidate remains after applying that precedence, the main assignment is unresolved. This avoids inventing priorities for the unshown drivers. A3 must consequently permit an **unresolved main assignment pending adjudication and exclusion**, distinct from the “no driver applies” state in A2. [E1] [E4] [E5]

**Failure shape still permitted:** a reproducible but inadequate dependence control. A valid shared cause can remain only in the non-linking secondary tags, so perfect agreement does not guarantee that the sensitivity analysis tests that dependence. The unresolved fallback also permits exclusion-driven changes to the confirmatory sample. Neither the prevalence of these cases nor their effect on the verdict is supplied: **no evidence in briefing**. [E1] [E3] [E4] [E5] [E6] [E7]

## Q2 — Unsettled main tags

### First distinguish partition changes from interval changes

**Deleting links makes connected components unchanged or finer; adding links makes them unchanged or coarser. Neither operation establishes a particular direction of interval-width change.** E6’s bootstrap depends on the block sums \(S_b\), group counts \(n_b\), and sampled multiplicities. The briefing supplies no realised group differences from which to determine the resulting interval. For a guaranteed width direction, or an increased probability of a particular wrong verdict: **no evidence in briefing**. [E4] [E6]

For an unchanged retained sample and unchanged primary groups, merely changing the sensitivity partition leaves the point estimate unchanged under E6. Excluding events does not have that protection because it changes the sample. [E1] [E6]

| Option | Definite consequence | Verdict risk supported by the briefing |
|---|---|---|
| **(a) Give the event no main tag** | Keeps the event and its markets but removes its contribution through driver links. Blocks can become finer or remain unchanged because primary-group links and other paths still exist. An unresolved selection is not the “no test applies” case in A2; assigning no main tag despite assigned drivers also conflicts with A3. [E4] | Omitting a genuine shared-cause connection could let an unwarranted PASS survive **if** the resulting analysis understates the relevant uncertainty. Actual narrowing or increased false-PASS probability: **no evidence in briefing**. [E4] [E5] [E6] |
| **(b) Mark unresolved and exclude with its markets** | Reduces the confirmatory sample. It can change the retained primary-group contributions and point estimate, as well as uncertainty. The retained-sample minima must be checked after exclusions. [E1] [E6] | It can prevent the design from meeting its minima and can change the population represented by the result. Neither the direction of the estimate change nor whether a wrong PASS or wrong FAIL becomes more likely is established: **no evidence in briefing**. [E1] [E6] |
| **(c) Let both tags link** | Keeps the sample and adds driver links, yielding unchanged or coarser components. It reinstates the multiple-link bridge mechanism that the Founder’s option A removed. [E2] [E3] [E4] | It can produce a construction that fails E6’s admissibility conditions, in which case a completed run must FAIL. But adding links does not guarantee a wider interval or make this option automatically conservative. Whether any resulting failure would reflect excessive grouping rather than a genuine limitation: **no evidence in briefing**. [E4] [E6] |

### Choice: (b)

**An event whose main assignment remains unresolved after evidence-based adjudication becomes unresolved and is excluded with its markets before the retained sample is frozen.** Apply this also when both readers recognise an overlap that the written selection rule cannot resolve. Preserve the original annotations and the exclusion reason, then apply the existing retained-sample minima. This extends E1’s unresolved-evidence policy without converting uncertainty into either a missing link or an extra link. [E1] [E3] [E4] [E7]

An exclusion is not inherently conservative: it changes the sample. Any eventual claim must concern the retained sample; evidence that excluded events would behave the same way is **no evidence in briefing**. [E1] [E6]

### Separate main-tag agreement threshold: no

**Do not add another aggregate numerical pass/fail threshold.** Report main-tag and full-tag agreement on the original independent assignments, before adjudication and exclusions. Every material main-tag disagreement must still receive evidence-based adjudication, and no event with an unresolved main assignment may remain in the confirmatory sample. [E1] [E4] [E7]

Under this choice, the enforceable controls are the written selection rule, mandatory resolution or exclusion, retained-sample minima, and E6’s sensitivity admissibility conditions. The agreement figure is a diagnostic, not a purported control that is incapable of failing. E7 does not require every reported diagnostic to have its own cutoff. [E1] [E4] [E6] [E7]

A separate cutoff could be adopted as additional governance, but the briefing provides no numerical main-tag threshold and no justification for transferring **0.80** from group-partition \(J_{\text{human}}\) to a different agreement quantity: **no evidence in briefing**. I choose the binding treatment of individual unresolved decisions instead. [E1] [E4]

This choice does permit low original main-tag agreement followed by enough evidenced adjudications to continue. That weakness must remain visible in the original agreement report and adjudication record; passing the retention rules does not establish general tagging reliability or independence. [E1] [E4] [E5] [E6] [E7]

## Q3 — Primary groups as bridges

**Yes.** If two events in one primary group have different main tags, the same-tag links reach each event, and the primary-group link connects them. Their drivers’ blocks therefore join. One main tag per event does **not** imply one driver per primary group or eliminate every possible bridge. [E1] [E4]

### Choice: (a), retain an evidenced bridge

**Once the primary group and both event-level main tags have survived adjudication, retain the bridge.** It is the correct result of the stated construction: sensitivity blocks preserve accepted primary groups, and E6 resamples blocks containing whole primary groups with their unchanged contributions. [E1] [E4] [E6]

This is a hole in any claim that option A **abolishes all bridging**. It is not, by itself, evidence that the remaining bridge is erroneous. Distinct main tags do not establish independence or prove that the events were wrongly placed in one primary group. For either proposition: **no evidence in briefing**. [E1] [E3] [E4] [E5]

The alternatives do not automatically repair a statistical error:

- **(b), one main tag per primary group,** would require a new group-level selection rule. Selecting one tag could suppress another accepted event-level driver connection; the fact that this produces finer blocks would not establish that the change is valid. [E3] [E4] [E5] [E6]
- **(c), requiring identical main tags,** would make a within-group difference an inconsistency by definition. Neither the primary-group rule nor the supplied driver tests establishes that requirement. A mismatch warrants checking the evidence, but it does not by itself justify forced relabelling or exclusion. [E1] [E4] [E5]

### How this works with the order of operations

1. **Step 3:** readers independently assign event groups, full tag sets, and main assignments under the frozen selection rule. They do not need final primary groups to make those event-level assignments. [E1] [E4]
2. **Step 3b:** adjudicate primary-group and main-tag disagreements with recorded evidence. Check mixed-tag primary groups for actual grouping or tagging errors. If the evidence confirms both the primary group and its differing main tags, keep them. Unresolved primary-group disputes follow E1; unresolved main assignments follow Q2. [E1] [E4] [E7]
3. **Step 4:** exclude unresolved events, test the retained-sample minima, and freeze the retained primary groups and event main tags. [E1] [E4]
4. **Step 5:** form connected components from both accepted link types. Do not retag, split, or drop accepted relationships because the resulting blocks are inconvenient. [E1] [E4] [E7]

Preserving **two adjudicated main tags on two different events in a validated primary group** is different from allowing **two unresolved candidate main tags on one event** to link. The former preserves accepted inputs and an accepted primary relationship; the latter substitutes extra links for an unsettled decision and reverses option A. [E1] [E2] [E3] [E4]

If a valid construction fails E6’s admissibility rule, “sensitivity inference not established” is a limitation of that analysis. A different, finer construction that might pass would not establish that the original failure was mistaken. [E6] [E7]

## Q4 — Is the amended step mechanical?

**Step 5 can remain mechanical; the whole process is not judgment-free.** Once the retained primary groups and adjudicated main tags are frozen, A1 determines the connected components, and E6 determines their resampling. Membership interpretation and evidence adjudication occur earlier, under written rules. A1–A4 alone leave those upstream choices incompletely specified. [E1] [E4] [E5] [E6]

The operational meaning of “No judgment is exercised at this step” should therefore be: **Step 5 accepts frozen inputs and permits no new tag selection, discretionary link deletion, or regrouping in response to block counts or results.** [E1] [E4] [E7]

### Single biggest remaining risk

**The main-only rule can omit dependence carried by a valid secondary driver and thereby let a PASS survive that should not.** E5 describes drivers as shared causes and allows multiple memberships; E3 and E4 expressly prevent secondary tags from linking. If a shared secondary cause is not represented by another path, the sensitivity partition does not capture that connection. Agreement and mechanical execution do not establish that the omitted connection is irrelevant. [E3] [E4] [E5] [E6]

For whether such an omission actually occurs in this pool, changes an interval, or changes the verdict: **no evidence in briefing**. It is a remaining methodological vulnerability, not a predicted result. [E4] [E5] [E6]

## Optional — Can tagging make the check toothless or unpassable?

**The amendment does not rule out either structural extreme, and its missing selection contract leaves room for tagging choices to influence them.** That is why the selection and unresolved-case rules must be fixed before tagging and cannot be adapted after counts or results become visible. [E4] [E7]

- **No additional sensitivity:** if the selected main tags add no links between distinct primary groups, the sensitivity partition equals the primary partition. E6 then reduces to resampling the primary groups and adds no broader dependence check. Whether this would reflect omitted genuine dependence or the correctly applied driver tests is **no evidence in briefing**. [E1] [E4] [E5] [E6]
- **Inadmissible sensitivity:** broad shared main tags and primary-group bridges can join components. If the retained construction has fewer than two blocks, or its resampling distribution is degenerate, E6 requires a completed run to FAIL. Outside those explicit conditions, coarser blocks do not establish a particular interval-width direction. [E2] [E4] [E6]

A2 does **not** authorize arbitrary use of “none”: it means that no driver test applies and is expressly not evidence of independence. The proposed Q2 policy must not turn an unresolved main choice into that state. [E4]

**Vendor: OpenAI**  
**Model: GPT-6 Astra Pro**