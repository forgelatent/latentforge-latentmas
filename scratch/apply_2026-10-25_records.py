#!/usr/bin/env python3
"""Apply the October 25, 2026 record edits. Run from the repo root.

  python3 scratch/apply_2026-10-25_records.py          -> check only, prints counts, writes nothing
  python3 scratch/apply_2026-10-25_records.py write    -> apply, only if every check passes

Edits: append the Sept 22 - Oct 25 entry to docs/incident_ledger.md and update its
"Last meaningful update" line; replace the HEAD anchor sentence in docs/state_manifest.md;
add two dated notes to docs/intent.md. Every anchor must occur exactly once; otherwise
nothing is written. Prints no file contents, only counts.
"""
import sys
from pathlib import Path

LEDGER = Path("docs/incident_ledger.md")
MANIFEST = Path("docs/state_manifest.md")
INTENT = Path("docs/intent.md")
ENTRY = Path("founder_inputs/2026-10-25_ledger_entry_sept22_oct25.md")

ENTRY_TITLE = "- **September 22 – October 25, 2026 — five-week gap"
LEDGER_UPDATE_PREFIX = "Last meaningful update: "
LEDGER_UPDATE_NEW = (
    "Last meaningful update: October 25, 2026 (September 22 – October 25 entry: five-week gap; "
    "pipeline six real nights of 34; registry v2 13 live, 2 retired; Founder decision note supersedes "
    "the $10M threshold; kalshi-pull paused; 412-market pool, 410 resolved; scoring rule v0.2; "
    "grouping design v3 CANDIDATE after cold rounds 2–4; GitHub credential replaced, push protection on; "
    "see the final entry)"
)

HEAD_OLD = "**HEAD:** `2db498f` — Founder decision note, October 25, 2026."
HEAD_NEW = (
    "**HEAD:** `aee6689` — records of the October 25 evening session (round 3 synthesis, grouping "
    "design v2, cold round 4); previous anchor `2db498f` (Founder decision note, October 25, 2026)."
)

INTENT_ANCHOR_1 = (
    "The $10M threshold is deliberate. In a field where narrative often outruns evidence, "
    "we chose to prove first and talk second."
)
INTENT_NOTE_1 = (
    "\n\n*Note, October 25, 2026:* the $10M threshold is superseded by the Founder decision note "
    "(`founder_inputs/2026-10-25_founder_decision_note.md`): \"proven\" now means a pre-registered test "
    "on at least 250 resolved markets across at least 150 independent units, the latent arm beating the "
    "text arm by more than a pre-registered margin, with error bars. The text above is left as history. "
    "See `incident_ledger.md`, September 22 – October 25 entry."
)

INTENT_ANCHOR_2 = (
    "Founder decision on the feed's purpose is open (see `state_manifest.md`). "
    "This note records the drift; it does not resolve it."
)
INTENT_NOTE_2 = (
    "\n  - *Note, October 25, 2026:* resolved. kalshi-pull was paused and unloaded by Founder decision "
    "on October 25; every file it saved since March 29 held only multi-leg sports combination markets "
    "(ledger, September 20 and 21 entries), so it was never a ground-truth feed for the markets this "
    "project studies. The description above is left as history."
)


def main() -> int:
    write = len(sys.argv) > 1 and sys.argv[1] == "write"
    ok = True

    def check(label, cond):
        nonlocal ok
        print(f"{'PASS' if cond else 'FAIL'}  {label}")
        ok = ok and cond

    for p in (LEDGER, MANIFEST, INTENT, ENTRY):
        check(f"exists: {p}", p.exists())
    if not ok:
        print("nothing written")
        return 1

    ledger = LEDGER.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")
    intent = INTENT.read_text(encoding="utf-8")
    entry = ENTRY.read_text(encoding="utf-8")

    update_lines = [l for l in ledger.splitlines() if l.startswith(LEDGER_UPDATE_PREFIX)]
    check("ledger: exactly one 'Last meaningful update' line", len(update_lines) == 1)
    check("ledger: entry not already present", ledger.count(ENTRY_TITLE) == 0)
    check("entry file: starts with the entry title", entry.startswith(ENTRY_TITLE))
    check("manifest: HEAD anchor sentence occurs once", manifest.count(HEAD_OLD) == 1)
    check("manifest: new HEAD not already present", manifest.count("`aee6689`") == 0)
    check("intent: $10M anchor occurs once", intent.count(INTENT_ANCHOR_1) == 1)
    check("intent: kalshi anchor occurs once", intent.count(INTENT_ANCHOR_2) == 1)
    check("intent: notes not already present", intent.count("*Note, October 25, 2026:*") == 0)

    if not ok:
        print("nothing written")
        return 1
    if not write:
        print("check only; nothing written. Rerun with the word  write  to apply.")
        return 0

    new_ledger = ledger.replace(update_lines[0], LEDGER_UPDATE_NEW, 1)
    if not new_ledger.endswith("\n"):
        new_ledger += "\n"
    new_ledger += "\n" + entry
    if not new_ledger.endswith("\n"):
        new_ledger += "\n"
    new_manifest = manifest.replace(HEAD_OLD, HEAD_NEW, 1)
    new_intent = intent.replace(INTENT_ANCHOR_1, INTENT_ANCHOR_1 + INTENT_NOTE_1, 1)
    new_intent = new_intent.replace(INTENT_ANCHOR_2, INTENT_ANCHOR_2 + INTENT_NOTE_2, 1)

    LEDGER.write_text(new_ledger, encoding="utf-8")
    MANIFEST.write_text(new_manifest, encoding="utf-8")
    INTENT.write_text(new_intent, encoding="utf-8")

    print("written. verification counts:")
    print("  ledger entry title:", LEDGER.read_text(encoding="utf-8").count(ENTRY_TITLE), "(expect 1)")
    print("  manifest aee6689:", MANIFEST.read_text(encoding="utf-8").count("`aee6689`"), "(expect 1)")
    print("  intent Oct 25 notes:", INTENT.read_text(encoding="utf-8").count("*Note, October 25, 2026:*"), "(expect 2)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
