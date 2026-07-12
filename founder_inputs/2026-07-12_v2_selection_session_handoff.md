# v2 selection session handoff — July 12, 2026

**From:** Round 5 synthesis session (same day). **Job:** select registry v2. Founder present; Founder decides.

## Decisions already made (do not re-open)

1. **v2 is triggered.** Founder decision, July 12, after cold three-engine review (unanimous direction).
2. **v1 fate: archive-on-handover.** The loader keeps reading v1 (daily exit 1 = normal) until v2 is locked and verified; then repoint the job to v2 and archive v1 the same day, with an archive note (template below).
3. **Selection rules, locked (3a-3f):**
   - 3a: 15 markets.
   - 3b: max 3 markets resolving in any one calendar month.
   - 3c: at least 5 markets open-ended or 6+ months to resolution.
   - 3d: version trigger — below 10 live, start next-version selection; below 6, urgent.
   - 3e: $10K liquidity floor; max 2 exceptions, each named, quantified, justified in writing.
   - 3f: category mix documented at selection time (write the recipe down; no quota pre-fixed).

## Gates (in order, none skippable)

- **Gate 2 — fresh pool, Tier 1.** The May 26 pool is stale. Regenerate before selecting.
  First move: `ls -la scratch/` and identify the Round 3 diagnostic/selection tooling by CONTENT
  (grep for 'liquidity' / 'markets'), not by filename (Pattern C). Do not invent script names.
  Selection happens ONLY against the fresh pull's output. No market may be proposed from an
  engine's general knowledge — that is the seed-file shape.
- **Gate 3 — loader limit fix before lock.** Add explicit `limit` param to `build_bulk_url`
  (ledger, July 11 afternoon). Gates: ast.parse clean, --selfcheck still returns 8/8 on v1,
  new hash recorded. Ships BEFORE v2 is locked.
- **Gate 4 — candidate then confirm.** Commit selection as `benchmark_registry_v2_CANDIDATE.json`.
  Promotion to locked v2 requires a cold re-read in a FRESH context (tomorrow morning's five
  minutes is fine). Only after promotion: repoint loader, archive v1.

## Archive note template (apply to v1 at handover, three places: registry companion note, manifest mode1-loader entry, ledger)

> ARCHIVED July 2026. Registry v1 ended early: 5 of its 8 markets shared ~June 30 deadlines and
> resolved together five weeks after selection. No longitudinal data was lost (zero accumulated).
> v2 selection rules add deadline diversity (3b), long-runway share (3c), and a version trigger
> (3d) specifically to prevent recurrence. See Round 5 record, incident_ledger.md July 12, 2026.

## Do / do not

- DO run selection against the fresh Tier 1 pool only; cite pool line for every pick.
- DO check every candidate against 3a-3f before proposing it to the Founder.
- Do NOT re-open decisions 1-3 above or Round 3's validity.
- Do NOT combine v1 and v2 data as one series, ever (ChatGPT transition rule, adopted).
- Do NOT promote CANDIDATE to locked v2 inside the selection session (Gate 4).
- Do NOT treat loader exit 1 as failure (recurring; it persists until handover).

## Context notes

- Taint: none. The synthesis session saw no pool data and proposed no markets.
- Round 5 is CLOSED; engine responses need no further weighing. Briefing Section 6's
  date-clustering read was independently verified at Tier 1 (4 of 5 retired slugs carry
  explicit June-30/end-of-June dates).
- Founder preferences: plain language offered proactively; per-item approval on deletions;
  keep moving, keep the gates.

*End of handoff.*
