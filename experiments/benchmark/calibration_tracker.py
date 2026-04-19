🚨 OLD DATA — see docs/INCIDENT_2026-04-18.md for details
"""
LatentForge Live Calibration Tracker v1.1
Fixed: date parsing, 90-day window, GTA VI filter
"""

import urllib.request
import json
import os
from pathlib import Path
from datetime import datetime, timezone

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
BASE_DIR = Path("/Users/latentforge/Projects/latentforge-latentmas/experiments/benchmark/calibration")
BASE_DIR.mkdir(parents=True, exist_ok=True)

PREDICTIONS_FILE = BASE_DIR / "predictions_log.json"

POLICY_KEYWORDS = [
    "regulation", "congress", "senate", "house", "election", "vote", "president",
    "fed", "federal reserve", "rate cut", "inflation", "cpi", "unemployment",
    "iran", "nuclear", "china", "taiwan", "ukraine", "russia", "nato",
    "powell", "treasury", "gdp", "recession", "tariff", "trade",
    "republican", "democrat", "midterm", "supreme court", "legislation",
    "parliament", "prime minister", "chancellor", "sanctions"
]

def get_category(question):
    q = question.lower()
    for kw in POLICY_KEYWORDS:
        if kw in q:
            return "policy"
    return "other"

BRIER_LOG_FILE = BASE_DIR / "brier_running.json"

NOISE_TERMS = ["gta vi", "gta6", "rihanna album", "playboi carti", "jesus christ return"]


def is_noise(question):
    q = question.lower()
    return any(term in q for term in NOISE_TERMS)


