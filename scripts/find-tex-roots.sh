\
#!/usr/bin/env bash
# SPDX-License-Identifier: CC-BY-4.0
# Copyright (c) 2025 David Jaroš
# This file is part of the Unified Biquaternion Theory project.
# Licensed under Creative Commons Attribution 4.0 International License.

set -euo pipefail

# Directories to exclude (space-separated, glob allowed)
EXCLUDES="${EXCLUDES:-consolidation_project/old}"

# Build find expression for excludes
exclude_args=()
for pat in $EXCLUDES; do
  exclude_args+=(-path "./$pat" -prune -o)
done

# Find all .tex files except excluded dirs, then keep only those with \documentclass
# Print as newline-separated list
find . \( "${exclude_args[@]}" \) -type f -name "*.tex" -print \
| while read -r f; do
    if grep -q "\\documentclass" "$f"; then
      # Normalize path without leading ./
      echo "${f#./}"
    fi
  done
