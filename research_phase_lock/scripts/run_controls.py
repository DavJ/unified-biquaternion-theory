#!/usr/bin/env python3
"""
run_controls.py

Execute control experiments (negative and positive controls) to validate
the phase-lock analysis pipeline.

Negative controls test for false positives (should NOT show phase lock).
Positive controls test for false negatives (should DEFINITELY show phase lock).

Usage:
    python scripts/run_controls.py --config configs/controls.yaml
    python scripts/run_controls.py --config configs/controls.yaml --type negative
    python scripts/run_controls.py --config configs/controls.yaml --type positive

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import sys
from pathlib import Path
import numpy as np

# Add parent directory to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from research_phase_lock.utils.io import load_yaml, save_yaml, make_output_dir
from research_phase_lock.utils.hashing import generate_run_id
from research_phase_lock.adapters.phase_lock_runner import run_phase_lock_scan


def generate_synthetic_control(params, control_type, replicate_id):
    """
    Generate synthetic data for control experiment.
    
    Args:
        params: Control experiment parameters
        control_type: "negative" or "positive"
        replicate_id: Replicate number for unique seeding
        
    Returns:
        Dictionary with synthetic map paths
    """
    import tempfile
    try:
        import healpy as hp
    except ImportError:
        print("WARNING: healpy not available, using mock data")
        hp = None
    
    nlat = params.get('nlat', 512)
    nlon = params.get('nlon', 1024)
    noise_sigma = params.get('noise_sigma', 1.0)
    locked_targets = params.get('locked_targets', [])
    phase_offset = params.get('phase_offset_rad', 0.0)
    lock_strength = params.get('lock_strength', 1.0)
    
    # Set seed for reproducibility
    seed = params.get('seed', 0) + replicate_id * 1000
    np.random.seed(seed)
    
    # Generate synthetic HEALPix maps
    if hp is not None:
        nside = 256  # Default resolution
        npix = hp.nside2npix(nside)
        
        # Generate TT map (scalar channel)
        tt_map = np.random.randn(npix) * noise_sigma
        
        # Generate Q/U maps (polarization)
        q_map = np.random.randn(npix) * noise_sigma
        u_map = np.random.randn(npix) * noise_sigma
        
        # For positive controls, embed phase-locked signals
        if control_type == "positive" and locked_targets:
            # Create phase-locked oscillations at target frequencies
            for k in locked_targets:
                # Generate phase-locked pattern in Fourier space
                # This is a simplified embedding - real implementation would be more sophisticated
                amplitude = lock_strength * noise_sigma * 5.0  # Signal above noise
                
                # Add coherent oscillation (simplified)
                # In real implementation, this would involve proper spherical harmonics
                theta = np.linspace(0, 2*np.pi, npix)
                signal = amplitude * np.sin(k * theta + phase_offset)
                
                tt_map += signal
                # BB channel gets same signal with controlled phase offset
                q_map += signal * np.cos(phase_offset)
                u_map += signal * np.sin(phase_offset)
        
        # Save to temporary FITS files
        tmp_dir = tempfile.mkdtemp(prefix="control_")
        tt_path = Path(tmp_dir) / "tt_control.fits"
        q_path = Path(tmp_dir) / "q_control.fits"
        u_path = Path(tmp_dir) / "u_control.fits"
        
        hp.write_map(str(tt_path), tt_map, overwrite=True, dtype=np.float32)
        hp.write_map(str(q_path), q_map, overwrite=True, dtype=np.float32)
        hp.write_map(str(u_path), u_map, overwrite=True, dtype=np.float32)
        
        return {
            'tt_map': str(tt_path),
            'q_map': str(q_path),
            'u_map': str(u_path),
            'temp_dir': tmp_dir
        }
    else:
        # Fallback: return None if healpy not available
        return None


def run_control_experiment(control_name, control_config, control_type, global_config, output_root):
    """
    Run a single control experiment with multiple replicates.
    
    Args:
        control_name: Name of the control experiment
        control_config: Configuration for this control
        control_type: "negative" or "positive"
        global_config: Global configuration settings
        output_root: Root directory for outputs
    """
    if not control_config.get('enabled', True):
        print(f"Skipping disabled control: {control_name}")
        return
    
    description = control_config.get('description', 'No description')
    n_replicates = control_config.get('n_replicates', 1)
    params = control_config.get('params', {})
    grid = control_config.get('grid', {})
    
    print(f"\nRunning {control_type} control: {control_name}")
    print(f"Description: {description}")
    print(f"Replicates: {n_replicates}")
    
    results = []
    
    for rep in range(n_replicates):
        print(f"  Replicate {rep + 1}/{n_replicates}...")
        
        # Generate synthetic data for this replicate
        synthetic_data = generate_synthetic_control(params, control_type, rep)
        
        if synthetic_data is None:
            print("  ERROR: Could not generate synthetic data (healpy not available)")
            continue
        
        # Build run configuration
        run_config = {
            'control_name': control_name,
            'control_type': control_type,
            'replicate': rep,
            'params': params,
            'grid': grid,
        }
        
        # Generate unique run ID
        run_id = generate_run_id(run_config)
        
        # Create output directory
        run_output_dir = Path(output_root) / f"{control_type}_controls" / control_name / f"rep_{rep:03d}"
        run_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save configuration
        config_path = run_output_dir / "config.yaml"
        save_yaml(run_config, config_path)
        
        # Run phase lock scan
        try:
            # Build command arguments for phase_lock_scan
            scan_args = {
                'tt_map': synthetic_data['tt_map'],
                'q_map': synthetic_data['q_map'],
                'u_map': synthetic_data['u_map'],
                'targets': grid.get('targets', ['137,139'])[0],
                'projection': grid.get('projection', ['torus'])[0],
                'window_size': grid.get('window_size', [128])[0],
                'nside_out': grid.get('nside_out', [256])[0],
                'window': grid.get('window_func', ['none'])[0],
                'null': grid.get('null_models', ['phase-shuffle'])[0],
                'mc': grid.get('mc_samples', [500])[0],
                'output_dir': str(run_output_dir),
            }
            
            # Run the scan
            result = run_phase_lock_scan(**scan_args)
            
            if result and result.get('success'):
                results.append({
                    'control_name': control_name,
                    'replicate': rep,
                    'run_id': run_id,
                    'output_dir': str(run_output_dir),
                    **result
                })
                print(f"  ✓ Success")
            else:
                print(f"  ✗ Failed")
        
        except Exception as e:
            print(f"  ✗ Error: {e}")
        
        # Cleanup temporary files
        if synthetic_data and 'temp_dir' in synthetic_data:
            import shutil
            try:
                shutil.rmtree(synthetic_data['temp_dir'])
            except:
                pass
    
    return results


def run_controls(config_path, control_type=None):
    """
    Run control experiments from configuration file.
    
    Args:
        config_path: Path to controls YAML configuration
        control_type: Run only "negative" or "positive" controls (None = both)
    """
    print("=" * 70)
    print("CONTROL EXPERIMENTS RUNNER")
    print("=" * 70)
    print(f"Config: {config_path}\n")
    
    # Load configuration
    config = load_yaml(config_path)
    
    global_config = config.get('global', {})
    output_root = global_config.get('output_root', 'research_phase_lock/outputs/controls')
    
    # Create output directory
    Path(output_root).mkdir(parents=True, exist_ok=True)
    
    all_results = []
    
    # Run negative controls
    if control_type is None or control_type == 'negative':
        print("\n" + "=" * 70)
        print("NEGATIVE CONTROLS (should NOT show phase lock)")
        print("=" * 70)
        
        neg_controls = config.get('negative_controls', {})
        for control_name, control_config in neg_controls.items():
            if isinstance(control_config, dict):
                results = run_control_experiment(
                    control_name, control_config, 'negative', global_config, output_root
                )
                if results:
                    all_results.extend(results)
    
    # Run positive controls
    if control_type is None or control_type == 'positive':
        print("\n" + "=" * 70)
        print("POSITIVE CONTROLS (should DEFINITELY show phase lock)")
        print("=" * 70)
        
        pos_controls = config.get('positive_controls', {})
        for control_name, control_config in pos_controls.items():
            if isinstance(control_config, dict):
                results = run_control_experiment(
                    control_name, control_config, 'positive', global_config, output_root
                )
                if results:
                    all_results.extend(results)
    
    # Save summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total control runs: {len(all_results)}")
    
    output_config = config.get('output', {})
    if output_config.get('generate_summary', True):
        summary_path = Path(output_config.get('summary_path', f'{output_root}/summary.csv'))
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write CSV summary
        import csv
        with open(summary_path, 'w', newline='') as f:
            if all_results:
                writer = csv.DictWriter(f, fieldnames=all_results[0].keys())
                writer.writeheader()
                writer.writerows(all_results)
        
        print(f"Summary saved to: {summary_path}")
    
    print("=" * 70)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Control Experiments Runner for Phase-Lock Validation",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--config',
        required=True,
        help='Path to controls YAML configuration file'
    )
    
    parser.add_argument(
        '--type',
        choices=['negative', 'positive'],
        help='Run only negative or positive controls (omit for both)'
    )
    
    args = parser.parse_args()
    
    run_controls(
        config_path=args.config,
        control_type=args.type
    )


if __name__ == '__main__':
    main()
