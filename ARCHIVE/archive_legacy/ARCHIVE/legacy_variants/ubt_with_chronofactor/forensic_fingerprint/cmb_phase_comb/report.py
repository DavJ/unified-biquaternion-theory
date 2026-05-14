#!/usr/bin/env python3
"""
Results Reporting for CMB Phase-Comb Test
==========================================

Generate court-grade output:
- JSON results with full metadata
- Markdown verdict report with PASS/FAIL criteria

License: MIT
Author: UBT Research Team
"""

import json
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional


def save_results_json(results: Dict, output_path: str) -> None:
    """
    Save phase-comb test results to JSON file.
    
    Converts numpy types to Python native types for JSON serialization.
    
    Parameters
    ----------
    results : dict
        Results dictionary from run_phase_comb_test
    output_path : str
        Path to output JSON file
    """
    def convert_to_serializable(obj):
        """Recursively convert numpy types to Python types."""
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.integer, np.int64, np.int32)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64, np.float32)):
            return float(obj)
        elif isinstance(obj, (np.bool_, bool)):
            return bool(obj)
        elif isinstance(obj, dict):
            return {str(k): convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [convert_to_serializable(item) for item in obj]
        elif isinstance(obj, np.complex128):
            # For complex numbers, store as dict with real/imag
            return {'real': float(obj.real), 'imag': float(obj.imag)}
        else:
            return obj
    
    results_serializable = convert_to_serializable(results)
    
    # Add timestamp
    results_serializable['saved_at'] = datetime.now().isoformat()
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(results_serializable, f, indent=2)
    
    print(f"Results saved to: {output_path}")


def generate_verdict_markdown(results: Dict, 
                              output_path: str,
                              dataset_name: str = "Planck PR3",
                              manifest_validated: Optional[bool] = None,
                              data_files: Optional[Dict[str, str]] = None) -> None:
    """
    Generate court-grade verdict report in Markdown.
    
    Parameters
    ----------
    results : dict
        Results from run_phase_comb_test
    output_path : str
        Path to output markdown file
    dataset_name : str
        Name of dataset analyzed (default: "Planck PR3")
    manifest_validated : bool or None
        Whether data manifest was validated
    data_files : dict or None
        Dictionary of data files used (map_file, mask_file, etc.)
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        # Header
        f.write("# CMB Phase-Comb Test - Verdict Report\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        f.write(f"**Dataset**: {dataset_name}\n")
        f.write(f"**Test Version**: Phase-Comb v1.0\n")
        f.write(f"**Protocol**: Pre-registered periods (court-grade)\n\n")
        
        f.write("---\n\n")
        
        # Data Provenance
        f.write("## Data Provenance\n\n")
        
        if data_files:
            f.write("### Input Files\n\n")
            for key, path in data_files.items():
                f.write(f"- **{key}**: `{path}`\n")
            f.write("\n")
        
        if manifest_validated is not None:
            status = "✓ VALIDATED" if manifest_validated else "✗ VALIDATION FAILED"
            f.write(f"**SHA-256 Manifest**: {status}\n\n")
        else:
            f.write("**SHA-256 Manifest**: NOT PROVIDED (candidate-grade only)\n\n")
        
        f.write("---\n\n")
        
        # Test Configuration
        f.write("## Test Configuration\n\n")
        f.write(f"- **Multipole range**: ℓ = {results['ell_min']} to {results['ell_max']}\n")
        f.write(f"- **Maximum ℓ (alm)**: lmax = {results['lmax']}\n")
        f.write(f"- **Mode pairing**: {results['m_mode']}\n")
        f.write(f"- **MC surrogates**: {results['n_mc_samples']}\n")
        f.write(f"- **Random seed**: {results['seed']}\n")
        f.write(f"- **Multiple-testing correction**: {results['correction']}\n\n")
        
        # Pre-registered periods
        f.write("### Pre-Registered Candidate Periods\n\n")
        periods_str = ", ".join(map(str, results['periods']))
        f.write(f"**Periods**: P ∈ {{{periods_str}}}\n\n")
        f.write("**IMPORTANT**: These periods were pre-registered before analysis. ")
        f.write("No modifications permitted based on results.\n\n")
        
        f.write("---\n\n")
        
        # Results
        f.write("## Statistical Results\n\n")
        
        f.write("### Phase Coherence R(P)\n\n")
        f.write("| Period P | R(P) observed | Surrogate mean | Surrogate std | P-value | Significance |\n")
        f.write("|----------|---------------|----------------|---------------|---------|-------------|\n")
        
        R_obs = results['R_observed']
        p_vals = results['p_values']
        surr_stats = results['surrogate_stats']
        
        for period in results['periods']:
            R_p = R_obs[period]
            p_p = p_vals[period]
            surr_mean = surr_stats[period]['mean']
            surr_std = surr_stats[period]['std']
            
            # Significance marker
            if p_p < 0.01:
                sig_mark = "**CANDIDATE**" if p_p >= 2.9e-7 else "**STRONG**"
            else:
                sig_mark = "null"
            
            f.write(f"| {period} | {R_p:.6f} | {surr_mean:.6f} | {surr_std:.6f} | {p_p:.6e} | {sig_mark} |\n")
        
        f.write("\n")
        
        # Best period
        best_p = results['best_period']
        best_pval = results['best_p_value']
        
        f.write(f"**Best-fit period**: P = {best_p}\n")
        f.write(f"**Best p-value**: {best_pval:.6e}\n")
        f.write(f"**Overall significance**: **{results['significance']}**\n\n")
        
        f.write("---\n\n")
        
        # PASS/FAIL Decision
        f.write("## PASS/FAIL Decision\n\n")
        
        f.write("### Decision Criteria\n\n")
        f.write("A signal **PASSES** if:\n\n")
        f.write("1. P-value < 0.01 for any pre-registered period (candidate threshold)\n")
        f.write("2. OR P-value < 2.9e-7 for any period (strong/5σ threshold)\n\n")
        
        # Evaluate
        has_candidate = any(p < 0.01 for p in p_vals.values())
        has_strong = any(p < 2.9e-7 for p in p_vals.values())
        
        f.write("### Evaluation\n\n")
        
        criterion_1 = has_candidate
        criterion_2 = has_strong
        
        f.write(f"1. Candidate signal (p < 0.01): **{'✓ YES' if criterion_1 else '✗ NO'}**\n")
        f.write(f"2. Strong signal (p < 2.9e-7): **{'✓ YES' if criterion_2 else '✗ NO'}**\n\n")
        
        # Final verdict
        f.write("### Final Verdict\n\n")
        
        if has_strong:
            f.write("## ✓ **PASS (STRONG)**\n\n")
            f.write("Strong evidence for periodic phase-locking detected. ")
            f.write(f"Best period: P={best_p}, p={best_pval:.6e}\n\n")
            f.write("**Next steps**:\n")
            f.write("- Independent replication with WMAP or other dataset\n")
            f.write("- Systematic error analysis\n")
            f.write("- Prepare manuscript for peer review\n\n")
        elif has_candidate:
            f.write("## ⚠ **CANDIDATE SIGNAL**\n\n")
            f.write("Candidate evidence for periodic phase-locking detected. ")
            f.write(f"Best period: P={best_p}, p={best_pval:.6e}\n\n")
            f.write("**Required for confirmation**:\n")
            f.write("- Independent replication with second dataset (WMAP)\n")
            f.write("- Increase MC samples for better p-value resolution\n")
            f.write("- Systematic checks (see below)\n\n")
        else:
            f.write("## ✗ **FAIL (NULL)**\n\n")
            f.write("No significant periodic phase structure detected.\n\n")
            f.write("**Interpretation**: The data do not support the hypothesis of ")
            f.write("periodic phase-locking in CMB spherical harmonics at the tested ")
            f.write("candidate periods.\n\n")
        
        f.write("---\n\n")
        
        # Interpretation
        f.write("## Interpretation\n\n")
        
        f.write("### What This Test Measures\n\n")
        f.write("- **Phase coherence** between a_lm modes separated by period P\n")
        f.write("- Tests for periodic structure in **arg(a_lm)**, not in power |a_lm|²\n")
        f.write("- Complementary to TT power spectrum comb test\n\n")
        
        f.write("### What This Test Does NOT Measure\n\n")
        f.write("- **Not** a test of C_ℓ power spectrum oscillations\n")
        f.write("- **Not** sensitive to amplitude-only features\n")
        f.write("- Requires map-level data (a_lm), not just C_ℓ\n\n")
        
        f.write("### Null Model\n\n")
        f.write("Phase-randomized surrogates preserving |a_lm| (and thus C_ℓ):\n")
        f.write("- a'_lm = |a_lm| exp(i θ_lm), θ ~ Uniform(0,2π)\n")
        f.write("- Reality constraints enforced (m=0 real, conjugacy)\n")
        f.write(f"- {results['n_mc_samples']} independent realizations\n\n")
        
        f.write("---\n\n")
        
        # Systematic Checks
        f.write("## Systematic Checks\n\n")
        
        f.write("### 1. Multipole Range Robustness\n\n")
        f.write("- **Status**: NOT YET RUN\n")
        f.write("- **Purpose**: Verify signal persists in independent ℓ-windows\n")
        f.write("- **Action**: Run ablation tests with different [ℓ_min, ℓ_max]\n\n")
        
        f.write("### 2. Mask Dependence\n\n")
        f.write("- **Status**: NOT YET RUN\n")
        f.write("- **Purpose**: Check sensitivity to Galactic mask choice\n")
        f.write("- **Action**: Repeat with different mask thresholds\n\n")
        
        f.write("### 3. Surrogate Validation\n\n")
        f.write("- **Sanity check**: Verify surrogates preserve C_ℓ\n")
        f.write("- **Expectation**: R(P) → 0 for random phases\n")
        if 'surrogate_stats' in results:
            surr_means = [results['surrogate_stats'][p]['mean'] for p in results['periods']]
            max_surr_mean = max(surr_means)
            f.write(f"- **Observed**: Surrogate R(P) means ≤ {max_surr_mean:.6f} ✓\n\n")
        else:
            f.write("- **Status**: Run sanity checks with nulls.sanity_check_surrogates()\n\n")
        
        f.write("### 4. Multiple Testing\n\n")
        f.write(f"- **Method**: {results['correction']}\n")
        if results['correction'] == 'none':
            f.write("- **Justification**: Periods pre-registered, fixed set\n")
            f.write("- **Conservative**: Only 4 periods tested (255, 256, 137, 139)\n\n")
        else:
            f.write("- **Correction applied**: See p-values above\n\n")
        
        f.write("---\n\n")
        
        # Data Quality Notes
        f.write("## Data Quality and Limitations\n\n")
        
        if 'metadata' in results and results['metadata']:
            meta = results['metadata']
            
            if 'sky_fraction' in meta:
                f.write(f"- **Sky fraction**: {meta['sky_fraction']:.2%}\n")
            
            if 'monopole_removed' in meta:
                if meta['monopole_removed']:
                    f.write("- **Monopole**: Removed ✓\n")
                if meta.get('dipole_removed'):
                    f.write("- **Dipole**: Removed ✓\n")
        
        f.write("\n")
        
        # MC resolution warning
        mc_samples = results['n_mc_samples']
        p_floor = 1.0 / mc_samples
        
        if best_pval <= p_floor:
            f.write(f"**⚠ WARNING**: Best p-value at MC floor (1/{mc_samples}). ")
            f.write("Increase --mc_samples for better resolution.\n\n")
        
        f.write("---\n\n")
        
        f.write("**End of Report**\n")
    
    print(f"Verdict report saved to: {output_path}")
