#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
alpha_selfconsistency.py — Self-consistency equation for the fine structure constant.

Task 1 (UBT Copilot Instructions File E):
  Test whether the self-consistency equation

      n* · α + g(α) = 1                        [HYPOTHESIS — see §E.8]

  has a solution α ≈ 1/137 for natural UBT UV cutoffs, where

      g(α) = δm/m_e  — QED one-loop mass correction relative to m_e.

  The equation uses ZERO free parameters (n* = 137 is the topological
  winding input; g(α) follows from standard QED in the UBT limit).

Physical starting point (from docs/ALPHA_FROM_ME_ANALYSIS.md):

      m_0 = 0.509856 MeV   [CALIBRATED — parameter A from fermion mass formula]
      m_e = 0.510999 MeV   [PDG]
      Δm  = m_e − m_0 = 1.143 keV
      Δm/m_e = 0.002237 ≈ α/2π = 0.001161   (close but not equal)

QED one-loop mass correction [DERIVED — standard QED, recovered in UBT limit]:

      δm_QED = (3α/4π) · m_e · ln(Λ²/m_e²)
             = (3α/4π) · m_e · 2·ln(Λ/m_e)

The choice of UV cutoff Λ is the key freedom.  This script tests all
natural UBT cutoffs and reports results honestly.

Self-consistency equation structure:
  m_0 = m_e − δm_QED
  α = m_0/(n*·m_e) = (m_e − δm_QED)/(n*·m_e) = (1 − g(α))/n*
  ⟺  n*·α + g(α) = 1

Circular-logic check:
  Inputs:  n* = 137 (topological — prime winding number, NOT fitted to α)
           g(α) — QED formula (standard, no free parameters)
  α enters only through g(α), making this a genuine self-consistency
  equation (not a tautology), PROVIDED n* is independently motivated.
  Currently n* is accepted as topological input; B_base derivation
  remains incomplete (see STATUS_ALPHA.md).

Classification labels:
    [POSTULATE]   — assumed as starting axiom
    [DERIVED]     — follows by calculation from postulates
    [CALIBRATED]  — free parameter chosen to match data
    [HYPOTHESIS]  — well-posed but not yet derivable; states what would prove it
    [SKETCH]      — outline only; full derivation pending
    [DEAD END]    — approach proved to fail; documented with concrete numbers

Layer: [L2] — requires QED (Standard Model input)
References:
    appendix_E_m0_derivation_strict.tex §E.8
    docs/ALPHA_FROM_ME_ANALYSIS.md
    canonical/interactions/qed.tex
