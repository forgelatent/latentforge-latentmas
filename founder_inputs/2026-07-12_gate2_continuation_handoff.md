# Gate 2 continuation handoff — July 12, 2026 (evening)

**From:** v2 selection session #1 (Gate 2, incomplete). **Job for next session:** finish Gate 2
(fresh Tier 1 pool), then Gates 3-4 per `founder_inputs/2026-07-12_v2_selection_session_handoff.md`,
which remains binding and should be loaded alongside this file.

## Why Gate 2 stopped mid-way

The May 26 pool tool's traversal method no longer works: the Gamma API now rejects
offset pagination past ~2000 rows. Session #1 characterized the API at Tier 1, built a
corrected copy of the pull tool (v2), and designed toward a partitioned traversal (v3) —
then hit a second structural finding (null-endDate markets invisible to date filters)
and stopped per Pattern D rather than design v4 in the same session.

## Tier 1 findings (all probe-verified this session; reproducers below)

1. **Offset ceiling ~2000.** `offset=2000` -> HTTP 200; `offset=2100` -> HTTP 422. Loud failure
   (a first for Gamma). Universe is >4000 live markets: ascending walk reaches ID ~964456,
   descending reaches ~2895623, full pages at both frontiers — the two ends do not meet.
   *Reproducer:* `curl -s -o /dev/null -w "%{http_code}" "https://gamma-api.polymarket.com/markets?closed=false&limit=100&offset=2100"` -> 422.

2. **No ID-comparison filter.** `id_min`, `min_id`, `start_id`, `id_gt`, `id.gt`, `after`,
   `from_id` are ALL silently ignored (HTTP 200, unfiltered results). `id=N` appears to be
   exact-match. True cursor pagination is impossible.
   *Reproducer:* `curl -s ".../markets?closed=false&limit=3&order=id&ascending=true&id_min=1000000"` returns ids 540817-19 (same as unfiltered).

3. **Working filters (verified):** `end_date_min`, `end_date_max` (date-bounded results with
   different IDs, confirmed), `liquidity_min` (all results >= threshold, confirmed),
   `order=id&ascending=true|false` (monotonic, confirmed). Parameter vocabulary sourced from
   HuakunShen/polymarket-kit OpenAPI schema (third-party; only the four above are probe-verified —
   verify any others before use).

4. **`limit` silently caps at 100.** Requested 500, got 100, no error. Keep PAGE_SIZE=100.

5. **Null-endDate markets exist and date filters exclude them.** Unfiltered vs
   `end_date_min=1970-01-01` walks diverge: offset 1000 -> 692303 vs 701592; offset 1900 ->
   942776 vs 960188. Date-window partitioning alone CANNOT produce a complete pool.
   Magnitude unquantified (dozens-to-hundreds in first 2000 is a loose estimate, not Tier 1).
   *Reproducer:* the paired-offset curl loop in session #1 transcript; rerun both walks at offset 1000 and compare first IDs.

## Tool state

- `scratch/full_pull_and_filter.py` — May 26 original, UNTOUCHED (Round 3 record).
- `scratch/full_pull_and_filter_v2.py` — hash `a96d13a9b97581c92752660a3e831b36c1bdd52562ca0eed9896b2d40ffee2f4`,
  309 lines. Four Founder-approved fixes: (a) dynamic TODAY; (b) run-dated OUTPUT_FILE;
  (c) fail-loud fetch (re-raise, no partial pool) — fired correctly on first run at page 21;
  (d) MAX_DAYS cap removed, null-endDate survivors kept + tagged `open_ended: true`.
  Probability band 0.15-0.80 KEPT (Founder decision). MIN_DAYS=14 kept.
  v2's traversal is still plain offset pagination — it CANNOT complete a full pull (finding 1).
- `scratch/qualifying_pool_2026-05-26.json` — intact, do not overwrite.
- NO fresh pool exists yet. Nothing dated 2026-07-12.

## The open design question (the actual work)

Build v3 with a traversal that is complete-by-construction despite findings 1, 2, 5:

- Date-windowed walks (end_date_min/max, half-open windows) cover dated markets.
  Window sizing probe (Probe B, designed but NOT run in session #1): for each candidate
  window, request offset=1900 — 0 rows = fits, 100 rows = split finer. Near-dated windows
  (Jul-Oct) most likely to overflow.
- Null-endDate markets need their own verified mechanism. UNSOLVED. Candidate probes:
  does `end_date_max=1970-01-01` return them? Does the /events endpoint expose them
  differently? Are they reachable only in the unfiltered first-2000? Probe before designing.
- Completeness cross-check (design carried over): union of all slices, dedup by conditionId,
  then verify every ID from the unfiltered ascending walk's first 2000 appears in the union.
  Any hole = loud fail, no output written.
- Do NOT use `liquidity_min` server-side for the pool: rule 3e permits up to 2 below-floor
  exceptions, so below-floor markets must be IN the pool. Filter at selection time.

## Session #1 self-corrections on record (context for the fresh reader)

- Predicted v2 line delta wrong (+2 predicted, -3 actual; accounted for post-hoc, file verified
  correct by content checks). Treat session #1's arithmetic predictions as untrusted; its
  probe results as Tier 1.
- "Open-ended = missing endDate" was assumed in fix (d) before finding 5 complicated it.
  Rule 3c's long-runway leg is satisfiable by far-dated markets (2028 endDates confirmed to
  exist) even if the null-endDate slice proves small or empty — but the pool must still
  capture null-endDate markets for completeness.

## Do / do not (additive to the binding selection handoff)

- DO load `founder_inputs/2026-07-12_v2_selection_session_handoff.md` alongside this file;
  its gates and rules 3a-3f govern.
- DO probe null-endDate retrieval BEFORE writing v3. No design on unverified API behavior —
  this API ignores unknown params with HTTP 200 (finding 2) and caps silently (finding 4).
- DO reuse v2's filter/dedup/fail-loud internals; only the traversal layer changes.
- Do NOT run v2 expecting a full pool (it aborts at page 21 by design).
- Do NOT overwrite the May 26 pool or the May 26 original script.
- Do NOT trust HTTP 200 as evidence a parameter worked; verify by result content.
- Ledger entries for findings 1, 2, 4 (offset ceiling, no-cursor, limit cap) are NOT yet
  written — draft them in the continuation session alongside the commit.

*End of handoff.*
