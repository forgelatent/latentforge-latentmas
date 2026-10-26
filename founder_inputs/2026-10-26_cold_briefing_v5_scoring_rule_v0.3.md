# Cold briefing v5 — scoring rule v0.3 and the driver list (October 26, 2026)

**To the reader:** you have no terminal and no file access. Everything you may rely on is in the evidence blocks E1–E6 below, copied verbatim from committed project files or from the CANDIDATE under review. Cite the block for every claim you make ("[E3]"). If the blocks do not support a claim, write "no evidence in briefing" rather than filling the gap. The Founder's view and the Systems Engine's view on every question are deliberately withheld. Do not propose a model. Do not estimate how many groups the pool will produce. At the end, state your vendor AND model name.

**What is being reviewed.** (1) Scoring rule CANDIDATE v0.3 for an experiment that asks whether agents communicating in latent states forecast resolved prediction markets better than the same agents communicating in text. v0.3 folds in an agreed grouping design (v3) and three Founder decisions. Four items in it are marked proposed, not decided. (2) A closed list of 31 "drivers" used only for a sensitivity check; its grain at the broad end is an open Founder decision. Nothing is implemented. The grouping has not been performed. No forecast has been made.

---

## E1 — Founder decision note, items 2, 5 and 9 (committed, amended October 25)
> 2. **What "proven" means (replaces the $10M figure).** On at least 250 resolved markets across at least 150 independent events from the collected Polymarket data, where the independent unit is the pre-registered outcome group and each group has equal weight in the primary score, the latent arm beats the text arm by more than the pre-registered margin, with error bars. The margin and the budget rule are set at pre-registration, not after.
> 5. **What stops me early.** Fewer than 150 independent events survive resolution lookup. No latent method passes the swap test on this task. The Mac Mini cannot run the chosen setup and $500 of GPU time cannot either. The budget rule cannot be written in a form a cold round accepts.
> 9. (a) Item 2 amended as above: the independent unit is the outcome group, each group weighted equally in the primary score (readers 3 of 3 on per-group weighting). (b) Inter-reader agreement threshold for the dependence grouping: J_human >= 0.80, chosen by me as a governance rule, not derived from evidence (readers 3 of 3 that no evidence can set it); below it the grouping step fails and this note's early stop applies; no third reader. (c) The sorters' review list may be ordered by resolution source, then event date, then normalised title, under the written contract that order is never evidence (readers 2 of 3); the cross-list check is required regardless.

## E2 — Grouping design v3, agreed October 25 (committed `2e1bf84`); excerpts
> **Definition.** An outcome group is a pre-declared dependence block, used for resampling and as the unit of primary weight. Two events are linked when (a) they resolve on the same proceeding, office, legal action, legislative instrument, or event instance; or (b) one event's resolution mathematically or legally restricts the valid outcomes of the other; or (c) they track the same named underlying measurement or process over overlapping *outcome windows*, where an outcome window is the period that the event's written resolution conditions say the outcome is measured over, with the boundary text recorded. [...] Final groups are the connected components of all accepted links. Different group ids do not establish independence.
> **Step 3 — two blind partitions plus driver tags.** [...] Each reader, for every event: (1) assigns it to a group or marks it unresolved; (2) assigns zero or more drivers from the closed list, or "none".
> **Step 3b.** [...] **If J_human < 0.80 the step fails** (Fail conditions). Otherwise adjudicate every material disagreement with recorded evidence. If the evidence does not settle it, every event in the disputed pair or component becomes unresolved. No default merge; no default split. [...] No third reader.
> **Step 4 — exclusions, then freeze.** Every unresolved event is removed from the confirmatory sample, with its markets. [...] Only now count. Test both minima on the retained sample: at least 250 markets and at least 150 primary groups. Report the group-size distribution, the number of groups with two or more events, the largest group's share of events, and the sensitivity-partition count beside it, never in place of it.
> **Step 5 — sensitivity partition, mechanical.** Two events are in one sensitivity block if they share any adjudicated driver tag or are in one primary group; blocks are connected components. No judgment is exercised at this step. The primary endpoint is recomputed with the same per-group weights and the same group means, resampling sensitivity blocks instead of primary groups. A PASS that does not survive is reported as not established. The resampling and normalisation formula is written out in the pre-registration.
> **Fail conditions.** The grouping step fails, and the decision note's early stop applies, if after Step 4: fewer than 250 markets or fewer than 150 primary groups are retained; or J_human < 0.80; or the driver list cannot be written with one-line membership tests before Step 1. None of these may be cured by splitting, by changing the definition or the lists, by re-including an unresolved event, by adding a reader, or by rerunning review with any count visible.

