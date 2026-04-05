import os, json, datetime
import anthropic
from pathlib import Path

CLIENT = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
MODEL = "claude-sonnet-4-6"
LOG_DIR = Path.home() / ".latentforge" / "shadow_match"
LOG_DIR.mkdir(parents=True, exist_ok=True)

MARKETS = [
    {"id": "desantis_2028", "question": "Will Ron DeSantis win the 2028 Republican presidential nomination?", "crowd_prob": 0.0265},
    {"id": "buttigieg_2028", "question": "Will Pete Buttigieg win the 2028 Democratic presidential nomination?", "crowd_prob": 0.0375},
    {"id": "vance_2028_rep", "question": "Will J.D. Vance win the 2028 Republican presidential nomination?", "crowd_prob": 0.367},
    {"id": "newsom_2028", "question": "Will Gavin Newsom win the 2028 US Presidential Election?", "crowd_prob": 0.1725},
    {"id": "vance_2028_gen", "question": "Will JD Vance win the 2028 US Presidential Election?", "crowd_prob": 0.1765},
    {"id": "bitcoin_60_80", "question": "Will Bitcoin hit $60k or $80k first?", "crowd_prob": 0.65},
    {"id": "china_taiwan", "question": "Will China blockade Taiwan by June 30?", "crowd_prob": 0.0365},
    {"id": "fed_cuts", "question": "Will 9 Fed rate cuts happen in 2026?", "crowd_prob": 0.0045},
    {"id": "powell", "question": "Will Jerome Powell be confirmed as Fed Chair?", "crowd_prob": 0.0015},
    {"id": "iran_deal", "question": "US-Iran nuclear deal by June 30?", "crowd_prob": 0.225},
    {"id": "ppp_korea", "question": "Will the People Power Party (PPP) win the 2026 South Korean local elections?", "crowd_prob": 0.0415},
]

SYSTEM = (
    "You are a rigorous forecasting analyst. Output ONLY a JSON object with two keys: "
    "probability (float 0-1) and reasoning (one sentence). No preamble, no markdown."
)

AGENTS = [
    ("Base Rate", "Focus on historical base rates and reference class forecasting."),
    ("News",      "Focus on recent developments and momentum signals."),
    ("Contrarian","Steelman the minority position. What is the crowd missing?"),
]

def predict(question, crowd_prob, role_instruction=""):
    lines = [
        "Question: " + question,
        "Crowd probability: " + f"{crowd_prob:.1%}",
    ]
    if role_instruction:
        lines.append("Your role: " + role_instruction)
    lines.append("Give your independent probability estimate.")
    msg = "\n".join(lines)
    r = CLIENT.messages.create(
        model=MODEL,
        max_tokens=256,
        system=SYSTEM,
        messages=[{"role": "user", "content": msg}]
    )
    try:
        return json.loads(r.content[0].text.strip())
    except Exception:
        return {"probability": None, "reasoning": r.content[0].text.strip()}

results = []
run_date = datetime.date.today().isoformat()
print("\nShadow Match — " + run_date)
print("=" * 60)

for m in MARKETS:
    q, cp = m["question"], m["crowd_prob"]
    print("\n" + q[:80])

    shadow = predict(q, cp)

    votes = []
    for name, role in AGENTS:
        v = predict(q, cp, role)
        v["agent"] = name
        votes.append(v)

    valid = [v["probability"] for v in votes if v.get("probability") is not None]
    swarm_prob = sum(valid) / len(valid) if valid else None

    print("  Crowd:  " + f"{cp:.1%}")
    sp = shadow.get("probability")
    print("  Shadow: " + (f"{sp:.1%}" if sp is not None else "ERR") + "  — " + str(shadow.get("reasoning", ""))[:80])
    print("  Swarm:  " + (f"{swarm_prob:.1%}" if swarm_prob is not None else "ERR"))

    results.append({
        "date": run_date,
        "market_id": m["id"],
        "question": q,
        "crowd_prob": cp,
        "shadow_prob": sp,
        "shadow_reasoning": shadow.get("reasoning"),
        "swarm_prob": swarm_prob,
        "swarm_agents": votes,
        "outcome": None,
        "shadow_brier": None,
        "swarm_brier": None,
    })

log_path = LOG_DIR / ("shadow_match_" + run_date + ".json")
with open(log_path, "w") as f:
    json.dump(results, f, indent=2)
print("\nSaved → " + str(log_path))
