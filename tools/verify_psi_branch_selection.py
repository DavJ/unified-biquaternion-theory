#!/usr/bin/env python3
"""
verify_psi_branch_selection.py
==============================
Regression / CAS checks for the ψ-branch selection research track.

This script verifies finite-dimensional algebraic and numerical claims from
  research_tracks/complex_time_branch_selection/psi_branch_selection.en.md
  research_tracks/complex_time_branch_selection/psi_branch_selection.cs.md

It is NOT a proof of the infinite-dimensional functional-analytic proposition.
LEAN-PENDING: A Lean 4 proof of the Hardy-H² branch selection proposition has
not yet been written or compiled.

Checks performed
----------------
V1  Factorisation of the second-order scalar operator (∂_t² + A²)
V2  Both time branches e^{±itA} are solutions of the second-order equation
V3  Analytic continuation t → t - iψ
V4  Decay / growth signs for the two branches under ψ > 0
V5  Finite-dimensional diagonal example with positive self-adjoint A
V6  Zero-mode degeneracy (ker A sector)
V7  Fourier eigenvalues n and n² on S¹
V8  Gaussian e^{-s n²} does not distinguish n from -n

Exit code: 0 if all checks pass, 1 if any check fails.
"""

import sys
import cmath
import math

PASS = "PASS"
FAIL = "FAIL"
results = []


def check(name: str, condition: bool, detail: str = "") -> None:
    status = PASS if condition else FAIL
    msg = f"  [{status}] {name}"
    if detail:
        msg += f": {detail}"
    print(msg)
    results.append((name, condition))


# ---------------------------------------------------------------------------
# V1: Factorisation of (∂_t² + A²) = (i∂_t - A)(-i∂_t - A)
#     Verify symbolically on a scalar exponential e^{iωt}.
#     For ω = A:  (i∂_t - A)e^{iAt} = (i·iA - A)e^{iAt} = (-A - A)e^{iAt} ≠ 0 in general,
#     but (i∂_t - A) applied to e^{itA} gives 0 when A = ω (positive branch),
#     and (-i∂_t - A) applied to e^{-itA} gives 0 (negative branch).
#     We check: (∂_t² + A²) applied to both branches gives 0.
# ---------------------------------------------------------------------------
print("V1: Factorisation of second-order operator")

def apply_d2_plus_A2(branch_fn, A_val, t_val):
    """
    Numerically approximate (∂_t² + A²)Φ at time t for a scalar branch Φ.
    branch_fn(t) -> complex scalar.
    """
    h = 1e-4  # finite-difference step; larger gives better cancellation for smooth oscillating functions
    d2 = (branch_fn(t_val + h) - 2 * branch_fn(t_val) + branch_fn(t_val - h)) / h**2
    return d2 + A_val**2 * branch_fn(t_val)

A = 2.5  # positive self-adjoint scalar (diagonal element)
t0 = 1.3

branch_pos = lambda t: cmath.exp(1j * A * t)   # e^{+itA}  (negative-frequency generator)
branch_neg = lambda t: cmath.exp(-1j * A * t)  # e^{-itA}  (positive-frequency generator)

res_pos = apply_d2_plus_A2(branch_pos, A, t0)
res_neg = apply_d2_plus_A2(branch_neg, A, t0)

check("V1a", abs(res_pos) < 1e-5, f"|result|={abs(res_pos):.2e}")
check("V1b", abs(res_neg) < 1e-5, f"|result|={abs(res_neg):.2e}")

# ---------------------------------------------------------------------------
# V2: Both branches satisfy second-order equation (already done in V1,
#     here we confirm with a second A value and a superposition)
# ---------------------------------------------------------------------------
print("V2: Both branches satisfy second-order equation")

A2 = 0.7
branch_super = lambda t: 0.6 * cmath.exp(1j * A2 * t) + 0.4 * cmath.exp(-1j * A2 * t)
res_super = apply_d2_plus_A2(branch_super, A2, t0)
check("V2a", abs(res_super) < 1e-5, f"superposition |result|={abs(res_super):.2e}")

# ---------------------------------------------------------------------------
# V3: Analytic continuation t → z = t - iψ
#     Φ(t,ψ) = e^{-itA}e^{-ψA} u_+  +  e^{+itA}e^{+ψA} u_-
# ---------------------------------------------------------------------------
print("V3: Analytic continuation t → t - iψ")

