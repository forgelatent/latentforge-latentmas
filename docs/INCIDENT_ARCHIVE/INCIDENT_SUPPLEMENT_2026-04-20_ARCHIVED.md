> Archived 2026-05-01. Consolidated into docs/incident_ledger.md. Preserved verbatim for audit trail.

# INCIDENT SUPPLEMENT — April 20, 2026
## Grok Confabulation + Discovery of Unremediated shadow_match.py

**Supplements:** `docs/INCIDENT_2026-04-18.md`, `docs/INCIDENT_SUPPLEMENT_2026-04-19.md`
**Status:** Closed with known-broken state documented. Further remediation deferred to next session.
**Session commit at time of writing:** `466ec98` (HEAD of main)

---

## Why this supplement exists

The April 18 incident was thought to be resolved by April 19. This supplement documents two findings from April 20 that invalidate that belief:

1. `03_text_swarm.py` had a price-extraction bug that silently returned 0.5 for every market since the April 18 rewrite. The "live data" claim was true (the script loaded the live JSON); the "used live prices" claim was false (it read a nonexistent field and fell back to 0.5).
2. `shadow_match.py` was never remediated in the April 18 reset. It still reads `policy_markets_seed.json` — the exact fictional file named as root cause in INCIDENT_2026-04-18.

Both issues existed for the 48 hours between April 18 PM and April 20 PM. No external claims were made in that window, so no external impact. Internal calibration numbers and any references to shadow_match output are invalidated.

---

## Findings (all tier `[VERIFIED_WITH_REPRO]`)

### 1. text_swarm price extraction bug

**Root cause:** `get_live_crowd_price()` read `m.get("current_price")` — a field that does not exist in the Polymarket gamma JSON. Fell back to the `outcomePrices` path, but `outcomePrices` is a JSON-encoded string (e.g. `'["0.749", "0.251"]'`), not a list. The `isinstance(..., list)` check failed. Fell through to hardcoded `0.5`. Every market. Every run.

**Reproducer:** `python3 -c 'import json; d=json.load(open("/Users/latentforge/Projects/data/polymarket/2026-04-20.json")); m=d[0]; print(type(m.get("outcomePrices")).__name__, m.get("current_price"))'` → prints `str None`.

**Fix:** Commit `987a171`. New `_extract_price()` helper with fallback chain: outcomePrices (JSON-parsed if string) → bestBid/bestAsk midpoint → lastTradePrice → 0.5.

**Status:** Extraction verified working against live 2026-04-20.json.

### 2. text_swarm matching logic broken

**Known broken, not fixed tonight.** The matching loop takes the first market whose question contains any word >3 chars from the benchmark query. High-frequency tokens like "2026" and "April" cause every benchmark question to map to one of the first few markets in the JSON (Ethereum intraday contract, Fiorentina UEFA qualification), regardless of topic.

