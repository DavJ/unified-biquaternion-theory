<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# ALPHA_FINAL_OFFENSIVE.md — Launch: No-Fit Structural Derivation of α

> **LEGACY / SUPERSEDED BANNER (2026-05-10)**  
> This root-level planning file is historical and superseded.  
> Canonical alpha truth is only `canonical/alpha/ALPHA_MASTER_STATUS.md`.  
> Current verdict: alpha is **NOT derived**; `alpha_bare^{-1}=137` is **CONDITIONAL ONLY**;  
> physical `alpha^{-1}=137.036` is **NOT derived**; **Gap G137-B remains open**.

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Final offensive pass  
**Priority**: CRITICAL  
**Purpose**: Execute the Alpha Final Offensive — a disciplined, last-pass attempt to
derive the fine-structure constant α from UBT structure alone, with zero parameters
fitted to match α.

> **Historical status (2026-05-10)**: This document is retained as historical
> planning context and is superseded for active alpha claims by
> `canonical/alpha/ALPHA_MASTER_STATUS.md`.

---

## Hard Rules (Non-Negotiable)

| Rule | Statement |
|------|-----------|
| R1 | No numerical constant may be chosen to reproduce α |
| R2 | Every constant must originate from an independent UBT sector |
| R3 | Every route must be classified: **viable** / **blocked** / **numerology** / **incomplete** |
| R4 | All inputs classified as CLEAN, SE (semi-empirical), CIRC (circular), or MC (motivated conjecture) |
| R5 | Routes involving any CIRC input cannot claim a first-principles derivation |

---

## Pre-Existing Foundation (Zero-Parameter Proved Results)

These results carry into this offensive as established [L0]/[L1] facts:

| Result | Formula | Classification | Source |
|--------|---------|----------------|--------|
| Fundamental algebra | ℂ⊗ℍ axiom | CLEAN [L0] | `canonical/fields/biquaternion_algebra.tex` |
| Complex time compactification | τ = t+iψ, S¹_ψ | CLEAN [L0] | `canonical/fields/biquaternion_time.tex` |
| N_eff = 12 modes | 3 × 2 × 2 from dim_ℝ(Im ℍ) | CLEAN [L0] | `canonical/n_eff/step3_N_eff_result.tex` |
| One-loop baseline | B₀ = 2πN_eff/3 = 8π | CLEAN [L1] | `canonical/n_eff/step2_vacuum_polarization.tex` |
| Effective potential form | V_eff(n) = n² − B·n·ln n | CLEAN [L1] given B | `canonical/alpha/veff_corrected.tex` |
| Stationarity condition | 2n* = B(ln n* + 1) | CLEAN [L1] given B | `canonical/alpha/veff_corrected_statement.tex` |
| Prime stability of n* = 137 | Homotopy argument | CLEAN [L1] | `canonical/appendices/appendix_alpha_geometry.tex §4` |
| Dirac charge quantisation | e^{iq∮A_ψdψ} = 1 | CLEAN [L0] | `canonical/appendices/appendix_alpha_geometry.tex §1` |

**Central unresolved gap carried forward**: B_base = N_eff^{3/2} requires
proving Kac-Moody level k = 1 (Gap G3-k).  This is the common root of
all blocking gaps in all five tracks below.

---

## Track A1 — GaugeNormalization

**Question**: Can the canonical normalization of the U(1) A-field in the UBT
kinetic term `Tr[(D_μΘ)†(D^μΘ)]` fix the electric charge e, and hence α, without
additional parameters?

**Canonical file**: `canonical/alpha/gauge_normalization_attempt.tex`

### Chain of Steps

