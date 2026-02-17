#!/usr/bin/env python3
"""
137 vs 139 Channel Analysis Script
===================================

This script analyzes scan-derived spectral signatures to determine if
137-channel vs 139-channel are distinguishable, and whether mod-4 prime
class structure shows systematic differences.

Part A1: Load and normalize scan data
Part A2: Local peak comparison (137 vs 139)
Part A3: Mod-4 class energy test (p≡1 vs p≡3 mod 4)
Part A4: Stability under protocols

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

import os
import sys
import glob
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats
import json

# Setup paths
REPO_ROOT = Path(__file__).parent.parent
SCANS_DIR = REPO_ROOT / "scans"
REPORTS_DIR = REPO_ROOT / "reports" / "channel_analysis"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def is_prime(n):
    """Deterministic primality test for integers."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def load_and_normalize_csv(filepath):
    """
    Load a CSV file and normalize columns.
    
    Returns:
        DataFrame with standardized columns: n, signal, and any additional metadata
    """
    df = pd.read_csv(filepath)
    
    # Create a copy to avoid modifying original
    normalized = df.copy()
    
    # Detect and standardize the 'n' column (scanned integer)
    # Extended list to include 'raw' and other common column names
    n_candidates = ['n', 'k', 'k_target', 'raw', 'period', 'ell', 'target', 'value', 'p']
    n_col = None
    for col in n_candidates:
        if col in normalized.columns:
            n_col = col
            break
    
    if n_col is None:
        raise ValueError(f"Could not find 'n' column in {filepath}")
    
    # Handle 'raw' column specially - round to integer when close
    if n_col == 'raw':
        raw_values = pd.to_numeric(normalized[n_col], errors='coerce')
        # Round to integer when within 1e-6 of an integer
        rounded = np.round(raw_values)
        is_close_to_int = np.abs(raw_values - rounded) < 1e-6
        # Use rounded value for integers, keep float for non-integers (local peaks)
        normalized['n'] = np.where(is_close_to_int, rounded, raw_values)
    else:
        normalized['n'] = pd.to_numeric(normalized[n_col], errors='coerce')
    
    # Filter by 'kind' column if present, keeping scan-related rows
    if 'kind' in normalized.columns:
        valid_kinds = ['scan', 'target', 'scan_peak']
        normalized = normalized[normalized['kind'].isin(valid_kinds)].copy()
    
    # Detect and standardize the 'signal' column
    # Priority: psd_obs > obs_psd > rarity_bits > -log10(p_mc) > -log10(p_global)
    signal_col = None
    if 'psd_obs' in normalized.columns:
        normalized['signal'] = pd.to_numeric(normalized['psd_obs'], errors='coerce')
        signal_col = 'psd_obs'
    elif 'obs_psd' in normalized.columns:
        normalized['signal'] = pd.to_numeric(normalized['obs_psd'], errors='coerce')
        signal_col = 'obs_psd'
    elif 'rarity_bits' in normalized.columns:
        normalized['signal'] = pd.to_numeric(normalized['rarity_bits'], errors='coerce')
        signal_col = 'rarity_bits'
    elif 'p_mc' in normalized.columns:
        p_mc = pd.to_numeric(normalized['p_mc'], errors='coerce')
        # Transform p-value: -log10(p), but handle p=0 and NaN
        normalized['signal'] = -np.log10(p_mc.replace(0, np.nan))
        signal_col = '-log10(p_mc)'
    elif 'p_global' in normalized.columns:
        p_global = pd.to_numeric(normalized['p_global'], errors='coerce')
        normalized['signal'] = -np.log10(p_global.replace(0, np.nan))
        signal_col = '-log10(p_global)'
    else:
        raise ValueError(f"Could not find signal column in {filepath}")
    
    # Remove NaN and inf values
    normalized = normalized.replace([np.inf, -np.inf], np.nan)
    normalized = normalized.dropna(subset=['n', 'signal'])
    
    # Store metadata
    normalized.attrs['source_file'] = filepath.name
    normalized.attrs['signal_col'] = signal_col
    normalized.attrs['n_col'] = n_col
    
    return normalized

