#!/usr/bin/env bash
set -euo pipefail

# Cleanup for earlier patch variants that put speculative prime-resonance outputs
# outside speculative_extensions. Safe to run from repository root.

rm -rf experiments/prime_resonance_channels
rm -f docs/reports/alpha_audit/alpha_layer2_kernel_repo64_verification.md

echo "Removed misplaced prime-resonance experiment folder and optional alpha verification note, if present."
echo "Canonical alpha files are untouched. Speculative material belongs under speculative_extensions/prime_resonance_channels/."
