#!/bin/bash
SCRIPT="$1"
LOG="$2"
MAX_RETRIES=3
RETRY_DELAY=300  # 5 minutes

API_KEY=$(security find-generic-password -a "latentforge" -s "latentforge-anthropic" -w 2>/dev/null)
if [[ -z "$API_KEY" ]]; then
  echo "$(date): ERROR — key not found in Keychain" >> "$LOG"
  exit 1
fi
export ANTHROPIC_API_KEY="$API_KEY"

attempt=1
while [[ $attempt -le $MAX_RETRIES ]]; do
  echo "$(date): Attempt $attempt of $MAX_RETRIES — running $SCRIPT" >> "$LOG"
  /usr/bin/python3 "$SCRIPT" >> "$LOG" 2>&1
  EXIT_CODE=$?

  if [[ $EXIT_CODE -eq 0 ]]; then
    echo "$(date): SUCCESS on attempt $attempt" >> "$LOG"
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
