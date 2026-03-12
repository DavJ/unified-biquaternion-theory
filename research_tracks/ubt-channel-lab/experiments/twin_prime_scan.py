#!/usr/bin/env python3
"""
S2: Twin Prime Coherence Criterion

Implements S2(k1, k2) = S1(k1) + S1(k2) + phase_coherence(k1, k2)

This script scans all twin prime pairs and evaluates their combined
stability and phase coherence.

Usage:
    python twin_prime_scan.py --config configs/scan_config.yaml
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


def find_twin_primes(k_min, k_max, gap=2):
    """Find all twin prime pairs in range."""
    twin_pairs = []
    for k1 in range(k_min, k_max + 1):
        k2 = k1 + gap
        if k2 <= k_max and is_prime(k1) and is_prime(k2):
            twin_pairs.append((k1, k2))
    return twin_pairs


def load_s1_results(config):
    """Load S1 results from previous scan."""
    results_dir = Path(config['output']['results_dir'])
    s1_file = results_dir / 's1_ranking.csv'
    
    if not s1_file.exists():
        raise FileNotFoundError(
            f"S1 results not found at {s1_file}. "
            "Please run spectral_scan.py first."
        )
    
    df = pd.read_csv(s1_file)
    s1_dict = dict(zip(df['k'], df['s1']))
    return s1_dict


def generate_synthetic_field(k, config):
    """Generate synthetic field configuration for channel k."""
    np.random.seed(config['synthetic']['random_seed'] + k)
    
    n_samples = config['twin_prime']['phase_samples']
    
    # Simple phase-space representation
    # Real biquaternions would be 8-dimensional, we simplify to 4D
    field = np.random.randn(n_samples, 4) + 1j * np.random.randn(n_samples, 4)
    
    # Add prime-dependent structure
    if is_prime(k):
        phase_factor = np.exp(2j * np.pi * k / 137)  # Reference to fine structure
        field *= phase_factor
    
    return field


def compute_phase_coherence(field_k1, field_k2):
    """Compute phase coherence between two field configurations."""
    # Flatten to vectors
    vec1 = field_k1.flatten()
    vec2 = field_k2.flatten()
    
    # Normalized inner product (complex)
    inner_prod = np.vdot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    coherence = np.abs(inner_prod) / (norm1 * norm2)
    return coherence


def compute_s2(k1, k2, s1_dict, config):
    """Compute S2(k1, k2) = S1(k1) + S1(k2) + phase_coherence(k1, k2)."""
    s1_k1 = s1_dict.get(k1, 0.0)
    s1_k2 = s1_dict.get(k2, 0.0)
    
    # Generate field configurations
    field_k1 = generate_synthetic_field(k1, config)
    field_k2 = generate_synthetic_field(k2, config)
    
    # Compute phase coherence
    coherence = compute_phase_coherence(field_k1, field_k2)
    
    # Combined stability
    s2 = s1_k1 + s1_k2 + coherence
    
    return s2, coherence


def run_twin_prime_scan(config):
    """Run twin prime coherence scan."""
    logging.info("Starting S2 twin prime coherence scan")
    
    # Load S1 results
    s1_dict = load_s1_results(config)
    
    # Find all twin prime pairs
    k_min = config['scan_range']['min']
    k_max = config['scan_range']['max']
    twin_prime_gap = config['primes']['twin_prime_max_gap']
    
    twin_pairs = find_twin_primes(k_min, k_max, gap=twin_prime_gap)
    logging.info(f"Found {len(twin_pairs)} twin prime pairs")
    
    # Scan all pairs
    results = []
    for k1, k2 in twin_pairs:
        s2, coherence = compute_s2(k1, k2, s1_dict, config)
        
        results.append({
            'k1': k1,
            'k2': k2,
            'pair': f"({k1}, {k2})",
            's1_k1': s1_dict.get(k1, 0.0),
            's1_k2': s1_dict.get(k2, 0.0),
            'phase_coherence': coherence,
            's2': s2
        })
    
    if not results:
        logging.warning("No twin prime pairs found in range!")
        return pd.DataFrame()
    
    df = pd.DataFrame(results)
    
    # Compute z-scores
    df['s2_zscore'] = zscore(df['s2'])
    df['coherence_zscore'] = zscore(df['phase_coherence'])
    
    # Rank by S2
    df = df.sort_values('s2', ascending=False).reset_index(drop=True)
    df['rank'] = df.index + 1
    df['percentile'] = df['rank'].apply(lambda r: (1 - r / len(df)) * 100)
    
    logging.info(f"Scan complete. Top pair: {df.iloc[0]['pair']}, S2={df.iloc[0]['s2']:.4f}")
    
    return df


def create_heatmap_matrix(config):
    """Create heatmap matrix for all pairs (not just twin primes)."""
    logging.info("Creating full S2 heatmap matrix")
    
    s1_dict = load_s1_results(config)
    k_values = sorted(s1_dict.keys())
    
    n = len(k_values)
    matrix = np.zeros((n, n))
    
    for i, k1 in enumerate(k_values):
        for j, k2 in enumerate(k_values):
            if i < j:  # Only compute upper triangle
                s2, _ = compute_s2(k1, k2, s1_dict, config)
                matrix[i, j] = s2
                matrix[j, i] = s2  # Symmetric
    
    return matrix, k_values


def main():
    parser = argparse.ArgumentParser(description='S2 Twin Prime Coherence Scan')
    parser.add_argument('--config', type=str, required=True, help='Path to config YAML')
    parser.add_argument('--output', type=str, default=None, help='Output CSV path')
    parser.add_argument('--heatmap', action='store_true', help='Generate full heatmap matrix')
    parser.add_argument('--verbose', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Load config
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Run scan
    results_df = run_twin_prime_scan(config)
    
    if results_df.empty:
        logging.error("No results generated. Exiting.")
        return
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        results_dir = Path(config['output']['results_dir'])
        results_dir.mkdir(exist_ok=True)
        output_path = results_dir / 's2_twin_prime_ranking.csv'
    
    # Save results
    results_df.to_csv(output_path, index=False)
    logging.info(f"Results saved to {output_path}")
    
    # Print top 10
    print("\n=== Top 10 Twin Prime Pairs by S2 (Coherence) ===")
    print(results_df[['rank', 'pair', 's2', 's2_zscore', 'phase_coherence', 'percentile']].head(10).to_string(index=False))
    
    # Check for (137, 139)
    pair_137_139 = results_df[(results_df['k1'] == 137) & (results_df['k2'] == 139)]
    if not pair_137_139.empty:
        row = pair_137_139.iloc[0]
        print(f"\n=== (137, 139) Performance ===")
        print(f"Rank: {row['rank']}")
        print(f"S2: {row['s2']:.4f}")
        print(f"Z-score: {row['s2_zscore']:.4f}")
        print(f"Phase Coherence: {row['phase_coherence']:.4f}")
        print(f"Percentile: {row['percentile']:.2f}%")
    
    # Generate heatmap matrix if requested
    if args.heatmap:
        logging.info("Generating heatmap matrix (this may take time)")
        matrix, k_values = create_heatmap_matrix(config)
        
        results_dir = Path(config['output']['results_dir'])
        np.save(results_dir / 's2_heatmap_matrix.npy', matrix)
        np.save(results_dir / 's2_heatmap_kvalues.npy', k_values)
        logging.info(f"Heatmap matrix saved to {results_dir}")


if __name__ == '__main__':
    main()
