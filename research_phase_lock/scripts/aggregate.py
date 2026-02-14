#!/usr/bin/env python3
"""
aggregate.py

Aggregate results from multiple grid runs into a single summary CSV
with statistical analysis and multiple-testing corrections.

This script:
1. Scans output directories for individual run results
2. Parses CSV files and configuration
3. Computes summary statistics
4. Applies FDR (Benjamini-Hochberg) correction for multiple testing
5. Exports unified summary CSV

Usage:
    python scripts/aggregate.py --input-dir outputs --output results/summary.csv
    python scripts/aggregate.py --input-dir outputs --output results/summary.csv --apply-fdr

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import List, Dict, Any
import numpy as np

# Add parent directory to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from research_phase_lock.utils.io import load_yaml


def benjamini_hochberg_correction(p_values, alpha=0.05):
    """
    Apply Benjamini-Hochberg FDR correction to p-values.
    
    Args:
        p_values: List or array of p-values
        alpha: FDR threshold (default 0.05)
        
    Returns:
        Tuple of (q_values, is_significant)
    """
    p_values = np.array(p_values)
    n = len(p_values)
    
    # Sort p-values and track original indices
    sorted_indices = np.argsort(p_values)
    sorted_p = p_values[sorted_indices]
    
    # Compute q-values (FDR-adjusted p-values)
    # q_i = p_i * n / i
    q_values = np.zeros(n)
    for i in range(n):
        rank = i + 1
        q_values[i] = sorted_p[i] * n / rank
    
    # Enforce monotonicity (q-values should not decrease)
    for i in range(n - 2, -1, -1):
        q_values[i] = min(q_values[i], q_values[i + 1])
    
    # Cap at 1.0
    q_values = np.minimum(q_values, 1.0)
    
    # Restore original order
    original_order_q = np.zeros(n)
    original_order_q[sorted_indices] = q_values
    
    # Determine significance
    is_significant = original_order_q <= alpha
    
    return original_order_q, is_significant


def find_result_files(input_dir):
    """
    Recursively find all result CSV files in input directory.
    
    Args:
        input_dir: Root directory to search
        
    Returns:
        List of tuples (run_dir, csv_path, config_path)
    """
    input_path = Path(input_dir)
    result_files = []
    
    # Look for run directories (typically named run_*)
    for run_dir in input_path.rglob('run_*'):
        if not run_dir.is_dir():
            continue
        
        # Look for results CSV
        csv_candidates = [
            run_dir / 'phase_lock_results.csv',
            run_dir / 'results.csv',
        ]
        
        csv_path = None
        for candidate in csv_candidates:
            if candidate.exists():
                csv_path = candidate
                break
        
        # Look for config YAML
        config_path = run_dir / 'config.yaml'
        
        if csv_path and config_path.exists():
            result_files.append((run_dir, csv_path, config_path))
    
    return result_files


def parse_result_row(csv_row, config, run_dir):
    """
    Parse a single CSV row and augment with config metadata.
    
    Args:
        csv_row: Dictionary from CSV reader
        config: Configuration dictionary
        run_dir: Path to run directory
        
    Returns:
        Enriched dictionary with metadata
    """
    row = dict(csv_row)
    
    # Add run metadata
    row['run_id'] = run_dir.name
    row['run_dir'] = str(run_dir)
    
    # Add config parameters
    for key in ['projection', 'window_size', 'nside_out', 'nlat', 'nlon',
                'window_func', 'null_model', 'mc_samples', 'seed']:
        if key in config:
            row[f'config_{key}'] = config[key]
    
    return row


def aggregate_results(input_dir, output_path, apply_fdr=True, fdr_alpha=0.05):
    """
    Aggregate all results into a single summary CSV.
    
    Args:
        input_dir: Directory containing run outputs
        output_path: Path for output summary CSV
        apply_fdr: Whether to apply FDR correction
        fdr_alpha: FDR threshold (default 0.05)
    """
    print("=" * 70)
    print("AGGREGATING RESULTS")
    print("=" * 70)
    print(f"Input directory: {input_dir}")
    print(f"Output file: {output_path}")
    print(f"Apply FDR: {apply_fdr} (alpha={fdr_alpha})")
    print()
    
    # Find all result files
    result_files = find_result_files(input_dir)
    
    print(f"Found {len(result_files)} result files")
    
    if not result_files:
        print("No results found. Exiting.")
        return
    
    # Parse all results
    all_rows = []
    
    for run_dir, csv_path, config_path in result_files:
        # Load configuration
        try:
            config = load_yaml(config_path)
        except Exception as e:
            print(f"Warning: Could not load config {config_path}: {e}")
            config = {}
        
        # Parse CSV
        try:
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    enriched_row = parse_result_row(row, config, run_dir)
                    all_rows.append(enriched_row)
        except Exception as e:
            print(f"Warning: Could not parse CSV {csv_path}: {e}")
    
    print(f"Parsed {len(all_rows)} total result rows")
    
    if not all_rows:
        print("No valid rows found. Exiting.")
        return
    
    # Apply FDR correction if requested
    if apply_fdr and len(all_rows) > 1:
        print("\nApplying Benjamini-Hochberg FDR correction...")
        
        # Extract p-values (handle missing/invalid values)
        p_values = []
        valid_indices = []
        
        for i, row in enumerate(all_rows):
            try:
                p_val = float(row.get('p_value', 1.0))
                if 0 <= p_val <= 1:
                    p_values.append(p_val)
                    valid_indices.append(i)
            except (ValueError, TypeError):
                pass
        
        if p_values:
            # Compute q-values
            q_values, is_significant = benjamini_hochberg_correction(
                p_values, alpha=fdr_alpha
            )
            
            # Add to rows
            for idx, valid_idx in enumerate(valid_indices):
                all_rows[valid_idx]['q_value'] = f"{q_values[idx]:.6f}"
                all_rows[valid_idx]['fdr_significant'] = str(is_significant[idx])
            
            n_significant = sum(is_significant)
            print(f"  {len(p_values)} p-values processed")
            print(f"  {n_significant} significant after FDR correction (q ≤ {fdr_alpha})")
        else:
            print("  No valid p-values found for FDR correction")
    
    # Write output CSV
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Determine fieldnames (union of all keys)
    fieldnames = set()
    for row in all_rows:
        fieldnames.update(row.keys())
    fieldnames = sorted(fieldnames)
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print(f"\n✓ Summary saved to: {output_path}")
    print(f"  Total rows: {len(all_rows)}")
    print(f"  Columns: {len(fieldnames)}")
    
    # Print basic statistics
    print("\n" + "=" * 70)
    print("BASIC STATISTICS")
    print("=" * 70)
    
    # Group by target k
    k_groups = {}
    for row in all_rows:
        k = row.get('k_target', 'unknown')
        if k not in k_groups:
            k_groups[k] = []
        k_groups[k].append(row)
    
    for k, rows in sorted(k_groups.items()):
        print(f"\nTarget k={k}:")
        print(f"  N runs: {len(rows)}")
        
        # Compute statistics for PC and p-values
        pc_values = []
        p_values = []
        
        for row in rows:
            try:
                pc = float(row.get('phase_coherence', 0))
                pc_values.append(pc)
            except (ValueError, TypeError):
                pass
            
            try:
                p = float(row.get('p_value', 1))
                p_values.append(p)
            except (ValueError, TypeError):
                pass
        
        if pc_values:
            print(f"  Phase Coherence: mean={np.mean(pc_values):.4f}, "
                  f"std={np.std(pc_values):.4f}, "
                  f"min={np.min(pc_values):.4f}, "
                  f"max={np.max(pc_values):.4f}")
        
        if p_values:
            print(f"  P-value: mean={np.mean(p_values):.4f}, "
                  f"median={np.median(p_values):.4f}, "
                  f"min={np.min(p_values):.4f}")
            
            # Count significant results
            n_sig_raw = sum(1 for p in p_values if p <= 0.01)
            print(f"  Significant (p ≤ 0.01): {n_sig_raw}/{len(p_values)} ({100*n_sig_raw/len(p_values):.1f}%)")
    
    print("\n" + "=" * 70)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Aggregate Phase-Lock Grid Results",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--input-dir',
        required=True,
        help='Input directory containing run results'
    )
    
    parser.add_argument(
        '--output',
        required=True,
        help='Output path for summary CSV'
    )
    
    parser.add_argument(
        '--apply-fdr',
        action='store_true',
        default=True,
        help='Apply Benjamini-Hochberg FDR correction (default: True)'
    )
    
    parser.add_argument(
        '--no-fdr',
        dest='apply_fdr',
        action='store_false',
        help='Disable FDR correction'
    )
    
    parser.add_argument(
        '--fdr-alpha',
        type=float,
        default=0.05,
        help='FDR threshold alpha (default: 0.05)'
    )
    
    args = parser.parse_args()
    
    aggregate_results(
        input_dir=args.input_dir,
        output_path=args.output,
        apply_fdr=args.apply_fdr,
        fdr_alpha=args.fdr_alpha
    )


if __name__ == '__main__':
    main()
