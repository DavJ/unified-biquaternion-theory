#!/usr/bin/env python3
# ubt_masses/export_leptons_csv.py
# SPDX-License-Identifier: MIT
"""
Export Lepton Masses to CSV
============================

Generates CSV files with computed lepton masses for use in LaTeX documents.
All values are computed from UBT formulas, not hard-coded.
"""
import csv
import sys
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from ubt_masses.core import compute_lepton_msbar_mass, ubt_alpha_msbar
from ubt_masses.qed import pole_from_msbar_lepton


def export_leptons_csv(output_path: str | Path = "data/leptons.csv"):
    """
    Export computed lepton masses to CSV.
    
    Args:
        output_path: Path to output CSV file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Compute electron mass (only one implemented so far)
    leptons = []
    
    # Electron
    try:
        mbar_e = compute_lepton_msbar_mass("e", mu=None)
        alpha_e = ubt_alpha_msbar(mbar_e)
        mpole_e = pole_from_msbar_lepton(mbar_e, mu=mbar_e, alpha_mu=alpha_e)
        
        leptons.append({
            "name": "electron",
            "symbol": "e",
            "msbar_mass_mev": f"{mbar_e:.12f}",
            "pole_mass_mev": f"{mpole_e:.12f}",
            "mu_mev": f"{mbar_e:.12f}",
            "alpha_mu": f"{alpha_e:.12e}",
        })
    except Exception as e:
        print(f"Warning: Could not compute electron mass: {e}", file=sys.stderr)
    
    # Muon and tau - not yet implemented
    for lepton_name, lepton_symbol in [("muon", "mu"), ("tau", "tau")]:
        leptons.append({
            "name": lepton_name,
            "symbol": lepton_symbol,
            "msbar_mass_mev": "NOT_IMPLEMENTED",
            "pole_mass_mev": "NOT_IMPLEMENTED",
            "mu_mev": "NOT_IMPLEMENTED",
            "alpha_mu": "NOT_IMPLEMENTED",
        })
    
    # Write CSV
    with output_path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["name", "symbol", "msbar_mass_mev", "pole_mass_mev", "mu_mev", "alpha_mu"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leptons)
    
    print(f"Exported lepton masses to {output_path}")
    return output_path


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Export computed lepton masses to CSV")
    parser.add_argument(
        "--output",
        "-o",
        default="data/leptons.csv",
        help="Output CSV file path (default: data/leptons.csv)",
    )
    
    args = parser.parse_args()
    export_leptons_csv(args.output)