"""

from __future__ import annotations

import math
import sys
from typing import Dict, Tuple

try:
    from scipy.optimize import brentq
except ImportError:
    print("ERROR: scipy not found.  Install with: pip install scipy", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Physical constants  [CALIBRATED / PDG]
# ---------------------------------------------------------------------------

ALPHA_EXP = 1.0 / 137.035999177  # CODATA 2022 fine structure constant
M_E_MEV = 0.510999               # electron mass [MeV], PDG 2022
M_0_MEV = 0.509856               # geometric mass scale [CALIBRATED — param A]
N_STAR = 137                     # topological winding number [TOPOLOGICAL INPUT]

DELTA_M_MEV = M_E_MEV - M_0_MEV  # 1.143 keV — gap to explain
DELTA_M_OVER_ME = DELTA_M_MEV / M_E_MEV  # 0.002237

# ---------------------------------------------------------------------------
# QED one-loop mass correction  [DERIVED — standard QED]
# ---------------------------------------------------------------------------


def g_QED(alpha: float, n_star: int = N_STAR, cutoff: str = "n_star_times_me") -> float:
    """
    Relative mass correction g(α) = δm/m_e from QED one-loop self-energy.

    δm_QED = (3α/4π) · m_e · ln(Λ²/m_e²) = (3α/4π) · m_e · 2·ln(Λ/m_e)
    g(α)   = δm_QED / m_e = (3α/4π) · 2·ln(Λ/m_e) = (3α/2π) · ln(Λ/m_e)

    [DERIVED — standard QED one-loop fermion self-energy, Peskin & Schroeder §7.1]
    UBT reduces to QED in ψ=const limit (Appendix D, canonical/interactions/qed.tex).

    Cutoff choices (UBT natural scales):
    ─────────────────────────────────────────────────────────────────────────
    'n_star_times_me'  :  Λ = n* · m_e     (KK tower at winding n*)
    'classical_radius' :  Λ = m_e / α      (Λ = 1/r_e, classical radius)
    'sqrt_alpha'       :  Λ = m_e / √α     (geometric mean of m_e and 1/r_e)
    'planck_reduced'   :  Λ = m_e/α²       (two powers of α below Planck-like)
    'pair_threshold'   :  Λ = 2 · m_e      (electron pair creation threshold)
    ─────────────────────────────────────────────────────────────────────────
    """
    if cutoff == "n_star_times_me":
        # Λ = n* · m_e  [KK compactification scale; HYPOTHESIS]
        log_ratio = math.log(n_star)  # ln(n*·m_e / m_e) = ln(n*)
    elif cutoff == "classical_radius":
        # Λ = m_e / α  [classical electron radius r_e = α/(m_e); STANDARD]
        log_ratio = math.log(1.0 / alpha)  # ln(m_e/α / m_e) = ln(1/α)
    elif cutoff == "sqrt_alpha":
        # Λ = m_e / √α  [intermediate scale; HYPOTHESIS]
        log_ratio = 0.5 * math.log(1.0 / alpha)
    elif cutoff == "planck_reduced":
        # Λ = m_e / α²  [very high scale; HYPOTHESIS]
        log_ratio = 2.0 * math.log(1.0 / alpha)
    elif cutoff == "pair_threshold":
        # Λ = 2 · m_e  [electron pair threshold; STANDARD QED IR]
        log_ratio = math.log(2.0)
    else:
        raise ValueError(f"Unknown cutoff: {cutoff!r}")

    return (3.0 * alpha / (2.0 * math.pi)) * log_ratio


# ---------------------------------------------------------------------------
# Self-consistency equation  [HYPOTHESIS — §E.8]
# ---------------------------------------------------------------------------


def selfconsistency_eq(
    alpha: float, n_star: int = N_STAR, cutoff: str = "n_star_times_me"
) -> float:
    """
    Residual of the self-consistency equation  n*·α + g(α) − 1 = 0.

    This equation, if satisfied, gives α with ZERO free parameters
    (given n* as topological input and g(α) from QED).

    [HYPOTHESIS — valid if:
     (a) m_0 is truly independent of α,
     (b) the QED formula with the chosen cutoff applies in UBT.]
    """
    return n_star * alpha + g_QED(alpha, n_star, cutoff) - 1.0


# ---------------------------------------------------------------------------
# Required cutoff for Δm = 1.143 keV  [DERIVED — inversion]
# ---------------------------------------------------------------------------


def required_log_ratio() -> Tuple[float, float]:
    """
    Compute ln(Λ/m_e) required so that δm_QED = Δm exactly.

    Inversion of:  (3α/2π) · ln(Λ/m_e) = Δm/m_e
    → ln(Λ/m_e) = (Δm/m_e) / (3·α_exp/(2π))

    [DERIVED — algebraic inversion, no free parameters]
    """
    rhs = DELTA_M_OVER_ME  # 0.002237
    prefactor = 3.0 * ALPHA_EXP / (2.0 * math.pi)  # 3α/(2π)
    log_lam = rhs / prefactor
    lam_over_me = math.exp(log_lam)
    return log_lam, lam_over_me


# ---------------------------------------------------------------------------
# Main: solve and report
# ---------------------------------------------------------------------------


def main() -> None:
    print("=" * 70)
    print("UBT α self-consistency equation  [HYPOTHESIS — Appendix E §E.8]")
    print("=" * 70)
    print()
    print("Observed gap:")
    print(f"  m_0   = {M_0_MEV:.6f} MeV  [CALIBRATED — fermion mass param A]")
    print(f"  m_e   = {M_E_MEV:.6f} MeV  [PDG]")
    print(f"  Δm    = {DELTA_M_MEV * 1e3:.3f} keV")
    print(f"  Δm/m_e = {DELTA_M_OVER_ME:.6f}  (cf. α/2π = {ALPHA_EXP/(2*math.pi):.6f})")
    print()

    # ── Step 1a-1c: δm_QED for each natural UBT cutoff at α = α_exp ──────
    print("─" * 70)
    print("Step 1 — δm_QED for natural UBT cutoffs at α = α_exp:")
    print(f"  QED formula: δm = (3α/4π)·m_e·2·ln(Λ/m_e)")
    print()

    cutoffs = [
        ("n_star_times_me", f"Λ = n*·m_e = {N_STAR}·m_e"),
        ("classical_radius", "Λ = m_e/α  (classical radius)"),
        ("sqrt_alpha", "Λ = m_e/√α"),
        ("planck_reduced", "Λ = m_e/α² "),
        ("pair_threshold", "Λ = 2·m_e  (pair threshold)"),
    ]

    results: Dict[str, Dict] = {}
    for key, desc in cutoffs:
        g = g_QED(ALPHA_EXP, N_STAR, key)
        delta_m_kev = g * M_E_MEV * 1e3
        factor = delta_m_kev / (DELTA_M_MEV * 1e3)
        results[key] = {"g": g, "delta_m_kev": delta_m_kev, "factor": factor}
        print(f"  {desc}")
        print(f"    g(α_exp) = {g:.6f},  δm = {delta_m_kev:.3f} keV  "
              f"(× {factor:.2f} vs Δm = {DELTA_M_MEV*1e3:.3f} keV)")

    print()

    # ── Step 1c: Required cutoff ─────────────────────────────────────────
    log_lam, lam_over_me = required_log_ratio()
    print("─" * 70)
    print("Step 1c — Required cutoff to reproduce Δm = 1.143 keV exactly:")
    print(f"  ln(Λ/m_e) = {log_lam:.4f}  →  Λ/m_e = {lam_over_me:.4f}")
    print(f"  Λ = {lam_over_me * M_E_MEV * 1e3:.1f} keV  ≈ {lam_over_me:.2f}·m_e")
    print(f"  (Pair threshold: 2·m_e = {2*M_E_MEV*1e3:.0f} keV;  "
          f"Λ/m_e = {lam_over_me:.3f} — NOT a standard UBT scale)")
    print()

    # ── Step 2: Self-consistency equation solutions ───────────────────────
    print("─" * 70)
    print("Step 2 — Self-consistency equation  n*·α + g(α) = 1:")
    print(f"  n* = {N_STAR}  [TOPOLOGICAL INPUT]")
    print(f"  α_exp = 1/{1/ALPHA_EXP:.6f}")
    print()

    header = f"  {'Cutoff':<30}  {'α_sol':>12}  {'1/α_sol':>10}  {'Error%':>8}  {'Status'}"
    print(header)
    print("  " + "-" * (len(header) - 2))

    sc_results = {}
    for key, desc in cutoffs:
        short = desc.split("(")[0].strip()
        try:
            sol = brentq(
                selfconsistency_eq, 1e-5, 0.5, args=(N_STAR, key), xtol=1e-14
            )
            err_pct = abs(sol - ALPHA_EXP) / ALPHA_EXP * 100.0
            status = "✓ (<1%)" if err_pct < 1.0 else "✗ DEAD END"
            sc_results[key] = {"alpha": sol, "error_pct": err_pct, "status": status}
            print(
                f"  {short:<30}  {sol:.8f}  {1/sol:>10.3f}  {err_pct:>7.3f}%  {status}"
            )
        except Exception as exc:
            sc_results[key] = {"alpha": None, "error_pct": None, "status": f"No solution: {exc}"}
            print(f"  {short:<30}  {'N/A':>12}  {'N/A':>10}  {'N/A':>8}  No solution: {exc}")

    print()

    # ── Summary / verdict ─────────────────────────────────────────────────
    print("─" * 70)
    print("VERDICT:")
    any_good = any(
        v.get("error_pct") is not None and v["error_pct"] < 1.0
        for v in sc_results.values()
    )
    if any_good:
        print("  ✓ Self-consistency equation solved with <1% error for at least")
        print("    one natural UBT cutoff.  Classification: [DERIVED — conditional")
        print("    on g(α) from QED in UBT limit and chosen cutoff].")
        print("  ⚠  Verify that the chosen cutoff is independently motivated")
        print("     (not fitted to reproduce α = 1/137).")
    else:
        best_key = min(
            (k for k, v in sc_results.items() if v.get("error_pct") is not None),
            key=lambda k: sc_results[k]["error_pct"],
            default=None,
        )
        if best_key is not None:
            best = sc_results[best_key]
            print(f"  ✗ No natural UBT cutoff gives <1% error.")
            print(f"    Best: '{best_key}' → α = 1/{1/best['alpha']:.2f}, "
                  f"error = {best['error_pct']:.2f}%")
        print()
        print("  CONCLUSION [DEAD END — concrete numbers]:")
        print("    The self-consistency equation  n*·α + g(α) = 1  has no solution")
        print("    within 1% of α_exp for any of the natural UBT UV cutoffs tested.")
        # Compute representative α⁻¹ from the best dead-end result
        if best_key is not None:
            rep_inv_alpha = round(1.0 / sc_results[best_key]["alpha"])
        else:
            rep_inv_alpha = 139  # fallback
        print(f"    All solutions cluster near α ≈ 1/{rep_inv_alpha}, not 1/137.")
        print()
        print("    The gap Δm = 1.143 keV would require Λ ≈ 1.90·m_e ≈ 970 keV,")
        print("    which lies between m_e and 2·m_e (pair threshold) — not a")
        print("    recognised UBT geometric scale.")
        print()
        print("    Classification: [HYPOTHESIS — no natural UBT cutoff confirmed]")
        print("    What would confirm it: derivation of Λ ≈ 1.9·m_e from UBT")
        print("    geometry without reference to m_e or α.")

    print()
    print(
        "See appendix_E_m0_derivation_strict.tex §E.8 for the analytic derivation."
    )
    print("See docs/ALPHA_FROM_ME_ANALYSIS.md §8 for the updated status.")


if __name__ == "__main__":
    main()
