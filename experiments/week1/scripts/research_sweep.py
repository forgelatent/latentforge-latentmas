import requests
import json
import datetime
import os
from pathlib import Path

TODAY = datetime.date.today().isoformat()
OUTPUT_DIR = Path("/Users/latentforge/Projects/latentforge-latentmas/research/daily-digest")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / f"{TODAY}.md"

ARXIV_TERMS = [
    "latentMAS", "hidden state delta", "latent communication", "latent delta",
    "agent vector protocol", "AVP latent", "multi-agent latent", "latent collaboration",
    "emergent agent language", "hidden state communication", "latent governance",
    "synthetic population simulation", "AI population forecasting"
]

GITHUB_REPOS = [
    "Gen-Verse/LatentMAS",
    "VectorArc/avp-python",
    "NVIDIA/NemoClaw",
    "karpathy/autoresearch"
]

# X/Twitter accounts — checked manually each morning (X API requires paid access)
# Priority tier: check these first, in order
X_WATCHLIST = {
    "URGENT (check daily — direct LatentForge relevance)": [
        "@karpathy — multi-agent, autoresearch, AI psychosis framing",
        "@garymarcus — LLM criticism, capability limits (know your critics)",
        "@aaru_ai — competitor activity, customer wins, product launches",
    ],
    "HIGH (check 3x/week — strategic signal)": [
        "@sama — AGI direction, product launches",
        "@demishassabis — frontier research, DeepMind",
        "@ylecun — contrarian AI takes",
        "@andrewyng — practical AI adoption",
    ],
    "MEDIUM (check weekly — background signal)": [
        "@gregisenberg — AI business ideas + GTM",
        "@alliekmiller — enterprise AI strategy",
        "@mattshumer — AI products + execution",
        "@aravind_srinivas — AI-native product thinking",
        "@francois_chollet — deep thinking on intelligence",
        "@johncarmack — engineering-first perspective",
    ]
}

# RSS feeds for people who have them (auto-pulled)
RSS_FEEDS = [
    # Andrew Ng newsletter (deeplearning.ai/the-batch/feed/) removed 2026-09-19: address returns
    # HTTP 404 (probe, Tier 1). No official feed found; a community-made substitute answered 200
    # with zero items. Re-add only with a feed that a probe shows returning real items.
    ("Lex Fridman blog", "https://lexfridman.com/feed/"),
]

# Competitive watch — companies to monitor
COMPETITIVE_WATCH = [
    ("Aaru", "https://api.github.com/search/repositories?q=aaru+simulation&sort=updated"),
]

FETCH_STATS = {"attempts": 0, "failures": 0}

# Failure contract (September 19 2026):
#   all fetches fail            -> no digest written, exit 1 (July 12)
#   every arXiv or GitHub fetch -> digest written WITH a FETCH FAILED section, then exit 1
#     fails (source dark)          so the wrapper retries; RSS is excluded from this trigger
#   some fetches fail           -> digest written, each failure named in banner and log, exit 0
FETCH_FAILURES = []   # (source, label, reason)
SOURCE_STATS = {}     # source -> [attempts, failures]

def note_attempt(source):
    FETCH_STATS["attempts"] += 1
    SOURCE_STATS.setdefault(source, [0, 0])[0] += 1

def note_failure(source, label, reason):
    FETCH_STATS["failures"] += 1
    SOURCE_STATS.setdefault(source, [0, 0])[1] += 1
    FETCH_FAILURES.append((source, label, reason))

def source_dark(source):
    attempts, failures = SOURCE_STATS.get(source, [0, 0])
    return attempts > 0 and failures == attempts

def arxiv_search():
    results = []
    seen = set()
    for term in ARXIV_TERMS:
        note_attempt("arxiv")
        url = f"https://export.arxiv.org/api/query?search_query=all:{term}&sortBy=submittedDate&sortOrder=descending&max_results=5"
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                import re
                titles = re.findall(r'<title>(.*?)</title>', resp.text)
                ids = re.findall(r'<id>http://arxiv.org/abs/(.*?)</id>', resp.text)
                for t, i in zip(titles[1:], ids):
                    key = i.strip()
                    if key not in seen:
                        seen.add(key)
                        results.append(f"arXiv [{term}]: {t.strip()} — https://arxiv.org/abs/{key}")
            if resp.status_code != 200:
                note_failure("arxiv", term, f"HTTP {resp.status_code}")
        except Exception as e:
            note_failure("arxiv", term, f"exception {type(e).__name__}")
    return results

