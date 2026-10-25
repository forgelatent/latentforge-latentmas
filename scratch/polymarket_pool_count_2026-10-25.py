# Counts the candidate pool in ~/Projects/data/polymarket. Read-only. Oct 25, 2026.
import json, glob, re, os, datetime as dt
D = os.path.expanduser("~/Projects/data/polymarket")
TODAY = "2026-10-25"
POL = r"president|election|senate|congress|\bfed\b|tariff|ceasefire|iran|russia|ukraine|china|trump|\bwar\b|minister|parliament|\bbill\b|supreme court|governor|prime|treaty|sanction|nato|strike|vote|approval|resign|impeach|ceo|gdp|inflation|unemployment|recession"
CRY = r"bitcoin|ethereum|solana|\bbtc\b|\beth\b|up or down|\bxrp\b|dogecoin"
first, rec = {}, {}
for f in sorted(glob.glob(os.path.join(D, "2026-*.json"))):
    day = os.path.basename(f)[:10]
    for x in json.load(open(f)):
        c = x.get("conditionId"); first.setdefault(c, day); rec[c] = x
def sport(x):
    e = x.get("events") or [{}]
    return bool(x.get("sportsMarketType")) or bool((e[0] if e else {}).get("gameId"))
keep = []
for c, x in rec.items():
    q = (x.get("question") or "").lower(); e = x.get("endDate") or ""
    try: lead = (dt.date.fromisoformat(e[:10]) - dt.date.fromisoformat(first[c])).days; ended = e[:10] < TODAY
    except Exception: continue
    if re.search(POL, q) and not re.search(CRY, q) and not sport(x) and ended and lead >= 7: keep.append(x)
say = [x for x in keep if re.search(r"\bsay\b|\bmention", (x.get("question") or "").lower())]
clean = [x for x in keep if x not in say]
ev = {(x.get("events") or [{}])[0].get("id") for x in clean}
print("files", len(glob.glob(os.path.join(D, "2026-*.json"))), "distinct", len(rec), "sports", sum(1 for x in rec.values() if sport(x)))
print("pool", len(keep), "word-games", len(say), "clean", len(clean), "events", len(ev))
