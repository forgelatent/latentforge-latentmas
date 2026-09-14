# Gate 4 cold re-read handoff — September 14, 2026

**From:** v2 selection session (fresh pool pulled, 15 picks Founder-approved
per-item, CANDIDATE committed).
**Job for next session:** Gate 4 cold re-read ONLY, then if confirmed:
promote, repoint loader, archive v1. Prior handoffs remain binding
(2026-07-12_v2_selection_session_handoff.md: rules 3a-3f, gates, archive
note template; 2026-07-12_gate2_gate3_close_handoff.md: session texture).

## State at close (all Tier 1, all committed)

- **CANDIDATE exists:** `benchmark_registry_v2_CANDIDATE.json`, sha256
  b5e9f9cd8a93b85368bb969537b7dc873d6d92be37d6766eae19f29812acec4f,
  commit 03ffbff. 15 markets, every entry a verbatim pool record.
- **Pool-of-record:** `scratch/qualifying_pool_2026-09-14.json`, sha256
  160b262836a8f6749e5712d0b9986a936d515b86bd564b5fc29d1df08d158380,
  12,640 markets, commit fd34111. Both completeness checks PASSED at pull.
- **Pull tool:** `scratch/full_pull_and_filter_v3_1.py` (auto-split
  traversal, sha256 e1b6e97c...). July artifacts untouched alongside.
- **Deviation on record:** July close handoff said select from the
  2026-07-12 pool; Founder approved fresh pull instead (64-day staleness).
  Rationale in commit fd34111.
- HEAD at close: 03ffbff.

## Cold re-read procedure (Gate 4)

Fresh session, bootstrap bundle + this file + the two July handoffs. Then:
1. Recompute CANDIDATE and pool hashes; match the values above.
2. Re-verify all six rules from the FILE's contents alone (not this
   handoff's claims): count, per-month spread, 180d+ supply, floor,
   exceptions used, category mix.
3. Live-check each of the 15 slugs against the Gamma API: still open,
   not resolved, liquidity not collapsed. (Markets move; a pick dead by
   re-read time goes back to selection, not silently swapped.)
4. Judgment pass: would a cold reader endorse these 15 as a fair,
   spread, liquid exam? Correlations 9/12 (US-Iran pair) and 14/15
   (Vance nom -> GOP general) were accepted by Founder knowingly.
5. If confirmed: promote per the binding handoff (rename/repoint, loader
   to v2, archive v1 with the July note template, manifest updates
   including the stale mode1-loader hash noted in the July close handoff).
6. If NOT confirmed: write findings, stop. Selection reopens with Founder.

## Data-quality notes for the ledger (not yet written - queue them)

- Gamma "open-ended" (null endDate) bucket contaminated: Nov-2026 midterm
  markets carry null endDate but ~7-week runway. 3c was satisfied from
  dated 180d+ markets only. Ledger entry pending.
- Recurring-market churn doubled July->Sept; event universe ~21K. The
  auto-split traversal (probe-then-bisect, 1-hour floor) absorbs this
  going forward. Ledger entry pending.
- Pattern-minting queue from July still open (inconsistent-view pattern;
  research-sweep silent-success second instance).

## Session texture

- Terminal `>....` echo blind spot appeared twice on large pastes; both
  times interior content checks (PASS lines + ast.parse) proved the writes
  whole. The checks-inside-the-paste discipline is what makes big pastes
  safe; keep it.
- One patcher check was drafted wrong (window-count arithmetic) and
  aborted a correct edit; the abort-on-doubt design meant the cost was a
  retry, not a corruption. Second patcher check had a vestigial always-
  false OR arm - flagged in-session, harmless, but check-drafting quality
  is the weak spot to watch.

*End of handoff.*