psi = 1.0
u_plus = 1.0 + 0j
u_minus = 1.0 + 0j
A3 = 1.5
t3 = 0.8

# Direct substitution z = t - i*psi into e^{-izA} = e^{-i(t-ipsi)A} = e^{-itA} e^{-psi*A}
z = t3 - 1j * psi
branch_continued_plus = cmath.exp(-1j * z * A3) * u_plus
expected_plus = cmath.exp(-1j * t3 * A3) * math.exp(-psi * A3) * u_plus

branch_continued_minus = cmath.exp(+1j * z * A3) * u_minus
expected_minus = cmath.exp(+1j * t3 * A3) * math.exp(+psi * A3) * u_minus

check("V3a_plus",  abs(branch_continued_plus  - expected_plus)  < 1e-12,
      f"diff={abs(branch_continued_plus-expected_plus):.2e}")
check("V3b_minus", abs(branch_continued_minus - expected_minus) < 1e-12,
      f"diff={abs(branch_continued_minus-expected_minus):.2e}")

# ---------------------------------------------------------------------------
# V4: Decay / growth signs under ψ > 0
#     Positive branch: e^{-ψA} decays for A > 0, ψ > 0
#     Negative branch: e^{+ψA} grows for A > 0, ψ > 0
# ---------------------------------------------------------------------------
print("V4: Decay / growth signs for ψ > 0")

A4 = 2.0
psi4 = 0.5
decay_factor  = math.exp(-psi4 * A4)
growth_factor = math.exp(+psi4 * A4)

check("V4a_decay",  decay_factor < 1.0,
      f"e^{{-ψA}} = {decay_factor:.4f} < 1  (decays)")
check("V4b_growth", growth_factor > 1.0,
      f"e^{{+ψA}} = {growth_factor:.4f} > 1  (grows)")
check("V4c_product", abs(decay_factor * growth_factor - 1.0) < 1e-12,
      "e^{-ψA}·e^{+ψA} = 1")

# ---------------------------------------------------------------------------
# V5: Finite-dimensional diagonal example
#     A = diag(a1, a2, a3) with all aᵢ > 0
#     After imposing the boundedness condition, u_- = 0 outside ker A.
# ---------------------------------------------------------------------------
print("V5: Finite-dimensional diagonal example")

import numpy as np

eigenvalues = np.array([0.5, 1.0, 3.0])  # all positive, ker A = {0}
psi5 = 1.0

# e^{+ψA} applied to a vector: grows without bound as ψ → ∞
# For boundedness we need the coefficient of e^{+ψA} to be 0 (outside ker A)
u_minus_vec = np.array([0.3, 0.7, 0.2])  # generic vector
growth_norms = np.exp(psi5 * eigenvalues) * np.abs(u_minus_vec)

# All components of e^{+ψA}u_- grow
check("V5a_all_grow", np.all(growth_norms > np.abs(u_minus_vec)),
      f"max growth norm = {growth_norms.max():.4f}")

# Positive branch decays
u_plus_vec = np.array([1.0, 0.5, 0.2])
decay_norms = np.exp(-psi5 * eigenvalues) * np.abs(u_plus_vec)
check("V5b_positive_decays", np.all(decay_norms < np.abs(u_plus_vec)),
      f"max remaining norm = {decay_norms.max():.4f}")

# The decayed vector has smaller norm than the original
check("V5c_norm_decrease",
      np.linalg.norm(decay_norms) < np.linalg.norm(u_plus_vec),
      f"‖e^{{-ψA}}u_+‖={np.linalg.norm(decay_norms):.4f} < ‖u_+‖={np.linalg.norm(u_plus_vec):.4f}")

# ---------------------------------------------------------------------------
# V6: Zero-mode degeneracy — elements of ker A are constant in t and ψ
# ---------------------------------------------------------------------------
print("V6: Zero-mode degeneracy (ker A sector)")

# Extend eigenvalues to include a zero
eigenvalues_with_zero = np.array([0.0, 1.0, 2.0])
A_zero = 0.0  # first eigenvalue is 0

