# Gate 2/3 close handoff — July 12, 2026 (late evening)

**From:** v2 selection continuation session (Gate 2 completed, Gate 3 completed).
**Job for next session:** Gate 4 ONLY — select 15 markets from the fresh pool,
commit as CANDIDATE, stop. Both prior handoffs
(`2026-07-12_v2_selection_session_handoff.md`, rules 3a-3f and gates;
`2026-07-12_gate2_continuation_handoff.md`, API findings context) remain binding.

## State at close (all Tier 1, all committed)

- **Fresh pool EXISTS:** `scratch/qualifying_pool_2026-07-12.json` — 4,040 markets,
  77 open-ended, hash `e5228143...`, commit `e1b19af`. Complete by construction
  (two fail-loud completeness checks, both passed; both fired on real holes during
  development first). THIS is the only valid selection source. Cite pool line for
  every pick.
- **Pull tool:** `scratch/full_pull_and_filter_v3.py`, hash `baedffec...`. Event-
  windowed traversal; details in ledger July 12 entry (commit `e8f5d14`).
- **Gate 3 DONE:** loader `build_bulk_url` now sends explicit `limit`
  (commit `e8f6e1d`, new file hash `8ce0ca39...`). Selfcheck 8/8 on v1 with live
  fetch, post-edit. **Manifest mode1-loader entry still cites old hash `f487be95`
  — needs one-line update, ride it with the next manifest edit.**
- Ledger July 12 Gate 2 entry: eight API findings, committed `e8f5d14`.
- HEAD at close: `e8f6e1d`.

## For the selection session (Gate 4)

- Rules 3a-3f from the binding handoff govern. Check every candidate against all six.
- Domain spread available in pool: geopolitics 483, ai-tech 237, policy 187,
  macro 111, crypto 103, other 2,919. The "other" bucket is keyword-tagger
  spillover — spot-check it; good candidates hide there mislabeled.
- 77 open-ended markets available for rule 3c's long-runway leg; far-dated
  (2027-2028) markets also qualify.
- Liquidity floor 3e filters at SELECTION time, not in the pool (by design —
  the pool deliberately includes below-floor markets so exceptions are choosable).
- v1's date-clustering failure is the thing 3b/3c exist to prevent. When tempted
  by a cluster of interesting markets sharing a deadline month: that's the trap,
  max 3 per calendar month.
- Commit as `benchmark_registry_v2_CANDIDATE.json`. Do NOT promote in-session.
  Cold re-read in a fresh context (Gate 4), then repoint loader, then archive v1
  with the note template from the binding handoff.

## Session texture (do/do-not for the fresh reader)

- DO judge API behavior by result content, never by HTTP 200. The API silently
  ignores unknown params, silently caps limit at 100, and serves inconsistent
  views between /markets and /events (ledger finding 7 — the headline).
- DO content-verify every heredoc paste AND every multi-variable shell loop
  (zsh word-splitting failure this session; loops now on the same footing).
  Terminal echo shows `>....` blind spots on large pastes — five out of five
  were false alarms tonight, verified whole by grep, but check every time.
- DO use the exactly-one-match-or-abort Python edit pattern for file changes;
  it aborted zero times incorrectly tonight and caught nothing bad because
  nothing bad happened — but it's the reason we know that.
- Do NOT rerun the pull tomorrow expecting identical numbers; the pool is a
  timestamped snapshot of a moving surface (window counts shifted between
  same-evening runs). Selection uses the committed 2026-07-12 pool as-is.
- Do NOT treat the "other" domain tag as meaning uninteresting.
- Pattern-minting queue for a fresh session: (a) inconsistent-view finding —
  possible new API-pathology pattern; (b) research-sweep silent-success second
  instance (July 12 morning entry) — minting decision was already deferred once.

## Founder context

Long day: Round 5 synthesis (morning), selection session #1 (afternoon),
this continuation (evening). Three sessions, five commits, zero shortcuts
taken under fatigue — the two check failures during v3 development were both
real holes caught by design, not process breakdowns. Founder preference
confirmed again: plain-language explanations proactively, per-item approval
on canonical-file changes, keep moving but keep the gates.

*End of handoff.*
