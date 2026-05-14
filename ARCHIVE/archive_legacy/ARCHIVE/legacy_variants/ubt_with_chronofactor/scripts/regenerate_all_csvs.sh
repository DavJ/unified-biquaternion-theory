#!/bin/bash
# regenerate_all_csvs.sh
# Regenerate all CSV files with computed physics constants
# SPDX-License-Identifier: MIT

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

cd "$REPO_ROOT"

echo "========================================="
echo "Regenerating All CSV Files"
echo "========================================="
echo ""

# 1. Generate alpha grid (main calculation)
echo "[1/4] Generating alpha two-loop grid..."
python -m alpha_core_repro.run_grid
echo "  ✓ Generated: alpha_core_repro/out/alpha_two_loop_grid.csv"
echo ""

# 2. Generate alternative alpha CSV for different mu values
echo "[2/4] Generating alpha grid for various mu scales..."
python -m alpha_core_repro.export_alpha_csv
echo "  ✓ Generated: data/alpha_two_loop_grid.csv"
echo ""

# 3. Generate lepton masses
echo "[3/4] Generating lepton mass CSV..."
python -m ubt_masses.export_leptons_csv
echo "  ✓ Generated: data/leptons.csv"
echo ""

# 4. Verify precision
echo "[4/4] Verifying CSV precision..."
python << 'PYTHON_EOF'
import csv
from pathlib import Path

def check_precision(csv_path, name):
    """Check decimal precision of CSV values."""
    if not Path(csv_path).exists():
        print(f"  ❌ {name}: File not found")
        return
    
    with open(csv_path, 'r') as f:
        content = f.read()
        # Find all decimal numbers
        import re
        decimals = re.findall(r'\d+\.(\d+)', content)
        if decimals:
            max_precision = max(len(d) for d in decimals)
            status = "✅" if max_precision >= 6 else "⚠️"
            print(f"  {status} {name}: {max_precision} decimal places")
        else:
            print(f"  ⚠️ {name}: No decimal values found")

print("\nPrecision Check:")
check_precision("alpha_core_repro/out/alpha_two_loop_grid.csv", "Alpha grid (prime sectors)")
check_precision("data/alpha_two_loop_grid.csv", "Alpha grid (mu scales)")
check_precision("data/leptons.csv", "Lepton masses")
PYTHON_EOF

echo ""
echo "========================================="
echo "Summary"
echo "========================================="
echo "All CSV files regenerated successfully!"
echo ""
echo "Generated files:"
echo "  1. alpha_core_repro/out/alpha_two_loop_grid.csv"
echo "  2. data/alpha_two_loop_grid.csv"
echo "  3. data/leptons.csv"
echo ""
echo "Next steps:"
echo "  - Run tests: python tests/test_docs_use_generated_csv.py"
echo "  - Verify: python tests/test_no_hardcoded_constants.py"
echo "  - Commit changes if values updated"
echo ""
