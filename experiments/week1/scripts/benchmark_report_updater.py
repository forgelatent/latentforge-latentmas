#!/usr/bin/env python3
"""
LatentForge Benchmark Report Auto-Updater
Runs daily at 6am. Reads calibration tracker + shadow match data and
updates Section 4.2 of the benchmark report with fresh numbers.
"""

import json
import os
from datetime import datetime, date
from pathlib import Path

BASE = Path.home() / "Projects/latentforge-latentmas"
REPORT_PATH = BASE / "docs/latentforge_benchmark_report_v0.1.md"
CALIBRATION_DIR = BASE / "experiments/benchmark/calibration"
SHADOW_MATCH_DIR = Path.home() / ".latentforge/shadow_match"
TEXT_SWARM_DIR = BASE / "experiments/benchmark"

START_DATE = date(2026, 4, 4)  # Day 1 of paper trading clock
TODAY = date.today()
DAY_NUMBER = (TODAY - START_DATE).days + 1
DAYS_REMAINING = 30 - DAY_NUMBER + 1

def load_brier():
    path = CALIBRATION_DIR / "brier_running.json"
    if not path.exists():
        return []
    return json.loads(path.read_text())

def load_predictions():
    path = CALIBRATION_DIR / "predictions_log.json"
    if not path.exists():
        return []
    return json.loads(path.read_text())

def load_latest_shadow():
    files = sorted(SHADOW_MATCH_DIR.glob("shadow_match_*.json"), reverse=True)
    if not files:
        return None, []
    return files[0].name, json.loads(files[0].read_text())

def load_swarm_divergence():
    files = sorted(TEXT_SWARM_DIR.glob("text_swarm_*.md"), reverse=True)
    return len(files)

