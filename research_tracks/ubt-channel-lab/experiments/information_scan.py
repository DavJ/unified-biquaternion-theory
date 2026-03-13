#!/usr/bin/env python3
"""
S4: Information Criterion

Implements I(k) = H(k) - H(k|context)

This script computes information-theoretic stability based on
mutual information and entropy.

Usage:
    python information_scan.py --config configs/scan_config.yaml
"""

import argparse
import numpy as np
import pandas as pd
import yaml
from pathlib import Path
import logging
from scipy.stats import zscore, entropy


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


def generate_field_distribution(k, config):
    """Generate field value distribution for channel k."""
    np.random.seed(config['synthetic']['random_seed'] + k * 100)
    
    n_samples = 10000
    
    # Base distribution: Gaussian with k-dependent mean and variance
    mu = k / 100.0
    sigma = 1.0 / np.sqrt(k) if k > 0 else 1.0
    
    samples = np.random.normal(mu, sigma, n_samples)
    
    # Primes have more structured distributions (lower entropy)
    if is_prime(k):
        # Add deterministic component
        samples = 0.7 * samples + 0.3 * np.sin(2 * np.pi * np.arange(n_samples) / k)
    
    return samples


def compute_entropy(samples, n_bins):
    """Compute Shannon entropy of distribution."""
    hist, _ = np.histogram(samples, bins=n_bins, density=True)
    # Normalize to probability distribution
    hist = hist / np.sum(hist)
    # Remove zeros to avoid log(0)
    hist = hist[hist > 0]
    return entropy(hist, base=2)


def compute_mutual_information(samples_k, samples_context, n_bins):
    """Compute mutual information between k and context."""
    # Create 2D histogram
    hist_2d, _, _ = np.histogram2d(samples_k, samples_context, bins=n_bins)
    hist_2d = hist_2d / np.sum(hist_2d)  # Normalize
    
    # Marginal distributions
    p_k = np.sum(hist_2d, axis=1)
    p_context = np.sum(hist_2d, axis=0)
    
    # Mutual information: I(X;Y) = Σ p(x,y) log(p(x,y) / (p(x)p(y)))
    mi = 0.0
    for i in range(n_bins):
        for j in range(n_bins):
            if hist_2d[i, j] > 0 and p_k[i] > 0 and p_context[j] > 0:
                mi += hist_2d[i, j] * np.log2(hist_2d[i, j] / (p_k[i] * p_context[j]))
    
    return mi


def run_information_scan(config):
    """Run information criterion scan."""
    logging.info("Starting S4 information criterion scan")
    
    k_min = config['scan_range']['min']
    k_max = config['scan_range']['max']
    k_values = list(range(k_min, k_max + 1))
    
    n_bins = config['information']['entropy_bins']
    context_window = config['information']['context_window']
    
    # Generate field distributions for all k
    distributions = {k: generate_field_distribution(k, config) for k in k_values}
    
    results = []
    
    for k in k_values:
        samples_k = distributions[k]
        
        # Compute entropy H(k)
        h_k = compute_entropy(samples_k, n_bins)
        
        # Compute context distribution (neighboring channels)
        context_samples = []
        for offset in range(-context_window, context_window + 1):
            k_neighbor = k + offset
            if k_neighbor != k and k_neighbor in distributions:
                context_samples.append(distributions[k_neighbor])
        
        if context_samples:
            # Average context distribution
            context_combined = np.concatenate(context_samples)
            # Sample to match size
            context_combined = np.random.choice(
                context_combined, size=len(samples_k), replace=True
            )
            
            # Mutual information I(k; context)
            mi = compute_mutual_information(samples_k, context_combined, n_bins)
            
            # Information criterion: H(k) - H(k|context) = I(k; context)
            i_k = mi
        else:
            # No context available
            i_k = h_k
        
        results.append({
            'k': k,
            'entropy': h_k,
            'mutual_information': i_k,
            'information_criterion': i_k,
            'is_prime': is_prime(k)
        })
    
    df = pd.DataFrame(results)
    
    # Compute z-scores
    df['info_zscore'] = zscore(df['information_criterion'])
    
    # Rank by information criterion (descending)
    df = df.sort_values('information_criterion', ascending=False).reset_index(drop=True)
    df['rank'] = df.index + 1
    df['percentile'] = df['rank'].apply(lambda r: (1 - r / len(df)) * 100)
    
    logging.info(f"Scan complete. Top channel: k={df.iloc[0]['k']}, I={df.iloc[0]['information_criterion']:.4f}")
    
    return df


def main():
    parser = argparse.ArgumentParser(description='S4 Information Criterion Scan')
    parser.add_argument('--config', type=str, required=True, help='Path to config YAML')
    parser.add_argument('--output', type=str, default=None, help='Output CSV path')
    parser.add_argument('--verbose', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Load config
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Run scan
    results_df = run_information_scan(config)
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        results_dir = Path(config['output']['results_dir'])
        results_dir.mkdir(exist_ok=True)
        output_path = results_dir / 's4_information_ranking.csv'
    
    # Save results
    results_df.to_csv(output_path, index=False)
    logging.info(f"Results saved to {output_path}")
    
    # Print top 10
    print("\n=== Top 10 Channels by S4 (Information Criterion) ===")
    print(results_df[['rank', 'k', 'information_criterion', 'info_zscore', 'is_prime', 'percentile']].head(10).to_string(index=False))
    
    # Compare primes vs non-primes
    prime_info = results_df[results_df['is_prime']]['information_criterion']
    non_prime_info = results_df[~results_df['is_prime']]['information_criterion']
    
    print(f"\n=== Prime vs Non-Prime Comparison ===")
    print(f"Prime mean I(k): {prime_info.mean():.4f} ± {prime_info.std():.4f}")
    print(f"Non-prime mean I(k): {non_prime_info.mean():.4f} ± {non_prime_info.std():.4f}")
    
    # Check if 137 is in dataset
    if 137 in results_df['k'].values:
        row_137 = results_df[results_df['k'] == 137].iloc[0]
        print(f"\n=== Channel 137 Performance ===")
        print(f"Rank: {row_137['rank']}")
        print(f"I(137): {row_137['information_criterion']:.4f}")
        print(f"Z-score: {row_137['info_zscore']:.4f}")
        print(f"Percentile: {row_137['percentile']:.2f}%")


if __name__ == '__main__':
    main()
