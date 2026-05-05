# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
complex_phase_scan.py
=====================
Numerical scan of the UBT effective potential extended to the complex domain.

Theory:
  V(q) = q^2 - B*q*ln(q),  q = r * exp(i*theta)

  Re(V) = r^2*cos(2*theta) - B*r*(ln(r)*cos(theta) - theta*sin(theta))
  Im(V) = r^2*sin(2*theta) - B*r*(ln(r)*sin(theta) + theta*cos(theta))

  B(p) = (p+1)/3  for prime p

  Stable primes (real domain): {2, 127, 137, 139, 151, 157}

Stationarity conditions (dV/dr = dV/dtheta = 0):
  (A)  2*r*cos(theta) = B*(ln(r) + 1)
  (B)  2*r*sin(theta) = B*theta

Sweep:
  r     in [100, 200]  (100 points)
  theta in [0, 2*pi]   (360 points)

Outputs:
  plots/complex_phase_landscape.png    -- 2-D heatmap of Re(V) and gradient norm
  plots/phase_minima_distribution.png  -- locations of gradient minima
  stdout: summary of stable (r, theta) points

Usage:
    python src/ubt_theta_lab/complex_phase_scan.py
    python src/ubt_theta_lab/complex_phase_scan.py --output-dir /path/to/plots
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import List, Tuple


# ---------------------------------------------------------------------------
# Core potential functions
# ---------------------------------------------------------------------------

def V_real(q: float, B: float) -> float:
    """Real-domain effective potential V(q) = q^2 - B*q*ln(q)."""
    if q <= 0:
        return float("inf")
    return q * q - B * q * math.log(q)


def V_complex(r: float, theta: float, B: float) -> complex:
    """
    Complex extension V(r*exp(i*theta)).

    Returns the full complex value of V.
    """
    if r <= 0:
        return complex(float("nan"), float("nan"))
    ln_r = math.log(r)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    cos_2t = math.cos(2 * theta)
    sin_2t = math.sin(2 * theta)

    re_part = r * r * cos_2t - B * r * (ln_r * cos_t - theta * sin_t)
    im_part = r * r * sin_2t - B * r * (ln_r * sin_t + theta * cos_t)
    return complex(re_part, im_part)


def gradient_norm(r: float, theta: float, B: float) -> float:
    """
    Norm of the complex gradient of V at (r, theta).

    The gradient is proportional to:
        G = 2*r*exp(i*theta) - B*(ln(r) + 1 + i*theta)
    Both dV/dr and dV/dtheta vanish iff G = 0.
    """
    if r <= 0:
        return float("inf")
    ln_r = math.log(r)
    g_re = 2 * r * math.cos(theta) - B * (ln_r + 1)
    g_im = 2 * r * math.sin(theta) - B * theta
    return math.hypot(g_re, g_im)


def B_of_prime(p: int) -> float:
    """Return B = (p+1)/3 for a given prime p."""
    return (p + 1) / 3


# ---------------------------------------------------------------------------
# Prime utilities
# ---------------------------------------------------------------------------

def sieve_primes(limit: int) -> List[int]:
    """Sieve of Eratosthenes."""
    if limit < 2:
        return []
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i :: i] = bytearray(len(is_prime[i * i :: i]))
    return [i for i in range(2, limit + 1) if is_prime[i]]


STABLE_PRIMES = [2, 127, 137, 139, 151, 157]
PRIMES_200 = [p for p in sieve_primes(200) if 100 <= p <= 200]


# ---------------------------------------------------------------------------
# Grid scan
# ---------------------------------------------------------------------------

def build_grid(
    r_min: float = 100.0,
    r_max: float = 200.0,
    n_r: int = 200,
    n_theta: int = 360,
    B: float = 46.0,
) -> Tuple:
    """
    Compute Re(V), Im(V), and gradient norm on a (r, theta) grid.

    Returns
    -------
    r_vals    : list of r values
    t_vals    : list of theta values
    re_grid   : 2-D array (n_r x n_theta) of Re(V)
    im_grid   : 2-D array (n_r x n_theta) of Im(V)
    grad_grid : 2-D array (n_r x n_theta) of gradient norm
    """
    import numpy as np

    r_vals = np.linspace(r_min, r_max, n_r)
    t_vals = np.linspace(0, 2 * math.pi, n_theta, endpoint=False)

    re_grid = np.empty((n_r, n_theta))
    im_grid = np.empty((n_r, n_theta))
    grad_grid = np.empty((n_r, n_theta))

    for i, r in enumerate(r_vals):
        ln_r = math.log(r)
        for j, theta in enumerate(t_vals):
            cos_t = math.cos(theta)
            sin_t = math.sin(theta)
            re_grid[i, j] = (r * r * math.cos(2 * theta)
                             - B * r * (ln_r * cos_t - theta * sin_t))
            im_grid[i, j] = (r * r * math.sin(2 * theta)
                             - B * r * (ln_r * sin_t + theta * cos_t))
            g_re = 2 * r * cos_t - B * (ln_r + 1)
            g_im = 2 * r * sin_t - B * theta
            grad_grid[i, j] = math.hypot(g_re, g_im)

    return r_vals, t_vals, re_grid, im_grid, grad_grid


