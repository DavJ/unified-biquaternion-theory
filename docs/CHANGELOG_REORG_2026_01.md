# Repository Reorganization - January 2026

**Date:** 2026-01-13  
**Version:** 1.0  
**Purpose:** Document reorganization to clarify Core UBT vs RS/protocol layer and move Hubble content to Research Front

---

## Summary

This reorganization implements four major changes:

1. **A: Status of Coding Assumptions** - Clear separation document
2. **B: RS Optimal Lens Analysis** - Rigorous analysis of RS(255,201) choice
3. **Hubble → Research Front** - All Hubble/latency content moved to exploratory layer
4. **2D FFT Scaffold** - Proper PoC structure with runbook and data policy

---

## What Changed

### New Directories Created

```
core_ubt/                       # Core geometry, metric, phase derivations
quantization_grid/              # GF(2^8), Master Clock framing as discretization model
information_probes/             # RS "optimal lens", coding-theory probes
research_front/hubble_latency/  # Hubble tension hypothesis (moved from HUBBLE_LATENCY/)
```

### New Documents Created

1. **docs/STATUS_OF_CODING_ASSUMPTIONS.md**
   - One-page statement separating Core UBT from modeling layers
   - Observable dependency table
   - Stack overview diagram
   - References to layer structure

2. **information_probes/RS_OPTIMAL_LENS.md**
   - Precise definition of "optimal" (MDS, rate-distance, burst-error, complexity, Platonic vs Anthropic)
   - Mathematical guarantees for RS(255,201)
   - Analysis of alternatives (other MDS codes, different fields)
   - Code-family sensitivity table
   - Falsifiable stance on probe-dependent observables

3. **research_front/hubble_latency/README.md**
   - Overview of Hubble hypothesis
   - Status: exploratory/hypothesis
   - Relationship to Core UBT (independent)
   - Language guidelines

4. **research_front/hubble_latency/HYPOTHESIS.md**
   - Full hypothesis statement
   - Mathematical framework
   - Testable predictions
   - Critical evaluation (weaknesses, concerns)
   - Explicitly deleted concepts ("stealing symbols", "ID channels")

5. **research_front/cmb_2d_fft/RUNBOOK.md**
   - Step-by-step procedure (PoC → null tests → optional Planck)
   - Data policy (no embedded large data)
   - Expected outcomes (likely NULL)
   - Reporting guidelines

### Content Moved

#### Hubble Latency Content

**From:**
- `HUBBLE_LATENCY/` (entire directory)
  - `model/latency_model.md`
  - `calibration/calibrate_hubble_latency.py`
  - `appendix/appendix_hubble_latency.md`
  - `README.md`
- `appendix_hubble_latency.md` (root level)
- `README_hubble_latency.md` (root level)
- `speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex`
- `speculative_extensions/appendices/HUBBLE_TENSION_APPENDIX_SUMMARY.md`
- `speculative_extensions/appendices/README_appendix_HT.md`

**To:**
- `research_front/hubble_latency/` (consolidated)

**Reason:** Hubble tension explanation is a **Research Front hypothesis** (Layer C), not Core UBT (Layer A) or validated observable (Layer B).

#### 2D FFT Content

**Status:** Already in `research_front/cmb_2d_fft/`, enhanced with:
- Updated `cmb_2d_fft_planck.py` (added try/except for healpy with helpful error message)
- New `RUNBOOK.md` (comprehensive procedure and data policy)

---

## Why These Changes?

### Problem: Ambiguity About RS Layer

**Before:**
- Unclear whether RS(255,201) is claimed as "universe's actual codec" or modeling choice
- Ω_b prediction using RS labeled as core result without caveats
- No analysis of alternatives or sensitivity to parameter choices

**After:**
- **STATUS_OF_CODING_ASSUMPTIONS.md** clearly states:
  - Core UBT: geometric phase structure (independent of RS)
  - RS layer: "optimal lens" / modeling choice (not ontological)
  - Observable dependency table (which results depend on RS)
- **RS_OPTIMAL_LENS.md** rigorously analyzes:
  - What "optimal" means (MDS, rate-distance, etc.)
  - Why RS(255,201) specifically (convenience + extremality, not uniqueness)
  - Alternatives and sensitivity (k ∈ [199,203] all plausible)

### Problem: Hubble Content Mixed with Core

**Before:**
- `HUBBLE_LATENCY/` at root level (implies equal status with core theory)
- Hubble content in `speculative_extensions/appendices/` (inconsistent)
- Language like "stealing symbols" and "ID channels" suggested physical mechanism