def local_peak_analysis(df, target_n, window_sizes=[10, 25]):
    """
    Analyze local peak statistics around target_n.
    
    Returns:
        Dictionary with local statistics
    """
    results = {}
    
    # Check if target_n exists in data
    if target_n not in df['n'].values:
        return None
    
    signal_at_n = df[df['n'] == target_n]['signal'].iloc[0]
    results['n'] = target_n
    results['signal'] = signal_at_n
    
    for window_size in window_sizes:
        window_key = f'w{window_size}'
        
        # Define window
        n_min = target_n - window_size
        n_max = target_n + window_size
        
        window_df = df[(df['n'] >= n_min) & (df['n'] <= n_max)]
        
        if len(window_df) < 3:
            continue
        
        window_signals = window_df['signal'].values
        mean_signal = np.mean(window_signals)
        std_signal = np.std(window_signals, ddof=1)
        
        # Z-score
        if std_signal > 0:
            z_local = (signal_at_n - mean_signal) / std_signal
        else:
            z_local = 0.0
        
        # Rank in window (1 = highest)
        rank = len(window_signals) - stats.rankdata(window_signals, method='average')[
            window_df['n'].values == target_n
        ][0] + 1
        
        # Local slopes (left and right)
        left_df = window_df[window_df['n'] < target_n].sort_values('n')
        right_df = window_df[window_df['n'] > target_n].sort_values('n')
        
        slope_left = None
        if len(left_df) >= 2:
            x = left_df['n'].values[-5:]  # Last 5 points
            y = left_df['signal'].values[-5:]
            if len(x) >= 2:
                slope_left = np.polyfit(x, y, 1)[0]
        
        slope_right = None
        if len(right_df) >= 2:
            x = right_df['n'].values[:5]  # First 5 points
            y = right_df['signal'].values[:5]
            if len(x) >= 2:
                slope_right = np.polyfit(x, y, 1)[0]
        
        # Peak width estimate (FWHM-like)
        half_max = signal_at_n / 2.0
        above_half = window_df[window_df['signal'] >= half_max]
        if len(above_half) > 0:
            peak_width = above_half['n'].max() - above_half['n'].min()
        else:
            peak_width = 0
        
        results[f'{window_key}_mean'] = mean_signal
        results[f'{window_key}_std'] = std_signal
        results[f'{window_key}_z'] = z_local
        results[f'{window_key}_rank'] = rank
        results[f'{window_key}_rank_pct'] = rank / len(window_signals) * 100
        results[f'{window_key}_slope_left'] = slope_left
        results[f'{window_key}_slope_right'] = slope_right
        results[f'{window_key}_peak_width'] = peak_width
    
    return results

def compare_137_139(df, output_prefix):
    """
    Compare local statistics around n=137 and n=139.
    """
    stats_137 = local_peak_analysis(df, 137)
    stats_139 = local_peak_analysis(df, 139)
    
    if stats_137 is None and stats_139 is None:
        return None, None
    
    # Create comparison DataFrame
    comparison_data = []
    if stats_137:
        comparison_data.append({
            'n': 137,
            **{k: v for k, v in stats_137.items() if k != 'n'}
        })
    if stats_139:
        comparison_data.append({
            'n': 139,
            **{k: v for k, v in stats_139.items() if k != 'n'}
        })
    
    comparison_df = pd.DataFrame(comparison_data)
    
    # Generate markdown report
    report_lines = [
        f"## Local Peak Comparison: 137 vs 139",
        f"",
        f"**Source**: {df.attrs.get('source_file', 'unknown')}",
        f"**Signal metric**: {df.attrs.get('signal_col', 'unknown')}",
        f"",
        f"### Summary Table",
        f"",
    ]
    
    # Add table
    report_lines.append(comparison_df.to_markdown(index=False, floatfmt='.4f'))
    report_lines.append("")
    
    # Add interpretation
    if stats_137 and stats_139:
        report_lines.extend([
            f"### Interpretation",
            f"",
            f"- **Signal at 137**: {stats_137['signal']:.6e}",
            f"- **Signal at 139**: {stats_139['signal']:.6e}",
            f"- **Ratio (137/139)**: {stats_137['signal']/stats_139['signal']:.6e}" if stats_139['signal'] != 0 else "- **Ratio (137/139)**: undefined (div by zero)",
            f"",
        ])
        
        for window_size in [10, 25]:
            wk = f'w{window_size}'
            if f'{wk}_z' in stats_137 and f'{wk}_z' in stats_139:
                report_lines.extend([
                    f"**Window ±{window_size}:**",
                    f"- Z-score at 137: {stats_137[f'{wk}_z']:.6e}",
                    f"- Z-score at 139: {stats_139[f'{wk}_z']:.6e}",
                    f"- Rank at 137: {stats_137[f'{wk}_rank']:.0f} ({stats_137[f'{wk}_rank_pct']:.1f}th percentile)",
                    f"- Rank at 139: {stats_139[f'{wk}_rank']:.0f} ({stats_139[f'{wk}_rank_pct']:.1f}th percentile)",
                    f"",
                ])
    
    report_text = '\n'.join(report_lines)
    
    return comparison_df, report_text

