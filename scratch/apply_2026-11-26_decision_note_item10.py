#!/usr/bin/env python3
"""Apply the November 26, 2026 amendment to the Founder decision note.

Adds item 10 (margin m = 0.01, Founder-approved wording) and one sentence
to the Status line. All-or-nothing: every check must pass or nothing is
written. Run from the repo root.

  python3 scratch/apply_2026-11-26_decision_note_item10.py           check only
  python3 scratch/apply_2026-11-26_decision_note_item10.py --write   apply

Prints PASS/FAIL lines, counts and hashes only. Never prints file contents.
"""
import hashlib
import sys
from pathlib import Path

NOTE = Path("founder_inputs/2026-10-25_founder_decision_note.md")

STATUS_ANCHOR = "by Founder decision after cold round 4; see item 9. Drafted by Systems Engine"
STATUS_NEW = (
    "by Founder decision after cold round 4; see item 9. "
    "Amended November 26, 2026: item 10 added (margin m), by Founder decision "
    "after cold round 8. Drafted by Systems Engine"
)

TAIL_ANCHOR = "which becomes agreed when I commit it."

ITEM_10 = (
    "10. **Decision of November 26, 2026: the margin m.** "
    "I choose m = 0.01 Brier units as the smallest improvement worth claiming. "
    "This is my governance judgment, not a value derived from any arm's result, "
    "from the pool's outcomes, or from Draft-KV's accuracy gains. "
    "m is an absolute reduction in group-averaged Brier under the scoring rule's §7. "
    "It was fixed before any arm (S, T, L, D) ran and before BR or C was scored on "
    "the frozen pool. No arm result, baseline score or noise estimate may change it. "
    "The method (a governance number fixed before any arm runs) was settled by cold "
    "round 8, 2 of 2 readers, Grok omitted by my decision: "
    "`founder_inputs/2026-11-26_cold_round8_synthesis.md`. "
    "When explaining the units, the Systems Engine showed three example sizes "
    "(0.005, 0.01, 0.02) and recommended none; I picked from an explanation that "
    "carried those examples."
)

ITEM_10_HEAD = "10. **Decision of November 26, 2026: the margin m.**"


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]


def main():
    write = "--write" in sys.argv[1:]
    results = []

    def check(name, ok, detail=""):
        results.append(ok)
        print(("PASS" if ok else "FAIL") + "  " + name + ((" (" + detail + ")") if detail else ""))

    if not NOTE.is_file():
        print("FAIL  decision note not found; run from the repo root")
        return 1

    old = NOTE.read_text(encoding="utf-8")
    body = old.rstrip("\n")

    check("status anchor found exactly once", old.count(STATUS_ANCHOR) == 1,
          "count " + str(old.count(STATUS_ANCHOR)))
    check("tail anchor found exactly once", old.count(TAIL_ANCHOR) == 1,
          "count " + str(old.count(TAIL_ANCHOR)))
    check("file ends with item 9's last sentence", body.endswith(TAIL_ANCHOR))
    check("item 9 present exactly once", old.count("\n9. **Decisions of October 25, 2026") == 1)
    check("item 10 not already present", old.count("\n10. ") == 0,
          "count " + str(old.count("\n10. ")))
    check("November 26 amendment not already present",
          old.count("Amended November 26, 2026") == 0)
    check("no value of m already in the note", old.count("m = 0.01") == 0)

    if not all(results):
        print("RESULT: checks failed; nothing written")
        return 1

    new = body.replace(STATUS_ANCHOR, STATUS_NEW) + "\n\n" + ITEM_10 + "\n"

    post = []

    def post_check(name, ok):
        post.append(ok)
        print(("PASS" if ok else "FAIL") + "  " + name)

    post_check("new text holds item 10 heading exactly once", new.count(ITEM_10_HEAD) == 1)
    post_check("new text holds 'm = 0.01 Brier units' exactly once",
               new.count("m = 0.01 Brier units") == 1)
    post_check("new text holds the November 26 status sentence exactly once",
               new.count("Amended November 26, 2026: item 10 added (margin m)") == 1)
    post_check("line count grows by exactly 2",
               len(new.splitlines()) == len(body.splitlines()) + 2)
    post_check("items 1 to 9 unchanged",
               new.split("\n\n" + ITEM_10)[0].replace(STATUS_NEW, STATUS_ANCHOR) == body)

    if not all(post):
        print("RESULT: post-checks failed; nothing written")
        return 1

    print("lines before: " + str(len(body.splitlines())) + " | lines after: " + str(len(new.splitlines())))
    print("sha256 before: " + sha(old) + " | sha256 after: " + sha(new))

    if not write:
        print("RESULT: all " + str(len(results) + len(post)) + " checks PASS; check only, nothing written")
        return 0

    NOTE.write_text(new, encoding="utf-8")
    back = NOTE.read_text(encoding="utf-8")
    if back != new:
        print("FAIL  read-back does not match what was written")
        return 1
    print("RESULT: all " + str(len(results) + len(post)) + " checks PASS; written and read back")
    return 0


if __name__ == "__main__":
    sys.exit(main())
