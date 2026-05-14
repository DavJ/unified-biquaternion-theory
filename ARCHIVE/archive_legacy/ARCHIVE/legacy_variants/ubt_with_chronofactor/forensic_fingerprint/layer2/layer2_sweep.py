#!/usr/bin/env python3
"""
Layer 2 Fingerprint Sweep - CLI Tool (Refactored)
==================================================

⚠️ PROTOTYPE WARNING: Uses PLACEHOLDER physics mapping by default.
Results are NOT scientifically interpretable until --mapping ubt is implemented.

This tool tests Layer 2 parameter space rigidity by sampling random
configurations and evaluating match rates against observed constants.

Usage:
    python3 layer2_sweep.py --space baseline --samples 5000 --seed 123

Options:
    --space: Configuration space (baseline|wide|debug)
    --samples: Number of configurations to sample
    --seed: Random seed for reproducibility
    --mapping: Physics mapping mode (placeholder|ubt)
    --outdir: Output directory
    --progress: Show progress (requires tqdm)

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import numpy as np

# Import modular components
sys.path.insert(0, str(Path(__file__).parent.parent))
from layer2.config_space import Layer2Config, ConfigurationSpace
from layer2.predictors import predict_constants, get_experimental_values, get_default_tolerances
from layer2.metrics import (
    normalize_error, combined_score, is_hit, 
    compute_hit_rate, compute_rarity_bits,
    compute_statistics, rank_configuration
)
from layer2.report import write_csv, write_summary_json, write_report_md


# Current Layer 2 parameters (for comparison)
CURRENT_CONFIG = Layer2Config(
    rs_n=255,
    rs_k=200,
    ofdm_channels=16,
    winding_number=137,
    prime_gate_pattern=0,
    quantization_grid=255
)


def run_sweep(
    space_type: str,
    n_samples: int,
    seed: int,
    mapping_mode: str,
    outdir: Path,
    show_progress: bool = False,
    range_scale: float = 1.0
) -> Dict:
    """
    Execute the fingerprint sweep.
    
    Parameters
    ----------
    space_type : str
        Configuration space type
    n_samples : int
        Number of samples
    seed : int
        Random seed
    mapping_mode : str
        'placeholder' or 'ubt'
    outdir : Path
        Output directory
    show_progress : bool
        Whether to show progress
    range_scale : float, optional
        Range scaling factor (default: 1.0)
        
    Returns
    -------
    Dict
        Summary statistics
    """
    # Create configuration space and RNG
    config_space = ConfigurationSpace(space_type, range_scale=range_scale)
    rng = np.random.default_rng(seed)
    
    # Get experimental values and tolerances
    exp_values = get_experimental_values()
    tolerances = get_default_tolerances()
    
    # Display header
    print("=" * 80)
    print("Layer 2 Fingerprint Sweep")
    print("=" * 80)
    
    if mapping_mode == 'placeholder':
        print("⚠️  WARNING: Using PLACEHOLDER physics mapping")
        print("⚠️  Results are NOT scientifically interpretable!")
        print("=" * 80)
    
    print(f"Configuration space: {space_type}")
    print(f"Number of samples: {n_samples}")
    print(f"Random seed: {seed}")
    print(f"Mapping mode: {mapping_mode}")
    print(f"Output directory: {outdir}")
    print()
    
    # Sample and evaluate configurations
    print("Sampling configurations...")
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
        predictions = predict_constants(config, mapping=mapping_mode)
        
        # Compute errors
        errors = {}
        for obs_name in predictions.keys():
            if obs_name in exp_values:
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
            f'{obs}_predicted': predictions[obs]
            for obs in predictions.keys()
        })
        result.update({
            f'{obs}_error': errors.get(obs, float('nan'))
            for obs in predictions.keys()
        })
        result['combined_score'] = score
        result['is_hit'] = is_hit(errors)
        
        results.append(result)
    
    print(f"Completed {n_samples} evaluations.")
    print()
    
    # Analyze results
    print("Analyzing results...")
    
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
    current_preds = predict_constants(CURRENT_CONFIG, mapping=mapping_mode)
    current_errors = {}
    for obs_name in current_preds.keys():
        if obs_name in exp_values:
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
    
    # Save outputs
    print("Saving outputs...")
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = outdir / f"layer2_sweep_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # Write files
    write_csv(results, run_dir / "configurations.csv")
    write_summary_json(summary, run_dir / "summary.json")
    write_report_md(summary, run_dir / "results.txt", mapping_mode)
    
    print(f"  Saved configurations to: {run_dir / 'configurations.csv'}")
    print(f"  Saved summary to: {run_dir / 'summary.json'}")
    print(f"  Saved report to: {run_dir / 'results.txt'}")
    print()
    print(f"Sweep complete. Results saved to: {run_dir}")
    print()
    
    # Display key results
    print("=" * 80)
    print("KEY RESULTS:")
    print("=" * 80)
    
    if mapping_mode == 'placeholder':
        print("⚠️  PLACEHOLDER MODE - Results not scientifically valid")
        print()
    
    print(f"Best score found: {best_score:.6f}")
    print(f"Current config rank: {current_rank['rank']}/{n_samples} ({current_rank['percentile']:.2f}%)")
    print(f"Configs matching all observables: {n_hits} ({hit_rate*100:.2f}%)")
    
    if rarity_bits != float('inf'):
        print(f"Rarity: {rarity_bits:.2f} bits")
    else:
        print(f"Rarity: infinite (no hits)")
    
    print()
    
    # Rigidity assessment
    if mapping_mode != 'placeholder':
        if hit_rate < 0.01:
            print("RIGIDITY: High - matching configurations are rare (<1%)")
        elif hit_rate < 0.05:
            print("RIGIDITY: Moderate - matching configurations uncommon (1-5%)")
        else:
            print("RIGIDITY: Low - matching configurations common (≥5%)")
    else:
        print("RIGIDITY: [Placeholder mode - assessment not valid]")
    
    return summary


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Layer 2 Fingerprint Sweep - Configuration Space Rigidity Test",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
⚠️  WARNING: Default mode uses PLACEHOLDER physics - results NOT interpretable!

Examples:
  # Quick debug test (placeholder physics)
  python3 layer2_sweep.py --space debug --samples 50

  # Baseline sweep (placeholder physics - framework demo only)
  python3 layer2_sweep.py --space baseline --samples 5000 --seed 123

  # Try UBT mode (will fail until implemented)
  python3 layer2_sweep.py --space baseline --samples 100 --mapping ubt

Output: Results saved to scans/layer2/layer2_sweep_<timestamp>/
  - configurations.csv  : All configs and scores
  - summary.json        : Machine-readable summary
  - results.txt         : Human-readable report
        """
    )
    
    parser.add_argument(
        '--space',
        type=str,
        choices=['baseline', 'wide', 'debug'],
        default='baseline',
        help='Configuration space to scan (default: baseline)'
    )
    
    parser.add_argument(
        '--samples',
        type=int,
        default=5000,
        help='Number of random configurations to sample (default: 5000)'
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
        help='Physics mapping mode (default: placeholder) ⚠️  ubt not yet implemented'
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
    
    # Run sweep
    try:
        run_sweep(
            space_type=args.space,
            n_samples=args.samples,
            seed=args.seed,
            mapping_mode=args.mapping,
            outdir=Path(args.outdir),
            show_progress=args.progress
        )
        return 0
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
