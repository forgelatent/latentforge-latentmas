> Archived 2026-05-01. Consolidated into docs/incident_ledger.md. Preserved verbatim for audit trail.

# INCIDENT SUPPLEMENT — April 19, 2026
## Manual Pipeline Simulation & Follow-up Findings

**Supplements:** `docs/INCIDENT_2026-04-18.md`
**Status:** Live (open follow-ups pending tomorrow)
**Session commit at time of writing:** `7e1d6e5`

---

## Context

Following the April 18 hard reset and the April 19 Option A+ merge (commit `479bc84`) integrating Mac Mini April 17 steering work, all four engines (Systems, Divergent, Analysis x 2) converged on Path 3 (stop, verify at 4:40 AM April 20 automated run). Founder Engine overrode to execute a manual simulation of the full launchd agent sequence tonight, using the production wrapper (`run_with_key.sh`).

This document records findings from that simulation.

---

## Scope of simulation

Ran each of the 8 relevant launchd-scheduled agents manually via `run_with_key.sh`:

| Scheduled time | Agent | Infrastructure | Content |
|---|---|---|---|
| 2:00 AM | compression-researcher | PASS | Clean |
| 4:30 AM | research-sweep | PASS | Clean |
| 4:40 AM | polymarket-pull | PASS | Clean |
| 4:45 AM | kalshi-pull | PASS | Clean |
| 5:00 AM | revenue-strategist | PASS | FAIL -- retracted narrative in prompt |
| 5:15 AM | text-swarm | PASS | FAIL -- market_mapping produces 50% fallback for all 11 markets |
| 5:30 AM | calibration-tracker | PASS (after repair) | FAIL -- Brier Skill Score -2.93 vs contaminated baselines |
| 5:45 AM | commercialization-agent | PASS | CRITICAL FAIL -- actively manufacturing Social Proof Loop from cherry-picked data |

benchmark-updater (6:00 AM) remained intentionally unloaded from the April 18 reset.

---

## Infrastructure issues found and repaired tonight

### calibration_tracker.py had broken Python syntax
April 18 contamination sweep prepended a markdown disclaimer to the top of the file as raw text, causing `SyntaxError: invalid character` on import. Would have silently failed at 5:30 AM tomorrow. Repaired via Python-comment-block replacement, verified `ast.parse` clean. Repo-wide AST scan confirms zero other broken `.py` files.

### ~/.zshrc had a poisoned `ANTHROPIC_API_KEY` export
Line 8 read `export ANTHROPIC_API_KEY=source ~/.zprofile` -- a malformed assignment that set the env var to the literal string "source" (6 chars). Launchd pipeline unaffected (uses Keychain via `run_with_key.sh`), but manual testing impossible. Repaired to load directly from Keychain.

### Plaintext Kalshi API key in .zshrc (line 4) -- flagged
Not repaired tonight. Filed for future Keychain migration.

---

## Content issues found tonight (unresolved -- deferred to tomorrow)

### A. Text swarm market_mapping failure
`03_text_swarm.py`'s `load_live_markets()` queries Polymarket for 11 hardcoded questions (e.g. "Will the Fed cut rates by at least 50bps in 2026?"). None of these match any real Polymarket market via the current search-term logic. All 11 fall back to 50.0%. Meanwhile `shadow_match.py` (separate agent, separate search-term map) successfully retrieves real prices for different questions (DeSantis, Vance, Bitcoin, etc.).

**Impact:** All post-reset swarm predictions are logged against 50% fallback crowd baselines. Calibration tracker's skill scores against these are meaningless.

**Fix path:** Merge shadow_match's battle-tested search-term map into text_swarm. Design decision: pick 11 markets based on what's actually liquid on Polymarket.

### B. Revenue strategist template contamination
Daily output continues to reference Rain Grant, prediction-market-research framing, "latent agents hold probability distributions" as the commercial story. Prompt template unchanged post-reset.