def mod4_class_energy_test(df, output_prefix, n_permutations=10000):
    """
    Test if primes p≡1 mod 4 vs p≡3 mod 4 have different energy distributions.
    """
    # Filter to primes only
    df_primes = df[df['n'].apply(is_prime)].copy()
    
    if len(df_primes) < 10:
        return None, "Not enough primes for analysis"
    
    # Partition by mod 4 class
    df_primes['mod4'] = df_primes['n'] % 4
    c1_primes = df_primes[df_primes['mod4'] == 1]
    c3_primes = df_primes[df_primes['mod4'] == 3]
    
    if len(c1_primes) < 2 or len(c3_primes) < 2:
        return None, "Not enough primes in each class"
    
    # Compute class energies
    E_c1 = c1_primes['signal'].sum()
    E_c3 = c3_primes['signal'].sum()
    E_diff_obs = E_c1 - E_c3
    
    # Compute z-score based energy
    all_signals = df['signal'].values
    mean_bg = np.mean(all_signals)
    std_bg = np.std(all_signals, ddof=1)
    
    if std_bg > 0:
        z_c1 = ((c1_primes['signal'] - mean_bg) / std_bg).sum()
        z_c3 = ((c3_primes['signal'] - mean_bg) / std_bg).sum()
        z_diff_obs = z_c1 - z_c3
    else:
        z_c1 = z_c3 = z_diff_obs = 0.0
    
    # Permutation test
    all_prime_signals = df_primes['signal'].values
    n_c1 = len(c1_primes)
    
    perm_diffs = []
    np.random.seed(42)  # Reproducible results
    
    for _ in range(n_permutations):
        shuffled = np.random.permutation(all_prime_signals)
        perm_E_c1 = shuffled[:n_c1].sum()
        perm_E_c3 = shuffled[n_c1:].sum()
        perm_diffs.append(perm_E_c1 - perm_E_c3)
    
    # Two-tailed p-value
    perm_diffs = np.array(perm_diffs)
    p_value = np.mean(np.abs(perm_diffs) >= np.abs(E_diff_obs))
    
    # Generate report
    report_lines = [
        f"## Mod-4 Class Energy Test",
        f"",
        f"**Source**: {df.attrs.get('source_file', 'unknown')}",
        f"**Signal metric**: {df.attrs.get('signal_col', 'unknown')}",
        f"",
        f"### Prime Statistics",
        f"",
        f"- Total primes analyzed: {len(df_primes)}",
        f"- Class C1 (p≡1 mod 4): {len(c1_primes)} primes",
        f"- Class C3 (p≡3 mod 4): {len(c3_primes)} primes",
        f"",
        f"### Energy Analysis",
        f"",
        f"**Raw Energy:**",
        f"- E(C1) = {E_c1:.6e}",
        f"- E(C3) = {E_c3:.6e}",
        f"- ΔE = E(C1) - E(C3) = {E_diff_obs:.6e}",
        f"",
        f"**Z-score Energy (robust):**",
        f"- E_z(C1) = {z_c1:.6e}",
        f"- E_z(C3) = {z_c3:.6e}",
        f"- ΔE_z = {z_diff_obs:.6e}",
        f"",
        f"### Permutation Test Result",
        f"",
        f"- Number of permutations: {n_permutations}",
        f"- Observed |ΔE|: {np.abs(E_diff_obs):.6e}",
        f"- p-value (two-tailed): {p_value:.6e}",
        f"",
        f"**Interpretation:**",
        f"",
    ]
    
    if p_value < 0.01:
        verdict = "SIGNIFICANT"
        interpretation = f"The difference between mod-4 classes is statistically significant (p < 0.01)"
    elif p_value < 0.05:
        verdict = "MARGINAL"
        interpretation = f"The difference shows marginal significance (p < 0.05)"
    else:
        verdict = "NOT SIGNIFICANT"
        interpretation = f"No significant difference detected between mod-4 classes (p = {p_value:.6e})"
    
    report_lines.append(f"- **Verdict**: {verdict}")
    report_lines.append(f"- {interpretation}")
    report_lines.append("")
    
    report_text = '\n'.join(report_lines)
    
    # Create summary DataFrame
    summary_df = pd.DataFrame([{
        'source': df.attrs.get('source_file', 'unknown'),
        'n_primes': len(df_primes),
        'n_c1': len(c1_primes),
        'n_c3': len(c3_primes),
        'E_c1': E_c1,
        'E_c3': E_c3,
        'delta_E': E_diff_obs,
        'z_c1': z_c1,
        'z_c3': z_c3,
        'delta_z': z_diff_obs,
        'p_value': p_value,
        'verdict': verdict
    }])
    
    return summary_df, report_text

