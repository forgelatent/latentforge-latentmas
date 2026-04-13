# Mac Mini M4 Pro — Day 1 Latent Test Sequence
## April 16, 2026
## Execute in exact order. No skipping steps. No improvising.

---

## PHASE 1 — System Setup (30 min)

```bash
# 1. Check macOS version
sw_vers

# 2. Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. Install Python 3.12
brew install python@3.12
python3.12 --version  # confirm 3.12.x

# 4. Install git
brew install git

# 5. Install Docker Desktop
# Download from docker.com/products/docker-desktop — Apple Silicon version
# Launch it. Wait for whale icon in menu bar.
docker run hello-world  # confirm running
```

---

## PHASE 2 — Create latentforge Account + Clone Repo (15 min)

```bash
# 6. Create latentforge user account
# System Settings > Users & Groups > Add User
# Username: latentforge
# Log into that account before continuing

# 7. Clone repo
cd ~
mkdir -p Projects
cd Projects
git clone https://github.com/forgelatent/latentforge-latentmas.git
cd latentforge-latentmas

# 8. Confirm BRAIN.md is current
head -n 5 BRAIN.md
# Should show: Version: 2.0 — April 11 update (final)
```

---

## PHASE 3 — API Keys + Environment (15 min)

```bash
# 9. Create .latentforge directory
mkdir -p ~/.latentforge

# 10. Store Anthropic API key (use getpass — never paste directly)
python3.12 -c "
import getpass, os
k = getpass.getpass('Paste Anthropic key then Enter: ')
open(os.path.expanduser('~/.latentforge/.env'),'w').write(f'export ANTHROPIC_API_KEY="{k}"
')
print('Saved. Length:', len(k))
"
# Should print: Saved. Length: 108

# 11. Add to zprofile
echo 'source ~/.latentforge/.env' >> ~/.zprofile
source ~/.zprofile

# 12. Store OpenAI key (for last30days-skill)
python3.12 -c "
import getpass, os
k = getpass.getpass('Paste OpenAI key then Enter: ')
open(os.path.expanduser('~/.latentforge/.openai.env'),'w').write(f'export OPENAI_API_KEY="{k}"
')
print('Saved. Length:', len(k))
"

# 13. Verify Anthropic key length
source ~/.latentforge/.env
echo ${#ANTHROPIC_API_KEY}  # should print 108
```

---

## PHASE 4 — Install Dependencies (20 min)

```bash
# 14. Install Python packages
pip3.12 install anthropic transformers torch sentence-transformers numpy scikit-learn --break-system-packages

# 15. Confirm torch MPS available
python3.12 -c "import torch; print('MPS:', torch.backends.mps.is_available())"
# Should print: MPS: True
```

---

## PHASE 5 — NemoClaw + OpenClaw (20 min)

```bash
# 16. Pull NemoClaw
docker pull nvcr.io/nvidia/nemo/nemoclaw:latest

# 17. Run OpenClaw
docker run --rm -it nvcr.io/nvidia/nemo/nemoclaw:latest openclaw

# 18. Write hello.txt — confirm OpenClaw alive
ls -la ~/Projects/latentforge-latentmas/hello.txt
```

---

## PHASE 6 — Pull Phi-3 Mini (30 min download)

```bash
# 19. Pull model
python3.12 -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
model_id = 'microsoft/Phi-3-mini-4k-instruct'
print('Downloading tokenizer...')
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
print('Downloading model...')
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map='auto', trust_remote_code=True)
print('Model loaded. Hidden size:', model.config.hidden_size)
"
# Should print hidden_size: 3072
```

---

## PHASE 7 — SILICON DELTA VERIFICATION (critical — new step)
## Confirm Mac Mini hidden state dimensions match RunPod A40 reference.
## M4 neural engine may handle hidden states differently than A40 GPU.

```bash
# 20. Extract one hidden state and verify dimensions
python3.12 -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, json

model_id = 'microsoft/Phi-3-mini-4k-instruct'
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map='auto', trust_remote_code=True)

inputs = tok('Will the Fed cut rates in 2026?', return_tensors='pt').to('mps')
with torch.no_grad():
    out = model(**inputs, output_hidden_states=True, return_dict=True)

last = out.hidden_states[-1][0, -1, :].float().cpu()
print(f'Hidden state dim: {last.shape[0]}')
print(f'Dtype: {last.dtype}')
print(f'Norm: {last.norm().item():.4f}')
print(f'Mean: {last.mean().item():.6f}')

# Save reference vector
import numpy as np
np.save('experiments/week4/mac_mini_reference_hidden.npy', last.numpy())
print('Reference vector saved.')
"

# VERIFY: dim should be 3072, dtype float32
# If dim != 3072 — STOP. Hardware mismatch. Investigate before proceeding.
```

---

## PHASE 8 — Run Manifest (5 min)

