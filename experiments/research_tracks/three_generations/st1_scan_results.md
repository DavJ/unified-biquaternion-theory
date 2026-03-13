# ST-1: Exhaustive Scan of ℂ⊗ℍ for Three-Fold Structure

**Track:** THREE_GENERATIONS  
**Date:** 2026-03-03  
**Status:** Complete — see per-candidate verdicts below  
**Author:** David Jaroš  

> © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0  
> Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.

---

## Summary

Four candidate mechanisms for producing a natural three-fold decomposition of
`ℂ⊗ℍ ≅ M₂(ℂ)` were investigated systematically.  Three are obstructed by
algebra; one — the complex-time ψ-mode expansion (Candidate 4) — provides a
genuine UBT-specific mechanism.

| Candidate | Description | Result |
|-----------|-------------|--------|
| 1 | Minimal left ideal decomposition of M₂(ℂ) | **NOT FOUND** — obstruction (§1) |
| 2 | Z₂³ grading refinement / Z₃ extension | **NOT FOUND** — obstruction (§2) |
| 3 | Tensor product (ℂ⊗ℍ)⊗ℂ³ or V_c⊗V_c | **NOT FOUND** — no canonical split (§3) |
| 4 | Complex time ψ-mode expansion of Θ | **FOUND** (conditional) — mechanism identified (§4) |

---

## 1. Ideal Decomposition

**Question.** Does M₂(ℂ) ≅ ℂ⊗ℍ admit a decomposition into three minimal left
ideals?

**Structure of minimal left ideals of M₂(ℂ).**  A minimal left ideal of M₂(ℂ)
is of the form L_e = M₂(ℂ)·e, where e is a primitive idempotent
(rank-1 projector, e² = e, rank(e) = 1).  Any such ideal satisfies
dim_ℂ(L_e) = 2.

**Decomposition into two ideals.**  The algebra M₂(ℂ) decomposes as a direct
sum of exactly two minimal left ideals:

```
M₂(ℂ) = L_{e₁} ⊕ L_{e₂}
```

where e₁ = diag(1,0), e₂ = diag(0,1) are the two standard rank-1 idempotents.
Each L_{eₖ} ≅ ℂ² as a ℂ-vector space (= one column of M₂(ℂ)).

**Obstruction to three ideals.**  Any collection of three minimal left ideals
would have total ℂ-dimension at least 3 × 2 = 6, but dim_ℂ M₂(ℂ) = 4.  Three
mutually disjoint minimal left ideals do not fit.  Moreover, M₂(ℂ) is a simple
algebra (Wedderburn–Artin), so every direct sum decomposition into left ideals
uses exactly `n` copies of the unique simple module (here n=2).

**Verdict: NOT FOUND.  Obstruction by dimension.**

---

## 2. Z₂³ Grading Refinement / Z₃ Extension

**Question.** Can the Z₂³ grading (proved in `papers/su3_triplet/arxiv_version.tex`)
be extended or combined with a Z₃ action to produce three isomorphic sectors?

**Z₂³ eigenspace structure.**  The three commuting involutions P₁, P₂, P₃ of
`ℬ = ℂ⊗ℍ` yield simultaneous eigenspaces.  The six non-empty sectors, their
(P₁,P₂,P₃) eigenvalues, representative basis elements, and ℝ-dimensions are:

```
(+,+,+): {1}           dim_ℝ = 1
(−,+,+): {i}           dim_ℝ = 1
(+,−,+): {J, K}        dim_ℝ = 2
(−,−,+): {iJ, iK}     dim_ℝ = 2
(+,+,−): {I}           dim_ℝ = 1
(−,+,−): {iI}          dim_ℝ = 1
```

(Sectors (+,−,−) and (−,−,−) are empty because P₃(I)=I but P₂(I)=−I and
P₃(J)=−J, so the P₃=−1 subspace lies inside P₂=−1.)

**No Z₃ subgroup in Z₂³.**  The group Z₂³ has order 8, which is not divisible
by 3.  Therefore Z₂³ contains no subgroup isomorphic to Z₃.  There is no Z₃
action compatible with the Z₂³ grading as a sub-action or quotient action.

**Attempt at an extrinsic Z₃.**  One might try to define a Z₃ action by a
120°-rotation of the J,K-plane combined with a phase on I.  However, any such
map would not commute with the algebra multiplication in ℬ (since the structure
constants of ℍ have Z₂ symmetry, not Z₃ symmetry), and would not preserve the
algebra structure of M₂(ℂ).  It would be a new, externally imposed symmetry,
not one intrinsic to ℬ.

**Verdict: NOT FOUND.  No Z₃ structure is intrinsic to ℂ⊗ℍ.**

---

## 3. Tensor Product V_c⊗V_c or (ℂ⊗ℍ)⊗ℂ³

**Question.** Does V_c⊗V_c or (ℂ⊗ℍ)⊗ℂ³ contain a natural three-fold
decomposition without adding new algebra?

