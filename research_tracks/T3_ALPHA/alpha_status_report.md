<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T3_ALPHA — Fine Structure Constant: Status Report

**Track**: T3_ALPHA — Fine Structure Constant or Layer2 Fallback  
**Objective**: Attempt α derivation without fitting; if blocked, redirect to Layer2 coding paper  
**Date**: 2026-04-27  
**Sources**: `canonical/appendices/appendix_alpha_geometry.tex`,
`research_tracks/research/theta_alpha_connection.md`,
`PRIORITIES_2026.md`, `DERIVATION_INDEX.md`

---

## Executive Summary

| Item | Status |
|------|--------|
| α⁻¹ bare value = 137 from V_eff minimum | PROVED [L1] given B_base |
| B₀ = 8π (one-loop baseline) | PROVED [L1] |
| N_eff = 12 from ℂ⊗ℍ modes | PROVED [L0] |
| B_base = N_eff^{3/2} = 41.57 | PARTIAL [L1] — k=1 (Kac-Moody) open |
| Correction δ = α⁻¹ − 137 ≈ 0.036 | SEMI-EMPIRICAL |
| R_ψ in physical units from S[Θ] | OPEN HARD PROBLEM |
| Fully closed first-principles derivation | **NOT ACHIEVED** |

**Assessment**: The α derivation is blocked by the B_base gap.  27+ approaches
have been exhausted.  A genuinely new algebraic route is needed.  If this is not
found, the Layer2 coding paper (see `fallback_layer2_outline.md`) is the
recommended pivot.

---

## What Has Been Proved

### N_eff = 12 [L0]

The effective number of charged modes contributing to one-loop vacuum polarisation:
```
N_eff = N_phases × N_helicity × N_charge = 3 × 2 × 2 = 12
```
where `N_phases = dim_ℝ(Im ℍ) = 3`.

This is a zero-free-parameter result from the `ℂ⊗ℍ` structure.  
**Source**: `canonical/n_eff/`, `canonical/appendices/appendix_alpha_geometry.tex §2`

### B₀ = 8π [L1]

The one-loop coefficient:
```
B₀ = 2π N_eff / 3 = 2π × 12 / 3 = 8π ≈ 25.133
```
Derived from the one-loop vacuum polarisation of `N_eff = 12` charged modes.  
**Source**: `canonical/n_eff/step2_vacuum_polarization.tex`

### Prime attractor n* = 137 [L1] (given B_base)

The effective potential:
```
V_eff(n) = n² − B ln n + const
```
has minimum at:
```
n* = √(B/2)
```
If `B = B_base · R²` with `B_base = 41.57` and `R = 1.114`, then `n* ≈ 137`.

The identification `α⁻¹_bare = n*` and the prime-stability of 137 are proved
given B_base.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §4`

### Toroidal compactification and Dirac quantisation [L0]

The ψ-circle compactification and Dirac quantisation condition:
```
e^{iq ∮_ψ A_ψ dψ} = 1
```
are proved.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §1`

---

## The Central Blocking Gap: B_base

### What is needed

Derive `B_base = N_eff^{3/2} = 41.57` from the UBT field equations — specifically,
fix the Kac-Moody level `k = 1` (Gap G3-k) without circular reference to `n*`.

The formula `B_base = N_eff^{3/2}` requires the exponent `3/2` to emerge from
the field theory.  The `3/2` is interpreted as a Kac-Moody level `k = 1` combined
with the `N_eff = 12` mode count via conformal field theory (CFT) methods.

### Why this is hard

- 27+ algebraic approaches have been exhausted.
- The most successful result is `k = 1` as a motivated conjecture from
  Chern-Simons term absence (H2 approach).
- The two-loop correction factor `R ≈ 1.114` (`ΔB = 3π/2` candidate)
  is a motivated conjecture only.

**Key obstruction**: The derivation of `B_base` requires knowing the partition
function of the UBT field theory on the torus.  This requires either:
1. A rigorous CFT treatment of the biquaternion field theory on `T² × S¹_ψ`.
2. A heat-kernel or ζ-function regularisation calculation of the one-loop
   determinant of `∇†∇` on the torus.