**Reproducer:** Run `03_text_swarm.py` against post-extraction-fix code, observe bimodal 9.5% / 99.5% output. 9.5% = Fiorentina (market #2, contains "2026-27"). 99.5% = Ethereum intraday (market #1, contains "April 20").

**Deferred to next session** to avoid doing design work while exhausted. Four-engine consensus on this decision.

### 3. shadow_match.py never remediated

**Root cause:** `SEED_FILE = BENCHMARK_DIR / "policy_markets_seed.json"` on line 23 of `shadow_match.py`. The April 18 remediation rewrote `03_text_swarm.py` but left `shadow_match.py` untouched. Still reads the fictional seed file. The `current_price` field exists in the seed file because it was hand-authored on March 29.

**Reproducer:** `grep SEED_FILE experiments/benchmark/shadow_match.py`

**Seed file quarantined (commit `466ec98`):** Moved to `docs/INCIDENT_ARCHIVE/policy_markets_seed_DEPRECATED_DO_NOT_LOAD.json`. Any script attempting to load the old path will now fail with `FileNotFoundError`. shadow_match.py is not in launchd, so no scheduled failure.

**Deferred to next session:** Rewrite shadow_match.py to pull from live Polymarket JSON, same source as text_swarm.

### 4. `01_kalshi_selector.py` orphaned and misnamed

**Discovered during tonight's grep-the-repo pass.** Script at `experiments/benchmark/01_kalshi_selector.py` is named "kalshi selector" but actually reads `policy_markets_seed.json` and writes to `experiments/benchmark/markets_YYYY-MM-DD.md`. Has nothing to do with Kalshi. The real `kalshi-pull` launchd job runs a different script at `experiments/week1/scripts/kalshi_pull.py` which hits the Kalshi API correctly.

**Status:** Not in launchd. Orphaned. Will fail-loud next manual invocation due to seed quarantine.

**Deferred to next session:** Delete or rewrite.

### 5. Correction to INCIDENT_SUPPLEMENT_2026-04-19

The April 19 supplement contains the statement: *"Shadow Match script verified pulling real prices (DeSantis 2.6%, Vance 39.1%, Bitcoin 28.5%, etc.)"*

**Retracted.** Those prices came from the seed file, not from the live API. The claim was not backed by file-path inspection. All four engines accepted it without `grep SEED_FILE`.

The supplement also implied shadow_match was part of the active pipeline. It is not — it has never been scheduled in launchd. The earlier `brainload_handoff` summary drafted April 20 PM repeated this misapprehension; that summary is retracted as well.

---

## Failure mode recap

This is the fourth compounding-narrative event in 72 hours:

| # | Event | Agent | Mechanism |
|---|---|---|---|
| 1 | Apr 18 | benchmark pipeline | "45% Brier improvement" synthesized from seed data |
| 2 | Apr 19 PM | commercialization agent | Cherry-picked Brier into compounding thesis file |
| 3 | Apr 19 PM | INCIDENT_SUPPLEMENT authors | Asserted shadow_match pulling real prices without grep |
| 4 | Apr 20 AM | Grok | Generated "low-liquidity 50%" thesis without inspecting JSON |

Common pattern: engine reads ambiguous output → generates confident narrative → forward-propagates without returning to raw data → narrative calcifies into artifact layer (report file, thesis file, incident doc).

The three-engine system prevents cross-engine amplification (Social Proof Loop) but does not prevent intra-engine confabulation. Different defense needed.

---

## Protocol changes ratified tonight

1. **Reproducer requirement.** Every claim in an incident doc must include a command or file-path check that a fresh agent could rerun. Claims without a reproducer are `[INFERRED]` by default, not `[VERIFIED]`.

2. **Three-tier source tagging:** `[VERIFIED_WITH_REPRO]` / `[OUTPUT_OBSERVED]` / `[INFERRED]`. Most of tonight's regressions came from treating `[OUTPUT_OBSERVED]` as `[VERIFIED]`.

3. **Hardcoded narrative lines in output files are prohibited.** Scripts may not write claims about system state into their own output files without those claims being dynamically computed and verifiable. Two such lines were removed tonight (one in `03_text_swarm.py` pre-existing, one Grok attempted to add).

4. **"Clean-looking wrong output" is worse than no output.** When a system is known-broken, quarantine the scheduled job rather than let it produce polished failure. Applied tonight to text-swarm.

---

## Actions taken tonight

1. Committed text_swarm extraction fix (`987a171`)
2. Unloaded `com.latentforge.text-swarm` from launchd
3. Quarantined `policy_markets_seed.json` via `git mv` to INCIDENT_ARCHIVE (`466ec98`)
4. Identified `01_kalshi_selector.py` as orphaned, misnamed, and seed-file-dependent
5. Wrote this supplement

---

## Launchd state at close of session

Active (5 jobs):
- compression-researcher (2:00)
- research-sweep (4:30)
- polymarket-pull (4:40)
- kalshi-pull (4:45)
- calibration-tracker (5:30)

Unloaded (4 jobs):
- benchmark-updater (from April 18)
- commercialization-agent (from April 19)
- revenue-strategist (from April 19)
- text-swarm (tonight)

---

## Tomorrow's starting state

- No automated run will produce new text_swarm output tomorrow morning (intentional)
- calibration-tracker will fire at 5:30 AM and process yesterday's/older contaminated logs — low-stakes but flagged; consider unloading if making pristine start matters
- polymarket-pull at 4:40 AM will produce `2026-04-21.json` normally (unaffected)
- kalshi-pull at 4:45 AM will produce a real Kalshi markets file (unaffected)

## Tomorrow's first tasks (priority order)

1. **Define matching contract.** Before writing any matching code. What counts as a match? Required keyword set per benchmark market? Scoring with threshold? Test cases that would prove or disprove correctness?
2. **Implement matching per contract.** Verify against live 2026-04-21.json.
3. **Rewrite shadow_match.py.** Point at live JSON. Reuse `_extract_price()`.
4. **Grep repo one more time for seed references.** If clean, delete the quarantined seed file.
5. **Decide fate of `01_kalshi_selector.py`.** Delete, rewrite, or rename.
6. **Reload text-swarm into launchd** only after 1-3 verified.

## Questions for the team

1. Are there other agents referencing local seed files we haven't found? Tonight caught one unremediated script (shadow_match) and one orphaned one (01_kalshi_selector). The grep was narrowly scoped to `policy_markets_seed` — broader audit warranted.

2. Should `calibration-tracker` be unloaded until there's real data to calibrate against? Pro: cleaner morning state. Con: defers the question of what it's actually measuring.

3. The three-engine system needs an intra-engine-confabulation defense. The reproducer requirement is step one. What else?

---

*End of supplement. Last edited: April 20, 2026 ~9:XX PM PST.*
