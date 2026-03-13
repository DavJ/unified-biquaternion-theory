#!/usr/bin/env python3
"""
UBT Planck Validation - Report Generation

This module generates markdown and CSV reports summarizing UBT predictions
against Planck 2018 observables.

Protocol Version: 1.0
Date: 2026-01-10
License: MIT License
"""

import os
from pathlib import Path
import csv
from datetime import datetime
import json

from . import constants
from . import mapping
from . import metrics


def generate_report(output_dir="out/planck_validation"):
    """
    Generate complete validation report.
    
    This function:
    1. Computes all UBT predictions (implemented only)
    2. Compares against Planck 2018 observations
    3. Computes statistical metrics
    4. Writes markdown and CSV reports
    
    Parameters
    ----------
    output_dir : str or Path
        Directory to write reports (created if doesn't exist)
    
    Returns
    -------
    dict
        Metrics summary (same as from metrics.compute_metrics_summary)
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get predictions (implemented only)
    predictions_dict = mapping.get_all_predictions()
    
    # Filter to implemented predictions only
    implemented = []
    for param_name, pred_value in predictions_dict.items():
        if pred_value is not None:
            implemented.append(param_name)
    
    # Extract predictions, observations, sigmas for implemented parameters
    predictions = []
    observations = []
    sigmas = []
    parameter_names = []
    
    for param_name in implemented:
        predictions.append(predictions_dict[param_name])
        
        if param_name == 'omega_b_h2':
            observations.append(constants.PLANCK_2018_OMEGA_B_H2)
            sigmas.append(constants.PLANCK_2018_OMEGA_B_H2_SIGMA)
            parameter_names.append('Omega_b h^2')
        elif param_name == 'omega_c_h2':
            observations.append(constants.PLANCK_2018_OMEGA_C_H2)
            sigmas.append(constants.PLANCK_2018_OMEGA_C_H2_SIGMA)
            parameter_names.append('Omega_c h^2')
        elif param_name == 'n_s':
            observations.append(constants.PLANCK_2018_N_S)
            sigmas.append(constants.PLANCK_2018_N_S_SIGMA)
            parameter_names.append('n_s')
        elif param_name == 'theta_star':
            observations.append(constants.PLANCK_2018_THETA_STAR)
            sigmas.append(constants.PLANCK_2018_THETA_STAR_SIGMA)
            parameter_names.append('theta_*')
        elif param_name == 'sigma_8':
            observations.append(constants.PLANCK_2018_SIGMA_8)
            sigmas.append(constants.PLANCK_2018_SIGMA_8_SIGMA)
            parameter_names.append('sigma_8')
    
    # Compute metrics
    summary = metrics.compute_metrics_summary(
        predictions, observations, sigmas, parameter_names
    )
    
    # Write reports
    _write_markdown_report(summary, output_path, predictions_dict)
    _write_csv_report(summary, output_path)
    _write_json_report(summary, output_path)
    
    return summary


def _write_markdown_report(summary, output_path, all_predictions):
    """Write markdown report."""
    filepath = output_path / "validation_report.md"
    
    with open(filepath, 'w') as f:
        # Header
        f.write("# UBT Planck Validation Report\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n\n")
        f.write(f"**Protocol Version:** {constants.PROTOCOL_VERSION}\n\n")
        f.write("---\n\n")
        
        # Architecture parameters
        f.write("## Pre-Registered Architecture Parameters\n\n")
        f.write(f"- **RS_N** (code length): {constants.RS_N} (LOCKED)\n")
        f.write(f"- **RS_K** (data symbols): {constants.RS_K} (LOCKED)\n")
        f.write(f"- **RS Parity symbols**: {constants.RS_PARITY}\n")
        f.write(f"- **OFDM Channels**: {constants.OFDM_CHANNELS} (LOCKED)\n\n")
        f.write("---\n\n")
        
        # Predictions table
        f.write("## UBT Predictions vs. Planck 2018\n\n")
        f.write("| Parameter | UBT Prediction | Planck 2018 | Sigma | Z-score | Status |\n")
        f.write("|-----------|----------------|-------------|-------|---------|--------|\n")
        
        for p in summary['parameters']:
            status_icon = "✓" if p['within_1sigma'] else ("⚠" if p['within_2sigma'] else "✗")
            f.write(
                f"| {p['name']} | {p['predicted']:.6f} | {p['observed']:.6f} | "
                f"{p['sigma']:.6f} | {p['z_score']:+.3f} | {status_icon} |\n"
            )
        
        # TBD parameters
        f.write("\n### To-Be-Determined Parameters\n\n")
        f.write("The following parameters are NOT YET IMPLEMENTED:\n\n")
        
        tbd_count = 0
        if all_predictions['theta_star'] is None:
            f.write(f"- **theta_\\*** (sound horizon angle): Target = {constants.PLANCK_2018_THETA_STAR:.4f} ± {constants.PLANCK_2018_THETA_STAR_SIGMA:.4f}\n")
            f.write("  - Must be derived from RS(255,200) architecture with NO new parameters\n")
            tbd_count += 1
        
        if all_predictions['sigma_8'] is None:
            f.write(f"- **sigma_8** (matter fluctuations): Target = {constants.PLANCK_2018_SIGMA_8:.3f} ± {constants.PLANCK_2018_SIGMA_8_SIGMA:.3f}\n")
            f.write("  - Must be derived from RS(255,200) architecture with NO new parameters\n")
            tbd_count += 1
        
        f.write("\n---\n\n")
        
        # Statistical metrics
        f.write("## Statistical Metrics\n\n")
        f.write(f"- **Chi-square**: {summary['chi2_total']:.3f}\n")
        f.write(f"- **Degrees of freedom**: {summary['dof']}\n")
        f.write(f"- **P-value**: {summary['pvalue']:.4f}\n")
        f.write(f"- **Success criterion** (all |z| ≤ 1): {'**YES** ✓' if summary['success'] else '**NO** ✗'}\n\n")
        
        # Interpretation
        f.write("---\n\n")
        f.write("## Interpretation\n\n")
        
        if summary['success']:
            f.write("**Status**: All implemented predictions agree with Planck 2018 within 1σ. ")
            f.write("This is consistent with the UBT digital-architecture hypothesis.\n\n")
        else:
            f.write("**Status**: Some predictions exceed 1σ deviation from Planck 2018. ")
            f.write("Further investigation needed.\n\n")
        
        if tbd_count > 0:
            f.write(f"**Important**: {tbd_count} parameter(s) remain TBD. ")
            f.write("The digital-architecture hypothesis is considered incomplete until these are derived ")
            f.write("from the same RS(255,200) structure with NO additional free parameters.\n\n")
        
        # Falsifiability statement
        f.write("---\n\n")
        f.write("## Falsifiability Statement\n\n")
        f.write("The UBT digital-architecture hypothesis is considered:\n\n")
        f.write("- **SUPPORTED** if all 5 parameters (including TBD) are reproduced within 1σ\n")
        f.write("- **FALSIFIED** if TBD parameters cannot be derived without new free parameters\n")
        f.write("- **FALSIFIED** if any parameter exceeds 3σ deviation\n\n")
        f.write("This follows the pre-registered protocol in `forensic_fingerprint/PROTOCOL.md`.\n\n")
        
        # Footer
        f.write("---\n\n")
        f.write("**References**:\n")
        f.write("- Protocol: `forensic_fingerprint/PROTOCOL.md`\n")
        f.write("- Governance: `REPO_GOVERNANCE.md`\n")
        f.write("- LaTeX appendix: `speculative_extensions/appendices/appendix_PX_planck_validation.tex`\n")
    
    print(f"Markdown report written to: {filepath}")


def _write_csv_report(summary, output_path):
    """Write CSV report."""
    filepath = output_path / "validation_results.csv"
    
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow(['parameter', 'predicted', 'observed', 'sigma', 'z_score', 'chi2_contribution'])
        
        # Data rows
        for p in summary['parameters']:
            writer.writerow([
                p['name'],
                f"{p['predicted']:.8f}",
                f"{p['observed']:.8f}",
                f"{p['sigma']:.8f}",
                f"{p['z_score']:.6f}",
                f"{p['chi2_contribution']:.6f}"
            ])
        
        # Summary row
        writer.writerow([])
        writer.writerow(['SUMMARY', '', '', '', '', ''])
        writer.writerow(['chi2_total', f"{summary['chi2_total']:.6f}", '', '', '', ''])
        writer.writerow(['dof', summary['dof'], '', '', '', ''])
        writer.writerow(['pvalue', f"{summary['pvalue']:.6f}", '', '', '', ''])
        writer.writerow(['success_criterion_met', 'YES' if summary['success'] else 'NO', '', '', '', ''])
    
    print(f"CSV report written to: {filepath}")


def _write_json_report(summary, output_path):
    """Write JSON report."""
    filepath = output_path / "validation_results.json"
    
    # Convert numpy types to Python types for JSON serialization
    json_summary = {
        'metadata': {
            'protocol_version': constants.PROTOCOL_VERSION,
            'protocol_date': constants.PROTOCOL_DATE,
            'generated': datetime.now().isoformat(),
            'rs_n': constants.RS_N,
            'rs_k': constants.RS_K,
            'ofdm_channels': constants.OFDM_CHANNELS
        },
        'parameters': summary['parameters'],
        'metrics': {
            'chi2_total': float(summary['chi2_total']),
            'dof': int(summary['dof']),
            'pvalue': float(summary['pvalue']),
            'success_criterion_met': bool(summary['success']),
            'n_parameters_evaluated': int(summary['n_parameters'])
        }
    }
    
    with open(filepath, 'w') as f:
        json.dump(json_summary, f, indent=2)
    
    print(f"JSON report written to: {filepath}")


if __name__ == '__main__':
    # Generate report when run as script
    print("=" * 80)
    print("UBT Planck Validation Report Generator")
    print("=" * 80)
    print()
    
    summary = generate_report()
    
    print()
    print(metrics.format_metrics_table(summary))
    print()
    print("Reports written to: out/planck_validation/")
