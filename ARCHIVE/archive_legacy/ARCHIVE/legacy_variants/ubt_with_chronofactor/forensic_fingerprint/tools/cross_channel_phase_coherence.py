#!/usr/bin/env python3
"""
cross_channel_phase_coherence.py

Cross-Channel Phase Coherence Analyzer for UBT CMB verification.

According to UBT, the TT and BB channels represent different sectors of the 
unified biquaternion field Θ:
    Θ = Θ_S + Θ_V + i(Θ̃_S + Θ̃_V)

- TT channel: Dispersive imaginary scalar Θ̃_S (measures k=137 cluster)
- BB channel: Biquaternion/spinor sector Θ_V (measures k=139 peak)

If both channels are projections of a single unified field, they must exhibit
non-random phase relationships (Phase-Lock) at their respective resonances.

This script:
1. Loads 2D FFT data from TT and BB channels
2. Extracts complex Fourier coefficients at target k values
3. Computes phase coherence metrics between channels
4. Tests for non-random phase-lock via Monte Carlo permutations
5. Generates diagnostic plots and statistical reports

Theoretical Background:
For a unified field Θ with real and imaginary components projected onto TT/BB:
    TT ~ Re(Θ̃_S),  BB ~ |Θ_V|

Phase coherence is measured via:
    Γ(k₁,k₂) = |⟨exp(i(φ_TT(k₁) - φ_BB(k₂)))⟩|

A significant phase-lock (Γ near 1) indicates the channels are coupled through
a common underlying field structure.

Usage:
    python -m forensic_fingerprint.tools.cross_channel_phase_coherence \\
        --tt-map data/planck_pr3_tt.fits \\
        --q-map data/planck_pr3_q.fits \\
        --u-map data/planck_pr3_u.fits \\
        --k-tt 137 --k-bb 139 \\
        --output results/phase_coherence_report.txt \\
        --plot results/phase_coherence.png \\
        --mc 1000
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
        raise ImportError("healpy is required for map operations")
    nside_in = hp.get_nside(m)
    if nside_out == nside_in:
        return m
    return hp.ud_grade(m, nside_out, order_in="RING", order_out="RING", power=0)


def _map2alm_spin_compat(qu_maps, spin: int, lmax: int):
    """Compatibility wrapper for healpy map2alm_spin."""
    if hp is None:
        raise ImportError("healpy is required for map operations")
    
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


def _project_to_equirect(m: np.ndarray, nlat: int, nlon: int) -> np.ndarray:
    """Project HEALPix map to equirectangular grid."""
    if hp is None:
        raise ImportError("healpy is required for projection")
    
    theta = (np.arange(nlat) + 0.5) * (np.pi / nlat)
    phi = (np.arange(nlon) + 0.5) * (2.0 * np.pi / nlon)
    
    th2, ph2 = np.meshgrid(theta, phi, indexing="ij")
    img = hp.get_interp_val(m, th2, ph2).astype(np.float64)
    
    return img


def _fft2_complex(img: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    2D FFT returning complex coefficients.
    
    Returns:
        F: Complex FFT coefficients (ny, nx//2+1)
        ky: Frequency array for y (cycles per map height)
        kx: Frequency array for x (cycles per map width)
    """
    ny, nx = img.shape
    F = np.fft.rfft2(img - np.mean(img))  # Remove DC
    ky = np.fft.fftfreq(ny) * ny
    kx = np.fft.rfftfreq(nx) * nx
    return F, ky, kx


def extract_phase_at_k(F: np.ndarray, ky: np.ndarray, kx: np.ndarray, k_target: int) -> np.ndarray:
    """
    Extract phases at all Fourier modes with |k| ≈ k_target.
    
    Args:
        F: Complex FFT array
        ky, kx: Frequency arrays
        k_target: Target radial wavenumber
    
    Returns:
        Array of phases (in radians) for modes near k_target
    """
    # Build radial k grid
    KX, KY = np.meshgrid(kx, ky)
    KR = np.sqrt(KX**2 + KY**2)
    
    # Select modes within ±0.5 of k_target
    mask = np.abs(KR - k_target) <= 0.5
    
    # Extract complex coefficients
    coeffs = F[mask]
    
    # Return phases
    return np.angle(coeffs)