```bash
# 21. Create run manifest
mkdir -p experiments/week4
python3.12 -c "
import datetime
manifest = open('experiments/week4/run_manifest.md','w')
manifest.write('# LatentForge Mac Mini A/B Run Manifest
')
manifest.write(f'Date: {datetime.date.today()}
')
manifest.write('Model: microsoft/Phi-3-mini-4k-instruct
')
manifest.write('Quantization: float16 (MPS, no 4-bit on Apple Silicon)
')
manifest.write('Temperature: 0.0
')
manifest.write('Random seed: 42
')
manifest.write('Sparsity method: Top-k, k=128
')
manifest.write('Device: MPS (Apple M4 Pro)
')
manifest.write('[record git log --oneline -1 as sparsity commit hash]
')
manifest.close()
print('Manifest created.')
"

# 22. Record commit hash
git log --oneline -1
# Paste this into run_manifest.md
```

---

## PHASE 9 — Latent Echo Test Pre-Gate (MUST PASS before benchmark)

```bash
# 23. Create output dirs
mkdir -p experiments/week4/scaling
mkdir -p experiments/week4/density
mkdir -p experiments/week4/shadow_overhead
mkdir -p experiments/week4/ineffable
mkdir -p experiments/week4/eof_compression

# 24. Run Echo Test
python3.12 experiments/week4/echo_test.py --mode pre-gate

# PASS threshold: >=0.95 similarity on 3 of 3 markets
# If FAIL: STOP. Debug W_a alignment. Do not proceed to benchmark.
# Log result is automatic — check experiments/week4/echo_log.md
```

---

## PHASE 10 — Scaling Test (before full benchmark)

```bash
# 25. Run scaling test at 2, 4, 8 agents (text and latent)
# This is Motor-Car Test 2 — the primary car signal
# Script TBD — build on Mac Mini based on echo_test.py architecture
# Log to: experiments/week4/scaling/
```

---

## PHASE 11 — Full Four-Arm Benchmark

```bash
# 26. Begin four-arm benchmark on 11 Shadow Match markets
# With continuous Echo fidelity logging active
# Arm 1: Text Single-Agent
# Arm 2: Text Swarm (3 agents)
# Arm 3: Latent Single-Agent
# Arm 4: Latent Swarm (3 agents)
# Log everything to experiments/week4/
```

---

## PHASE 12 — Compression Tournament (optional Day 1-2)

After benchmark passes, run compression bake-off per Section 4.6 of spec:
1. Top-k sparsity k=128 (baseline)
2. EOF adaptive (95% variance)
3. EOF + sparse residual hybrid
4. Product Quantization
5. Predictive Coding Residuals (EMA-delta, Suggestion 1 April 13)
   Transmit EMA-delta residual instead of raw delta. ~50 lines NumPy.
   Directly supports Information Density motor-car test.

---

## PHASE 13 — Launchd Migration

```bash
# 27. Copy all 8 plist files
cp ~/Projects/latentforge-latentmas/scripts/launchd/*.plist ~/Library/LaunchAgents/

# 28. Load all jobs
for f in ~/Library/LaunchAgents/com.latentforge.*.plist; do launchctl load "$f"; done

# 29. Store API key in Keychain for launchd
security add-generic-password -a "latentforge" -s "latentforge-anthropic" -w "$(cat ~/.latentforge/.env | grep -o 'sk-ant[^"]*')" -U

# 30. Verify Keychain
security find-generic-password -a "latentforge" -s "latentforge-anthropic" -w | wc -c
# Should print: 109

# 31. Unload MacBook jobs
# On MacBook:
for f in ~/Library/LaunchAgents/com.latentforge.*.plist; do launchctl unload "$f"; done
```

---

## PHASE 14 — Optional Tools (if time allows)

```bash
# last30days-skill
cd ~/.claude/skills/last30days
source ~/.latentforge/.openai.env
python3.12 scripts/last30days.py "US AI regulation 2026 prediction market" --quick --emit=compact

# andrej-karpathy-skills
# /plugin install andrej-karpathy-skills@karpathy-skills

# Claude Mem
# git clone github.com/thedotmack/claude-mem ~/.claude/skills/claude-mem
```

---

## GO / NO-GO CHECKLIST

Before starting any benchmark:
- [ ] hello.txt written by OpenClaw
- [ ] Phi-3 Mini loaded — hidden size 3072 confirmed
- [ ] Silicon delta: dim=3072, dtype=float32, norm reasonable
- [ ] run_manifest.md populated
- [ ] Echo Test PASSED (>=0.95 on 3/3 markets)
- [ ] All 8 launchd jobs registered on Mac Mini
- [ ] MacBook launchd jobs unloaded
- [ ] API key in Keychain — length 109 confirmed

All 8 boxes checked -> begin scaling test -> then full benchmark.

---

Experiment spec: docs/mac_mini_experiment_spec_v2.md
Pre-registered: April 11, 2026. No amendments after first run.
