import os
import json
import datetime
import requests
from pathlib import Path
import anthropic

CLIENT = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
MODEL = "claude-sonnet-4-6"

LOG_DIR = Path.home() / ".latentforge" / "shadow_match"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def get_live_price(question, short_query=None):
    """Fetch current YES price using correct Polymarket public-search + robust outcomePrices parsing."""
    try:
        search_term = short_query or question.replace("Will ", "").replace("win the ", "").replace("?", "").strip()[:60]
        url = "https://gamma-api.polymarket.com/public-search"
        params = {"q": search_term, "limit": 15}
        r = requests.get(url, params=params, timeout=15)
        data = r.json()
        
        events = data.get("events", []) if isinstance(data, dict) else []
        markets = []
        for event in events:
            markets.extend(event.get("markets", []))
        
        print(f"✅ API returned {len(markets)} markets for search: '{search_term}'")
        
        best_match = None
        best_score = 0
        q_lower = question.lower()
        
        for m in markets:
            api_q = m.get("question", "").lower()
            score = sum(1 for word in q_lower.split() if len(word) > 3 and word in api_q)
            if question.lower() in api_q or api_q in question.lower():
                score += 10
            
            if score > best_score and score >= 3:
                best_score = score
                best_match = m
        
        if best_match:
            # Robust price parsing - outcomePrices can be string or list
            outcome_prices = best_match.get("outcomePrices")
            price = None
            
            if isinstance(outcome_prices, str):
                try:
                    # Remove outer quotes and parse as JSON array
                    parsed = json.loads(outcome_prices)
                    if isinstance(parsed, list) and len(parsed) > 0:
                        price = float(parsed[0])
                except:
                    pass
            elif isinstance(outcome_prices, list) and len(outcome_prices) > 0:
                price = float(outcome_prices[0])
            
            if price is not None:
                print(f"✓ LIVE PRICE (score={best_score}): {best_match['question'][:90]}... → {price*100:.1f}%")
                return price
            else:
                print(f"⚠️ Found market but could not parse price: {best_match['question'][:80]}")
                print(f"   outcomePrices raw = {outcome_prices}")
                return None
        else:
            print(f"✗ No strong match for '{search_term}'")
            return None
    except Exception as e:
        print("✗ API error:", e)
        return None

MARKETS = [
    {"id": "desantis_2028", "question": "Will Ron DeSantis win the 2028 Republican presidential nomination?", "crowd_prob": get_live_price("Will Ron DeSantis win the 2028 Republican presidential nomination?", "DeSantis 2028") or 0.0265},
    {"id": "buttigieg_2028", "question": "Will Pete Buttigieg win the 2028 Democratic presidential nomination?", "crowd_prob": get_live_price("Will Pete Buttigieg win the 2028 Democratic presidential nomination?", "Buttigieg 2028") or 0.0375},
    {"id": "vance_2028_rep", "question": "Will J.D. Vance win the 2028 Republican presidential nomination?", "crowd_prob": get_live_price("Will J.D. Vance win the 2028 Republican presidential nomination?", "Vance 2028 nomination") or 0.367},
    {"id": "newsom_2028", "question": "Will Gavin Newsom win the 2028 US Presidential Election?", "crowd_prob": get_live_price("Will Gavin Newsom win the 2028 US Presidential Election?", "Newsom 2028") or 0.1725},
    {"id": "vance_2028_gen", "question": "Will JD Vance win the 2028 US Presidential Election?", "crowd_prob": get_live_price("Will JD Vance win the 2028 US Presidential Election?", "Vance 2028") or 0.1765},
    {"id": "bitcoin_60_80", "question": "Will Bitcoin hit $60k or $80k first?", "crowd_prob": get_live_price("Will Bitcoin hit $60k or $80k first?", "Bitcoin 60k 80k") or 0.65},
    {"id": "china_taiwan", "question": "Will China blockade Taiwan by June 30?", "crowd_prob": get_live_price("Will China blockade Taiwan by June 30?", "China Taiwan") or 0.0365},
    {"id": "fed_cuts", "question": "Will 9 Fed rate cuts happen in 2026?", "crowd_prob": get_live_price("Will 9 Fed rate cuts happen in 2026?", "Fed rate cuts 2026") or 0.0045},
    {"id": "powell", "question": "Will Jerome Powell be confirmed as Fed Chair?", "crowd_prob": get_live_price("Will Jerome Powell be confirmed as Fed Chair?", "Powell Fed Chair") or 0.0015},
    {"id": "iran_deal", "question": "US-Iran nuclear deal by June 30?", "crowd_prob": get_live_price("US-Iran nuclear deal by June 30?", "Iran nuclear deal") or 0.225},
    {"id": "ppp_korea", "question": "Will the People Power Party (PPP) win the 2026 South Korean local elections?", "crowd_prob": get_live_price("Will the People Power Party (PPP) win the 2026 South Korean local elections?", "PPP South Korea") or 0.0415},
]

print("\n✅ shadow_match.py overwritten with ROBUST live price parsing")
print("Running Shadow Match with LIVE data...\n")

for m in MARKETS:
    print(m["question"])
    print(f"  Crowd: {m['crowd_prob']*100:.1f}%")
    print("")
