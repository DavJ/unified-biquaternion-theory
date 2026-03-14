# Higgs and Yukawa Sector — Preliminary Scan

**Project**: Unified Biquaternion Theory (UBT)  
**Version**: v59  
**Date**: 2026-03-14  
**Status**: Preliminary scan — Motivated Conjectures; no closed derivations  
**Track**: `research_tracks/` (not yet canonical)

> AGENTS.md §13: do less, not more.  
> Do NOT claim Yukawa couplings derived without explicit S[Θ] computation.  
> Do NOT claim full SM from UBT — sin²θ_W is a Dead End.

---

## 1. Background and Scope

UBT has established:

- **SU(3)×SU(2)_L×U(1)** gauge group from ℂ⊗ℍ **[Proved L0]**
  (see `canonical/su3_derivation/su3_from_involutions.tex`,
  `canonical/interactions/B_base_derivation_complete.tex`)
- **Gravitational sector**: Schwarzschild from Θ₀ **[Proved L1]**
- **QED sector**: U(1)_EM unbroken, Schwinger term, Lamb shift sketch **[L1]**

**What is missing for full SM**:
1. Higgs boson / spontaneous symmetry breaking (SSB) mechanism
2. Yukawa couplings (fermion masses from Higgs VEV)
3. sin²θ_W (Weinberg angle) — **confirmed Dead End** (see §4)

**Scope of this scan**: Steps 1 and 2 only.
Fermion mass spectrum: **not attempted here** — confirmed Dead End
(KK mismatch; see `docs/STATUS_ALPHA.md` and
`ARCHIVE/archive_legacy/consolidation_project/appendix_K_fermion_mass.tex`).

---

## 2. Does S[Θ] Contain a Higgs Potential?

### 2.1 UBT Action

The UBT action is (schematically):

```
S[Θ] = ∫ d⁴x dψ  Sc[ (∇†Θ)†(∇†Θ) ]
```

where Sc[·] denotes the scalar (real) part of the biquaternion product,
∇† is the biquaternionic conjugate derivative, and the integral is over
real spacetime M⁴ and the imaginary-time circle S¹(R_ψ).

### 2.2 Effective Potential from ψ-Integration

Integrating out the ψ-circle gives an effective 4d action with an effective
potential V_eff(|Θ|). The leading terms in an expansion around a constant
background Θ = Θ₀ are:

```
V_eff(|Θ|²) = a₂|Θ|² + a₄|Θ|⁴ + O(|Θ|⁶)
```

**Key observation**: The mirror-sector structure of UBT (sectors n* = 137
and n** = 139) implies a Z₂ symmetry:

```
Θ → -Θ   ⟹   V_eff(|Θ|²) = V_eff(|-Θ|²)
```

This symmetry forbids odd powers of |Θ| and forces the Mexican-hat form
when a₂ < 0:

```
V(|Θ|²) = λ(|Θ|² - v²)²    (Higgs potential)
```

with λ = a₄ > 0 and v² = -a₂/(2a₄).

### 2.3 Assessment

**Motivated Conjecture**: V(|Θ|²) = λ(|Θ|²−v²)² arises from S[Θ] at tree
level in the ψ-integration, driven by the Z₂ symmetry of mirror sectors.

**NOT proved**: The explicit values of λ and v from S[Θ] are not derived
here.

**Open Gaps**:
- **Gap H1**: Compute a₄ = λ from the quartic term in S[Θ] expansion
- **Gap H2**: Compute a₂ and the VEV v² = −a₂/(2a₄); same as Gap Y2
  in `DERIVATION_INDEX.md §QED Reproducibility` (derive VEV v from V\_eff(θ₀) on ψ-circle)

**Status**: **Motivated Conjecture** — algebraic argument present;
explicit S[Θ] computation required for [L1] status.

---

## 3. Does S[Θ] Contain a Yukawa Coupling?

### 3.1 Θ-Fermion Coupling Term

The biquaternion product of Θ with a left-handed spinor ψ_L and
right-handed spinor ψ_R (both embedded as biquaternions via Clifford
algebra) gives:

```
Θ† · ψ_L · ψ_R    (biquaternion product)
```

Taking the scalar part Sc[·] extracts the Lorentz-invariant combination:

```
ℒ_Yukawa = y · Sc(Θ† · ψ_L · ψ_R) + h.c.
```

This is structurally identical to the Standard Model Yukawa coupling
after Θ is identified with the Higgs doublet H via the SU(2)_L embedding.

### 3.2 Assessment

**Motivated Conjecture**: The Yukawa coupling ℒ_Yukawa ~ Sc(Θ†·ψ_L·ψ_R)
is present in the Θ-fermion sector of S[Θ] at tree level.

**NOT proved**:
- The explicit coupling constant y is not derived
- The fermion mass m_f = y·v requires both y and v (Gaps Y1, Y2)
- The derivation of fermion mass ratios is a confirmed **Dead End**
  (KK mismatch for three generations)

**Open Gap Y1**: Derive Yukawa coupling y from S[Θ] — see
`DERIVATION_INDEX.md §QED Reproducibility` Gap Y1.

**Status**: **Motivated Conjecture** — structural argument present;
y from S[Θ] requires explicit computation.

---

## 4. Weinberg Angle sin²θ_W — Confirmed Dead End

The Weinberg angle sin²θ_W = g'²/(g² + g'²) requires the ratio of
U(1)_Y and SU(2)_L gauge couplings g', g. In UBT:

- g (SU(2)_L) is fixed by the biquaternion structure
- g' (U(1)_Y) involves a free mixing parameter that ℂ⊗ℍ alone does
  not constrain

**Confirmed Dead End**: sin²θ_W cannot be derived from ℂ⊗ℍ alone.
The algebra fixes the gauge symmetry group but not the relative coupling
strengths between factors.

This is consistent with the finding in `DERIVATION_INDEX.md` that the
Standard Model mixing is not an algebraic consequence of ℂ⊗ℍ.

---

## 5. Summary Table

| Question | Answer | Status |
|----------|--------|--------|
| Does S[Θ] contain V(|Θ|²) = λ(|Θ|²−v²)²? | Yes, motivated by Z₂ symmetry | **Motivated Conjecture** |
| Are λ, v derived? | No — Gaps H1, H2 | **Open** |
| Does S[Θ] contain ℒ_Yukawa ~ Sc(Θ†·ψ_L·ψ_R)? | Yes, structurally | **Motivated Conjecture** |
| Is y derived? | No — Gap Y1 | **Open** |
| Can fermion masses be derived? | No — KK mismatch | **Dead End** |
| Can sin²θ_W be derived from ℂ⊗ℍ? | No | **Dead End** |

---

## 6. Next Steps

1. **Gap H1**: Expand S[Θ] to quartic order around Θ = Θ₀ = v·**1**;
   extract λ = a₄ explicitly. This is a concrete algebraic computation.

2. **Gap H2 / Y2**: Compute V_eff minimum on ψ-circle to fix v.
   This is related to the n*=137 attractor (circular if not done
   independently).

3. **Gap Y1**: Compute the Yukawa vertex from the Θ-fermion coupling
   Lagrangian term. This requires specifying the fermion embedding
   in the biquaternion algebra.

None of these steps should claim to derive the full fermion mass spectrum —
that remains a confirmed Dead End.

---

*© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0*  
*See LICENSE.md for full license text.*
