**Engine:** xAI. **Model:** Grok 4.7 (as self-reported). **Briefing:** 2026-10-25_cold_briefing_v4_grouping_v2.md. Tier 3. Filed verbatim. Path: chat → Systems Engine → file (not clipboard → file).

**Q1 — Weighting.** Choose (B): each group weight 1, a group’s score being the mean of its events.  
Under (A) the primary mean of \(d_e\) can assign nearly half the total weight to a single group while still meeting the nominal 150-group count [E4, E3]; that average no longer corresponds to “150 independent events” in the sense required by E1. Under (B) the average is the unweighted mean across dependence blocks, so each independent unit contributes equally regardless of how many events it contains. Report alongside it the group-size distribution, the share of events in the largest groups, and \(N_{\text{eff}}\) [E3, E7]. The E1 claim (“250 resolved markets across 150 independent events”) still describes the eligibility floor but no longer describes the weighted quantity being tested; the primary endpoint must be stated as the unweighted mean across groups.

**Q2 — Ordering by title.** Unsafe. Ordering singletons by normalised `title` after `resolutionSource` reopens the matching-without-a-contract failure by another door [E6, E8 step 2].  
Even as a “reading aid only,” adjacency by shared title tokens can cause a reviewer to notice and then join events that would not have been joined from the definition alone, exactly the structured false-match pattern already recorded. No written contract can bind it once the titles are visible in the packet. Instead order untagged singletons by a non-text key already copied in step 1 (for example `resolutionSource` then `eventDate` then a hash of `conditionId`), so that same-fact events without API tags are not systematically placed next to each other by wording.

**Q3 — Agreement threshold.**  
(i) Compute joined-pair agreement only on the pairs that at least one reader joined (the set already named in E8 step 3b); do not include the large number of pairs neither reader joined. Report the fraction of those pairs on which both readers agreed to join, and the fraction on which they disagreed.  
(ii) No evidence in briefing supports any particular number; E7 states that none of the three readers named one, and no block supplies a calibration or power argument for a threshold.  
(iii) Below the threshold the step fails under E9; do not adjudicate anyway and do not introduce a third reader after seeing the disagreement count.

**Q4 — Pre-registrable?** No. A cold auditor cannot follow and check design v2 plus its fail conditions without talking to the authors, because the joined-pair agreement threshold remains unset [E9] and the definition’s edge cases (overlapping windows, sequential legal steps) still lack enumerated decision rules [E8].  
The single biggest remaining way it could produce a PASS or FAIL that is not real is residual dependence among the final groups that share an unnamed common driver; the bootstrap treats groups as independent while the sensitivity grouping only recomputes under one pre-declared broader partition [E3, E8 step 5, E9].

**Optional.** Yes. Because the agreement threshold is required but not numerically fixed before Step 3 [E9], and because adjudication defaults to merge when evidence does not settle a disagreement [E8 step 3b], a thin or arbitrary grouping can still be frozen once the readers produce any partitions that clear an after-the-fact threshold or that are forced together by the merge rule. Nothing in E8 or E9 forces the process to declare that its independence claim has failed when the residual-dependence limit is reached.

**Filing.** Vendor: xAI Model: Grok 4.7
