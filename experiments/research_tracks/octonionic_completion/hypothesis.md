<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Track B: Octonionic Completion Hypothesis

**Status:** Hypothesis — conditional, not yet proven necessary.

## Hypothesis Statement

> Physical consistency of UBT requires a non-associative completion ℂ⊗𝕆.
> Until the conditions below are proven, octonions remain an optional extension.

## Required Justification Conditions

The octonionic extension (embedding ℂ⊗ℍ into ℂ⊗𝕆) becomes **necessary** only if at least one
of the following conditions is established:

1. **Associative closure fails dynamically:** The dynamics of the Θ-field
   generate configurations that cannot be closed within the associative
   algebra ℂ⊗ℍ — i.e., consistent time evolution requires non-associative
   structure.

2. **Fermion representation mismatch in ℂ⊗ℍ:** The observed fermion content
   (three generations, colour triplets, weak doublets) cannot be embedded as
   representations of Aut(ℂ⊗ℍ) alone.

3. **Minimal extension gives G₂ symmetry uniquely:** Any minimal consistent
   extension of ℂ⊗ℍ that accommodates a colour-triplet sector necessarily
   produces G₂ = Aut(𝕆), with SU(3) ⊂ G₂ as the colour subgroup.

## Measurable Criteria for Necessity

| Condition | Status | Test |
|-----------|--------|------|
| Associative closure failure | Open | Construct explicit Θ trajectory; check closure |
| Fermion rep mismatch | Plausible | Classify irreps of Aut(ℂ⊗ℍ); compare to SM content |
| Minimal extension uniqueness | Open | Classify all rank-1 extensions of ℂ⊗ℍ |

## What Is Currently Established

- ℂ⊗𝕆 embedding **works**: SU(3) ⊂ G₂ = Aut(𝕆) is a clean mathematical fact.
- This gives a **sufficient** path to SU(3) in UBT.
- It is **not yet shown** that this path is **necessary**.

## Relationship to Track A

Track A (see `research_tracks/associative_su3/strategy.md`) investigates whether
SU(3) can arise without octonions. A negative result from Track A (SU(3) ⊄ Aut(ℂ⊗ℍ)
confirmed) would strengthen the case for Track B necessity but would not by itself
establish it (a different non-octonionic mechanism might still exist).

## Current Classification

Octonions in UBT are currently classified as:

- ✅ **Sufficient** for obtaining SU(3) via G₂ embedding
- ❓ **Necessary?** — open question (Conditions 1–3 above not yet proven)
- ❌ **Not inevitable** from ℂ⊗ℍ alone

## References

- `consolidation_project/appendix_E2_SM_geometry.tex` — Section "Emergence of SU(3)"
- `research_tracks/associative_su3/strategy.md` — Track A
- Baez & Huerta (2010), "The Algebra of Grand Unified Theories"
