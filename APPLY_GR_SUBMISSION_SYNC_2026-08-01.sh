#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DELETE_LIST="$ROOT/DELETE_PATHS_GR_SUBMISSION_SYNC_2026-08-01.txt"

while IFS= read -r rel; do
  [[ -z "$rel" ]] && continue
  rm -f -- "$ROOT/$rel"
done < "$DELETE_LIST"

printf 'GR submission/status synchronization deletions applied.\n'
