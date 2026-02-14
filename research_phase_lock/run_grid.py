#!/usr/bin/env python3
"""
run_grid.py

Main grid runner for Phase-Lock A/B/C/D verification.

This script:
1. Loads YAML configuration
2. Generates cartesian product of grid parameters
3. Runs unified_phase_lock_scan for each configuration
4. Aggregates and summarizes results

Usage:
    python -m research_phase_lock.run_grid --config research_phase_lock/configs/grid_v1.yaml

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import itertools
import os
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, List

# Add parent to path
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from research_phase_lock.utils.io import load_yaml, save_yaml, make_output_dir
from research_phase_lock.utils.hashing import generate_run_id
from research_phase_lock.adapters.phase_lock_runner import run_phase_lock_scan
from research_phase_lock.analysis.summarize import (
    summarize_grid_results,
    aggregate_results,
    print_summary_stats,
    find_best_runs
)


def expand_grid(grid_params: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Generate cartesian product of grid parameters.
    
    Args:
        grid_params: Dictionary of parameter lists
        
    Returns:
        List of parameter combinations
    """
    # Convert single values to lists
    params = {}
    for key, value in grid_params.items():
        if isinstance(value, list):
            params[key] = value
        else:
            params[key] = [value]
    
    # Generate cartesian product
    keys = list(params.keys())
    values = [params[k] for k in keys]
    
    combinations = []
    for combo in itertools.product(*values):
        config = dict(zip(keys, combo))
        combinations.append(config)
    
    return combinations


def run_grid(config_path: str, resume: bool = False, dry_run: bool = False) -> None:
    """
    Run grid of experiments from YAML config.
    
    Args:
        config_path: Path to YAML configuration file
        resume: Skip already completed runs
        dry_run: Print plan without executing
    """
    # Load configuration
    print("=" * 70)
    print("PHASE-LOCK GRID RUNNER")
    print("=" * 70)
    print(f"Config: {config_path}\n")
    
    config = load_yaml(config_path)
    
    # Extract sections
    global_config = config.get('global', {})
    data_config = config.get('data', {})
    grid_params = config.get('grid', {})
    
    output_root = global_config.get('output_root', 'research_phase_lock/results')
    seed = global_config.get('seed', 42)
    max_runs = global_config.get('max_runs', None)
    
    data_mode = data_config.get('mode', 'synthetic')
    
    # Generate grid
    print("[grid] Generating parameter combinations...")
    combinations = expand_grid(grid_params)
    
    print(f"[grid] Total combinations: {len(combinations)}")
    
    if max_runs and len(combinations) > max_runs:
        print(f"[grid] Limiting to {max_runs} runs")
        combinations = combinations[:max_runs]
    
    # Print grid summary
    print("\n[grid] Parameter ranges:")
    for key, values in grid_params.items():
        if isinstance(values, list):
            print(f"  {key}: {len(values)} values")
        else:
            print(f"  {key}: 1 value")
    
    if dry_run:
        print("\n[grid] DRY RUN - printing first 5 configurations:")
        for i, combo in enumerate(combinations[:5]):
            print(f"\nRun {i+1}:")
            for k, v in combo.items():
                print(f"  {k}: {v}")
        print(f"\n... and {len(combinations)-5} more configurations")
        return
    
    # Execute grid
    print("\n" + "=" * 70)
    print("EXECUTING GRID")
    print("=" * 70)
    
    completed = 0
    failed = 0
    skipped = 0
    
    for i, combo in enumerate(combinations):
        print(f"\n[{i+1}/{len(combinations)}] " + "=" * 50)
        
        # Add seed to config
        combo['seed'] = seed
        
        # Generate run ID
        run_id = generate_run_id(combo)
        output_dir = make_output_dir(output_root, run_id)
        
        # Check if already completed
        results_csv = os.path.join(output_dir, "phase_lock_results.csv")
        if resume and os.path.exists(results_csv):
            print(f"[{run_id}] SKIPPED (already completed)")
            skipped += 1
            continue
        
        print(f"[{run_id}] Running...")
        print(f"  Config: {combo}")
        
        # Save run config
        config_path = os.path.join(output_dir, "config.yaml")
        save_yaml(combo, config_path)
        
        # Prepare data config
        if data_mode == 'synthetic':
            run_data_config = data_config.get('synthetic', {})
        else:
            run_data_config = data_config.get('planck', {})
        
        # Run phase lock scan
        try:
            result = run_phase_lock_scan(
                config=combo,
                output_dir=output_dir,
                data_mode=data_mode,
                data_config=run_data_config,
                verbose=True
            )
            
            print(f"[{run_id}] SUCCESS")
            completed += 1
            
        except Exception as e:
            print(f"[{run_id}] FAILED: {e}")
            traceback.print_exc()
            
            # Save error info
            error_path = os.path.join(output_dir, "error.txt")
            with open(error_path, 'w') as f:
                f.write(f"Error: {e}\n\n")
                f.write(traceback.format_exc())
            
            failed += 1
    
    # Summary
    print("\n" + "=" * 70)
    print("GRID EXECUTION COMPLETE")
    print("=" * 70)
    print(f"Total runs: {len(combinations)}")
    print(f"  Completed: {completed}")
    print(f"  Failed: {failed}")
    print(f"  Skipped: {skipped}")
    
    # Aggregate results
    print("\n" + "=" * 70)
    print("AGGREGATING RESULTS")
    print("=" * 70)
    
    summary_path = os.path.join(output_root, "grid_summary.csv")
    summarize_grid_results(output_root, summary_path)
    
    # Print statistics
    results = aggregate_results(output_root)
    print_summary_stats(results)
    
    # Find best runs
    if results:
        print("\n" + "=" * 70)
        print("TOP 5 RUNS (by phase coherence)")
        print("=" * 70)
        
        best = find_best_runs(results, metric='phase_coherence', n=5)
        for i, r in enumerate(best):
            print(f"{i+1}. run_id={r.get('run_id', 'unknown')}")
            print(f"   k={r.get('k_target', '?')}, PC={r.get('phase_coherence', '?')}, p={r.get('p_value', '?')}")
        
        print("\n" + "=" * 70)
        print("TOP 5 RUNS (by p-value)")
        print("=" * 70)
        
        best_pval = find_best_runs(results, metric='p_value', n=5, ascending=True)
        for i, r in enumerate(best_pval):
            print(f"{i+1}. run_id={r.get('run_id', 'unknown')}")
            print(f"   k={r.get('k_target', '?')}, PC={r.get('phase_coherence', '?')}, p={r.get('p_value', '?')}")
    
    print("\n" + "=" * 70)
    print(f"Results saved to: {output_root}")
    print(f"Summary CSV: {summary_path}")
    print("=" * 70)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Phase-Lock Grid Runner for A/B/C/D Verification",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--config',
        required=True,
        help='Path to YAML configuration file'
    )
    
    parser.add_argument(
        '--resume',
        action='store_true',
        help='Skip already completed runs'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print plan without executing'
    )
    
    args = parser.parse_args()
    
    run_grid(
        config_path=args.config,
        resume=args.resume,
        dry_run=args.dry_run
    )


if __name__ == '__main__':
    main()
