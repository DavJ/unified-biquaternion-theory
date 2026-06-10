<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T1_GR — Proof Gap List

**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Enumerate every open gap in the GR recovery chain with precise scope,
obstruction, and what a proof would require.  
**Date**: 2026-04-27  
**Sources**: `canonical/gr_closure/`, `research_tracks/research/gr_offshell_gap.md`,
`canonical/geometry/gr_completion_attempt.tex`

---

## Summary

| Gap ID | Short name | Status | Blocks paper? |
|--------|------------|--------|---------------|
| GAP-10 | Off-shell Θ-only closure | OPEN [L2] | **No** — on-shell result sufficient |
| GAP-Z  | Zerilli equation (even-parity) | **PROVED [L1]** — `canonical/gr_closure/zerilli_derivation.tex` | N/A — closed |
| GAP-M  | Compact M⁴ off-shell | OPEN [L2] | No |
| GAP-Q  | Quantum GR (path integral) | OPEN [L3] | No — classical paper only |
| GAP-C  | Cosmological solutions (de Sitter, FRW) | OPEN [L2] | No — but desirable |

**Assessment**: The GR paper can be submitted with all remaining gaps explicitly stated.
Steps 1–5, Schwarzschild, ASD/twistor, Regge-Wheeler, and Zerilli are all proved [L1].

---

## GAP-10: Off-Shell Θ-Only Closure

**Canonical name**: GAP-10  
**Canonical source**: `research_tracks/research/gr_offshell_gap.md`,
`canonical/gr_closure/step2_theta_only_closure.tex`  
**Status**: OPEN [L2]

### What has been proved (on-shell)

For `Θ ∈ A_UBT` (admissible class: linearly independent derivatives, non-constant):
- The induced variation map `J = δg^μν/δΘ` is non-degenerate **on-shell**.
- Consequently, `δŜ[Θ]/δΘ = 0` is equivalent to Einstein equations on `g = g[Θ]`.
- This is the "Level 2 recovery" labelled in `DERIVATION_INDEX.md`.

### What is missing (off-shell)

The claim that the same non-degeneracy holds for **all** Θ in the full off-shell
field space — i.e., including configurations where `∂_μΘ = 0` along a codimension-1
surface.

### Precise missing lemma

> **Lemma (GAP-10)**: The kernel of `J = δg^μν/δΘ : T_Θ(Field) → Γ(Sym²T*M)`
> consists only of gauge directions (pure phase rotation or diffeomorphism) for
> all Θ in the full off-shell field space, not only for on-shell Θ ∈ A_UBT.

### Known obstructions

1. **Rank mismatch**: `Re(∇†∇Θ)` is a scalar (rank-0); `G_μν` is rank-2.
   The multi-step chain `Θ → ∂_μΘ → G_μν → g_μν` is needed; each step must
   remain non-degenerate off-shell.

2. **Topology**: Global injectivity of `Θ → g[Θ]` requires Θ to be a global
   section of a principal bundle with structure group from the ℂ⊗ℍ automorphism
   group.  Whether global sections exist depends on the topology of M⁴
   (specifically `H²(M⁴,ℤ)`) and is generally a hard problem in global analysis.

3. **Non-perturbative existence**: A fixed-point theorem in an appropriate Banach
   or Sobolev space is required to assert well-posedness of `δŜ/δΘ = 0` as a
   PDE off-shell.

### Why this does not block the paper

The on-shell result (Steps 1–5 + Schwarzschild + Regge-Wheeler) is self-contained
and correct.  GAP-10 is a question about off-shell path integral completeness and
quantum theory — it does not affect the classical GR recovery.

### Approach that might close this gap

- Global analysis: compute the cohomology of the `ker J` sheaf over `M⁴`.
  If `H^1(M⁴, ker J) = 0`, then global non-degeneracy follows from the local result.
- Alternatively: prove that the set of degenerate `Θ` (where `det J = 0`) has
  measure zero in any reasonable function space, making it irrelevant for
  path-integral purposes.

---

## GAP-Z: Zerilli Equation (Even-Parity Graviton)

**Status**: **PROVED [L1]** (closed 2026-05-13)
**Canonical proof**: `canonical/gr_closure/zerilli_derivation.tex`

Both graviton polarisation sectors are now closed at [L1]:
- Odd-parity (Regge-Wheeler): proved in `papers/UBT_GR_Submission.tex` §5
- Even-parity (Zerilli): proved in `canonical/gr_closure/zerilli_derivation.tex`

This gap is no longer open.  See `WHAT_IS_PROVED.md §G15` and `STATUS.md §T1_GR` for the
canonical record.

---

## GAP-M: Compact M⁴ Off-Shell Closure

**Status**: OPEN [L2]

### Description

For compact spacetimes (e.g., $M^4 = T^4$ or $S^4$), the global topology
places additional constraints on sections of the Θ-bundle.  The off-shell
proof of GR recovery for compact M⁴ requires:
- Existence of global sections (may fail if the bundle is topologically
  non-trivial, e.g., winding number ≠ 0).
- A version of GAP-10 adapted to the compact case.

### Current status

The compact case is not addressed in the canonical files.  The non-compact
case (e.g., Minkowski spacetime, Schwarzschild exterior) is the main focus.

---

## GAP-Q: Quantum GR (Path Integral)

**Status**: OPEN [L3]

### Description

A path integral quantisation of UBT would require:
1. Off-shell closure (GAP-10).
2. A well-defined measure on the space of Θ fields.
3. Renormalisability or UV completion of the biquaternionic field theory.

This is well beyond the scope of the GR recovery paper and is listed here for
completeness only.

---

## GAP-C: Cosmological Solutions

**Status**: OPEN [L2], lower priority

### Description

FRW and de Sitter solutions have not been derived from a specific Θ ansatz in
the same style as the Schwarzschild derivation.  A cosmological Θ ansatz with
time-dependent scale factor would need:
1. An ansatz compatible with spatial homogeneity and isotropy.
2. Derivation of the Friedmann equations from the UBT action.

The Friedmann equations should follow from Steps 1–5 by applying them to an
FRW metric, but the explicit biquaternionic construction is missing.

---

## Priority Order for Future Work

| Priority | Gap | Reason |
|----------|-----|--------|
| 1 | GAP-C (cosmological) | High scientific interest; FRW is standard |
| 2 | GAP-M (compact) | Needed for mathematical completeness |
| 3 | GAP-10 (off-shell) | Fundamental but hard; topology-dependent |
| 4 | GAP-Q (quantum) | Very long-term |

*GAP-Z (Zerilli) was Priority 1 and is now **PROVED [L1]** — removed from this list.*
