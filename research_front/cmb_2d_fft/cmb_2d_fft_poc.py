"""
UBT / CMB 2D FFT proof-of-concept (Standalone Version)
- Generate synthetic test patterns (no external data required)
- Apodize (taper) to suppress edge ringing
- Compute 2D FFT power
- Detect oriented "comb"/grid-like anisotropy and estimate tilt angle

Dependencies: numpy, scipy, matplotlib only
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from pathlib import Path

from scipy.ndimage import gaussian_filter
from scipy.signal import windows


# =========================
# SYNTHETIC DATA GENERATORS
# =========================

def generate_synthetic_grid(size, tilt_deg, pix_scale=1.0, seed=0):
    """
    Create a 2D pattern with a very small tilt.
    Uses a cosine comb in spatial domain, rotated by tilt_deg.
    
    Args:
        size: int, dimensions of square patch (size x size)
        tilt_deg: float, tilt angle in degrees
        pix_scale: float, pixel scale (optional, affects wavelength)
        seed: int, random seed for noise
    
    Returns:
        patch: 2D array with tilted grid pattern
    """
    np.random.seed(seed)
    
    # Create coordinate grid
    y = np.arange(size) - size // 2
    x = np.arange(size) - size // 2
    X, Y = np.meshgrid(x, y)
    
    # Rotation matrix
    theta = np.deg2rad(tilt_deg)
    X_rot = X * np.cos(theta) - Y * np.sin(theta)
    Y_rot = X * np.sin(theta) + Y * np.cos(theta)
    
    # Create comb pattern with wavelength ~ size/16 (creates visible grid)
    wavelength = size / 16.0
    pattern = np.cos(2 * np.pi * X_rot / wavelength)
    pattern += np.cos(2 * np.pi * Y_rot / wavelength)
    
    # Add small amount of noise to make it more realistic
    noise = np.random.randn(size, size) * 0.1
    patch = pattern + noise
    
    return patch.astype(np.float32)


def generate_gaussian_field(size, seed=0, smoothing=2.0):
    """
    Generate isotropic Gaussian random field (null control).
    White noise smoothed with Gaussian kernel.
    
    Args:
        size: int, dimensions of square patch
        seed: int, random seed
        smoothing: float, Gaussian smoothing sigma
    
    Returns:
        patch: 2D array with Gaussian random field
    """
    np.random.seed(seed)
    
    # Generate white noise
    noise = np.random.randn(size, size)
    
    # Smooth to create correlations
    if smoothing > 0:
        noise = gaussian_filter(noise, sigma=smoothing)
    
    return noise.astype(np.float32)


def generate_injected(size, tilt_deg, snr=0.2, pix_scale=1.0, seed=0):
    """
    Generate injected signal: gaussian_field + epsilon * synthetic_grid.
    
    Args:
        size: int, dimensions of square patch
        tilt_deg: float, tilt angle for grid pattern
        snr: float, signal-to-noise ratio (controls epsilon)
        pix_scale: float, pixel scale
        seed: int, random seed
    
    Returns:
        patch: 2D array with injected signal
    """
    # Generate background Gaussian field
    background = generate_gaussian_field(size, seed=seed, smoothing=2.0)
    
    # Generate grid pattern with same seed offset
    signal = generate_synthetic_grid(size, tilt_deg, pix_scale=pix_scale, seed=seed+1000)
    
    # Compute signal strength based on SNR
    # epsilon = snr * std(background) / std(signal)
    std_bg = np.std(background)
    std_sig = np.std(signal)
    epsilon = snr * std_bg / std_sig if std_sig > 0 else snr
    
    # Combine
    patch = background + epsilon * signal
    
    return patch.astype(np.float32)


# =========================
# PROCESSING FUNCTIONS
# =========================

def apodize_2d(patch, alpha=0.2):
    """
    Apply a 2D taper window (Tukey) to reduce edge ringing.
    
    Args:
        patch: 2D array
        alpha: Tukey window parameter (0=rect, 1=Hann)
    
    Returns:
        patch_windowed: windowed patch
        window: 2D window function
    """
    ny, nx = patch.shape
    wx = windows.tukey(nx, alpha=alpha)
    wy = windows.tukey(ny, alpha=alpha)
    w2 = np.outer(wy, wx).astype(np.float32)
    
    x = patch * w2
    return x, w2


def fft_power(patch):
    """
    Compute centered FFT power spectrum.
    
    Args:
        patch: 2D array
    
    Returns:
        power: 2D FFT power spectrum
    """
    f = np.fft.fft2(patch)
    f = np.fft.fftshift(f)
    p = np.abs(f) ** 2
    return p


def angle_map(ny, nx):
    """
    Return angle (radians) of each FFT pixel w.r.t. center.
    
    Args:
        ny, nx: dimensions
    
    Returns:
        ang: angle map in radians [-pi, pi]
        r: radius map
    """
    y = np.arange(ny) - ny // 2
    x = np.arange(nx) - nx // 2
    X, Y = np.meshgrid(x, y)
    ang = np.arctan2(Y, X)  # [-pi, pi]
    r = np.sqrt(X * X + Y * Y)
    return ang, r


def oriented_energy(P, ang, r, rmin=10, rmax=None, theta_deg=0.0, dtheta_deg=0.25):
    """
    Measure energy in an angular wedge around theta and theta+pi (both directions),
    within radial band [rmin, rmax].
    
    Args:
        P: 2D FFT power spectrum
        ang: angle map
        r: radius map
        rmin, rmax: radial band limits
        theta_deg: central angle in degrees
        dtheta_deg: wedge half-width in degrees
    
    Returns:
        energy: total energy in wedge
    """
    if rmax is None:
        rmax = r.max()
    theta = np.deg2rad(theta_deg)
    dtheta = np.deg2rad(dtheta_deg)
    
    # wrap angle distance
    def angdist(a, b):
        d = np.angle(np.exp(1j * (a - b)))
        return np.abs(d)
    
    sel_r = (r >= rmin) & (r <= rmax)
    
    sel1 = sel_r & (angdist(ang, theta) <= dtheta)
    sel2 = sel_r & (angdist(ang, theta + np.pi) <= dtheta)
    return float(P[sel1].sum() + P[sel2].sum())


def scan_tilt(P, ang, r, rmin=10, rmax=None, scan_deg=(-5, 5), step_deg=0.05, wedge_deg=0.25):
    """
    Scan for the angle maximizing oriented energy.
    
    Args:
        P: 2D FFT power spectrum
        ang: angle map
        r: radius map
        rmin, rmax: radial band limits
        scan_deg: tuple, (min_angle, max_angle) to scan
        step_deg: angle resolution
        wedge_deg: wedge half-width
    
    Returns:
        best_angle: angle in degrees with maximum energy
        angles: array of scanned angles
        energies: array of energies at each angle
    """
    angles = np.arange(scan_deg[0], scan_deg[1] + 1e-9, step_deg)
    energies = np.array([
        oriented_energy(P, ang, r, rmin=rmin, rmax=rmax, 
                       theta_deg=a, dtheta_deg=wedge_deg)
        for a in angles
    ], dtype=np.float64)
    best_idx = int(np.argmax(energies))
    return angles[best_idx], angles, energies


# =========================
# MAIN PIPELINE
# =========================

def main():
    parser = argparse.ArgumentParser(
        description="UBT CMB 2D FFT PoC - Standalone version with synthetic data"
    )
    parser.add_argument(
        "--mode",
        choices=["synthetic_grid", "gaussian_field", "injected"],
        default="gaussian_field",
        help="Data generation mode (default: gaussian_field)"
    )
    parser.add_argument(
        "--tilt_deg",
        type=float,
        default=np.degrees(np.arctan(1/256)),
        help="Target tilt angle in degrees (default: arctan(1/256) ≈ 0.224°)"
    )
    parser.add_argument(
        "--size",
        type=int,
        default=512,
        help="Patch size in pixels (default: 512)"
    )
    parser.add_argument(
        "--pix_scale",
        type=float,
        default=1.0,
        help="Pixel scale (optional, default: 1.0)"
    )
    parser.add_argument(
        "--snr",
        type=float,
        default=0.2,
        help="Signal-to-noise ratio for injected mode (default: 0.2)"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed (default: 0)"
    )
    parser.add_argument(
        "--outdir",
        type=str,
        default="research_front/cmb_2d_fft/out",
        help="Output directory for figures (default: research_front/cmb_2d_fft/out)"
    )
    
    args = parser.parse_args()
    
    # Create output directory
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("UBT CMB 2D FFT Proof-of-Concept (Standalone)")
    print("=" * 60)
    print(f"Mode: {args.mode}")
    print(f"Target tilt: {args.tilt_deg:.6f}°")
    print(f"Patch size: {args.size}x{args.size}")
    print(f"Random seed: {args.seed}")
    if args.mode == "injected":
        print(f"SNR: {args.snr}")
    print(f"Output directory: {outdir}")
    print()
    
    # Generate patch based on mode
    if args.mode == "synthetic_grid":
        patch = generate_synthetic_grid(
            args.size, args.tilt_deg, pix_scale=args.pix_scale, seed=args.seed
        )
        print("Generated: Synthetic grid with tilt")
    elif args.mode == "gaussian_field":
        patch = generate_gaussian_field(args.size, seed=args.seed)
        print("Generated: Gaussian random field (null control)")
    elif args.mode == "injected":
        patch = generate_injected(
            args.size, args.tilt_deg, snr=args.snr, 
            pix_scale=args.pix_scale, seed=args.seed
        )
        print(f"Generated: Injected signal (SNR={args.snr})")
    
    # Remove mean
    patch0 = patch - patch.mean()
    
    # Apodize
    patch_w, win = apodize_2d(patch0, alpha=0.2)
    
    # FFT power
    P = fft_power(patch_w)
    P_log = np.log1p(P)  # stabilize dynamic range
    
    # Smooth FFT power slightly
    SMOOTH_SIGMA_PIX = 1.5
    P_s = gaussian_filter(P_log, sigma=SMOOTH_SIGMA_PIX)
    
    ang, r = angle_map(*P_s.shape)
    
    # Scan small angles around 0 deg to find tiny tilt
    best, angles, energies = scan_tilt(
        P_s, ang, r,
        rmin=20, rmax=r.max() * 0.9,
        scan_deg=(-2, 2),
        step_deg=0.05,
        wedge_deg=0.25
    )
    
    # Compute confidence proxy: peak/median ratio
    median_energy = np.median(energies)
    peak_energy = np.max(energies)
    confidence = peak_energy / median_energy if median_energy > 0 else 0.0
    
    print("-" * 60)
    print("RESULTS:")
    print(f"  Best detected tilt angle: {best:.6f}°")
    print(f"  Target tilt angle:        {args.tilt_deg:.6f}°")
    print(f"  Difference:               {abs(best - args.tilt_deg):.6f}°")
    print(f"  Confidence (peak/median): {confidence:.3f}")
    print("-" * 60)
    print()
    
    # =========================
    # SAVE FIGURES
    # =========================
    
    # Figure 1: Patch
    fig1, ax1 = plt.subplots(figsize=(8, 7))
    ax1.set_title(f"Input Patch ({args.mode})")
    im1 = ax1.imshow(patch0, origin="lower", cmap='RdBu_r')
    plt.colorbar(im1, ax=ax1, fraction=0.046)
    ax1.set_xlabel("x (pixels)")
    ax1.set_ylabel("y (pixels)")
    patch_path = outdir / "patch.png"
    plt.savefig(patch_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {patch_path}")
    plt.close(fig1)
    
    # Figure 2: FFT power
    fig2, ax2 = plt.subplots(figsize=(8, 7))
    ax2.set_title("FFT Power (log-scale, smoothed)")
    im2 = ax2.imshow(P_s, origin="lower", cmap='viridis')
    plt.colorbar(im2, ax=ax2, fraction=0.046)
    ax2.set_xlabel("kx (pixels)")
    ax2.set_ylabel("ky (pixels)")
    fft_path = outdir / "fft_power.png"
    plt.savefig(fft_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {fft_path}")
    plt.close(fig2)
    
    # Figure 3: Energy vs angle
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.set_title("Oriented Energy vs Angle")
    ax3.plot(angles, energies, linewidth=2, label='Measured energy')
    ax3.axvline(args.tilt_deg, linestyle="--", color='red', 
                label=f"Target: {args.tilt_deg:.4f}°")
    ax3.axvline(best, linestyle="-", color='green', 
                label=f"Best: {best:.4f}°")
    ax3.set_xlabel("Angle (degrees)")
    ax3.set_ylabel("Energy (a.u.)")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    energy_path = outdir / "energy_vs_angle.png"
    plt.savefig(energy_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {energy_path}")
    plt.close(fig3)
    
    print()
    print("=" * 60)
    print("Analysis complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

