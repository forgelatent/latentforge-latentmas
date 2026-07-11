# Registry v2 briefing — cold review request (Round 5)

**Date:** July 11, 2026
**From:** Founder Engine (John McGuire), LatentForge
**To:** Reviewing engine (cold — you have not seen other engines' responses or any Founder/Systems framing of the answer)
**Question class:** Mode 1 benchmark registry — continue v1 on reduced markets, or trigger v2

---

## Rules for this review (read first)

1. **You have no terminal access.** Every factual claim in this briefing is accompanied by embedded verbatim terminal output or a commit reference. You are reviewing the operator's evidence, not the live system.
2. **Citation requirement.** For every load-bearing claim in your response, point at the specific embedded evidence line (or briefing section) it rests on. Claims you cannot ground in this document should be labeled SPECULATION explicitly.
3. **Do not invent code, files, metrics, or history.** A prior review round (May 24) included an engine fabricating findings shaped like a different component's real failures. If the evidence for something is not in this document, say "not in evidence" rather than filling the gap.
4. **Tier discipline.** Section 4 is Tier 1 (raw system output). Section 5 is operational fact. Section 6 is explicitly Tier 3 (one engine's interpretation) — weigh it as opinion, verify its reasoning independently, and feel free to reject it.
5. **Answer the question in Section 7.** Do not redesign Mode 1, do not re-open locked decisions (Section 3), do not propose specific replacement markets (that is a later step if v2 is chosen).

---

## 1. What Mode 1 v1 is for

Mode 1 is the market-state measurement layer for the four-arm benchmark: a **longitudinal measuring stick**. A fixed registry of markets is snapshotted daily so that agent forecasting behavior can be compared across time on a stable question set. Stability of the question set is the load-bearing property — swapping questions destroys the longitudinal comparison. (Same design logic as the text-swarm 11 fixed questions: fixed on purpose.)

The registry is **Variant A: immutable within a version.** Markets are never added, removed, or swapped inside registry v1. Moving to a new set is a *version decision* (v2), which is a legal move under the locked architecture — this briefing is about whether to make it, not whether it is allowed.

## 2. How registry v1 was selected (Round 3, May 26, 2026)

- Qualifying pool of 298 markets generated from full Polymarket pull diagnostics.
- 8 markets locked with a **$10K liquidity floor**, with two named soft exceptions (China GDP ~$4K, SCOTUS ~$5K).
- Committed as `benchmark_registry_v1.json` at commit `be7aa94`.
- All 8 verified live at the June 27 contract synthesis and at the June 28 loader verification.

## 3. What is locked and NOT being re-opened

- The Mode 1 architecture and its purpose (Section 1).
- The loader contract Q1-Q5 (commit `c0b53ce`), as amended July 11 (two-pass fetch, dual provenance hashes — commit `9248b63`). The loader is installed, verified, and running (commit `6476c03`).
- Variant A immutability *within* a version.
- The Round 3 selection of v1 itself. v1 was validly selected; this question is about what happens next, not whether Round 3 erred.

## 4. Current registry state — Tier 1 evidence

Verbatim terminal output, July 11, 2026, reading the loader's current snapshot (symlink `market_state_current.json` -> dated file):

```
Snapshot file: market_state_current.json -> market_state_2026-07-11.json
Snapshot sha256: 84a43b9472205ca6...
Run: 14b6ca56-6eab-4f31-a388-1465324b25d3  at 2026-07-11T20:19:26.229789+00:00
Run state: RETIRED_PRESENT

STATE    CAUSE    MARKET
LIVE     -        will-china-gdp-growth-in-q2-2026-be-between-4pt6-and-4pt9
RETIRED  closed   scotus-bars-counting-mail-ballots-after-election-day
RETIRED  closed   israel-x-iran-permanent-peace-deal-by-june-30-2026-262
RETIRED  closed   will-anthropic-have-the-best-ai-model-at-the-end-of-june-2026
RETIRED  closed   iran-agrees-to-surrender-enriched-uranium-stockpile-by-june-30-2026
RETIRED  closed   will-crude-oil-cl-hit-high-120-by-end-of-june
LIVE     -        will-gpt-6-be-released
LIVE     -        fed-rate-cut-by-december-2026-meeting

Totals: 3 LIVE / 5 RETIRED of 8
```

- All 5 retirements have `cause_of_death: closed` (genuine market resolution, not identity failure or data loss). Resolutions occurred around June 30, 2026.
- The loader classified these correctly and exited 1 (RETIRED_PRESENT — a defined success tier meaning "founder decision required"), which is the event that generates this briefing.

## 5. Operational facts bearing on the decision

- **Timeline:** registry locked May 26; loader installed July 11; 5 of 8 markets resolved ~June 30 — i.e., the registry lost 5 markets roughly five weeks after selection, and *before* any downstream Mode 1 consumer was built. **No downstream consumer reads Mode 1 output yet.** Nothing breaks today under any option; the cost of each option is to the future benchmark, not to running code.
- **Longitudinal data collected so far under the loader:** effectively zero days of unattended operation (first unattended run is tonight). There is no accumulated v1 time-series that a v2 switch would discard.
- **Loader handles a shrinking live count** by design; exit 1 recurs daily while any RETIRED market is present.
- **Known constraint for any larger v2:** the loader bulk URL sets no explicit `limit` parameter; at 8 markets any truncation fails loud via the identity check, but a v2 with more markets requires adding an explicit limit (cold re-read finding, July 11, ledger).
- **Known selection-pool fact from Round 3:** the qualifying pool (298 markets) and selection tooling (`scratch/` diagnostic scripts) still exist, but pool data is from May 26 and would need regeneration for any v2 selection.

## 6. Systems Engine observations — Tier 3, interpretive, verify independently

*These are one engine's reads of the Section 4/5 facts. They are opinions. Ground your response in Sections 1-5; treat this section as a hypothesis to test, not evidence.*

- **Date-clustering read:** four of the five retired markets had explicit June 30 deadlines in the question text. Under this read, the die-off was structurally predictable at selection time: mixing hard-dated and open-dated questions produces clumped expirations. If true, it bears on v2 selection *rules* (deadline diversity), whichever option is chosen.
- **Runway read:** the three survivors are all long-dated (China GDP Q2 resolves ~late July at earliest; GPT-6 open-ended; Fed Dec runs to the December meeting). Under this read, option (a) below has a real runway measured in months, not days — though the China GDP market may itself resolve within weeks.

## 7. The question

**Does a 3-market registry still constitute a valid longitudinal instrument for Mode 1 v1's stated purpose (Section 1), or does the 5-of-8 retirement trigger the v2 decision now?**

Options, presented flat and unranked. Argue for one, or propose (d):

- **(a) Run out v1's clock on 3 markets.** v1 continues as-is; its longitudinal record is 3 markets deep going forward; v2 is deferred until v1 reaches a natural endpoint (definition of endpoint would be needed).
- **(b) Trigger v2 now.** Regenerate the qualifying pool, select a v2 registry under Round 3-style rules (possibly amended), retire v1. Since no time-series has accumulated yet, nothing measured is lost.
- **(c) Hybrid.** v1 keeps running on 3 markets (data is cheap, loader is installed) while v2 selection proceeds in parallel; v2 becomes the benchmark registry when locked.
- **(d) Other** — a structurally different answer, with your reasoning.

Whatever you choose, also answer: **which Round 3 selection rules should carry over to any v2, and which should change** (e.g., liquidity floor, category mix, deadline diversity, market count)? Cite which briefing facts drive each recommendation.

## 8. What is NOT being asked

- Not asking for specific replacement markets.
- Not asking to redesign Mode 1, the loader, or the contract.
- Not asking whether Round 3 was a mistake.
- Not asking about any other component (text-swarm, calibration-tracker, etc.).

*End of briefing. Respond cold; cite embedded evidence; label speculation.*
