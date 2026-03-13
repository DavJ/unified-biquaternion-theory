#!/usr/bin/env python3
"""
Heatmap Visualization

Generates heatmaps for:
- S1(k) across channels
- S2(k1, k2) for all pairs
- Prime vs non-prime comparisons

Usage:
    python heatmap_visualization.py --config configs/scan_config.yaml
"""

import argparse
import numpy as np
import pandas as pd
import yaml
from pathlib import Path
import logging
import matplotlib.pyplot as plt
import seaborn as sns


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


def load_results(config):
    """Load all available results."""
    results_dir = Path(config['output']['results_dir'])
    
    data = {}
    
    # S1
    s1_file = results_dir / 's1_ranking.csv'
    if s1_file.exists():
        data['s1'] = pd.read_csv(s1_file)
    
    # S2
    s2_file = results_dir / 's2_twin_prime_ranking.csv'
    if s2_file.exists():
        data['s2'] = pd.read_csv(s2_file)
    
    # S3
    s3_file = results_dir / 's3_energy_ranking.csv'
    if s3_file.exists():
        data['s3'] = pd.read_csv(s3_file)
    
    # S4
    s4_file = results_dir / 's4_information_ranking.csv'
    if s4_file.exists():
        data['s4'] = pd.read_csv(s4_file)
    
    return data


def plot_s1_heatmap(df, config, output_dir):
    """Plot S1(k) as a heatmap bar."""
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # Reshape for heatmap
    k_values = df['k'].values
    s1_values = df['s1'].values
    
    # Create 1D heatmap
    data = s1_values.reshape(1, -1)
    
    sns.heatmap(data, cmap=config['visualization']['colormap'], 
                xticklabels=k_values, yticklabels=False,
                cbar_kws={'label': 'S1 (Spectral Robustness)'}, ax=ax)
    
    ax.set_xlabel('Channel k')
    ax.set_title('S1: Spectral Robustness Across Channels')
    
    # Highlight primes
    prime_indices = [i for i, k in enumerate(k_values) if is_prime(k)]
    for idx in prime_indices:
        ax.axvline(x=idx, color='red', alpha=0.3, linewidth=0.5)
    
    plt.tight_layout()
    output_file = output_dir / 's1_heatmap.png'
    plt.savefig(output_file, dpi=config['visualization']['dpi'])
    plt.close()
    
    logging.info(f"S1 heatmap saved to {output_file}")


def plot_s2_heatmap(config, output_dir):
    """Plot S2(k1, k2) heatmap matrix."""
    results_dir = Path(config['output']['results_dir'])
    
    # Check if heatmap matrix exists
    matrix_file = results_dir / 's2_heatmap_matrix.npy'
    kvalues_file = results_dir / 's2_heatmap_kvalues.npy'
    
    if not matrix_file.exists() or not kvalues_file.exists():
        logging.warning("S2 heatmap matrix not found. Run twin_prime_scan.py with --heatmap first.")
        return
    
    matrix = np.load(matrix_file)
    k_values = np.load(kvalues_file)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sns.heatmap(matrix, cmap=config['visualization']['colormap'],
                xticklabels=k_values[::10], yticklabels=k_values[::10],
                cbar_kws={'label': 'S2 (Twin Prime Coherence)'}, ax=ax)
    
    ax.set_xlabel('Channel k2')
    ax.set_ylabel('Channel k1')
    ax.set_title('S2: Twin Prime Coherence Matrix')
    
    plt.tight_layout()
    output_file = output_dir / 's2_heatmap_full.png'
    plt.savefig(output_file, dpi=config['visualization']['dpi'])
    plt.close()
    
    logging.info(f"S2 heatmap saved to {output_file}")


def plot_prime_comparison(data, config, output_dir):
    """Plot prime vs non-prime comparison across all criteria."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    criteria = [
        ('s1', 's1', 'S1: Spectral Robustness'),
        ('s3', 'energy', 'S3: Energy (lower = better)'),
        ('s4', 'information_criterion', 'S4: Information Criterion'),
    ]
    
    for idx, (key, col, title) in enumerate(criteria):
        if key not in data:
            continue
        
        df = data[key]
        
        row = idx // 2
        col_idx = idx % 2
        ax = axes[row, col_idx]
        
        # Separate primes and non-primes
        primes = df[df['is_prime']][col]
        non_primes = df[~df['is_prime']][col]
        
        # Box plot
        ax.boxplot([primes, non_primes], tick_labels=['Primes', 'Non-Primes'])
        ax.set_ylabel(title)
        ax.set_title(f'{title}\nPrime vs Non-Prime')
        ax.grid(True, alpha=0.3)
    
    # Remove unused subplot
    fig.delaxes(axes[1, 1])
    
    plt.tight_layout()
    output_file = output_dir / 'prime_vs_nonprime_comparison.png'
    plt.savefig(output_file, dpi=config['visualization']['dpi'])
    plt.close()
    
    logging.info(f"Prime comparison plot saved to {output_file}")


def plot_s1_distribution(df, config, output_dir):
    """Plot S1 distribution with prime highlights."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    primes = df[df['is_prime']]['s1']
    non_primes = df[~df['is_prime']]['s1']
    
    ax.hist(non_primes, bins=30, alpha=0.5, label='Non-Primes', color='blue')
    ax.hist(primes, bins=30, alpha=0.7, label='Primes', color='red')
    
    ax.set_xlabel('S1 (Spectral Robustness)')
    ax.set_ylabel('Frequency')
    ax.set_title('S1 Distribution: Primes vs Non-Primes')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_file = output_dir / 's1_distribution.png'
    plt.savefig(output_file, dpi=config['visualization']['dpi'])
    plt.close()
    
    logging.info(f"S1 distribution saved to {output_file}")


def plot_null_distributions(config, output_dir):
    """Plot null distributions from bootstrap test."""
    results_dir = Path(config['output']['results_dir'])
    
    # Find null distribution files
    null_files = list(results_dir.glob('null_distribution_*.npy'))
    
    if not null_files:
        logging.warning("No null distribution files found. Run bootstrap_null.py first.")
        return
    
    fig, axes = plt.subplots(1, len(null_files), figsize=(15, 4))
    
    if len(null_files) == 1:
        axes = [axes]
    
    for idx, null_file in enumerate(null_files):
        null_dist = np.load(null_file)
        
        ax = axes[idx]
        ax.hist(null_dist, bins=50, alpha=0.7, color='gray', edgecolor='black')
        ax.set_xlabel('Null Statistic')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Null Distribution\n{null_file.stem}')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_file = output_dir / 'null_distributions.png'
    plt.savefig(output_file, dpi=config['visualization']['dpi'])
    plt.close()
    
    logging.info(f"Null distributions plot saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate Heatmap Visualizations')
    parser.add_argument('--config', type=str, required=True, help='Path to config YAML')
    parser.add_argument('--output-dir', type=str, default=None, help='Output directory')
    parser.add_argument('--verbose', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Load config
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path(config['output']['results_dir'])
    
    output_dir.mkdir(exist_ok=True)
    
    # Load results
    data = load_results(config)
    
    if not data:
        logging.error("No results found. Run scans first!")
        return
    
    # Generate plots
    logging.info("Generating visualizations...")
    
    if 's1' in data:
        plot_s1_heatmap(data['s1'], config, output_dir)
        plot_s1_distribution(data['s1'], config, output_dir)
    
    plot_s2_heatmap(config, output_dir)
    plot_prime_comparison(data, config, output_dir)
    plot_null_distributions(config, output_dir)
    
    logging.info("All visualizations complete!")


if __name__ == '__main__':
    main()
