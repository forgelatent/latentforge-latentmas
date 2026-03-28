import requests
import json
from datetime import datetime
import os

date_str = datetime.now().strftime("%Y-%m-%d")
output_dir = os.path.expanduser("~/Projects/data/polymarket")
os.makedirs(output_dir, exist_ok=True)
output_file = f"{output_dir}/{date_str}.json"

url = "https://gamma-api.polymarket.com/markets?active=true&limit=100"
response = requests.get(url)
markets = response.json()

with open(output_file, "w") as f:
    json.dump(markets, f, indent=2)

print(f"Saved {len(markets)} markets to {output_file}")
print(f"Timestamp: {datetime.now()}")