# ---------------------------------------------------------------------------
# Local-minimum finder in the gradient-norm landscape
# ---------------------------------------------------------------------------

def find_gradient_minima(
    r_vals, t_vals, grad_grid, threshold: float = 5.0
) -> List[dict]:
    """
    Identify grid cells where the gradient norm is below `threshold`.

    Returns a list of dicts with keys: r, theta, grad_norm.
    """
    import numpy as np

    minima = []
    n_r, n_theta = grad_grid.shape
    for i in range(n_r):
        for j in range(n_theta):
            g = grad_grid[i, j]
            if g < threshold:
                # Check local minimum in 8-neighbourhood
                i_lo, i_hi = max(0, i - 1), min(n_r - 1, i + 1)
                j_lo, j_hi = max(0, j - 1), min(n_theta - 1, j + 1)
                neighbourhood = grad_grid[i_lo:i_hi + 1, j_lo:j_hi + 1]
                if g <= neighbourhood.min():
                    minima.append({
                        "r": float(r_vals[i]),
                        "theta": float(t_vals[j]),
                        "grad_norm": g,
                    })
    return minima


# ---------------------------------------------------------------------------
# Stationarity condition residual check (for validation)
# ---------------------------------------------------------------------------

def stationary_residual(r: float, theta: float, B: float) -> float:
    """
    Returns |G|^2 where G = 2r*exp(i*theta) - B*(ln(r)+1+i*theta).
    Zero iff (r, theta) is a stationary point.
    """
    return gradient_norm(r, theta, B) ** 2


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def make_plots(
    r_vals, t_vals, re_grid, im_grid, grad_grid,
    minima: List[dict],
    B: float,
    output_dir: Path,
) -> None:
    """Generate and save the two required plots."""
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("[WARNING] matplotlib not available; skipping plots.", file=sys.stderr)
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    T, R = np.meshgrid(t_vals, r_vals)

    # ── Plot 1: Re(V) heatmap + gradient-norm contour ──────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    vmin_re = float(np.percentile(re_grid, 2))
    vmax_re = float(np.percentile(re_grid, 98))

    ax = axes[0]
    im = ax.pcolormesh(T, R, re_grid, cmap="viridis",
                       vmin=vmin_re, vmax=vmax_re, shading="auto")
    ax.contour(T, R, re_grid, levels=20, colors="white", linewidths=0.4, alpha=0.5)
    plt.colorbar(im, ax=ax, label=r"$\Re V(r,\theta)$")
    ax.set_xlabel(r"$\theta$ (rad)")
    ax.set_ylabel(r"$r$")
    ax.set_title(rf"$\Re V(r,\theta)$, $B={B:.3f}$")
    ax.set_xticks([0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi])
    ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])

    ax2 = axes[1]
    log_grad = np.log10(grad_grid + 1e-10)
    im2 = ax2.pcolormesh(T, R, log_grad, cmap="plasma", shading="auto")
    ax2.contour(T, R, log_grad, levels=10, colors="white", linewidths=0.4, alpha=0.5)
    plt.colorbar(im2, ax=ax2, label=r"$\log_{10}|\nabla V|$")
    ax2.set_xlabel(r"$\theta$ (rad)")
    ax2.set_ylabel(r"$r$")
    ax2.set_title(r"Gradient norm $\log_{10}|\nabla V|$")
    ax2.set_xticks([0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi])
    ax2.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])

    # Mark stable primes on real axis
    for p in STABLE_PRIMES:
        if r_vals[0] <= p <= r_vals[-1]:
            for ax_ in axes:
                ax_.axhline(p, color="red", linewidth=0.8, linestyle="--", alpha=0.7)
                ax_.text(0.05, p + 0.5, str(p), color="red", fontsize=7)

    # Mark gradient minima
    if minima:
        m_theta = [m["theta"] for m in minima]
        m_r = [m["r"] for m in minima]
        axes[1].scatter(m_theta, m_r, c="cyan", s=20, zorder=5,
                        label="gradient minima")
        axes[1].legend(fontsize=8)

    fig.suptitle(
        rf"UBT Complex Phase Landscape: $V(r\,e^{{i\theta}}) = r^2 e^{{2i\theta}}"
        rf" - B\,r\,e^{{i\theta}}(\ln r + i\theta)$",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    path1 = output_dir / "complex_phase_landscape.png"
    fig.savefig(path1, dpi=150)
    plt.close(fig)
    print(f"[INFO] Saved {path1}")

    # ── Plot 2: Phase-minima distribution ──────────────────────────────────
    fig2, axes2 = plt.subplots(1, 2, figsize=(13, 5))

    # Left: Re(V) slice at theta=0 vs r, comparing real-domain V
    ax3 = axes2[0]
    r_arr = np.array(r_vals)
    re_slice_theta0 = re_grid[:, 0]
    real_V = r_arr ** 2 - B * r_arr * np.log(r_arr)
    ax3.plot(r_arr, re_slice_theta0, "b-", label=r"$\Re V(r, 0)$")
    ax3.plot(r_arr, real_V, "r--", linewidth=1.5, label=r"$V_{\rm real}(r)$")
    for p in STABLE_PRIMES:
        if r_vals[0] <= p <= r_vals[-1]:
            ax3.axvline(p, color="gray", linewidth=0.7, linestyle=":")
            ax3.text(p + 0.3, ax3.get_ylim()[0] if ax3.get_ylim()[0] > -1e5 else 0,
                     str(p), fontsize=7, color="gray")
    ax3.set_xlabel(r"$r$")
    ax3.set_ylabel(r"$V$")
    ax3.set_title(r"$\theta = 0$ slice: $\Re V$ vs real $V$")
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    # Right: scatter of gradient minima
    ax4 = axes2[1]
    if minima:
        m_r_arr = [m["r"] for m in minima]
        m_t_arr = [m["theta"] for m in minima]
        m_g_arr = [m["grad_norm"] for m in minima]
        sc = ax4.scatter(m_t_arr, m_r_arr, c=m_g_arr, cmap="hot_r",
                         s=40, zorder=5)
        plt.colorbar(sc, ax=ax4, label=r"$|\nabla V|$")
    for p in STABLE_PRIMES:
        if r_vals[0] <= p <= r_vals[-1]:
            ax4.axhline(p, color="blue", linewidth=0.8, linestyle="--", alpha=0.6)
            ax4.text(0.05, p + 0.5, str(p), color="blue", fontsize=7)
    ax4.set_xlabel(r"$\theta$ (rad)")
    ax4.set_ylabel(r"$r$")
    ax4.set_title("Gradient minima distribution")
    ax4.set_xticks([0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi])
    ax4.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax4.grid(True, alpha=0.3)

    fig2.suptitle("Phase Minima Distribution — UBT Complex Phase Scan", fontsize=11)
    fig2.tight_layout(rect=[0, 0, 1, 0.95])
    path2 = output_dir / "phase_minima_distribution.png"
    fig2.savefig(path2, dpi=150)
    plt.close(fig2)
    print(f"[INFO] Saved {path2}")


# ---------------------------------------------------------------------------
# Main scan loop
# ---------------------------------------------------------------------------

def run_scan(
    r_min: float = 100.0,
    r_max: float = 200.0,
    n_r: int = 200,
    n_theta: int = 360,
    B: float = 46.0,
    grad_threshold: float = 5.0,
    output_dir: Path = Path("plots"),
    verbose: bool = True,
) -> List[dict]:
    """
    Run the full complex phase scan and return list of near-stationary points.
    """
    if verbose:
        print(f"[INFO] Scanning r in [{r_min}, {r_max}] ({n_r} pts), "
              f"theta in [0, 2pi] ({n_theta} pts), B={B:.4f}")

    r_vals, t_vals, re_grid, im_grid, grad_grid = build_grid(
        r_min, r_max, n_r, n_theta, B
    )

    minima = find_gradient_minima(r_vals, t_vals, grad_grid, threshold=grad_threshold)

    if verbose:
        print(f"[INFO] Found {len(minima)} near-stationary points "
              f"(|grad| < {grad_threshold})")

    # Separate into real-axis (|theta| < 0.05 or |theta - 2pi| < 0.05) and off-axis
    real_axis = [m for m in minima
                 if m["theta"] < 0.05 or abs(m["theta"] - 2 * math.pi) < 0.05]
    off_axis = [m for m in minima
                if not (m["theta"] < 0.05 or abs(m["theta"] - 2 * math.pi) < 0.05)]

    if verbose:
        print(f"[INFO]   on real axis (theta ~ 0):  {len(real_axis)} points")
        print(f"[INFO]   off-axis (theta != 0):     {len(off_axis)} points")
        if real_axis:
            print("\nReal-axis stationary points (r, theta, |grad|):")
            for m in sorted(real_axis, key=lambda x: x["r"]):
                print(f"  r={m['r']:7.2f}  theta={m['theta']:.4f}  |grad|={m['grad_norm']:.4e}")
        if off_axis:
            print("\nOFF-AXIS stationary points (r, theta, |grad|):")
            for m in sorted(off_axis, key=lambda x: x["grad_norm"]):
                print(f"  r={m['r']:7.2f}  theta={m['theta']:.4f}  |grad|={m['grad_norm']:.4e}")
        else:
            print("\n[RESULT] No off-axis stationary points found in scan range.")

    make_plots(r_vals, t_vals, re_grid, im_grid, grad_grid, minima, B, output_dir)
    return minima


# ---------------------------------------------------------------------------
# Per-prime stability check
# ---------------------------------------------------------------------------

def check_prime_sectors(
    primes: List[int] = STABLE_PRIMES,
    n_r: int = 200,
    n_theta: int = 360,
    grad_threshold: float = 5.0,
    output_dir: Path = Path("plots"),
    verbose: bool = True,
) -> dict:
    """
    For each stable prime p, use B = B(p) and scan r in [p-30, p+30].
    Report how many sectors (distinct theta basins) contain near-stationary points.
    """
    results = {}
    for p in primes:
        if p < 10:
            continue  # skip p=2 (too small for log analysis)
        B = B_of_prime(p)
        r_lo = max(2.0, p - 30)
        r_hi = p + 30
        r_vals, t_vals, _, _, grad_grid = build_grid(
            r_lo, r_hi, n_r, n_theta, B
        )
        mins = find_gradient_minima(r_vals, t_vals, grad_grid, threshold=grad_threshold)
        off = [m for m in mins
               if not (m["theta"] < 0.05 or abs(m["theta"] - 2 * math.pi) < 0.05)]
        results[p] = {
            "B": B,
            "total_minima": len(mins),
            "off_axis_minima": len(off),
            "sectors": 1 + (1 if off else 0),
        }
        if verbose:
            print(f"  p={p:3d}  B={B:.3f}  total_mins={len(mins):3d}  "
                  f"off-axis={len(off):3d}  sectors={results[p]['sectors']}")
    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="UBT complex phase scan: V(q) = q^2 - B*q*ln(q), q=r*exp(i*theta)"
    )
    parser.add_argument("--r-min", type=float, default=100.0,
                        help="Minimum r (default: 100)")
    parser.add_argument("--r-max", type=float, default=200.0,
                        help="Maximum r (default: 200)")
    parser.add_argument("--n-r", type=int, default=200,
                        help="Grid points in r (default: 200)")
    parser.add_argument("--n-theta", type=int, default=360,
                        help="Grid points in theta (default: 360)")
    parser.add_argument("--B", type=float, default=46.0,
                        help="B coefficient (default: 46.0 ≈ B(137))")
    parser.add_argument("--threshold", type=float, default=5.0,
                        help="Gradient-norm threshold for minima detection (default: 5.0)")
    parser.add_argument("--output-dir", type=Path, default=Path("plots"),
                        help="Directory for output plots (default: plots/)")
    parser.add_argument("--per-prime", action="store_true",
                        help="Run per-stable-prime sector analysis")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("=" * 60)
    print("UBT Complex Phase Scan")
    print("V(q) = q^2 - B*q*ln(q),  q = r*exp(i*theta)")
    print("Stable primes (real domain):", STABLE_PRIMES)
    print("=" * 60)

    minima = run_scan(
        r_min=args.r_min,
        r_max=args.r_max,
        n_r=args.n_r,
        n_theta=args.n_theta,
        B=args.B,
        grad_threshold=args.threshold,
        output_dir=args.output_dir,
        verbose=True,
    )

    if args.per_prime:
        print("\n" + "=" * 60)
        print("Per-prime sector analysis:")
        print("=" * 60)
        results = check_prime_sectors(
            primes=STABLE_PRIMES,
            n_r=args.n_r,
            n_theta=args.n_theta,
            grad_threshold=args.threshold,
            output_dir=args.output_dir,
            verbose=True,
        )
        print("\nSummary:")
        for p, res in results.items():
            print(f"  p={p}: {res['sectors']} sector(s), "
                  f"off-axis minima={res['off_axis_minima']}")

    print("\n[DONE]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
