# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
connect_prime_stability_to_spectrum.py
======================================

Task: connect_prime_stability_to_spectrum

Tests whether prime-stable primes (primes p for which the UBT ψ-mode
dynamics has a stable fixed point — i.e. all primes, by the Prime Attractor
Theorem) correspond to special features in the spectrum of the ψ-sector
Hamiltonian H_ψ.

Background
----------
From ubt_hamiltonian_trace_formula.md (Definition 2.1):

    H_ψ = −d²/dψ²  +  V_eff(ψ)

acting on L²(S¹_ψ) with periodic boundary conditions on ψ ∈ [0, L_ψ).

The effective potential V_eff arises from the UBT biquaternion field.  In the
KK expansion Θ(x,ψ) = Σ_n a_n(x) exp(inψ), prime-indexed modes a_p are
asymptotically stable (no resonant submode mixing), while composite-indexed
modes are unstable.

Energy mapping
--------------
For the flat Laplacian the KK energy of mode n is

    E_n = (2π n / L_ψ)²

For L_ψ = 2π this simplifies to E(n) = n².  We treat E(p) = p² as the
candidate energy scale for prime p.

Checks performed
----------------
  1. Are prime energy values E(p) = p² near local **maxima** of ρ(E)?
     (would indicate prime modes sit in spectral bands)
  2. Do they align with **spectral gaps** (ρ near zero between bands)?
     (would indicate prime modes are gapped, hence protected)
  3. Do **twin prime** pairs (p, p+2) correspond to near-**degeneracy** in
     the spectrum, i.e. a pair of eigenvalues near E(p) and E(p+2)?

Deliverables
------------
  * plot  : spectrum_vs_primes.png  (saved next to this script)
  * table : printed to stdout; also returned by analyse()
  * conclusion : printed to stdout; also returned by analyse()

Status / Caveats
----------------
All ζ-related conjectures (G1–G6 in gap_inventory.md) remain open.  This
script is a **numerical exploration** on a *model* V_eff; it does not
constitute a proof of any spectral property.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import NamedTuple

import numpy as np


# ---------------------------------------------------------------------------
# Prime helpers
# ---------------------------------------------------------------------------

def sieve_primes(n_max: int) -> list[int]:
    """Return all primes p ≤ n_max via the Sieve of Eratosthenes."""
    if n_max < 2:
        return []
    sieve = bytearray([1]) * (n_max + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i in range(2, n_max + 1) if sieve[i]]


def twin_prime_pairs(primes: list[int], gap: int = 2) -> list[tuple[int, int]]:
    """Return all (p, p+gap) pairs where both are prime."""
    prime_set = set(primes)
    return [(p, p + gap) for p in primes if (p + gap) in prime_set]


# ---------------------------------------------------------------------------
# H_ψ construction
# ---------------------------------------------------------------------------

def build_H_psi(
    N: int = 400,
    L_psi: float = 2 * math.pi,
    kappa: float = 1.0,
    potential: str = "cos",
) -> tuple[np.ndarray, np.ndarray]:
    """
    Build the finite-difference matrix for H_ψ = −d²/dψ² + V_eff(ψ) on
    the circle [0, L_ψ) with periodic boundary conditions.

    Parameters
    ----------
    N       : Number of grid points.
    L_psi   : Period of the circle.
    kappa   : Coupling constant for V_eff.
    potential : Shape of V_eff.  Options:
                "cos"   → V_eff(ψ) = κ (1 − cos ψ)   (quantum pendulum)
                "cos2"  → V_eff(ψ) = κ cos²(ψ)        (double-well-like)
                "flat"  → V_eff(ψ) = 0                 (free Laplacian)

    Returns
    -------
    psi_grid : ndarray, shape (N,)
    eigenvalues : ndarray of real eigenvalues, sorted ascending.
    """
    dpsi = L_psi / N
    psi = np.linspace(0.0, L_psi, N, endpoint=False)

    # Kinetic matrix T = −d²/dψ²  via second-order central differences
    t_diag = np.full(N, 2.0 / dpsi**2)
    t_off = np.full(N - 1, -1.0 / dpsi**2)
    T = np.diag(t_diag) + np.diag(t_off, 1) + np.diag(t_off, -1)
    # Periodic boundary: wrap-around corners
    T[0, -1] = -1.0 / dpsi**2
    T[-1, 0] = -1.0 / dpsi**2

    # Effective potential
    if potential == "cos":
        V = kappa * (1.0 - np.cos(psi))
    elif potential == "cos2":
        V = kappa * np.cos(psi) ** 2
    elif potential == "flat":
        V = np.zeros(N)
    else:
        raise ValueError(f"Unknown potential '{potential}'")

    H = T + np.diag(V)
    eigenvalues = np.linalg.eigvalsh(H)
    return psi, eigenvalues


