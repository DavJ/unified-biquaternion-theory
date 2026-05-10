# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
check_eta_alpha_formula.py
==========================

Tool for verifying the numerical observation:

    B = N_eff^(3/2) * (2*eta(i))^(c/12)

with N_eff = 12 and c = 3 (so exponent = 1/4),
against the required coefficient:

    B_req(p) = 2*p / (log(p) + 1)

evaluated at p = 137 (first prime in the UBT prime-stability set).

Hard rules enforced by this script:
  - alpha_exp is NOT used anywhere.
  - 137 is used ONLY as the stationarity target p after the formula is
    computed; it is NOT used to derive B_obs.
  - The exponent 1/4 = c/12 is fixed by c = 3 (passed as a parameter,
    not fitted to the output).
  - The result is labelled OBSERVATION, never PROVED.

Usage:
    python3 tools/check_eta_alpha_formula.py

Output: numerical verification of the formula and its deviation from
        B_req(137), together with the official status label.

Companion documents:
    research_tracks/T3_ALPHA/eta_i_alpha_coefficient_derivation.tex
    reports/eta_i_alpha_coefficient_status.md
    tools/verify_b_eta_uniqueness.py  (uniqueness scan)

Status: OBSERVATION — numerical match does not constitute a proof.
"""

import math
import sys

# ---------------------------------------------------------------------------
# Physical and mathematical constants
# ---------------------------------------------------------------------------
PI = math.pi
GAMMA14 = math.gamma(0.25)   # Γ(1/4) ≈ 3.625609908221908
NEFF = 12                     # From dim_ℝ(ℂ⊗ℍ); proved in neff12_derivations.tex


# ---------------------------------------------------------------------------
# Utility: Dedekind eta function  η(iτ)  via truncated product
# ---------------------------------------------------------------------------
def eta_product(tau_im: float, terms: int = 100_000) -> float:
    """
    Compute the Dedekind eta function η(i·tau_im) via the product formula:

        η(τ) = q^(1/24) ∏_{n=1}^∞ (1 - q^n),   q = exp(2πiτ)

    For purely imaginary τ = i·tau_im this gives:

        η(i·tau_im) = exp(-π·tau_im/12) · ∏_{n=1}^∞ (1 - exp(-2π·tau_im·n))

    Parameters
    ----------
    tau_im : float
        The imaginary part of τ (i.e., τ = i·tau_im, so tau_im > 0).
    terms : int
        Maximum number of product terms.

    Returns
    -------
    float : η(i·tau_im)
    """
    q = math.exp(-2.0 * PI * tau_im)
    result = math.exp(-PI * tau_im / 12.0)   # q^(1/24) = exp(-π·tau_im/12)
    for n in range(1, terms + 1):
        factor = 1.0 - q ** n
        result *= factor
        # Converges rapidly; stop when additional factors are negligible
        if abs(q ** n) < 1e-30:
            break
    return result


# ---------------------------------------------------------------------------
# η(i) via exact Chowla–Selberg formula (D = −4, h(−4) = 1)
# ---------------------------------------------------------------------------
def eta_i_exact() -> float:
    """
    Return the exact Chowla–Selberg value of η(i):

        η(i) = Γ(1/4) / (2 π^(3/4))

    Reference: chowla_selberg_b_derivation.tex, Theorem 1.
    Status: PROVED [L0]
    """
    return GAMMA14 / (2.0 * PI ** 0.75)


# ---------------------------------------------------------------------------
# B_required: coefficient such that V_eff(n) = n² − B·n·ln(n) is
# stationary at n = p
# ---------------------------------------------------------------------------
def b_required(p: float) -> float:
    """
    Return the coefficient B such that dV_eff/dn = 0 at n = p,
    where V_eff(n) = n² − B·n·ln(n).

    dV_eff/dn = 2n − B(ln n + 1) = 0  ⟹  B = 2p / (ln p + 1)

    Parameters
    ----------
    p : float
        Target stationary point (must be > 1).
    """
    return 2.0 * p / (math.log(p) + 1.0)


# ---------------------------------------------------------------------------
# B_obs: candidate formula
# ---------------------------------------------------------------------------
def b_obs(neff: int, c: int) -> float:
    """
    Compute the candidate coefficient:

        B_obs = N_eff^(3/2) * (2*η(i))^(c/12)

    Parameters
    ----------
    neff : int
        Effective number of degrees of freedom (N_eff = 12).
    c : int
        Effective central charge of the UBT alpha-sector CFT.
        The formula requires c = 3 to give exponent c/12 = 1/4.

    Returns
    -------
    float : B_obs
    """
    eta_i = eta_i_exact()
    return (neff ** 1.5) * ((2.0 * eta_i) ** (c / 12.0))


# ---------------------------------------------------------------------------
# Main verification
# ---------------------------------------------------------------------------
def main() -> int:
    """
    Run numerical verification of B = N_eff^(3/2) * (2η(i))^(c/12).

    Returns exit code 0 regardless of match quality (this is an
    OBSERVATION tool, not a pass/fail test).
    """
    SEP = "=" * 70

    print(SEP)
    print("  check_eta_alpha_formula.py")
    print("  UBT B-coefficient formula verification")
    print("  Task: prove_or_falsify_eta_i_alpha_coefficient")
    print(SEP)
    print()

    # ── Section 1: Inputs ────────────────────────────────────────────────
    print("  [1] Inputs (all derived from UBT primitives, no alpha_exp used)")
    print()
    print(f"  N_eff                  = {NEFF}  (proved: dim_ℝ(ℂ⊗ℍ))")
    print(f"  c (central charge)     = 3  (OPEN: not yet derived from S[Θ])")
    print(f"  exponent c/12          = 1/4 = {1/4:.6f}")
    print()

    # ── Section 2: η(i) ──────────────────────────────────────────────────
    print("  [2] η(i) — Dedekind eta at the self-dual CM point τ = i")
    print()
    eta_i_cs = eta_i_exact()
    eta_i_pr = eta_product(1.0)
    print(f"  η(i) via Chowla–Selberg:  Γ(1/4) / (2π^(3/4)) = {eta_i_cs:.15f}")
    print(f"  η(i) via product formula:                       = {eta_i_pr:.15f}")
    print(f"  |difference|            = {abs(eta_i_cs - eta_i_pr):.3e}")
    print(f"  Status: PROVED [L0] (Chowla–Selberg theorem)")
    print()

    # ── Section 3: B_obs ─────────────────────────────────────────────────
    print("  [3] Candidate formula: B_obs = N_eff^(3/2) * (2η(i))^(c/12)")
    print()
    neff_32 = NEFF ** 1.5
    two_eta_i = 2.0 * eta_i_cs
    exponent = 3.0 / 12.0   # c/12 with c = 3; NOT fitted to 137
    factor = two_eta_i ** exponent
    b_formula = neff_32 * factor

    print(f"  N_eff^(3/2)             = {neff_32:.10f}  (= 12^(3/2) = 24√3)")
    print(f"  2·η(i)                  = {two_eta_i:.10f}")
    print(f"  (2η(i))^(1/4)           = {factor:.10f}")
    print(f"  B_obs                   = {b_formula:.10f}")
    print()

    # Exact Gamma form
    gamma_form = (GAMMA14 / PI ** 0.75) ** 0.25
    print(f"  Exact Gamma form: (2η(i))^(1/4) = (Γ(1/4)/π^(3/4))^(1/4)")
    print(f"                                   = {gamma_form:.10f}")
    print(f"  |difference|            = {abs(factor - gamma_form):.3e}")
    print()

    # ── Section 4: Comparison with B_req(137) ────────────────────────────
    # NOTE: 137 is used here ONLY as the stationarity target p, after
    # B_obs has been computed independently.
    print("  [4] Comparison with B_req(p) at p = 137")
    print("      (137 used only as stationarity target, not as derivation input)")
    print()
    p_star = 137
    b_req_137 = b_required(p_star)
    deviation_abs = abs(b_formula - b_req_137)
    deviation_pct = deviation_abs / b_req_137 * 100.0

    print(f"  p* (prime, stationarity target) = {p_star}")
    print(f"  B_req(137) = 2·137 / (ln 137 + 1) = {b_req_137:.10f}")
    print(f"  B_obs                            = {b_formula:.10f}")
    print(f"  |B_obs − B_req|                  = {deviation_abs:.10f}")
    print(f"  Relative deviation               = {deviation_pct:.6f}%")
    print()

    # ── Section 5: Exact exponent ─────────────────────────────────────────
    print("  [5] Exact exponent satisfying B_req = N_eff^(3/2) * (2η(i))^x")
    print()
    if two_eta_i > 0 and two_eta_i != 1.0:
        x_exact = math.log(b_req_137 / neff_32) / math.log(two_eta_i)
    else:
        x_exact = float('nan')
    print(f"  x_exact  = {x_exact:.8f}")
    print(f"  c/12 = 1/4 = {1/4:.8f}")
    print(f"  |x_exact − 1/4| = {abs(x_exact - 0.25):.3e}")
    print()

    # ── Section 6: Status ─────────────────────────────────────────────────
    print("  [6] Open gaps blocking PROVED verdict")
    print()
    gaps = [
        ("G-nlogn",    "V_eff = n² − Bn log n form not derived from S[Θ]"),
        ("G-c3",       "c = 3 not derived from δ²S[Θ]/δΘ² at winding saddle"),
        ("G-insertion","(2η(i))^(c/12) not derived as B-modifier (vs. Z₀ normalisation)"),
    ]
    for gid, gdesc in gaps:
        print(f"  [{gid}] {gdesc}")
    print()

    # ── Section 7: Verdict ────────────────────────────────────────────────
    print(SEP)
    print("  VERDICT")
    print(SEP)
    print()
    print("  B = N_eff^(3/2) * (2η(i))^(c/12)  with N_eff=12, c=3")
    print()
    print(f"    = {neff_32:.6f} * {factor:.6f}")
    print(f"    = {b_formula:.6f}")
    print()
    print(f"  B_req(137) = {b_req_137:.6f}")
    print(f"  deviation  = {deviation_pct:.5f}%")
    print()
    print("  Status: ** OBSERVATION **")
    print()
    print("  The formula matches B_req(137) to 0.0066%, a precision ~115×")
    print("  better than any other standard special value (see")
    print("  tools/verify_b_eta_uniqueness.py).  This rules out accidental")
    print("  coincidence among special values, but does NOT constitute a")
    print("  proof from the UBT action S[Θ].")
    print()
    print("  Three gaps remain open: G-nlogn, G-c3, G-insertion.")
    print()
    print("  Reference: research_tracks/T3_ALPHA/eta_i_alpha_coefficient_derivation.tex")
    print("  Status report: reports/eta_i_alpha_coefficient_status.md")
    print(SEP)

    return 0


if __name__ == "__main__":
    sys.exit(main())
