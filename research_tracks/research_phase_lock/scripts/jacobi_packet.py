#!/usr/bin/env python3
"""
jacobi_packet.py

Analyze the full Jacobi packet (k=134-143) for phase coherence patterns.

According to UBT theory, the Jacobi cluster around k≈137 represents a
special "resonance packet" in the biquaternion field. This script analyzes
phase coherence across all frequencies in this cluster.

Analysis includes:
1. Individual k coherence profiles
2. Cluster-wide coherence patterns
3. Inter-frequency phase relationships
4. Statistical significance across the packet

Usage:
    python scripts/jacobi_packet.py --config configs/grid.yaml
    python scripts/jacobi_packet.py --config configs/grid.yaml --output results/jacobi/

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

from research_phase_lock.utils.io import load_yaml, save_yaml
from research_phase_lock.adapters.phase_lock_runner import run_phase_lock_scan

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


# Define Jacobi packet frequencies
JACOBI_PACKET = list(range(134, 144))  # [134, 135, ..., 143]


def run_jacobi_analysis(config_path, output_dir=None):
    """
    Run phase lock analysis for full Jacobi packet.
    
    Args:
        config_path: Path to configuration YAML
        output_dir: Output directory (default: from config)
    """
    print("=" * 70)
    print("JACOBI PACKET ANALYSIS (k=134-143)")
    print("=" * 70)
    print(f"Config: {config_path}\n")
    
    # Load configuration
    config = load_yaml(config_path)
    
    global_config = config.get('global', {})
    data_config = config.get('data', {})
    grid_config = config.get('grid', {})
    
    if output_dir is None:
        output_dir = Path(global_config.get('output_root', 'research_phase_lock/outputs')) / 'jacobi_packet'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Output directory: {output_dir}\n")
    
    # Determine data mode
    data_mode = data_config.get('mode', 'synthetic')
    
    # Build run parameters (using first element of each grid parameter)
    run_params = {
        'projection': grid_config.get('projection', ['torus'])[0],
        'window_size': grid_config.get('window_size', [128])[0],
        'nside_out': grid_config.get('nside_out', [256])[0],
        'window': grid_config.get('window_func', ['none'])[0],
        'null': grid_config.get('null_models', ['phase-shuffle'])[0],
        'mc': grid_config.get('mc_samples', [500])[0],
    }
    
    # Generate synthetic data if needed
    if data_mode == 'synthetic':
        print("Generating synthetic data with Jacobi packet phase lock...")
        synthetic_config = data_config.get('synthetic', {})
        
        # Generate synthetic maps with all Jacobi frequencies locked
        synthetic_data = generate_jacobi_synthetic_data(
            nlat=synthetic_config.get('nlat', 512),
            nlon=synthetic_config.get('nlon', 1024),
            locked_targets=JACOBI_PACKET,
            noise_sigma=synthetic_config.get('noise_sigma', 0.1),
            phase_offset=synthetic_config.get('phase_offset_rad', 0.05),
            output_dir=output_dir
        )
        
        run_params.update({
            'tt_map': synthetic_data['tt_map'],
            'q_map': synthetic_data['q_map'],
            'u_map': synthetic_data['u_map'],
        })
    else:
        # Use Planck data
        planck_config = data_config.get('planck', {})
        run_params.update({
            'tt_map': planck_config.get('tt_map'),
            'q_map': planck_config.get('q_map'),
            'u_map': planck_config.get('u_map'),
        })
    
    # Run analysis for each frequency in Jacobi packet
    print("Running phase lock scan for each Jacobi frequency...")
    print()
    
    results = []
    
    for k in JACOBI_PACKET:
        print(f"Analyzing k={k}...")
        
        # Set target
        run_params['targets'] = f"{k}"
        run_params['output_dir'] = str(output_dir / f"k_{k}")
        
        # Run scan
        try:
            result = run_phase_lock_scan(**run_params)
            
            if result and result.get('success'):
                # Extract key metrics
                result_summary = {
                    'k': k,
                    'phase_coherence': result.get('phase_coherence'),
                    'p_value': result.get('p_value'),
                    'z_score': result.get('z_score'),
                }
                results.append(result_summary)
                print(f"  ✓ k={k}: PC={result_summary['phase_coherence']:.4f}, p={result_summary['p_value']:.4f}")
            else:
                print(f"  ✗ k={k}: Failed")
        
        except Exception as e:
            print(f"  ✗ k={k}: Error - {e}")
    
    # Save results
    print("\n" + "=" * 70)
    print("JACOBI PACKET RESULTS")
    print("=" * 70)
    
    if results:
        # Save CSV
        csv_path = output_dir / 'jacobi_packet_summary.csv'
        with open(csv_path, 'w', newline='') as f:
            fieldnames = ['k', 'phase_coherence', 'p_value', 'z_score']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        print(f"Summary saved to: {csv_path}")
        
        # Print statistics
        print("\nJacobi Packet Statistics:")
        pc_values = [r['phase_coherence'] for r in results if r['phase_coherence'] is not None]
        p_values = [r['p_value'] for r in results if r['p_value'] is not None]
        
        if pc_values:
            print(f"  Phase Coherence: mean={np.mean(pc_values):.4f}, std={np.std(pc_values):.4f}")
            print(f"  PC range: [{np.min(pc_values):.4f}, {np.max(pc_values):.4f}]")
        
        if p_values:
            n_sig = sum(1 for p in p_values if p <= 0.01)
            print(f"  Significant (p ≤ 0.01): {n_sig}/{len(p_values)}")
        
        # Create visualizations
        if HAS_MATPLOTLIB:
            print("\nGenerating visualizations...")
            plot_jacobi_spectrum(results, output_dir)
        
    else:
        print("No results generated")
    
    print("=" * 70)


def generate_jacobi_synthetic_data(nlat, nlon, locked_targets, noise_sigma, phase_offset, output_dir):
    """
    Generate synthetic HEALPix maps with Jacobi packet phase lock.
    
    Args:
        nlat: Latitude grid points
        nlon: Longitude grid points
        locked_targets: List of k values to lock
        noise_sigma: Noise level
        phase_offset: Phase offset between channels (radians)
        output_dir: Directory for output FITS files
        
    Returns:
        Dictionary with map paths
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required for synthetic data generation")
    
    nside = 256
    npix = hp.nside2npix(nside)
    
    # Initialize maps with noise
    np.random.seed(42)  # Fixed seed for reproducibility
    tt_map = np.random.randn(npix) * noise_sigma
    q_map = np.random.randn(npix) * noise_sigma
    u_map = np.random.randn(npix) * noise_sigma
    
    # Embed phase-locked signals at all Jacobi frequencies
    for k in locked_targets:
        amplitude = noise_sigma * 3.0  # Signal above noise
        
        # Simple oscillation pattern (simplified for demonstration)
        theta = np.linspace(0, 2*np.pi, npix)
        signal = amplitude * np.sin(k * theta)
        
        tt_map += signal
        q_map += signal * np.cos(phase_offset)
        u_map += signal * np.sin(phase_offset)
    
    # Save to FITS
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    tt_path = output_dir / 'synthetic_jacobi_tt.fits'
    q_path = output_dir / 'synthetic_jacobi_q.fits'
    u_path = output_dir / 'synthetic_jacobi_u.fits'
    
    hp.write_map(str(tt_path), tt_map, overwrite=True, dtype=np.float32)
    hp.write_map(str(q_path), q_map, overwrite=True, dtype=np.float32)
    hp.write_map(str(u_path), u_map, overwrite=True, dtype=np.float32)
    
    return {
        'tt_map': str(tt_path),
        'q_map': str(q_path),
        'u_map': str(u_path),
    }


