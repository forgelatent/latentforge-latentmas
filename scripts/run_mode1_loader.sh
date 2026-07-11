#!/bin/bash
# Mode 1 market-state loader wrapper — 2026-07-11.
# NO API key: the loader hits Polymarket's public Gamma endpoint only.
# Deliberately NOT run_with_key.sh (per LOADER_HANDOVER_2026-06-28 step 5).
#
# Exit-code contract (loader's Q5.2 tiers — differs from other pulls):
#   0 = ALL_LIVE          -> clean success, no retry
#   1 = RETIRED_PRESENT   -> clean success WITH retirements, no retry.
#       Exit 1 is NOT a failure for this loader. Retrying on 1 would
#       re-run a successful job 3x per night once any market retires.
#   2 = ERROR             -> loud fail (sidecar written), retry.
# Wrapper exits 0 on either success tier so launchd sees a clean run;
# the RETIRED_PRESENT detail lives in the log line and the output file.

LOADER="/Users/latentforge/Projects/latentforge-latentmas/experiments/benchmark/04_market_state_loader.py"
LOG="/Users/latentforge/Projects/latentforge-latentmas/experiments/benchmark/mode1/cron.log"
MAX_RETRIES=3
RETRY_DELAY=300  # 5 minutes

attempt=1
while [[ $attempt -le $MAX_RETRIES ]]; do
  echo "$(date): Attempt $attempt of $MAX_RETRIES — running $LOADER" >> "$LOG"
  /usr/bin/python3 "$LOADER" --run >> "$LOG" 2>&1
  EXIT_CODE=$?

  if [[ $EXIT_CODE -eq 0 ]]; then
    echo "$(date): SUCCESS on attempt $attempt (ALL_LIVE, exit 0)" >> "$LOG"
    exit 0
  elif [[ $EXIT_CODE -eq 1 ]]; then
    echo "$(date): SUCCESS on attempt $attempt (RETIRED_PRESENT, exit 1 — retirements are data, not failure)" >> "$LOG"
    exit 0
  else
    echo "$(date): FAILED on attempt $attempt (exit code $EXIT_CODE)" >> "$LOG"
    if [[ $attempt -lt $MAX_RETRIES ]]; then
      echo "$(date): Retrying in ${RETRY_DELAY}s..." >> "$LOG"
      sleep $RETRY_DELAY
    fi
  fi
  attempt=$((attempt + 1))
done

echo "$(date): PERMANENT FAILURE after $MAX_RETRIES attempts — manual rerun required" >> "$LOG"
exit 1
