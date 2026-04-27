<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T3_ALPHA — Assumptions Audit

**Track**: T3_ALPHA — Fine Structure Constant or Layer2 Fallback  
**Scope**: Full audit of every assumption used in the α derivation chain,
classified by type and justification.  
**Date**: 2026-04-27  
**Sources**: `canonical/appendices/appendix_alpha_geometry.tex`,
`canonical/n_eff/`, `canonical/interactions/B_base_derivation_complete.tex`,
`canonical/geometry/Rpsi_dynamical_fix.tex`

---

## Purpose of This Audit

A complete first-principles derivation of α must not use α or m_e as inputs
at any step.  This document audits every assumption in the current chain and
marks whether it is circular (uses α or m_e), semi-empirical, or derived.

A step is marked:
- **CLEAN** — derived from UBT axioms with zero external input
- **SE** — semi-empirical: value fixed by experiment
- **CIRC** — circular: uses α or m_e as input (must be eliminated for a
  true first-principles derivation)
- **MC** — motivated conjecture: algebraically motivated but not proved
- **OPEN** — missing derivation with no known method

---

## Assumption Inventory

### A1: Fundamental algebra is ℂ⊗ℍ

**Used for**: Everything  
**Justification**: Axiomatic postulate of UBT — the minimal algebra containing
complex structure (quantum phases) and quaternionic structure (Lorentzian geometry)  
**Classification**: CLEAN (axiom, not assumption about α)  
**Circularity check**: ✓ No reference to α or m_e

---

### A2: Complex time τ = t + iψ with S¹_ψ compactification

**Used for**: KK spectrum, N_eff counting, three generations  
**Justification**: Axiomatic; ψ-circle compactification follows from unitarity
of the charged field Θ (Dirac quantisation)  
**Classification**: CLEAN  
**Circularity check**: ✓ No reference to α or m_e

---

### A3: N_eff = 12 = 3 × 2 × 2

**Used for**: B₀ = 2πN_eff/3, and B_base = N_eff^{3/2}  
**Derivation**:
```
N_phases = dim_ℝ(Im ℍ) = 3
N_helicity = 2 (left/right helicity)
N_charge = 2 (charge conjugate pairs)
N_eff = 3 × 2 × 2 = 12
```
**Classification**: CLEAN [L0]  
**Circularity check**: ✓ No reference to α or m_e  
**Source**: `canonical/n_eff/step1_mode_decomposition.tex`

---

### A4: B₀ = 2π N_eff / 3 = 8π

**Used for**: V_eff minimum, B_base lower bound  
**Derivation**: One-loop coefficient from vacuum polarisation of N_eff = 12
charged modes on the ψ-circle.  
**Classification**: CLEAN [L1]  
**Circularity check**: ✓ No reference to α or m_e  
**Source**: `canonical/n_eff/step2_vacuum_polarization.tex`

---

### A5: B_base = N_eff^{3/2} = 12^{3/2} ≈ 41.57

**Used for**: V_eff minimum at n* = 137  
**Derivation status**: PARTIAL [L1] — the formula is derived assuming
Kac-Moody level k = 1, but k = 1 is only a motivated conjecture.  
**Classification**: MC (motivated conjecture for the exponent 3/2)  
**Circularity check**: ✓ No reference to α or m_e  
**Note**: This is the central blocking gap.  If k = 1 were proved, B_base
would be clean.  
**Source**: `canonical/interactions/B_base_derivation_complete.tex`

---

### A6: V_eff(n) = n² − B ln n

**Used for**: Prime attractor at n* = 137  
**Derivation**: One-loop effective potential for winding mode n on S¹_ψ,
combining kinetic term n² and one-loop log term B ln n.  
**Classification**: CLEAN given B — the functional form follows from
one-loop field theory  
**Circularity check**: ✓ No reference to α or m_e  
**Note**: The form is standard; the blocking is B_base (A5).  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §3`

---

### A7: Stationarity condition n* = √(B/2) identifies α⁻¹_bare

**Used for**: α⁻¹_bare = n* = 137  
**Derivation**: `∂V_eff/∂n|_{n*} = 0 ⟹ n* = √(B/2)`.  With B = B_base,
n* ≈ 137.  Identification α⁻¹_bare = n*.  
**Classification**: CLEAN given B_base [L1]  
**Circularity check**: ✓ No reference to α or m_e  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §4`

---

### A8: Prime stability of n* = 137

