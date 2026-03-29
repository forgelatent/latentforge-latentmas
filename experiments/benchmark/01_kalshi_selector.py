import json, datetime
from pathlib import Path

D = datetime.datetime.now().strftime("%Y-%m-%d")
S = Path("experiments/benchmark/policy_markets_seed.json")
O = Path("experiments/benchmark") / ("markets_" + D + ".md")

markets = json.load(open(S))
out = open(O, "w")
out.write("Benchmark Markets " + D + "\n\n")
for i, m in enumerate(markets, 1):
    out.write(str(i) + ". " + m.get("question", "") + "\n")
    out.write("Crowd: " + str(m.get("current_price", "")) + "\n")
    out.write("End: " + str(m.get("end_date", "")) + "\n\n")
out.close()
print("Saved to " + str(O))
