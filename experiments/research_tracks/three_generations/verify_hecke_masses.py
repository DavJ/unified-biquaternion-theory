# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
verify_hecke_masses.py
======================

Step 3 of the Hecke-generations research track:
Test the conjecture that lepton mass ratios equal Hecke eigenvalue ratios
for the modular forms f_n associated to the UBT Fourier modes Θ̂_n.

Conjecture 2.1 (Hecke generations, step2_modular_symmetry.tex):
    m_n / m_0 = λ_p(f_n) / λ_p(f_0)
where p = 137 is the UBT prime from α⁻¹ = p + Δ_CT.

Run with:
    python verify_hecke_masses.py
"""

import numpy as np

# -------------------------------------------------------------------------
# Experimental mass ratios (CODATA / PDG 2022)
# -------------------------------------------------------------------------
m_mu_over_me  = 206.7682830   # muon/electron
m_tau_over_me = 3477.23       # tau/electron

print("=== Experimental mass ratios ===")
print(f"m_μ/m_e = {m_mu_over_me:.4f}")
print(f"m_τ/m_e = {m_tau_over_me:.4f}")

p = 137  # UBT prime (α⁻¹ = p + Δ_CT, cf. UBT_HeckeWorlds_theta_zeta_primes_appendix.tex)

# -------------------------------------------------------------------------
# Approach A: Eisenstein series E_k
# For Eisenstein series: λ_p(E_k) = 1 + p^(k-1)
# -------------------------------------------------------------------------
print(f"\n=== Hecke eigenvalues for Eisenstein series E_k at p={p} ===")
for k in [2, 4, 6, 8, 10, 12]:
    lam = 1 + p**(k-1)
    print(f"  k={k}: λ_{p}(E_{k}) = {lam:.2e}")

# -------------------------------------------------------------------------
# Search for (k_0, k_1, k_2) giving experimental mass ratios
# Using λ_p(E_{k_n}) / λ_p(E_{k_0}) with tolerance 10 %
# -------------------------------------------------------------------------
print(f"\n=== Search for (k_0, k_1, k_2) giving experimental ratios ===")
found_any = False
for k0 in range(2, 14, 2):
    lam0 = 1 + p**(k0-1)
    for k1 in range(2, 14, 2):
        lam1 = 1 + p**(k1-1)
        ratio1 = lam1 / lam0
        for k2 in range(2, 14, 2):
            lam2 = 1 + p**(k2-1)
            ratio2 = lam2 / lam0
            err1 = abs(ratio1 - m_mu_over_me) / m_mu_over_me
            err2 = abs(ratio2 - m_tau_over_me) / m_tau_over_me
            if err1 < 0.1 and err2 < 0.1:
                found_any = True
                print(f"  MATCH: k=({k0},{k1},{k2}), "
                      f"ratios=({ratio1:.2f},{ratio2:.2f}), "
                      f"errors=({err1:.1%},{err2:.1%})")

if not found_any:
    print("  No exact match within 10% found for Eisenstein series.")
    print("  Documenting best candidates per ratio:")
    # Report best per individual ratio
    best1 = min(
        ((k0, k1, abs((1+p**(k1-1))/(1+p**(k0-1)) - m_mu_over_me)/m_mu_over_me)
         for k0 in range(2, 14, 2) for k1 in range(2, 14, 2)),
        key=lambda t: t[2]
    )
    best2 = min(
        ((k0, k2, abs((1+p**(k2-1))/(1+p**(k0-1)) - m_tau_over_me)/m_tau_over_me)
         for k0 in range(2, 14, 2) for k2 in range(2, 14, 2)),
        key=lambda t: t[2]
    )
    print(f"    Best muon  ratio: k0={best1[0]}, k1={best1[1]}, "
          f"ratio={(1+p**(best1[1]-1))/(1+p**(best1[0]-1)):.2f}, "
          f"error={best1[2]:.1%}")
    print(f"    Best tau   ratio: k0={best2[0]}, k2={best2[1]}, "
          f"ratio={(1+p**(best2[1]-1))/(1+p**(best2[0]-1)):.2f}, "
          f"error={best2[2]:.1%}")

# -------------------------------------------------------------------------
# Approach B: Ramanujan bound ranges for cusp forms
# For weight-k cusp form: |λ_p(f)| ≤ 2 p^((k-1)/2)
# -------------------------------------------------------------------------
print(f"\n=== Ramanujan bound ranges at p={p} ===")
for k in [2, 4, 6, 8, 12]:
    bound = 2 * p**((k-1)/2)
    print(f"  k={k}: |λ_p| ≤ {bound:.2f}")

print(f"\nExperimental target: λ_ratio ~ 207 or 3477")
print(f"Does any weight give eigenvalues in this range?")

# -------------------------------------------------------------------------
# Summary: cusp-form range check
# The conjecture requires λ_137(f_1)/λ_137(f_0) ≈ 206.77
# and λ_137(f_2)/λ_137(f_0) ≈ 3477.
# If |λ_p(f_n)| ≤ 2*p^((k_n-1)/2) (Ramanujan), the ratio can be at most
#   2*p^((k_1-1)/2) / (lower bound of |λ_137(f_0)|).
# For a cusp form, the lower bound of |λ_p(f_0)| need not be bounded away
# from zero, so Ramanujan alone does not rule out the conjecture.
# -------------------------------------------------------------------------
print(f"\n=== Cusp-form scenario: can ratios reach 207 and 3477? ===")
print("  Ramanujan bound gives |λ_p(f_n)| ≤ 2*p^((k_n-1)/2).")
print("  If f_0 is a cusp form with small |λ_p(f_0)|, large ratios ARE possible.")
print("  Example: if |λ_137(f_0)| = 1 (as for weight-2 normalised newform),")
print("           then λ_ratio ≈ 2*137^((k_1-1)/2).")
for k in [4, 6, 8, 10, 12]:
    candidate_ratio = 2 * p**((k-1)/2)
    print(f"    k_1={k}: max ratio with λ_0=1 → {candidate_ratio:.1f}")
print(f"  Target ratios: {m_mu_over_me:.1f} (muon), {m_tau_over_me:.1f} (tau)")
print()
print("  Interpretation:")
print("  - k=4 max ratio 3207 > 207  → k_1=4 CAN accommodate m_μ/m_e")
print(f"  - k=4 max ratio 3207 < 3477 → k_2=4 CANNOT accommodate m_τ/m_e")
print(f"  - k=6 max ratio 4.4e5 > 3477 → k_2=6 CAN accommodate m_τ/m_e")
print(f"  Minimal consistent weight assignment: k=(2,4,6)")

# -------------------------------------------------------------------------
# Conclusion
# -------------------------------------------------------------------------
print("\n=== CONCLUSION ===")
print("Approach A (Eisenstein series):")
print(f"  λ_p(E_k) = 1 + p^(k-1) grows as p^(k-1) for large p.")
print(f"  Consecutive even weights k give ratios p^(k1-k0) = 137^2 = {137**2}.")
print(f"  None of these simple ratios coincides with 206.77 or 3477.2.")
print(f"  Verdict: Eisenstein series with standard weights do NOT match.")
print()
print("Approach B (cusp forms):")
print(f"  The Ramanujan bound does not rule out ratios of 207 or 3477.")
print(f"  A weight-k_1 cusp form could yield λ_137 ≈ 207 if normalised correctly.")
print(f"  This requires identifying the specific newform whose Hecke eigenvalue")
print(f"  at p=137 equals the experimental ratio — an open arithmetic problem.")
print()
print("Framework verdict:")
print("  The Hecke generations conjecture (Conjecture 2.1) is NOT RULED OUT")
print("  by this numerical test, but it is not confirmed by Eisenstein series alone.")
print("  The minimal consistent weight assignment is k=(2,4,6):")
print("   k_0=2 (weight-2 newform for f_0),")
print("   k_1=4 (weight-4 cusp form for f_1, Ramanujan bound 3207 > 207),")
print("   k_2=6 (weight-6 cusp form for f_2, Ramanujan bound ~4.4e5 > 3477).")
print("  The required modular forms are cusp forms (newforms) whose L-function")
print("  special values need to be matched to mass ratios — see step4_modular_forms.tex.")