def plot_jacobi_spectrum(results, output_dir):
    """
    Create visualization of Jacobi packet spectrum.
    
    Args:
        results: List of result dictionaries
        output_dir: Output directory for plots
    """
    if not HAS_MATPLOTLIB:
        return
    
    # Extract data
    k_values = [r['k'] for r in results]
    pc_values = [r['phase_coherence'] for r in results]
    p_values = [r['p_value'] for r in results]
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: Phase Coherence spectrum
    ax1.plot(k_values, pc_values, 'o-', linewidth=2, markersize=8, color='steelblue')
    ax1.axhline(y=0.5, color='red', linestyle='--', linewidth=2, alpha=0.5, label='PC = 0.5 threshold')
    ax1.set_xlabel('Frequency k', fontsize=12)
    ax1.set_ylabel('Phase Coherence', fontsize=12)
    ax1.set_title('Jacobi Packet (k=134-143) Phase Coherence Spectrum', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xticks(k_values)
    
    # Highlight twin primes
    if 137 in k_values:
        idx_137 = k_values.index(137)
        ax1.plot(137, pc_values[idx_137], 'ro', markersize=12, label='k=137 (twin prime)')
    if 139 in k_values:
        idx_139 = k_values.index(139)
        ax1.plot(139, pc_values[idx_139], 'ro', markersize=12, label='k=139 (twin prime)')
    
    # Plot 2: P-value spectrum (log scale)
    ax2.semilogy(k_values, p_values, 'o-', linewidth=2, markersize=8, color='darkgreen')
    ax2.axhline(y=0.01, color='red', linestyle='--', linewidth=2, alpha=0.5, label='p = 0.01')
    ax2.axhline(y=0.05, color='orange', linestyle='--', linewidth=2, alpha=0.5, label='p = 0.05')
    ax2.set_xlabel('Frequency k', fontsize=12)
    ax2.set_ylabel('P-value (log scale)', fontsize=12)
    ax2.set_title('Jacobi Packet Statistical Significance', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xticks(k_values)
    ax2.set_ylim([min(p_values) * 0.5, 1.0])
    
    plt.tight_layout()
    output_path = Path(output_dir) / 'jacobi_packet_spectrum.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Spectrum plot saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Jacobi Packet (k=134-143) Phase Lock Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--config',
        required=True,
        help='Path to YAML configuration file'
    )
    
    parser.add_argument(
        '--output',
        help='Output directory (default: from config)'
    )
    
    args = parser.parse_args()
    
    run_jacobi_analysis(
        config_path=args.config,
        output_dir=args.output
    )


if __name__ == '__main__':
    main()
