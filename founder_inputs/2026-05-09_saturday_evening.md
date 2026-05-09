# May 9, 2026 — Saturday evening handoff (Sunday morning resumption)

## Why this note exists

This is a substantial state-carry note. Tonight's session moved from "implement the matching contract" to "discover that three upstream issues block contract finalization." The strategic shape changed in the last 90 minutes. Sunday morning should start with this note + the bootstrap bundle, then make three decisions before any code or contract work resumes.

## Today's commit (Saturday May 9 afternoon)

One commit on `main`:

- **`46b2467`** — incident_ledger.md gained "May 9, 2026 audit findings" subsection (kalshi-pull wrapper silent-success bug). state_manifest.md downgraded kalshi-pull to VALID: limited and updated HEAD to bd5dd63.

## The strategic recovery plan (from this afternoon's synthesis)

A "what needs to be done to get the project back on track" synthesis was produced this afternoon. Eight items in four tiers. The Founder pushed back on three of the eight, and those pushbacks are now incorporated:

**Tier 1 — Unblock the prediction-market measurement layer:**
1. Define the matching contract for text-swarm (paused tonight at v0.9 — see below)
2. Implement matching per the contract (blocked on #1)
3. Rewrite shadow_match.py to use live data
4. Rebuild the benchmark report v0.2 (blocked on #1, #2, #3)

**Tier 1.5 / 2 — Upgraded per Founder pushback:**
6. Fix revenue-strategist BRAIN.md runtime-input dependency (this is bigger than originally scoped — BRAIN.md is a runtime input to TWO agents per April 29 audit, and INVALIDATED banners are being fed into agent prompts daily)

**Tier 2 — Unlock the strategic-thinking layer:**
5. Fix commercialization-agent compounding bugs (two channels per April 29 audit)

**Tier 3 — Operational reliability:**
7. kalshi-pull wrapper fix (today's finding — script-level)
8. WakeForJob asymmetry investigation (queued, deferred)

**Tier 4 — Next phase, not in this week:**
9. V0.1 demo + OpenSpiel benchmark (weeks-floor; explicitly out of scope until measurement layer rebuilt)

## The matching contract conversation (tonight)

The contract was being drafted to address Tier 1 Item #1. We got to v0.9 with the following structure agreed:

**Two paths:**
- Path A (live): for questions whose resolution date has not passed — match against current Polymarket markets
- Path B (resolved): for questions whose resolution date has passed — score against historical real-world resolution

**Four-gate match logic for Path A** (independent boolean gates, no soft scoring):
- Topic match
- Threshold match (numerical thresholds must be equal)
- Time-window match
- Polarity match (rejects inverse-polarity markets)

**Per-question keyword sets** required: required-keywords (must all appear) + forbidden-keywords (any appearance disqualifies).

**No-live-match-today is a first-class output** — never fall through to 0.5 or any default price. Honest absence over fabricated presence.

**Path B forward-looking only** — pre-contract swarm predictions are retracted (contamination + broken matching). Post-contract resolutions accumulate clean Brier scores forward.

**Test suite as executable contract:**
- Test 1: known matches (hand-curated expected matches for 11 questions)
- Test 2: adversarial non-matches (false-positive resistance)
- Test 3: bimodal failure check (output should not collapse onto 1-2 markets)
- Test 4: empty-input check (no Polymarket data → "no live match" not 0.5)

**Founder additions to the contract before finalization:**
- A: Q-rewrite resets longitudinal clock. Pre-rewrite predictions are not comparable to post-rewrite predictions for that question.
- B: Keyword authoring is real design work. Estimated 1-2 hours for all 11 questions. Scoped as separate Sunday morning task.

**Founder push-backs accepted:**
- Four-gate independence: keep as-is (no soft scoring)
- No-live-match-today as expected output: keep as-is
- Inverse-polarity (edge case 5): rejected — question-level rewrite is cleaner
- Multi-market aggregation (edge case 1): originally deferred, but tonights empirical check made this un-deferrable (see below)

## Tonights empirical findings (the strategic shift)

Quick checks against `~/Projects/data/polymarket/2026-05-09.json` revealed three structural issues that block contract finalization:

**Issue 1 — Data-pull scope mismatch.**
- The polymarket-pull script queries `closed=false&limit=200&order=volume&ascending=false` — sorted by volume.
- Volume concentrates on short-horizon retail markets. Today's pull: 70% resolve in May 2026, 85% by end of June.
- Long-horizon macro/policy markets (which the benchmark questions need) are not in the top-200-by-volume slice.
- Q1 (Fed cuts in 2026): zero candidates in todays pull
- Q2 (Bitcoin $150K end of 2026): 3 candidates, all short-horizon BTC ranges, none matching
- Likely affects Q1, Q2, Q4 (Musk/Tesla), Q8 (unemployment) — long-horizon macro questions

**Issue 2 — Multi-market aggregation is now load-bearing, not deferrable.**
- Q9 (Republicans win House majority): Polymarket lists 9 individual House seat races in November 2026, no canonical "who controls the House" market.
- This is the State 2 (family of markets, no exact match) case showing up in real data.
- Edge case 1 of the contract draft was deferring multi-market aggregation. That deferral is no longer viable.
- Either build aggregation logic (with defined rules) or accept Q9/Q10 as State 3 entirely and route to Path B-only.

**Issue 3 — Some benchmark questions may have no Polymarket coverage at all.**
- Q10 (Democrats win Senate majority): zero Senate-race markets in todays November-2026 listings (only House races and CA governor).
- Q11 (voter turnout): zero turnout markets in todays pull. Possibly always State 3.

## The three Sunday-morning decisions

These have to be made before contract v1.0 finalization or any implementation work:

**Decision 1 — Question set audit.** For each of the 11 benchmark questions, determine whether Polymarket lists matching markets at all (expanding the data-pull query if needed). Outcomes possible per question:
- Keep (Polymarket has good coverage, contract works as drafted)
- Replace (Polymarket doesnt cover this; swap for a question they do cover)
- Restructure (Polymarket covers it differently; rewrite Q to match Polymarkets convention)
- Accept as Path B only (no live coverage; resolution-only scoring)

The decision affects the longitudinal clock — Q-rewrite resets it per contract addition A.

**Decision 2 — Multi-market aggregation: build or skip.** Q9 forces this. Two clean choices:
- Build aggregation logic (define rules: how do you aggregate 9 seat races into a House-majority probability? Sum-of-probabilities? Volume-weighted? Define this *before* code.)
- Skip it: route Q9/Q10 to Path B only, accept that majority-control questions only score on resolution.

**Decision 3 — Data-pull scope expansion.** If Decision 1 keeps any long-horizon macro questions, polymarket_pull.py needs a broader query. Options:
- Run a separate query for political/macro markets alongside the volume-sorted query
- Increase limit beyond 200
- Use category filters

**Order:** Decision 1 first (it constrains Decisions 2 and 3). Decision 2 and 3 can be done in parallel after Decision 1.

**Estimated time:** 2-3 hours for the three decisions. Then keyword authoring (1-2 hours). Then implementation (afternoon if time permits, otherwise Monday evening).

## What did NOT happen tonight (carried forward)

- Multi-market frequency check for Q3, Q4, Q8 (stopped at Q1, Q2, plus the November-2026 distribution check — enough evidence to surface the structural issues)
- Resolution-date pass for the 11 questions (5-min task, do tomorrow)
- Keyword authoring (Sunday morning, fresh)
- Contract v1.0 finalization (blocked on the three decisions)

## Still queued from previous notes

**From Friday + Saturday afternoon notes:**
- kalshi-pull wrapper fix (Tier 3, ~30 min)
- text-swarm matching contract (this is the work)
- shadow_match.py rewrite to live data
- benchmark-updater v0.2 template
- BRAIN.md runtime-input remediation (upgraded to Tier 1.5 priority)
- commercialization-agent compounding fixes (two channels)
- WakeForJob asymmetry investigation

## Meta-observations from tonights session

- The data-pull-scope finding was the kind of thing a contract design conversation can hide. Drafting matching logic against a non-representative data sample would have produced a contract that "works" but had nothing to match. The empirical check (Q1=0, Q2=3-but-irrelevant) caught this before the contract was finalized.
- This generalizes: future contract conversations should include "verify against real data" as a step *before* finalization, not as a Test 3 implementation gate after.
- The strategic recovery plan from this afternoon is structurally sound but the time estimates assumed all eight items were independent. They are not — Tier 1 items have order constraints (matching contract → matching code → calibration → benchmark report) that the plan correctly captured, but it didnt anticipate that Decision 1 (question set audit) would surface as a prerequisite to even starting the contract.
- Discipline: the Founder set a 45-60 min cap on tonight, and we hit it almost exactly. The strategic-shift moment came at minute ~50. Stopping at the cap rather than pushing through to "complete the contract tonight" was the right call.

## Today's full git arc

- Friday May 8 PM: `eae4846` (revenue-strategist date + bootstrap pattern broadening), `bd5dd63` (text-swarm date + Day 30 date + research-sweep threshold ordering)
- Saturday May 9 PM: `46b2467` (kalshi-pull finding + VALID downgrade + state_manifest HEAD update)

Three commits. Build_log.md review fully closed. Operational finding documented. Strategic recovery plan synthesized but not yet implemented. Matching contract drafted to v0.9 with three upstream blockers identified.

## Status of queued items at session close

| Item | Status |
|---|---|
| Build_log.md review (Sundays seven findings) | Done — Friday |
| Data-pull diagnostic | Done — Saturday afternoon |
| kalshi-pull silent-success finding documentation | Done — Saturday afternoon |
| state_manifest.md HEAD anchor update | Done — Saturday afternoon |
| Strategic recovery synthesis (eight items) | Drafted — Saturday afternoon |
| Matching contract v0.9 | Drafted — Saturday evening |
| Question set audit (Decision 1) | Queued — Sunday morning |
| Multi-market aggregation decision (Decision 2) | Queued — Sunday morning |
| Data-pull scope expansion (Decision 3) | Queued — Sunday morning |
| Keyword authoring | Queued — Sunday after Decisions 1-3 |
| Contract v1.0 finalization | Blocked — pending Decisions 1-3 |
| Implementation | Blocked — pending contract v1.0 |
| kalshi-pull wrapper fix | Queued — its own session |
| Structural backlog (Tier 2 items) | Queued — each its own session |
