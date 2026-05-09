# May 9, 2026 — Saturday afternoon handoff

## Why this note exists

Saturday May 9 afternoon session ran the data-pull diagnostic queued in the Saturday morning handoff note. Diagnostic surfaced a real finding (kalshi-pull silent-success bug) that was documented in incident_ledger.md and triggered a VALID downgrade in state_manifest.md. This note carries forward the state from that work.

## What got done Saturday May 9 afternoon

One commit on `main`:

- **`46b2467`** — incident_ledger.md gained a "May 9, 2026 audit findings" subsection documenting the kalshi-pull wrapper silent-success bug. state_manifest.md downgraded kalshi-pull from VALID: yes to VALID: limited with a scope note pointing to the May 9 finding. state_manifest.md HEAD anchor updated from 860fa04 to bd5dd63, "Last meaningful update" moved to May 9, 2026.

## The kalshi-pull finding (headline item)

On May 5 and May 6, kalshi-pull encountered a fatal `urllib3.exceptions.NameResolutionError` (DNS resolution failed for `api.elections.kalshi.com` during laptop-closed wake-with-no-network) but the wrapper logged `SUCCESS on attempt 1` immediately after the error message and exited with code 0. No data was written, no retry was attempted, and launchctl registered the run as clean.

polymarket-pull's wrapper handled the same DNS failure correctly on the same days: `FAILED on attempt 3 (exit code 1)` and `PERMANENT FAILURE after 3 attempts — manual rerun required`.

This is a Pattern A-shaped silent-failure bug (job claiming success when it failed) and a Pattern B-extension (scope narrowness — post-April-18 sweep audited data-content correctness in pull outputs but did not audit error-handling in pull wrappers).

## What changes about kalshi-pull trust going forward

The component is trustworthy on days when the network is reachable at job-fire time. It is not trustworthy as a freshness signal — the launchctl exit status that previously supported VALID: yes is unreliable because the wrapper masks errors. A fresh session reading state_manifest.md should now see VALID: limited and the scope note pointing to incident_ledger.md.

## Saturday afternoon plan that did NOT execute (queued forward)

The Saturday morning handoff note had three items. Items 1 and 2 ran. Item 3 (this note) is now being written.

The structural backlog from Friday's note remains untouched and is still queued for separate sessions:

- **text-swarm matching contract** — incident_ledger.md Apr 20 Pending Item 1. This is the upstream block for the four-arm benchmark and for calibration-tracker re-validation.
- **shadow_match.py rewrite to live data** — incident_ledger.md Apr 20 Pending Item 3.
- **benchmark-updater v0.2 template** — state_manifest.md benchmark-updater entry.
- **BRAIN.md runtime-input remediation** — state_manifest.md April 29 audit finding.
- **kalshi-pull wrapper fix** — new today. Examine `experiments/week1/scripts/kalshi_pull.py` wrapper for the error-handling path that allows fatal exceptions to exit 0. Make failure reporting structurally parallel to polymarket-pull.

## Recursive-staleness observation about state_manifest.md HEAD anchor

state_manifest.md was updated to anchor at `bd5dd63` as part of today's commit, but the commit itself produced HEAD `46b2467`. So the manifest is now stale by one commit again — the natural rhythm where every commit that touches state_manifest.md makes its own HEAD field stale immediately. Per the Precedence Rule clause 2, the manifest is always a snapshot.

This is not an action item. It is a structural property of the file's role. Worth knowing for future sessions: when the manifest is read, the HEAD anchor names "the previous commit," not "the current commit," unless explicitly chased.

## Today's full git arc

- Friday May 8 evening: `eae4846` (revenue-strategist date + bootstrap pattern broadening), `bd5dd63` (text-swarm date + Day 30 date + research-sweep threshold ordering)
- Saturday May 9 afternoon: `46b2467` (kalshi-pull finding + VALID downgrade + state_manifest HEAD update)

Three commits across two days. Build_log.md review work fully closed; new operational finding documented.

## Meta-notes from Saturday session

- Diagnostic-first approach (cron.log inspection) revealed a finding that the original Wednesday hypothesis (WakeForJob asymmetry) had not predicted. The hypothesis was directionally on the right track (laptop-closed conditions matter) but missed the wrapper bug that turned a recoverable network failure into a Pattern A silent success. Generalization: when cron.log evidence is available, run it before settling on an environmental hypothesis.
- Python heredoc approach for documentation edits worked cleanly twice today (incident_ledger.md insertion, state_manifest.md three-edit atomic). Recommended pattern for future structured documentation work over TextEdit Find & Replace.
- One Pattern A class observation worth carrying forward: the post-April-18 architecture audited *data content* (is the data what we think it is?) but did not audit *wrapper reporting* (is the launchctl exit status what we think it is?). The kalshi-pull bug is the first concrete instance of the wrapper-reporting gap. If a second instance surfaces in another component, this likely warrants a separate pattern letter and an explicit audit pass over all launchd wrappers.

## Status of queued items at session close

| Item | Status |
|---|---|
| Build_log.md review (Sunday's seven findings) | Done — Friday |
| Data-pull diagnostic | Done — Saturday afternoon |
| kalshi-pull silent-success finding documentation | Done — Saturday afternoon |
| state_manifest.md HEAD anchor update | Done — Saturday afternoon |
| kalshi-pull wrapper fix | Queued — its own session |
| Structural backlog (4 items from Friday note) | Queued — each its own session |
