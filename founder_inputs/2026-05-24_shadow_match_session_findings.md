# Raw notes — findings during May 24 shadow_match decision sprint

**Status:** Not canonical. Raw observation notes captured during the May 24 evening session while making shadow_match restoration decisions. Pattern D guard applied: writing canonical ledger entries while still inside the cognitive pressure of fresh discoveries is the failure shape the guard exists to defend against. Decision on whether to elevate either or both findings to `incident_ledger.md` is deferred to a fresh-context session.

**Context of discovery:** During the reload-gate decision (one of three open decisions on shadow_match restoration), Founder asked whether any tracked markets resolve in the next day or two. The two findings below surfaced while attempting to answer that question.

**Cross-reference:** `founder_inputs/2026-05-24_shadow_match_restoration_review.md` (the multi-engine review record this session was working through); `docs/state_manifest.md` polymarket-pull and calibration-tracker component entries.

---

## Finding 1: Silent-fallback parse bug in a Claude-written diagnostic one-liner

### What happened

Claude wrote a one-line Python script to count markets in `~/Projects/data/polymarket/2026-05-24.json` resolving within various time horizons (7 days, 14 days, 30 days, etc.). The script reported "0 markets resolving within 365 days" for all 91 markets in the file. This was structurally implausible — Polymarket markets always have resolution dates — so the Founder asked to look closer.

A follow-up diagnostic revealed the dates were present and several resolved in the next 1-14 days. The original script had silently swallowed a parse error and reported zero counts as if the filter had simply matched nothing.

### Root cause

The script's parse logic:

```python
end = m.get('endDateIso') or m.get('endDate')
try:
    dt = datetime.fromisoformat(end.replace('Z','+00:00'))
    ...
except: pass
```

When `endDateIso` was present (a date-only string like `'2026-06-01'`), `fromisoformat` parsed it as a naive datetime (no timezone). The subsequent comparison `now <= dt <= horizon` raised a TypeError because `now` and `horizon` were timezone-aware. The bare `except: pass` swallowed every such error. Every market hit this path. The script printed "0" as if the filter had matched nothing rather than failing.

### Why this matters

This is a Pattern A shape — a script reporting success/clean output while silently hiding failure. It is the same failure shape the post-April-18 architecture was designed to prevent. Tonight's instance is small (a throwaway diagnostic one-liner Claude wrote in the chat to support a decision conversation, not a production launchd component), but the shape is the same.

The discipline implication: even short scripts Claude writes in service of session conversations need the "fail loudly, not silently" discipline. Bare `except: pass` is a contamination-shape pattern regardless of the script's scope or lifespan. Future Claude-written diagnostics should either let exceptions propagate or explicitly print/log what was skipped and why.

### Reproducer (the buggy script, verbatim)

```python
python3 -c "
import json
from datetime import datetime, timezone, timedelta
d = json.load(open('/Users/latentforge/Projects/data/polymarket/2026-05-24.json'))
now = datetime.now(timezone.utc)
horizon = now + timedelta(days=7)
soon = []
for m in d:
    end = m.get('endDateIso') or m.get('endDate')
    if not end: continue
    try:
        dt = datetime.fromisoformat(end.replace('Z','+00:00'))
        if now <= dt <= horizon:
            soon.append((dt, m.get('question','?')[:80]))
    except: pass
soon.sort()
print(f'Markets resolving in next 7 days: {len(soon)}')
"
```

Output: `Markets resolving in next 7 days: 0` (incorrect; truth was a non-zero count visible in Finding 2 sample data).

### Reproducer for the correct count

The corrected script should prefer the timezone-bearing `endDate` field (full ISO timestamp ending in `Z`) over the date-only `endDateIso` field. A clean version not yet implemented; documenting the fix-direction here rather than writing/running it tonight under cognitive pressure.

### Disposition

Finding logged. No production code affected. Ledger elevation decision deferred to fresh session — open question is whether this small instance is worth a separate ledger entry under Section 4, or whether it folds into the existing "Pattern A: silent fallback" framing in Section 8.

---

## Finding 2: polymarket-pull output is unfiltered general Polymarket data, not the policy/macro/geopolitics/elections subset

### What happened

While running the corrected diagnostic from Finding 1, the first five markets in `~/Projects/data/polymarket/2026-05-24.json` were inspected. Sample (verbatim from terminal output):

```
question: Kosice: Kilian Feldbausch vs Gilles Arnaud Bailly
  endDate: '2026-06-01T08:00:00Z'

question: Will the match end in a draw?
  endDate: '2026-06-06T18:45:00Z'

question: Will Monero hit $1000 in 2026?
  endDate: '2027-01-01T05:00:00Z'

question: Will Colombia win on 2026-06-01?
  endDate: '2026-06-01T23:00:00Z'

question: CD La Serena vs. CD Limache: O/U 2.5
  endDate: '2026-05-24T19:00:00Z'
```

Three of five are sports markets (tennis, soccer over/under, soccer match outcome). One is a crypto price market. One is a soccer match outcome with date. None are policy, macro, geopolitics, or elections markets — the categories the project's prediction-market work is supposed to track.

