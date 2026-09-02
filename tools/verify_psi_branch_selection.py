#!/usr/bin/env python3
"""
Regression / CAS checks for the complex-time branch-selection research track.

This script checks only the finite-dimensional or exact symbolic identities
encoded below. It is not a proof of the infinite-dimensional bounded-semigroup
selection proposition.

LEAN-PENDING: no compiled Lean proof is added here.
"""

from __future__ import annotations

import sys

PASS = "PASS"
FAIL = "FAIL"
NOT_RUN = "NOT RUN"
results: list[tuple[str, str, str]] = []


def record(name: str, status: str, detail: str) -> None:
    print(f"  [{status}] {name}: {detail}")
    results.append((name, status, detail))


def check(name: str, condition: bool, detail: str) -> None:
    record(name, PASS if condition else FAIL, detail)


try:
    import sympy as sp
except ImportError:
    print("NOT RUN: SymPy is not installed, so exact CAS checks are unavailable.")
    print("LEAN-PENDING: the infinite-dimensional bounded-semigroup proposition is")
    print("  not formally proved in this environment.")
    raise SystemExit(0)


def matrix_is_zero(mat: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


print("V1: Exact factorization")
t = sp.symbols("t", real=True)
A = sp.symbols("A", real=True)
phi = sp.Function("phi")(t)
lhs_v1 = sp.I * sp.diff(-sp.I * sp.diff(phi, t) - A * phi, t) - A * (
    -sp.I * sp.diff(phi, t) - A * phi
)
rhs_v1 = sp.diff(phi, t, 2) + A**2 * phi
check(
    "V1",
    sp.simplify(lhs_v1 - rhs_v1) == 0,
    "(i∂_t-A)(-i∂_t-A)=(∂_t^2+A^2) on a generic scalar test function",
)

print("V2: Exact exponential branches")
branch_pos = sp.exp(-sp.I * A * t)
branch_neg = sp.exp(sp.I * A * t)
check(
    "V2a_second_order_positive",
    sp.simplify(sp.diff(branch_pos, t, 2) + A**2 * branch_pos) == 0,
    "e^{-itA} solves (∂_t^2+A^2)Φ=0",
)
check(
    "V2b_second_order_negative",
    sp.simplify(sp.diff(branch_neg, t, 2) + A**2 * branch_neg) == 0,
    "e^{+itA} solves (∂_t^2+A^2)Φ=0",
)
check(
    "V2c_first_order_positive",
    sp.simplify(sp.I * sp.diff(branch_pos, t) - A * branch_pos) == 0,
    "(i∂_t-A)e^{-itA}=0",
)
check(
    "V2d_first_order_negative",
    sp.simplify(-sp.I * sp.diff(branch_neg, t) - A * branch_neg) == 0,
    "(-i∂_t-A)e^{+itA}=0",
)

print("V3: Exact continuation identity")
s = sp.symbols("s", positive=True, real=True)
z = t - sp.I * s
check(
    "V3a_damped",
    sp.simplify(sp.exp(-sp.I * A * z) - sp.exp(-sp.I * A * t) * sp.exp(-s * A)) == 0,
    "e^{-iA(t-is)}=e^{-itA}e^{-sA}",
)
check(
    "V3b_growing",
    sp.simplify(sp.exp(sp.I * A * z) - sp.exp(sp.I * A * t) * sp.exp(s * A)) == 0,
    "e^{+iA(t-is)}=e^{+itA}e^{+sA}",
)

print("V4: Decay / growth signs")
lam = sp.symbols("lam", positive=True, real=True)
check("V4a_decay_exponent", (-s * lam).is_negative is True, "-s·λ is negative for s>0, λ>0")
check("V4b_growth_exponent", (s * lam).is_positive is True, "+s·λ is positive for s>0, λ>0")
check(
    "V4c_inverse_pair",
    sp.simplify(sp.exp(-s * lam) * sp.exp(s * lam) - 1) == 0,
    "e^{-sλ}e^{+sλ}=1",
)

print("V5: Finite-dimensional diagonal boundedness example")
P_eps = sp.diag(0, 1, 1)
u_bad = sp.Matrix([0, 1, 0])
u_good = sp.Matrix([5, 0, 0])
continued_bad = sp.Matrix([0, sp.exp(s), 0])
continued_good = sp.Matrix([5, 0, 0])
check(
    "V5a_projection_bad",
    P_eps * u_bad == sp.Matrix([0, 1, 0]),
    "E_A([1,∞))u_- keeps the positive-spectrum component",
)
check(
    "V5b_projection_good",
    P_eps * u_good == sp.zeros(3, 1),
    "E_A([1,∞))u_-=0 for a kernel-only vector",
)
check(
    "V5c_bad_unbounded",
    sp.limit((continued_bad.T * continued_bad)[0], s, sp.oo) == sp.oo,
    "a positive-spectrum component makes ‖e^{sA}u_-‖^2 diverge",
)
check(
    "V5d_good_bounded",
    sp.simplify((continued_good.T * continued_good)[0] - 25) == 0,
    "a kernel-only vector remains bounded",
)

print("V6: Zero mode")
u0, v0 = sp.symbols("u0 v0", real=True)
phi0 = u0 + t * v0
check(
    "V6a_general_zero_mode",
    sp.diff(phi0, t, 2) == 0,
    "Φ_0(t)=u_0+t·v_0 is the general scalar zero-mode form",
)
check(
    "V6b_nonconstant_if_v0_nonzero",
    sp.simplify(phi0.subs({u0: 0, v0: 1}) - t) == 0,
    "for v_0≠0 the zero mode is linear rather than constant",
)
check(
    "V6c_unbounded_linear_mode",
    sp.limit(phi0.subs({u0: 0, v0: 1}), t, sp.oo) == sp.oo,
    "boundedness in real t removes the linear zero mode",
)

print("V7: Whole Fourier-mode differentiation")
q, psi, n, R_psi = sp.symbols("q psi n R_psi", real=True, nonzero=True)
Theta_n = sp.Function("Theta_n")(q, t)
whole_mode = Theta_n * sp.exp(sp.I * n * psi / R_psi)
check(
    "V7",
    sp.simplify(
        -sp.I * sp.diff(whole_mode, psi)
        - (n / R_psi) * Theta_n * sp.exp(sp.I * n * psi / R_psi)
    )
    == 0,
    "-i∂_ψ[Θ_n(q,t)e^{inψ/R_ψ}]=(n/R_ψ)Θ_n(q,t)e^{inψ/R_ψ}",
)

print("V8: Fourier eigenvalues")
pure_mode = sp.exp(sp.I * n * psi / R_psi)
check(
    "V8a_first_eigenvalue",
    sp.simplify(-sp.I * sp.diff(pure_mode, psi) - (n / R_psi) * pure_mode) == 0,
    "-i∂_ψ has eigenvalue n/R_ψ",
)
check(
    "V8b_second_eigenvalue",
    sp.simplify(-sp.diff(pure_mode, psi, 2) - (n**2 / R_psi**2) * pure_mode) == 0,
    "-∂_ψ^2 has eigenvalue n^2/R_ψ^2",
)

print("V9: Gaussian n↔-n degeneracy")
check(
    "V9",
    sp.simplify(sp.exp(-s * n**2 / R_psi**2) - sp.exp(-s * (-n) ** 2 / R_psi**2)) == 0,
    "e^{-sn^2/R_ψ^2}=e^{-s(-n)^2/R_ψ^2}",
)

print("V10: Flat Γ_* square")
a, hbar, p = sp.symbols("a hbar p", real=True)
D4 = sp.Matrix([[0, a], [a, 0]])
Gamma_star = sp.diag(1, -1)
check(
    "V10a_anticommutator",
    matrix_is_zero(D4 * Gamma_star + Gamma_star * D4),
    "{D_4^(0),Γ_*}=0 in the explicit flat model",
)
for eps_name, gamma_psi, eps_value in (
    ("plus", Gamma_star, 1),
    ("minus", sp.I * Gamma_star, -1),
):
    D5 = D4 + sp.I * hbar * gamma_psi * p
    target = D4**2 - hbar**2 * eps_value * p**2 * sp.eye(2)
    check(
        f"V10b_square_{eps_name}",
        matrix_is_zero(sp.simplify(D5**2 - target)),
        f"(D_5^(0))^2=(D_4^(0))^2-hbar^2·{eps_value}·p^2·I",
    )

print()
print("=" * 60)
n_pass = sum(1 for _name, status, _detail in results if status == PASS)
n_fail = sum(1 for _name, status, _detail in results if status == FAIL)
n_not_run = sum(1 for _name, status, _detail in results if status == NOT_RUN)
print(f"Results: {n_pass} passed, {n_fail} failed, {n_not_run} not run")
print("NOTE: This script is a regression / CAS check, not a proof of the")
print("  infinite-dimensional bounded-semigroup proposition.")
print("LEAN-PENDING: operator-domain and continuation existence details remain open.")

if n_fail:
    print("FAILED checks:")
    for name, status, _detail in results:
        if status == FAIL:
            print(f"  {name}")

sys.exit(0 if n_fail == 0 else 1)
