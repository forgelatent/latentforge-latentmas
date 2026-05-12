# May 11, 2026 — Monday evening handoff

## Why this note exists

Saturday evening's handoff queued the kalshi-pull wrapper fix as "its own session." Monday evening was that session. This note captures what shipped and updates the chronology so a fresh session reading the founder_inputs sequence has accurate state.

## What got done Monday May 11 evening

One commit on `main`:

- **`48eb062`** — fix(kalshi_pull): exit non-zero on exception to enable wrapper retry. Two-line script change (`import sys`, `sys.exit(1)`). incident_ledger.md May 9 finding marked Resolved May 11. state_manifest.md kalshi-pull restored to VALID: yes. Empty-data API response observation added as separate Tier 3 follow-on ticket.

## Session shape

Started 7:22 PM PST after skipped Sunday. Time budget: 1 hour. Actual: ~60 min including verification, commit message authoring, and this note.

Sequence:
1. Cron status check (Sunday May 10 + Monday May 11) — all four files present, data layer healthy under laptop-open conditions
2. Attention level check — "Decent," routed to Option A (kalshi-pull wrapper fix) rather than substantive Decision 1 work
3. Read kalshi_pull.py, polymarket_pull.py, run_with_key.sh, and the launchd plist to map full call chain
4. Diagnosis: bug is in script-level `except Exception` handler, not wrapper. Wrapper does correct retry-on-non-zero-exit; script wasn't exiting non-zero.
5. Two-line fix via Python heredoc (atomic-or-nothing edit). Verified syntax with `ast.parse`.
6. Happy-path test (exit 0, 1000 markets saved)
7. Failure-path test (WiFi off, exit 1, NameResolutionError logged with same text format as May 5/6 cron.log)
8. incident_ledger.md and state_manifest.md updates via single atomic Python script (5 edits across 2 files, all-or-nothing)
9. Commit with multi-paragraph message documenting root cause, fix, and verification

## The fix in one paragraph

`kalshi_pull.py` wrapped its API call in `try/except Exception as e:` which swallowed exceptions and let the function return normally (exit code 0). The shared wrapper `scripts/run_with_key.sh` correctly handles retry/exit-code logic — but only fires retries on non-zero exit. The script-level exception swallow prevented the wrapper from ever seeing failures. Fix: add `import sys` and `sys.exit(1)` in the except handler (lines 7 and 55). After the fix, kalshi-pull behaves structurally identical to polymarket-pull on the same exception types: any unhandled exception causes the wrapper to log FAILED, retry up to 3 times with 5-minute delays, and finally log PERMANENT FAILURE if all attempts fail.

## What's still queued (unchanged from Saturday evening note)

The Sunday-morning decisions from Saturday evening's note remain the canonical next-action items:

- **Decision 1:** Question set audit per question (keep / replace / restructure / accept Path B only)
- **Decision 2:** Multi-market aggregation build-or-skip (Q9 forces this)
- **Decision 3:** Data-pull scope expansion (polymarket_pull volume-sort biases toward short-horizon markets)
- Then: keyword authoring (1-2 hours), then contract v1.0 finalization, then implementation

Other structural backlog items unchanged:

- shadow_match.py rewrite to live data
- benchmark-updater v0.2 template
- BRAIN.md runtime-input remediation (Tier 1.5 priority)
- commercialization-agent compounding fixes (two channels)
- WakeForJob asymmetry investigation (lower priority since data layer is healthy under laptop-open conditions)
- kalshi_pull empty-data response handling (tonight's follow-on Tier 3 ticket)

## Today's full git arc

- Saturday May 9 PM: `46b2467` (kalshi-pull finding + VALID downgrade)
- Saturday May 9 evening: `42830a1` (founder_inputs notes for May 3, May 6, May 9 morning/afternoon/evening)
- Monday May 11 PM: `48eb062` (kalshi-pull fix + resolution markup)

Saturday evening's "queued kalshi-pull wrapper fix" item is now closed. The git history is the truth source; this note brings the founder_inputs chronology back in sync.

## Meta-observation worth carrying forward

The data-pull diagnostic Saturday afternoon framed the bug as "wrapper masks fatal errors as SUCCESS." That framing was structurally accurate (the wrapper did log SUCCESS) but causally wrong (the wrapper was doing the right thing; the script was the source). Tonight's reading of the actual code clarified the call chain: launchd → wrapper → Python script, with the wrapper bearing only what the Python script tells it via exit code.

Generalization for future debugging: when a wrapper appears to misbehave, read the script before reading the wrapper. The wrapper's job is to translate exit codes into log lines and retries; if exit codes are wrong, the wrapper looks broken even when it isn't.

This is the kind of thing the Decision Rule for Design Changes guards against. Saturday's incident_ledger entry said "fix requires examining kalshi_pull.py AND any wrapper shell script for the error-handling path." That "AND" was hedge-language that obscured which file actually had the bug. Tonight's diagnosis was faster because we read both files and saw the asymmetry directly (kalshi has a try/except, polymarket doesn't). The lesson: when documenting a bug pre-fix, the entry should commit to a hypothesis about location even if uncertain, so the resolution can confirm or refute the hypothesis explicitly.

## Status of queued items at session close

| Item | Status |
|---|---|
| kalshi-pull wrapper fix | Done — Monday May 11 PM |
| kalshi_pull empty-data response (follow-on) | Queued — Tier 3 ticket in incident_ledger |
| Decision 1, 2, 3 (text-swarm matching contract path) | Queued — fresh session |
| Structural backlog (shadow_match, benchmark-updater, BRAIN.md, commercialization) | Queued — each its own session |
| WakeForJob asymmetry investigation | Lower priority — data layer healthy |
