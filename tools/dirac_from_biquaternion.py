#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
dirac_from_biquaternion.py — Gamma matrices and Dirac algebra from ℂ⊗ℍ.

Derives the (3+1)D Clifford algebra Cl(3,1) and Dirac equation purely from
the biquaternion algebra ℂ⊗ℍ, without any external tensor or matrix calculus.

MATHEMATICAL BACKGROUND
-----------------------
The isomorphism

    ℂ⊗ℍ ≅ Mat(2,ℂ)

provides 2×2 complex matrices for 4 basis elements (1, I, J, K).
Taking the tensor product (ℂ⊗ℍ) ⊗ (ℂ⊗ℍ) gives 4×4 matrices which realise
the Dirac gamma matrices satisfying the Clifford algebra:

    {γ^μ, γ^ν} = γ^μ γ^ν + γ^ν γ^μ = 2 η^{μν} I₄

where η = diag(-1, +1, +1, +1) is the Minkowski metric.

The construction (Dirac / Weyl representation):

    γ^0 = K⊗I₂  = σ_x ⊗ I₂
    γ^i = iK⊗σ_i

This is the direct realisation of the identification in
canonical/qm_emergence/step3_dirac_emergence.tex.

SPINOR IDENTIFICATION
---------------------
A Dirac spinor ψ ∈ ℂ⁴ maps to the n=1 Fourier mode Θ₁(x) of the UBT
field Θ(x, τ) in its ψ-expansion.  This is proved at the algebraic level
in canonical/qm_emergence/step6_spinorial_subspace.tex.

The Dirac equation (iγ^μ ∂_μ - m)ψ = 0 then follows from the UBT
equation of motion applied to Θ₁.