**V_c⊗_ℂ V_c.**  As a ℂ-vector space, V_c⊗V_c ≅ ℂ⁹.  Under SU(3)_{V_c},
this transforms in the adjoint-plus-singlet decomposition:
`3 ⊗ 3̄ = 8 ⊕ 1` (8-dimensional adjoint + singlet).  The Clebsch–Gordan
decomposition `3 ⊗ 3 = 6 ⊕ 3̄` gives a 6 and a 3̄, neither of which is a
three-fold direct sum of equivalent representations.  No natural three
isomorphic copies arise.

**(ℂ⊗ℍ)⊗_ℂ ℂ³ = M₂(ℂ)⊗_ℂ ℂ³.**  As a ℂ-algebra module, M₂(ℂ)⊗ℂ³ ≅ M₂(ℂ³)
(the 3×3 block-diagonal embedding).  As a ℂ-vector space this is 12-dimensional.
One can write it as a direct sum of three copies of M₂(ℂ) (one copy per
ℂ-basis vector of ℂ³), but this decomposition requires *choosing* the basis of
the external ℂ³ factor.  It is not intrinsic to M₂(ℂ) alone; the ℂ³ has been
added by hand.  This does not produce three generations from ℂ⊗ℍ — it
generates them by postulating ℂ³ from outside.

**Verdict: NOT FOUND.  Tensor products require external ℂ³ input, which
is not intrinsic to ℬ.**

---

## 4. Complex Time τ = t + iψ: ψ-Mode Expansion

**Question.** Does the imaginary time coordinate ψ in τ = t+iψ introduce a
natural three-fold structure through Fourier/Taylor expansion in ψ?

**Setup.**  In UBT, the Θ-field is a ℬ-valued function of complex time:
Θ(x, τ) = Θ(x, t+iψ) where x ∈ M⁴, τ ∈ ℂ, ψ = Im(τ).

**ψ-Taylor modes.**  Expand formally around ψ=0:

```
Θ(x, t, ψ) = Θ₀(x,t) + ψ·Θ₁(x,t) + ψ²·Θ₂(x,t) + …
```

Each coefficient Θₙ(x,t) is a ℬ-valued field on ordinary (real) spacetime.

**Three-generation candidate.**  The lowest three modes Θ₀, Θ₁, Θ₂ are
ℬ-valued fields that:

1. **Carry the same SU(3) quantum numbers** — each Θₙ lives in the same carrier
   space ℬ and, when projected to V_c, transforms in the fundamental
   representation **3** of SU(3)_{V_c}.

2. **Are kinematically independent** — for a general Θ analytic in τ, the
   Taylor coefficients Θ₀, Θ₁, Θ₂ are independent functions on M⁴ (they are
   partial-ψ-derivatives of Θ at ψ=0, hence independent initial data).

3. **Are separated by a conserved ψ-mode number** — under the
   shift τ → τ + iε (i.e., ψ → ψ + ε), Θₙ gains a phase factor
   (−1)ⁿ for ψ → −ψ.  More precisely, under ψ-parity P_ψ: ψ → −ψ,
   Θₙ → (−1)ⁿ Θₙ.  The modes with n=0,1,2 have distinct ψ-parity
   structure (even/odd/even), but their ψ-mode number n = 0, 1, 2
   is an additional label.

4. **Mass hierarchy (conjecture, not proved)** — higher ψ-modes are
   associated with larger "ψ-excitation energy," suggesting
   m(Θ₀) ≪ m(Θ₁) ≪ m(Θ₂), which would correspond to the hierarchy
   m_e ≪ m_μ ≪ m_τ.  This is **not proved** at this stage.

**UBT-specific character.**  This mechanism is entirely absent from Furey's
approach (ℂ⊗𝕆), which has no complex time.  The ψ-modes are a direct
consequence of AXIOM B (τ = t+iψ) in the UBT axiomatic base.

**Verdict: FOUND (conditional).**  The ψ-mode expansion provides a natural
three-fold structure with the correct SU(3) quantum numbers.  Independence of
modes is established kinematically.  Mass hierarchy and mixing suppression
remain **conjectures** pending dynamical analysis (see ST-3).

---

## Overall Conclusion

Three algebraic routes to three generations within ℂ⊗ℍ are obstructed:

> **Structural theorem (ST-2 preview):**  ℂ⊗ℍ ≅ M₂(ℂ) does not admit an
> intrinsic decomposition into three mutually isomorphic subspaces preserved by
> the Z₂³ grading and carrying independent SU(3)_{V_c} representations.

The unique UBT-specific route via complex time ψ-modes does provide a
three-generation mechanism:

> **Working hypothesis (ST-3):**  Three generations of fermions in UBT arise as
> the three lowest Taylor modes Θ₀, Θ₁, Θ₂ of the Θ-field in the imaginary
> time coordinate ψ.  Octonions are not required.

Full details: ST-2 obstruction proof → `st2_obstruction.tex`;
ψ-mode mechanism → `st3_complex_time_generations.tex`;
Furey comparison → `st4_furey_comparison.md`.