# ---------------------------------------------------------------------------
# Spectral density
# ---------------------------------------------------------------------------

def spectral_density(
    eigenvalues: np.ndarray,
    E_grid: np.ndarray,
    bandwidth: float | None = None,
) -> np.ndarray:
    """
    Gaussian KDE estimate of ρ(E) evaluated on *E_grid*.

    Parameters
    ----------
    eigenvalues : sorted eigenvalue array (output of build_H_psi).
    E_grid      : 1-D array of energies at which to evaluate ρ.
    bandwidth   : KDE bandwidth σ.  Defaults to Silverman's rule.

    Returns
    -------
    rho : ndarray, same shape as E_grid.
    """
    N = len(eigenvalues)
    if bandwidth is None:
        # Silverman's rule of thumb
        std = float(np.std(eigenvalues))
        bandwidth = 1.06 * std * N ** (-0.2)
        bandwidth = max(bandwidth, 1e-6)

    rho = np.zeros(len(E_grid))
    for lam in eigenvalues:
        rho += np.exp(-0.5 * ((E_grid - lam) / bandwidth) ** 2)
    rho /= N * bandwidth * math.sqrt(2 * math.pi)
    return rho


# ---------------------------------------------------------------------------
# Spectral feature extraction
# ---------------------------------------------------------------------------

def find_local_maxima(rho: np.ndarray, E_grid: np.ndarray) -> np.ndarray:
    """Return energies at which ρ has a local maximum (simple ±1 neighbour)."""
    idx = np.where((rho[1:-1] > rho[:-2]) & (rho[1:-1] > rho[2:]))[0] + 1
    return E_grid[idx]


def find_spectral_gaps(
    eigenvalues: np.ndarray, min_gap: float = 0.5
) -> list[tuple[float, float]]:
    """
    Return list of (E_lo, E_hi) pairs where the gap E_hi − E_lo ≥ min_gap.

    Uses sorted eigenvalues; a gap is the interval between consecutive ones.
    """
    ev = np.sort(eigenvalues)
    gaps = []
    for i in range(len(ev) - 1):
        delta = ev[i + 1] - ev[i]
        if delta >= min_gap:
            gaps.append((float(ev[i]), float(ev[i + 1])))
    return gaps


def nearest_eigenvalue(E: float, eigenvalues: np.ndarray) -> tuple[float, float]:
    """Return (nearest_eigenvalue, distance) for a query energy E."""
    idx = int(np.argmin(np.abs(eigenvalues - E)))
    return float(eigenvalues[idx]), abs(float(eigenvalues[idx]) - E)


# ---------------------------------------------------------------------------
# Analysis result type
# ---------------------------------------------------------------------------

class PrimeSpectralRecord(NamedTuple):
    p: int
    E_p: float
    rho_E_p: float
    nearest_ev: float
    dist_to_ev: float
    in_gap: bool
    gap_lo: float | None
    gap_hi: float | None
    near_maximum: bool
    is_twin: bool
    twin_partner: int | None
    # degeneracy check for twin pairs
    twin_near_degenerate: bool | None


# ---------------------------------------------------------------------------
# Core analysis
# ---------------------------------------------------------------------------

