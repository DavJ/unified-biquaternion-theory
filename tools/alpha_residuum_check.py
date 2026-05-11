# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Check whether self-consistency residuum can match one-loop QED correction."""

from __future__ import annotations

import math


def f_self_consistency(p: int) -> float:
    return (5 * p - 1) / (p + 1) - math.log(p)


def delta_qed_lepton(mass_gev: float, alpha: float, uv_scale_gev: float) -> float:
    return (alpha / (3 * math.pi)) * math.log(uv_scale_gev / mass_gev)


def solve_uv_scale_for_single_lepton(target_delta: float, alpha: float, mass_gev: float) -> float:
    exponent = target_delta * (3 * math.pi) / alpha
    return mass_gev * math.exp(exponent)


def solve_uv_scale_for_three_leptons(
    target_delta: float,
    alpha: float,
    m_e: float,
    m_mu: float,
    m_tau: float,
) -> float:
    # target = (alpha/3π) * (ln(Λ/me)+ln(Λ/mμ)+ln(Λ/mτ))
    # => 3 ln Λ = target * (3π/alpha) + ln(me mμ mτ)
    ln_lambda = (target_delta * (3 * math.pi) / alpha + math.log(m_e * m_mu * m_tau)) / 3
    return math.exp(ln_lambda)


def classify_match(relative_error_percent: float) -> str:
    if relative_error_percent < 5:
        return "[MC] strong"
    if relative_error_percent <= 20:
        return "[MC] weak"
    return "[NC]"


def main() -> None:
    p = 137
    f137 = f_self_consistency(p)

    alpha_phys = 1 / 137.036
    alpha_ref = 1 / 137

    m_e = 0.511e-6
    m_mu = 0.1057
    m_tau = 1.777
    m_pl = 1.22e19

    de = delta_qed_lepton(m_e, alpha_phys, m_pl)
    dmu = delta_qed_lepton(m_mu, alpha_phys, m_pl)
    dtau = delta_qed_lepton(m_tau, alpha_phys, m_pl)
    dsum = de + dmu + dtau

    delta_alpha_exp = 137.035999 - 137

    rel_vs_exp = abs(f137 - delta_alpha_exp) / abs(delta_alpha_exp) * 100
    rel_vs_qed = abs(f137 - dsum) / abs(dsum) * 100

    lambda_single = solve_uv_scale_for_single_lepton(f137, alpha_ref, m_e)
    lambda_three = solve_uv_scale_for_three_leptons(f137, alpha_ref, m_e, m_mu, m_tau)

    print("Self-consistency residuum check")
    print("=" * 72)
    print(f"f(137)                  = {f137:.6f}")
    print(f"Δα^-1(exp; observational)= {delta_alpha_exp:.6f}")
    print(f"Relative error vs Δα^-1 = {rel_vs_exp:.3f}%")
    print(f"f(137)/Δα^-1(exp)       = {f137/delta_alpha_exp:.4f}")
    print()

    print("One-loop leptonic QED estimate with Λ = M_Pl")
    print(f"Δ_QED(e)                = {de:.6f}")
    print(f"Δ_QED(μ)                = {dmu:.6f}")
    print(f"Δ_QED(τ)                = {dtau:.6f}")
    print(f"ΣΔ_QED                  = {dsum:.6f}")
    print(f"Relative error vs ΣΔ_QED= {rel_vs_qed:.2f}%")
    print(f"f(137)/ΣΔ_QED           = {f137/dsum:.4f}")
    print(f"Classification          = {classify_match(rel_vs_qed)}")
    print()

    print("UV scale solving Δ_QED(Λ) = f(137)")
    print(f"Single-lepton formula (electron only): Λ = {lambda_single:.3e} GeV")
    print(f"Λ / M_Pl (single-lepton)              = {lambda_single/m_pl:.3e}")
    print(f"Three-lepton summed formula: Λ        = {lambda_three:.3e} GeV")
    print(f"Λ / M_Pl (three-lepton)               = {lambda_three/m_pl:.3e}")


if __name__ == "__main__":
    main()
