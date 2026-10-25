# Resolution lookup for the Oct 25 candidate pool. Writes ONE file in scratch/. Oct 25, 2026.
# Borrows the mode1 loader's Gamma mechanics: real User-Agent, two-pass live/closed fetch, limit<=100, JSON-string outcomePrices.
import json, glob, re, os, time, hashlib, urllib.request, urllib.parse, datetime as dt
D = os.path.expanduser("~/Projects/data/polymarket"); TODAY = "2026-10-25"
OUT = "scratch/pool_resolutions_2026-10-25.json"
UA = "LatentForge-pool-resolution/1.0"; EP = "https://gamma-api.polymarket.com/markets"
POL = r"president|election|senate|congress|\bfed\b|tariff|ceasefire|iran|russia|ukraine|china|trump|\bwar\b|minister|parliament|\bbill\b|supreme court|governor|prime|treaty|sanction|nato|strike|vote|approval|resign|impeach|ceo|gdp|inflation|unemployment|recession"
CRY = r"bitcoin|ethereum|solana|\bbtc\b|\beth\b|up or down|\bxrp\b|dogecoin"
first, rec = {}, {}
for f in sorted(glob.glob(os.path.join(D, "2026-*.json"))):
    day = os.path.basename(f)[:10]
    for x in json.load(open(f)):
        c = x.get("conditionId"); first.setdefault(c, day); rec[c] = x
def sport(x):
    e = x.get("events") or [{}]; return bool(x.get("sportsMarketType")) or bool((e[0] if e else {}).get("gameId"))
pool = {}
for c, x in rec.items():
    q = (x.get("question") or "").lower(); e = x.get("endDate") or ""
    try: lead = (dt.date.fromisoformat(e[:10]) - dt.date.fromisoformat(first[c])).days; ended = e[:10] < TODAY
    except Exception: continue
    if c and re.search(POL, q) and not re.search(CRY, q) and not sport(x) and ended and lead >= 7 and not re.search(r"\bsay\b|\bmention", q): pool[c] = x
assert len(pool) == 412, f"pool is {len(pool)}, expected 412"
def fetch(cids, closed):
    params = [("condition_ids", c) for c in cids] + ([("closed", "true")] if closed else []) + [("limit", "100")]
    url = EP + "?" + urllib.parse.urlencode(params); last = None
    for i in range(3):
        if i: time.sleep([10, 30][i - 1])
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30) as r: raw = r.read()
            m = json.loads(raw.decode("utf-8"))
            if isinstance(m, list): return raw, m
            last = "body was not a JSON list"
        except Exception as ex: last = f"{type(ex).__name__}: {ex}"
    raise SystemExit(f"fetch failed after 3 tries: {last}")
cids = sorted(pool); found = {}; prov = []
for i in range(0, len(cids), 50):
    batch = cids[i:i + 50]
    for closed in (False, True):
        raw, ms = fetch(batch, closed); prov.append({"batch": i // 50, "closed": closed, "sha256": hashlib.sha256(raw).hexdigest(), "n": len(ms)})
        for m in ms:
            c = m.get("conditionId")
            if c in found: raise SystemExit(f"{c} returned by BOTH live and closed passes; refusing to merge")
            found[c] = (closed, m)
        time.sleep(1)
def status(closed, m):
    if not closed: return "STILL_OPEN", None
    try: p = [float(v) for v in json.loads(m.get("outcomePrices") or "null")]
    except Exception: return "UNREADABLE_PRICES", None
    if len(p) != 2: return "NON_BINARY", None
    if p[0] >= 0.99 and p[1] <= 0.01: return "RESOLVED_YES", 1
    if p[1] >= 0.99 and p[0] <= 0.01: return "RESOLVED_NO", 0
    return "CLOSED_AMBIGUOUS", None
out = []
for c in cids:
    x = pool[c]; ev = (x.get("events") or [{}])[0].get("id")
    if c in found:
        closed, m = found[c]; st, y = status(closed, m)
        out.append({"conditionId": c, "slug": m.get("slug"), "question": m.get("question"), "status": st, "outcome": y, "outcomePrices_raw": m.get("outcomePrices"), "umaResolutionStatuses_raw": m.get("umaResolutionStatuses"), "endDate": m.get("endDate"), "updatedAt": m.get("updatedAt"), "first_seen": first[c], "event_id": ev, "volumeNum_snapshot": x.get("volumeNum")})
    else: out.append({"conditionId": c, "slug": x.get("slug"), "question": x.get("question"), "status": "NOT_FOUND", "outcome": None, "first_seen": first[c], "event_id": ev})
counts = {}
for o in out: counts[o["status"]] = counts.get(o["status"], 0) + 1
assert sum(counts.values()) == 412, counts
json.dump({"generated_at": dt.datetime.now(dt.timezone.utc).isoformat(), "pool_size": 412, "counts": counts, "provenance": prov, "markets": out}, open(OUT, "w"), indent=1)
print("counts", counts); print("resolved events", len({o["event_id"] for o in out if o["outcome"] is not None})); print("wrote", OUT)
