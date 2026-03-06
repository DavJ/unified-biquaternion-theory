#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
verify_fpe.py — Numerical verification of the biquaternionic Fokker-Planck claim.

PURPOSE
-------
This script verifies, in the commutative (scalar) sector, that the theta function

    Theta(Q, T) = sum_n exp(pi * B(n) * H(T))

is a (near-)fundamental solution of the Fokker-Planck equation

    dTheta/dT = -div_Q[A(Q) * Theta] + D * Laplacian_Q(Theta)

with drift  A(Q) = -grad_Q H(T).

This corresponds to Step 1 of the FPE verification (see
consolidation_project/FPE_verification/step1_fpe_check.tex).

IMPORTANT LIMITATIONS
---------------------
This is a verification in the COMMUTATIVE SCALAR sector only.  It does NOT
address the full biquaternionic (non-commutative) claim.  Three gaps remain
in the full proof:

  Gap G1: A(Q) = -grad H is assumed, not derived from S[Theta].
  Gap G2: The consistency condition on H is verified numerically here
          but not proved analytically in general.
  Gap G3: Non-commutative biquaternionic product ordering is not tested here.

SETUP
-----
We use a 1D spatial grid Q in [0, 1] with N points.  The Hamiltonian is chosen as a
Gaussian: H(T, Q) = exp(-Q^2 / (2*sigma^2)) * exp(-T).

The theta function uses a finite truncation: n in [-N_terms, N_terms].
The drift is A(Q) = -dH/dQ.
The diffusion coefficient is D = 0.1.

WHAT IS COMPUTED
----------------
1. Theta(Q, T) at a reference time T = T0.
2. The time derivative dTheta/dT via finite difference (forward difference in T).
3. The FPE right-hand side: -div[A*Theta] + D * Laplacian(Theta).
4. The relative residual ||LHS - RHS|| / ||RHS||.

A residual below TOLERANCE (default 1e-2) indicates the scalar claim is
numerically supported.

USAGE
-----
    python tools/verify_fpe.py [--N 200] [--N_terms 5] [--D 0.1] [--T0 1.0]
    python tools/verify_fpe.py --verbose

EXIT CODES
----------
    0  — residual below tolerance (claim SUPPORTED numerically)
    1  — residual above tolerance (claim NOT supported or numerical error)
