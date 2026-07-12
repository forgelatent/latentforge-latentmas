Cold review decision: Registry v2
Decision

Choose (c): keep v1 running on its three surviving markets while immediately selecting and locking v2. Make v2 the benchmark registry once it is ready.

A three-market v1 remains a valid record of those three fixed questions, but it is no longer a sufficiently robust primary instrument for Mode 1’s broader purpose. Mode 1 is intended to compare forecasting behavior over time on a stable set of markets, not merely preserve continuity at any cost. The current set has contracted from eight markets to three, with five genuine resolutions. [Evidence: Section 1, “fixed registry of markets…so that agent forecasting behavior can be compared across time on a stable question set”; Section 4, “Totals: 3 LIVE / 5 RETIRED of 8.”]

The hybrid option preserves everything worth preserving in v1 without allowing its accidental three-market remainder to determine the benchmark’s future. Continuing v1 is operationally cheap because the loader is already installed and explicitly supports a shrinking live count. [Evidence: Section 5, “Loader handles a shrinking live count by design”; “data is cheap, loader is installed” in option (c).]

At the same time, there is no accumulated longitudinal asset that argues for delaying v2. The loader has effectively zero days of unattended operation, and no downstream consumer currently reads Mode 1 output. [Evidence: Section 5, “effectively zero days of unattended operation”; “No downstream consumer reads Mode 1 output yet.”]

Therefore:

v1 should remain active as a legacy cohort.
v2 selection should begin now.
v2 should become the official benchmark registry when locked.
v1 and v2 results should never be combined as though they came from one unchanged registry.
Does three markets still constitute a valid longitudinal instrument?

Technically yes, but only in a narrow sense. Operationally, it should not remain the primary Mode 1 benchmark.

It is still longitudinal because the three surviving questions remain fixed within v1, satisfying Variant A immutability. [Evidence: Sections 1 and 3, “Markets are never added, removed, or swapped inside registry v1”; “Variant A immutability within a version.”]

However, the instrument has lost 62.5% of its original market coverage:

[
5 \div 8 = 62.5%
]

That is not merely a small reduction in sample breadth. The surviving registry is now dominated by the particular characteristics of three questions: China GDP, GPT-6 release, and a December Federal Reserve rate cut. [Evidence: Section 4, three LIVE market records.]

The briefing contains no predefined minimum live-market threshold and no formal statistical power requirement. Therefore, it is not in evidence that three markets are mathematically insufficient. But it is equally not in evidence that three markets provide adequate breadth for reliable benchmark-level conclusions.

Judgment: three markets are sufficient to preserve a historical v1 trace, but too fragile to carry the full benchmark role prospectively.

SPECULATION: With only three questions, measured differences among the four arms are more likely to be driven by market-specific characteristics rather than broadly repeatable forecasting behavior. The briefing supplies no variance analysis or power calculation, so this risk cannot be quantified from the evidence provided.

Why not option (a)?

Running out v1’s clock would prioritize registry continuity even though almost no usable continuity has yet accumulated. [Evidence: Section 5, “effectively zero days of unattended operation.”]

It would also require inventing a “natural endpoint.” None is currently defined. [Evidence: Section 7, option (a), “definition of endpoint would be needed.”]

Possible endpoints such as “all markets retired,” “only one remains,” or “December 2026” are not established by the locked architecture and would be arbitrary unless separately adopted.

Most importantly, option (a) would leave future Mode 1 comparisons dependent on only three questions for potentially months. The possible runway does not solve the breadth problem; it only extends it. The Systems Engine’s runway interpretation is plausible, but the exact resolution timing of China GDP is not established as Tier 1 or Tier 2 evidence. [Evidence: Section 6 is explicitly Tier 3.]

Why not pure option (b)?

Triggering v2 now is directionally correct, but there is no operational reason to terminate v1 immediately.

The loader is working, the retired markets are being classified correctly, and continuing to collect the three surviving series is inexpensive. [Evidence: Section 4, “loader classified these correctly”; Section 5, “Loader handles a shrinking live count by design.”]

Keeping v1 running has three benefits:

It preserves an auditable record of the original registry.
It supplies early operational evidence from the installed loader.
It allows future analysis of the surviving markets without pretending they belong to v2.

None of those benefits conflicts with selecting v2 now.

Recommended transition rule

Adopt the following version boundary:

Registry v1 remains an active legacy registry until all its markets retire or until an explicit archival decision is made. Registry v2 becomes the official Mode 1 benchmark on the date its registry is locked and its first conforming snapshot is produced. Data from v1 and v2 are reported as separate versioned cohorts.

This preserves the locked rule that markets cannot be swapped inside a version. [Evidence: Sections 1 and 3.]

It also avoids calling the v2 transition a continuation of the v1 time series. Changing the questions necessarily creates a new longitudinal series, which is exactly why the architecture provides registry versions. [Evidence: Section 1, “Moving to a new set is a version decision.”]

Round 3 rules that should carry over
1. Preserve immutability within each version

This is the central design rule and should remain unchanged. Stability of the question set is explicitly identified as Mode 1’s load-bearing property. [Evidence: Section 1.]

No market should be added, removed, or replaced inside v2 after it is locked. Retirement should change market state, not registry membership.

2. Regenerate the selection pool from current data

Do not select v2 directly from the May 26 pool.

The prior pool contains 298 qualifying markets, but its data is from May 26 and the briefing explicitly states that it would need regeneration for a v2 selection. [Evidence: Sections 2 and 5.]

The existing scripts may be reused as tooling, but their output should be regenerated.

3. Retain a meaningful liquidity qualification rule