**Mitigation tonight:** Unloaded from launchd (two-engine consensus -- Gemini + Claude).

### C. Commercialization agent actively regenerating Social Proof Loop
Most significant finding. Agent:
1. Reads `calibration_tracker` output showing Brier 0.0173 for Full Track, BSS -2.93 vs crowd
2. Cherry-picks the absolute Brier; ignores negative skill score
3. Generates prose like "performance in adversarial liquid markets where professional forecasters..."
4. Writes to `commercialization_thesis.md` which **compounds daily** -- tomorrow's run reads today's thesis as input

This is the exact failure mode the April 18 reset was designed to prevent. And it was already regenerating itself from the prompt template.

**Mitigation tonight:** Unloaded from launchd (unanimous four-engine consensus).

### D. Calibration metrics currently uninterpretable
Pre-April 19 swarm predictions scored against fictional seed baselines. Post-April 19 predictions (starting today) scored against 50% fallbacks. Neither reading is meaningful until issue A is fixed.

---

## New protocols ratified tonight

### Manual simulation as standard practice
Whenever a global annotation sweep or contamination cleanup is performed, the full launchd agent sequence must be manually simulated via production wrappers before the reset is considered "closed." Tonight's simulation caught: one broken Python file, one poisoned shell env, one market-mapping content failure, one actively-regenerating Social Proof Loop. Without the simulation, all four would have surfaced at staggered times tomorrow morning in production.

### Attested summaries rule (Gemini, pending tomorrow)
Data files passed between agents must carry validity headers (e.g. `[DATA_VALIDITY: INVALIDATED_PRE_RESET]`). Downstream agents must parse these headers. Agents are forbidden from making high-confidence narrative claims when upstream data is tagged invalid.

### Structural vs prompt distinction (ChatGPT, ratified by Gemini)
Narrative agents synthesizing misleading claims from real data is not a prompt bug -- it's a structural protocol violation. Fix is evidence-tier enforcement and claim validation, not prompt tweaks.

---

## Launchd state after tonight's work

Active (6 jobs): compression-researcher, research-sweep, polymarket-pull, kalshi-pull, text-swarm, calibration-tracker.
Unloaded (3 jobs): benchmark-updater (pre-existing), commercialization-agent (tonight), revenue-strategist (tonight).

---

## Pending work (handoff to April 20 session)

In priority order:

1. Four-point check on 4:40 AM automated run
2. Merge `shadow_match` search-term map into `text_swarm.load_live_markets()` (fixes A, enables D)
3. Re-evaluate calibration validity once text_swarm is producing real crowd baselines
4. Design attested-summaries protocol (header format, validator logic, agent-prompt enforcement)
5. Rewrite revenue_strategist + commercialization_agent prompt templates under new protocol
6. BRAIN.md narrative rewrite grounded in April 20 live data
7. v0.2 clean rewrite salvaging technical content from PRE_RESET_DRAFT
8. Bearish asymmetry re-validation (Gemini's flag: may be proxy contamination)
9. Move Kalshi key to Keychain
10. Mac Mini bidirectional steering work -- only after 1-8 stable

---

## Final engine alignment on tonight's scope

| Engine | Vote on tonight scope |
|---|---|
| Systems (Claude) | Unload 2 narrative agents + commit fix + stop |
| Divergent (Grok) | Unload commercialization + commit + document + stop |
| Analysis (ChatGPT) | Unload commercialization + commit + stop (keep revenue-strategist for diagnostic) |
| Analysis (Gemini) | Aggressive unload + commit + stop |
| Founder (John) | Accepted aggressive unload + commit + document + stop |

Four-engine agreement on: unload commercialization, commit, stop.
Split on: unload revenue-strategist (2 yes, 1 no, 1 silent).
Systems Engine call: unload on tiebreaker.

---

*End of supplement. Full audit trail in this file + INCIDENT_2026-04-18.md.*
