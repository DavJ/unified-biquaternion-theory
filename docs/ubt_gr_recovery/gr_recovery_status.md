# GR Recovery Status

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0

This document tracks the proof status of the General Relativity recovery claim
in the Unified Biquaternion Theory (UBT).  Each assumption is stated, its
location of use is noted, and its current proof status is indicated.

## Precise Claim

> **Under assumptions A1–A3 below, the real projection of the biquaternionic
> field equation**
>
>   Re(𝒢_μν) = κ Re(𝒯_μν)
>
> **yields the Einstein tensor G_μν satisfying ∇^μ G_μν = 0 (Bianchi identity)
> and matching the standard GR form G_μν = R_μν − ½ g_μν R = 8πG T_μν.**

GR is therefore **not contradicted** by UBT; it is **embedded** as the real-valued
limit of the richer biquaternionic structure.

---

## Enumerated Assumptions

| ID | Assumption | Where used | Status |
|----|-----------|------------|--------|
| A1 | **Hermitian tetrad in real limit**: In the limit ψ → 0, E_μ† = E_μ, so that 𝒢_μν → g_μν ∈ ℝ | Lemma `lem:re_omega_levi_civita` (appendix_R_GR_equivalence.tex §3); imaginary cross-term cancellation in metric compatibility | **Assumed** (consistent with standard real-tetrad constructions in GR) |
| A2 | **Torsion-free in real sector**: Ω^λ_[μν] = 0 after real projection | Lemma `lem:re_omega_levi_civita` Step 2; uniqueness of Levi-Civita connection | **Assumed** (corresponds to zero torsion condition; physically natural for gravity without spin-torsion coupling) |
| A3 | **Inverse tetrad exists**: ∃ Ẽ^μ with Ẽ^μ ∘ E_μ = 𝟏 | Lemma `lem:omega_from_tetrad` (biquaternion_connection.tex §4); used to solve tetrad postulate for Ω_μ | **Assumed** (generic for non-degenerate frames; degeneracy is a measure-zero condition) |

---

## Symbol Disambiguation

| Symbol | Meaning | Location |
|--------|---------|----------|
| 𝒢_μν  | Biquaternionic metric tensor (𝒢_μν ∈ ℬ) | biquaternion_metric.tex |
| g_μν   | Real spacetime metric: g_μν := Re(𝒢_μν) | appendix_R_GR_equivalence.tex |
| G_μν   | Classical Einstein tensor: G_μν := R_μν − ½ g_μν R | appendix_R_GR_equivalence.tex §4 |
| ℰ_μν  | Biquaternionic Einstein tensor: ℰ_μν := ℛ_μν − ½(𝒢_μν ℛ), where ℛ = 𝒢^μν ℛ_μν (left-multiplication convention) | biquaternion_curvature.tex |
| Ω_μ    | Biquaternionic connection (derived from tetrad postulate) | biquaternion_connection.tex |
| Γ^λ_μν | Levi-Civita connection: Γ^λ_μν = Re(Ω^λ_μν) | Proved in Lemma `lem:re_omega_levi_civita` |

> **No symbol collision**: 𝒢_μν always denotes the biquaternionic *metric*; G_μν always
> denotes the classical Einstein *tensor*.  These are distinct objects.

---

## Proof Checklist

- [x] **Biquaternion algebra is associative** — stated in `canonical/fields/biquaternion_algebra.tex`
  §"Algebraic Properties"; incorrect non-associativity claims removed from geometry files.
- [x] **Ω_μ derived from tetrad postulate** — Lemma `lem:omega_from_tetrad` in
  `canonical/geometry/biquaternion_connection.tex`; Christoffel-by-substitution removed.
- [x] **Re(Ω) = Levi-Civita Γ** — Lemma `lem:re_omega_levi_civita` in
  `consolidation_project/appendix_R_GR_equivalence.tex` with explicit 3-step proof.
- [x] **Second Bianchi identity in non-commutative setting** — Theorem `thm:bianchi_biquaternion`
  in `canonical/geometry/biquaternion_curvature.tex`; proof uses associativity and
  graded Jacobi via commutator; does not assume commutativity.
- [x] **Contracted Bianchi → ∇^μ G_μν = 0** — follows from theorem above after real
  projection; cross-terms vanish under A1.
- [ ] **Full operator Re(∇†∇Θ) → G_μν**: the detailed step-by-step reduction of the
  biquaternionic d'Alembertian to the Einstein tensor is stated but not yet fully
  expanded; labeled as **conjecture pending detailed derivation**.

---

## Files Modified in This Pass

| File | Change |
|------|--------|
| `canonical/geometry/biquaternion_connection.tex` | Removed non-associativity claim; added Lemma `lem:omega_from_tetrad` (tetrad postulate derivation); removed invalid Christoffel substitution |
| `canonical/geometry/biquaternion_curvature.tex` | Removed non-associativity claim; replaced Bianchi section with Theorem `thm:bianchi_biquaternion` (explicit proof) |
| `canonical/geometry/biquaternion_tetrad.tex` | Removed non-associativity claim |
| `THEORY/architecture/geometry/biquaternion_connection.tex` | Synced with canonical |
| `THEORY/architecture/geometry/biquaternion_curvature.tex` | Synced with canonical |
| `THEORY/architecture/geometry/biquaternion_tetrad.tex` | Synced with canonical |
| `consolidation_project/appendix_R_GR_equivalence.tex` | Replaced "can be shown" with Lemma `lem:re_omega_levi_civita`; added assumptions A1–A3 |
| `docs/ubt_gr_recovery/gr_recovery_status.md` | This file (new) |