Round 3 used a $10,000 liquidity floor, with two named soft exceptions. [Evidence: Section 2.]

The basic principle should carry over because it provided an explicit, reviewable eligibility criterion. There is no evidence in the briefing that the liquidity floor caused the five retirements; every retirement was due to normal closure rather than identity failure or data loss. [Evidence: Section 4, “All 5 retirements have cause_of_death: closed.”]

Therefore, the retirement event does not support abandoning liquidity screening.

4. Require explicit documentation for exceptions

The two v1 exceptions were named and quantified: China GDP at approximately $4,000 and SCOTUS at approximately $5,000. [Evidence: Section 2.]

Any v2 exception should likewise be individually identified and justified before the registry is locked. Exceptions should not become an undefined discretionary category.

5. Preserve verification before lock

All eight v1 markets were verified live during contract synthesis and loader verification. [Evidence: Section 2.]

The same pre-lock verification principle should carry over to v2, particularly because the registry is immutable once locked.

Round 3 rules that should change
1. Add explicit deadline-diversity constraints

The v2 selection process should prevent too much of the registry from sharing the same or closely clustered resolution window.

Four of the five retired question names contain an explicit June 30 deadline:

Israel–Iran permanent peace deal by June 30
Anthropic best AI model at the end of June
Iran uranium surrender by June 30
Crude oil at $120 by the end of June

[Evidence: Section 4 market names.]

The briefing says the five resolutions occurred around June 30, approximately five weeks after selection. [Evidence: Sections 4 and 5.]

Thus, even without relying on the Systems Engine’s interpretation, the raw market names and retirement timing establish substantial deadline clustering.

A v2 rule should cap the percentage of markets expected to resolve in any single short time window. The precise window and cap are not in evidence and must be set as governance parameters.

2. Add a minimum remaining-runway rule at selection

A market may be live when selected but still have very little useful measurement life remaining.

The registry was selected May 26, and five markets resolved around June 30. [Evidence: Sections 2, 4 and 5.]

Therefore, “live at selection” is not by itself an adequate longevity criterion for a longitudinal registry.

Each candidate should be evaluated for expected remaining observation time. Hard-dated questions approaching resolution should either be excluded or limited as a portion of the registry.

The exact minimum runway is not in evidence.

3. Increase the initial market count or establish an attrition-resilience requirement

Eight markets proved vulnerable to one clustered retirement event: five closures reduced the active set to three. [Evidence: Section 4.]

The evidence supports changing the resilience requirement, although it does not establish one uniquely correct v2 count.

A defensible rule would be:

Select enough markets that a foreseeable cluster of normal resolutions does not immediately reduce the registry below its declared minimum viable breadth.

SPECULATION: A larger registry would generally reduce dependence on individual markets, but the briefing contains no cost analysis, statistical power calculation, or operational ceiling from which to derive an exact number.

Consequently, I would not prescribe a specific figure such as 12, 16, or 20 from this evidence alone. The v2 decision record should declare both:

the initial market count; and
the minimum live-market count below which planning for the next version is automatically triggered.
4. Define version-trigger criteria before v2 launches

The present review exists because no natural endpoint or minimum live count was established. [Evidence: Section 7, option (a).]

V2 should therefore be accompanied by a prospective trigger policy. Possible trigger dimensions include:

absolute live-market count;
percentage of registry retired;
concentration of remaining markets;
elapsed time since launch;
proximity to clustered deadlines.

The exact thresholds are not in evidence. They should be decided before v2 begins, not after its first major attrition event.

5. Amend the loader request limit before adopting a larger v2

The bulk URL currently has no explicit limit parameter. At eight markets, truncation fails loudly through the identity check, but the briefing says a larger v2 requires an explicit limit. [Evidence: Section 5.]

This is not a redesign of the loader contract; it is a known prerequisite already identified in the operational record.

The limit change should be completed and verified before the first official v2 run if the registry expands.

Category mix

The briefing does not describe the Round 3 category-allocation rule, if one existed. It lists the resulting markets, but it does not state required category proportions or the reasoning used to determine them.

Therefore:

Maintaining cross-category breadth is directionally consistent with avoiding dependence on a narrow question type.
The exact Round 3 category rule is not in evidence.
No specific category allocation should be claimed as a carryover requirement based solely on this briefing.

Any v2 category-mix rule should be documented explicitly rather than inferred retrospectively from the eight v1 markets.

Liquidity floor recommendation

Carry forward the $10,000 floor as the default starting rule, subject to validation against the newly regenerated pool. [Evidence: Section 2.]

Do not automatically carry forward the two specific soft exceptions; those exceptions belonged to individual v1 markets. Instead, carry forward the exception process:

exceptions must be named;
the liquidity shortfall must be stated;
the reason for accepting the shortfall must be documented;
the aggregate number of exceptions should be constrained.

The evidence provides no basis for raising or lowering the $10,000 figure. Any numerical change would require evidence from the regenerated pool or operating performance not included here.

Final determination

The 5-of-8 retirement should trigger the v2 process now.

The decisive facts are:

the registry has contracted to three live markets; [Section 4]
the contraction occurred only about five weeks after selection; [Section 5]
essentially no unattended v1 time series has accumulated; [Section 5]
no downstream consumer depends on v1 today; [Section 5]
the loader can continue recording v1 without interfering with v2; [Section 5]
changing the market set is already permitted through versioning. [Sections 1 and 3]

Accordingly, v1 should be retained as a separate legacy series, while v2 is selected from a regenerated pool under improved attrition-resilience rules.

Disposition: (c) Hybrid — trigger v2 now, continue v1 separately, and promote v2 when locked.