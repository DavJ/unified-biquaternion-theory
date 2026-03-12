#!/usr/bin/env python3
"""
Results Summary and Aggregation

Combines all stability criteria into a unified ranking with
statistical significance and robustness scores.

Usage:
    python results_summary.py --config configs/scan_config.yaml
"""

import argparse
import numpy as np
import pandas as pd
import yaml
from pathlib import Path
import logging
from scipy.stats import zscore


def is_prime(n):
    """Check if n is prime."""
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


def load_all_results(config):
    """Load all criterion results."""
    results_dir = Path(config['output']['results_dir'])
    
    data = {}
    
    # S1
    s1_file = results_dir / 's1_ranking.csv'
    if s1_file.exists():
        data['s1'] = pd.read_csv(s1_file)[['k', 's1', 's1_zscore']]
    
    # S3
    s3_file = results_dir / 's3_energy_ranking.csv'
    if s3_file.exists():
        df = pd.read_csv(s3_file)[['k', 'energy', 'inv_energy', 'is_local_minimum']]
        df['s3_zscore'] = zscore(df['inv_energy'])
        data['s3'] = df
    
    # S4
    s4_file = results_dir / 's4_information_ranking.csv'
    if s4_file.exists():
        data['s4'] = pd.read_csv(s4_file)[['k', 'information_criterion', 'info_zscore']]
    
    # S2 (twin primes)
    s2_file = results_dir / 's2_twin_prime_ranking.csv'
    if s2_file.exists():
        data['s2'] = pd.read_csv(s2_file)
    
    # P-values (if available)
    for criterion in ['s1', 's3', 's4']:
        pval_file = results_dir / f'null_test_{criterion}_pvalues.csv'
        if pval_file.exists():
            data[f'{criterion}_pvalues'] = pd.read_csv(pval_file)
    
    return data


def compute_combined_score(data, config):
    """Compute weighted combined stability score."""
    # Get weights
    weights = config['weights']
    w1 = weights['s1_spectral']
    w2 = weights['s2_twin_prime']
    w3 = weights['s3_energy']
    w4 = weights['s4_information']
    
    # Merge all on k
    df = data['s1'][['k', 's1_zscore']].copy()
    
    if 's3' in data:
        df = df.merge(data['s3'][['k', 's3_zscore']], on='k', how='left')
    else:
        df['s3_zscore'] = 0.0
    
    if 's4' in data:
        df = df.merge(data['s4'][['k', 'info_zscore']], on='k', how='left')
        df.rename(columns={'info_zscore': 's4_zscore'}, inplace=True)
    else:
        df['s4_zscore'] = 0.0
    
    # Fill NaN with 0
    df.fillna(0, inplace=True)
    
    # For S2, we need to aggregate per k (a k can be in multiple pairs)
    if 's2' in data:
        s2_df = data['s2']
        # For each k, find max S2 it participates in
        s2_scores = {}
        for _, row in s2_df.iterrows():
            k1, k2, s2 = row['k1'], row['k2'], row['s2']
            s2_scores[k1] = max(s2_scores.get(k1, -np.inf), s2)
            s2_scores[k2] = max(s2_scores.get(k2, -np.inf), s2)
        
        # Z-score the S2 values
        s2_values = list(s2_scores.values())
        s2_mean = np.mean(s2_values)
        s2_std = np.std(s2_values)
        
        s2_zscore = {k: (v - s2_mean) / s2_std if s2_std > 0 else 0 
                     for k, v in s2_scores.items()}
        
        df['s2_zscore'] = df['k'].map(lambda k: s2_zscore.get(k, 0.0))
    else:
        df['s2_zscore'] = 0.0
    
    # Compute combined score
    df['combined_score'] = (
        w1 * df['s1_zscore'] +
        w2 * df['s2_zscore'] +
        w3 * df['s3_zscore'] +
        w4 * df['s4_zscore']
    )
    
    # Add metadata
    df['is_prime'] = df['k'].apply(is_prime)
    
    # Add p-values if available
    for criterion in ['s1', 's3', 's4']:
        pval_key = f'{criterion}_pvalues'
        if pval_key in data:
            pval_df = data[pval_key][['k', 'p_corrected']]
            pval_df = pval_df.rename(columns={'p_corrected': f'{criterion}_p'})
            df = df.merge(pval_df, on='k', how='left')
    
    # Rank
    df = df.sort_values('combined_score', ascending=False).reset_index(drop=True)
    df['rank'] = df.index + 1
    df['percentile'] = df['rank'].apply(lambda r: (1 - r / len(df)) * 100)
    
    return df