**Used for**: Selection of n* = 137 as the unique attractor among nearby integers  
**Derivation**: Homotopy argument — the winding number n must be stable under
π₁(S¹_ψ) deformations, which requires n* to be prime (no sub-harmonic modes).  
**Classification**: CLEAN [L1] (mathematical argument)  
**Circularity check**: ✓ No reference to α or m_e  
**Note**: Primality of 137 is used as a *consequence*, not an input.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §4`

---

### A9: Correction δ = α⁻¹ − 137 ≈ 0.036 from two-loop QED

**Used for**: Agreement with experimental α⁻¹ = 137.036  
**Derivation**:
```
α⁻¹(m_e) = α⁻¹_bare + (1/3π) ln(Λ/m_e) + O(α)
```
with Λ ≈ m_e/√α.  
**Classification**: **CIRC** — uses both α and m_e as inputs.  
**Circularity check**: ✗ Circular. Eliminates self-sufficiency of the derivation.  
**Status**: Semi-empirical [SE] until a non-circular derivation is found.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §5`

---

### A10: R_ψ = ℏ/(m_e c) (T-duality self-dual point)

**Used for**: Setting the KK energy scale and relating n* to physical α  
**Derivation**: T-duality: `R_ψ ↔ 1/(2R_ψ)`.  Self-dual point `R_ψ = 1/√2`
in string units.  Calibration: `R_ψ = ℏ/(m_e c)` sets physical units.  
**Classification**: **SE** — the calibration uses m_e as input.  The T-duality
argument is CLEAN, but the physical calibration requires m_e.  
**Circularity check**: ✗ Uses m_e.  
**Source**: `canonical/geometry/Rpsi_dynamical_fix.tex`

---

### A11: N_eff^{3/2} exponent from Kac-Moody level k = 1

**Used for**: B_base = N_eff^{3/2}  
**Derivation**: If the UBT biquaternion field theory on the torus has
Kac-Moody algebra at level k, then the central charge contribution gives
a `k^{1/2}` enhancement of B_base over B₀.  With k = 1:
`B_base = N_eff × k^{1/2} × ... = N_eff^{3/2}` (specific CFT formula).  
**Classification**: MC — k = 1 is a motivated conjecture from CS-term absence  
**Circularity check**: ✓ No reference to α or m_e  
**Source**: `canonical/interactions/B_base_derivation_complete.tex`,
`research_tracks/research/theta_alpha_connection.md §3.1 (H2 approach)`

---

### A12: ΔB = 3π/2 ≈ 4.712 (R-factor additive conjecture)

**Used for**: Correction factor R ≈ 1.114 in B = B_base · R²  
**Derivation**: Motivated by heat-kernel modular weight k = 3/2 and SSB
half-period θ_W^min = π.  
**Classification**: MC — motivated conjecture; 27+ approaches have not
closed this.  
**Circularity check**: ✓ No reference to α (but derivation uses θ_W which
is semi-empirical — indirect circularity)  
**Source**: `DERIVATION_INDEX.md §α`, `research_tracks/research/theta_alpha_connection.md`

---

## Circularity Map

```
DERIVATION CHAIN:
A1 → A2 → A3 → A4 → A5* → A6 → A7 → A8 → n* = 137 = α⁻¹_bare

* A5 blocked by A11 (k=1, MC only)

EMPIRICAL INPUTS (not yet derived):
A9  → δ = 0.036     (uses α, m_e — CIRC)
A10 → R_ψ physical  (uses m_e — SE)
A12 → ΔB = 3π/2     (uses θ_W — indirect SE)
```

**For a truly closed first-principles derivation, A9, A10, A12 must be eliminated,
and A5/A11 must be proved.**

---

## What Would Make the Derivation Clean

| Assumption | Currently | Needed |
|-----------|-----------|--------|
| A5/A11 (k=1, B_base exponent) | MC | Prove k=1 from CFT (modular bootstrap) |
| A9 (δ = 0.036) | CIRC | Derive from S[Θ] without using α or m_e |
| A10 (R_ψ calibration) | SE | Derive R_ψ from S[Θ] without using m_e |
| A12 (ΔB = 3π/2) | MC | Derive from S[Θ] without using θ_W |

**Minimum to claim "first-principles derivation of α⁻¹ = 137"**:
- Prove A5/A11 (k=1 from CFT)
- Accept bare α⁻¹ = 137 as the result (state δ = 0.036 as a known QED correction)

This more limited claim — "UBT predicts α⁻¹_bare = 137" — is achievable if
A5/A11 is proved, and is scientifically significant.

---

## Clean Steps (Can be Presented Without Caveats)

1. N_eff = 12 from ℂ⊗ℍ — CLEAN [L0]
2. B₀ = 8π from one-loop vacuum polarisation — CLEAN [L1]
3. V_eff(n) = n² − B ln n — CLEAN given B [L1]
4. n* = √(B/2) stationarity — CLEAN given B [L1]
5. Prime stability n* = 137 — CLEAN [L1]
6. ψ-circle compactification and Dirac quantisation — CLEAN [L0]
7. T-duality self-dual point (algebraic part) — CLEAN [L0]
