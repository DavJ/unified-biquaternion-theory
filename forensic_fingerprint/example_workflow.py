#!/usr/bin/env python3
"""
Example: Complete CMB Comb Test Workflow
=========================================

This script demonstrates the complete workflow for running the CMB comb fingerprint
test on real data using the one-command runner.

This example uses synthetic data for demonstration. For real analysis, replace
with actual Planck PR3 and WMAP data files.

Author: UBT Research Team
License: MIT
"""

import os
import sys
from pathlib import Path
import numpy as np

# Get repository root
repo_root = Path(__file__).resolve().parents[1]
os.chdir(repo_root)

print("=" * 80)
print("CMB COMB FINGERPRINT TEST - COMPLETE WORKFLOW EXAMPLE")
print("=" * 80)
print()

# Step 1: Generate synthetic test data
print("Step 1: Generating synthetic test data...")
print()

test_data_dir = Path('/tmp/cmb_example_data')
test_data_dir.mkdir(exist_ok=True)

# Create Planck synthetic data
np.random.seed(42)
with open(test_data_dir / 'planck_obs.txt', 'w') as f:
    f.write("# ell C_ell sigma\n")
    for ell in range(30, 500):
        cl = 6000.0 * (ell / 10.0)**(-0.5) * np.exp(-ell / 800.0)
        sigma = 0.05 * cl + 50.0
        obs = cl + np.random.normal(0, sigma)
        f.write(f"{ell} {obs:.6f} {sigma:.6f}\n")

with open(test_data_dir / 'planck_model.txt', 'w') as f:
    f.write("# ell C_ell\n")
    for ell in range(30, 500):
        cl = 6000.0 * (ell / 10.0)**(-0.5) * np.exp(-ell / 800.0)
        f.write(f"{ell} {cl:.6f}\n")

# Create WMAP synthetic data (different noise realization)
np.random.seed(137)
with open(test_data_dir / 'wmap_obs.txt', 'w') as f:
    f.write("# ell C_ell sigma\n")
    for ell in range(30, 200):
        cl = 6000.0 * (ell / 10.0)**(-0.5) * np.exp(-ell / 800.0)
        sigma = 0.08 * cl + 80.0  # WMAP has lower sensitivity
        obs = cl + np.random.normal(0, sigma)
        f.write(f"{ell} {obs:.6f} {sigma:.6f}\n")

print(f"✓ Synthetic data created in {test_data_dir}")
print()

# Step 2: Run the one-command CMB comb test
print("Step 2: Running one-command CMB comb test...")
print()
print("Command:")
print("--------")

cmd = f"""python forensic_fingerprint/run_real_data_cmb_comb.py \\
    --planck_obs {test_data_dir}/planck_obs.txt \\
    --planck_model {test_data_dir}/planck_model.txt \\
    --wmap_obs {test_data_dir}/wmap_obs.txt \\
    --ell_min_planck 30 --ell_max_planck 499 \\
    --ell_min_wmap 30 --ell_max_wmap 199 \\
    --variant C --mc_samples 1000 \\
    --output_dir /tmp/cmb_example_output"""

print(cmd)
print()
print("Running...")
print()

# Execute the command
os.system(cmd)

# Step 3: Show the results
print()
print("=" * 80)
print("Step 3: Results Summary")
print("=" * 80)
print()

output_dir = Path('/tmp/cmb_example_output')

if output_dir.exists():
    print(f"✓ Results saved to: {output_dir}")
    print()
    print("Output files:")
    for file in sorted(output_dir.glob('*')):
        if file.is_file():
            size = file.stat().st_size
            print(f"  - {file.name} ({size:,} bytes)")
    
    if (output_dir / 'figures').exists():
        print(f"  - figures/")
        for fig in sorted((output_dir / 'figures').glob('*.png')):
            size = fig.stat().st_size
            print(f"    - {fig.name} ({size:,} bytes)")
    
    print()
    print("-" * 80)
    print("COMBINED VERDICT (first 50 lines):")
    print("-" * 80)
    print()
    
    verdict_file = output_dir / 'combined_verdict.md'
    if verdict_file.exists():
        with open(verdict_file, 'r') as f:
            lines = f.readlines()[:50]
            print(''.join(lines))
        
        if len(lines) >= 50:
            print("\n... (see full verdict in combined_verdict.md)")
    else:
        print("ERROR: combined_verdict.md not found")
else:
    print("ERROR: Output directory not created")

print()
print("=" * 80)
print("WORKFLOW COMPLETE")
print("=" * 80)
print()
print("Next steps:")
print("1. Review combined_verdict.md for PASS/FAIL decision")
print("2. Examine figures/*.png for visual diagnostics")
print("3. Use JSON files for programmatic analysis")
print()
print("For real analysis:")
print("- Download Planck PR3 and WMAP data from https://pla.esac.esa.int/")
print("- Use SHA-256 manifests for data provenance")
print("- Increase --mc_samples to 10000-100000 for publication")
print()