### What this means structurally

`polymarket-pull` (the launchd job at 4:40 AM nightly) pulls **general Polymarket data without category filtering**. The 91 markets in the daily file are whatever the Polymarket Gamma API returns from its general endpoint — primarily sports and crypto by volume, with policy/macro/elections markets as a small subset.

The category filtering the project relies on for forecasting work happens **downstream**, inside `calibration_tracker.py` (per `build_log.md` Section 2.3.2: "5-95% crowd probability filter + policy/macro/geopolitics/elections category filter, dual-track reporting"). `calibration_tracker.py` applies its filters in-script when it iterates over the daily pull.

This is not a bug. It is a design choice: pull layer does *only* the pull, category judgment lives downstream where it can be inspected and changed without modifying the data layer (per the April 6 architectural rule "LLMs handle judgment, scripts handle everything else"). The pull layer's neutrality is a feature.

### Why this matters for shadow_match restoration

The multi-engine review captured in `2026-05-24_shadow_match_restoration_review.md` reached Decision 1: 1A (shared benchmark-questions module between shadow_match and text-swarm) by unanimous engine vote. Both Gemini's and ChatGPT's code outlines assumed the polymarket-pull file contained the benchmark markets and that shadow_match's filtering work was just "match question text" or "filter by market ID." Sample from Gemini's outline:

```python
filtered_markets = [m for m in all_markets if str(m.get("id")) in LONGITUDINAL_MARKETS]
```

This assumes `LONGITUDINAL_MARKETS` IDs are present in the daily pull. If the 11 benchmark markets are policy/macro questions, and the daily pull contains mostly sports and crypto, the 11 benchmark markets may or may not be in the daily pull on any given day — depending on whether Polymarket's general API is currently returning them.

The implementation work for Decision 1 therefore needs more than the engine outlines captured. shadow_match needs to either:

1. Do both category filtering (drop sports/crypto/etc.) *and* benchmark-question matching, in that order — same shape as calibration_tracker but for the 11-question set instead of the live-discovered set
2. Read the same data calibration_tracker reads (the post-filtered subset) rather than the raw pull
3. Pull directly from Polymarket's API itself, applying its own category and question-matching filters

None of these are obviously correct without more investigation. The right call depends on how calibration_tracker is currently feeding its filtered markets back out — whether they're stored anywhere shadow_match could read, or whether they live in calibration_tracker's runtime only.

### Reproducer

Show the polymarket-pull file structure:
```
python3 -c "import json; d=json.load(open('/Users/latentforge/Projects/data/polymarket/2026-05-24.json')); print('type:', type(d).__name__); print('count:', len(d) if hasattr(d,'__len__') else 'n/a'); print('keys of first item:', list(d[0].keys()) if isinstance(d,list) and d else 'n/a')"
```

Show the first five markets:
```
python3 -c "
import json
d = json.load(open('/Users/latentforge/Projects/data/polymarket/2026-05-24.json'))
for m in d[:5]:
    print(f'  question: {m.get(\"question\",\"?\")[:60]}')
    print(f'    endDate: {repr(m.get(\"endDate\"))}')
    print(f'    active: {m.get(\"active\")}, closed: {m.get(\"closed\")}')
    print()
"
```

### Disposition

Finding logged. No production code change tonight. This finding affects shadow_match Decision 1's implementation scope but does not change Decision 1's *direction* (the unanimous 1A vote stands; the question is just *how* to implement it). In a fresh session:

- Decide whether to update the `2026-05-24_shadow_match_restoration_review.md` review file with a Decision 1 implementation note flagging this finding
- Decide whether this is worth a separate ledger entry under Section 4 (May 24 third entry), or whether it folds into the existing build_log.md Section 2.3.2 framing
- Investigate whether calibration_tracker's filtered output is reusable (i.e., does it persist its filtered set anywhere on disk that shadow_match could read?)

---

## Session-discipline observation

Both findings emerged inside a 30-minute decision sprint that was attempting to finish the three open shadow_match decisions tonight. The Pattern D guard fired correctly when the second finding (which has design implications for a decision already made) surfaced — the session paused, the findings were captured, and structural changes to the review record were deferred to a fresh session.

The original decision sprint completed two of three decisions before the pause:

- Decision 3 (cost-comparison layer): **3B** — remove entirely. Reasoning: the cost number's original purpose was the Rain grant pitch, which is on hold per the April 8 all-engines decision. No current 2026 reason to keep it.
- Decision: implementation sequencing: **Gemini's order** — Data → strip bias (cost + grant prose) → scoring → docstring rewrite. Reasoning: clean out structural bias before adding new measurements, so new measurements get added to a clean foundation.

Decision: reload-gate stringency — **deferred** pending fresh-session investigation of when the 11 benchmark markets actually resolve. (This was the question that surfaced Findings 1 and 2.)

These two locked decisions should be folded into `2026-05-24_shadow_match_restoration_review.md` in the same fresh session that handles the deferred reload-gate decision.

---

*End of raw notes. Not for citation. Pending fresh-session review for canonical placement.*