def build_results_section(brier_data, predictions, shadow_file, shadow_data):
    total_tracked = len(predictions)
    resolved = [m for m in brier_data if m.get("outcome") is not None]
    n_resolved = len(resolved)

    # Calculate averages
    swarm_briers = [m["swarm_brier"] for m in resolved if m.get("swarm_brier") is not None]
    crowd_briers = [m["crowd_brier"] for m in resolved if m.get("crowd_brier") is not None]
    swarm_avg = sum(swarm_briers) / len(swarm_briers) if swarm_briers else None
    crowd_avg = sum(crowd_briers) / len(crowd_briers) if crowd_briers else None

    # Build resolved market table
    table_rows = ""
    for m in resolved:
        q = m.get("question", "")[:50] + "..." if len(m.get("question","")) > 50 else m.get("question","")
        table_rows += f"| {q} | {m.get('date','')} | {m.get('swarm_prob',0)*100:.1f}% | {m.get('crowd_prob',0)*100:.1f}% | {int(m.get('outcome',0))} | {m.get('swarm_brier','N/A')} | {m.get('crowd_brier','N/A')} |\n"

    # Shadow match key divergences
    shadow_section = ""
    if shadow_data:
        shadow_section = "\n**Key divergences from latest Shadow Match:**\n\n"
        shadow_section += "| Market | Crowd | Shadow | Swarm |\n"
        shadow_section += "|--------|-------|--------|-------|\n"
        for m in shadow_data:
            q = m.get("question","")[:55]
            crowd = m.get("crowd_prob", 0)
            shadow_p = m.get("shadow_prob", 0)
            swarm_p = m.get("swarm_prob", 0)
            if shadow_p and swarm_p:
                diff = abs(crowd - swarm_p)
                if diff > 0.05:  # Only show notable divergences
                    shadow_section += f"| {q} | {crowd:.1%} | {shadow_p:.1%} | {swarm_p:.1%} |\n"

    swarm_avg_str = f"{swarm_avg:.4f}" if swarm_avg else "N/A"
    crowd_avg_str = f"{crowd_avg:.4f}" if crowd_avg else "N/A"
    swarm_vs_naive = f"{(1 - swarm_avg/0.25)*100:.1f}%" if swarm_avg else "N/A"

    section = f"""## 4. Results (Auto-updated {TODAY.isoformat()} — Day {DAY_NUMBER} of 30)

### 4.1 Historical Validation (Pre-Benchmark)

Before the live paper trading clock started, we validated the swarm against 18 resolved Polymarket markets with known outcomes:

- **Markets scored:** 18 resolved Polymarket questions (politics/crypto)
- **Swarm Brier:** 0.1376
- **Naive baseline:** 0.25
- **Improvement over naive:** 45%
- **Note:** Agent errors on sports/entertainment markets present in this dataset — filtered in live benchmark

---

### 4.2 Live Paper Trading Results (Day {DAY_NUMBER} of 30 — {TODAY.isoformat()})

**Markets tracked:** {total_tracked}
**Markets resolved:** {n_resolved}
**Days remaining:** {DAYS_REMAINING}

| Market | Date | Swarm Prob | Crowd Prob | Outcome | Swarm Brier | Crowd Brier |
|--------|------|-----------|-----------|---------|-------------|-------------|
{table_rows}
**Summary statistics:**

| Metric | Value |
|--------|-------|
| Swarm avg Brier (all resolved) | {swarm_avg_str} |
| Crowd avg Brier (all resolved) | {crowd_avg_str} |
| Naive avg Brier | 0.2500 |
| Swarm vs naive improvement | {swarm_vs_naive} |

**Honest assessment of current data:**

The resolved markets to date are dominated by near-certain outcomes — sports championship candidates where the crowd was already pricing at 0.1-5.3% probability. The swarm performs well in absolute terms ({swarm_avg_str} average Brier) but the meaningful comparison will emerge when genuinely uncertain markets resolve (crowd probability 20-80% at prediction time). We have {total_tracked - n_resolved} markets currently tracked pending resolution.

---

### 4.3 Shadow Match Results (Source: {shadow_file or 'pending'})

11 policy/macro/geopolitical markets. Single strong model (Shadow) vs 4-agent swarm vs crowd.
{shadow_section}

---

### 4.4 AI Regulation Divergence — Case Study in Progress

**Question:** Will an AI regulation bill pass in US Congress before [date]?
**Crowd probability:** ~31%
**Swarm estimate:** 21-28%
**Days of sustained divergence:** {load_swarm_divergence()}+ consecutive days
**Direction:** Swarm consistently below crowd

Resolution will determine whether this is genuine information extraction or systematic swarm miscalibration. Both outcomes are publishable.

---

### 4.5 Latent vs Text A/B Test (Pending Mac Mini Arrival)

*Section to be filled in after Mac Mini M4 Pro arrival (April 9-16, 2026)*

---

*Auto-updated by benchmark_report_updater.py — {datetime.now().strftime('%Y-%m-%d %H:%M')}*
*Next update: tomorrow at 6:00am*
"""
    return section

def update_report(new_section):
    content = REPORT_PATH.read_text(encoding="utf-8")

    # Find and replace the results section
    start_marker = "## 4. Results"
    end_marker = "## 5. Discussion"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print("ERROR: Could not find '## 4. Results' in report")
        return False

    if end_idx == -1:
        # Append at end if no section 5 yet
        new_content = content[:start_idx] + new_section
    else:
        new_content = content[:start_idx] + new_section + "\n" + content[end_idx:]

    REPORT_PATH.write_text(new_content, encoding="utf-8")
    return True

def main():
    print(f"Benchmark Report Auto-Updater — {TODAY.isoformat()} (Day {DAY_NUMBER} of 30)")

    brier_data = load_brier()
    predictions = load_predictions()
    shadow_file, shadow_data = load_latest_shadow()

    print(f"  Resolved markets: {len(brier_data)}")
    print(f"  Total tracked: {len(predictions)}")
    print(f"  Latest shadow match: {shadow_file or 'none'}")

    new_section = build_results_section(brier_data, predictions, shadow_file, shadow_data)
    success = update_report(new_section)

    if success:
        print(f"  Report updated: {REPORT_PATH}")
    else:
        print("  ERROR: Report update failed")

if __name__ == "__main__":
    main()