## E3 — Step 0b lists CANDIDATE (committed `1f30486`): the driver list, in full, and its grain note
How to use: for each event, a sorter assigns every driver whose test the event passes, or `none`. Tests are applied to the question text and the event description. A driver written `Dnn-<X>` takes a parameter copied from the question. Multiple drivers on one event are allowed and expected. A driver is a *shared cause*, broader than a group; passing the same driver test never by itself puts two events in one primary group.

| Id | Driver | Membership test (one line) |
|---|---|---|
| D01 | US–Iran conflict and negotiations, 2026 | The outcome depends on hostilities, ceasefire or negotiation between Iran and the US, Israel or a Gulf state; on shipping or control in the Strait of Hormuz; on Iranian leadership, sanctions, or the rial; or on Iran's participation or exclusion from an international event. |
| D02 | Yemen / Red Sea conflict, 2026 | The outcome depends on fighting or a ceasefire involving the Houthis, Saudi Arabia or Israel in or over Yemen. |
| D03 | Russia–Ukraine war: front line and peace process | The outcome depends on territorial control in Ukraine, on Russia–Ukraine negotiations, or on a meeting, call or clash whose stated subject is that war (including NATO–Russia and Trump–Putin/Zelenskyy contacts about it). |
| D04 | Russian domestic politics, 2026 | The outcome is a Russian federal, regional or local election result, or the tenure of a Russian office-holder. |
| D05 | US Federal Reserve, 2026 | The outcome is a Federal Reserve rate decision, dissent, or sequence of decisions, or the tenure of the Fed Chair. |
| D06 | US macroeconomic statistics, 2026 | The outcome is a published US statistic (inflation, unemployment, GDP) for a stated period. If the question names no country, the description decides; if neither does, the event is unresolved. |
| D07-<country> | National statistical release, by country | The outcome is a published statistic of the named country for a stated period (GDP, inflation, unemployment). One driver per country. |
| D08-<bank> | Central-bank decision, by bank (not the Fed) | The outcome is a rate decision of the named central bank. One driver per bank. |
| D09-<state> | US 2026 primaries and nominations, by state | The outcome is decided by a 2026 party primary, primary runoff, caucus or nomination contest in the named US state or territory, for any office. One driver per state. |
| D10-<city> | US or Canadian municipal election, by city | The outcome is decided by the named city's 2026 mayoral or council election or its party nomination for it. One driver per city. |
| D11 | Trump's public statements and posts | The outcome is determined by what Donald Trump posts, says, praises or insults, in a stated window. |
| D12 | Trump's travel and meetings | The outcome is whether Donald Trump attends, visits, meets or speaks with a named person, event or country in a stated window. |
| D13 | Trump administration appointments and tenure | The outcome is an appointment to, departure from, or continuation in a US federal office, including the presidency. |
| D14 | US–China trade and tariffs, 2026 | The outcome depends on US–China trade measures, purchases or tariff agreements. |
| D15 | Brazil 2026 general election | The outcome is decided by Brazil's 2026 presidential, Senate or state elections, or a party's nomination for them. |
| D16 | Colombia 2026 presidential election | The outcome is decided by Colombia's 2026 presidential election, either round. |
| D17 | Peru 2026 presidential election | The outcome is decided by Peru's 2026 presidential election, either round. |
| D18 | South Korea June 3, 2026 local elections and by-elections | The outcome is decided by the South Korean elections held on June 3, 2026. |
| D19 | UK May 2026 local and mayoral elections | The outcome is decided by the United Kingdom local, council or mayoral elections held in May 2026. |
| D20 | UK Westminster by-elections and Labour leadership, 2026 | The outcome is decided by a 2026 UK parliamentary by-election or by the Labour Party's leadership process. |
| D21 | German 2026 state (Landtag) elections | The outcome is decided by a German state parliamentary election held in 2026. |
| D22 | Andalusia 2026 regional election | The outcome is decided by the 2026 Andalusian regional election or the government it produces. |
| D23 | Sweden 2026 general election | The outcome is decided by Sweden's 2026 parliamentary election or the government it produces. |
| D24 | Malta 2026 general election | The outcome is decided by Malta's 2026 general election. |
| D25 | Latvia 2026 parliamentary election | The outcome is decided by Latvia's 2026 parliamentary election. |
| D26 | Romania government formation, 2026 | The outcome is who becomes, or when someone becomes, Romania's Prime Minister. |
| D27 | China–Taiwan military action | The outcome is whether China invades or blockades Taiwan in a stated window. |
| D28 | Israel–Hamas ceasefire | The outcome depends on the state of the Israel–Hamas ceasefire. |
| D29 | Quebec 2026 general election | The outcome is decided by Quebec's 2026 general election. |
| D30 | British Columbia politics, 2026 | The outcome is decided by a 2026 election or party leadership contest in British Columbia. |
| D31-<country> | Other national or regional election, by country | The outcome is decided by a 2026 election in a country not named above (one driver per country), including presidential, parliamentary, regional, mayoral and leadership contests there. |
| none | — | No test above applies, or the outcome is a sports result, an entertainment vote, a corporate figure, a referendum not tied to an election above, or a personal-life event of a named individual. |

