<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Alpha Derivation — No-Fit Audit Report

**Author**: Ing. David Jaroš  
**Date**: 2026-04-27  
**Status**: Audit — research phase, not a proof  
**Canonical source**: `docs/STATUS_ALPHA.md`  
**Route survey**: `canonical/alpha/alpha_derivation_routes.md`

---

## Purpose

This report audits all active derivation routes for the fine-structure constant
α ≈ 1/137.036 against the acceptance criterion: **no parameter may be chosen
to match α**.  Every numerical input must come from another UBT sector.

The audit is structured as a reverse-burden-of-proof check: for each route,
we ask *what numerical value would α take if only UBT-internal inputs are used*,
and compare to the observed value.

---

## Audit Criteria

| ID | Criterion | Pass condition |
|----|-----------|----------------|
| C1 | No fitted constant | No number chosen to reproduce α |
| C2 | UBT-internal inputs only | All numbers from biquaternion algebra, prime attractor, or N_eff |
| C3 | Reproducible | Each claim can be verified by running the companion script |
| C4 | Status classified | Each route is labeled: proven / conditional / numerical coincidence / failed |
| C5 | Failure modes listed | Dead ends and near-misses explicitly recorded |

---

## Route A1: Gauge Normalization

**File**: `canonical/alpha/gauge_normalization_attempt.tex`

### Audit Checklist