def github_activity():
    results = []
    for repo in GITHUB_REPOS:
        note_attempt("github")
        url = f"https://api.github.com/repos/{repo}/commits?per_page=3"
        try:
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                for c in resp.json()[:2]:
                    msg = c['commit']['message'][:100].replace('\n', ' ')
                    results.append(f"GitHub {repo}: {msg}... — {c['html_url']}")
            if resp.status_code != 200:
                note_failure("github", repo, f"HTTP {resp.status_code}")
        except Exception as e:
            note_failure("github", repo, f"exception {type(e).__name__}")
    return results

def rss_check():
    results = []
    for name, url in RSS_FEEDS:
        note_attempt("rss")
        try:
            resp = requests.get(url, timeout=60)
            if resp.status_code == 200:
                import re
                titles = re.findall(r'<title>(.*?)</title>', resp.text)
                links = re.findall(r'<link>(.*?)</link>', resp.text)
                if len(titles) > 1:
                    results.append(f"{name}: {titles[1].strip()} — {links[1].strip() if len(links) > 1 else ''}")
                else:
                    note_failure("rss", name, "HTTP 200 but no items in feed")
            if resp.status_code != 200:
                note_failure("rss", name, f"HTTP {resp.status_code}")
        except Exception as e:
            note_failure("rss", name, f"exception {type(e).__name__}")
    return results

def build_x_watchlist():
    lines = []
    for tier, accounts in X_WATCHLIST.items():
        lines.append(f"\n### {tier}")
        for account in accounts:
            lines.append(f"- {account}")
    return lines

def main():
    arxiv_results = arxiv_search()
    github_results = github_activity()
    rss_results = rss_check()

    if FETCH_STATS["attempts"] > 0 and FETCH_STATS["failures"] == FETCH_STATS["attempts"]:
        print(f"FETCH FAILURE: all {FETCH_STATS['attempts']} fetch attempts failed (network down?) — refusing to write an 'all quiet' digest")
        raise SystemExit(1)
    x_lines = build_x_watchlist()

    content = f"# Research Nervous System Digest — {TODAY}\n\n"

    if FETCH_STATS["failures"] > 0:
        content += f"**WARNING: {FETCH_STATS['failures']} of {FETCH_STATS['attempts']} fetch attempts failed this run — sections below may be incomplete.**\n\n"
        for source, label, reason in FETCH_FAILURES:
            content += f"- FAILED {source}: {label} ({reason})\n"
        content += "\n"

    content += "## X/Twitter Watchlist (manual check)\n"
    content += "\n".join(x_lines)
    content += "\n\n"

    content += "## Competitive Watch\n"
    content += "- **Aaru** (aaru.com) — $1B valuation, text-based population simulation, Series A (Redpoint). Direct comparison point for LatentForge latent vs text benchmark.\n"
    content += "- **VectorArc/AVP** — adjacent protocol, KV-cache handoff, no governance layer. Monitor releases.\n"
    content += "- **CulturePulse, Simile** — Aaru competitors in social simulation space.\n\n"

    content += "## arXiv Recent Papers\n"
    if arxiv_results:
        content += "\n".join([f"- {r}" for r in arxiv_results])
    elif source_dark("arxiv"):
        content += f"**FETCH FAILED: all {SOURCE_STATS['arxiv'][0]} arXiv queries failed. This is NOT a quiet day. arXiv was not checked.**"
    else:
        content += "No new results found."
    content += "\n\n"

    content += "## GitHub Activity (key repos)\n"
    if github_results:
        content += "\n".join([f"- {r}" for r in github_results])
    elif source_dark("github"):
        content += f"**FETCH FAILED: all {SOURCE_STATS['github'][0]} GitHub repo checks failed. This is NOT a quiet day. GitHub was not checked.**"
    else:
        content += "No recent activity."
    content += "\n\n"

    if rss_results:
        content += "## RSS Feeds\n"
        content += "\n".join([f"- {r}" for r in rss_results])
        content += "\n\n"

    content += "## Relevance Guide\n"
    content += "- Score >0.8 on any latent communication paper → morning strategy session before Claude Code work\n"
    content += "- Aaru product launch or customer win → immediate dual-engine review\n"
    content += "- Karpathy posts anything about multi-agent communication → read before anything else\n"
    content += "- New competing product in latent agent space → emergency dual-engine session\n"

    with open(OUTPUT_FILE, "w") as f:
        f.write(content)

    print(f"Research digest saved to {OUTPUT_FILE}")
    print(f"  arXiv hits: {len(arxiv_results)} | GitHub updates: {len(github_results)} | RSS: {len(rss_results)} | fetch failures: {FETCH_STATS['failures']}/{FETCH_STATS['attempts']}")
    for source, label, reason in FETCH_FAILURES:
        print(f"  FAILED {source}: {label} ({reason})")

    dark = [s for s in ("arxiv", "github") if source_dark(s)]
    if dark:
        print(f"SOURCE DARK: every {' and '.join(dark)} fetch failed. Digest written with FETCH FAILED markers; exiting 1 so the wrapper retries.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