> Notes on grain, so the Founder can judge the list: D01, D03, D09 (summed over states), D15, D05, D06 and D11 are the broad drivers; on a first read each of the first two would touch dozens of events. That is intended: the sensitivity partition exists to show what happens if those shocks are treated as one block, and its count is reported beside the primary count, never in place of it (v3, Step 4). Two deliberate omissions: there is no "Trump" driver and no "US politics" driver, because "same topic" is not a shared cause; the three Trump drivers (D11, D12, D13) are three different processes. There is no "geopolitics" driver for the same reason.
> **Still open at Step 0b.** [...] Whether the Founder wants fewer or more drivers at the broad end (D01, D03, D09, D15): fewer risks missing a real shock; more risks the sensitivity partition collapsing into a few blocks, which Gemini named as a false-FAIL mechanism.

## E4 — Scoring rule CANDIDATE v0.3 (not yet committed; drafted October 26); excerpts
> **The data:** 410 resolved markets (81 YES, 329 NO). The file holds 292 events; 291 carry resolved markets and one carries only STILL_OPEN markets and is never in the confirmatory sample.
> **[v0.3] Sensitivity block:** the connected components of "same primary group OR shares an adjudicated driver tag" (v3, Step 5). Used only to recompute uncertainty (section 7); never a unit of weight.
> **D (deranged control):** identical to L, except B receives the latent states of a donor draft written by agent A for a market in a different primary group. **[v0.3, proposed, open]** Where sensitivity blocks exist, the donor is drawn from a different sensitivity block as well, so that no driver is shared; the donor is chosen by a seeded deterministic rule fixed at pre-registration, matched on draft length within a stated tolerance and on format. B's own input is unchanged.
> **BR (base rate):** a constant forecast equal to the pool's YES rate computed leaving out the group being scored. Leave-one-out is by group, not by event.
> **Per group:** mean of its events' per-event Brier (each event weight 1 within its group). Each group has weight 1 in every arm-level score and in the primary endpoint. **Primary endpoint:** paired difference per group, d_g = Brier_T(g) − Brier_L(g). Positive favors latent. Report the mean of d_g over groups with a 95% bootstrap interval; the bootstrap resamples primary groups (10,000 resamples, with replacement, equal probability per group).
> **Sensitivity recomputation (v3, Step 5), written out:** the statistic is unchanged — the equal-weight mean of d_g over primary groups — and only the resampling unit changes. Each resample draws sensitivity blocks with replacement (equal probability per block); every primary group inside a drawn block enters the statistic once per draw of its block; the resample's value is the mean of d_g over the groups so entered. 10,000 resamples; 95% interval. The point estimate under sensitivity is therefore the same number as the primary point estimate; what moves is the interval.
> **Divergence:** a market is "divergent" if |p_L − p_T| ≥ delta. delta is pre-registered. Proposed 0.10; unaddressed by any cold round; still open.
> **Gates (both required; both 95% group-bootstrap intervals; Brier, not accuracy):** Gate 1, pairing: mean over groups of Brier_D(g) − Brier_L(g) > 0, interval excluding zero. Gate 2, usefulness: mean over groups of Brier_S(g) − Brier_L(g) > 0, interval excluding zero. Both gates are also recomputed under the sensitivity resampling and reported. Whether a gate must also survive sensitivity to count as met is open; the primary endpoint must.
> **Pass:** primary-endpoint interval entirely above the pre-registered margin m under primary-group resampling, AND the sensitivity interval entirely above m (proposed reading of v3's "survives"), AND Gate 1, AND Gate 2, AND L beats BR. **Fail:** a valid run that does not pass. [...] A primary PASS whose sensitivity interval does not clear m is reported as "not established under the sensitivity partition" and is a FAIL. **Void:** only for execution or protocol failure: the information rule broken; the budget rule not satisfied; the market list, the groups file, the driver tags or any Step 0b list changed after the freeze; any group or candidate count shown to a reader during Step 3; the run incomplete. **Early stop (before any forecast):** the grouping step fails under v3's Fail conditions. This is the decision note's §5 stop, not a run outcome.
> **Margin:** m is an absolute reduction in group-averaged Brier, set at pre-registration after the noise estimate and before any T or L forecast. Noise estimate: the spread of per-group Brier differences from arms that do not involve the channel, S and BR, on the full pool, under the same group weights.

## E5 — The one external number on expected effect size (October 25 handoff, committed)
> Draft-KV (arXiv 2609.34754, Sept 28) [...]: latent beats text in 33 of 35 settings, mean +5.85 pp; on the only strong-receiver row (Qwen3-8B -> Qwen3-4B) the gap runs -0.1 to +3.8 pp, mean about +2.1. [...] No error bars on the medium gap. Its swap test gives LatentMAS 0.60 pp pairing gain of a 4.86 pp system gain on ARC-C.
Note: these are accuracy points on a QA benchmark, not Brier on this pool. The project has recorded that the size of the expected effect in Brier here is unknown.

## E6 — Project history relevant to control arms (incident ledger, committed)
A prior script in this project hard-coded a 3x cost ratio and three pre-written favorable narratives, one per verdict branch, so that no outcome could produce an unfavorable result; it is recorded as a "Pro-Thesis Optimization Loop." A prior A/B test gave its two arms different information and is recorded as not a matched comparison. The project treats any control that cannot fail, and any arm that receives different information, as a known failure shape.

---

## Questions

**Q1.** Is the written-out sensitivity recomputation [E4] a correct implementation of v3 Step 5 [E2]: same statistic, same group weights, resampling unit changed to the sensitivity block, each group counted once per draw of its block? Name any way it understates or overstates the uncertainty, or any way the point estimate could lawfully differ from the primary one. Cite the block.

**Q2.** v3 says "A PASS that does not survive is reported as not established" [E2] without defining "survive." v0.3 proposes: the sensitivity interval must lie entirely above m [E4]. Is that the right reading, or should it be "interval excludes zero," or something else? State what each reading allows a run to claim.

**Q3.** v0.3 recomputes both gates under the sensitivity resampling but leaves open whether a gate must survive it to count as met [E4]. Must they? For each choice, name the failure shape it permits, with reference to the gates' purposes (Gate 1: the channel carries task-relevant content; Gate 2: the channel beats silence).

**Q4.** The donor rule for the deranged control D [E4]: v0.3 proposes the donor comes from a different sensitivity block as well as a different primary group, chosen by a seeded deterministic rule matched on draft length and format. Is a different sensitivity block the right constraint, too strong, or too weak? What else must the rule fix for D to remain a control and not a second experiment [E6]? Could length-matching itself leak information?

**Q5.** The driver list [E3]. For each of the four broad drivers the Founder must decide on — D01, D03, D09 (summed over states), D15 — say accept, split, or merge, and why, in terms of the two named risks (missing a real shock → false PASS survives; collapsing the sensitivity partition into few blocks → false "not established"). Separately: does the closed list plus the `none` row leave any class of events that is plausibly in this pool (resolved 2026 policy, geopolitics, elections, macro) on `none` when it is in fact a shared cause? Name the class and which test you would add or widen. Do not estimate how many events any driver would catch.

**Q6.** delta = 0.10 for "divergent" markets [E4] has gone unaddressed through three cold rounds. Is 0.10 the right line in probability units? Should it scale with the group's base rate or with the forecast's distance from 0.5? Or should the divergence secondary endpoint be dropped as not pre-registrable? If kept, what would make it falsifiable rather than descriptive?

**Optional.** Is there anything in E4 that lets a run be declared PASS that should not be, that turns a FAIL into a VOID, or that lets the early stop be avoided after the grouping has failed?

**Filing.** Vendor: ____ Model: ____