| Step | Formula | Status |
|------|---------|--------|
| Covariant derivative | D_μ = ∂_μ + ig_s G^a_μ T^a + igW^i_μτ^i + ig'B_μY | CLEAN [L0] |
| Photon field after SSB | A_μ = sinθ_W W³_μ + cosθ_W B_μ | CLEAN (algebra) |
| Electric charge relation | e = g sinθ_W = g' cosθ_W | CLEAN (algebra) |
| Fine-structure constant | α = e²/(4π) = g² sin²θ_W / (4π) | CLEAN given g, θ_W |
| Fix g from ℂ⊗ℍ | — | **GAP EW-1a** — OPEN |
| Fix θ_W = arctan(g'/g) from Aut(ℂ⊗ℍ) | — | **GAP EW-1b** — OPEN |

### Gap EW-1 Analysis

The ratio g'/g is not constrained by the UBT algebra as currently formulated.
By Schur's lemma, the U(1)_Y generator Y commutes with all su(2)_L generators
and is proportional to the identity on each SU(2)_L representation.  This means
Y's overall normalisation is a free parameter relative to the SU(2)_L generators.

**Possible resolution**: If UBT embeds SU(3)_c × SU(2)_L × U(1)_Y into a larger
simple group G_GUT as a maximal subgroup, the Lie algebra structure fixes g'/g
at the GUT scale.  For SU(5): sin²θ_W(GUT) = 3/8 — an algebraic result with no
free parameter.

**Blocking assessment**:

- Without a GUT completion: **BLOCKED** (g'/g is free)
- With SU(5)-type GUT completion from ℂ⊗ℍ: **CONDITIONAL** on Gap GUT-UBT
  (whether ℂ⊗ℍ forces a specific GUT group)

### Classification: **CONDITIONAL**

Blocked by Gap EW-1.  Would be viable if ℂ⊗ℍ forces a GUT group that fixes
sin²θ_W at the unification scale.

---

## Track A2 — ElectroweakProjection

**Question**: Does the spontaneous symmetry breaking pattern SU(2)_L × U(1)_Y →
U(1)_EM in UBT fix the Weinberg angle θ_W from the biquaternion structure, giving
e = g sinθ_W without free parameters?

**Canonical file**: `canonical/alpha/symmetry_breaking_alpha_attempt.tex`

### Chain of Steps

| Step | Status |
|------|--------|
| SSB pattern SU(2)_L × U(1)_Y → U(1)_EM | Adopted from SM — not yet derived from S[Θ] |
| Unbroken generator Q = T₃ + Y/2 | CLEAN (algebra) |
| VEV structure Θ₀ as SU(2)_L doublet | **GAP EW-2** — OPEN |
| tan(θ_W) = g'/g from Aut(M_2(ℂ)) | **GAP EW-1** — OPEN (same as A1) |
| α from e = g sinθ_W | Conditional on EW-1 and EW-2 |

### GUT Completion Sub-Route (A2-GUT)

If the UBT algebra ℂ⊗ℍ embeds into SU(5) (or SO(10), E₆, E₈):

- SU(5) forces sin²θ_W(GUT) = 3/8 as a Lie algebra consequence (no free parameter)
- Running from Λ_GUT to m_Z using SM β-functions gives sin²θ_W(m_Z) ≈ 0.231
- This then yields α(m_Z) ≈ 1/128 and α(0) ≈ 1/137.036 via RGE

**Remaining gaps**:
1. **Gap GUT-UBT**: Does ℂ⊗ℍ force a specific GUT group?  
   dim_ℝ(ℂ⊗ℍ) = 8; dim(SU(5)) = 24.  No natural embedding is known.
2. **Gap GUT-scale**: Even with a GUT group, the GUT scale Λ_GUT is a free parameter
   unless fixed algebraically by UBT.
3. **Gap EW-2**: VEV doublet structure must come from S[Θ], not from SM analogy.

### Key Exclusion

The naive condition g = g' at the electroweak scale gives sin²θ_W = 1/2,
hence α ≈ g²/(8π) ≈ 1/97.  This is **excluded** by experiment
(sin²θ_W ≈ 0.231 at m_Z).  This route is a dead end.

### Classification: **CONDITIONAL**

Blocked by Gaps EW-1, EW-2, and GUT-UBT.  The GUT completion sub-route
is a viable research direction if ℂ⊗ℍ can be embedded into a simple GUT group.

---

## Track A3 — ModularTheta

**Question**: Do the modular properties of complex time τ = t + iψ, treated as a
modular parameter, uniquely determine the electromagnetic coupling α via modular
invariants, Hecke eigenvalues, or the partition function Ẑ(τ) = ϑ₃³(τ)?

**Companion documents**: `research_tracks/T3_ALPHA/alpha_status_report.md §3.4`

### Modular Structure of UBT

The complex time τ transforms under SL(2,ℤ): τ → (aτ+b)/(cτ+d).  The UBT
partition function on the torus is:
```
Ẑ(τ) = ϑ₃³(τ)
```
where ϑ₃(τ) is the Jacobi theta function.  Under S: τ → −1/τ:
```
ϑ₃(−1/τ) = (−iτ)^{1/2} ϑ₃(τ)
```
so Ẑ(τ) has modular weight 3/2 (confirmed, Gap G8 closed in ALPHA_PROGRESS_REPORT.md).

### Systematic Modular Search Results

| Expression | Value | Equals α⁻¹ = 137.036? | Assessment |
|------------|-------|------------------------|------------|
| j(i) / 1000 | 1.728 | No | Unrelated |
| e^π (Gelfond) | 23.140 | No | Unrelated |
| 16π³ | 4961 | No | Unrelated |
| τ(137) Ramanujan | −182213199 | No | Large integer |
| V_eff minimum n* | 137 (bare integer) | Yes (bare) | Already proved [L1]; not new |
| Modular bootstrap k_KM | Unknown | Unknown | NOT YET ATTEMPTED |

### Modular Bootstrap (Untested Route)

The modular weight 3/2 of Ẑ(τ) = ϑ₃³(τ) does NOT directly give the Kac-Moody
level k = 1.  These are different quantities.  The bootstrap question is:

> Does imposing crossing symmetry on the 4-point function of the biquaternion
> field theory on T² force k_KM = 1 as a consistency condition?

If yes: k = 1 is proved, B_base closes, α⁻¹_bare = 137 is a zero-parameter result.  
If no: the modular route cannot fix k, and this track is exhausted.

**Strategic recommendation**: Time-box to 4 weeks from 2026-04-28.
See `ALPHA_PROGRESS_REPORT.md §3.4` for detailed plan.

### Classification: **INCOMPLETE**

The modular bootstrap sub-route is the one genuinely untested approach.  All
other modular methods have been exhausted (27+ approaches documented in
`DERIVATION_INDEX.md`).  The integer n* = 137 from the prime attractor is
already proved — this route does not need to re-derive it.

---

## Track A4 — RGFlow

**Question**: Does UBT predict the value of α at some UV scale (e.g., the Planck
scale, the GUT scale, or the T-duality scale R_ψ), from which α(0) ≈ 1/137.036
can be obtained by running down to IR using the SM RGE?

### RG Structure of α in UBT

The QED β-function gives:
```
α⁻¹(μ) = α⁻¹(μ₀) − (1/3π) ln(μ/μ₀) + O(α)
```
For a prediction of α(0) from α(μ_UV):
1. One needs α(μ_UV) predicted by UBT structure alone (not by fitting).
2. One needs μ_UV identified with an algebraic UBT scale (not a free parameter).
3. One needs the SM running as a bridge — an external input.

### Assessment of Each Sub-Requirement

**Sub-requirement 1: Predict α(μ_UV) from UBT**

The only UV prediction currently in UBT is the prime-attractor result
α⁻¹_bare = 137, which is a bare (UV) value from the winding mode n* on S¹_ψ.
This is already the best-case starting point for the RG flow.

If α⁻¹_UV = 137 (bare), then running to IR using QED β-function:
```
α⁻¹(0) = 137 + (1/3π) ln(Λ/m_e)
```
This gives α⁻¹(0) ≈ 137.036 only with Λ ≈ m_e · e^{3π × 0.036} ≈ 1.36 m_e.
However, identifying Λ = 1.36 m_e requires m_e as input — circular.

**Sub-requirement 2: Fix the UV scale algebraically**

The T-duality self-dual point gives R_ψ = 1/√2 (in string units).  In physical
units, R_ψ = ℏ/(m_e c) — but this calibration uses m_e.  No algebraic fixation
of R_ψ in physical units is known without m_e input.

**Sub-requirement 3: SM running as input**

Using SM (or QED) β-functions to run α from UV to IR introduces external inputs
(the SM matter content, scale thresholds, m_e, m_Z).  This is not a UBT-internal
prediction.

### GUT-Scale Completion Sub-Route (A4-GUT)

If the A2 GUT completion succeeds (Gap GUT-UBT resolved), the following chain
becomes viable:
```
ℂ⊗ℍ  →  G_GUT forced  →  sin²θ_W(GUT) = 3/8  →  α_GUT free
         [algebraic]         [algebraic]          [STILL FREE]
```
The GUT-scale value of α is not fixed by the Lie algebra structure alone; it is
the value of the unified coupling at the GUT scale, which is an independent free
parameter.  Running it down to m_Z would give α(m_Z), but α_GUT is unknown without
an additional UBT prediction.

**Summary**: The RG route does not add independent predictive power beyond what
A2 already provides.  It converts a UV-scale α prediction into a scale-evolved
prediction, but both the UV prediction and the running scale must be provided
from other sources.

### Classification: **BLOCKED**

The RG flow route cannot deliver α(0) without either:
(a) α at some UV scale already predicted by UBT (requires A1 or A2 to succeed first), or
(b) The UV scale itself fixed algebraically from UBT (R_ψ requires m_e — circular).

The RG route is a **relay leg**, not a starting point.  Its value is to check
whether a UV prediction from A1/A2 is consistent with the observed low-energy α,
once those tracks succeed.

---

## Track A5 — CodingSecondary

**Question**: Do the Layer2 coding structures (Hamming (8,4,4), Gray transport,
1⊕3⊕3̄⊕1 decomposition) constrain charge quantisation, and can they additionally
fix the magnitude of e (thereby fixing α)?

**Script**: `research_tracks/alpha/layer2_coding_alpha_scan.py`

### What the Coding Layer Establishes

| Result | Status |
|--------|--------|
| ℂ⊗ℍ ≅ M_2(ℂ) — 8-dimensional over ℝ | CLEAN [L0] |
| ℤ₂×ℤ₂×ℤ₂ involutions encode SU(3) | CLEAN [L0] |
| Gray code structure of involutions | CLEAN [L0] |
| 1⊕3⊕3̄⊕1 decomposition under SU(2) | CLEAN [L0] |
| 8 real dimensions match Hamming block length | Structural observation [O] |
| Hamming (8,4,4) enforces charge quantisation (integer multiples) | PLAUSIBLE [MC] |
| Gray code constrains U(1) phase step ordering | HYPOTHESIS [MC] |
| Coding layer fixes magnitude of charge e | **FAILED** |

### Critical Structural Observation

The 1⊕3⊕3̄⊕1 decomposition under SU(2) contains no j=1/2 doublet irrep.  This
means the SM Higgs mechanism cannot be directly implemented on the biquaternion
field in its fundamental representation.  A new input is required for the SSB doublet
(same as Gap EW-2 in A2).

### Scope Boundary

The Layer2 coding structures fix:
- **Which charges are allowed**: integer or half-integer multiples of a unit charge,
  determined by the Hamming parity constraints on the 8-dimensional real space
- **Which phase transitions are preferred**: Gray-adjacent steps in the ψ-direction

The Layer2 coding structures do NOT fix:
- **The magnitude of the unit charge e**: this depends on the dynamics of S[Θ],
  not on the discrete code structure
- **The value of α = e²/(4π)**: requires knowing e in physical units, which depends
  on the UV cutoff and renormalization scheme

### Positive Scope for Layer2

While Layer2 does not deliver α, it is the foundation of an independent publishable
result: the Gray code structure of SU(3) from ℂ⊗ℍ.  See
`research_tracks/T3_ALPHA/fallback_layer2_outline.md` for the full outline.
This paper is publication-ready in ≈6 weeks and does not depend on B_base.

### Classification: **INCOMPLETE**

Layer2 constrains charge quantisation (spectrum of allowed charges), but cannot
determine the coupling magnitude.  This is the correct and definitive scope of
the coding layer.  Not a failure — a boundary identification.

---

## Gap Inventory

| Gap ID | Description | Blocks Track(s) | Priority |
|--------|-------------|-----------------|----------|
| G3-k | Prove Kac-Moody level k = 1 from CFT/modular bootstrap | All viable routes | CRITICAL |
| EW-1 | Derive tan(θ_W) = g'/g from Aut(ℂ⊗ℍ) | A1, A2 | CRITICAL |
| EW-2 | Derive Θ₀ VEV as SU(2)_L doublet from S[Θ] | A2 | HIGH |
| GUT-UBT | Does ℂ⊗ℍ force a specific GUT group? | A2-GUT, A4-GUT | HIGH |
| A9 | Derive δ = 0.036 without α, m_e input | All full claims | HIGH |
| A10 | Derive R_ψ in physical units without m_e | A4 | HIGH |
| A12 | Derive ΔB = 3π/2 from S[Θ] without θ_W | Prime-attractor chain | MEDIUM |

---

## Strategic Assessment

### Convergence Structure

All routes with any chance of delivering α converge on a single algebraic question:

> **Can the UBT biquaternion algebra ℂ⊗ℍ fix one independent dimensionless
> coupling constant without external input?**

The prime-attractor route answers this for α⁻¹_bare = 137, conditional on k=1.  
The electroweak routes answer it for α(m_Z), conditional on Gaps EW-1 + EW-2.

These two answers are not independent: k=1 may follow from the same modular
bootstrap that also constrains the effective g'/g ratio in the torus CFT.

### Decision Gate

**+4 weeks from 2026-04-28 → 2026-05-26**

| Outcome | Action |
|---------|--------|
| Modular bootstrap yields k=1 | Draft "α⁻¹_bare = 137" minimal paper |
| EW-1 resolved from Aut(ℂ⊗ℍ) analysis | Draft full α derivation paper |
| Both blocked | Declare T3_ALPHA time-boxed; activate Layer2 paper |

**Regardless of gate outcome**: Activate Layer2 coding paper immediately.
It does not compete with the α attempt.

### Best Remaining Bet

**Track A3 modular bootstrap** for k=1:  
- One new route not yet attempted  
- Would simultaneously close B_base and possibly constrain EW structure  
- Hard but not impossible: 2D CFT crossing symmetry methods are mature  

**Track A2-GUT completion**:  
- Research whether ℂ⊗ℍ embeds into an exceptional group naturally  
- ℂ⊗ℍ is an 8-dimensional subalgebra; the octonions ℝ⊗ℍ⊗ℍ-related algebras connect to E₆, E₇, E₈  
- If an exceptional GUT emerges from UBT algebra, sin²θ_W is fixed

---

## References

| File | Content |
|------|---------|
| `ALPHA_PROGRESS_REPORT.md` | Full progress report including 27+ exhausted approaches |
| `reports/alpha_no_fit_audit.md` | No-fit audit of four active routes |
| `alpha_routes_scorecard.md` | Structured scorecard (this offensive) |
| `best_candidate_derivation.tex` | Best-candidate derivation (this offensive) |
| `canonical/alpha/gauge_normalization_attempt.tex` | Route A1 formal attempt |
| `canonical/alpha/symmetry_breaking_alpha_attempt.tex` | Route A2 formal attempt |
| `canonical/appendices/appendix_alpha_geometry.tex` | Prime-attractor L1 proof |
| `canonical/n_eff/` | N_eff = 12, B₀ = 8π proofs |
| `canonical/interactions/B_base_derivation_complete.tex` | B_base partial derivation |
| `research_tracks/T3_ALPHA/` | Full T3_ALPHA track documentation |
| `DERIVATION_INDEX.md` | Full approach inventory (27+ documented) |
