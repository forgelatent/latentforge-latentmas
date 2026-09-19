# Competitive scan — who else is working on latent agent communication

**Date:** September 19, 2026 (fourth session). **Requested by:** Founder ("a competitive scan to see who else is working in our area").
**Tier:** 3 — agent synthesis. Six live web searches by the Systems Engine in one sitting. **Not canon. Not evidence. A map to check.**
**Limit, stated per the enumeration clause:** six searches is a window, not the field. Anything not found here is not thereby absent. Commercial and stealth work is especially likely to be missed; every source below is a paper, a repo or a press article.

## The headline

The area now has a name ("latent communication in LLM-based multi-agent systems") and a survey. A June 2026 survey organises eighteen methods from 2024-2026 by what is sent (embeddings, hidden states, KV-caches, other), how sender and receiver are aligned, and how the message is fused in.
Source: https://arxiv.org/abs/2606.05711

## 1. Building the same kind of engine

- **LatentMAS** (our base). Accepted at ICML 2026 as a spotlight. Its repo now lists downstream projects, AVP among them. https://github.com/Gen-Verse/LatentMAS
- **Interlat.** Agents pass last hidden states directly, with a learned compression step. ACL 2026 main conference. https://aclanthology.org/2026.acl-long.1248/
- **KVComm** (ICLR 2026) and **Cache-to-Cache.** Share attention state (KV-cache) between models. Listed in the survey above.
- **State delta trajectory.** Sends the change in hidden state at each layer, not the state itself. **Closest published idea to "deltas against a shared seed". Read first.** arXiv 2506.19209, as cited in the survey.
- **Vision Wormhole** (already watched) and **RecursiveMAS** (arXiv 2604.25917): heterogeneous and recursive variants.

## 2. Packaging it as a product or protocol

- **AVP / VectorArc** (already watched). A binary protocol for passing KV-cache and hidden states between agents; built on LatentMAS; installable package; falls back to JSON when models are incompatible. Publishes token-savings and speed numbers across seven benchmarks. This is the "cheaper coordination" half of our claim, with numbers already public.
  https://github.com/VectorArc/avp-spec  and  https://pypi.org/project/avp/

## 3. Checking whether it really works  (most relevant to our Phase 11 lesson)

- **"Do Latent Channels Actually Communicate? A Causal Audit"** (July 29, 2026). Swaps in a message from a different example at the point where it enters the receiver. On one benchmark more than half of the measured gain survived the swap, so end-task accuracy alone does not show the receiver used the message's content. This is our Phase 11 finding (the channel was not influencing generation) turned into a published evaluation method. https://arxiv.org/abs/2607.26773
- **"When Does Latent Communication Pay?"** (August 2026). A second causal audit, of relayed KV-caches. https://arxiv.org/abs/2608.04893

## 4. Oversight and safety of latent channels  (Shadow Self territory)

- **"When Latent Agents Lie"** — KV-cache integrity; hidden manipulation behind plausible visible text. https://arxiv.org/abs/2606.28958
- **"Out of Sight, Not Out of Mind"** — attacks on latent-based multi-agent systems through hidden-state or KV-cache steering. https://arxiv.org/abs/2605.28214
- **Verifiable Latent Alignments ("Beyond the Transcript").** Records each private latent handoff beside the public action it led to, then runs a three-layer monitor (anomaly detection, counterfactual influence, sparse-autoencoder interpretation). **Nearest thing found to Shadow Self.** arXiv 2608.19161.
- The survey reports the field has settled on a hybrid: natural language where human oversight is needed, latent for intermediate agent-to-agent steps.

## 5. Aaru  (named in the digest's static note)

Still accurate as of the sources found: Series A led by Redpoint, a $1B headline valuation with a lower blended figure (reported December 2025). Aaru simulates human populations with text-based agents. **Different field: a benchmark comparison point, not a latent-communication competitor.**
https://finance.yahoo.com/news/sources-ai-synthetic-research-startup-233859223.html

## What this suggests — Systems Engine reading, to be challenged

- **Cheaper coordination:** crowded, and others have published numbers.
- **Useful divergence (the motor-car question):** nobody found claiming it. Six searches; see the limit above.
- **Governance:** no longer an empty lane. Audit tooling for latent channels is now being published.
- **Our own discipline is being published as method.** The causal-audit papers formalise the check that caught Phase 10/11.

## For the nightly watch, when it is designed

A watch needs a definition of "relevant" before it needs code. This scan supplies candidates for that definition: the specific papers above and what cites them; the LatentMAS and VectorArc repos; the survey's successive versions. That is a matching contract in embryo. "Search GitHub for the word Aaru" is not.
