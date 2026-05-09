<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Modular Covariance Verdict for `S[Theta]`

**Task**: `prove_or_kill_modular_covariance_of_ubt_action`  
**Date**: 2026-05-09  
**Companion file**: `research_tracks/alpha_spectral/modular_covariance_of_STheta.tex`

---

## Verdict

> **NO-GO**
>
> Full SL(2,ℤ) modular covariance of the current UBT action S[Θ] is **not
> established**.  Two precisely located obstructions block the proof (O1, O2),
> and a third obstruction (O3) for equal-action Hecke saddles follows as a
> corollary.  The arithmetic layer (torus setup, mode relabelling, Jacobi count
> p+1) is exact and unconditional; the physics layer fails at the operator and
> measure levels.

---

## Requirement-by-requirement outcome

| Requirement | Outcome | Notes |
|---|---|---|
| Define τ = t+iψ as torus modulus | **PROVED** | Def. 1.1 in companion .tex; τ = (t+iψ)/β ∈ ℍ whenever ψ > 0. Euclidean compactification of both t and ψ required for genuine torus. |
| Define SL(2,ℤ) action on τ | **PROVED** | Standard Möbius action γ·τ = (aτ+b)/(cτ+d); generators T: τ↦τ+1, S: τ↦−1/τ. Group law and ℍ-stability exact. |
| Compute induced transformation of Θ modes | **PROVED** | Lattice relabelling: Θ'_{m,n}(x) = Θ_{(m,n)γ⁻¹}(x). Mode map U_γ is unitary on ℓ²(ℤ²). Lemma 3.1 in companion .tex. |
| T-covariance of ∇†∇ (flat background) | **PROVED** | Spectrum λ_{m,n,k} is periodic in integer lattice labels; T-shift t_E → t_E+β only cycles indices. Proposition 4.1. |
| S-covariance of ∇†∇ (flat background, generic torus) | **NO-GO** | Obstruction O1: spectrum (m²/R_t² + n²/R_ψ²) does not acquire a definite modular weight under S unless R_t = R_ψ (square torus). Proposition 4.2. |
| Definite modular weight for ∇†∇ (curved background) | **NO-GO** | Obstruction O1 (curved): Weitzenböck curvature couplings require weight assignment for the full Θ hierarchy; absent from canonical axioms. |
| Jacobian of dψ under SL(2,ℤ) | **PROVED** | dψ → \|cτ+d\|⁻² dψ (Case A, only ψ transforms). d t_E dψ → \|cτ+d\|⁻⁴ d t_E dψ (Case B, full torus reparametrisation). Proposition 5.1. |
| Compensation of Jacobian by ℒ (weight +2 or +4) | **NO-GO** | Obstruction O2: Lagrangian density ℒ has not been shown to carry modular weight +2 (Case A) or +4 (Case B). No ghost/compensator sector defined in UBT. |
| Equal-action Hecke saddles | **NO-GO** | Obstruction O3 (= O1 + O2): equal-action ↔ S[Θ] is SL(2,ℤ)-invariant (Proposition 6.1, necessary and sufficient). Blocked by O1 and O2. |

---

## Exact obstructions

### O1 — Operator weight under S-generator

**Statement**: On a generic torus with R_t ≠ R_ψ, the kinetic operator
∇†∇ does not transform with a definite modular weight under S: τ ↦ −1/τ.
The spectrum after mode relabelling becomes (n²/R_t² + m²/R_ψ²) which
differs from the original unless R_t = R_ψ.

**Where it bites**: Without a proved operator weight, the kinetic Lagrangian
density cannot be assigned a definite modular weight, blocking O2 and O3.

**What would resolve it**:
- **Path A**: Show that UBT field equations on T² imply R_t = R_ψ (self-dual
  condition). On the square torus, S acts as a cycle swap that does preserve
  the spectrum after mode relabelling.
