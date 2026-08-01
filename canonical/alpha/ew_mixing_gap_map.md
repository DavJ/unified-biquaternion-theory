<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->


# ew_mixing_gap_map.md — Electroweak Mixing Gap Map

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Weinberg-Angle Program  
**Purpose**: Exact map of every gap between current UBT and a first-principles
derivation of sin²θ_W = g'²/(g²+g'²) ≈ 0.231.  Every claim linked to a source.  
**Companion**: `canonical/alpha/weinberg_angle_routes.md`,
`reports/ew_mixing_status.md`, `report/polyhedral_weinberg_scan.md`

---

## Current Position: What Is Proved

| Claim | Status | Source |
|-------|--------|--------|
| SU(2)_L from left-unitary action on ℂ⊗ℍ ≅ Mat(2,ℂ) | [L0] PROVED | `canonical/interactions/sm_gauge.tex §SU2` |
| U(1)_Y from right scalar phase action on Mat(2,ℂ) | [L0] PROVED | `canonical/interactions/sm_gauge.tex §U1` |
| Photon field A_μ = sin θ_W W³_μ + cos θ_W B_μ | [L1] PROVED | Standard EW algebra |
| e = g sin θ_W = g' cos θ_W | [L1] PROVED | `canonical/alpha/gauge_normalization_attempt.tex §3` |
| α = g² sin²θ_W / (4π) | [L1] PROVED | Follows from above |
| Generator norms in fundamental: Tr(T₃²) = Tr(Y²) = 1/2 | [L0] PROVED | EW1 computation |
| N_eff = 12 from ℂ⊗ℍ mode counting | [L0] PROVED | `canonical/n_eff/` |
| B₀ = 8π one-loop coefficient | [L1] PROVED | `canonical/n_eff/step2_vacuum_polarization.tex` |

**Established near-miss (EXCLUDED)**:

The algebraically simplest result — equal coupling constants g = g' from the
natural kinetic term normalization — gives sin²θ_W = 1/2, which is excluded by
experiment. This confirms that the UBT algebra gives a non-trivial structure
for the EW sector, but the specific value 0.231 requires additional input.

---

## Gap Map: Ordered by Criticality

### GAP EW-1 — Derive tan θ_W = g'/g from UBT algebra

**Status**: OPEN CRITICAL  
**Description**: The ratio of coupling constants g'/g is a free parameter in
the current UBT formulation. Neither the kinetic term Tr[(D_μΘ)†(D^μΘ)] nor
the gauge structure fixes this ratio without additional input.

**Obstruction**: SU(2)_L and U(1)_Y act on different sectors of ℂ⊗ℍ. SU(2)_L
acts via left-unitary transformations; U(1)_Y via right phase rotations. These
two actions are orthogonal in the algebra (they commute), so the Killing form on
su(2)_L ⊕ u(1)_Y has no mixed term — the relative normalization of the two
sectors is a free parameter.

**What would close this gap**:
1. A principle that fixes the relative normalization of the SU(2)_L and U(1)_Y
   kinetic terms in S[Θ] — i.e., a derivation of the "GUT normalization" of Y.
2. OR: An embedding of SU(2)_L × U(1)_Y in a larger (possibly non-continuous)
   structure that determines g'/g.

**Research routes** (from `canonical/alpha/weinberg_angle_routes.md`):
- UBT algebra normalization route (Gap EW-1a)
- Geometric projection route — A5 (5−√5)/10 result (not yet anchored)
- GUT boundary condition route via McKay-ADE
- RG running from a GUT boundary

---

### GAP EW-2 — Derive Θ₀ as SU(2)_L doublet with Y = 1/2

**Status**: OPEN HIGH  
**Description**: For electroweak symmetry breaking in UBT to proceed via the
standard Higgs mechanism, the UBT Θ-field (or its vacuum expectation value Θ₀)
must transform as an SU(2)_L doublet with hypercharge Y = 1/2. This
identification has been assumed but not derived from S[Θ].

**Obstruction**: The UBT field Θ takes values in ℂ⊗ℍ ≅ Mat(2,ℂ). Under
SU(2)_L × SU(2)_R (the full unitary group of Mat(2,ℂ)), Θ transforms as (2,2̄).
The restriction to SU(2)_L doublet (2,1) requires a symmetry-breaking argument.