3. A string theory analogy where `k = 1` follows from the level-matching
   condition.

None of these has been completed.

### Inventory of tested approaches

| Approach | Method | Result | Status |
|----------|--------|--------|--------|
| H1 | Direct N_eff counting with anomaly | B₀ = 8π | Proved [L1] |
| H2 | CS-term absence → k=1 | k=1 motivated | Conjectured [MC] |
| H3 | Modular bootstrap ϑ₃³(τ) | k = 3/2 modular weight | Computed [L0], disconnected |
| H4 | j(τ) = 1728 = 12³ coincidence | Numerical coincidence | Noted [O] |
| H5 | Spectral gap q-suppression | R_ψ-dependent | [SE] |
| H6 | RG attractor τ* = i/137 | Modular interpretation | [MC] |
| H7–H27 | Variants of above | No new closure | Documented in DERIVATION_INDEX.md |

### One new route not yet tried: Modular bootstrap

**Proposed approach**:
1. Compute the partition function `Ẑ(τ) = ϑ₃³(τ)` on the UBT torus.
2. Use modular bootstrap (crossing symmetry constraint) to fix `k` from
   consistency conditions.
3. If `k = 1` follows from crossing symmetry, B_base is proved.

**Status**: NOT YET ATTEMPTED  
**Difficulty**: Hard — requires detailed CFT computation  
**Recommendation**: This is the single new route recommended in `PRIORITIES_2026.md §4`.

---

## Correction Term δ = 0.036

The observed `α⁻¹ = 137.036` exceeds the bare value by `δ ≈ 0.036`.

**Identification**: Two-loop QED vacuum polarisation on the ψ-circle:
```
α⁻¹(m_e) = α⁻¹_bare + (1/3π) ln(Λ/m_e) + O(α)
```
with `Λ ≈ m_e/√α` giving `δ = 0.036`.

**Status**: SEMI-EMPIRICAL — uses `α` and `m_e` as input.  
The additive conjecture `ΔB = 3π/2 ≈ 4.712` (from heat-kernel modular weight
`k = 3/2` and SSB half-period `θ_W^min = π`) has Motivated Conjecture status.

---

## R_ψ: The Hard Parameter

The physical radius `R_ψ` of the imaginary time circle enters the derivation:
- `E_{k,n} = |k|²/R_t² + n²/R_ψ²` (KK spectrum)
- T-duality fixed point: `R_ψ = R_t = ℏ/(m_e c)` (self-dual, calibrated)
- This calibration uses `m_e` as external input.

**Status**: OPEN HARD PROBLEM  
**Source**: `canonical/geometry/Rpsi_dynamical_fix.tex`

---

## Current Bottom Line

```
α = e²/(4πε₀ℏc) ≈ 1/137.036

Derived in UBT:
  - α⁻¹_bare = 137  [L1] given B_base
  - B₀ = 8π        [L1]
  - N_eff = 12      [L0]

Not derived:
  - B_base exponent (k = 1)  [MC only]
  - δ = 0.036                [SE]
  - R_ψ in physical units    [OPEN HARD]

Status: INCOMPLETE — cannot claim first-principles derivation of α
```

---

## Recommendation

Given the exhaustion of 27+ approaches on B_base:

1. **Attempt the modular bootstrap approach** (one new route).
   Time-box this to 4 weeks.  If no progress, stop.

2. **If blocked**, redirect effort to the Layer2 coding paper
   (see `fallback_layer2_outline.md`).  The Layer2 paper is:
   - Publishable now
   - Does not depend on B_base
   - High visibility in information theory / physics coding community

3. **Do not** continue exhausting variants of approaches H2–H27.
   They have been documented; repeating them wastes resources.

4. **Record** the B_base gap as an open hard problem in both the SM paper
   and the GR paper, establishing intellectual honesty without blocking
   those submissions.
