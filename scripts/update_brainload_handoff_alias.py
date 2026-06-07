#!/usr/bin/env python3
"""
update_brainload_handoff_alias.py

Reproducer for the May 2, 2026 brainload_handoff alias update.

Adds founder_inputs/2026-05-02_handoff.md to the cat list in the
brainload_handoff alias defined at ~/.zprofile line 11.

Defensive: aborts before writing if any structural assertion fails.
Writes a backup at ~/.zprofile.backup-2026-05-02 before modifying.
Prints only structural confirmation; never echoes alias content to stdout.

Idempotent: if the handoff file is already in the cat list, exits 0
without modifying the file (still writes backup for audit trail).
"""

import re
import shutil
import sys
from pathlib import Path

ZPROFILE = Path.home() / ".zprofile"
BACKUP = Path.home() / ".zprofile.backup-2026-05-02"
TARGET_LINE_NUM = 11
ALIAS_PREFIX = "alias brainload_handoff="
NEW_FILE = "founder_inputs/2026-05-02_handoff.md"


def main():
    if not ZPROFILE.exists():
        print("FAIL: zprofile does not exist", file=sys.stderr)
        return 1

    lines = ZPROFILE.read_text().splitlines(keepends=True)

    if len(lines) < TARGET_LINE_NUM:
        print("FAIL: too few lines in zprofile", file=sys.stderr)
        return 2

    target = lines[TARGET_LINE_NUM - 1]

    if not target.startswith(ALIAS_PREFIX):
        print("FAIL: line 11 prefix mismatch", file=sys.stderr)
        return 3

    cat_match = re.search(r"\bcat\b\s+([^|]+?)\s*\|\s*pbcopy", target)
    if not cat_match:
        print("FAIL: cat-pbcopy pattern not found", file=sys.stderr)
        return 4

    file_list = cat_match.group(1).split()

    if NEW_FILE in file_list:
        print("NOOP: handoff already in cat list at position " + str(file_list.index(NEW_FILE)))
        shutil.copy2(ZPROFILE, BACKUP)
        print("backup written")
        return 0

    new_file_list = file_list + [NEW_FILE]
    new_target = (
        target[: cat_match.start(1)]
        + " ".join(new_file_list)
        + target[cat_match.end(1):]
    )

    new_lines = lines[:]
    new_lines[TARGET_LINE_NUM - 1] = new_target

    if len(new_lines) != len(lines):
        print("FAIL: line count changed", file=sys.stderr)
        return 5

    if new_target[-1:] != target[-1:]:
        print("FAIL: line ending changed", file=sys.stderr)
        return 6

    if "| pbcopy" not in new_target:
        print("FAIL: pbcopy missing after replacement", file=sys.stderr)
        return 7

    shutil.copy2(ZPROFILE, BACKUP)
    ZPROFILE.write_text("".join(new_lines))

    print("OK: modified line " + str(TARGET_LINE_NUM))
    print("OK: cat list count " + str(len(file_list)) + " -> " + str(len(new_file_list)))
    print("backup written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
