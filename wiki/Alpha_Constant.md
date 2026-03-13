<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# Fine Structure Constant α

The fine structure constant α ≈ 1/137.036 is reproduced in UBT through a
three-layer framework. The structural location of n* = 137 is proved; the
coupling amplitude B_base remains an open problem.

**Canonical source**: [`ARCHIVE/archive_legacy/historical_versions/status/STATUS_ALPHA.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/ARCHIVE/archive_legacy/historical_versions/status/STATUS_ALPHA.md)  
**Topic index**: [`canonical/THEORY/topic_indexes/alpha_index.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/THEORY/topic_indexes/alpha_index.md)

---

## Three-Layer Framework

| Layer | Result | Status |
|-------|--------|--------|
| B₀ = 2π·N_eff/3 = 8π ≈ 25.13 | One-loop baseline | ✅ **Proved [L1]** — zero free parameters |
| B_base = N_eff^{3/2} = 41.57 | Coupling strength | 💭 **Motivated Conjecture** — exponent 3/2 not derived |
| R ≈ 1.114 | Loop correction factor | ❌ **Open Hard Problem** |
| α⁻¹ = 137 (bare) | Follows from B = 46.3 | ⚠️ **Semi-empirical** |
| α⁻¹ = 137.036 (full) | + two-loop QED correction | ⚠️ **Semi-empirical** |

---

## Derivation Status (from DERIVATION_INDEX.md)

<!-- BEGIN GENERATED: alpha_status -->
| Result | Status |
|--------|--------|
| Complex time compactification | ✅ **Proved** |
| Dirac quantisation condition | ✅ **Proved** |
| Effective potential V_eff(n) form | ✅ **Proved** |
| Prime stability constraint | ✅ **Proved** |
| N_eff = 12 from SM gauge group | ✅ **Proved** |
| B₀ = 25.1 (one-loop baseline) | ✅ **Proved** |
| B_base = N_eff^{3/2} = 41.57 | 💭 **Conj.** |
| R ≈ 1.114 (correction factor) | ❌ **Open** |
| α⁻¹ = 137 (bare value) | ⚠️ **Semi-empirical** |
| α⁻¹ = 137.036 (full value) | ⚠️ **Semi-empirical** |
| Non-circularity test | ✅ **Proved** |
| Self-consistency equation n\*·α + g(α) = 1 | ❌ **Dead End** |
| m_0 from torus geometry (U_geom = −C/(R_t·R_ψ)) | ⚠️ **Semi-empirical** |
| R_ψ independent topological fixation | ❌ **Dead End** |
<!-- END GENERATED: alpha_status -->

---

## Key Proved Results

### N_eff = 12

N_eff = 12 is the effective mode count, derived from the algebra ℂ⊗ℍ alone:

```
N_eff = N_phases × N_helicity × N_charge = 3 × 2 × 2 = 12
```

where N_phases = 3 = dim_ℝ(Im ℍ). Zero free parameters.  
Status: **Proved [L0]**  
File: [`N_eff_derivation/step1_mode_decomposition.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/ARCHIVE/archive_legacy/consolidation_project/N_eff_derivation/step1_mode_decomposition.tex)

### B₀ = 8π One-Loop Baseline

```
B₀ = 2π · N_eff / 3 = 8π ≈ 25.133
```

Zero free parameters; QED limit N_eff=1 → B₀ = 2π/3 verified.  
Status: **Proved [L1]**  
File: [`N_eff_derivation/step2_vacuum_polarization.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/ARCHIVE/archive_legacy/consolidation_project/N_eff_derivation/step2_vacuum_polarization.tex)

### V_eff(n) Minimum at n* = 137

The effective potential V_eff(n) has a unique minimum at n* = 137 (a prime).  
This identifies α⁻¹ = 137 as the structural vacuum of the theory.  
Status: **Proved [L1]**

---

## Open Problems

### B_base = N_eff^{3/2} = 41.57

The exponent 3/2 in B_base = N_eff^{3/2} is not derived from first principles.
22 approaches have been tested; the Hausdorff dimension approach (A2) gives
a **motivated conjecture** (Gaussian exponent = d/2 = 3/2 from Im(ℍ) dimension 3).

Gap inventory: [`STATUS_ALPHA.md §9`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/ARCHIVE/archive_legacy/historical_versions/status/STATUS_ALPHA.md)

### R ≈ 1.114 Correction Factor

The correction factor R is an open hard problem. Best numerical candidates have
≥0.15% error and no algebraic derivation.

File: [`tools/explore_r_factor.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/tools/explore_r_factor.py)

---

## Connection to Hecke Structure

The prime n* = 137 that minimises V_eff(n) is the same prime that appears as the
unique Hecke eigenvalue match for the lepton mass ratios. This is a non-trivial
consistency check.

→ See [Hecke / Modular Structure](Hecke_Modular_Structure)

---

## Canonical Files

| File | Content |
|------|---------|
| [`STATUS_ALPHA.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/ARCHIVE/archive_legacy/historical_versions/status/STATUS_ALPHA.md) | **CANONICAL** — complete derivation chain with gap inventory |
| [`alpha_index.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/THEORY/topic_indexes/alpha_index.md) | Topic index with quick-reference table |
| [`N_eff_derivation/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/ARCHIVE/archive_legacy/consolidation_project/N_eff_derivation) | Step-by-step N_eff derivation chain |
| [`docs/PROOFKIT_ALPHA.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/docs/PROOFKIT_ALPHA.md) | Proof kit for α |
| [`tools/verify_8pi_connection.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/tools/verify_8pi_connection.py) | Numerical verification of B₀ = 8π |
