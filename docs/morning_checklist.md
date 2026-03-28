# LatentForge Daily Morning Checklist
Run every morning before any engineering work. Total time: ~10 minutes.

---

## Step 1 — Check Polymarket data (1 minute)
```bash
ls -la ~/Projects/data/polymarket/ | tail -5
```

Should show a file dated today. If missing, run manually:
```bash
python3 ~/Projects/latentforge-latentmas/experiments/week1/scripts/polymarket_pull.py
```

---

## Step 2 — Check Polymarket cron log (1 minute)
```bash
tail -10 ~/Projects/data/polymarket/cron.log
```

Should show "Saved 100 markets" with today's timestamp. If errors, flag it.

---

## Step 3 — Check Research Nervous System digest (5 minutes)
```bash
ls ~/Projects/latentforge-latentmas/research/daily-digest/
```

Open the latest file:
```bash
cat ~/Projects/latentforge-latentmas/research/daily-digest/$(ls ~/Projects/latentforge-latentmas/research/daily-digest/ | tail -1)
```

If any relevance score >0.8 — stop and do a strategy session before any engineering work.

---

## Step 4 — Check research sweep cron log (1 minute)
```bash
tail -10 ~/Projects/latentforge-latentmas/research/daily-digest/cron.log
```

Should show a successful run at 7:30am. If errors, run manually:
```bash
python3 ~/Projects/latentforge-latentmas/experiments/week1/scripts/research_sweep.py
```

---

## Step 5 — Open Claude session with current BRAIN.md (3 minutes)
```bash
cat ~/Projects/latentforge-latentmas/BRAIN.md
```

Copy the output. Open a new Claude session. Paste BRAIN.md at the top using the session template from Section 8. Ask your one question for the day.

---

Last updated: March 28, 2026
