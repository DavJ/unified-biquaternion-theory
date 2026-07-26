#!/usr/bin/env python3
"""
Layer 2 Fingerprint Sweep - Configuration Space Rigidity Test
==============================================================

⚠️ PROTOCOL REQUIREMENT: Use --mapping ubt for scientifically interpretable results!
The default --mapping placeholder is for framework demonstration ONLY.

This tool tests Layer 2 parameter space rigidity by sampling random
configurations and evaluating match rates against observed constants.

Full protocol: forensic_fingerprint/protocols/PROTOCOL_LAYER2_RIGIDITY.md

Usage Examples:
---------------
# Quick debug test (placeholder physics - NOT interpretable)
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \\
    --space debug --samples 10 --mapping placeholder

# UBT mode (scientifically valid)
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \\
    --space baseline --samples 5000 --mapping ubt --seed 123

# Robustness analysis
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \\
    --space baseline --samples 1000 --mapping ubt --robustness

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

# Add parent directories to path
script_dir = Path(__file__).resolve().parent
repo_root = script_dir.parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Import modular components
from forensic_fingerprint.layer2.config_space import Layer2Config, ConfigurationSpace
from forensic_fingerprint.layer2.predictors import (
    predict_constants,
    get_experimental_values,
    get_default_tolerances,
)
from forensic_fingerprint.layer2.metrics import (
    normalize_error,
    combined_score,
    is_hit,
    compute_hit_rate,
    compute_rarity_bits,
    compute_statistics,
    rank_configuration,
)
from forensic_fingerprint.layer2.report import (
    write_csv,
    write_summary_json,
    write_report_md,
    write_verdict_md,
    save_figures,
)

import numpy as np


# Current Layer 2 parameters (for comparison)
CURRENT_CONFIG = Layer2Config(
    rs_n=255,
    rs_k=200,
    ofdm_channels=16,
    winding_number=137,
    prime_gate_pattern=0,
    quantization_grid=255
)


def run_single_sweep(
    space_type: str,
    n_samples: int,
    seed: int,
    mapping_mode: str,
    targets: List[str],
    tolerances: Dict[str, float],
    range_scale: float,
    outdir: Path,
    show_progress: bool = False
) -> Dict[str, Any]:
    """
    Execute a single fingerprint sweep.
    
    Returns summary with hit_rate, rarity_bits, etc.
    """
    # Create configuration space and RNG
    config_space = ConfigurationSpace(space_type, range_scale=range_scale)
    rng = np.random.default_rng(seed)
    
    # Get experimental values
    exp_values = get_experimental_values()
    
    # Sample and evaluate configurations
    results = []
    scores = []
    n_hits = 0
    
    # Progress tracking
    progress_interval = max(1, n_samples // 10)
    
    for i in range(n_samples):
        if show_progress and (i + 1) % progress_interval == 0:
            print(f"  Processed {i + 1}/{n_samples} samples...")
        
        # Sample configuration
        config = config_space.sample(rng)
        
        # Predict observables
        try:
            predictions = predict_constants(config, mapping=mapping_mode, targets=targets)
        except RuntimeError as e:
            # If UBT mapping fails, report error and exit
            print(f"\nERROR: UBT mapping failed: {e}", file=sys.stderr)
            raise
        
        # Compute errors
        errors = {}
        for obs_name in targets:
            if obs_name in exp_values and obs_name in predictions:
                err = normalize_error(
                    predictions[obs_name],
                    exp_values[obs_name],
                    tolerances[obs_name]
                )
                errors[obs_name] = err
        
        # Compute combined score
        score = combined_score(errors)
        scores.append(score)
        
        # Check if hit
        if is_hit(errors):
            n_hits += 1
        
        # Store result
        result = config.to_dict()
        result.update({
            f'{obs}_predicted': predictions.get(obs, float('nan'))
            for obs in targets
        })
        result.update({
            f'{obs}_error': errors.get(obs, float('nan'))
            for obs in targets
        })
        result['combined_score'] = score
        result['is_hit'] = is_hit(errors)
        
        results.append(result)
    
    # Analyze results
    
    # Find best configuration
    best_idx = np.argmin(scores)
    best_result = results[best_idx]
    best_score = scores[best_idx]
    
    # Compute statistics
    score_stats = compute_statistics(scores)
    
    # Hit-rate analysis
    hit_rate = compute_hit_rate(n_hits, n_samples)
    rarity_bits = compute_rarity_bits(hit_rate)
    
    # Rank current UBT configuration
    current_preds = predict_constants(CURRENT_CONFIG, mapping=mapping_mode, targets=targets)
    current_errors = {}
    for obs_name in targets:
        if obs_name in exp_values and obs_name in current_preds:
            current_errors[obs_name] = normalize_error(
                current_preds[obs_name],
                exp_values[obs_name],
                tolerances[obs_name]
            )
    current_score = combined_score(current_errors)
    current_rank = rank_configuration(current_score, scores)
    
    # Build summary
    summary = {
        'space_type': space_type,
        'n_samples': n_samples,
        'seed': seed,
        'mapping_mode': mapping_mode,
        'range_scale': range_scale,
        'targets': targets,
        'tolerances': tolerances,
        'best_score': best_score,
        'best_config': {k: v for k, v in best_result.items() 
                        if k in Layer2Config.__annotations__},
        'best_predictions': {k: v for k, v in best_result.items() 
                              if k.endswith('_predicted')},
        'score_statistics': score_stats,
        'n_hits': n_hits,
        'hit_rate': hit_rate,
        'rarity_bits': rarity_bits,
        'current_config_score': current_score,
        'current_config_rank': current_rank['rank'],
        'current_config_percentile': current_rank['percentile'],
    }
    
    return summary, results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Layer 2 Fingerprint Sweep - Parameter Space Rigidity Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
⚠️  CRITICAL: Default --mapping placeholder uses TOY physics - NOT interpretable!

For scientifically valid results, use --mapping ubt.

Examples:
  # Quick debug test (placeholder - framework demo only)
  python3 %(prog)s --space debug --samples 10

  # UBT mode (scientifically valid)
  python3 %(prog)s --space baseline --samples 5000 --mapping ubt

  # Robustness analysis (multiple range scales)
  python3 %(prog)s --space baseline --samples 1000 --mapping ubt --robustness

Output: scans/layer2/layer2_sweep_<timestamp>/
  - configurations.csv  : All configs and scores
  - summary.json        : Machine-readable summary
  - report.md           : Human-readable report
  - VERDICT.md          : Final verdict with robustness
  - figures/            : Diagnostic plots
        """
    )
    
    parser.add_argument(
        '--space',
        type=str,
        choices=['baseline', 'wide', 'debug'],
        default='baseline',
        help='Configuration space (default: baseline)'
    )
    
    parser.add_argument(
        '--samples',
        type=int,
        default=5000,
        help='Number of configurations to sample (default: 5000)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=123,
        help='Random seed for reproducibility (default: 123)'
    )
    
    parser.add_argument(
        '--mapping',
        type=str,
        choices=['placeholder', 'ubt'],
        default='placeholder',
        help='Physics mapping mode (default: placeholder) ⚠️ Use ubt for valid results!'
    )
    
    parser.add_argument(
        '--targets',
        type=str,
        default='alpha_inv,electron_mass',
        help='Comma-separated target observables (default: alpha_inv,electron_mass)'
    )
    
    parser.add_argument(
        '--tolerances',
        type=str,
        default=None,
        help='Override tolerances: obs1=val1,obs2=val2 (optional)'
    )
    
    parser.add_argument(
        '--range-scale',
        type=float,
        default=1.0,
        help='Range scaling factor (default: 1.0). Use with --robustness for auto-sweep.'
    )
    
    parser.add_argument(
        '--robustness',
        action='store_true',
        help='Run robustness analysis (scales 0.8, 1.0, 1.2) and generate VERDICT.md'
    )
    
    parser.add_argument(
        '--outdir',
        type=str,
        default='scans/layer2',
        help='Output directory (default: scans/layer2/)'
    )
    
    parser.add_argument(
        '--progress',
        action='store_true',
        help='Show progress during sweep'
    )
    
    args = parser.parse_args()
    
    # Parse targets
    targets = [t.strip() for t in args.targets.split(',')]
    
    # Parse tolerances
    if args.tolerances:
        tolerances = {}
        for pair in args.tolerances.split(','):
            obs, val = pair.split('=')
            tolerances[obs.strip()] = float(val.strip())
    else:
        tolerances = get_default_tolerances()
        # Filter to requested targets
        tolerances = {k: v for k, v in tolerances.items() if k in targets}
    
    # Display header
    print("=" * 80)
    print("Layer 2 Fingerprint Sweep - Protocol v1.0")
    print("=" * 80)
    print()
    
    # Warning for placeholder mode
    if args.mapping == 'placeholder':
        print("╔" + "=" * 78 + "╗")
        print("║" + " " * 78 + "║")
        print("║" + "  ⚠️  WARNING: PLACEHOLDER PHYSICS MAPPING".ljust(78) + "║")
        print("║" + " " * 78 + "║")
        print("║" + "  Results have NO scientific interpretation!".ljust(78) + "║")
        print("║" + "  Framework demonstration only.".ljust(78) + "║")
        print("║" + "  For valid results, use --mapping ubt".ljust(78) + "║")
        print("║" + " " * 78 + "║")
        print("╚" + "=" * 78 + "╝")
        print()
    
    print(f"Configuration space: {args.space}")
    print(f"Samples per run: {args.samples}")
    print(f"Random seed: {args.seed}")
    print(f"Mapping mode: {args.mapping}")
    print(f"Targets: {', '.join(targets)}")
    print(f"Tolerances: {tolerances}")
    print(f"Robustness mode: {'Yes' if args.robustness else 'No'}")
    print()
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = Path(args.outdir) / f"layer2_sweep_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        if args.robustness:
            # Robustness mode: run with multiple range scales
            print("Running robustness analysis...")
            print()
            
            scales = [0.8, 1.0, 1.2]
            robustness_results = {}
            all_results_by_scale = {}
            
            for scale in scales:
                print(f">>> Range scale = {scale}")
                print()
                
                summary, results = run_single_sweep(
                    space_type=args.space,
                    n_samples=args.samples,
                    seed=args.seed + int(scale * 1000),  # Different seed for each scale
                    mapping_mode=args.mapping,
                    targets=targets,
                    tolerances=tolerances,
                    range_scale=scale,
                    outdir=run_dir,
                    show_progress=args.progress
                )
                
                robustness_results[scale] = summary
                all_results_by_scale[scale] = results
                
                print(f"  Hits: {summary['n_hits']} / {summary['n_samples']}")
                print(f"  Hit-rate: {summary['hit_rate']:.6f} ({summary['hit_rate']*100:.4f}%)")
                if summary['rarity_bits'] != float('inf'):
                    print(f"  Rarity: {summary['rarity_bits']:.2f} bits")
                else:
                    print(f"  Rarity: ∞ (no hits)")
                print()
            
            # Use baseline (scale=1.0) as primary results
            baseline_summary = robustness_results[1.0]
            baseline_results = all_results_by_scale[1.0]
            
            # Save baseline outputs
            write_csv(baseline_results, run_dir / "configurations.csv")
            write_summary_json(baseline_summary, run_dir / "summary.json")
            write_report_md(baseline_summary, run_dir / "report.md", args.mapping)
            
            # Save VERDICT with robustness analysis
            write_verdict_md(
                baseline_summary,
                run_dir / "VERDICT.md",
                args.mapping,
                robustness_results=robustness_results
            )
            
            # Save figures (baseline)
            save_figures(baseline_results, run_dir)
            
        else:
            # Single run mode
            print("Running single sweep...")
            print()
            
            summary, results = run_single_sweep(
                space_type=args.space,
                n_samples=args.samples,
                seed=args.seed,
                mapping_mode=args.mapping,
                targets=targets,
                tolerances=tolerances,
                range_scale=args.range_scale,
                outdir=run_dir,
                show_progress=args.progress
            )
            
            print(f"Completed {args.samples} evaluations.")
            print()
            
            # Save outputs
            print("Saving outputs...")
            write_csv(results, run_dir / "configurations.csv")
            write_summary_json(summary, run_dir / "summary.json")
            write_report_md(summary, run_dir / "report.md", args.mapping)
            write_verdict_md(summary, run_dir / "VERDICT.md", args.mapping)
            save_figures(results, run_dir)
        
        print(f"  Saved to: {run_dir}")
        print()
        
        # Display key results
        print("=" * 80)
        print("KEY RESULTS:")
        print("=" * 80)
        print()
        
        if args.mapping == 'placeholder':
            print("⚠️  PLACEHOLDER MODE - Results not scientifically valid")
            print()
        
        if args.robustness:
            summary = robustness_results[1.0]
        
        print(f"Best score found: {summary['best_score']:.6f}")
        print(f"Configurations matching all observables: {summary['n_hits']} ({summary['hit_rate']*100:.4f}%)")
        
        if summary['rarity_bits'] != float('inf'):
            print(f"Rarity: {summary['rarity_bits']:.2f} bits")
        else:
            print(f"Rarity: infinite (no hits)")
        
        print()
        
        if 'current_config_rank' in summary:
            print(f"Current UBT config rank: {summary['current_config_rank']}/{summary['n_samples']} ({summary['current_config_percentile']:.2f}%)")
            print()
        
        # Rigidity assessment
        if args.mapping == 'ubt':
            hit_rate = summary['hit_rate']
            if hit_rate < 0.01:
                print("RIGIDITY: High - matching configurations are rare (<1%)")
            elif hit_rate < 0.05:
                print("RIGIDITY: Moderate - matching configurations uncommon (1-5%)")
            else:
                print("RIGIDITY: Low - matching configurations common (≥5%)")
        else:
            print("RIGIDITY: [Placeholder mode - assessment not valid]")
        
        print()
        print("=" * 80)
        print()
        print(f"Full report: {run_dir / 'VERDICT.md'}")
        print()
        
        return 0
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