def analyse(
    N: int = 400,
    L_psi: float = 2 * math.pi,
    kappa: float = 1.0,
    potential: str = "cos",
    p_max: int = 30,
    gap_threshold: float = 0.5,
    max_near: float = 0.3,
    rho_max_tol: float = 0.15,
    twin_degen_tol: float = 0.5,
) -> tuple[list[PrimeSpectralRecord], str]:
    """
    Run the prime-stability vs H_ψ spectrum analysis.

    Parameters
    ----------
    N           : Grid points for H_ψ discretization.
    L_psi       : Circle period.
    kappa       : V_eff coupling constant.
    potential   : V_eff shape ("cos", "cos2", "flat").
    p_max       : Check all primes p ≤ p_max.
    gap_threshold : Minimum gap size to be considered a spectral gap.
    max_near    : |E(p) − E_local_max| / E(p)  threshold for "near maximum".
    rho_max_tol : Fraction of rho range used for "near maximum" via density.
    twin_degen_tol : Two eigenvalues within this distance count as degenerate.

    Returns
    -------
    records    : List of PrimeSpectralRecord for each prime p ≤ p_max.
    conclusion : Multiline string summarising findings.
    """
    # --- Build spectrum -------------------------------------------------------
    psi_grid, eigenvalues = build_H_psi(N=N, L_psi=L_psi, kappa=kappa,
                                        potential=potential)

    # Energy grid for ρ(E)
    E_min = max(0.0, float(eigenvalues[0]) - 2.0)
    # Use largest prime energy as upper bound + buffer
    primes = sieve_primes(p_max)
    E_max_prime = float(max(primes)) ** 2 + 10.0
    E_max = max(float(eigenvalues[-1]) + 2.0, E_max_prime)
    E_grid = np.linspace(E_min, E_max, 5000)

    rho = spectral_density(eigenvalues, E_grid)

    # Spectral features
    gap_list = find_spectral_gaps(eigenvalues, min_gap=gap_threshold)
    local_maxima = find_local_maxima(rho, E_grid)

    rho_mean = float(np.mean(rho))
    rho_range = float(np.max(rho) - np.min(rho))

    # --- Twin prime pairs -----------------------------------------------------
    twin_pairs = twin_prime_pairs(primes)
    twin_set: set[int] = set()
    twin_partner: dict[int, int] = {}
    for p1, p2 in twin_pairs:
        twin_set.add(p1)
        twin_set.add(p2)
        twin_partner[p1] = p2
        twin_partner[p2] = p1

    # --- Per-prime checks -----------------------------------------------------
    records: list[PrimeSpectralRecord] = []
    for p in primes:
        E_p = float(p) ** 2  # KK energy on unit circle (L_ψ = 2π)

        # ρ(E_p)
        rho_Ep = float(np.interp(E_p, E_grid, rho))

        # Nearest eigenvalue
        near_ev, dist_ev = nearest_eigenvalue(E_p, eigenvalues)

        # Is E_p inside a spectral gap?
        in_gap = False
        g_lo = g_hi = None
        for lo, hi in gap_list:
            if lo < E_p < hi:
                in_gap = True
                g_lo, g_hi = lo, hi
                break

        # Is E_p near a local maximum of ρ?
        near_max = False
        if len(local_maxima) > 0:
            dist_to_max = float(np.min(np.abs(local_maxima - E_p)))
            near_max = dist_to_max / (E_p + 1e-9) < max_near

        # Twin-prime degeneracy check
        is_twin = p in twin_set
        t_partner = twin_partner.get(p)
        twin_degen = None
        if is_twin and t_partner is not None and t_partner > p:
            E_p2 = float(t_partner) ** 2
            ev1, _ = nearest_eigenvalue(E_p, eigenvalues)
            ev2, _ = nearest_eigenvalue(E_p2, eigenvalues)
            twin_degen = abs(ev2 - ev1) < twin_degen_tol

        records.append(PrimeSpectralRecord(
            p=p,
            E_p=E_p,
            rho_E_p=rho_Ep,
            nearest_ev=near_ev,
            dist_to_ev=dist_ev,
            in_gap=in_gap,
            gap_lo=g_lo,
            gap_hi=g_hi,
            near_maximum=near_max,
            is_twin=is_twin,
            twin_partner=t_partner,
            twin_near_degenerate=twin_degen,
        ))

    # --- Conclusion -----------------------------------------------------------
    n_near_max = sum(1 for r in records if r.near_maximum)
    n_in_gap = sum(1 for r in records if r.in_gap)
    twin_records = [r for r in records if r.is_twin and r.twin_partner is not None
                    and r.twin_near_degenerate is not None]
    n_twin_degen = sum(1 for r in twin_records if r.twin_near_degenerate)

    lines = [
        "=" * 70,
        "CONCLUSION: Prime-Stable Primes vs H_ψ Spectrum",
        "=" * 70,
        f"Parameters: N={N}, L_ψ=2π, V_eff={potential}, κ={kappa}",
        f"Primes checked: {len(records)} (p ≤ {p_max})",
        f"Spectral gaps found (δE ≥ {gap_threshold}): {len(gap_list)}",
        "",
        "Extrema alignment:",
        f"  Primes near spectral density maximum: "
        f"{n_near_max}/{len(records)} "
        f"({100*n_near_max/len(records):.0f}%)",
        "",
        "Gap alignment:",
        f"  Primes whose E(p) falls inside a gap: "
        f"{n_in_gap}/{len(records)} "
        f"({100*n_in_gap/len(records):.0f}%)",
        "",
        "Twin prime degeneracy:",
        f"  Twin pairs checked: {len(twin_records)}",
        f"  Near-degenerate pairs (δλ < {twin_degen_tol}): "
        f"{n_twin_degen}",
        "",
    ]

    # Interpret
    frac_max = n_near_max / len(records) if records else 0.0
    frac_gap = n_in_gap / len(records) if records else 0.0

    if frac_max > 0.5:
        lines.append("Signal: PRIMES CLUSTER NEAR SPECTRAL MAXIMA "
                     "(majority near density peaks).")
    elif frac_gap > 0.5:
        lines.append("Signal: PRIMES CLUSTER IN SPECTRAL GAPS "
                     "(majority in gaps → protected modes).")
    else:
        lines.append("Signal: NO CLEAR STRUCTURAL ALIGNMENT detected for "
                     "this potential / energy mapping.")
        lines.append("  This is consistent with the null hypothesis: E(p)=p²"
                     " hits spectral features randomly.")
    lines.append("")
    lines.append("NOTE: All UBT ζ-connections remain CONJECTURAL (Gaps G1–G6"
                 " in gap_inventory.md).")
    lines.append("  This numerical result is exploratory evidence only.")
    lines.append("=" * 70)

    conclusion = "\n".join(lines)
    return records, conclusion


