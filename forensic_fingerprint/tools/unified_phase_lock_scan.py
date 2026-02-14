#!/usr/bin/env python3
"""
unified_phase_lock_scan.py

Unified Phase-Lock Scan for UBT CMB Verification.

Implements segment-based cross-channel phase coherence analysis to verify
the hypothesis that TT (scalar Θ̃_S) and BB (spinor Θ_V) channels are
phase-locked as predicted by the Unified Biquaternion Theory equation:
    D(∂μ, ∂τ)Θ = 0

According to UBT:
- TT channel (k≈137): Dispersive imaginary scalar sector (Jacobi cluster 134-143)
- BB channel (k≈139): Spinor/biquaternion vector sector

If the universe is a "biquaternion machine", the phase difference between
these channels at frequencies 137/139 should NOT be random.

Method:
1. Segmentation: Divide toroidal projection into N identical W×W windows
2. FFT: Compute 2D FFT (without windowing as --window none) for both channels
3. Cross-Spectrum: For each segment and frequency k, compute S_xy = X·Y*
4. Phase Coherence (PC): PC = |mean(normalized_cross_spectrum)| across segments
5. Monte Carlo: Validate via phase-shuffle null model

The PC metric ranges from 0 (random phases) to 1 (perfect phase lock).

Usage:
    python -m forensic_fingerprint.tools.unified_phase_lock_scan \\
        --tt-map data/planck_pr3_tt.fits \\
        --q-map data/planck_pr3_q.fits \\
        --u-map data/planck_pr3_u.fits \\
        --targets 137,139 \\
        --window-size 128 \\
        --window none \\
        --mc 1000 \\
        --report-csv results/phase_lock.csv \\
        --plot results/phase_lock.png

Author: UBT Team (implementation of David Jaroš's theoretical framework)
License: See repository LICENSE.md
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np

try:
    import healpy as hp
except ImportError:
    hp = None  # type: ignore


# -------------------------
# Helper Functions
# -------------------------

def _parse_list_csv(s: str) -> List[str]:
    """Parse comma-separated list."""
    return [x.strip() for x in (s or "").split(",") if x.strip()]


def _parse_ints_csv(s: str) -> List[int]:
    """Parse comma-separated integers."""
    return [int(tok) for tok in _parse_list_csv(s)]


def _ensure_dir_for(path: Optional[str]) -> None:
    """Create directory for file path if needed."""
    if not path:
        return
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)


def _ud_grade(m: np.ndarray, nside_out: int) -> np.ndarray:
    """Degrade or upgrade HEALPix map to target nside."""
    if hp is None:
        raise ImportError("healpy is required")
    nside_in = hp.get_nside(m)
    if nside_out == nside_in:
        return m
    return hp.ud_grade(m, nside_out, order_in="RING", order_out="RING", power=0)


def _map2alm_spin_compat(qu_maps, spin: int, lmax: int):
    """Compatibility wrapper for healpy map2alm_spin across versions."""
    if hp is None:
        raise ImportError("healpy is required")
    
    attempts = [
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax),
    ]
    for fn in attempts:
        try:
            return fn()
        except TypeError:
            continue
    return hp.map2alm_spin(qu_maps, spin, lmax)


def _window_1d(name: str, n: int) -> np.ndarray:
    """Create 1D window function."""
    name = (name or "none").lower()
    if name in ("none", "rect", "boxcar"):
        return np.ones(n, dtype=float)
    if name in ("hann", "hanning"):
        return np.hanning(n).astype(float)
    if name == "hamming":
        return np.hamming(n).astype(float)
    if name == "blackman":
        return np.blackman(n).astype(float)
    raise ValueError(f"Unknown window: {name}")


def _window_2d(name: str, ny: int, nx: int, normalize_rms: bool = True) -> np.ndarray:
    """Create 2D window function."""
    wy = _window_1d(name, ny)
    wx = _window_1d(name, nx)
    w = wy[:, None] * wx[None, :]
    if normalize_rms:
        rms = math.sqrt(float(np.mean(w**2)))
        if rms > 0:
            w = w / rms
    return w


def _project_to_equirect(m: np.ndarray, nlat: int, nlon: int) -> np.ndarray:
    """Project HEALPix map to equirectangular grid."""
    if hp is None:
        raise ImportError("healpy is required")
    
    theta = (np.arange(nlat) + 0.5) * (np.pi / nlat)
    phi = (np.arange(nlon) + 0.5) * (2.0 * np.pi / nlon)
    
    th2, ph2 = np.meshgrid(theta, phi, indexing="ij")
    img = hp.get_interp_val(m, th2, ph2).astype(np.float64)
    
    return img


def _torusify_lat(img: np.ndarray) -> np.ndarray:
    """Make latitude axis periodic by mirroring (torus projection)."""
    return np.vstack([img, img[::-1, :]])


# -------------------------
# Core Phase-Lock Functions
# -------------------------

def compute_phase_lock(
    fft_segments_tt: List[np.ndarray],
    fft_segments_bb: List[np.ndarray],
    targets: List[int] = None
) -> Tuple[np.ndarray, Dict[int, float]]:
    """
    Compute Phase Coherence (PC) between two channels via cross-spectrum.
    
    This is the core implementation of the phase-lock scan as described
    in the UBT theoretical framework.
    
    Args:
        fft_segments_tt: List of complex 2D FFT arrays for TT channel
        fft_segments_bb: List of complex 2D FFT arrays for BB channel
        targets: Optional list of target k values to report
    
    Returns:
        coherence: Array of phase coherence values for each k
        target_values: Dict mapping target k to PC value
    
    Theory:
        For each segment and radial frequency k:
            1. Compute normalized cross-spectrum: (X * Y*) / (|X| * |Y|)
            2. This extracts pure phase relationship: exp(i·Δφ)
            3. Accumulate phasors across segments for each k
            4. Phase Coherence = |mean_phasor| ∈ [0, 1]
        
        PC = 1.0 means perfect phase lock (all segments coherent)
        PC = 0.0 means total phase chaos (random phase differences)
    """
    if targets is None:
        targets = [137, 139]
    
    n_segments = len(fft_segments_tt)
    if n_segments == 0 or len(fft_segments_bb) == 0:
        raise ValueError("No FFT segments provided")
    
    print(f"[phase_lock] Processing {n_segments} segments...")
    
    # Get shape from first segment
    h, w = fft_segments_tt[0].shape
    
    # Build radial frequency grid
    y, x = np.indices((h, w))
    center = (h // 2, w // 2)
    r = np.sqrt((x - center[1])**2 + (y - center[0])**2)
    r = np.round(r).astype(int)
    max_k = int(np.max(r))
    
    # Initialize phasor accumulators for each k
    # We accumulate normalized cross-spectrum: (X * Y*) / (|X| * |Y|)
    phasor_sum = np.zeros(max_k + 1, dtype=complex)
    counts = np.zeros(max_k + 1, dtype=int)
    
    # Process each segment
    for i, (seg_tt, seg_bb) in enumerate(zip(fft_segments_tt, fft_segments_bb)):
        if (i + 1) % 10 == 0:
            print(f"  Segment {i+1}/{n_segments}")
        
        # Shift FFT for radial analysis (DC at center)
        s_tt = np.fft.fftshift(seg_tt)
        s_bb = np.fft.fftshift(seg_bb)
        
        # Compute normalized cross-spectrum to extract pure phase
        # cross_phase = (s_tt * conj(s_bb)) / (|s_tt| * |s_bb|)
        # This gives exp(i·Δφ) where Δφ is the phase difference
        denom = np.abs(s_tt) * np.abs(s_bb)
        
        # Avoid division by zero
        valid = denom > 0
        cross_phase = np.zeros_like(s_tt, dtype=complex)
        cross_phase[valid] = (s_tt[valid] * np.conj(s_bb[valid])) / denom[valid]
        
        # Accumulate by radial frequency k
        for k_val in range(max_k + 1):
            mask = (r == k_val)
            if np.any(mask):
                phasor_sum[k_val] += np.sum(cross_phase[mask])
                counts[k_val] += np.sum(mask)
    
    # Compute Phase Coherence: |mean_phasor|
    # Avoid division by zero
    with np.errstate(invalid='ignore', divide='ignore'):
        coherence = np.abs(phasor_sum / np.maximum(counts, 1))
    
    # Set coherence to 0 where no data
    coherence[counts == 0] = 0.0
    
    # Extract target values
    target_values = {}
    for k in targets:
        if 0 <= k < len(coherence):
            target_values[k] = float(coherence[k])
        else:
            target_values[k] = float('nan')
    
    print(f"[phase_lock] Phase coherence computed for k=0..{max_k}")
    for k in targets:
        if k in target_values:
            print(f"  PC(k={k}) = {target_values[k]:.6f}")
    
    return coherence, target_values


def segment_and_fft(
    img: np.ndarray,
    window_size: int,
    stride: Optional[int] = None,
    window_name: str = "none"
) -> List[np.ndarray]:
    """
    Segment image into overlapping windows and compute 2D FFT for each.
    
    Args:
        img: 2D image array
        window_size: Size of square window (W×W)
        stride: Step size for window sliding (default: W/2 for Welch method)
        window_name: Window function name ("none", "hann", etc.)
    
    Returns:
        List of complex 2D FFT arrays for each segment
    """
    if stride is None:
        stride = max(1, window_size // 2)
    
    nlat, nlon = img.shape
    w = window_size
    
    # Create window function
    window_2d = _window_2d(window_name, w, w, normalize_rms=True)
    
    fft_segments = []
    n_lat = (nlat - w) // stride + 1
    n_lon = (nlon - w) // stride + 1
    total_segments = n_lat * n_lon
    
    print(f"[segment_fft] Creating {total_segments} segments ({n_lat}×{n_lon} grid)")
    print(f"[segment_fft] Window: {w}×{w}, Stride: {stride}, Function: {window_name}")
    
    for i_lat in range(0, nlat - w + 1, stride):
        for i_lon in range(0, nlon - w + 1, stride):
            # Extract segment
            patch = img[i_lat:i_lat+w, i_lon:i_lon+w]
            
            # Remove mean
            patch = patch - np.mean(patch)
            
            # Apply window
            patch_windowed = patch * window_2d
            
            # 2D FFT
            F = np.fft.fft2(patch_windowed)
            fft_segments.append(F)
    
    print(f"[segment_fft] Generated {len(fft_segments)} FFT segments")
    return fft_segments


def monte_carlo_phase_lock(
    img_tt: np.ndarray,
    img_bb: np.ndarray,
    window_size: int,
    targets: List[int],
    n_mc: int,
    seed: int = 0,
    stride: Optional[int] = None,
    window_name: str = "none",
    null_method: str = "phase-shuffle"
) -> Tuple[Dict[int, float], Dict[int, float], Dict[int, float]]:
    """
    Monte Carlo validation of phase coherence using null model.
    
    Args:
        img_tt, img_bb: TT and BB channel images
        window_size: Segment window size
        targets: Target k values
        n_mc: Number of Monte Carlo samples
        seed: Random seed
        stride: Window stride
        window_name: Window function
        null_method: "phase-shuffle" or "phi-roll"
    
    Returns:
        mc_mean: Mean PC for each target under null
        mc_std: Std dev of PC under null
        p_values: One-sided p-values for each target
    """
    rng = np.random.default_rng(seed)
    
    # Compute observed coherence
    print("[mc] Computing observed phase coherence...")
    fft_tt = segment_and_fft(img_tt, window_size, stride, window_name)
    fft_bb = segment_and_fft(img_bb, window_size, stride, window_name)
    _, obs_pc = compute_phase_lock(fft_tt, fft_bb, targets)
    
    # MC null distribution
    mc_samples = {k: [] for k in targets}
    
    print(f"[mc] Running {n_mc} Monte Carlo samples with null={null_method}...")
    
    for i in range(n_mc):
        if (i + 1) % 100 == 0 or n_mc <= 100:
            print(f"  MC sample {i+1}/{n_mc}")
        
        # Generate null by shuffling BB phases
        if null_method == "phase-shuffle":
            # Shuffle BB image phases in Fourier domain
            F_bb = np.fft.fft2(img_bb)
            phase_bb = np.angle(F_bb)
            mag_bb = np.abs(F_bb)
            
            # Shuffle phases randomly
            phase_shuffled = rng.permutation(phase_bb.ravel()).reshape(phase_bb.shape)
            F_bb_null = mag_bb * np.exp(1j * phase_shuffled)
            img_bb_null = np.real(np.fft.ifft2(F_bb_null))
        
        elif null_method == "phi-roll":
            # Roll each latitude row by random longitude shift
            nlat, nlon = img_bb.shape
            img_bb_null = np.empty_like(img_bb)
            shifts = rng.integers(0, nlon, size=nlat)
            for i_lat in range(nlat):
                img_bb_null[i_lat] = np.roll(img_bb[i_lat], int(shifts[i_lat]))
        
        else:
            raise ValueError(f"Unknown null method: {null_method}")
        
        # Compute phase coherence for null
        fft_bb_null = segment_and_fft(img_bb_null, window_size, stride, window_name)
        _, null_pc = compute_phase_lock(fft_tt, fft_bb_null, targets)
        
        for k in targets:
            mc_samples[k].append(null_pc[k])
    
    # Compute statistics
    mc_mean = {}
    mc_std = {}
    p_values = {}
    
    print("\n[mc] Monte Carlo statistics:")
    for k in targets:
        samples = np.array(mc_samples[k])
        mc_mean[k] = float(np.mean(samples))
        mc_std[k] = float(np.std(samples))
        
        # One-sided p-value: P(null >= observed)
        p_values[k] = float(np.mean(samples >= obs_pc[k]))
        
        z_score = (obs_pc[k] - mc_mean[k]) / mc_std[k] if mc_std[k] > 0 else 0.0
        
        print(f"  k={k}:")
        print(f"    Observed PC = {obs_pc[k]:.6f}")
        print(f"    MC mean     = {mc_mean[k]:.6f}")
        print(f"    MC std      = {mc_std[k]:.6f}")
        print(f"    Z-score     = {z_score:.4f}")
        print(f"    p-value     = {p_values[k]:.6g}")
    
    return mc_mean, mc_std, p_values


# -------------------------
# Main Entry Point
# -------------------------

@dataclass
class PhaseLockConfig:
    """Configuration for phase-lock scan."""
    tt_map_path: str
    q_map_path: str
    u_map_path: str
    targets: List[int]
    nside_out: int
    lmax_alm: int
    nlat: int
    nlon: int
    window_size: int
    stride: Optional[int]
    window_name: str
    projection: str
    mc: int
    null_method: str
    seed: int
    report_csv: str
    plot_png: str
    dump_full_csv: str


def main() -> None:
    """Main entry point for unified phase-lock scan."""
    if hp is None:
        print("[error] healpy is required. Install with: pip install healpy")
        return
    
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Input maps
    ap.add_argument("--tt-map", required=True,
                    help="HEALPix FITS for TT (temperature) channel")
    ap.add_argument("--q-map", required=True,
                    help="HEALPix FITS for Q polarization")
    ap.add_argument("--u-map", required=True,
                    help="HEALPix FITS for U polarization")
    
    # Target frequencies
    ap.add_argument("--targets", default="137,139",
                    help="Comma-separated target k values (default: 137,139)")
    
    # Map processing
    ap.add_argument("--nside-out", type=int, default=256,
                    help="Degrade maps to this NSIDE (default: 256)")
    ap.add_argument("--lmax-alm", type=int, default=512,
                    help="lmax for E/B decomposition (default: 512)")
    ap.add_argument("--nlat", type=int, default=512,
                    help="Grid height for projection (default: 512)")
    ap.add_argument("--nlon", type=int, default=1024,
                    help="Grid width for projection (default: 1024)")
    ap.add_argument("--projection", choices=["lonlat", "torus"], default="torus",
                    help="Projection type (default: torus for toroidal periodicity)")
    
    # Segmentation
    ap.add_argument("--window-size", type=int, default=128,
                    help="Segment window size W×W (default: 128)")
    ap.add_argument("--stride", type=int, default=None,
                    help="Window stride (default: W/2 for Welch overlap)")
    ap.add_argument("--window", dest="window_name", default="none",
                    help="Window function: none|hann|hamming (default: none)")
    
    # Monte Carlo
    ap.add_argument("--mc", type=int, default=0,
                    help="Number of Monte Carlo samples (default: 0, no MC)")
    ap.add_argument("--null", dest="null_method", 
                    choices=["phase-shuffle", "phi-roll"], default="phase-shuffle",
                    help="Null model method (default: phase-shuffle)")
    ap.add_argument("--seed", type=int, default=0,
                    help="Random seed (default: 0)")
    
    # Output
    ap.add_argument("--report-csv", default="",
                    help="Output CSV for target results")
    ap.add_argument("--plot", dest="plot_png", default="",
                    help="Output PNG for diagnostic plot")
    ap.add_argument("--dump-full-csv", default="",
                    help="Output CSV with full spectrum (all k values)")
    
    args = ap.parse_args()
    
    # Parse configuration
    config = PhaseLockConfig(
        tt_map_path=args.tt_map,
        q_map_path=args.q_map,
        u_map_path=args.u_map,
        targets=_parse_ints_csv(args.targets),
        nside_out=args.nside_out,
        lmax_alm=args.lmax_alm,
        nlat=args.nlat,
        nlon=args.nlon,
        window_size=args.window_size,
        stride=args.stride,
        window_name=args.window_name,
        projection=args.projection,
        mc=args.mc,
        null_method=args.null_method,
        seed=args.seed,
        report_csv=args.report_csv,
        plot_png=args.plot_png,
        dump_full_csv=args.dump_full_csv
    )
    
    print("=" * 70)
    print("UNIFIED PHASE-LOCK SCAN FOR UBT CMB VERIFICATION")
    print("=" * 70)
    print(f"TT map:       {config.tt_map_path}")
    print(f"Q/U maps:     {config.q_map_path}, {config.u_map_path}")
    print(f"Targets:      {config.targets}")
    print(f"Grid:         {config.nlat}×{config.nlon}")
    print(f"Window:       {config.window_size}×{config.window_size}")
    print(f"Stride:       {config.stride or config.window_size//2}")
    print(f"Window func:  {config.window_name}")
    print(f"Projection:   {config.projection}")
    print(f"MC samples:   {config.mc}")
    print("=" * 70 + "\n")
    
    # Load maps
    print("[load] Loading TT map...")
    tt_map = hp.read_map(config.tt_map_path, field=0, verbose=False)
    tt_map = _ud_grade(tt_map, config.nside_out)
    
    print("[load] Loading Q/U maps...")
    q_map = hp.read_map(config.q_map_path, field=0, verbose=False)
    u_map = hp.read_map(config.u_map_path, field=0, verbose=False)
    q_map = _ud_grade(q_map, config.nside_out)
    u_map = _ud_grade(u_map, config.nside_out)
    
    # Compute BB map
    print(f"[load] Computing E/B decomposition (lmax={config.lmax_alm})...")
    almE, almB = _map2alm_spin_compat([q_map, u_map], 2, config.lmax_alm)
    bb_map = hp.alm2map(almB, nside=config.nside_out, lmax=config.lmax_alm, verbose=False)
    
    # Project to equirectangular
    print(f"[project] Projecting TT to {config.nlat}×{config.nlon}...")
    img_tt = _project_to_equirect(tt_map, config.nlat, config.nlon)
    
    print(f"[project] Projecting BB to {config.nlat}×{config.nlon}...")
    img_bb = _project_to_equirect(bb_map, config.nlat, config.nlon)
    
    # Apply toroidal periodicity if requested
    if config.projection == "torus":
        print("[project] Applying toroidal periodicity (latitude mirroring)...")
        img_tt = _torusify_lat(img_tt)
        img_bb = _torusify_lat(img_bb)
    
    # Segment and compute FFTs
    print("\n[fft] Segmenting TT channel...")
    fft_tt = segment_and_fft(img_tt, config.window_size, config.stride, config.window_name)
    
    print("[fft] Segmenting BB channel...")
    fft_bb = segment_and_fft(img_bb, config.window_size, config.stride, config.window_name)
    
    # Compute phase coherence
    print("\n[analysis] Computing phase coherence...")
    coherence_full, coherence_targets = compute_phase_lock(fft_tt, fft_bb, config.targets)
    
    # Monte Carlo validation
    mc_mean = None
    mc_std = None
    p_values = None
    
    if config.mc > 0:
        print("\n[analysis] Running Monte Carlo validation...")
        mc_mean, mc_std, p_values = monte_carlo_phase_lock(
            img_tt, img_bb,
            window_size=config.window_size,
            targets=config.targets,
            n_mc=config.mc,
            seed=config.seed,
            stride=config.stride,
            window_name=config.window_name,
            null_method=config.null_method
        )
    
    # Print results
    print("\n" + "=" * 70)
    print("PHASE-LOCK RESULTS")
    print("=" * 70)
    for k in config.targets:
        print(f"\nk = {k}:")
        print(f"  Phase Coherence (PC) = {coherence_targets[k]:.8f}")
        if p_values:
            print(f"  MC null mean         = {mc_mean[k]:.8f}")
            print(f"  MC null std          = {mc_std[k]:.8f}")
            z = (coherence_targets[k] - mc_mean[k]) / mc_std[k] if mc_std[k] > 0 else 0
            print(f"  Z-score              = {z:.4f}")
            print(f"  p-value              = {p_values[k]:.6g}")
            if p_values[k] < 0.001:
                print(f"  Significance         = *** HIGHLY SIGNIFICANT ***")
            elif p_values[k] < 0.01:
                print(f"  Significance         = ** SIGNIFICANT **")
            elif p_values[k] < 0.05:
                print(f"  Significance         = * MARGINALLY SIGNIFICANT *")
    print("=" * 70 + "\n")
    
    # Write target results CSV
    if config.report_csv:
        _ensure_dir_for(config.report_csv)
        with open(config.report_csv, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow([
                "k_target", "phase_coherence", "mc_mean", "mc_std", "z_score", "p_value",
                "window_size", "stride", "window_func", "projection", "mc_samples"
            ])
            for k in config.targets:
                pc = coherence_targets[k]
                if p_values:
                    mean = mc_mean[k]
                    std = mc_std[k]
                    z = (pc - mean) / std if std > 0 else 0
                    p = p_values[k]
                else:
                    mean = std = z = p = float('nan')
                
                w.writerow([
                    k, pc, mean, std, z, p,
                    config.window_size, config.stride or config.window_size//2,
                    config.window_name, config.projection, config.mc
                ])
        print(f"[output] Wrote target results: {config.report_csv}")
    
    # Write full spectrum CSV
    if config.dump_full_csv:
        _ensure_dir_for(config.dump_full_csv)
        with open(config.dump_full_csv, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(["k", "phase_coherence"])
            for k in range(len(coherence_full)):
                w.writerow([k, coherence_full[k]])
        print(f"[output] Wrote full spectrum: {config.dump_full_csv}")
    
    # Generate plot
    if config.plot_png:
        try:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            
            _ensure_dir_for(config.plot_png)
            
            fig = plt.figure(figsize=(12, 8))
            
            # Plot 1: Full spectrum
            ax1 = plt.subplot(2, 1, 1)
            k_vals = np.arange(len(coherence_full))
            ax1.plot(k_vals, coherence_full, linewidth=1, color='blue', alpha=0.7)
            
            # Highlight targets
            for k in config.targets:
                if k < len(coherence_full):
                    ax1.axvline(k, color='red', linestyle='--', alpha=0.6, linewidth=1.5)
                    ax1.text(k, coherence_full[k], f' k={k}', 
                            fontsize=9, verticalalignment='bottom')
            
            ax1.set_xlabel('k (cycles per map)', fontsize=11)
            ax1.set_ylabel('Phase Coherence PC', fontsize=11)
            ax1.set_title('Unified Phase-Lock Scan: TT vs BB Cross-Channel Coherence',
                         fontsize=12, fontweight='bold')
            ax1.grid(True, alpha=0.3)
            ax1.set_ylim(0, 1.05)
            
            # Plot 2: Target zoom
            ax2 = plt.subplot(2, 1, 2)
            k_min = max(0, min(config.targets) - 10)
            k_max = min(len(coherence_full), max(config.targets) + 10)
            k_zoom = k_vals[k_min:k_max]
            pc_zoom = coherence_full[k_min:k_max]
            
            ax2.plot(k_zoom, pc_zoom, linewidth=2, color='blue', marker='o', markersize=4)
            
            for k in config.targets:
                if k_min <= k < k_max:
                    ax2.axvline(k, color='red', linestyle='--', alpha=0.6, linewidth=1.5)
                    label = f'k={k}\nPC={coherence_targets[k]:.4f}'
                    if p_values:
                        label += f'\np={p_values[k]:.3g}'
                    ax2.text(k, coherence_targets[k], label, 
                            fontsize=8, verticalalignment='bottom',
                            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
            
            ax2.set_xlabel('k (cycles per map)', fontsize=11)
            ax2.set_ylabel('Phase Coherence PC', fontsize=11)
            ax2.set_title(f'Zoom: Jacobi Cluster Region (k={k_min}..{k_max})',
                         fontsize=11, fontweight='bold')
            ax2.grid(True, alpha=0.3)
            ax2.set_ylim(0, 1.05)
            
            plt.tight_layout()
            plt.savefig(config.plot_png, dpi=150)
            plt.close(fig)
            
            print(f"[output] Wrote plot: {config.plot_png}")
        
        except ImportError:
            print("[warn] matplotlib not available; skipping plot")
    
    print("\n[complete] Unified Phase-Lock Scan finished successfully.")


if __name__ == '__main__':
    main()