# e^{±ψ·0} = 1 for all ψ: zero mode is bounded in both half-planes
for psi_test in [0.1, 1.0, 10.0, 100.0]:
    val = math.exp(psi_test * A_zero)  # = 1.0
    if abs(val - 1.0) > 1e-12:
        check("V6_zero_mode_bounded", False, f"failed at ψ={psi_test}")
        break
else:
    check("V6_zero_mode_bounded", True,
          "e^{±ψ·0} = 1 for all ψ — zero mode is in neither branch")

# Non-zero modes: growth factor at ψ=100
A_nonzero = eigenvalues_with_zero[1]
growth_large_psi = math.exp(100.0 * A_nonzero)
check("V6_nonzero_mode_grows", growth_large_psi > 1e30,
      f"e^{{100·{A_nonzero}}} = {growth_large_psi:.2e}")

# ---------------------------------------------------------------------------
# V7: Fourier eigenvalues n and n² on S¹
#     -i∂_ψ e^{inψ/R} = (n/R) e^{inψ/R}   → eigenvalue n
#     -∂_ψ² e^{inψ/R} = (n/R)² e^{inψ/R}  → eigenvalue n²/R²
# ---------------------------------------------------------------------------
print("V7: Fourier eigenvalues n and n² on S¹")

R_psi = 2.0  # radius of S¹_ψ
psi_test = 0.9

for n in [-3, -1, 0, 1, 2, 3]:
    mode = cmath.exp(1j * n * psi_test / R_psi)
    # -i ∂_ψ: numerical derivative
    h = 1e-5
    mode_fwd = cmath.exp(1j * n * (psi_test + h) / R_psi)
    mode_bwd = cmath.exp(1j * n * (psi_test - h) / R_psi)
    d_psi = (mode_fwd - mode_bwd) / (2 * h)
    eigenval_first = -1j * d_psi / mode if abs(mode) > 1e-15 else 0
    expected_n = n / R_psi

    # Second derivative uses a smaller step for better accuracy
    h2 = 1e-4
    mode_fwd2 = cmath.exp(1j * n * (psi_test + h2) / R_psi)
    mode_bwd2 = cmath.exp(1j * n * (psi_test - h2) / R_psi)
    d2_psi = (mode_fwd2 - 2 * mode + mode_bwd2) / h2**2
    eigenval_second = -d2_psi / mode if abs(mode) > 1e-15 else 0
    expected_n2 = (n / R_psi) ** 2

    err_first  = abs(eigenval_first  - expected_n)
    err_second = abs(eigenval_second - expected_n2)

    if err_first > 1e-5 or err_second > 1e-5:
        check(f"V7_n={n}", False,
              f"Δ_first={err_first:.2e}, Δ_second={err_second:.2e}")
        break
else:
    check("V7_all_n", True,
          "eigenvalues n/R and n²/R² verified for n ∈ {-3,-1,0,1,2,3}")

# ---------------------------------------------------------------------------
# V8: Gaussian e^{-sn²} does not distinguish n from -n
# ---------------------------------------------------------------------------
print("V8: Gaussian e^{-sn²} does not distinguish n from -n")

s_val = 0.3
R8 = 2.0
all_symmetric = True
for n in range(1, 6):
    pos = math.exp(-s_val * (n / R8) ** 2)
    neg = math.exp(-s_val * ((-n) / R8) ** 2)
    if abs(pos - neg) > 1e-15:
        all_symmetric = False
        check(f"V8_n={n}", False, f"e^{{-s·n²}} ≠ e^{{-s·(-n)²}}: {pos} vs {neg}")
        break

if all_symmetric:
    check("V8_symmetry", True,
          "e^{-s n²/R²} = e^{-s(-n)²/R²} for n=1,...,5  (n and -n indistinguishable)")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print()
print("=" * 60)
n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
print(f"Results: {n_pass} passed, {n_fail} failed out of {len(results)} checks")

if n_fail > 0:
    print()
    print("FAILED checks:")
    for name, ok in results:
        if not ok:
            print(f"  {name}")

print()
print("NOTE: This script verifies finite-dimensional algebraic identities only.")
print("LEAN-PENDING: The infinite-dimensional Hardy-H² branch selection proposition")
print("  (Section 2.4 of psi_branch_selection.en.md) has not been Lean-formalised.")

sys.exit(0 if n_fail == 0 else 1)