def main():
    """Main analysis function."""
    print("=" * 80)
    print("137 vs 139 Channel Analysis")
    print("=" * 80)
    print()
    
    # A1: Load and normalize
    print("A1: Loading and normalizing scan data...")
    
    # Preferred files
    preferred_patterns = [
        "bb_scan_100_200.csv",
        "*scan_int_*.csv",  # Include integer scan files
        "tt_obs_w128.csv",
        "*k137_139*.csv"
    ]
    
    csv_files = []
    for pattern in preferred_patterns:
        csv_files.extend(glob.glob(str(SCANS_DIR / pattern)))
    
    # Also get some general scans
    if len(csv_files) < 5:
        csv_files.extend(glob.glob(str(SCANS_DIR / "*.csv")))
    
    csv_files = list(set(csv_files))  # Remove duplicates
    csv_files.sort()
    
    print(f"Found {len(csv_files)} CSV files")
    
    # Create inventory
    inventory_lines = [
        "# Input Data Inventory",
        "",
        f"Total CSV files found: {len(csv_files)}",
        "",
        "## Files to be analyzed:",
        ""
    ]
    
    valid_datasets = []
    
    for csv_file in csv_files[:50]:  # Limit to first 50 to avoid overwhelming
        try:
            df = load_and_normalize_csv(Path(csv_file))
            valid_datasets.append((Path(csv_file).name, df))
            
            inventory_lines.append(f"- `{Path(csv_file).name}`")
            inventory_lines.append(f"  - Signal column: {df.attrs['signal_col']}")
            inventory_lines.append(f"  - n column: {df.attrs['n_col']}")
            inventory_lines.append(f"  - Data points: {len(df)}")
            inventory_lines.append(f"  - n range: [{df['n'].min():.0f}, {df['n'].max():.0f}]")
            inventory_lines.append("")
            
        except Exception as e:
            inventory_lines.append(f"- `{Path(csv_file).name}` - **ERROR**: {str(e)}")
            inventory_lines.append("")
    
    inventory_text = '\n'.join(inventory_lines)
    inventory_path = REPORTS_DIR / "input_inventory.md"
    inventory_path.write_text(inventory_text)
    print(f"Wrote inventory to {inventory_path}")
    
    # A2: Local peak comparison
    print("\nA2: Local peak comparison (137 vs 139)...")
    
    all_comparisons = []
    comparison_reports = []
    
    for filename, df in valid_datasets:
        print(f"  Analyzing {filename}...")
        comparison_df, report_text = compare_137_139(df, filename)
        
        if comparison_df is not None:
            comparison_df.insert(0, 'source', filename)
            all_comparisons.append(comparison_df)
            comparison_reports.append(report_text)
    
    if all_comparisons:
        combined_comparison = pd.concat(all_comparisons, ignore_index=True)
        combined_comparison.to_csv(
            REPORTS_DIR / "local_137_139_comparison.csv",
            index=False
        )
        
        # Combined report
        combined_report = '\n\n---\n\n'.join(comparison_reports)
        (REPORTS_DIR / "local_137_139_comparison.md").write_text(combined_report)
        print(f"  Wrote comparison report")
    
    # A3: Mod-4 class energy test
    print("\nA3: Mod-4 class energy test...")
    
    all_mod4_results = []
    mod4_reports = []
    
    for filename, df in valid_datasets:
        print(f"  Testing {filename}...")
        summary_df, report_text = mod4_class_energy_test(df, filename)
        
        if summary_df is not None:
            all_mod4_results.append(summary_df)
            mod4_reports.append(report_text)
    
    if all_mod4_results:
        combined_mod4 = pd.concat(all_mod4_results, ignore_index=True)
        combined_mod4.to_csv(
            REPORTS_DIR / "mod4_class_energy.csv",
            index=False
        )
        
        combined_mod4_report = '\n\n---\n\n'.join(mod4_reports)
        (REPORTS_DIR / "mod4_class_energy.md").write_text(combined_mod4_report)
        print(f"  Wrote mod-4 report")
    
    # Generate summary
    print("\nGenerating summary...")
    
    summary_lines = [
        "# Channel Analysis Summary",
        "",
        "## Overview",
        "",
        f"This analysis examines {len(valid_datasets)} scan datasets to determine:",
        "1. Whether signals at n=137 vs n=139 are distinguishable",
        "2. Whether primes p≡1 mod 4 vs p≡3 mod 4 show systematic differences",
        "",
        "## Key Findings",
        "",
        "### 137 vs 139 Local Peak Comparison",
        "",
    ]
    
    if all_comparisons:
        # Analyze the comparison results
        n137_data = combined_comparison[combined_comparison['n'] == 137]
        n139_data = combined_comparison[combined_comparison['n'] == 139]
        
        if len(n137_data) > 0 and len(n139_data) > 0:
            avg_signal_137 = n137_data['signal'].mean()
            avg_signal_139 = n139_data['signal'].mean()
            
            summary_lines.extend([
                f"- Analyzed {len(n137_data)} datasets with n=137 data",
                f"- Analyzed {len(n139_data)} datasets with n=139 data",
                f"- Average signal at 137: {avg_signal_137:.6e}",
                f"- Average signal at 139: {avg_signal_139:.6e}",
                f"- Average ratio (137/139): {avg_signal_137/avg_signal_139:.4f}",
                "",
            ])
            
            # Check if distinguishable
            if 'w10_z' in combined_comparison.columns:
                avg_z137 = n137_data['w10_z'].mean()
                avg_z139 = n139_data['w10_z'].mean()
                
                summary_lines.extend([
                    f"**Local significance (window ±10):**",
                    f"- Mean z-score at 137: {avg_z137:.3f}",
                    f"- Mean z-score at 139: {avg_z139:.3f}",
                    "",
                ])
    
    summary_lines.extend([
        "### Mod-4 Prime Class Test",
        "",
    ])
    
    if all_mod4_results:
        n_significant = (combined_mod4['p_value'] < 0.05).sum()
        n_total = len(combined_mod4)
        
        summary_lines.extend([
            f"- Tested {n_total} datasets",
            f"- Significant results (p < 0.05): {n_significant}/{n_total} ({n_significant/n_total*100:.1f}%)",
            "",
            "**Verdict:**",
            "",
        ])
        
        if n_significant / n_total > 0.5:
            summary_lines.append(
                "- **SYSTEMATIC DIFFERENCE DETECTED**: More than half of datasets "
                "show significant mod-4 class differences"
            )
        elif n_significant > 0:
            summary_lines.append(
                f"- **MIXED RESULTS**: Some datasets ({n_significant}/{n_total}) show "
                "mod-4 class differences, but not consistently across all protocols"
            )
        else:
            summary_lines.append(
                "- **NO SYSTEMATIC DIFFERENCE**: None of the datasets show significant "
                "mod-4 class energy differences"
            )
    
    summary_lines.extend([
        "",
        "## Pipeline Dependencies",
        "",
        "Results are pipeline-dependent. Different analysis protocols (TT, EE, BB, FFT, etc.) ",
        "may show different sensitivities to the 137/139 distinction.",
        "",
        "See detailed reports:",
        "- `local_137_139_comparison.md` - Full local peak analysis",
        "- `mod4_class_energy.md` - Complete mod-4 class test results",
        ""
    ])
    
    summary_text = '\n'.join(summary_lines)
    (REPORTS_DIR / "summary.md").write_text(summary_text)
    print(f"Wrote summary to {REPORTS_DIR / 'summary.md'}")
    
    print("\n" + "=" * 80)
    print("Analysis complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()