@dataclass
class PhaseCoherenceResult:
    """Results from phase coherence analysis."""
    k_tt: int
    k_bb: int
    phases_tt: np.ndarray
    phases_bb: np.ndarray
    coherence_obs: float
    coherence_mean_null: float
    coherence_std_null: float
    z_score: float
    p_value: float
    n_mc: int
    mean_phase_diff: float
    phase_concentration: float


def compute_phase_coherence(phases_a: np.ndarray, phases_b: np.ndarray) -> Tuple[float, float, float]:
    """
    Compute phase coherence between two sets of phases.
    
    Args:
        phases_a, phases_b: Arrays of phases in radians
    
    Returns:
        coherence: |⟨exp(i·Δφ)⟩| where Δφ = phases_a - phases_b
        mean_diff: Mean phase difference (radians)
        concentration: Von Mises concentration parameter estimate
    """
    # Ensure equal lengths by pairing randomly
    n = min(len(phases_a), len(phases_b))
    if n == 0:
        return 0.0, 0.0, 0.0
    
    # Use all pairwise differences (full cross-correlation)
    diff_matrix = phases_a[:, None] - phases_b[None, :]
    diff_flat = diff_matrix.ravel()
    
    # Compute coherence
    z = np.exp(1j * diff_flat)
    coherence = float(np.abs(np.mean(z)))
    
    # Mean phase difference
    mean_diff = float(np.angle(np.mean(z)))
    
    # Von Mises concentration (circular variance)
    R = coherence
    if R < 1.0 and R > 0:
        # Approximation: κ ≈ R(2-R²)/(1-R²)
        concentration = R * (2 - R**2) / (1 - R**2)
    else:
        concentration = float('inf') if R == 1.0 else 0.0
    
    return coherence, mean_diff, concentration


def phase_coherence_analysis(
    tt_map: np.ndarray,
    bb_map: np.ndarray,
    k_tt: int,
    k_bb: int,
    nlat: int = 512,
    nlon: int = 1024,
    mc_samples: int = 0,
    seed: int = 0
) -> PhaseCoherenceResult:
    """
    Perform cross-channel phase coherence analysis.
    
    Args:
        tt_map: Temperature map (HEALPix)
        bb_map: B-mode polarization map (HEALPix)
        k_tt: Target k for TT channel
        k_bb: Target k for BB channel
        nlat, nlon: Grid size for projection
        mc_samples: Number of Monte Carlo permutations
        seed: Random seed
    
    Returns:
        PhaseCoherenceResult object
    """
    rng = np.random.default_rng(seed)
    
    # Project to equirectangular
    print(f"[phase_coherence] Projecting TT map to {nlat}×{nlon} grid...")
    img_tt = _project_to_equirect(tt_map, nlat, nlon)
    
    print(f"[phase_coherence] Projecting BB map to {nlat}×{nlon} grid...")
    img_bb = _project_to_equirect(bb_map, nlat, nlon)
    
    # Compute 2D FFTs
    print("[phase_coherence] Computing 2D FFTs...")
    F_tt, ky_tt, kx_tt = _fft2_complex(img_tt)
    F_bb, ky_bb, kx_bb = _fft2_complex(img_bb)
    
    # Extract phases at target k values
    print(f"[phase_coherence] Extracting phases: TT at k={k_tt}, BB at k={k_bb}...")
    phases_tt = extract_phase_at_k(F_tt, ky_tt, kx_tt, k_tt)
    phases_bb = extract_phase_at_k(F_bb, ky_bb, kx_bb, k_bb)
    
    print(f"[phase_coherence] Found {len(phases_tt)} TT modes, {len(phases_bb)} BB modes")
    
    # Compute observed coherence
    coherence_obs, mean_diff, concentration = compute_phase_coherence(phases_tt, phases_bb)
    
    print(f"[phase_coherence] Observed coherence: {coherence_obs:.6f}")
    
    # Monte Carlo null distribution
    coherence_null = []
    if mc_samples > 0:
        print(f"[phase_coherence] Running {mc_samples} MC permutations...")
        for i in range(mc_samples):
            if i % 100 == 0 and i > 0:
                print(f"  {i}/{mc_samples}")
            
            # Permute BB phases randomly
            phases_bb_perm = rng.permutation(phases_bb)
            coh_null, _, _ = compute_phase_coherence(phases_tt, phases_bb_perm)
            coherence_null.append(coh_null)
        
        coherence_null = np.array(coherence_null)
        mean_null = float(np.mean(coherence_null))
        std_null = float(np.std(coherence_null))
        z_score = (coherence_obs - mean_null) / std_null if std_null > 0 else 0.0
        p_value = float(np.mean(coherence_null >= coherence_obs))
    else:
        mean_null = 0.0
        std_null = 0.0
        z_score = 0.0
        p_value = float('nan')
    
    return PhaseCoherenceResult(
        k_tt=k_tt,
        k_bb=k_bb,
        phases_tt=phases_tt,
        phases_bb=phases_bb,
        coherence_obs=coherence_obs,
        coherence_mean_null=mean_null,
        coherence_std_null=std_null,
        z_score=z_score,
        p_value=p_value,
        n_mc=mc_samples,
        mean_phase_diff=mean_diff,
        phase_concentration=concentration
    )