def generate_summary_report(combined_df, data, config):
    """Generate text summary report."""
    report = []
    
    report.append("=" * 70)
    report.append("UBT CHANNEL STABILITY LAB - FINAL RESULTS SUMMARY")
    report.append("=" * 70)
    report.append("")
    
    # Top 10 channels
    report.append("TOP 10 STABLE CHANNELS (Combined Score)")
    report.append("-" * 70)
    top10 = combined_df.head(10)[['rank', 'k', 'combined_score', 'is_prime', 'percentile']]
    report.append(top10.to_string(index=False))
    report.append("")
    
    # Top primes
    top_primes = combined_df[combined_df['is_prime']].head(10)
    report.append("TOP 10 PRIME CHANNELS")
    report.append("-" * 70)
    report.append(top_primes[['rank', 'k', 'combined_score', 'percentile']].to_string(index=False))
    report.append("")
    
    # Twin prime pairs
    if 's2' in data:
        report.append("TOP 10 TWIN PRIME PAIRS")
        report.append("-" * 70)
        s2_df = data['s2'].head(10)[['rank', 'pair', 's2', 's2_zscore', 'percentile']]
        report.append(s2_df.to_string(index=False))
        report.append("")
    
    # Channel 137 analysis
    if 137 in combined_df['k'].values:
        row_137 = combined_df[combined_df['k'] == 137].iloc[0]
        report.append("CHANNEL 137 DETAILED ANALYSIS")
        report.append("-" * 70)
        report.append(f"Overall Rank: {row_137['rank']} / {len(combined_df)}")
        report.append(f"Percentile: {row_137['percentile']:.2f}%")
        report.append(f"Combined Score: {row_137['combined_score']:.4f}")
        report.append(f"S1 Z-Score: {row_137['s1_zscore']:.4f}")
        report.append(f"S2 Z-Score: {row_137['s2_zscore']:.4f}")
        report.append(f"S3 Z-Score: {row_137['s3_zscore']:.4f}")
        report.append(f"S4 Z-Score: {row_137['s4_zscore']:.4f}")
        
        # P-values if available
        for criterion in ['s1', 's3', 's4']:
            col = f'{criterion}_p'
            if col in row_137:
                report.append(f"{criterion.upper()} p-value: {row_137[col]:.4f}")
        
        report.append("")
    
    # Twin pair (137, 139)
    if 's2' in data:
        pair_137_139 = data['s2'][(data['s2']['k1'] == 137) & (data['s2']['k2'] == 139)]
        if not pair_137_139.empty:
            row = pair_137_139.iloc[0]
            report.append("TWIN PRIME PAIR (137, 139) ANALYSIS")
            report.append("-" * 70)
            report.append(f"Rank: {row['rank']} / {len(data['s2'])}")
            report.append(f"S2 Score: {row['s2']:.4f}")
            report.append(f"S2 Z-Score: {row['s2_zscore']:.4f}")
            report.append(f"Phase Coherence: {row['phase_coherence']:.4f}")
            report.append(f"Percentile: {row['percentile']:.2f}%")
            report.append("")
    
    # Statistical summary
    report.append("STATISTICAL SUMMARY")
    report.append("-" * 70)
    n_channels = len(combined_df)
    n_primes = combined_df['is_prime'].sum()
    report.append(f"Total channels scanned: {n_channels}")
    report.append(f"Prime channels: {n_primes} ({100*n_primes/n_channels:.1f}%)")
    
    if 's2' in data:
        n_twin_pairs = len(data['s2'])
        report.append(f"Twin prime pairs found: {n_twin_pairs}")
    
    report.append("")
    report.append("=" * 70)
    
    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description='Aggregate Results and Generate Summary')
    parser.add_argument('--config', type=str, required=True, help='Path to config YAML')
    parser.add_argument('--output', type=str, default=None, help='Output directory')
    parser.add_argument('--verbose', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Load config
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Load all results
    data = load_all_results(config)
    
    if 's1' not in data:
        logging.error("S1 results not found! Run spectral_scan.py first.")
        return
    
    # Compute combined score
    combined_df = compute_combined_score(data, config)
    
    # Determine output directory
    if args.output:
        output_dir = Path(args.output)
    else:
        output_dir = Path(config['output']['results_dir'])
    
    output_dir.mkdir(exist_ok=True)
    
    # Save combined ranking
    output_file = output_dir / 'combined_ranking.csv'
    combined_df.to_csv(output_file, index=False)
    logging.info(f"Combined ranking saved to {output_file}")
    
    # Generate summary report
    report = generate_summary_report(combined_df, data, config)
    
    # Save report
    report_file = output_dir / 'final_summary_report.txt'
    with open(report_file, 'w') as f:
        f.write(report)
    
    logging.info(f"Summary report saved to {report_file}")
    
    # Print to console
    print(report)


if __name__ == '__main__':
    main()
