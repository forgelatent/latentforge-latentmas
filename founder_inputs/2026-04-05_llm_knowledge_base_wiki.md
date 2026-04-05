# LLM Knowledge Base as Compounding Wiki — April 5, 2026

Source: X/Twitter (author unknown)
Topic: Using LLMs to build personal knowledge bases as compounding markdown wikis

## Key insight
Raw data (papers, articles, repos) gets ingested into a raw/ directory. An LLM incrementally compiles it into a wiki of .md files with summaries, backlinks, and concept articles. The wiki grows and compounds — every query gets filed back in, making future queries better. At ~100 articles / 400K words, complex Q&A becomes possible without RAG.

## Stack they use
- Obsidian as the IDE/frontend to view raw data + wiki + visualizations
- Obsidian Web Clipper to convert web articles to .md
- LLM writes and maintains all wiki content — human rarely touches it directly
- Marp for slide output, matplotlib for images
- Simple vibe-coded search engine as a CLI tool for the LLM

## Why this matters for LatentForge
1. Our research sweep agent saves daily digests but they do not compound — each day is a new file, nothing connects to previous days. This person is describing a compounding wiki where every new paper gets linked to existing concepts.

2. BRAIN.md is our version of this but it is human-maintained. The wiki approach is LLM-maintained. Worth considering whether the research sweep agent should be building a compounding latent research wiki instead of daily flat files.

3. The Q&A against the wiki is essentially what we want the compression researcher agent to be doing — but right now it just reads arXiv, not a structured knowledge base of everything we have learned.

4. Key quote: "I think there is room here for an incredible new product instead of a hacky collection of scripts." This is LatentForge applied to knowledge management.

## Potential Week 4+ direction
Build a LatentForge research wiki using this approach:
- raw/ directory fed by research sweep agent daily
- LLM compiles into compounding wiki of latent research concepts
- Compression researcher agent queries the wiki instead of raw arXiv
- Wiki grows with every session — dataset moat for research, not just predictions

## Priority: Week 4+ — after Mac Mini latent experiments are running
