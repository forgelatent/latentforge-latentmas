"""
Kalshi RSA Auth Client v1.1
Fixed: PSS padding (not PKCS1v15), correct base URL
"""

import urllib.request
import urllib.parse
import json
import time
import base64
from pathlib import Path
from datetime import datetime

API_KEY_ID = "2d1376e8-d62f-4524-9a36-507cd005d6a4"
PRIVATE_KEY_PATH = Path("/Users/latentforge/Projects/latentforge-latentmas/config/kalshi/kalshi_private.pem")
BASE_URL = "https://trading-api.kalshi.com"
OUTPUT_DIR = Path("/Users/latentforge/Projects/latentforge-latentmas/data/kalshi/policy")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_private_key():
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend
    with open(PRIVATE_KEY_PATH, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())


def sign_request(method, path):
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding

    ts = str(int(time.time() * 1000))
    # Strip query params from path before signing
    path_no_query = path.split("?")[0]
    message = ts + method.upper() + path_no_query

    private_key = load_private_key()
    signature = private_key.sign(
        message.encode("utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.DIGEST_LENGTH
        ),
        hashes.SHA256()
    )
    sig_b64 = base64.b64encode(signature).decode("utf-8")
    return ts, sig_b64


def kalshi_get(path, params=None):
    full_path = path
    if params:
        full_path = path + "?" + urllib.parse.urlencode(params)

    ts, sig = sign_request("GET", full_path)

    req = urllib.request.Request(
        BASE_URL + full_path,
        headers={
            "Content-Type": "application/json",
            "KALSHI-ACCESS-KEY": API_KEY_ID,
            "KALSHI-ACCESS-TIMESTAMP": ts,
            "KALSHI-ACCESS-SIGNATURE": sig,
        }
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def fetch_policy_markets():
    categories = ["Economics", "Politics", "Financials", "Climate"]
    all_markets = []

    for category in categories:
        print("Fetching: " + category)
        try:
            data = kalshi_get("/trade-api/v2/markets", {
                "limit": 100,
                "category": category,
                "status": "open"
            })
            markets = data.get("markets", [])
            all_markets.extend(markets)
            print("  Got " + str(len(markets)) + " markets")
        except Exception as e:
            print("  Error: " + str(e))

    return all_markets


def save_markets(markets):
    date_str = datetime.now().strftime("%Y-%m-%d")
    out = OUTPUT_DIR / ("policy_markets_" + date_str + ".json")
    with open(out, "w") as f:
        json.dump(markets, f, indent=2)
    print("Saved " + str(len(markets)) + " markets to " + str(out))


def print_sample(markets, n=5):
    print("")
    print("=== SAMPLE POLICY MARKETS ===")
    for m in markets[:n]:
        title = m.get("title", m.get("question", "no title"))
        yes_bid = m.get("yes_bid", "?")
        print("  " + str(title)[:80])
        print("    yes_bid: " + str(yes_bid))


if __name__ == "__main__":
    print("Kalshi RSA Auth Client v1.1")
    print("Key ID: " + API_KEY_ID)
    print("Base URL: " + BASE_URL)
    print("")

    markets = fetch_policy_markets()

    if markets:
        print_sample(markets)
        save_markets(markets)
    else:
        print("No markets returned.")
        print("")
        print("If still 401: check that public key is uploaded at kalshi.com -> Settings -> API Keys")
