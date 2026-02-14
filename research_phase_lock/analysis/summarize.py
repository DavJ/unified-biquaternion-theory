#!/usr/bin/env python3
"""
summarize.py

Result aggregation and summary for grid experiments.

Provides utilities to:
- Aggregate results from multiple runs
- Compute summary statistics
- Identify best/worst performers
- Generate summary reports

Author: UBT Research Team
License: See repository LICENSE.md
"""

import os
from typing import Any, Dict, List
from pathlib import Path

from research_phase_lock.utils.io import read_csv_dict, write_csv_dict


def aggregate_results(results_dir: str) -> List[Dict[str, Any]]:
    """
    Aggregate results from all runs in results directory.
    
    Walks through the results directory and collects phase_lock_results.csv
    from each run subdirectory.
    
    Args:
        results_dir: Base results directory
        
    Returns:
        List of aggregated result dictionaries
    """
    aggregated = []
    
    results_path = Path(results_dir)
    if not results_path.exists():
        return aggregated
    
    # Find all run directories
    for run_dir in results_path.iterdir():
        if not run_dir.is_dir():
            continue
        
        # Look for results CSV
        results_csv = run_dir / "phase_lock_results.csv"
        if not results_csv.exists():
            continue
        
        # Read results
        try:
            rows = read_csv_dict(str(results_csv))
            for row in rows:
                # Add run_id
                row['run_id'] = run_dir.name
                aggregated.append(row)
        except Exception as e:
            print(f"Warning: Failed to read {results_csv}: {e}")
            continue
    
    return aggregated


def summarize_grid_results(
    results_dir: str,
    output_path: str,
    sort_by: str = "p_value"
) -> None:
    """
    Create summary CSV of all grid runs.
    
    Args:
        results_dir: Base results directory
        output_path: Output CSV path
        sort_by: Column to sort by (default: p_value)
    """
    # Aggregate all results
    results = aggregate_results(results_dir)
    
    if not results:
        print("Warning: No results found")
        return
    
    # Sort results
    if sort_by in results[0]:
        try:
            results.sort(key=lambda x: float(x.get(sort_by, float('inf'))))
        except (ValueError, TypeError):
            pass  # Keep original order if sorting fails
    
    # Write summary
    write_csv_dict(results, output_path)
    
    print(f"Aggregated {len(results)} results to {output_path}")


def print_summary_stats(results: List[Dict[str, Any]]) -> None:
    """
    Print summary statistics for grid results.
    
    Args:
        results: List of result dictionaries
    """
    if not results:
        print("No results to summarize")
        return
    
    print("\n" + "=" * 70)
    print("GRID SUMMARY STATISTICS")
    print("=" * 70)
    print(f"Total runs: {len(results)}")
    
    # Group by k_target
    k_targets = {}
    for row in results:
        k = row.get('k_target', 'unknown')
        if k not in k_targets:
            k_targets[k] = []
        k_targets[k].append(row)
    
    for k, rows in sorted(k_targets.items()):
        print(f"\nTarget k = {k}:")
        print(f"  Runs: {len(rows)}")
        
        # Extract numeric values
        pcs = []
        pvals = []
        for r in rows:
            try:
                pc = float(r.get('phase_coherence', 0))
                pcs.append(pc)
            except (ValueError, TypeError):
                pass
            
            try:
                pval = float(r.get('p_value', 1))
                pvals.append(pval)
            except (ValueError, TypeError):
                pass
        
        if pcs:
            import statistics
            print(f"  Phase coherence: min={min(pcs):.4f}, max={max(pcs):.4f}, mean={statistics.mean(pcs):.4f}")
        
        if pvals:
            sig_001 = sum(1 for p in pvals if p < 0.001)
            sig_01 = sum(1 for p in pvals if p < 0.01)
            sig_05 = sum(1 for p in pvals if p < 0.05)
            print(f"  Significant runs: p<0.001: {sig_001}, p<0.01: {sig_01}, p<0.05: {sig_05}")
    
    print("=" * 70 + "\n")


def find_best_runs(
    results: List[Dict[str, Any]],
    metric: str = "phase_coherence",
    n: int = 10,
    ascending: bool = False
) -> List[Dict[str, Any]]:
    """
    Find top N runs by specified metric.
    
    Args:
        results: List of result dictionaries
        metric: Metric to sort by (default: phase_coherence)
        n: Number of top runs to return
        ascending: Sort ascending if True (for p-values)
        
    Returns:
        Top N runs
    """
    # Filter results with valid metric
    valid_results = []
    for r in results:
        try:
            float(r.get(metric, float('inf') if not ascending else float('-inf')))
            valid_results.append(r)
        except (ValueError, TypeError):
            continue
    
    # Sort
    valid_results.sort(
        key=lambda x: float(x.get(metric, float('inf') if not ascending else float('-inf'))),
        reverse=not ascending
    )
    
    return valid_results[:n]
