#!/usr/bin/env python3
"""
S3: Energy Criterion

Implements E(k) = ∫ |∇Θ_k|² dV

This script computes energy-based stability via discrete Laplacian
approximation and detects local minima.

Usage:
    python energy_scan.py --config configs/scan_config.yaml
"""

import argparse
import numpy as np
import pandas as pd
import yaml
from pathlib import Path
import logging
from scipy.stats import zscore
from scipy import integrate


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


def generate_field_configuration(k, config):
    """Generate field configuration Θ_k on a discrete grid."""
    np.random.seed(config['synthetic']['random_seed'] + k * 10)
    
    grid_res = config['energy']['grid_resolution']
    
    # 1D spatial grid for simplicity (can extend to 3D)
    x = np.linspace(0, 2 * np.pi, grid_res)
    
    # Field configuration: complex-valued with k-dependent structure
    # In real UBT, this would be a biquaternion (8 real components)
    # We simplify to complex scalar field
    
    # Base mode: sinusoidal with k-dependent frequency
    field = np.sin(k * x / 10) + 1j * np.cos(k * x / 10)
    
    # Add noise
    noise = config['synthetic']['noise_level'] * (
        np.random.randn(grid_res) + 1j * np.random.randn(grid_res)
    )
    field += noise
    
    # Prime enhancement (structural stability)
    if is_prime(k):
        # Primes have smoother field configurations (less noise)
        field = 0.9 * field + 0.1 * np.sin(k * x / 10)
    
    return field, x


def compute_energy(field, dx):
    """Compute E(k) = ∫ |∇Θ_k|² dx."""
    # Discrete gradient via finite differences
    grad_field = np.gradient(field, dx)
    
    # Energy density: |∇Θ|²
    energy_density = np.abs(grad_field) ** 2
    
    # Integrate over space using Simpson's rule
    total_energy = integrate.simpson(energy_density, dx=dx)
    
    return total_energy


def is_local_minimum(energies, idx):
    """Check if energy at idx is a local minimum."""
    if idx == 0 or idx == len(energies) - 1:
        return False
    
    return energies[idx] < energies[idx - 1] and energies[idx] < energies[idx + 1]


def run_energy_scan(config):
    """Run energy criterion scan."""
    logging.info("Starting S3 energy criterion scan")
    
    k_min = config['scan_range']['min']
    k_max = config['scan_range']['max']
    k_values = list(range(k_min, k_max + 1))
    
    results = []
    energies = []
    
    for k in k_values:
        # Generate field configuration
        field, x = generate_field_configuration(k, config)
        dx = x[1] - x[0]
        
        # Compute energy
        energy = compute_energy(field, dx)
        energies.append(energy)
        
        results.append({
            'k': k,
            'energy': energy,
            'is_prime': is_prime(k)
        })
    
    # Detect local minima
    for i, result in enumerate(results):
        result['is_local_minimum'] = is_local_minimum(energies, i)
    
    df = pd.DataFrame(results)
    
    # Compute inverse energy for ranking (lower energy = higher stability)
    # Use 1/E for ranking purposes
    df['inv_energy'] = 1.0 / df['energy']
    df['energy_zscore'] = zscore(df['energy'])
    
    # Rank by energy (ascending)
    df = df.sort_values('energy', ascending=True).reset_index(drop=True)
    df['rank'] = df.index + 1
    df['percentile'] = df['rank'].apply(lambda r: (1 - r / len(df)) * 100)
    
    # Statistics
    n_minima = df['is_local_minimum'].sum()
    n_prime_minima = df[df['is_prime'] & df['is_local_minimum']].shape[0]
    n_primes = df['is_prime'].sum()
    
    logging.info(f"Total local minima: {n_minima}")
    logging.info(f"Prime local minima: {n_prime_minima} / {n_primes} primes")
    
    return df


def main():
    parser = argparse.ArgumentParser(description='S3 Energy Criterion Scan')
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
    results_df = run_energy_scan(config)
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        results_dir = Path(config['output']['results_dir'])
        results_dir.mkdir(exist_ok=True)
        output_path = results_dir / 's3_energy_ranking.csv'
    
    # Save results
    results_df.to_csv(output_path, index=False)
    logging.info(f"Results saved to {output_path}")
    
    # Print top 10 (lowest energy)
    print("\n=== Top 10 Channels by S3 (Energy Minima) ===")
    print(results_df[['rank', 'k', 'energy', 'is_local_minimum', 'is_prime', 'percentile']].head(10).to_string(index=False))
    
    # Print local minima that are primes
    prime_minima = results_df[results_df['is_prime'] & results_df['is_local_minimum']]
    if not prime_minima.empty:
        print(f"\n=== Prime Local Energy Minima ({len(prime_minima)} found) ===")
        print(prime_minima[['rank', 'k', 'energy', 'percentile']].to_string(index=False))
    
    # Check if 137 is in dataset
    if 137 in results_df['k'].values:
        row_137 = results_df[results_df['k'] == 137].iloc[0]
        print(f"\n=== Channel 137 Performance ===")
        print(f"Rank: {row_137['rank']}")
        print(f"Energy: {row_137['energy']:.6f}")
        print(f"Is Local Minimum: {row_137['is_local_minimum']}")
        print(f"Percentile: {row_137['percentile']:.2f}%")


if __name__ == '__main__':
    main()
