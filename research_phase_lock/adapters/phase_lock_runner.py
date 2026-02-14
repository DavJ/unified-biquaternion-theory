#!/usr/bin/env python3
"""
phase_lock_runner.py

Adapter for calling forensic_fingerprint.tools.unified_phase_lock_scan.

This module provides a high-level interface for invoking the unified phase-lock
scan tool with different parameter combinations. It handles:
- Command-line argument construction
- Synthetic vs. Planck data mode
- Output file management
- Error handling and logging

CRITICAL: This module does NOT modify the unified_phase_lock_scan tool.
It only wraps calls to the existing tool.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add parent directory to path for imports
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from research_phase_lock.utils.subprocess import run_python_module
from research_phase_lock.utils.io import ensure_dir


def create_synthetic_maps(
    nlat: int,
    nlon: int,
    locked_targets: List[int],
    noise_sigma: float,
    phase_offset_rad: float,
    output_dir: str,
    seed: int = 42
) -> Dict[str, str]:
    """
    Create synthetic HEALPix maps with embedded phase-locked signals.
    
    This creates simple synthetic data for testing without requiring Planck data.
    The synthetic maps have coherent waves at specified k values.
    
    Args:
        nlat: Latitude grid size
        nlon: Longitude grid size
        locked_targets: k values to embed coherent signals
        noise_sigma: Noise level
        phase_offset_rad: Phase offset between channels
        output_dir: Directory to save FITS files
        seed: Random seed
        
    Returns:
        Dictionary with keys 'tt', 'q', 'u' mapping to FITS file paths
    """
    import numpy as np
    
    # For synthetic mode, we create minimal FITS-like arrays
    # The actual unified_phase_lock_scan tool will handle the projection
    # We just need to provide map files
    
    # For now, create dummy placeholder files
    # In a real implementation, this would use healpy to create proper maps
    
    ensure_dir(os.path.join(output_dir, "dummy"))
    
    # Create simple text files as placeholders
    # The actual tool expects FITS files, so we'll need to use real FITS
    # For synthetic mode, we can create minimal HEALPix maps
    
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy is required for synthetic map generation")
    
    # Create minimal HEALPix maps at nside=64 (12288 pixels)
    nside = 64
    npix = hp.nside2npix(nside)
    
    np.random.seed(seed)
    
    # TT map: noise + signal
    tt_map = np.random.randn(npix) * noise_sigma
    
    # Q, U maps: noise + phase-locked signal
    q_map = np.random.randn(npix) * noise_sigma
    u_map = np.random.randn(npix) * noise_sigma
    
    # Add coherent signal at locked targets
    # (Simplified: in real case, would add proper spherical harmonic modes)
    for k in locked_targets:
        # Add a simple coherent pattern
        signal = np.sin(np.arange(npix) * k * 0.01 + phase_offset_rad)
        tt_map += signal * 0.1
        q_map += signal * 0.05
        u_map += signal * 0.05
    
    # Write FITS files
    tt_path = os.path.join(output_dir, "synthetic_tt.fits")
    q_path = os.path.join(output_dir, "synthetic_q.fits")
    u_path = os.path.join(output_dir, "synthetic_u.fits")
    
    hp.write_map(tt_path, tt_map, overwrite=True, dtype=np.float32)
    hp.write_map(q_path, q_map, overwrite=True, dtype=np.float32)
    hp.write_map(u_path, u_map, overwrite=True, dtype=np.float32)
    
    return {
        'tt': tt_path,
        'q': q_path,
        'u': u_path
    }


def run_phase_lock_scan(
    config: Dict[str, Any],
    output_dir: str,
    data_mode: str = "planck",
    data_config: Optional[Dict[str, Any]] = None,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Run unified_phase_lock_scan with specified configuration.
    
    Args:
        config: Parameter configuration (projection, window, etc.)
        output_dir: Directory for output files
        data_mode: "planck" or "synthetic"
        data_config: Data-specific configuration (maps, synthetic params)
        verbose: Whether to print progress
        
    Returns:
        Dictionary with run status and output paths
        
    Raises:
        RuntimeError: If scan fails
    """
    ensure_dir(output_dir)
    
    # Build command-line arguments
    args = []
    
    # Handle data mode
    if data_mode == "synthetic":
        if not data_config:
            raise ValueError("data_config required for synthetic mode")
        
        # Create synthetic maps
        if verbose:
            print(f"[phase_lock_runner] Creating synthetic maps...")
        
        maps = create_synthetic_maps(
            nlat=data_config.get('nlat', 256),
            nlon=data_config.get('nlon', 512),
            locked_targets=data_config.get('locked_targets', [137, 139]),
            noise_sigma=data_config.get('noise_sigma', 0.1),
            phase_offset_rad=data_config.get('phase_offset_rad', 0.1),
            output_dir=output_dir,
            seed=data_config.get('seed', 42)
        )
        
        args.extend(['--tt-map', maps['tt']])
        args.extend(['--q-map', maps['q']])
        args.extend(['--u-map', maps['u']])
        
    elif data_mode == "planck":
        if not data_config:
            raise ValueError("data_config required for planck mode")
        
        # Use provided Planck maps
        if 'tt_map' not in data_config:
            raise ValueError("tt_map required in data_config for planck mode")
        
        args.extend(['--tt-map', data_config['tt_map']])
        args.extend(['--q-map', data_config.get('q_map', data_config['tt_map'])])
        args.extend(['--u-map', data_config.get('u_map', data_config['tt_map'])])
        
    else:
        raise ValueError(f"Unknown data_mode: {data_mode}")
    
    # Add scan parameters
    if 'targets' in config:
        args.extend(['--targets', config['targets']])
    
    if 'projection' in config:
        args.extend(['--projection', config['projection']])
    
    if 'window' in config:
        args.extend(['--window', config['window']])
    
    if 'window_size' in config:
        args.extend(['--window-size', str(config['window_size'])])
    
    if 'nside_out' in config:
        args.extend(['--nside-out', str(config['nside_out'])])
    
    if 'nlat' in config:
        args.extend(['--nlat', str(config['nlat'])])
    
    if 'nlon' in config:
        args.extend(['--nlon', str(config['nlon'])])
    
    # Handle both 'null' and 'null_method' for backwards compatibility
    null_method = config.get('null_method', config.get('null'))
    if null_method:
        args.extend(['--null', null_method])
    
    if 'mc' in config:
        args.extend(['--mc', str(config['mc'])])
    
    if 'seed' in config:
        args.extend(['--seed', str(config['seed'])])
    
    # Output files
    report_csv = os.path.join(output_dir, "phase_lock_results.csv")
    full_csv = os.path.join(output_dir, "phase_lock_full_spectrum.csv")
    plot_png = os.path.join(output_dir, "phase_lock_plot.png")
    
    args.extend(['--report-csv', report_csv])
    args.extend(['--dump-full-csv', full_csv])
    args.extend(['--plot', plot_png])
    
    # Run the tool
    if verbose:
        print(f"[phase_lock_runner] Running unified_phase_lock_scan...")
        print(f"[phase_lock_runner] Output: {output_dir}")
    
    try:
        returncode, stdout, stderr = run_python_module(
            'forensic_fingerprint.tools.unified_phase_lock_scan',
            args,
            cwd=str(repo_root),
            verbose=verbose
        )
        
        if returncode != 0:
            raise RuntimeError(f"unified_phase_lock_scan failed with exit code {returncode}\nStderr: {stderr}")
        
        return {
            'status': 'success',
            'report_csv': report_csv,
            'full_csv': full_csv,
            'plot_png': plot_png,
            'stdout': stdout,
            'stderr': stderr
        }
        
    except Exception as e:
        if verbose:
            print(f"[phase_lock_runner] ERROR: {e}")
        raise
