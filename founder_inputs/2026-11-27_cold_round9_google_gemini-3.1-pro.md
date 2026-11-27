**Engine:** Google. **Model:** Gemini 3.1 Pro (as self-reported). **Briefing:** 2026-11-26_cold_briefing_v9_main_driver_tag.md. Tier 3. Filed verbatim. Route: attachment → Systems Engine → file (shell cat, header prepended).

**Q1 — Choosing the main tag**

* **Is a written rule required?** Yes. Under E7, the project explicitly treats "any judgment step without a written test" and "any rule that can be bent after counts or results are visible" as known failure shapes [E7]. Leaving readers to rely on unguided judgment (even with agreement reported under A4 [E4]) allows inconsistent tie-breaking between broad geopolitical drivers and personal-activity drivers [E2, E7].
* **Proposed selection rule (under 80 words):**
> When an event passes multiple driver tests, select the single main driver using this strict priority order: (1) **Substantive domain/conflict driver** (e.g., war, elections, macroeconomic policy, regulation) over personal-activity or procedural drivers (`D11`, `D12`); (2) **Direct causal determinant** (the event outcome directly resolves that driver's condition rather than an incidental condition); (3) **Lowest numerical driver ID** (`D01` before `D03`) if two drivers tie on rules 1 and 2.


* **Application to E2's example:** For a Trump meeting whose stated subject is the Russia–Ukraine war (passing both `D03` and `D12` [E5]), Rule 1 selects **`D03` (Russia–Ukraine war)** over **`D12` (Trump's travel and meetings)**, preventing `D12` from bridging `D03` into unrelated geopolitical blocks [E2, E5].
* **Failure shape permitted:** Using a deterministic tie-breaker (such as lowest ID) when two substantive conflict drivers genuinely co-determine an outcome still forces an arbitrary cut that can fragment true macro-dependence across separate sensitivity blocks, potentially understating block variance [E2, E6].

**Q2 — Unsettled main tags**

* **Option (a) — Event carries no main tag:**
* *Effect on sample/interval:* Retains the event in the sample, but strips its driver link so it stays isolated in its primary group [E1, E4]. This creates smaller, more numerous sensitivity blocks ($K$ increases), narrowing the bootstrap interval [E6].
* *Wrong verdict made more likely:* **False PASS** (easier to clear margin $m$ because the sensitivity interval narrows toward the primary-group interval) [E6].


* **Option (b) — Event becomes unresolved and is excluded with its markets:**
* *Effect on sample/interval:* Shrinks the retained confirmatory sample (risking the 250-market / 150-group minima in Step 4 [E1]) and discards contested cross-cutting events from both primary and sensitivity analyses [E1].
* *Wrong verdict made more likely:* **False FAIL / VOID** (loss of statistical power widens intervals or triggers Step 4 sample-size failure) [E1, E6].


* **Option (c) — Both tags link for that event:**
* *Effect on sample/interval:* Re-introduces the exact bridge-node flaw identified in E2, merging distinct driver blocks into mega-blocks ($K$ drops sharply), which widens the bootstrap interval or triggers E6's admissibility failure ($K < 2$) [E2, E6].
* *Wrong verdict made more likely:* **False FAIL / "sensitivity inference not established"** (artificially inflated interval or degenerate block count) [E2, E6].


* **Choice:** **Option (b) (treat as unresolved and exclude, matching v3 Step 3b [E1])**, paired with the written priority rule from Q1 so unresolvable ties rarely occur. Because v3 Step 3b already enforces "No default merge; no default split" and marks unsettled partition disagreements as unresolved [E1], applying Option (b) prevents both artificial block fragmentation (Option a) and bridge-node mega-blocks (Option c) [E2, E6].
* **Separate pass/fail threshold for main-tag agreement:** **Yes.** Without a threshold, low main-tag agreement indicates the driver taxonomy or priority rule failed, yet the sensitivity check would still run on noisy tags (a control that cannot fail [E7]). Setting a governance threshold (analogous to $J_{\text{human}} \ge 0.80$ [E1], exact threshold value: no evidence in briefing) where falling below it fails Step 3b prevents a degraded sensitivity test from rubber-stamping a PASS [E1, E7].

**Q3 — Primary groups as bridges**

* **Does it join blocks like E2?** **Yes.** Under A1, two events are in one sensitivity block if they carry the same main driver tag *or* are in one primary group, taking connected components [E4]. If Event 1 in Primary Group G has main tag `D03` and Event 2 in Group G has main tag `D12`, Group G acts as a bridge node joining the entire `D03` block and `D12` block into one component [E2, E4].
* **Is it a hole or correct behavior?** It is a **hole to repair**, because primary groups are narrow sets of events resolving on the same fact [Intro, E5], whereas drivers are macro shared causes [E5]; allowing inconsistent event-level tags inside one primary group re-creates the transitive bridge-node collapse banned by the Founder in E3 [E2, E3].
* **Choice:** **Option (c) — Require events in one primary group to share a main tag, and treat a mismatch as a disagreement to adjudicate.**
* **How it works given blind Step 3 order:** Readers still tag events blind in Step 3 before primary groups are finalized [E1, E4]. In Step 3b, immediately after the primary-group partition is adjudicated and frozen [E1], an automated check inspects every retained primary group for conflicting main driver tags across its member events; any primary group containing multiple distinct main tags is flagged for Step 3b adjudication using the Q1 priority rule (or marked unresolved under Q2(b) if evidence does not settle which main tag governs the primary group) [E1, E4].

**Q4 — Is the amended step mechanical?**

* **Is Step 5 still mechanical?** **Yes**, Step 5 itself remains purely mechanical ("No judgment is exercised at this step" [E1]) because once Step 3b freezes the adjudicated primary groups and single main driver tags, Step 5 merely computes connected components via a deterministic graph algorithm [E1, E4]. All human judgment is confined to Steps 3 and 3b [E1, E4].
* **Single biggest remaining failure risk:** Because A4 explicitly omits any pass/fail threshold for main-tag agreement [E4] and E5 notes the 31-driver list is still under revision [E5], readers can assign heterogeneous or sparse main tags during Step 3—producing either fragmented micro-blocks (making sensitivity resampling indistinguishable from primary-group resampling, letting an invalid PASS survive [E4, E6]) or over-broad driver assignment (collapsing $K < 2$ blocks and triggering a spurious "sensitivity inference not established" FAIL under E6 [E6]).

**Optional**

* **Yes.** Under E4 (A2 and A4), two choices during tagging can make the check toothless or unpassable:
1. **Toothless (too fine):** Under A2, events tagged with no driver (`none`) carry an empty tag set and link to nothing [E4]. If readers aggressively tag events as `none` or split causes across narrow tags—permitted without failing because A4 sets no threshold on driver-tag agreement [E4]—nearly every primary group becomes its own singleton sensitivity block, reducing sensitivity resampling to the primary-group analysis [E4, E6].
2. **Unpassable (too coarse):** Conversely, if readers assign a single dominant macro-driver (such as a broad political actor or overarching conflict) as the main tag across most of the pool, connected components merge nearly all primary groups into fewer than two blocks ($K < 2$) or produce a near-zero-width bootstrap distribution, automatically forcing a FAIL ("sensitivity inference not established") under E6's Admissibility rule [E4, E6].



**Filing.** Vendor: Google Model: Gemini 3.1 Pro