# ---------------------------------------------------------------------------
# Table formatter
# ---------------------------------------------------------------------------

def format_table(records: list[PrimeSpectralRecord]) -> str:
    """Return a fixed-width ASCII table of the analysis results."""
    header = (
        f"{'p':>4}  {'E(p)':>8}  {'ρ(E(p))':>10}  "
        f"{'near_ev':>10}  {'dist':>7}  "
        f"{'in_gap':>7}  {'near_max':>8}  "
        f"{'twin':>5}  {'degen':>5}"
    )
    sep = "-" * len(header)
    rows = [header, sep]
    for r in records:
        degen_str = (
            "yes" if r.twin_near_degenerate
            else ("no" if r.twin_near_degenerate is False
                  else "  -")
        )
        rows.append(
            f"{r.p:>4}  {r.E_p:>8.1f}  {r.rho_E_p:>10.4e}  "
            f"{r.nearest_ev:>10.3f}  {r.dist_to_ev:>7.3f}  "
            f"{'yes' if r.in_gap else 'no':>7}  "
            f"{'yes' if r.near_maximum else 'no':>8}  "
            f"{'yes' if r.is_twin else 'no':>5}  "
            f"{degen_str:>5}"
        )
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------

def make_plot(
    records: list[PrimeSpectralRecord],
    eigenvalues: np.ndarray,
    E_grid: np.ndarray,
    rho: np.ndarray,
    out_path: Path,
) -> None:
    """Save a three-panel diagnostic figure."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return  # matplotlib not available; skip silently

    primes = [r.p for r in records]
    E_p_vals = [r.E_p for r in records]
    rho_Ep_vals = [r.rho_E_p for r in records]
    is_twin = [r.is_twin for r in records]

    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    fig.suptitle(
        "Prime-Stable Primes vs H_ψ Spectrum\n"
        r"$H_\psi = -\partial^2_\psi + \kappa(1-\cos\psi)$, "
        r"$E(p) = p^2$ (KK mapping, $L_\psi = 2\pi$)",
        fontsize=11,
    )

    # --- Panel 1: eigenvalue staircase ----------------------------------------
    ax = axes[0]
    ev_sorted = np.sort(eigenvalues)
    indices = np.arange(1, len(ev_sorted) + 1)
    ax.step(ev_sorted, indices, where="post", color="steelblue", lw=0.8,
            label="N(E) = #{λ ≤ E}")
    for i, (p, E_p) in enumerate(zip(primes, E_p_vals)):
        col = "red" if is_twin[i] else "darkorange"
        ax.axvline(E_p, color=col, lw=0.8, alpha=0.6)
    ax.set_xlabel("Energy E")
    ax.set_ylabel("N(E)")
    ax.set_xlim(0, max(E_p_vals) * 1.05)
    ax.set_title("Eigenvalue staircase  (orange = prime E(p), red = twin prime)")
    ax.legend(fontsize=8)

    # --- Panel 2: spectral density ρ(E) + prime markers ----------------------
    ax = axes[1]
    ax.plot(E_grid, rho, color="steelblue", lw=1.2, label=r"$\rho(E)$ (KDE)")
    for i, (p, E_p, rho_Ep) in enumerate(zip(primes, E_p_vals, rho_Ep_vals)):
        col = "red" if is_twin[i] else "darkorange"
        ax.axvline(E_p, color=col, lw=0.7, alpha=0.5)
        ax.scatter([E_p], [rho_Ep], color=col, s=25, zorder=5)
    ax.set_xlabel("Energy E")
    ax.set_ylabel(r"$\rho(E)$")
    ax.set_xlim(0, max(E_p_vals) * 1.05)
    ax.set_title(r"Spectral density $\rho(E)$ and prime energy markers")
    ax.legend(fontsize=8)

    # --- Panel 3: ρ(E(p)) bar chart by prime ----------------------------------
    ax = axes[2]
    colors = ["red" if t else "darkorange" for t in is_twin]
    ax.bar(primes, rho_Ep_vals, color=colors, alpha=0.7)
    ax.axhline(float(np.mean(rho_Ep_vals)), color="black", lw=1.0,
               linestyle="--", label="mean ρ(E(p))")
    ax.set_xlabel("Prime p")
    ax.set_ylabel(r"$\rho(E(p))$")
    ax.set_title(r"$\rho(E(p))$ per prime  (red = twin prime)")
    ax.legend(fontsize=8)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Convenience wrapper used by tests (returns raw numerical objects)
# ---------------------------------------------------------------------------

def run(
    N: int = 400,
    L_psi: float = 2 * math.pi,
    kappa: float = 1.0,
    potential: str = "cos",
    p_max: int = 20,
    gap_threshold: float = 0.5,
) -> dict:
    """
    Run the analysis and return a dict with all numerical results.

    Suitable for use in unit tests (no I/O side-effects).
    """
    records, conclusion = analyse(
        N=N, L_psi=L_psi, kappa=kappa, potential=potential,
        p_max=p_max, gap_threshold=gap_threshold,
    )
    psi_grid, eigenvalues = build_H_psi(N=N, L_psi=L_psi, kappa=kappa,
                                        potential=potential)
    primes = sieve_primes(p_max)
    E_p_vals = [float(p) ** 2 for p in primes]
    E_grid = np.linspace(
        max(0.0, float(eigenvalues[0]) - 2.0),
        float(eigenvalues[-1]) + 2.0,
        2000,
    )
    rho = spectral_density(eigenvalues, E_grid)
    return {
        "records": records,
        "conclusion": conclusion,
        "eigenvalues": eigenvalues,
        "E_grid": E_grid,
        "rho": rho,
        "primes": primes,
        "E_p_vals": E_p_vals,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    records, conclusion = analyse(
        N=400,
        L_psi=2 * math.pi,
        kappa=1.0,
        potential="cos",
        p_max=30,
        gap_threshold=0.5,
    )

    print(format_table(records))
    print()
    print(conclusion)

    # Save plot
    out_path = Path(__file__).parent / "spectrum_vs_primes.png"
    psi_grid, eigenvalues = build_H_psi(N=400, kappa=1.0, potential="cos")
    primes = sieve_primes(30)
    E_max = float(max(primes)) ** 2 + 10.0
    E_grid = np.linspace(0.0, E_max, 5000)
    rho = spectral_density(eigenvalues, E_grid)
    make_plot(records, eigenvalues, E_grid, rho, out_path)
    print(f"\nPlot saved to: {out_path}")


if __name__ == "__main__":
    main()