**What would close this gap**: Show that the UBT action S[Θ] has an asymmetric
vacuum that selects the doublet structure. This connects to Gap C1 (chirality).

---

### GAP EW-3 — Fix the U(1)_Y normalization convention independently

**Status**: OPEN MEDIUM  
**Description**: The standard convention is Tr(Y²)_fund = 1/2 (same as
Tr(T₃²)_fund). This is a convention choice in the SM, arising from the SU(5)
embedding. In UBT, this convention is not yet derived from a physical principle.

**What would close this gap**: Show that the UBT kinetic term enforces the
same normalization for the U(1)_Y and SU(2)_L generators. Equivalently:
show that Y and T₃ have the same Dynkin index in the fundamental representation
of some UBT-derived GUT group.

---

### GAP EW-4 — Identify the U(1)_Y generator within ℂ⊗ℍ

**Status**: PARTIALLY DONE — needs formalization  
**Description**: The U(1)_Y generator Y has been identified as the right scalar
phase action on Mat(2,ℂ). However, the hypercharge quantum numbers of specific
fermion representations (Y = 1/6 for quarks, etc.) have not been derived.

**What would close this gap**: A complete classification of UBT matter irreps
under SU(3) × SU(2) × U(1)_Y with all hypercharge quantum numbers derived
from the ψ-winding representation theory.

---

## Summary: What Blocks sin²θ_W Derivation

```
sin²θ_W is blocked primarily by GAP EW-1 (coupling ratio free).
GAP EW-2 is needed for the SSB mechanism.
GAP EW-3 is needed for the normalization.
GAP EW-4 is needed for the full fermion spectrum.
```

The chain of dependencies:

```
GAP EW-4 (fermion Y quantum numbers)
    ↓
GAP EW-3 (Y normalization)
    ↓
GAP EW-2 (SSB doublet structure)
    ↓
GAP EW-1 (coupling ratio g'/g)
    ↓
sin²θ_W = g'²/(g²+g'²)  DERIVED
    ↓
α = g² sin²θ_W / (4π)   DERIVED
```

---

## Research Routes with Current Status

| Route | Current state | What's needed | Est. difficulty |
|-------|--------------|---------------|-----------------|
| A. Algebra normalization (canonical ℂ⊗ℍ) | Equal norms → sin²θ_W = 1/2 (excluded) | New principle to break norm symmetry | HIGH |
| B. Geometric projection (A5 icosahedral) | (5−√5)/10 ≈ 0.276 (suggestive) | Physical axis identification | MEDIUM (if A5 acts on EW sector) |
| C. GUT boundary (McKay → E₆ → SU(5)) | sin²θ_W(GUT) = 3/8 (reproduced) | This is SU(5) physics, not UBT-specific | N/A |
| D. RG running | Standard result 0.231 at M_Z | Need A, B, or C first | Depends |
| E. ψ-winding representation theory | Y from ψ-winding: partial | Full fermion Y assignments | HARD |

---

## Immediate Next Steps

Priority order for closing EW-1:

1. **Check if the UBT kinetic term Tr[(D_μΘ)†(D^μΘ)] has a broken U(1) × U(1)
   normalisation**: compute the relative coefficient of the SU(2)_L and U(1)_Y
   kinetic terms from the canonical covariant derivative in ℂ⊗ℍ.

2. **Investigate whether A5 ⊂ Aut(ℂ⊗ℍ) acts on the EW mixing sector**: if A5
   is a symmetry of the UBT action, the icosahedral axis angles could provide
   the T₃ and Y identification needed for the (5−√5)/10 prediction.

3. **Compute sin²θ_W from E₆/E₇/E₈ via the full breaking chain**: go beyond
   the SU(5) subalgebra and use the full ADE algebra data to constrain
   alternatives to sin²θ_W = 3/8.

---

## Cross-References

- `canonical/alpha/weinberg_angle_routes.md` — route survey
- `report/polyhedral_weinberg_scan.md` — Platonic solid route scan (new)
- `reports/ew_mixing_status.md` — high-level status
- `canonical/interactions/sm_gauge.tex` — proved SM gauge structure  
- `canonical/alpha/gauge_normalization_attempt.tex` — EW-1 working doc
- `canonical/symmetry/effective_vs_fundamental_breaking.tex` — SSB structure
