#!/bin/bash
#
# Court-Grade CMB Comb Pipeline - Shell Wrapper
# ==============================================
#
# This script is a simple wrapper around run_court_grade_cmb_comb.py
# for users who prefer a single shell command.
#
# Usage:
#   bash forensic_fingerprint/tools/run_court_grade_cmb_comb.sh
#   bash forensic_fingerprint/tools/run_court_grade_cmb_comb.sh --mc_samples 100000
#
# All arguments are passed through to the Python script.

set -euo pipefail

# Find script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Call Python script with all arguments
python3 "${SCRIPT_DIR}/run_court_grade_cmb_comb.py" "$@"
