#!/usr/bin/env python3
"""
test_kalshi_pull.py  -  September 19, 2026

Offline test for experiments/week1/scripts/kalshi_pull.py.
Feeds the script nine fake Kalshi answers. No internet. It never touches
~/Projects/data/kalshi: the output path is pointed at a temporary folder.

Run from the repo root:   python3 ~/Downloads/test_kalshi_pull.py

For every BAD answer it checks two things:
  - the script stops with the right exit code, and
  - a good file that was already on disk is left byte-for-byte untouched.
On the UNPATCHED script, expect 3 of 9 (six FAILs). That is the bug, shown.
On the PATCHED script, all nine must PASS.
"""
import contextlib
import importlib.util
import io
import json
import os
import pathlib
import sys
import tempfile

sys.dont_write_bytecode = True  # leave no __pycache__ folder in the repo

TARGET = os.path.join("experiments", "week1", "scripts", "kalshi_pull.py")
SENTINEL = b'[{"title": "GOOD FILE ALREADY ON DISK"}]'


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self.payload


def load_script():
    spec = importlib.util.spec_from_file_location("kalshi_pull_under_test", TARGET)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_case(mod, tmpdir, fake_get):
    out = pathlib.Path(tmpdir) / "markets_TEST.json"
    out.write_bytes(SENTINEL)
    mod.OUTPUT_FILE = out
    mod.requests.get = fake_get
    code = 0
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            mod.main()
        except SystemExit as exc:
            code = exc.code if isinstance(exc.code, int) else 1
    return code, out.read_bytes(), buf.getvalue()


def answer(payload):
    return lambda *a, **k: FakeResponse(payload)


def network_down(*a, **k):
    raise ConnectionError("simulated: no network")


GOOD = [{"title": "A market"}]

# name, fake answer, expected exit code, should the file be rewritten?
CASES = [
    ("good answer, dict with markets",        answer({"markets": GOOD, "cursor": ""}),    0, True),
    ("good answer, more pages exist",         answer({"markets": GOOD, "cursor": "abc"}), 0, True),
    ("good answer, plain list",               answer(GOOD),                               0, True),
    ("BAD: empty markets list",               answer({"markets": []}),                    2, False),
    ("BAD: wrong shape, no markets key",      answer({"error": "something"}),             2, False),
    ("BAD: markets is null",                  answer({"markets": None}),                  2, False),
    ("BAD: answer is just a string",          answer("not what we expected"),             2, False),
    ("BAD: empty plain list",                 answer([]),                                 2, False),
    ("BAD: network down",                     network_down,                               1, False),
]


def main():
    if not os.path.isfile(TARGET):
        print("Cannot find " + TARGET + " - run this from the repo root.")
        sys.exit(1)
    try:
        mod = load_script()
    except Exception as exc:
        print("Could not load the script: " + type(exc).__name__ + ": " + str(exc))
        sys.exit(1)

    passed = 0
    with tempfile.TemporaryDirectory() as tmpdir:
        for name, fake_get, want_code, want_rewrite in CASES:
            code, on_disk, printed = run_case(mod, tmpdir, fake_get)
            rewritten = on_disk != SENTINEL
            problems = []
            if code != want_code:
                problems.append("exit code " + str(code) + ", wanted " + str(want_code))
            if rewritten != want_rewrite:
                problems.append("good file was OVERWRITTEN" if rewritten
                                else "file was not written")
            if want_rewrite and not problems:
                try:
                    if json.loads(on_disk.decode("utf-8")) != GOOD:
                        problems.append("saved content is not what was sent")
                except Exception:
                    problems.append("saved file is not valid JSON")
            if "more pages exist" in name and "first page only" not in printed:
                problems.append("no first-page-only NOTE in the log")
            if problems:
                print("FAIL  " + name + "  ->  " + "; ".join(problems))
            else:
                passed += 1
                print("PASS  " + name)

    total = len(CASES)
    print("RESULT: " + str(passed) + " of " + str(total) + " passed")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
