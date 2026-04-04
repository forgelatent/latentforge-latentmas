#!/bin/bash
SCRIPT="$1"
LOG="$2"
API_KEY=$(security find-generic-password -a "latentforge" -s "latentforge-anthropic" -w 2>/dev/null)
if [[ -z "$API_KEY" ]]; then
  echo "$(date): ERROR — key not found in Keychain" >> "$LOG"
  exit 1
fi
export ANTHROPIC_API_KEY="$API_KEY"
/usr/bin/python3 "$SCRIPT" >> "$LOG" 2>&1