- **Path B**: Postulate field weight (k,k̄) for Θ and derive that the kinetic
  density then has weight +2; verify consistency with GR/SM limits.

### O2 — Measure Jacobian cancellation

**Statement**: The integration measure d⁴x dψ acquires Jacobian |cτ+d|⁻²
(if only ψ transforms, Case A) or |cτ+d|⁻⁴ (if the full t_E-ψ torus is
reparametrised, Case B). The Lagrangian density must carry weight +2 (or +4)
to cancel. This cancellation has not been derived.

**Where it bites**: Blocks full SL(2,ℤ) invariance of S[Θ], and thereby
blocks the equal-action saddle conclusion.

**What would resolve it**:
- **Path C**: Identify fermionic + bosonic one-loop modular anomaly
  cancellation within Θ, analogous to the superstring. Requires counting
  bosonic/fermionic DoF in Θ and their weight contributions.

### O3 — Equal-action Hecke saddles (corollary of O1+O2)

**Statement**: Equal-action Hecke saddle degeneracy holds if and only if
S[Θ] is SL(2,ℤ)-invariant (Proposition 6.1 in companion .tex, necessary and
sufficient). Resolves automatically once O1 and O2 are resolved.

---

## What is exact (unconditional)

| Claim | Proof |
|---|---|
| τ = (t+iψ)/β ∈ ℍ for ψ > 0 | Elementary complex analysis |
| SL(2,ℤ) acts on ℍ by Möbius transformations | Standard modular forms |
| Mode relabelling U_γ is unitary on ℓ²(ℤ²) | Lemma 3.1 (bijection of ℤ², measure-preserving) |
| T-covariance of ∇†∇ on flat background | Proposition 4.1 |
| dψ → \|cτ+d\|⁻² dψ | Proposition 5.1 (Jacobian computation) |
| \|Γ₀(p)∖SL(2,ℤ)\| = p+1 | Index formula for congruence subgroups |
| p+1 saddle candidates exist | Coset construction (arithmetic) |
| Equal-action ↔ SL(2,ℤ)-invariant S | Proposition 6.1 (necessary and sufficient) |

---

## What is conditional or unproved

| Claim | Condition needed |
|---|---|
| S-covariance of ∇†∇ | O1: R_t = R_ψ (or field-weight assignment) |
| Lagrangian has weight +2 | O2: compensation mechanism |
| S[Θ] is SL(2,ℤ)-invariant | O1 + O2 |
| p+1 saddles are equal-action | O1 + O2 + O3 |

---

## Upgrade paths

Three routes from NO-GO to CONDITIONAL:

| Path | Mechanism | Difficulty |
|---|---|---|
| A | Derive R_t = R_ψ from UBT field equations | Requires variational analysis of the ψ-sector |
| B | Assign modular weight to Θ; verify consistency | Requires checking all canonical limits (GR, SM) |
| C | Fermionic/bosonic anomaly cancellation | Requires DoF count and one-loop weight computation |

None of the three paths can be completed without significant additional derivation
from S[Θ]. Until at least one path is completed, the verdict remains NO-GO.

---

## Downstream implications

- **Hecke bridge (hecke_equivariant_path_integral.tex)**: Obstruction O1 of
  that document is confirmed and identical to O1 here. The present analysis
  provides the precise mathematical statement of O1 (spectrum mismatch under
  S on generic torus).
- **B-coefficient gap G137-B**: Remains conditional. B(p) = (p+1)/3 is
  arithmetically exact but its physical derivation from S[Θ] is blocked by O1–O3.
- **Modular prime attractor theorem**: Unaffected by this analysis; that
  theorem operates at the arithmetic level and does not depend on S[Θ] being
  SL(2,ℤ)-invariant.

---

## Hard-rule compliance

- No α input used. ✓
- No fixed-prime (p = 137 or similar) input used. ✓
- No η(i) fitting used. ✓
- Final verdict class from mandatory set: **NO-GO**. ✓

