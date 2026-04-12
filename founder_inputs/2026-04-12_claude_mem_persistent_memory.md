# Claude Mem — Persistent Memory Plugin (Mac Mini Queue)

Repo: github.com/thedotmack/claude-mem
Source: @Suryanshti777 X thread, April 2026

What it does:
- Automatically captures session learnings and compresses them
- Injects relevant context into future Claude Code sessions
- Reduces context rot across long-running projects

Fit for LatentForge:
- RELEVANT — every Claude session starts fresh, relies entirely on BRAIN.md
- Claude Mem could complement BRAIN.md by capturing session-specific
  learnings that are too granular for BRAIN.md but still useful
- Most valuable for Mac Mini phase when coding sessions become more
  frequent and complex (echo_test.py refinements, compression pipeline,
  benchmark runs)

Decision: Park for Mac Mini Day 1 evaluation.
Test alongside andrej-karpathy-skills — they are complementary not redundant.
Karpathy = coding discipline rules
Claude Mem = session continuity / context persistence

Install: git clone into ~/.claude/skills/ or via Claude Code marketplace
Skip: Superpowers (redundant with Karpathy), LightRAG (overkill for
current repo size), UI UX Pro Max and n8n-MCP (irrelevant to LatentForge)