| Check | Result |
|-------|--------|
| C1 — No fitted constant | ✅ PASS — no constant chosen to match α |
| C2 — UBT-internal inputs | ⚠️ PARTIAL — e = g sin(θ_W) is standard electroweak algebra; g and θ_W are not yet UBT-internal |
| C3 — Reproducible | ✅ PASS — the algebraic steps are verifiable |
| C4 — Status classified | ✅ PASS — labeled CONDITIONAL |
| C5 — Failure modes listed | ✅ PASS — Gap EW-1 (g'/g free) documented |

**Blocking gap**: Gap EW-1 — the ratio g'/g is not determined by the UBT biquaternion algebra.

**Classification**: **CONDITIONAL**

**What would change this**: A proof that the automorphism group Aut(ℂ⊗ℍ) constrains
the ratio of the SU(2)_L and U(1)_Y coupling normalizations.

---

## Route A2: Symmetry-Breaking Projection

**File**: `canonical/alpha/symmetry_breaking_alpha_attempt.tex`

### Audit Checklist

| Check | Result |
|-------|--------|
| C1 — No fitted constant | ✅ PASS — no constant chosen to match α |
| C2 — UBT-internal inputs | ⚠️ PARTIAL — the SSB pattern is adopted from SM, not derived from S[Θ] |
| C3 — Reproducible | ✅ PASS — the electroweak algebra is standard |
| C4 — Status classified | ✅ PASS — labeled CONDITIONAL |
| C5 — Failure modes listed | ✅ PASS — g = g' excluded; GUT route noted; Gap EW-2 documented |

**Key excluded near-miss**: The hypothesis g = g' at the electroweak scale gives
sin²θ_W = 1/2, hence α = g²/(8π).  This is **excluded** because sin²θ_W ≈ 0.231
experimentally.

**Blocking gaps**: Gap EW-1 (g'/g) and Gap EW-2 (VEV as doublet).

**Classification**: **CONDITIONAL**

**What would change this**: Either (a) a UBT derivation of the breaking pattern
and the Θ₀ doublet VEV, or (b) a UBT embedding into a grand-unified group that fixes
sin²θ_W(GUT) = 3/8 (algebraic prediction of SU(5) GUT, then running to electroweak scale).

---

## Route A3: Theta/Modular Route

### Audit Checklist

| Check | Result |
|-------|--------|
| C1 — No fitted constant | ✅ PASS — no fitting attempted |
| C2 — UBT-internal inputs | ✅ PASS — only modular-form values used |
| C3 — Reproducible | ✅ PASS — all modular values computable from τ |
| C4 — Status classified | ✅ PASS — labeled FAILED |
| C5 — Failure modes listed | ✅ PASS — systematic search shows no modular invariant = 137.036 |

**Search result summary**:

| Expression | Value | Match α⁻¹ = 137? |
|------------|-------|------------------|
| e^π | 23.14 | No |
| 16π³ | 4961 | No |
| j(i)/1000 | 1.728 | No |
| τ(137) (Ramanujan) | −182213199 | No |
| V_eff minimum n* = 137 | 137 (bare integer) | Yes (bare, integer) |

**Note on n* = 137**: The prime-attractor result from the existing L1 derivation
(appendix_alpha_geometry.tex) does produce α⁻¹_bare = 137 as a modular/toroidal
feature.  This is already proved at L1 and is NOT a new result from Route A3.
The full 137.036 remains open.

**Classification**: **NUMERICAL COINCIDENCE** (for the integer 137 as a torus feature)
/ **FAILED** (for producing 137.036 from modular invariants without the existing L1 result)

---

## Route A4: Layer 2 Coding Constraint

**Script**: `research_tracks/alpha/layer2_coding_alpha_scan.py`

### Audit Checklist

| Check | Result |
|-------|--------|
| C1 — No fitted constant | ✅ PASS — scan systematically tests all combinations |
| C2 — UBT-internal inputs | ✅ PASS — only Hamming/Gray/1⊕3⊕3̄⊕1 parameters used |
| C3 — Reproducible | ✅ PASS — run `python layer2_coding_alpha_scan.py` |
| C4 — Status classified | ✅ PASS — labeled FAILED |
| C5 — Failure modes listed | ✅ PASS — see script output section "near-miss candidates" |

**Near-miss candidates** (from scan script):
The scan tests all combinations of the form α = (C_code / N_gray^k)² / (4π) with
C_code ∈ {1, 4, 8} (Hamming parameters) and N_gray ∈ {2, 4, ..., 256}, k ∈ {1,2,3}.
Zero combinations produce α⁻¹ within 5% of 137.036 with UBT motivation.

**Critical finding**: The 1⊕3⊕3̄⊕1 decomposition under SU(2) contains **no j=1/2
doublet** irrep.  This means the SM Higgs mechanism cannot be directly implemented
with the biquaternion field in its fundamental representation — a new input is needed.

**Classification**: **FAILED** (coding does not determine coupling magnitude)

---

## Pre-Existing Results: What Is Already Proved

These results are not new to this audit; they are recorded for completeness.

| Result | File | Status |
|--------|------|--------|
| Bare α⁻¹ = 137 (prime attractor) | `canonical/appendices/appendix_alpha_geometry.tex` | **PROVED [L1]** |
| Dirac charge quantization | `docs/STATUS_ALPHA.md §2` | **PROVED [L0]** |
| N_eff = 12 from ℂ⊗ℍ | `canonical/n_eff/step3_N_eff_result.tex` | **PROVED [L1]** |
| B₀ = 8π (one-loop baseline) | `canonical/n_eff/step2_vacuum_polarization.tex` | **PROVED [L1]** |
| Two-loop QED correction | `experiments/alpha_core_repro/alpha_two_loop.py` | **PROVED [L1]** |

---

## Failure Inventory

### Failed routes (no path to α without fitting)

| Route | Failure reason |
|-------|---------------|
| A3 (modular) | No modular invariant produces 137.036; 137 is already from L1 result |
| A4 (coding) | Coding fixes charge spectrum structure, not coupling magnitude |

### Conditional routes (could work if gap resolved)

| Route | Blocking gap | Gap priority |
|-------|-------------|--------------|
| A1 (gauge normalization) | EW-1: g'/g from Aut(ℂ⊗ℍ) | CRITICAL |
| A2 (symmetry breaking) | EW-1 + EW-2: VEV structure | CRITICAL |

### Near-misses that were tested and rejected

| Expression | Value | Why rejected |
|-----------|-------|--------------|
| g = g' at EW scale | sin²θ_W = 1/2, α = g²/(8π) ≈ 1/97 | Contradicts experiment |
| Hamming coding alone | α = (1/4)²/(4π) ≈ 1/200 | No UBT motivation for e = 1/d_min |
| Gray 4-bit coding | α⁻¹ ≈ 3217 | N=16 gives wrong order of magnitude |
| B₀ = 8π → α⁻¹ = √(B₀/2) ≈ 3.5 | Far from 137 | B₀ is baseline, not full B |

---

## New Gaps Registered by This Audit

| Gap ID | Description | Priority | File |
|--------|-------------|----------|------|
| EW-1 | Derive tan(θ_W) = g'/g from Aut(ℂ⊗ℍ) representation theory | **CRITICAL** | `canonical/alpha/gauge_normalization_attempt.tex` |
| EW-2 | Derive Θ₀ VEV as an SU(2)_L doublet from S[Θ] | HIGH | `canonical/alpha/symmetry_breaking_alpha_attempt.tex` |
| L2-α | Clarify whether L2S/L2T constrain coupling magnitude or only spectrum | MEDIUM | `research_tracks/alpha/layer2_coding_alpha_scan.py` |
| GUT-UBT | Determine whether ℂ⊗ℍ embeds into a simple GUT group fixing sin²θ_W(GUT) | MEDIUM | `canonical/alpha/symmetry_breaking_alpha_attempt.tex §3.3` |

---

## Overall Assessment

| Route | Classification | Can deliver α without fitting? |
|-------|---------------|-------------------------------|
| A1 — Gauge normalization | CONDITIONAL | Yes, if Gap EW-1 resolved |
| A2 — Symmetry breaking | CONDITIONAL | Yes, if Gaps EW-1 + EW-2 resolved |
| A3 — Modular | NUMERICAL COINCIDENCE / FAILED | No (integer 137 already known) |
| A4 — Coding | FAILED | No (coding = spectrum, not magnitude) |

**Primary bottleneck**: All viable routes converge on Gap EW-1 — the ratio g'/g
must be derived from the UBT algebra to fix θ_W and hence α.

**Recommended next action**: Investigate whether the embedding of
SU(2)_L × U(1)_Y in Aut(ℂ⊗ℍ) ≅ Aut(M_2(ℂ)) forces a unique normalization
of the hypercharge generator relative to the isospin generators.

**Status of α derivation after this audit**: The integer bare value α⁻¹_bare = 137
remains the only zero-parameter UBT result (proved, L1).  The full value
α⁻¹ = 137.036 and any derivation via electroweak symmetry breaking remain
**conditional** on resolving Gap EW-1.

---

## References

- `docs/STATUS_ALPHA.md` — master α derivation status and gap inventory
- `canonical/THEORY/topic_indexes/alpha_index.md` — topic index
- `canonical/appendices/appendix_alpha_geometry.tex` — prime-attractor proof (L1)
- `canonical/alpha/alpha_derivation_routes.md` — routes survey
- `canonical/alpha/gauge_normalization_attempt.tex` — Route A1
- `canonical/alpha/symmetry_breaking_alpha_attempt.tex` — Route A2
- `research_tracks/alpha/layer2_coding_alpha_scan.py` — Route A4 scan script
- `DERIVATION_INDEX.md` — full derivation inventory