def fetch_near_term_markets(days=90, limit=200):
    req = urllib.request.Request(
        "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=" + str(limit) + "&competitive=true",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())

    now = datetime.now(timezone.utc)
    near_term = []
    for m in data:
        question = m.get("question", "")
        market_id = m.get("id", "")
        if not question or not market_id:
            continue
        if is_noise(question):
            continue
        end = m.get("endDate", "") or m.get("endDateIso", "")
        try:
            end_dt = datetime.strptime(end[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            days_remaining = (end_dt - now).days
            if days_remaining <= days:  # includes negative (overdue, waiting resolution)
                last_price = m.get("lastTradePrice", 0.5)
                if not last_price or float(last_price) < 0.05 or float(last_price) > 0.95:
                    continue
                near_term.append({
                    "id": market_id,
                    "question": question,
                    "end_date": end[:10],
                    "days_remaining": days_remaining,
                    "crowd_prob": float(last_price) if last_price else 0.5
                })
        except Exception:
            pass

    near_term.sort(key=lambda x: x["days_remaining"])
    return near_term


def check_resolution(market_id):
    req = urllib.request.Request(
        "https://gamma-api.polymarket.com/markets/" + str(market_id),
        headers={"User-Agent": "Mozilla/5.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            m = json.loads(r.read())
        prices_raw = m.get("outcomePrices", "")
        if not prices_raw:
            return None
        p = [float(x) for x in json.loads(prices_raw)]
        if all(v == 0 for v in p):
            return None
        if p[0] > 0.95:
            return 1
        if p[0] < 0.05:
            return 0
        return None
    except Exception:
        return None


def swarm_estimate(question):
    if not ANTHROPIC_API_KEY:
        return None
    agents = [
        "You are a macro analyst forecasting political and economic events. Give a probability 0-100 that this market resolves YES. Reply with a single integer only.",
        "You are a quantitative researcher. Give a probability 0-100 that this market resolves YES. Reply with a single integer only.",
        "You are a contrarian forecaster who challenges consensus. Give a probability 0-100 that this market resolves YES. Reply with a single integer only.",
    ]
    probs = []
    for system in agents:
        try:
            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 10,
                "system": system,
                "messages": [{"role": "user", "content": question}]
            }).encode()
            req = urllib.request.Request(
                "https://api.anthropic.com/v1/messages",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": ANTHROPIC_API_KEY,
                    "anthropic-version": "2023-06-01"
                }
            )
            with urllib.request.urlopen(req, timeout=20) as r:
                resp = json.loads(r.read())
            raw = resp["content"][0]["text"].strip().replace("%", "")
            probs.append(float(raw) / 100.0)
        except Exception as e:
            print("    Agent error: " + str(e)[:60])
    return round(sum(probs) / len(probs), 3) if probs else None


def load_predictions():
    if PREDICTIONS_FILE.exists():
        with open(PREDICTIONS_FILE) as f:
            return json.load(f)
    return {}


def save_predictions(preds):
    with open(PREDICTIONS_FILE, "w") as f:
        json.dump(preds, f, indent=2)


def load_brier_log():
    if BRIER_LOG_FILE.exists():
        with open(BRIER_LOG_FILE) as f:
            return json.load(f)
    return []


def save_brier_log(log):
    with open(BRIER_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


def run():
    today = datetime.now().strftime("%Y-%m-%d")
    print("LatentForge Live Calibration Tracker v1.1")
    print("Date: " + today)
    print("")

    predictions = load_predictions()
    brier_log = load_brier_log()

    # Step 1: Check existing predictions for resolution
    print("Checking " + str(len(predictions)) + " tracked markets for resolution...")
    newly_resolved = 0
    for market_id, entry in list(predictions.items()):
        if entry.get("resolved"):
            continue
        outcome = check_resolution(market_id)
        if outcome is not None:
            entry["resolved"] = True
            entry["outcome"] = outcome
            entry["resolved_date"] = today
            swarm_prob = entry.get("swarm_prob", 0.5)
            crowd_prob = entry.get("crowd_prob", 0.5)
            if crowd_prob < 0.05 or crowd_prob > 0.95:
                continue
            swarm_brier = round((swarm_prob - outcome) ** 2, 4)
            crowd_brier = round((crowd_prob - outcome) ** 2, 4)
            naive_brier = round((0.5 - outcome) ** 2, 4)
            entry["swarm_brier"] = swarm_brier
            entry["crowd_brier"] = crowd_brier
            entry["naive_brier"] = naive_brier
            brier_log.append({
                "date": today,
                "market_id": market_id,
                "question": entry.get("question", "")[:80],
                "swarm_prob": swarm_prob,
                "crowd_prob": crowd_prob,
                "outcome": outcome,
                "swarm_brier": swarm_brier,
                "crowd_brier": crowd_brier,
                "naive_brier": naive_brier
            })
            newly_resolved += 1
            print("  RESOLVED [" + str(outcome) + "] " + entry.get("question", "")[:60])
            print("    swarm=" + str(swarm_prob) + " crowd=" + str(crowd_prob) + " swarm_brier=" + str(swarm_brier))

    if newly_resolved == 0:
        print("  No new resolutions today.")

    # Step 2: Fetch near-term markets and predict new ones
    print("")
    print("Fetching markets closing within 90 days...")
    markets = fetch_near_term_markets(days=90, limit=200)
    print("Found " + str(len(markets)) + " qualifying markets")

    new_predictions = 0
    for m in markets[:20]:
        market_id = m["id"]
        if market_id in predictions:
            continue
        question = m["question"]
        days_left = m["days_remaining"]
        tag = "overdue" if days_left < 0 else (str(days_left) + "d")
        print("  [" + tag + "] " + question[:65])
        swarm_prob = swarm_estimate(question)
        if swarm_prob is None:
            continue
        predictions[market_id] = {
            "question": question,
            "end_date": m["end_date"],
            "days_remaining": m["days_remaining"],
            "crowd_prob": m["crowd_prob"],
            "swarm_prob": swarm_prob,
            "predicted_date": today,
            "resolved": False
        }
        print("    swarm=" + str(swarm_prob) + " crowd=" + str(m["crowd_prob"]))
        new_predictions += 1

    save_predictions(predictions)
    save_brier_log(brier_log)

    # Step 3: Summary
    print("")
    print("=== CALIBRATION SUMMARY ===")
    print("Total markets tracked: " + str(len(predictions)))
    print("New predictions today: " + str(new_predictions))
    print("Newly resolved: " + str(newly_resolved))

    brier_log_all = [e for e in brier_log if 0.05 <= e.get("crowd_prob", 0.5) <= 0.95]
    brier_log_policy = [e for e in brier_log_all if get_category(e.get("question","")) == "policy"]

    def print_track(label, log):
        if not log:
            print(f"  No resolved {label} markets yet.")
            return
        n = len(log)
        avg_swarm = round(sum(e["swarm_brier"] for e in log) / n, 4)
        avg_crowd = round(sum(e["crowd_brier"] for e in log) / n, 4)
        avg_naive = round(sum(e["naive_brier"] for e in log) / n, 4)
        swarm_vs_naive = round((avg_naive - avg_swarm) / avg_naive * 100, 1)
        swarm_vs_crowd = round((avg_crowd - avg_swarm) / avg_crowd * 100, 1) if avg_crowd != 0 else 0.0
        bss = round(1 - (avg_swarm / avg_crowd), 4) if avg_crowd != 0 else 0.0
        import math
        swarm_probs = [e["swarm_prob"] for e in log if e.get("swarm_prob") is not None]
        crowd_probs = [e["crowd_prob"] for e in log if e.get("crowd_prob") is not None]
        swarm_entropy = round(-sum(p * math.log2(p) + (1-p) * math.log2(1-p) for p in swarm_probs if 0 < p < 1) / len(swarm_probs), 4) if swarm_probs else 0.0
        swarm_dispersion = round((max(swarm_probs) - min(swarm_probs)) * 100, 1) if len(swarm_probs) > 1 else 0.0
        crowd_dispersion = round((max(crowd_probs) - min(crowd_probs)) * 100, 1) if len(crowd_probs) > 1 else 0.0
        avg_divergence = round(sum(abs(e["swarm_prob"] - e["crowd_prob"]) for e in log) / n * 100, 1)
        print(f"  Resolved markets scored: {n}")
        print(f"  Swarm avg Brier:  {avg_swarm}")
        print(f"  Crowd avg Brier:  {avg_crowd}")
        print(f"  Naive avg Brier:  {avg_naive}")
        print(f"  Swarm vs naive:   {swarm_vs_naive}%")
        print(f"  Swarm vs crowd:   {swarm_vs_crowd}%")
        print(f"  Brier Skill Score:{bss}  (0=crowd-level, 1=perfect, negative=worse than crowd)")
        print(f"  Swarm entropy:    {swarm_entropy}  (higher = more uncertain)")
        print(f"  Swarm dispersion: {swarm_dispersion}pts  (range of swarm predictions)")
        print(f"  Crowd dispersion: {crowd_dispersion}pts  (range of crowd predictions)")
        print(f"  Avg divergence:   {avg_divergence}pts  (avg |swarm - crowd| on resolved markets)")

    print("")
    print("--- PRIMARY TRACK (policy/macro/geopolitics/elections) ---")
    print_track("policy", brier_log_policy)
    print("")
    print("--- FULL TRACK (all categories, for transparency) ---")
    print_track("all", brier_log_all)
    if not brier_log_all:
        print("No resolved markets yet — check back daily as markets close.")

    print("")
    print("Logs: " + str(BASE_DIR))


if __name__ == "__main__":
    run()
