# May 6, 2026 — data-pull gap and Friday handoff

## Why this note exists

Logged on tonight (Wed May 6, ~6:15 PM) for the first time since Sunday's wrap. Work this week meant Mon and Tue were unavailable. Spent ~30 minutes orienting. Pausing until Friday.

## What I found tonight

Ran a quick diagnostic before opening any Claude session:

- Data pulls (polymarket, kalshi) for May 5 and May 6: MISSING.
- Data pulls for May 4: present and clean.
- Research jobs (research-sweep, compression-researcher) for May 5 and May 6: present and substantive (May 6 daily-digest is 39 lines).
- `launchctl list` shows last-exit-status `1` for polymarket-pull and calibration-tracker; status `0` for research-sweep, kalshi-pull, compression-researcher.

Almost certainly caused by laptop-closed sleep state. Mac was closed Sunday evening through Wednesday. `WakeForJob=true` is supposed to handle this (per BRAIN.md April 4 entry on cron-to-launchd migration) but apparently doesn't reliably wake the machine for all jobs when the lid is closed.

The asymmetry — research jobs ran cleanly, data-pull jobs failed silently — is the interesting question. Same launchd configuration, same machine, same wake-mechanism assumption, different outcomes. Worth investigating; not investigated tonight.

## Operational consequence

Calibration-tracker has been scoring against missing data for two days. But: text-swarm is unloaded, commercialization-agent is unloaded, calibration-tracker itself is `VALID: no` per state_manifest.md. The entire propagation surface for Polymarket data is currently turned off, so the data gap doesn't actually contaminate anything trusted.

Tomorrow morning's natural 4:40/4:45 AM cycle should refresh the pipeline assuming the laptop stays open and plugged in.

## Sunday session is mid-fix on Findings 3 + 4

I reopened Sunday's Claude session tonight (the one that did the build_log.md review). They are mid-fix on the revenue-strategist date contradiction:

- They verified my git log on the launchd plist returns empty (plist not in repo).
- They defaulted to `incident_ledger.md` Section 6 Finding B as canonical: April 19, 2026 unload date.
- They drafted exact replacement text for Section 2.4.1 (status table row + closing paragraph) and Section 4.4 (decision table row, to be moved to sit with other April 19 entries).
- They asked me to confirm the reorder and the hand-edit mechanism. I confirmed both.
- They were about to send the final paste blocks. I told them I'm pausing until Friday.

## Friday resumption

If the Sunday session is still reachable (browser tab open or recoverable):

- Reopen it. Their last message will be the final paste blocks for Section 2.4.1 + Section 4.4. Or, if they took my "pausing" message as a closing message, send a one-liner asking for the paste blocks.
- Use the helper Claude session (the one this note was drafted with) to walk through the TextEdit edits step-by-step, same shape as Sunday's edits.
- After Findings 3 + 4 land and verify, move to Finding 6 (Trinity bootstrap framing in Section 5.5).

If the Sunday session is unreachable (tab closed, etc.):

- Open a fresh Claude session.
- Paste bundle via `brainload_handoff` (which is current — main is at `31fb5e6`, all five files load, verified Sunday).
- Brief them on Group A status from the May 3 note + this note: revenue-strategist date fix is in flight (April 19 confirmed canonical), Section 4.4 row to be moved to April 19 cluster, Finding 6 not yet started.
- A fresh session would need to redo the date verification (~5 min: git log on plist returns empty, default to incident_ledger.md).

## Other queued items (carryover from May 3 note)

Group B (verify before fix):
- Finding 2: text-swarm May 2 unload date
- Finding 9: Day 30 date (build_log says May 7, may be wrong; check BRAIN.md Day 1 anchor)
- Finding 10: meta-version of 2 and 3

Group C (low priority):
- Finding 1: research-sweep threshold prose order

## New queued items from tonight

1. **Data-pull WakeForJob asymmetry investigation.** Why did research-sweep and compression-researcher run cleanly through May 5 and May 6 while polymarket-pull and kalshi-pull failed? Possible verification commands when investigating:
   - `tail -50 ~/Projects/data/polymarket/cron.log` — looking for errors vs empty entries (distinguishes "fired and failed" from "didn't fire")
   - Compare plists for the working vs failing jobs
   - Check IOPMAssertionCreateWithName / `pmset -g` for relevant power management state during failure window
2. **Manual data-pull catch-up question.** Should we fire a manual polymarket+kalshi pull to fill the May 5 and May 6 gap? Probably not, because (a) downstream consumers are unloaded and (b) leaving the gap preserves the diagnostic surface. But worth a deliberate decision rather than letting the gap drift.

## Three operational questions still deferred (from May 3 note)

1. Runtime data files (`brier_running.json`, cron logs) — commit, gitignore, or leave?
2. Backup files (`docs/*.backup-*`) — commit, gitignore, delete, or leave?
3. Audit-trail script (`scripts/update_brainload_handoff_alias.py`) — commit as audit trail, or leave?

## Where state is

- Main: `31fb5e6` (unchanged since Sunday)
- Local: clean (no uncommitted edits to load-bearing files)
- Backups: `~/.zprofile.backup-2026-05-02` (pre-alias-edit)
- Sunday session: was active when I sent the pausing message. Browser tab open as of this note.
- This note's filename: `2026-05-06_data_pull_gap_and_friday_handoff.md`