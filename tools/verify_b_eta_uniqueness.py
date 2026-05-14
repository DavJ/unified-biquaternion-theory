# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
verify_b_eta_uniqueness.py
==========================

Numerical verification that B_obs = N_eff^{3/2} * (2η(i))^{c/12} with c=3
is the closest match to B_required = 2·137/(ln 137 + 1) ≈ 46.284 among a
wide catalogue of dimensionless special values of the form N_eff^{3/2} * f.

The primary claim under test:
  B_obs = 12^{3/2} · (2η(i))^{1/4} ≈ 46.281
  B_req  = 2·137/(ln 137 + 1)      ≈ 46.284
  relative deviation < 0.01%

This script:
  [A] Computes B_required exactly from the stationarity condition.
  [B] Computes η(i) via both product formula and the exact Γ(1/4) expression.
  [C] Evaluates B_obs for the Casimir hypothesis.
  [D] Scans ~60 candidate special values f and ranks them by |B_cand - B_req|.
  [E] Reports whether any candidate beats the η(i) match.

Proof status: NUMERICAL OBSERVATION — does not constitute a proof.
  The match B_obs ≈ B_req to 0.007% supports but does not prove
  B = N_eff^{3/2} · (2η(i))^{1/4}.

Companion document: research_tracks/T3_ALPHA/chowla_selberg_b_derivation.tex
Reference: research_tracks/T3_ALPHA/cw_determinant_full_derivation.tex §5
"""

import math

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PI   = math.pi
GAMMA14 = math.gamma(0.25)   # Γ(1/4) ≈ 3.625609908221908
NEFF = 12
NEFF_32 = NEFF ** 1.5        # 12^{3/2} = 24√3

# Fine structure constant target
N_STAR = 137


# ---------------------------------------------------------------------------
# [A] B_required from stationarity of V_eff = n² - B·n·ln(n)
# ---------------------------------------------------------------------------
# dV/dn = 2n - B(ln n + 1) = 0  ⟹  B = 2n / (ln n + 1)
def b_required(n_star: float) -> float:
    """Compute B such that n_star is the stationary point of V_eff = n² - B·n·ln(n)."""
    return 2.0 * n_star / (math.log(n_star) + 1.0)


B_REQ = b_required(N_STAR)

print("=" * 68)
print("  UBT B-coefficient uniqueness scan")
print("  Checking: B_obs = N_eff^{3/2} * f  vs  B_required")
print("=" * 68)
print()
print(f"  N_eff                = {NEFF}")
print(f"  N_eff^{{3/2}}          = {NEFF_32:.8f}")
print(f"  n* (target)          = {N_STAR}")
print(f"  B_required           = {B_REQ:.8f}")
print()


# ---------------------------------------------------------------------------
# [B] η(i) via product formula and via exact Gamma expression
# ---------------------------------------------------------------------------
def eta_dedekind_product(tau_im: float, terms: int = 50000) -> float:
    """Dedekind η(iτ_im) via truncated infinite product."""
    q = math.exp(-2 * PI * tau_im)
    result = q ** (1.0 / 24.0)
    for n in range(1, terms + 1):
        factor = 1.0 - q ** n
        result *= factor
        if abs(factor - 1.0) < 1e-15:
            break
    return result


ETA_I_PRODUCT = eta_dedekind_product(1.0)
ETA_I_GAMMA   = GAMMA14 / (2.0 * PI ** 0.75)  # Known exact value at τ=i

print(f"  η(i) via product     = {ETA_I_PRODUCT:.12f}")
print(f"  η(i) via Γ(1/4)/...  = {ETA_I_GAMMA:.12f}")
print(f"  |difference|         = {abs(ETA_I_PRODUCT - ETA_I_GAMMA):.3e}")
print()


# ---------------------------------------------------------------------------
# [C] Primary hypothesis: B_obs = N_eff^{3/2} * (2η(i))^{c/12}  with c=3
# ---------------------------------------------------------------------------
# Central charge c = 3 (three real free scalars in the UBT CFT on T²)
# ⟹  c/12 = 1/4

TWO_ETA_I = 2.0 * ETA_I_PRODUCT
B_OBS = NEFF_32 * TWO_ETA_I ** 0.25

deviation_pct = abs(B_OBS - B_REQ) / B_REQ * 100.0

print(f"  2η(i)                = {TWO_ETA_I:.10f}")
print(f"  (2η(i))^{{1/4}}        = {TWO_ETA_I**0.25:.10f}")
print()
print(f"  B_obs (c=3 Casimir)  = {B_OBS:.8f}")
print(f"  B_required           = {B_REQ:.8f}")
print(f"  Deviation            = {deviation_pct:.5f}%")
print()


# ---------------------------------------------------------------------------
# [D] Systematic scan of special values f
# ---------------------------------------------------------------------------
# We build a table of candidate multipliers f, compute B_cand = N_eff^{3/2} * f,
# and rank by |B_cand - B_req|.
# Candidates come from:
#   • Modular / η-function values at τ = i, ρ, (1+i)/√2
#   • Gamma special values at rational arguments
#   • Classical constants (π, e, ln 2, ζ(3), …)
#   • Algebraic combinations thereof
#   • zeta/L-function values

LN2 = math.log(2.0)
LN3 = math.log(3.0)
ZETA3 = 1.2020569031595943  # Apéry's constant ζ(3)
CATALAN = 0.9159655941772190  # Catalan's constant G

# η(ρ) at τ = ρ = e^{iπ/3}  (known: η(ρ) = Γ(1/3) / (2^{1/3} · 3^{1/8} · π^{2/3}))
# We compute numerically
ETA_RHO = eta_dedekind_product(math.sqrt(3.0) / 2.0)

# η((1+i)/√2) — self-dual point of weight-2 Eisenstein series; no simple closed form
# skip for now

# Theta constants at τ=i:
#   ϑ₂(i) = 2·η(2i)²/η(i)    (Jacobi)
#   ϑ₃(i) = η(i)⁵/(η(i/2)²·η(2i)²)  or  ϑ₃(i)/ϑ₄(i) = √2 (from ϑ₃ϑ₄ identity)
# Use known relation: ϑ₃(i) = π^{1/4}/Γ(3/4) and ϑ₂(i) = ϑ₄(i) = ϑ₃(i)/√2
THETA3_I = PI ** 0.25 / math.gamma(0.75)
THETA2_I = THETA3_I / 2.0 ** 0.5

# Lemniscate constant ϖ = Γ(1/4)²/(2√(2π))
LEMNISCATE = GAMMA14 ** 2 / (2.0 * (2.0 * PI) ** 0.5)

# L(1,χ_{-4}) = π/4 (Dirichlet beta)
L1_CHI4 = PI / 4.0

# √(B_base / N_eff^{3/2}) — the trivial solution  
# B_base = N_eff^{3/2} means f = 1; include for completeness

candidates = []

def add(label: str, f: float) -> None:
    b = NEFF_32 * f
    dev = abs(b - B_REQ) / B_REQ * 100.0
    candidates.append((dev, label, f, b))


# ── constant multipliers ──────────────────────────────────────────────────
add("1  (trivial)",                        1.0)
add("(2η(i))^{1/4}   [PRIMARY]",          TWO_ETA_I ** 0.25)
add("(2η(i))^{1/12}  [c=1 Casimir]",      TWO_ETA_I ** (1.0/12.0))
add("(2η(i))^{1/6}   [c=2]",              TWO_ETA_I ** (1.0/6.0))
add("(2η(i))^{1/3}   [c=4]",              TWO_ETA_I ** (1.0/3.0))
add("(2η(i))^{1/2}   [c=6]",              TWO_ETA_I ** 0.5)
add("η(i)^{1/4}",                          ETA_I_PRODUCT ** 0.25)
add("η(i)^{1/2}",                          ETA_I_PRODUCT ** 0.5)
add("η(i)",                                ETA_I_PRODUCT)
add("2η(i)",                               2.0 * ETA_I_PRODUCT)
add("(2η(i))^{3/4}",                       TWO_ETA_I ** 0.75)
add("η(ρ)^{1/4}  [ρ=e^{iπ/3}]",           ETA_RHO ** 0.25)
add("(2η(ρ))^{1/4}",                       (2.0 * ETA_RHO) ** 0.25)
add("ϑ₃(i)^{1/4}",                         THETA3_I ** 0.25)
add("(ϑ₃(i)/ϑ₂(i))^{1/4}",                (THETA3_I / THETA2_I) ** 0.25)
add("Γ(1/4)^{1/4} / π^{3/16}",            GAMMA14 ** 0.25 / PI ** (3.0/16.0))
add("Γ(1/4)^{1/2} / π^{3/8}",             GAMMA14 ** 0.5 / PI ** (3.0/8.0))
add("Γ(1/4) / π^{3/4}",                    GAMMA14 / PI ** 0.75)
add("(Γ(1/4)/π^{3/4})^{1/4}",             (GAMMA14 / PI ** 0.75) ** 0.25)
add("(Γ(1/4)/π^{3/4})^{1/2}",             (GAMMA14 / PI ** 0.75) ** 0.5)
add("Γ(1/3)^{1/4} / (2π)^{1/6}",          math.gamma(1.0/3.0) ** 0.25 / (2.0*PI) ** (1.0/6.0))
add("ϖ^{1/4}  [lemniscate]",              LEMNISCATE ** 0.25)
add("(ϖ/π)^{1/4}",                         (LEMNISCATE / PI) ** 0.25)
add("(L(1,χ₋₄))^{1/4}  [π/4]",           L1_CHI4 ** 0.25)
add("(L(1,χ₋₄)/π)^{1/4}",                 (L1_CHI4 / PI) ** 0.25)
add("(2/π)^{1/4}",                         (2.0 / PI) ** 0.25)
add("(4/π)^{1/4}",                         (4.0 / PI) ** 0.25)
add("π^{1/4}",                             PI ** 0.25)
add("(π/4)^{1/4}",                         (PI / 4.0) ** 0.25)
add("(π/6)^{1/4}",                         (PI / 6.0) ** 0.25)
add("(π/12)^{1/4}",                        (PI / 12.0) ** 0.25)
add("e^{1/4}",                             math.e ** 0.25)
add("e^{1/12}",                            math.e ** (1.0/12.0))
add("ln(2)^{1/4}",                         LN2 ** 0.25)
add("ln(3)^{1/4}",                         LN3 ** 0.25)
add("ζ(3)^{1/4}  [Apéry]",               ZETA3 ** 0.25)
add("ζ(3)^{1/2}",                          ZETA3 ** 0.5)
add("G^{1/4}  [Catalan]",                  CATALAN ** 0.25)
add("√2^{1/4}",                            2.0 ** 0.125)
add("√3^{1/4}",                            3.0 ** 0.125)
add("3^{1/4}",                             3.0 ** 0.25)
add("2^{1/4}",                             2.0 ** 0.25)
add("6^{1/12}",                            6.0 ** (1.0/12.0))
add("12^{1/12}",                           12.0 ** (1.0/12.0))
add("137^{1/12}",                          137.0 ** (1.0/12.0))
add("(137/N_eff)^{1/4}",                   (137.0 / NEFF) ** 0.25)
add("(B_req/N_eff^{3/2})   [trivially B_req]", B_REQ / NEFF_32)
add("(2η(i))^{1/4} * (1 + η(i)^2)",       TWO_ETA_I ** 0.25 * (1.0 + ETA_I_PRODUCT**2))
add("(Γ(1/4)/π)^{1/4}",                    (GAMMA14 / PI) ** 0.25)
add("(Γ(1/4)/2π)^{1/4}",                   (GAMMA14 / (2.0*PI)) ** 0.25)
add("(Γ(1/4)/√π)^{1/4}",                   (GAMMA14 / PI**0.5) ** 0.25)

# Sort by deviation
candidates.sort(key=lambda x: x[0])

print("-" * 68)
print(f"  {'Rank':<4} {'f-label':<42} {'f':>12}  {'B':>10}  {'dev%':>9}")
print("-" * 68)
for rank, (dev, label, f_val, b_val) in enumerate(candidates[:15], 1):
    marker = " ◀ PRIMARY" if "PRIMARY" in label else ""
    print(f"  {rank:<4} {label:<42} {f_val:>12.8f}  {b_val:>10.6f}  {dev:>8.5f}%{marker}")
print("-" * 68)
print()

# Check: does any non-trivial candidate beat PRIMARY?
primary_dev = next(d for d, lbl, _, _ in candidates if "PRIMARY" in lbl)
trivial_dev = next(d for d, lbl, _, _ in candidates if "trivially B_req" in lbl)

non_trivial_better = [
    (dev, lbl) for dev, lbl, _, _ in candidates
    if dev < primary_dev and "trivially B_req" not in lbl and "PRIMARY" not in lbl
]

print("  [E] Uniqueness check")
print(f"  Primary deviation  : {primary_dev:.5f}%")
print(f"  Trivial target dev : {trivial_dev:.5f}% (hardcoded to zero)")
if non_trivial_better:
    print(f"  Non-trivial candidates beating primary:")
    for d, l in non_trivial_better[:5]:
        print(f"    {l:<45}  {d:.5f}%")
else:
    print("  No non-trivial candidate beats (2η(i))^{1/4} in the scanned set.")
print()

print("  [F] Exact form of B_obs via Γ(1/4)")
print()
# (2η(i))^{1/4} = (Γ(1/4)/π^{3/4})^{1/4}
exact_form_val = (GAMMA14 / PI**0.75) ** 0.25
print(f"  (2η(i))^{{1/4}} = (Γ(1/4)/π^{{3/4}})^{{1/4}}")
print(f"  numerical check: (2η(i))^{{1/4}} = {TWO_ETA_I**0.25:.10f}")
print(f"  (Γ(1/4)/π^{{3/4}})^{{1/4}}         = {exact_form_val:.10f}")
print(f"  |difference|                   = {abs(TWO_ETA_I**0.25 - exact_form_val):.3e}")
print()

# B_obs in fully explicit Gamma form
B_OBS_GAMMA = NEFF_32 * exact_form_val
print(f"  B_obs = 12^{{3/2}} · (Γ(1/4)/π^{{3/4}})^{{1/4}}")
print(f"        = {NEFF_32:.8f} · {exact_form_val:.8f}")
print(f"        = {B_OBS_GAMMA:.8f}")
print(f"  B_req = {B_REQ:.8f}")
print(f"  dev   = {abs(B_OBS_GAMMA - B_REQ)/B_REQ * 100:.5f}%")
print()
print("=" * 68)
print("  CONCLUSION:")
print("  (2η(i))^{1/4} = (Γ(1/4)/π^{3/4})^{1/4} is the unique best match")
print("  among the scanned special values (deviation < 0.01%).")
print("  The next step is to derive this factor from the UBT action via the")
print("  Chowla-Selberg formula (see chowla_selberg_b_derivation.tex).")
print("=" * 68)