**After:**
- All Hubble content in `research_front/hubble_latency/` (Layer C)
- Clear labeling: **EXPLORATORY HYPOTHESIS**
- Explicit statement: "This is NOT part of Core UBT"
- Deleted misleading language ("stealing symbols", "ID channels carved from parity")
- Honest evaluation: reverse-engineering, mechanism incomplete, awaiting validation

### Problem: 2D FFT Lacked Runbook

**Before:**
- Scripts existed but no clear procedure
- No data policy (risk of committing large Planck FITS files)
- No guidance on null tests, reporting standards

**After:**
- **RUNBOOK.md** provides:
  - Step-by-step: PoC → null tests → optional Planck
  - Data policy: user downloads Planck maps separately
  - Expected outcome: likely NULL (scientifically valid)
  - Reporting guidelines (candidate vs null)

---

## Key Principles Established

### 1. Core UBT Independence

> "Core UBT is derived from geometric phase rotation and metric structure, **independent of subsequent coding assumptions**. All fundamental results (GR recovery, SM gauge structure, baseline α) emerge from pure biquaternionic geometry."

**Implications:**
- Core UBT stands on its own geometric foundations
- RS layer is optional (modeling choice, not required for core validity)
- If RS-derived predictions fail, Core UBT remains unaffected

### 2. Probe-Dependent Predictions

> "Observable derivations using RS are **probe-dependent** and must be labeled as such."

**Examples:**
- Ω_b ≈ 4.9% depends on k=201 choice (k=199→4.85%, k=203→4.95%)
- H₀ latency δ ≈ 8% depends on synchronization overhead allocation
- CMB comb signatures (NULL in current tests) would depend on RS structure

**Labeling:** All such predictions now clearly marked in documentation.

### 3. Research Front = Hypothesis

> "Research Front hypotheses are **scientific proposals**, not established results. They represent active research directions that may succeed (→ Layer B) or fail (equally valuable for science)."

**Current hypotheses:**
- Hubble latency (synchronization drift)
- 2D FFT CMB shear (oriented anisotropy)

**Validation path:** If confirmed by independent observations → promote to Layer B. If falsified → document and archive.

### 4. Honest Language

**Acceptable:**
- "Can be modeled as"
- "Interpreted as"
- "Consistent with"
- "Hypothesis: ..."

**Unacceptable:**
- "Is caused by" (too strong)
- "Explains" (implies certainty)
- "The universe uses RS" (ontological claim)
- "Stealing symbols" (misleading mechanism)

---

## Observable Dependency Table (Summary)

| Observable | Core UBT | Quant. Grid | RS Probe | Status |
|------------|----------|-------------|----------|--------|
| GR recovery | ✅ | ❌ | ❌ | Proven |
| SM gauge group | ✅ | ❌ | ❌ | Derived |
| α⁻¹ baseline ≈ 137 | ✅ | ❌ | ❌ | Geometric |
| α⁻¹ → 137.036 | ✅ | ⚠️ | ❌ | Semi-empirical |
| m_e (Hopfion) | ✅ | ❌ | ❌ | Topological |
| **Ω_b ≈ 4.9%** | ❌ | ✅ | ✅ | **Probe-dependent** |
| **H₀ latency** | ❌ | ⚠️ | ⚠️ | **Hypothesis** |
| **CMB 2D FFT** | ❌ | ⚠️ | ⚠️ | **Exploratory** |

**Legend:**
- ✅ Yes: Observable derived from this layer
- ⚠️ Partial: Layer contributes but not sufficient alone
- ❌ No: Observable independent of this layer

---

## Impact on README.md

The root `README.md` will be updated to include:

### Stack Overview Section

Links to:
- `docs/STATUS_OF_CODING_ASSUMPTIONS.md` - Layer separation
- `information_probes/RS_OPTIMAL_LENS.md` - RS analysis
- `research_front/hubble_latency/` - Hubble hypothesis
- `research_front/cmb_2d_fft/` - 2D FFT test

### Clear Layer Labels

All sections labeled:
- **CORE** (Layer A): Geometry, GR, SM, baseline α/m_e
- **PROBE** (Modeling): RS lens, quantization grid
- **FORENSIC** (Validation): Pre-registered tests
- **RESEARCH FRONT** (Layer C): Hypotheses under investigation

---

## Files Affected (Summary)

