#!/usr/bin/env python3
"""
Layer 2 Rigidity Experiment Runner - Multi-Scale Stability Test
================================================================

This tool implements a reproducible multi-run experiment pipeline to assess
the stability of Layer 2 parameter space under scaling perturbations.

The experiment runs three sweeps at different range scales:
- Baseline (scale = 1.0): Standard parameter ranges
- Narrow (scale = 0.8): -20% range contraction  
- Wide (scale = 1.2): +20% range expansion

For each scale, the tool:
1. Samples random configurations
2. Computes hit_rate (fraction matching observables)
3. Computes rarity_bits (-log2(hit_rate))
4. Evaluates stability metrics

Stability Verdict:
------------------
The experiment produces a consolidated VERDICT based on:
- max_delta: Maximum change in rarity_bits across scales
- ratio_hit_rate: Ratio of max/min hit rates

Robustness Rule:
IF ratio_hit_rate <= 3 AND max_delta <= 2 bits:
    VERDICT = "STABLE"
ELSE:
    VERDICT = "UNSTABLE"

Usage:
------
    python3 layer2_rigidity_experiment.py \
        --samples 5000 \
        --mapping placeholder \
        --seed 123 \
        --space baseline \
        --outdir scans/layer2/

Output:
-------
Creates directory: scans/layer2/rigidity_experiment_<timestamp>/
    - scale_0.8/ (configurations.csv, summary.json, results.txt)
    - scale_1.0/ (configurations.csv, summary.json, results.txt)
    - scale_1.2/ (configurations.csv, summary.json, results.txt)
    - VERDICT.md (consolidated stability verdict)

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

# Import layer2 sweep module
sys.path.insert(0, str(Path(__file__).parent.parent))
from layer2.layer2_sweep import run_sweep


def compute_stability_metrics(results: List[Dict]) -> Dict:
    """
    Compute stability metrics from multi-scale experiment results.
    
    Parameters
    ----------
    results : List[Dict]
        List of summary results from each scale run
        
    Returns
    -------
    Dict
        Dictionary with stability metrics:
        - max_delta: Maximum change in rarity_bits
        - ratio_hit_rate: Ratio of max/min hit rates
        - verdict: "STABLE" or "UNSTABLE"
    """
    # Extract metrics
    hit_rates = [r['hit_rate'] for r in results]
    rarity_bits = [r['rarity_bits'] for r in results]
    scales = [r['range_scale'] for r in results]
    
    # Get baseline (scale=1.0) values for reference
    baseline_idx = scales.index(1.0)
    baseline_rarity = rarity_bits[baseline_idx]
    
    # Compute max_delta: maximum absolute change from baseline
    max_delta = max(abs(rb - baseline_rarity) for rb in rarity_bits)
    
    # Compute ratio_hit_rate: max/min of all hit rates
    # Handle zero hit rates carefully
    non_zero_rates = [hr for hr in hit_rates if hr > 0]
    if len(non_zero_rates) < len(hit_rates):
        # If any hit rate is zero, ratio is infinite (unstable)
        ratio_hit_rate = float('inf')
    elif len(non_zero_rates) > 0:
        ratio_hit_rate = max(non_zero_rates) / min(non_zero_rates)
    else:
        # All hit rates are zero
        ratio_hit_rate = float('nan')
    
    # Apply robustness rule
    if ratio_hit_rate <= 3.0 and max_delta <= 2.0:
        verdict = "STABLE"
    else:
        verdict = "UNSTABLE"
    
    return {
        'max_delta': max_delta,
        'ratio_hit_rate': ratio_hit_rate,
        'verdict': verdict,
        'baseline_rarity_bits': baseline_rarity,
        'hit_rates': hit_rates,
        'rarity_bits': rarity_bits,
        'scales': scales,
    }


def write_verdict_md(
    stability: Dict,
    results: List[Dict],
    outdir: Path,
    args: argparse.Namespace
):
    """
    Write consolidated VERDICT.md file.
    
    Parameters
    ----------
    stability : Dict
        Stability metrics dictionary
    results : List[Dict]
        List of summary results from each scale run
    outdir : Path
        Output directory path
    args : argparse.Namespace
        Command-line arguments
    """
    verdict_path = outdir / "VERDICT.md"
    
    with open(verdict_path, 'w') as f:
        f.write("# Layer 2 Rigidity Experiment - Stability Verdict\n\n")
        f.write("=" * 80 + "\n\n")
        
        # Experiment metadata
        f.write("## Experiment Configuration\n\n")
        f.write(f"- **Timestamp**: {datetime.now().isoformat()}\n")
        f.write(f"- **Configuration Space**: {args.space}\n")
        f.write(f"- **Samples per Scale**: {args.samples}\n")
        f.write(f"- **Random Seed**: {args.seed}\n")
        f.write(f"- **Mapping Mode**: {args.mapping}\n")
        f.write(f"- **Scales Tested**: 0.8, 1.0, 1.2\n\n")
        
        # Results table
        f.write("## Results by Scale\n\n")
        f.write("| Scale | Hit Rate | Rarity Bits | N Hits | N Samples |\n")
        f.write("|-------|----------|-------------|--------|----------|\n")
        
        for r in results:
            scale = r['range_scale']
            hit_rate = r['hit_rate']
            rarity = r['rarity_bits']
            n_hits = r['n_hits']
            n_samples = r['n_samples']
            
            # Format rarity bits (handle inf)
            rarity_str = f"{rarity:.2f}" if not np.isinf(rarity) else "∞"
            
            f.write(f"| {scale:.1f} | {hit_rate:.6f} | {rarity_str} | "
                   f"{n_hits} | {n_samples} |\n")
        
        f.write("\n")
        
        # Stability metrics
        f.write("## Stability Metrics\n\n")
        f.write(f"- **Max Delta (rarity_bits)**: {stability['max_delta']:.3f} bits\n")
        
        ratio = stability['ratio_hit_rate']
        if np.isinf(ratio):
            f.write(f"- **Ratio Hit Rate (max/min)**: ∞ (unstable - zero hit rate detected)\n")
        elif np.isnan(ratio):
            f.write(f"- **Ratio Hit Rate (max/min)**: N/A (all hit rates zero)\n")
        else:
            f.write(f"- **Ratio Hit Rate (max/min)**: {ratio:.3f}\n")
        
        f.write(f"- **Baseline Rarity**: {stability['baseline_rarity_bits']:.3f} bits\n\n")
        
        # Verdict
        f.write("## Robustness Verdict\n\n")
        f.write("**Robustness Rule**:\n")
        f.write("```\n")
        f.write("IF ratio_hit_rate <= 3.0 AND max_delta <= 2.0 bits:\n")
        f.write("    VERDICT = STABLE\n")
        f.write("ELSE:\n")
        f.write("    VERDICT = UNSTABLE\n")
        f.write("```\n\n")
        
        verdict = stability['verdict']
        f.write(f"### **VERDICT: {verdict}**\n\n")
        
        # Interpretation
        f.write("## Interpretation\n\n")
        
        if verdict == "STABLE":
            f.write("✅ **The Layer 2 parameter space shows STABLE behavior under ±20% range scaling.**\n\n")
            f.write("The hit rate and rarity metrics remain consistent across different "
                   "parameter range scales, suggesting that the configuration space rigidity "
                   "is robust to the sampling range choice.\n\n")
        else:
            f.write("⚠️ **The Layer 2 parameter space shows UNSTABLE behavior under ±20% range scaling.**\n\n")
            
            # Provide specific diagnostics
            if stability['ratio_hit_rate'] > 3.0:
                f.write(f"- Hit rate varies by more than 3x across scales "
                       f"(ratio = {stability['ratio_hit_rate']:.2f})\n")
            
            if stability['max_delta'] > 2.0:
                f.write(f"- Rarity bits shift by more than 2 bits across scales "
                       f"(max_delta = {stability['max_delta']:.2f} bits)\n")
            
            f.write("\nThis suggests that the rigidity assessment is sensitive to the "
                   "choice of parameter ranges. Further investigation is recommended.\n\n")
        
        # Warning for placeholder mode
        if args.mapping == 'placeholder':
            f.write("\n---\n\n")
            f.write("⚠️ **IMPORTANT**: This experiment used PLACEHOLDER physics mapping.\n\n")
            f.write("Results are NOT scientifically interpretable until `--mapping ubt` "
                   "is implemented with proper UBT-to-observables mapping.\n\n")
        
        # File locations
        f.write("## Output Files\n\n")
        f.write("Detailed results for each scale are in:\n")
        for r in results:
            scale = r['range_scale']
            f.write(f"- `scale_{scale}/` - Configurations and analysis for scale={scale}\n")
        f.write("\n")
    
    print(f"  ✓ Saved verdict to: {verdict_path}")


def run_rigidity_experiment(
    samples: int,
    mapping: str,
    seed: int,
    space: str,
    outdir: Path,
) -> int:
    """
    Run the complete rigidity experiment.
    
    Parameters
    ----------
    samples : int
        Number of samples per scale
    mapping : str
        Physics mapping mode ('placeholder' or 'ubt')
    seed : int
        Random seed for reproducibility
    space : str
        Configuration space type
    outdir : Path
        Base output directory
        
    Returns
    -------
    int
        Exit code (0 = success)
    """
    # Create experiment directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = outdir / f"rigidity_experiment_{timestamp}"
    exp_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 80)
    print("Layer 2 Rigidity Experiment - Multi-Scale Stability Test")
    print("=" * 80)
    print()
    print(f"Experiment directory: {exp_dir}")
    print(f"Configuration space: {space}")
    print(f"Samples per scale: {samples}")
    print(f"Random seed: {seed}")
    print(f"Mapping mode: {mapping}")
    print()
    
    if mapping == 'placeholder':
        print("⚠️  WARNING: Using PLACEHOLDER physics mapping")
        print("⚠️  Results are NOT scientifically interpretable!")
        print()
    
    # Define scales to test
    scales = [0.8, 1.0, 1.2]
    
    # Run sweeps for each scale
    results = []
    
    for scale in scales:
        print("=" * 80)
        print(f"Running sweep for scale = {scale:.1f} ({scale*100-100:+.0f}%)")
        print("=" * 80)
        print()
        
        # Create scale-specific output directory
        scale_dir = exp_dir / f"scale_{scale}"
        scale_dir.mkdir(parents=True, exist_ok=True)
        
        # Run sweep
        summary = run_sweep(
            space_type=space,
            n_samples=samples,
            seed=seed,
            mapping_mode=mapping,
            outdir=scale_dir.parent,  # Will create subdirectory with timestamp
            show_progress=True,
            range_scale=scale
        )
        
        # Move timestamped directory to our expected location
        # The run_sweep creates a timestamped directory, we need to find it and move contents
        sweep_dirs = sorted(scale_dir.parent.glob("layer2_sweep_*"))
        if sweep_dirs:
            latest_sweep = sweep_dirs[-1]
            # Move contents to scale_dir
            for item in latest_sweep.iterdir():
                item.rename(scale_dir / item.name)
            latest_sweep.rmdir()
        
        # Add scale to summary for tracking
        summary['range_scale'] = scale
        
        # Store result
        results.append(summary)
        
        print()
        print(f"✓ Completed scale={scale:.1f}: hit_rate={summary['hit_rate']:.6f}, "
              f"rarity_bits={summary['rarity_bits']:.2f}")
        print()
    
    # Compute stability metrics
    print("=" * 80)
    print("Computing Stability Metrics")
    print("=" * 80)
    print()
    
    stability = compute_stability_metrics(results)
    
    print(f"Max Delta (rarity_bits): {stability['max_delta']:.3f} bits")
    print(f"Ratio Hit Rate (max/min): {stability['ratio_hit_rate']:.3f}")
    print(f"Verdict: {stability['verdict']}")
    print()
    
    # Save stability metrics to JSON
    stability_path = exp_dir / "stability_metrics.json"
    with open(stability_path, 'w') as f:
        # Convert to JSON-serializable format
        stability_json = {
            'max_delta': float(stability['max_delta']) if not (np.isinf(stability['max_delta']) or np.isnan(stability['max_delta'])) else None,
            'ratio_hit_rate': float(stability['ratio_hit_rate']) if not (np.isinf(stability['ratio_hit_rate']) or np.isnan(stability['ratio_hit_rate'])) else None,
            'verdict': stability['verdict'],
            'baseline_rarity_bits': float(stability['baseline_rarity_bits']) if not (np.isinf(stability['baseline_rarity_bits']) or np.isnan(stability['baseline_rarity_bits'])) else None,
            'scales': [float(s) for s in stability['scales']],
            'hit_rates': [float(hr) for hr in stability['hit_rates']],
            'rarity_bits': [float(rb) if not (np.isinf(rb) or np.isnan(rb)) else None for rb in stability['rarity_bits']],
        }
        json.dump(stability_json, f, indent=2)
    
    print(f"✓ Saved stability metrics to: {stability_path}")
    
    # Create command-line args namespace for verdict writing
    args = argparse.Namespace(
        samples=samples,
        mapping=mapping,
        seed=seed,
        space=space
    )
    
    # Write consolidated verdict
    write_verdict_md(stability, results, exp_dir, args)
    
    print()
    print("=" * 80)
    print("EXPERIMENT COMPLETE")
    print("=" * 80)
    print()
    print(f"Results saved to: {exp_dir}")
    print(f"Verdict: {stability['verdict']}")
    print()
    
    return 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Layer 2 Rigidity Experiment - Multi-Scale Stability Test",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This tool runs a reproducible multi-scale experiment to assess Layer 2
parameter space stability. It executes sweeps at three different range scales
(0.8, 1.0, 1.2) and produces a consolidated stability verdict.

Examples:
  # Run baseline experiment
  python layer2_rigidity_experiment.py --samples 5000 --mapping placeholder --seed 123

  # Run with UBT mapping (when implemented)
  python layer2_rigidity_experiment.py --samples 10000 --mapping ubt --seed 456 --space wide

Output:
  Creates directory: scans/layer2/rigidity_experiment_<timestamp>/
    - scale_0.8/        : Results for -20% range scale
    - scale_1.0/        : Results for baseline scale
    - scale_1.2/        : Results for +20% range scale
    - VERDICT.md        : Consolidated stability verdict
    - stability_metrics.json : Machine-readable stability metrics
        """
    )
    
    parser.add_argument(
        '--samples',
        type=int,
        default=5000,
        help='Number of samples per scale (default: 5000)'
    )
    
    parser.add_argument(
        '--mapping',
        type=str,
        choices=['placeholder', 'ubt'],
        default='placeholder',
        help='Physics mapping mode (default: placeholder)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=123,
        help='Random seed for reproducibility (default: 123)'
    )
    
    parser.add_argument(
        '--space',
        type=str,
        choices=['baseline', 'wide', 'debug'],
        default='baseline',
        help='Configuration space type (default: baseline)'
    )
    
    parser.add_argument(
        '--outdir',
        type=str,
        default='scans/layer2',
        help='Output directory (default: scans/layer2/)'
    )
    
    args = parser.parse_args()
    
    # Run experiment
    return run_rigidity_experiment(
        samples=args.samples,
        mapping=args.mapping,
        seed=args.seed,
        space=args.space,
        outdir=Path(args.outdir)
    )


if __name__ == '__main__':
    sys.exit(main())
