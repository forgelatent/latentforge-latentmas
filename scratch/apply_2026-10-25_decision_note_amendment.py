#!/usr/bin/env python3
"""Amend founder_inputs/2026-10-25_founder_decision_note.md. Run from the repo root.

  python3 scratch/apply_2026-10-25_decision_note_amendment.py          -> check only
  python3 scratch/apply_2026-10-25_decision_note_amendment.py write    -> apply if every check passes

Three edits: the Status line gains an amendment note; item 2 gains the outcome-group wording;
item 9 is appended recording the three decisions of October 25 (evening). Every anchor must
occur exactly once; otherwise nothing is written. Prints counts only.
"""
import sys
from pathlib import Path

NOTE = Path("founder_inputs/2026-10-25_founder_decision_note.md")

STATUS_OLD = "**Status:** DECISION MADE."
STATUS_NEW = (
    "**Status:** DECISION MADE. Amended October 25, 2026 (evening): item 2 reworded and item 9 added, "
    "by Founder decision after cold round 4; see item 9."
)

ITEM2_OLD = (
    "On at least 250 resolved markets across at least 150 independent events from the collected "
    "Polymarket data, the latent arm beats the text arm by more than the pre-registered margin, with error bars."
)
ITEM2_NEW = (
    "On at least 250 resolved markets across at least 150 independent events from the collected "
    "Polymarket data, where the independent unit is the pre-registered outcome group and each group has "
    "equal weight in the primary score, the latent arm beats the text arm by more than the pre-registered "
    "margin, with error bars."
)

ITEM8_TAIL = "pre-register -> run -> Shadow Self v0."
ITEM9 = (
    "\n\n9. **Decisions of October 25, 2026 (evening), after cold round 4.** (a) Item 2 amended as above: "
    "the independent unit is the outcome group, each group weighted equally in the primary score "
    "(readers 3 of 3 on per-group weighting). (b) Inter-reader agreement threshold for the dependence "
    "grouping: J_human >= 0.80, chosen by me as a governance rule, not derived from evidence (readers "
    "3 of 3 that no evidence can set it); below it the grouping step fails and this note's early stop "
    "applies; no third reader. (c) The sorters' review list may be ordered by resolution source, then "
    "event date, then normalised title, under the written contract that order is never evidence "
    "(readers 2 of 3); the cross-list check is required regardless. The design carrying these is "
    "`founder_inputs/2026-10-25_grouping_design_v3.md`, which becomes agreed when I commit it."
)


def main() -> int:
    write = len(sys.argv) > 1 and sys.argv[1] == "write"
    ok = True

    def check(label, cond):
        nonlocal ok
        print(f"{'PASS' if cond else 'FAIL'}  {label}")
        ok = ok and cond

    check(f"exists: {NOTE}", NOTE.exists())
    if not ok:
        print("nothing written")
        return 1
    text = NOTE.read_text(encoding="utf-8")
    check("status anchor occurs once", text.count(STATUS_OLD) == 1)
    check("item 2 sentence occurs once", text.count(ITEM2_OLD) == 1)
    check("item 8 tail occurs once", text.count(ITEM8_TAIL) == 1)
    check("item 9 not already present", text.count("9. **Decisions of October 25") == 0)
    check("outcome-group wording not already present", text.count("pre-registered outcome group") == 0)
    if not ok:
        print("nothing written")
        return 1
    if not write:
        print("check only; nothing written. Rerun with the word  write  to apply.")
        return 0

    new = text.replace(STATUS_OLD, STATUS_NEW, 1)
    new = new.replace(ITEM2_OLD, ITEM2_NEW, 1)
    new = new.replace(ITEM8_TAIL, ITEM8_TAIL + ITEM9, 1)
    if not new.endswith("\n"):
        new += "\n"
    NOTE.write_text(new, encoding="utf-8")
    after = NOTE.read_text(encoding="utf-8")
    print("written. verification counts:")
    print("  item 9:", after.count("9. **Decisions of October 25"), "(expect 1)")
    print("  outcome-group wording:", after.count("pre-registered outcome group"), "(expect 1)")
    print("  amended status:", after.count("Amended October 25, 2026 (evening)"), "(expect 1)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
