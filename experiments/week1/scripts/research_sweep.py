import requests
import json
import datetime
import os
from pathlib import Path

TODAY = datetime.date.today().isoformat()
OUTPUT_DIR = Path("research/daily-digest")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / f"{TODAY}.md"

# TIGHTER, MORE FOCUSED TERMS
ARXIV_TERMS = [
    "latentMAS", "hidden state delta", "latent communication", "latent delta", 
    "agent vector protocol", "AVP latent", "multi-agent latent", "latent collaboration",
    "emergent agent language", "hidden state communication", "latent governance"
]

GITHUB_REPOS = [
    "Gen-Verse/LatentMAS", 
    "VectorArc/avp-python", 
    "NVIDIA/NemoClaw", 
    "karpathy/autoresearch"
]

def arxiv_search():
    results = []
    for term in ARXIV_TERMS:
        url = f"https://export.arxiv.org/api/query?search_query=all:{term}&sortBy=submittedDate&sortOrder=descending&max_results=8"
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                import re
                titles = re.findall(r'<title>(.*?)</title>', resp.text)
                ids = re.findall(r'<id>http://arxiv.org/abs/(.*?)</id>', resp.text)
                for t, i in zip(titles[1:], ids):
                    results.append(f"arXiv: {t.strip()} — https://arxiv.org/abs/{i}")
        except:
            pass
    return results

def github_activity():
    results = []
    for repo in GITHUB_REPOS:
        url = f"https://api.github.com/repos/{repo}/commits?per_page=3"
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                for c in resp.json()[:2]:
                    msg = c['commit']['message'][:100].replace('\n', ' ')
                    results.append(f"GitHub {repo}: {msg}... — {c['html_url']}")
        except:
            pass
    return results

def main():
    arxiv_results = arxiv_search()
    github_results = github_activity()

    content = f"# Research Nervous System Digest — {TODAY}\n\n"
    content += "## arXiv Recent Papers\n"
    content += "\n".join([f"- {r}" for r in arxiv_results]) or "No new results found.\n"
    content += "\n\n## GitHub Activity (key repos)\n"
    content += "\n".join([f"- {r}" for r in github_results]) or "No recent activity.\n"
    content += "\n\nNote: Focused monitoring for latent deltas, governance, divergence, AVP, and related developments.\n"

    with open(OUTPUT_FILE, "w") as f:
        f.write(content)

    print(f"✅ Research digest saved → {OUTPUT_FILE}")
    print(f"   arXiv hits: {len(arxiv_results)} | GitHub updates: {len(github_results)}")

if __name__ == "__main__":
    main()