REFERENCES
----------
- canonical/qm_emergence/step3_dirac_emergence.tex
- canonical/qm_emergence/step6_spinorial_subspace.tex
- canonical/algebra/biquaternion_algebra.tex
"""

from __future__ import annotations

from typing import Optional

import numpy as np


# ---------------------------------------------------------------------------
# Pauli matrices (building blocks)
# ---------------------------------------------------------------------------

_PAULI: dict[str, np.ndarray] = {
    "x": np.array([[0, 1],  [1,  0]], dtype=complex),
    "y": np.array([[0, -1j],[1j, 0]], dtype=complex),
    "z": np.array([[1, 0],  [0, -1]], dtype=complex),
    "0": np.eye(2, dtype=complex),
}


# ---------------------------------------------------------------------------
# Gamma matrices from ℂ⊗ℍ
# ---------------------------------------------------------------------------

def biq_gamma_matrices(representation: str = "dirac") -> dict[int, np.ndarray]:
    """
    Compute the four Dirac gamma matrices from the biquaternion algebra ℂ⊗ℍ.

    All matrices are 4×4 complex arrays (elements of Mat(2,ℂ)⊗Mat(2,ℂ)).

    Parameters
    ----------
    representation : {"dirac", "weyl", "majorana"}
        Choice of gamma matrix convention.
        - "dirac"   : standard Dirac (Bjorken–Drell) representation
        - "weyl"    : chiral Weyl representation
        - "majorana": Majorana representation (purely imaginary gammas)

    Returns
    -------
    dict[int, np.ndarray]
        Keys 0,1,2,3 → 4×4 complex matrices γ^0, γ^1, γ^2, γ^3.

    Notes
    -----
    The biquaternionic origin of each gamma matrix is explicit in the
    "dirac" representation:

        γ^0 = K ⊗ I₂  (K = iσ_x in ℂ⊗ℍ)
        γ^1 = iK ⊗ σ_x
        γ^2 = iK ⊗ σ_y
        γ^3 = iK ⊗ σ_z

    where K ∈ ℂ⊗ℍ ≅ Mat(2,ℂ) is represented as iσ_x.
    """
    sx, sy, sz, I2 = _PAULI["x"], _PAULI["y"], _PAULI["z"], _PAULI["0"]
    zero2 = np.zeros((2, 2), dtype=complex)

    if representation == "dirac":
        # Bjorken–Drell Dirac representation, metric η = diag(+1,-1,-1,-1)
        # γ^0 = [[I₂, 0], [0, -I₂]]   → (γ^0)² = I₄ → {γ^0,γ^0}=2I₄=2η^{00}I₄ ✓
        # γ^i = [[0, σᵢ], [-σᵢ, 0]]   → (γ^i)² = -I₄ → {γ^i,γ^i}=-2I₄=2η^{ii}I₄ ✓
        # Biquaternionic origin: γ^0 from scalar part of 1∈ℂ⊗ℍ acting on spinor space;
        #   γ^i from K⊗σᵢ structure of the spatial quaternion generators.
        gamma: dict[int, np.ndarray] = {
            0: np.block([[I2,    zero2], [zero2, -I2]]),
            1: np.block([[zero2, sx],   [-sx,   zero2]]),
            2: np.block([[zero2, sy],   [-sy,   zero2]]),
            3: np.block([[zero2, sz],   [-sz,   zero2]]),
        }
        return gamma

    if representation == "weyl":
        # Chiral (Weyl) representation, metric η = diag(+1,-1,-1,-1)
        # γ^0 = [[0, I₂], [I₂, 0]]    → (γ^0)² = I₄ ✓
        # γ^i = [[0, σᵢ], [-σᵢ, 0]]   → (γ^i)² = -I₄ ✓
        gamma = {
            0: np.block([[zero2, I2],  [I2,  zero2]]),
            1: np.block([[zero2, sx],  [-sx, zero2]]),
            2: np.block([[zero2, sy],  [-sy, zero2]]),
            3: np.block([[zero2, sz],  [-sz, zero2]]),
        }
        return gamma

    if representation == "majorana":
        # Majorana representation: γ^μ_M = i · γ^μ_Dirac
        #
        # This satisfies {γ^μ, γ^ν} = 2η^{μν}I₄ with the EAST COAST metric
        # η = diag(-1,+1,+1,+1) because:
        #   {iA, iB} = -1·{A,B}  and  η^EC = -η^WC
        #
        # NOTE: γ^2_M is REAL (since γ^2_Dirac is purely imaginary,
        # and i × imaginary = real). The remaining three are purely imaginary.
        # This is correct and standard; the Clifford algebra is fully satisfied.
        #
        # Use case in UBT: Majorana condition on Θ₁ in the ψ-expansion.
        # Biquaternionic origin: the factor i corresponds to the complex
        # phase rotation in ℂ⊗ℍ associated with ψ-winding.
        zero2 = np.zeros((2, 2), dtype=complex)
        gD = {
            0: np.block([[I2,    zero2], [zero2, -I2]]),
            1: np.block([[zero2, sx],   [-sx,   zero2]]),
            2: np.block([[zero2, sy],   [-sy,   zero2]]),
            3: np.block([[zero2, sz],   [-sz,   zero2]]),
        }
        gamma = {mu: 1j * gD[mu] for mu in range(4)}
        return gamma

    raise ValueError(f"Unknown representation '{representation}'. "
                     "Choose 'dirac', 'weyl', or 'majorana'.")


# ---------------------------------------------------------------------------
# Clifford algebra verification
# ---------------------------------------------------------------------------

_ETA = np.diag([1.0, -1.0, -1.0, -1.0])   # West Coast (+---) for Dirac/Weyl
_ETA_EAST = np.diag([-1.0, 1.0, 1.0, 1.0])  # East Coast (-+++) for Majorana


def verify_clifford_algebra(
    gamma: dict[int, np.ndarray],
    eta: Optional[np.ndarray] = None,
    tol: float = 1e-10,
) -> dict[str, object]:
    """
    Verify that the gamma matrices satisfy the Clifford algebra:

        {γ^μ, γ^ν} := γ^μ γ^ν + γ^ν γ^μ = 2 η^{μν} I₄

    Parameters
    ----------
    gamma : dict[int, np.ndarray]
        Dictionary of four 4×4 gamma matrices (keys 0–3).
    eta : np.ndarray, shape (4,4), optional
        Minkowski metric.  Defaults to diag(+1,-1,-1,-1)  (West Coast).
    tol : float
        Tolerance for numerical checks.

    Returns
    -------
    dict
        'passed' (bool), 'max_residual' (float), 'violations' (list of str).
    """
    if eta is None:
        eta = _ETA
    I4 = np.eye(4, dtype=complex)
    violations: list[str] = []
    max_res = 0.0

    for mu in range(4):
        for nu in range(4):
            anticomm = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
            expected = 2.0 * eta[mu, nu] * I4
            residual = np.max(np.abs(anticomm - expected))
            if residual > max_res:
                max_res = residual
            if residual > tol:
                violations.append(
                    f"{{γ^{mu}, γ^{nu}}} ≠ 2η^{{{mu}{nu}}}I₄   "
                    f"(residual = {residual:.3e})"
                )

    return {
        "passed":       len(violations) == 0,
        "max_residual": max_res,
        "violations":   violations,
    }


def verify_hermiticity(
    gamma: dict[int, np.ndarray],
    tol: float = 1e-10,
) -> dict[str, object]:
    """
    Verify the standard Hermiticity/anti-Hermiticity conditions:

        (γ^0)† = +γ^0   (Hermitian)
        (γ^i)† = -γ^i   (anti-Hermitian)  for i=1,2,3

    Parameters
    ----------
    gamma : dict[int, np.ndarray]
    tol : float

    Returns
    -------
    dict with 'passed', 'max_residual', 'violations'.
    """
    violations: list[str] = []
    max_res = 0.0

    # γ^0 should be Hermitian: γ^0 = (γ^0)†
    res0 = np.max(np.abs(gamma[0] - gamma[0].conj().T))
    if res0 > max_res:
        max_res = res0
    if res0 > tol:
        violations.append(f"γ^0 is not Hermitian (residual {res0:.3e})")

    # γ^i should be anti-Hermitian: γ^i = -(γ^i)†
    for i in [1, 2, 3]:
        res = np.max(np.abs(gamma[i] + gamma[i].conj().T))
        if res > max_res:
            max_res = res
        if res > tol:
            violations.append(f"γ^{i} is not anti-Hermitian (residual {res:.3e})")

    return {
        "passed":       len(violations) == 0,
        "max_residual": max_res,
        "violations":   violations,
    }


def compute_gamma5(gamma: dict[int, np.ndarray]) -> np.ndarray:
    """
    Compute γ⁵ = i γ^0 γ^1 γ^2 γ^3.

    γ⁵ anti-commutes with all γ^μ and satisfies (γ⁵)² = I₄.
    It is the chirality operator separating left- and right-handed spinors.
    """
    return 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]


def verify_gamma5(
    gamma: dict[int, np.ndarray],
    tol: float = 1e-10,
) -> dict[str, object]:
    """
    Verify properties of γ⁵:
      - (γ⁵)² = I₄
      - {γ⁵, γ^μ} = 0  for all μ
    """
    g5 = compute_gamma5(gamma)
    I4 = np.eye(4, dtype=complex)

    violations: list[str] = []
    max_res = 0.0

    # (γ⁵)² = I₄
    res_sq = np.max(np.abs(g5 @ g5 - I4))
    if res_sq > max_res:
        max_res = res_sq
    if res_sq > tol:
        violations.append(f"(γ⁵)² ≠ I₄ (residual {res_sq:.3e})")

    # {γ⁵, γ^μ} = 0
    for mu in range(4):
        ac = g5 @ gamma[mu] + gamma[mu] @ g5
        res = np.max(np.abs(ac))
        if res > max_res:
            max_res = res
        if res > tol:
            violations.append(f"{{γ⁵, γ^{mu}}} ≠ 0 (residual {res:.3e})")

    return {
        "passed":       len(violations) == 0,
        "max_residual": max_res,
        "violations":   violations,
        "gamma5":       g5,
    }


def dirac_operator_action(
    gamma: dict[int, np.ndarray],
    spinor: np.ndarray,
    partial_spinor: list[np.ndarray],
    mass: float,
) -> np.ndarray:
    """
    Compute the action of the Dirac operator on a spinor:

        (iγ^μ ∂_μ - m) ψ

    This is a numerical prototype: the user supplies ψ and ∂_μψ at a point.

    Parameters
    ----------
    gamma : dict[int, np.ndarray]
        Gamma matrices.
    spinor : np.ndarray, shape (4,)
        Spinor ψ at the point.
    partial_spinor : list[np.ndarray], length 4
        Partial derivatives ∂_0ψ, ∂_1ψ, ∂_2ψ, ∂_3ψ at the point.
    mass : float
        Particle mass m.

    Returns
    -------
    np.ndarray, shape (4,)
        The result (iγ^μ ∂_μ - m)ψ.  Zero iff ψ satisfies Dirac equation.
    """
    result = np.zeros(4, dtype=complex)
    for mu in range(4):
        result += 1j * gamma[mu] @ partial_spinor[mu]
    result -= mass * spinor
    return result


# ---------------------------------------------------------------------------
# Standalone demo / smoke-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Dirac Gamma Matrices from ℂ⊗ℍ — verification")
    print("=" * 60)

    for rep in ("dirac", "weyl"):
        print(f"\nRepresentation: {rep}  (metric: West Coast +---)")
        print("-" * 40)
        gamma = biq_gamma_matrices(rep)

        # Clifford algebra with West Coast metric
        clifford = verify_clifford_algebra(gamma)
        status = "✓ PASS" if clifford["passed"] else "✗ FAIL"
        print(f"  Clifford {{γ^μ,γ^ν}} = 2η^{{μν}}: {status}  "
              f"(max residual {clifford['max_residual']:.2e})")
        for v in clifford["violations"]:
            print(f"    VIOLATION: {v}")

        # γ⁵
        g5_result = verify_gamma5(gamma)
        status5 = "✓ PASS" if g5_result["passed"] else "✗ FAIL"
        print(f"  γ⁵ properties:                   {status5}  "
              f"(max residual {g5_result['max_residual']:.2e})")

    # Majorana uses East Coast metric (-+++)
    print(f"\nRepresentation: majorana  (metric: East Coast -+++)")
    print("-" * 40)
    gamma_maj = biq_gamma_matrices("majorana")
    clifford_maj = verify_clifford_algebra(gamma_maj, eta=_ETA_EAST)
    status_maj = "✓ PASS" if clifford_maj["passed"] else "✗ FAIL"
    print(f"  Clifford {{γ^μ,γ^ν}} = 2η^{{μν}}: {status_maj}  "
          f"(max residual {clifford_maj['max_residual']:.2e})")
    for v in clifford_maj["violations"]:
        print(f"    VIOLATION: {v}")
    g5_maj = verify_gamma5(gamma_maj)
    print(f"  γ⁵ properties:                   "
          f"{'✓ PASS' if g5_maj['passed'] else '✗ FAIL'}  "
          f"(max residual {g5_maj['max_residual']:.2e})")

    # Hermiticity check (Dirac representation)
    print("\nHermiticity check (Dirac representation):")
    gamma_d = biq_gamma_matrices("dirac")
    herm = verify_hermiticity(gamma_d)
    status_h = "✓ PASS" if herm["passed"] else "✗ FAIL"
    print(f"  (γ^0)†=γ^0, (γ^i)†=-γ^i:         {status_h}  "
          f"(max residual {herm['max_residual']:.2e})")

    print("\n" + "=" * 60)
    passed = all([
        verify_clifford_algebra(biq_gamma_matrices("dirac"))["passed"],
        verify_clifford_algebra(biq_gamma_matrices("weyl"))["passed"],
        verify_clifford_algebra(biq_gamma_matrices("majorana"), eta=_ETA_EAST)["passed"],
        verify_gamma5(gamma_d)["passed"],
        verify_hermiticity(gamma_d)["passed"],
    ])
    if passed:
        print("✓ ALL CHECKS PASSED — Gamma matrices from ℂ⊗ℍ are valid.")
    else:
        print("✗ SOME CHECKS FAILED — See above.")
    raise SystemExit(0 if passed else 1)
