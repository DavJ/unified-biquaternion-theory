#!/usr/bin/env python3
"""
S1: Spectral Robustness Criterion

Implements S1(k) = peak_strength(k) - local_noise(k)

This script scans integer channels k and computes spectral stability
based on peak strength relative to local background noise.

Usage:
    python spectral_scan.py --config configs/scan_config.yaml
    python spectral_scan.py --config configs/scan_config.yaml --output results/s1.csv
"""

import argparse
import numpy as np
import pandas as pd
import yaml
from pathlib import Path
from scipy import signal
from scipy.stats import zscore
import logging


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


def generate_synthetic_spectrum(k_values, config):
    """Generate synthetic spectral data for testing."""
    np.random.seed(config['synthetic']['random_seed'])
    
    n_freq = config['spectral']['frequency_samples']
    spectrum = {}
    
    noise_level = config['synthetic']['noise_level']
    signal_strength = config['synthetic']['signal_strength']
    prime_enhancement = config['synthetic']['prime_enhancement']
    
    for k in k_values:
        # Base signal: sinusoidal with noise
        freqs = np.linspace(0, 10, n_freq)
        base_signal = signal_strength * np.sin(2 * np.pi * k / 100 * freqs)
        
        # Add noise
        noise = noise_level * np.random.randn(n_freq)
        
        # Enhance primes (if enabled)
        if is_prime(k) and prime_enhancement > 0:
            base_signal *= (1 + prime_enhancement)
        
        spectrum[k] = base_signal + noise
    
    return spectrum


def load_spectrum(config):
    """Load spectrum from file or generate synthetic."""
    external_file = config['data'].get('external_spectrum')
    
    if external_file and Path(external_file).exists():
        logging.info(f"Loading external spectrum from {external_file}")
        data = np.load(external_file, allow_pickle=True).item()
        return data
    else:
        logging.info("Generating synthetic spectrum")
        k_min = config['scan_range']['min']
        k_max = config['scan_range']['max']
        k_values = range(k_min, k_max + 1)
        return generate_synthetic_spectrum(k_values, config)


def compute_peak_strength(spectrum_k):
    """Compute peak strength for channel k."""
    return np.max(np.abs(spectrum_k))


def compute_local_noise(spectrum, k, noise_window):
    """Compute local noise around channel k."""
    k_values = sorted(spectrum.keys())
    idx = k_values.index(k)
    
    # Get neighbors within window
    start_idx = max(0, idx - noise_window)
    end_idx = min(len(k_values), idx + noise_window + 1)
    
    neighbor_keys = [k_values[i] for i in range(start_idx, end_idx) if k_values[i] != k]
    
    if not neighbor_keys:
        return 0.0
    
    # Compute standard deviation of neighboring spectra
    neighbor_powers = [np.std(spectrum[k_n]) for k_n in neighbor_keys]
    return np.mean(neighbor_powers)


def compute_s1(k, spectrum, config):
    """Compute S1(k) = peak_strength(k) - local_noise(k)."""
    noise_window = config['spectral']['noise_window']
    
    peak = compute_peak_strength(spectrum[k])
    noise = compute_local_noise(spectrum, k, noise_window)
    
    s1 = peak - noise
    return s1


def run_spectral_scan(config):
    """Run full spectral scan and return results."""
    logging.info("Starting S1 spectral robustness scan")
    
    # Load or generate spectrum
    spectrum = load_spectrum(config)
    
    # Scan all channels
    results = []
    k_values = sorted(spectrum.keys())
    
    for k in k_values:
        s1 = compute_s1(k, spectrum, config)
        
        results.append({
            'k': k,
            's1': s1,
            'peak_strength': compute_peak_strength(spectrum[k]),
            'local_noise': compute_local_noise(spectrum, k, config['spectral']['noise_window']),
            'is_prime': is_prime(k)
        })
    
    df = pd.DataFrame(results)
    
    # Compute z-scores
    df['s1_zscore'] = zscore(df['s1'])
    
    # Rank by S1
    df = df.sort_values('s1', ascending=False).reset_index(drop=True)
    df['rank'] = df.index + 1
    
    # Compute percentile
    df['percentile'] = df['rank'].apply(lambda r: (1 - r / len(df)) * 100)
    
    logging.info(f"Scan complete. Top channel: k={df.iloc[0]['k']}, S1={df.iloc[0]['s1']:.4f}")
    
    return df


def main():
    parser = argparse.ArgumentParser(description='S1 Spectral Robustness Scan')
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
    results_df = run_spectral_scan(config)
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        results_dir = Path(config['output']['results_dir'])
        results_dir.mkdir(exist_ok=True)
        output_path = results_dir / 's1_ranking.csv'
    
    # Save results
    results_df.to_csv(output_path, index=False)
    logging.info(f"Results saved to {output_path}")
    
    # Print top 10
    print("\n=== Top 10 Channels by S1 (Spectral Robustness) ===")
    print(results_df[['rank', 'k', 's1', 's1_zscore', 'is_prime', 'percentile']].head(10).to_string(index=False))
    
    # Check if 137 is in dataset
    if 137 in results_df['k'].values:
        row_137 = results_df[results_df['k'] == 137].iloc[0]
        print(f"\n=== Channel 137 Performance ===")
        print(f"Rank: {row_137['rank']}")
        print(f"S1: {row_137['s1']:.4f}")
        print(f"Z-score: {row_137['s1_zscore']:.4f}")
        print(f"Percentile: {row_137['percentile']:.2f}%")


if __name__ == '__main__':
    main()