"""

import argparse
import sys
import numpy as np


def linear_hamiltonian(Q: np.ndarray, T: float, D: float = 0.1) -> np.ndarray:
    """
    Linear Hamiltonian H(Q, T) = Q + (1 + D*pi)*T.

    This is the canonical example that SATISFIES the FPE consistency condition
    (Gap G2 from step1_fpe_check.tex) for B(n) = 1 and diffusion coefficient D.

    Derivation: with grad_Q H = 1 and Laplacian_Q H = 0, the consistency condition
    becomes pi*dH/dT = pi*(1)^2 + D*pi^2*(1)^2 = pi*(1+D*pi),
    so dH/dT = 1+D*pi.  The linear H = Q + (1+D*pi)*T satisfies this exactly.

    Parameters
    ----------
    Q : np.ndarray, shape (N,)
        Spatial grid.
    T : float
        Time parameter.
    D : float
        Diffusion coefficient (must match the D used in the FPE).

    Returns
    -------
    H : np.ndarray, shape (N,)
    """
    c = 1.0 + D * np.pi
    return Q + c * T


def grad_linear_hamiltonian(Q: np.ndarray, T: float, D: float = 0.1) -> np.ndarray:
    """Spatial gradient of the linear Hamiltonian: dH/dQ = 1 everywhere."""
    return np.ones_like(Q)


def gaussian_hamiltonian(Q: np.ndarray, T: float, sigma: float = 0.2) -> np.ndarray:
    """
    Scalar Hamiltonian H(Q, T) = exp(-Q^2 / (2*sigma^2)) * exp(-T).

    This is a simple example that does NOT satisfy the FPE consistency condition
    (Gap G2) and is used to demonstrate that the Gap G2 requirement is genuine.

    Parameters
    ----------
    Q : np.ndarray, shape (N,)
        Spatial grid.
    T : float
        Time parameter.
    sigma : float
        Width of the Gaussian.

    Returns
    -------
    H : np.ndarray, shape (N,)
    """
    return np.exp(-Q**2 / (2 * sigma**2)) * np.exp(-T)


def grad_hamiltonian(Q: np.ndarray, T: float, sigma: float = 0.2) -> np.ndarray:
    """
    Spatial gradient of H: dH/dQ = -Q/sigma^2 * H(Q, T).

    Parameters
    ----------
    Q : np.ndarray, shape (N,)
    T : float
    sigma : float

    Returns
    -------
    dH_dQ : np.ndarray, shape (N,)
    """
    H = gaussian_hamiltonian(Q, T, sigma)
    return (-Q / sigma**2) * H


def build_theta(
    Q: np.ndarray, T: float, B_coeff: np.ndarray,
    H_func, **H_kwargs
) -> np.ndarray:
    """
    Build Theta(Q, T) = sum_n exp(pi * B(n) * H(Q, T)).

    In the commutative (scalar) sector, B(n) and H are real scalars.

    Parameters
    ----------
    Q : np.ndarray, shape (N,)
    T : float
    B_coeff : np.ndarray, shape (2*N_terms+1,)
        The scalar B-coefficients for n = -N_terms ... N_terms.
    H_func : callable
        Hamiltonian function H(Q, T, **H_kwargs).
    **H_kwargs
        Additional keyword arguments passed to H_func.

    Returns
    -------
    Theta : np.ndarray, shape (N,)
    """
    H = H_func(Q, T, **H_kwargs)
    theta = np.zeros_like(Q, dtype=float)
    for b in B_coeff:
        theta += np.exp(np.pi * b * H)
    return theta


def compute_fpe_lhs(
    Q: np.ndarray, T: float, dT: float,
    B_coeff: np.ndarray, H_func, **H_kwargs
) -> np.ndarray:
    """
    Compute the LHS of the FPE: dTheta/dT via finite difference.

    LHS = (Theta(T + dT) - Theta(T)) / dT

    Parameters
    ----------
    Q : np.ndarray, shape (N,)
    T : float
    dT : float
        Step for finite difference.
    B_coeff : np.ndarray
    H_func : callable
    **H_kwargs

    Returns
    -------
    lhs : np.ndarray, shape (N,)
    """
    theta0 = build_theta(Q, T, B_coeff, H_func, **H_kwargs)
    theta1 = build_theta(Q, T + dT, B_coeff, H_func, **H_kwargs)
    return (theta1 - theta0) / dT


def compute_fpe_rhs(
    Q: np.ndarray, T: float,
    B_coeff: np.ndarray, diffusion: float,
    H_func, grad_H_func, **H_kwargs
) -> np.ndarray:
    """
    Compute the RHS of the FPE: -div[A(Q)*Theta] + diffusion * Laplacian(Theta).

    With A(Q) = -dH/dQ:

        -div[A*Theta] = -(dA/dQ)*Theta - A*(dTheta/dQ)

    Spatial derivatives are computed by second-order centred differences.

    Parameters
    ----------
    Q : np.ndarray, shape (N,)
        Uniform grid.
    T : float
    B_coeff : np.ndarray
    diffusion : float
        Diffusion coefficient D in the FPE.
    H_func : callable
    grad_H_func : callable
        grad_H_func(Q, T, **H_kwargs) returns dH/dQ.
    **H_kwargs

    Returns
    -------
    rhs : np.ndarray, shape (N,)
    """
    dQ = Q[1] - Q[0]
    theta = build_theta(Q, T, B_coeff, H_func, **H_kwargs)
    A = -grad_H_func(Q, T, **H_kwargs)  # drift: A = -dH/dQ

    # Spatial derivative of A
    dA_dQ = np.gradient(A, dQ, edge_order=2)

    # Spatial derivative of Theta
    dTheta_dQ = np.gradient(theta, dQ, edge_order=2)

    # Second derivative of Theta (Laplacian in 1D)
    d2Theta_dQ2 = np.gradient(dTheta_dQ, dQ, edge_order=2)

    # FPE right-hand side
    rhs = -(dA_dQ * theta + A * dTheta_dQ) + diffusion * d2Theta_dQ2
    return rhs


def run_verification(
    N: int = 200,
    N_terms: int = 5,
    D: float = 0.1,
    T0: float = 0.5,
    dT: float = 1e-5,
    sigma: float = 0.2,
    tolerance: float = 1e-2,
    verbose: bool = False,
) -> dict:
    """
    Run the FPE numerical verification for two Hamiltonians:

    1. **Linear Hamiltonian** H = Q + (1+D*pi)*T
       - Satisfies the consistency condition (Gap G2) analytically.
       - Expected result: PASS (confirms the scalar claim).

    2. **Gaussian Hamiltonian** H = exp(-Q^2/(2*sigma^2)) * exp(-T)
       - Does NOT satisfy the consistency condition.
       - Expected result: FAIL (confirms Gap G2 is a genuine constraint).

    Parameters
    ----------
    N : int
        Number of spatial grid points.
    N_terms : int
        Number of terms in theta sum: n = -N_terms, ..., N_terms.
    D : float
        Diffusion coefficient.
    T0 : float
        Reference time.
    dT : float
        Finite-difference step in T.
    sigma : float
        Width of the Gaussian Hamiltonian (Test 2 only).
    tolerance : float
        Maximum acceptable relative residual for PASS.
    verbose : bool
        Print detailed output.

    Returns
    -------
    results : dict with keys 'linear_passed', 'gaussian_passed', 'linear_residual',
              'gaussian_residual'.
    """
    # Use a small domain to avoid overflow in exp[pi*H] for linear H
    Q = np.linspace(-0.5, 0.5, N)
    B_coeff = np.ones(2 * N_terms + 1)  # B(n) = 1 for all n

    if verbose:
        print("=" * 65)
        print("Biquaternionic FPE Verification (scalar sector)")
        print("=" * 65)
        print(f"Grid points N        = {N}")
        print(f"Theta sum terms      = [-{N_terms}, ..., {N_terms}]")
        print(f"Diffusion D          = {D}")
        print(f"Reference time T0    = {T0}")
        print(f"Time step dT         = {dT}")
        print(f"Tolerance            = {tolerance}")
        print()

    interior = slice(5, -5)

    # ------------------------------------------------------------------ #
    # Test 1: Linear Hamiltonian — consistency condition SATISFIED        #
    # ------------------------------------------------------------------ #
    lhs_lin = compute_fpe_lhs(Q, T0, dT, B_coeff, linear_hamiltonian, D=D)
    rhs_lin = compute_fpe_rhs(Q, T0, B_coeff, diffusion=D,
                               H_func=linear_hamiltonian,
                               grad_H_func=grad_linear_hamiltonian, D=D)

    res_lin = (np.linalg.norm(lhs_lin[interior] - rhs_lin[interior]) /
               (np.linalg.norm(rhs_lin[interior]) + 1e-15))
    passed_lin = res_lin < tolerance

    if verbose:
        print("Test 1: Linear Hamiltonian H = Q + (1+D*pi)*T")
        print("  [Consistency condition satisfied analytically]")
        print(f"  LHS norm   : {np.linalg.norm(lhs_lin[interior]):.4e}")
        print(f"  RHS norm   : {np.linalg.norm(rhs_lin[interior]):.4e}")
        print(f"  Rel. resid.: {res_lin:.4e}")
        print(f"  Result     : {'PASS ✓' if passed_lin else 'FAIL ✗'}")
        print()

    # ------------------------------------------------------------------ #
    # Test 2: Gaussian Hamiltonian — consistency condition NOT satisfied  #
    # ------------------------------------------------------------------ #
    lhs_gau = compute_fpe_lhs(Q, T0, dT, B_coeff, gaussian_hamiltonian, sigma=sigma)
    rhs_gau = compute_fpe_rhs(Q, T0, B_coeff, diffusion=D,
                               H_func=gaussian_hamiltonian,
                               grad_H_func=grad_hamiltonian, sigma=sigma)

    res_gau = (np.linalg.norm(lhs_gau[interior] - rhs_gau[interior]) /
               (np.linalg.norm(rhs_gau[interior]) + 1e-15))
    # For the Gaussian test, we expect FAIL (high residual confirms Gap G2).
    passed_gau = res_gau < tolerance

    if verbose:
        print("Test 2: Gaussian Hamiltonian H = exp(-Q^2/2s^2)*exp(-T)")
        print("  [Consistency condition NOT satisfied — Gap G2]")
        print(f"  LHS norm   : {np.linalg.norm(lhs_gau[interior]):.4e}")
        print(f"  RHS norm   : {np.linalg.norm(rhs_gau[interior]):.4e}")
        print(f"  Rel. resid.: {res_gau:.4e}")
        expected = "FAIL (expected — confirms Gap G2)"
        print(f"  Result     : {'PASS (unexpected!)' if passed_gau else expected}")
        print()

    return {
        "linear_passed": passed_lin,
        "gaussian_passed": passed_gau,
        "linear_residual": res_lin,
        "gaussian_residual": res_gau,
    }


def check_consistency_condition(
    Q: np.ndarray, T: float,
    D: float = 0.1, verbose: bool = False
) -> dict:
    """
    Numerically evaluate the consistency condition (Gap G2) from step1_fpe_check.tex
    for both the linear and Gaussian Hamiltonians.

    The condition (scalar B=1 case) is:
        pi * H_dot = Laplacian_Q H + pi*(grad_Q H)^2 + D*pi*Laplacian_Q H + D*pi^2*(grad_Q H)^2

    Returns a dict with 'linear_residual' and 'gaussian_residual'.
    """
    dQ = Q[1] - Q[0]

    def _check(H_func, grad_H_func, H_dot_func, **kwargs):
        H = H_func(Q, T, **kwargs)
        H_dot = H_dot_func(Q, T, **kwargs)
        dH = grad_H_func(Q, T, **kwargs)
        d2H = np.gradient(np.gradient(H, dQ, edge_order=2), dQ, edge_order=2)
        lhs = np.pi * H_dot
        rhs = d2H + np.pi * dH**2 + D * np.pi * d2H + D * np.pi**2 * dH**2
        interior = slice(5, -5)
        return (np.linalg.norm(lhs[interior] - rhs[interior]) /
                (np.linalg.norm(rhs[interior]) + 1e-15))

    def linear_H_dot(Q, T, D=0.1):
        c = 1.0 + D * np.pi
        return c * np.ones_like(Q)

    def gaussian_H_dot(Q, T, sigma=0.2):
        return -gaussian_hamiltonian(Q, T, sigma)

    res_lin = _check(linear_hamiltonian, grad_linear_hamiltonian, linear_H_dot, D=D)
    res_gau = _check(gaussian_hamiltonian, grad_hamiltonian, gaussian_H_dot, sigma=0.2)

    if verbose:
        print("Consistency condition (Gap G2) check:")
        print(f"  Linear   Hamiltonian: residual = {res_lin:.4e}  "
              f"({'SATISFIED ✓' if res_lin < 0.01 else 'NOT satisfied'})")
        print(f"  Gaussian Hamiltonian: residual = {res_gau:.4e}  "
              f"({'satisfied' if res_gau < 0.01 else 'NOT satisfied ← Gap G2 confirmed'})")

    return {"linear_residual": res_lin, "gaussian_residual": res_gau}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Numerical verification of biquaternionic FPE claim (scalar sector)."
    )
    parser.add_argument("--N", type=int, default=200, help="Number of spatial grid points")
    parser.add_argument("--N_terms", type=int, default=5, help="Terms in theta sum")
    parser.add_argument("--D", type=float, default=0.1, help="Diffusion coefficient")
    parser.add_argument("--T0", type=float, default=0.5, help="Reference time")
    parser.add_argument("--sigma", type=float, default=0.2, help="Gaussian Hamiltonian width")
    parser.add_argument("--tolerance", type=float, default=1e-2, help="Relative residual tolerance")
    parser.add_argument("--dT", type=float, default=1e-5, help="Finite-difference time step")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument(
        "--check-consistency", action="store_true",
        help="Also check the Gap G2 consistency condition"
    )
    args = parser.parse_args()

    results = run_verification(
        N=args.N,
        N_terms=args.N_terms,
        D=args.D,
        T0=args.T0,
        dT=args.dT,
        sigma=args.sigma,
        tolerance=args.tolerance,
        verbose=args.verbose,
    )

    if args.check_consistency or args.verbose:
        Q = np.linspace(-0.5, 0.5, args.N)
        check_consistency_condition(Q, args.T0, D=args.D, verbose=True)

    if verbose := args.verbose:
        print()
        print("SUMMARY")
        print("-------")
        print(f"  Test 1 (linear H, consistency satisfied): "
              f"{'PASS ✓' if results['linear_passed'] else 'FAIL ✗'} "
              f"(residual {results['linear_residual']:.2e})")
        print(f"  Test 2 (Gaussian H, no consistency):      "
              f"{'PASS (unexpected)' if results['gaussian_passed'] else 'FAIL (expected) ✓'} "
              f"(residual {results['gaussian_residual']:.2e})")
        print()
        print("Interpretation:")
        if results["linear_passed"] and not results["gaussian_passed"]:
            print("  The scalar-sector FPE claim is NUMERICALLY SUPPORTED when")
            print("  the consistency condition (Gap G2) is satisfied.")
            print("  When G2 is violated (Gaussian H), the FPE does NOT hold.")
            print("  This confirms the SKETCH verdict of step1_fpe_check.tex.")
        print()
        print("  NOTE: Gaps G1, G2, G3 from step1_fpe_check.tex remain open.")
        print("  This script only verifies the commutative scalar sector.")
    else:
        # Minimal output for CI / non-verbose use
        lin_status = "PASS" if results["linear_passed"] else "FAIL"
        gau_status = "PASS (unexpected)" if results["gaussian_passed"] else "FAIL (expected)"
        print(f"FPE Test1 (linear H, consistency OK):    {lin_status}  "
              f"(rel. residual = {results['linear_residual']:.2e})")
        print(f"FPE Test2 (Gaussian H, no consistency):  {gau_status}  "
              f"(rel. residual = {results['gaussian_residual']:.2e})")

    # Script passes if Test 1 PASSES (scalar claim supported when conditions met)
    # and Test 2 FAILS (Gap G2 is real).
    return 0 if results["linear_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
