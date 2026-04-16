# Paper Log — April 16, 2026

Source: arXiv:2604.13349v1
Title: When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration
Authors: Yiping Li, Zhiyu An, Wan Du — UC Merced

Key finding: KV-cache compression for LatentMAS relay achieves 79.8-89.4% reduction.
OBF (Orthogonal Backfill): injects orthogonal residual from discarded KV states back into retained states.

LatentForge relevance:
- NOT competitive — different mechanism (KV relay vs activation steering)
- OBF is mathematically adjacent to our contrastive injection
- Validates LatentMAS ecosystem is expanding
- Differentiator: we test on live prediction markets, they test on synthetic benchmarks

Thesis impact: strengthen — ecosystem validation
Motor-car linkage: Compression / Architecture
Action: Cite in benchmark report. Add OBF as Arm 5 in compression tournament.
