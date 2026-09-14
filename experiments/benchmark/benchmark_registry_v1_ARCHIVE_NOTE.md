# benchmark_registry_v1.json — ARCHIVED

**Archived:** September 14, 2026 (decision taken July 12, 2026; executed at v2 handover)
**Superseded by:** `benchmark_registry_v2.json` (repo root), locked September 14, 2026
**Loader:** `04_market_state_loader.py` repointed to v2 at commit `1665078`

---

## Archive note (July 2026 template, as ratified)

> ARCHIVED July 2026. Registry v1 ended early: 5 of its 8 markets shared ~June 30 deadlines and
> resolved together five weeks after selection. No longitudinal data was lost (zero accumulated).
> v2 selection rules add deadline diversity (3b), long-runway share (3c), and a version trigger
> (3d) specifically to prevent recurrence. See Round 5 record, incident_ledger.md July 12, 2026.

## State at handover

v1 continued to be read by the loader from the July decision through September 14, 2026, under the
agreed archive-on-handover policy (loader keeps reading v1, daily exit 1 is normal, until v2 is
locked and verified). Final state on the September 14 04:58 scheduled run: **1 live, 7 retired** —
past the 3d urgent threshold of below 6 live.

## What v1 taught v2

- **3b (max 3 settling per calendar month)** exists because of v1's date-clustering failure. During
  the v2 Gate 4 cold re-read, 3b caught a four-market cluster the candidate had passed by bucketing
  on `end_date`. See `founder_inputs/2026-09-14_gate4_findings.md` finding F1.
- **`endDate` is unreliable** — first recorded June 27, 2026 (Fed December market trading past its
  stated end date). v2 carries a `settlement_month` field derived from question text, because the
  Gate 4 re-read found `end_date` misrepresenting settlement on three separate surfaces.
- **Liquidity floor alone is insufficient.** v1 used a $10K floor with two written exceptions.
  v2 uses the same floor with zero exceptions, plus a volume check — Gate 4 found a candidate with
  $114K posted depth against $3.9K lifetime trading. See finding F2 and decision D2.

## Do not

- Do **not** load this file as a current registry. The loader no longer reads it.
- Do **not** combine v1 and v2 market data as one series (ChatGPT transition rule, adopted July 2026).
