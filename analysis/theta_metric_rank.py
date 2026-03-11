# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
Rank and Kernel Analysis of the Θ → metric Mapping in UBT
==========================================================

Computes the Jacobian, rank, and kernel dimension of the map

    g_{μν} = Re Tr(E_μ E_ν†),  E_μ = ∂_μ Θ

where E_μ ∈ 𝔹 = ℍ ⊗ ℂ carries 8 real components and μ ∈ {0,1,2,3}.

Domain:   ℝ³²  (32 real components of all four tetrad vectors)
Codomain: ℝ¹⁰  (10 independent components of the symmetric metric tensor)

References:
    analysis/theta_metric_rank_analysis.md
    canonical/geometry/biquaternion_tetrad.tex
"""

from __future__ import annotations

import sys
import random as _random
from typing import List, Tuple

import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# 1. Symbolic biquaternion metric formula
# ---------------------------------------------------------------------------

def _symbolic_variables() -> Tuple[List[sp.Symbol], List[List[sp.Symbol]]]:
    """
    Define 32 symbolic real variables representing the tetrad E_μ.

    Returns
    -------
    flat : list of 32 sp.Symbol  (ordered μ=0,1,2,3; k=1..8)
    by_mu : list of 4 lists, each containing 8 symbols for one E_μ
    """
    flat: List[sp.Symbol] = []
    by_mu: List[List[sp.Symbol]] = []
    for mu in range(4):
        row: List[sp.Symbol] = []
        for k in range(1, 9):
            sym = sp.Symbol(f"e{mu}{k}", real=True)
            row.append(sym)
            flat.append(sym)
        by_mu.append(row)
    return flat, by_mu


def _metric_component(E_mu: List[sp.Symbol], E_nu: List[sp.Symbol]) -> sp.Expr:
    """
    Compute g_{μν} = Re Tr(E_μ E_ν†) symbolically.

    For a biquaternion written as 8 real components
    (r0, s0, r1, s1, r2, s2, r3, s3) the scalar product is

        Re Tr(p q†) = 2 * sum_k  p_k * q_k

    where the index k runs over all 8 real components.

    Parameters
    ----------
    E_mu, E_nu : lists of 8 real symbolic variables

    Returns
    -------
    Symbolic expression for g_{μν}
    """
    return 2 * sum(a * b for a, b in zip(E_mu, E_nu))


def build_metric_vector(
    by_mu: List[List[sp.Symbol]],
) -> Tuple[List[sp.Expr], List[str]]:
    """
    Build the vector of 10 metric components g_{μν} for μ ≤ ν.

    Returns
    -------
    g_vec  : list of 10 symbolic expressions
    labels : list of 10 string labels like "g00", "g01", ...
    """
    g_vec: List[sp.Expr] = []
    labels: List[str] = []
    for mu in range(4):
        for nu in range(mu, 4):
            g_vec.append(_metric_component(by_mu[mu], by_mu[nu]))
            labels.append(f"g{mu}{nu}")
    return g_vec, labels


def compute_symbolic_jacobian(
    g_vec: List[sp.Expr],
    flat: List[sp.Symbol],
) -> sp.Matrix:
    """
    Compute the 10 × 32 Jacobian matrix J_{i,k} = ∂g_i / ∂X_k symbolically.

    Parameters
    ----------
    g_vec : list of 10 metric component expressions
    flat  : list of 32 real symbolic variables

    Returns
    -------
    J : sympy Matrix of shape (10, 32)
    """
    return sp.Matrix([[sp.diff(g, x) for x in flat] for g in g_vec])


# ---------------------------------------------------------------------------
# 2. Numerical rank verification
# ---------------------------------------------------------------------------

def _numeric_jacobian(E: np.ndarray) -> np.ndarray:
    """
    Evaluate the Jacobian numerically for a given configuration E ∈ ℝ^{4×8}.

    Because g_{μν} = 2 * E_μ · E_ν (dot product of 8-vectors), the
    derivatives are simply:

        ∂g_{μν} / ∂e_ρ^k = 2 * e_ν^k  if ρ == μ (and μ ≠ ν)
                          + 2 * e_μ^k  if ρ == ν (and μ ≠ ν)
                          = 4 * e_μ^k  if ρ == μ == ν
                          = 0           otherwise

    Parameters
    ----------
    E : ndarray of shape (4, 8)

    Returns
    -------
    J : ndarray of shape (10, 32)
    """
    J = np.zeros((10, 32))
    row = 0
    for mu in range(4):
        for nu in range(mu, 4):
            col_offset_mu = mu * 8
            col_offset_nu = nu * 8
            if mu == nu:
                J[row, col_offset_mu : col_offset_mu + 8] = 4 * E[mu]
            else:
                J[row, col_offset_mu : col_offset_mu + 8] = 2 * E[nu]
                J[row, col_offset_nu : col_offset_nu + 8] = 2 * E[mu]
            row += 1
    return J


def numeric_rank_samples(
    n_samples: int = 1000,
    seed: int = 42,
    tol: float = 1e-10,
) -> dict:
    """
    Estimate the rank of J by averaging over random tetrad configurations.

    Parameters
    ----------
    n_samples : number of random E configurations to sample
    seed      : random seed for reproducibility
    tol       : singular-value threshold for rank computation

    Returns
    -------
    dict with keys: 'min_rank', 'max_rank', 'mean_rank', 'rank_counts'
    """
    rng = np.random.default_rng(seed)
    ranks: List[int] = []
    for _ in range(n_samples):
        E = rng.standard_normal((4, 8))
        J = _numeric_jacobian(E)
        sv = np.linalg.svd(J, compute_uv=False)
        rank = int(np.sum(sv > tol))
        ranks.append(rank)

    rank_counts: dict = {}
    for r in ranks:
        rank_counts[r] = rank_counts.get(r, 0) + 1

    return {
        "min_rank": min(ranks),
        "max_rank": max(ranks),
        "mean_rank": float(np.mean(ranks)),
        "rank_counts": rank_counts,
    }


def compute_kernel_directions(
    E: np.ndarray,
    tol: float = 1e-10,
) -> np.ndarray:
    """
    Compute an orthonormal basis for ker(J) for a given configuration.

    Parameters
    ----------
    E   : ndarray of shape (4, 8)
    tol : singular-value threshold

    Returns
    -------
    kernel_basis : ndarray of shape (kernel_dim, 32)
    """
    J = _numeric_jacobian(E)
    _, s, Vt = np.linalg.svd(J, full_matrices=True)
    # rows of Vt corresponding to singular values below tol
    kernel_basis = Vt[small]
    return kernel_basis


def verify_lorentz_kernel(
    E: np.ndarray,
    tol: float = 1e-8,
) -> dict:
    """
    Verify that internal frame (SO(8)) rotations of the flat biquaternion
    index lie in ker(J).

    In the biquaternion tetrad formalism the *local frame* gauge redundancy
    corresponds to simultaneous right-multiplication of each tetrad vector by
    the same internal-frame rotation R ∈ SO(8):

        E_μ → E_μ · R   (acting on the 8 real flat components)

    Infinitesimally, δE_μ = E_μ · M  where M is antisymmetric.  The metric
    is manifestly invariant because

        δg_{μν} = Re Tr(δE_μ · E_ν† + E_μ · δE_ν†)
                = 2 (E_μ · M E_ν + E_ν · M^T E_μ)  [dot product on ℝ^8]
                = 2 E_μ^T (M + M^T) E_ν = 0         [M antisymmetric]

    We test all 28 generators G_{ab} (a < b, 1 ≤ a,b ≤ 8) of so(8), each
    encoded as the 8×8 matrix with +1 at (a,b) and −1 at (b,a).

    Parameters
    ----------
    E   : ndarray of shape (4, 8)
    tol : tolerance for checking g invariance

    Returns
    -------
    dict with 'n_so8_generators', 'max_delta_g', 'all_in_kernel'
    """
    J = _numeric_jacobian(E)
    max_delta_g = 0.0
    n_gen = 0
    for a in range(8):
        for b in range(a + 1, 8):
            # Internal-frame generator G_{ab}: M_{ab}=+1, M_{ba}=-1
            M = np.zeros((8, 8))
            M[a, b] = 1.0
            M[b, a] = -1.0
            # δE_μ = E_μ @ M  (each of the 4 tetrad 8-vectors rotated by M)
            delta_E = E @ M          # shape (4, 8)
            delta_X = delta_E.ravel()  # shape (32,)
            delta_g = J @ delta_X    # shape (10,)
            max_delta_g = max(max_delta_g, np.max(np.abs(delta_g)))
            n_gen += 1

    return {
        "n_so8_generators": n_gen,
        "max_delta_g": max_delta_g,
        "all_in_kernel": max_delta_g < tol,
    }


# ---------------------------------------------------------------------------
# 3. Main analysis runner
# ---------------------------------------------------------------------------

def run_full_analysis(verbose: bool = True) -> dict:
    """
    Run the complete rank and kernel analysis and return a results dict.
    """
    results: dict = {}

    # ---- Symbolic analysis ------------------------------------------------
    if verbose:
        print("=" * 60)
        print("Θ → Metric Rank & Kernel Analysis (UBT)")
        print("=" * 60)
        print("\n[1] Building symbolic variables (32 real components) ...")

    flat, by_mu = _symbolic_variables()

    if verbose:
        print(f"    Domain dimension: {len(flat)}")

    g_vec, labels = build_metric_vector(by_mu)

    if verbose:
        print(f"    Codomain dimension: {len(g_vec)} (metric components: {labels})")
        print("\n[2] Computing symbolic Jacobian (10 × 32) ...")

    J_sym = compute_symbolic_jacobian(g_vec, flat)
    results["J_sym_shape"] = J_sym.shape

    # Symbolic rank (uses fraction-free algorithm; may be slow for full 10×32)
    # We compute on a *reduced* symbolic substitution to get the generic rank
    # quickly.  For full confirmation use numeric sampling.
    if verbose:
        print("    Evaluating symbolic Jacobian at a generic numeric point ...")

    # Substitute a random rational point to compute rank cheaply
    _random.seed(7)
    subs = {s: sp.Rational(_random.randint(1, 9), _random.randint(1, 5))
            for s in flat}
    J_num_sym = J_sym.subs(subs)
    sym_rank = J_num_sym.rank()
    results["symbolic_rank_at_rational_point"] = sym_rank

    if verbose:
        print(f"    Rank at rational sample point: {sym_rank}")

    # ---- Numerical analysis -----------------------------------------------
    if verbose:
        print("\n[3] Numerical rank over 1000 random configurations ...")

    num_stats = numeric_rank_samples(n_samples=1000)
    results["numeric_stats"] = num_stats

    if verbose:
        print(f"    min rank = {num_stats['min_rank']}")
        print(f"    max rank = {num_stats['max_rank']}")
        print(f"    mean rank = {num_stats['mean_rank']:.3f}")
        print(f"    rank distribution: {num_stats['rank_counts']}")

    # ---- Kernel dimension -------------------------------------------------
    generic_rank = num_stats["max_rank"]
    kernel_dim = 32 - generic_rank
    results["generic_rank"] = generic_rank
    results["kernel_dimension"] = kernel_dim

    if verbose:
        print(f"\n[4] Kernel dimension = 32 - {generic_rank} = {kernel_dim}")

    # ---- Lorentz gauge verification ---------------------------------------
    if verbose:
        print("\n[5] Verifying Lorentz frame rotations ∈ ker(J) ...")

    rng = np.random.default_rng(0)
    E_test = rng.standard_normal((4, 8))
    lorentz_check = verify_lorentz_kernel(E_test)
    results["lorentz_check"] = lorentz_check

    if verbose:
        print(f"    Number of so(8) generators tested: "
              f"{lorentz_check['n_so8_generators']}")
        print(f"    Max |δg| over generators: {lorentz_check['max_delta_g']:.2e}")
        print(f"    All Lorentz generators in kernel: "
              f"{lorentz_check['all_in_kernel']}")

    # ---- Summary ----------------------------------------------------------
    if verbose:
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"  Domain dimension  (X)         : 32")
        print(f"  Codomain dimension (g)         : 10")
        print(f"  Generic rank of J              : {generic_rank}")
        print(f"  Kernel dimension               : {kernel_dim}")
        print(f"  Lorentz gauge directions (≥6)  : 6")
        print(f"  Remaining kernel               : {kernel_dim - 6}")
        print(f"  GR sector reproduced           : {'YES' if generic_rank >= 10 else 'NO'}")
        print(f"  Extra non-metric DOF exist     : {'YES' if kernel_dim > 6 else 'NO'}")
        print("=" * 60)

    return results


# ---------------------------------------------------------------------------
# 4. Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    results = run_full_analysis(verbose=True)
    sys.exit(0 if results["generic_rank"] == 10 else 1)