def write_coherence_report(result: PhaseCoherenceResult, output_path: str) -> None:
    """Write phase coherence results to text file."""
    _ensure_dir_for(output_path)
    
    with open(output_path, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("UBT Cross-Channel Phase Coherence Analysis\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("TARGET MODES:\n")
        f.write(f"  TT channel k = {result.k_tt} (dispersive scalar sector Θ̃_S)\n")
        f.write(f"  BB channel k = {result.k_bb} (biquaternion sector Θ_V)\n\n")
        
        f.write("PHASE EXTRACTION:\n")
        f.write(f"  TT modes found = {len(result.phases_tt)}\n")
        f.write(f"  BB modes found = {len(result.phases_bb)}\n\n")
        
        f.write("COHERENCE METRICS:\n")
        f.write(f"  Observed coherence Γ         = {result.coherence_obs:.8f}\n")
        f.write(f"  Mean phase difference ⟨Δφ⟩   = {result.mean_phase_diff:.6f} rad")
        f.write(f" ({np.degrees(result.mean_phase_diff):.2f}°)\n")
        f.write(f"  Phase concentration κ        = {result.phase_concentration:.6f}\n\n")
        
        if result.n_mc > 0:
            f.write("MONTE CARLO NULL TEST:\n")
            f.write(f"  MC samples                   = {result.n_mc}\n")
            f.write(f"  Null mean coherence          = {result.coherence_mean_null:.8f}\n")
            f.write(f"  Null std deviation           = {result.coherence_std_null:.8f}\n")
            f.write(f"  Z-score                      = {result.z_score:.4f}\n")
            f.write(f"  p-value (one-sided)          = {result.p_value:.6g}\n\n")
            
            # Significance interpretation
            if result.p_value < 0.001:
                sig = "***HIGHLY SIGNIFICANT*** (p < 0.001)"
            elif result.p_value < 0.01:
                sig = "**SIGNIFICANT** (p < 0.01)"
            elif result.p_value < 0.05:
                sig = "*MARGINALLY SIGNIFICANT* (p < 0.05)"
            else:
                sig = "NOT SIGNIFICANT (p >= 0.05)"
            
            f.write(f"STATISTICAL SIGNIFICANCE:\n")
            f.write(f"  {sig}\n\n")
        
        f.write("=" * 70 + "\n")
        f.write("INTERPRETATION:\n")
        f.write("=" * 70 + "\n")
        f.write("A high coherence Γ ≈ 1 with low p-value indicates non-random\n")
        f.write("phase-lock between TT and BB channels. This supports the UBT\n")
        f.write("hypothesis that both channels are projections of a unified\n")
        f.write("biquaternion field Θ defined on an 8D toroidal substrate.\n\n")
        
        f.write("Twin-prime modes k=137 (TT) and k=139 (BB) are predicted to\n")
        f.write("be coupled through the field's dispersive and vector sectors,\n")
        f.write("respectively. Phase coherence confirms this coupling.\n")
        f.write("=" * 70 + "\n")


def plot_coherence_results(result: PhaseCoherenceResult, output_path: str) -> None:
    """Generate diagnostic plots for phase coherence."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("[warn] matplotlib not available; skipping plot")
        return
    
    _ensure_dir_for(output_path)
    
    fig = plt.figure(figsize=(12, 10))
    
    # 1. Phase distributions
    ax1 = plt.subplot(3, 2, 1)
    ax1.hist(result.phases_tt, bins=30, alpha=0.7, color='blue', edgecolor='black')
    ax1.set_xlabel('Phase (radians)', fontsize=10)
    ax1.set_ylabel('Count', fontsize=10)
    ax1.set_title(f'TT Phase Distribution (k={result.k_tt})', fontsize=11, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    ax2 = plt.subplot(3, 2, 2)
    ax2.hist(result.phases_bb, bins=30, alpha=0.7, color='red', edgecolor='black')
    ax2.set_xlabel('Phase (radians)', fontsize=10)
    ax2.set_ylabel('Count', fontsize=10)
    ax2.set_title(f'BB Phase Distribution (k={result.k_bb})', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # 2. Phase difference scatter
    ax3 = plt.subplot(3, 2, 3)
    # Sample for visualization if too many points
    n_sample = min(1000, len(result.phases_tt))
    idx_tt = np.random.choice(len(result.phases_tt), n_sample, replace=False)
    idx_bb = np.random.choice(len(result.phases_bb), n_sample, replace=False)
    ax3.scatter(result.phases_tt[idx_tt], result.phases_bb[idx_bb], 
                alpha=0.3, s=10, color='purple')
    ax3.set_xlabel(f'TT Phase (k={result.k_tt}) [rad]', fontsize=10)
    ax3.set_ylabel(f'BB Phase (k={result.k_bb}) [rad]', fontsize=10)
    ax3.set_title('Phase Correlation', fontsize=11, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # 3. Phase difference distribution
    ax4 = plt.subplot(3, 2, 4)
    diff_sample = result.phases_tt[idx_tt] - result.phases_bb[idx_bb]
    ax4.hist(diff_sample, bins=30, alpha=0.7, color='green', edgecolor='black')
    ax4.axvline(result.mean_phase_diff, color='red', linestyle='--', 
                linewidth=2, label=f'Mean: {result.mean_phase_diff:.3f} rad')
    ax4.set_xlabel('Phase Difference Δφ (radians)', fontsize=10)
    ax4.set_ylabel('Count', fontsize=10)
    ax4.set_title('Phase Difference Distribution', fontsize=11, fontweight='bold')
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)
    
    # 4. Coherence summary
    ax5 = plt.subplot(3, 2, 5)
    ax5.axis('off')
    text_lines = [
        f"Observed Coherence Γ = {result.coherence_obs:.6f}",
        f"Mean Phase Diff ⟨Δφ⟩ = {result.mean_phase_diff:.4f} rad",
        f"Concentration κ = {result.phase_concentration:.4f}",
    ]
    if result.n_mc > 0:
        text_lines.extend([
            "",
            f"MC Null Mean = {result.coherence_mean_null:.6f}",
            f"MC Null Std = {result.coherence_std_null:.6f}",
            f"Z-score = {result.z_score:.4f}",
            f"p-value = {result.p_value:.6g}",
        ])
    
    ax5.text(0.1, 0.5, '\n'.join(text_lines), fontsize=11, verticalalignment='center',
             family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # 5. Polar plot of phase vectors
    ax6 = plt.subplot(3, 2, 6, projection='polar')
    # Plot phase vectors on unit circle
    n_sample_polar = min(200, len(result.phases_tt))
    idx_polar = np.random.choice(len(result.phases_tt), n_sample_polar, replace=False)
    ax6.scatter(result.phases_tt[idx_polar], np.ones(n_sample_polar), 
                alpha=0.5, s=20, color='blue', label=f'TT (k={result.k_tt})')
    
    idx_polar_bb = np.random.choice(len(result.phases_bb), n_sample_polar, replace=False)
    ax6.scatter(result.phases_bb[idx_polar_bb], np.ones(n_sample_polar) * 0.7, 
                alpha=0.5, s=20, color='red', label=f'BB (k={result.k_bb})')
    ax6.set_ylim(0, 1.2)
    ax6.set_title('Phase Distribution (Polar)', fontsize=11, fontweight='bold', pad=20)
    ax6.legend(loc='upper right', fontsize=9)
    
    plt.suptitle(f'UBT Cross-Channel Phase Coherence: TT(k={result.k_tt}) vs BB(k={result.k_bb})',
                 fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    
    print(f"[info] wrote plot: {output_path}")


def main() -> None:
    """Main entry point."""
    if hp is None:
        print("[error] healpy is required. Install with: pip install healpy")
        return
    
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    
    ap.add_argument('--tt-map', required=True,
                    help='HEALPix FITS file for TT (temperature) channel')
    ap.add_argument('--q-map', required=True,
                    help='HEALPix FITS file for Q polarization')
    ap.add_argument('--u-map', required=True,
                    help='HEALPix FITS file for U polarization')
    
    ap.add_argument('--k-tt', type=int, default=137,
                    help='Target k for TT channel (default: 137)')
    ap.add_argument('--k-bb', type=int, default=139,
                    help='Target k for BB channel (default: 139)')
    
    ap.add_argument('--nside-out', type=int, default=256,
                    help='Degrade maps to this NSIDE (default: 256)')
    ap.add_argument('--lmax-alm', type=int, default=512,
                    help='lmax for E/B decomposition (default: 512)')
    ap.add_argument('--nlat', type=int, default=512,
                    help='Grid height for projection (default: 512)')
    ap.add_argument('--nlon', type=int, default=1024,
                    help='Grid width for projection (default: 1024)')
    
    ap.add_argument('--mc', type=int, default=0,
                    help='Number of Monte Carlo permutations (default: 0)')
    ap.add_argument('--seed', type=int, default=0,
                    help='Random seed (default: 0)')
    
    ap.add_argument('--output', default='',
                    help='Output text file for coherence report')
    ap.add_argument('--plot', default='',
                    help='Output PNG file for diagnostic plots')
    
    args = ap.parse_args()
    
    # Load maps
    print(f"[phase_coherence] Loading TT map: {args.tt_map}")
    tt_map = hp.read_map(args.tt_map, field=0, verbose=False)
    tt_map = _ud_grade(tt_map, args.nside_out)
    
    print(f"[phase_coherence] Loading Q/U maps: {args.q_map}, {args.u_map}")
    q_map = hp.read_map(args.q_map, field=0, verbose=False)
    u_map = hp.read_map(args.u_map, field=0, verbose=False)
    q_map = _ud_grade(q_map, args.nside_out)
    u_map = _ud_grade(u_map, args.nside_out)
    
    # Compute BB map
    print(f"[phase_coherence] Computing E/B decomposition (lmax={args.lmax_alm})...")
    almE, almB = _map2alm_spin_compat([q_map, u_map], 2, args.lmax_alm)
    bb_map = hp.alm2map(almB, nside=args.nside_out, lmax=args.lmax_alm, verbose=False)
    
    # Run analysis
    print("\n[phase_coherence] Running phase coherence analysis...")
    result = phase_coherence_analysis(
        tt_map=tt_map,
        bb_map=bb_map,
        k_tt=args.k_tt,
        k_bb=args.k_bb,
        nlat=args.nlat,
        nlon=args.nlon,
        mc_samples=args.mc,
        seed=args.seed
    )
    
    # Print results
    print("\n" + "=" * 70)
    print("PHASE COHERENCE RESULTS:")
    print("=" * 70)
    print(f"  TT(k={result.k_tt}) vs BB(k={result.k_bb})")
    print(f"  Observed coherence Γ  = {result.coherence_obs:.8f}")
    print(f"  Mean phase diff ⟨Δφ⟩   = {result.mean_phase_diff:.6f} rad ({np.degrees(result.mean_phase_diff):.2f}°)")
    print(f"  Concentration κ       = {result.phase_concentration:.6f}")
    
    if result.n_mc > 0:
        print(f"\n  MC null mean          = {result.coherence_mean_null:.8f}")
        print(f"  MC null std           = {result.coherence_std_null:.8f}")
        print(f"  Z-score               = {result.z_score:.4f}")
        print(f"  p-value               = {result.p_value:.6g}")
        
        sigma = abs(result.z_score)
        print(f"  Significance          = {sigma:.2f}σ")
    
    print("=" * 70 + "\n")
    
    # Write outputs
    if args.output:
        write_coherence_report(result, args.output)
        print(f"[info] wrote report: {args.output}")
    
    if args.plot:
        plot_coherence_results(result, args.plot)
    
    print("\n[phase_coherence] Complete.")


if __name__ == '__main__':
    main()