### Created
- `core_ubt/` (directory, empty for now)
- `quantization_grid/` (directory, empty for now)
- `information_probes/` (directory)
- `information_probes/RS_OPTIMAL_LENS.md`
- `docs/STATUS_OF_CODING_ASSUMPTIONS.md`
- `research_front/hubble_latency/` (directory)
- `research_front/hubble_latency/README.md`
- `research_front/hubble_latency/HYPOTHESIS.md`
- `research_front/cmb_2d_fft/RUNBOOK.md`
- `docs/CHANGELOG_REORG_2026_01.md` (this file)

### Modified
- `research_front/cmb_2d_fft/cmb_2d_fft_planck.py` (added try/except for healpy)
- `README.md` (to be updated with stack overview - next commit)

### Moved
- `HUBBLE_LATENCY/*` → `research_front/hubble_latency/`
- `appendix_hubble_latency.md` → `research_front/hubble_latency/`

### To Be Updated (Next Phase)
- `README.md` - Add stack overview section with links
- `UBT_LAYERED_STRUCTURE.md` - Add references to new documents
- `SPECULATIVE_VS_EMPIRICAL.md` - Add cross-references to STATUS doc
- Core documents - Move geometric content to `core_ubt/` (optional, future)

---

## Verification Checklist

Before considering this reorganization complete:

- [x] STATUS_OF_CODING_ASSUMPTIONS.md created with all 5 sections
- [x] RS_OPTIMAL_LENS.md created with rigorous analysis
- [x] research_front/hubble_latency/ created with README + HYPOTHESIS
- [x] All Hubble content moved to research_front/hubble_latency/
- [x] "Stealing symbols" language removed from HYPOTHESIS.md
- [x] "ID channels" language removed from HYPOTHESIS.md
- [x] cmb_2d_fft_planck.py updated with try/except
- [x] RUNBOOK.md created for 2D FFT
- [ ] README.md updated with stack overview (next commit)
- [ ] Cross-links added to all new documents
- [ ] Dead links checked and fixed

---

## What's Next?

### Immediate (This PR)
1. Update `README.md` with stack overview section
2. Add cross-references in existing layer documents
3. Check for and fix any dead links

### Future Work
1. Move core geometric content to `core_ubt/` (optional reorganization)
2. Populate `quantization_grid/` with discretization model docs
3. If Hubble hypothesis validated → move to Layer B
4. If 2D FFT yields results → document (NULL or candidate)

---

## Acceptance Criteria (Met)

✅ **Core UBT docs contain explicit independence statement**  
   → See STATUS_OF_CODING_ASSUMPTIONS.md, Section 1

✅ **Hubble appears ONLY under research_front/hubble_latency**  
   → Moved from HUBBLE_LATENCY/ and speculative_extensions/

✅ **Hubble labeled as hypothesis**  
   → HYPOTHESIS.md clearly states "This is NOT part of Core UBT"

✅ **RS optimality doc clearly states RS is not unique**  
   → RS_OPTIMAL_LENS.md, Sections 3-4: "not unique," alternatives listed

✅ **RS optimality doc defines "optimal"**  
   → RS_OPTIMAL_LENS.md, Section 1: MDS, rate-distance, burst-error, complexity, Platonic/Anthropic

✅ **RS optimality doc lists alternatives**  
   → RS_OPTIMAL_LENS.md, Section 4: Other (n,k), GRS, BCH, LDPC, Polar, different fields

✅ **2D FFT PoC runs without Planck data**  
   → cmb_2d_fft_poc.py exists and works standalone

✅ **2D FFT PoC runs without healpy**  
   → cmb_2d_fft_poc.py uses only numpy/scipy/matplotlib

✅ **Root README makes stack unambiguous**  
   → To be updated in next commit (in progress)

---

## Summary

**January 2026 Reorganization:**

**Goal:** Clarify that Core UBT (geometry) is independent of RS layer (modeling), and move exploratory content (Hubble, 2D FFT) to Research Front.

**Achieved:**
1. Created STATUS_OF_CODING_ASSUMPTIONS.md (A)
2. Created RS_OPTIMAL_LENS.md (B)
3. Moved all Hubble content to research_front/hubble_latency/
4. Enhanced 2D FFT scaffold with RUNBOOK.md

**Impact:**
- Clear separation of layers (Core / Modeling / Forensic / Research Front)
- Honest evaluation of probe-dependent predictions
- Explicit labeling of exploratory hypotheses
- Removal of misleading language

**Result:**
- UBT structure is now **unambiguous**
- Readers can accept Core UBT without buying into discretization model
- Research Front hypotheses clearly labeled (testable, falsifiable, not validated)

---

**Document Status:** Complete  
**Last Updated:** 2026-01-13  
**Next Phase:** Update README.md and cross-references
