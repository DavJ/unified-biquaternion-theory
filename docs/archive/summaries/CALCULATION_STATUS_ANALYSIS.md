# Calculation Status Analysis

**Date:** 2025-11-09  
**Issue:** Suspicious values in CSV files that appear to be hardcoded

## Executive Summary

After deep analysis of the calculation implementations, I confirmed that **both alpha and electron mass calculations use hardcoded experimental values**, not UBT first-principles derivations.

## Critical Findings

### ❌ Alpha IS HARDCODED - CONFIRMED

**File:** `alpha_core_repro/alpha_two_loop.py`  
**Lines 189 and 196:**
```python
if p == 137:
    # Reference value (experimental matching)
    delta_ct = 0.035999000  # ← HARDCODED (line 189)
else:
    delta_137 = 0.035999000  # ← HARDCODED (line 196)
    # Extrapolate using approximation...
    delta_ct = delta_137 + 0.001 * (float(p) - 137.0) / 137.0
```

**Proof:**
- Direct source inspection shows `delta_ct = 0.035999000` on line 189
- Value is **EXACTLY** 0.035999 (verified with floating-point hex representation)
- Does NOT vary when changing parameters (always returns 0.035999 for p=137)
- Other primes calculated using linear approximation from this hardcoded anchor

**The value α^-1 = 137.035999000000 is:**
- ❌ NOT calculated from UBT theory
- ❌ NOT derived from two-loop integrals  
- ✅ Hardcoded experimental target (CODATA 2022: α^-1 = 137.035999177)
- ✅ Used as anchor point for approximating other sectors

### ❌ Electron Mass IS HARDCODED - CONFIRMED

**File:** `alpha_core_repro/alpha_two_loop.py`

**Lines 187-214:**
```python
if p == 137:
    # Reference value (experimental matching)
    delta_ct = 0.035999000  # ← HARDCODED
else:
    # Extrapolate using beta function
    # ...
    delta_ct = delta_137 + 0.001 * (float(p) - 137.0) / 137.0
```

**Status:**
- ✅ The value `0.035999` matches experimental α^-1 = 137.035999
- ⚠️ The value is **HARDCODED** for p=137, not derived from first principles
- ⚠️ Other primes use a simplified approximation formula
- The code includes theoretical framework (N_eff, R_psi, beta functions) but doesn't use them for actual calculation

**What it claims:**
- "Fit-free UBT calculation"
- "Two-loop QED vacuum polarization"
- "No fitted parameters"

**What it actually does:**
- Uses `delta_ct = 0.035999000` hardcoded for p=137
- Applies simple linear approximation for other primes

### 2. Electron Mass Calculation - HARDCODED ⚠️

**File:** `ubt_masses/core.py`

**Lines 141-143:**
```python
# Experimental pole mass (PDG 2024): m_e = 0.51099895 MeV
# MSbar mass at μ = m_e is approximately:
m_pole_experimental = 0.51099895  # MeV  # ← HARDCODED
mbar_approx = m_pole_experimental * (1.0 - delta_qed)
```

**Status:**
- ❌ The value `0.51099895 MeV` is **HARDCODED from PDG experimental data**
- ❌ MSbar mass is computed as simple 1-loop QED correction to experimental value
- ❌ NOT derived from UBT theory at all

**What it claims:**
- "Fit-free mass calculations using α from UBT"
- "UBT mass operator for electron"
- "Core UBT formula that produces m̄_e from theory invariants"

**What it actually does:**
- Uses experimental PDG value: `m_pole_experimental = 0.51099895`
- Applies simple QED correction
- Comment says "TODO: Replace with actual UBT derivation"

## Why Values Look Suspicious

### Alpha: 137.035999000000
- The value is **exactly** 0.035999 for the correction
- This is because it's hardcoded to match experiment
- The trailing zeros are from floating-point representation
- It's not a "derived" value, it's a **target value** that was hardcoded

### Electron Mass: 0.510996192910
- Computed from hardcoded experimental value `0.51099895`
- QED correction applied: `m̄ = m_pole × (1 - α/π)`
- The precision comes from the calculation, but the input is experimental

## What is Actually Implemented

### Alpha Calculation Framework:
✅ **Present (but not used for p=137):**
- Two-loop QED formalism structure
- Beta function calculations
- N_eff = 12 (biquaternion modes)
- R_psi = 1 (compactification radius)
- MSbar scheme constants

❌ **Missing actual two-loop calculation:**
- Master integrals not evaluated
- Ward identity not applied numerically  
- Just returns hardcoded 0.035999 for p=137

### Electron Mass Framework:
✅ **Present:**
- MSbar/pole mass conversion (1-loop QED)
- Fixed-point iteration for self-consistency
- Alpha coupling from (partially hardcoded) alpha calculator

❌ **Missing UBT mass formula:**
- No Θ field derivation
- No complex time structure
- No geometric invariants
- Code explicitly says "TODO: Replace with actual UBT derivation"

## CSV File Status

| CSV File | Contains | Source | Status |
|----------|----------|--------|--------|
| `alpha_core_repro/out/alpha_two_loop_grid.csv` | Alpha for various primes | Hardcoded 0.035999 + approximation | ⚠️ Not fully derived |
| `data/leptons.csv` | Electron mass | Hardcoded PDG value + QED | ❌ Experimental input |

## Precision Analysis

The **precision is genuine** in the sense that:
- Calculations use full floating-point precision
- QED corrections are properly applied
- CSV files correctly store all decimal places

However, the **underlying values are not UBT-derived**:
- Alpha: Uses experimental target `α^-1 = 137.035999`
- Electron: Uses experimental PDG value `m_e = 0.51099895 MeV`

## Implications for Documentation

The PYTHON_SCRIPTS_REPORT.md states:
- "✅ PROPER ALPHA CALCULATION" - **INCORRECT** - should be "⚠️ EXPERIMENTAL FIT"
- "✅ PROPER LEPTON MASS CALCULATION" - **INCORRECT** - should be "❌ USES PDG VALUE"

## Recommendations

1. **Update Documentation:**
   - Clearly mark that current implementation uses experimental target values
   - Distinguish between "calculation framework" and "actual derivation"
   - Mark as "experimental fitting" not "fit-free calculation"

2. **Fix the Code or Update Claims:**
   - Option A: Implement actual UBT derivations
   - Option B: Update comments/docs to say "experimental calibration point"

3. **Update PYTHON_SCRIPTS_REPORT.md:**
   - Change "PROPER CALCULATION" to "EXPERIMENTAL FIT"
   - Add warning that values are hardcoded targets
   - Note that only the precision and QED corrections are computed

4. **Update CSV_AND_DOCUMENTATION_POLICY.md:**
   - Clarify that CSV values come from experimental calibration
   - Note that UBT derivations are TODO

## Correct Status

### What IS Implemented:
- ✅ QED 1-loop and 2-loop correction formulas (structure only)
- ✅ MSbar/pole mass conversion (QED)
- ✅ Beta function framework
- ✅ CSV export pipeline
- ✅ LaTeX integration via pgfplotstable

### What is NOT Implemented:
- ❌ UBT first-principles derivation of α
- ❌ UBT first-principles derivation of m_e
- ❌ Master integral evaluation for two-loop
- ❌ Θ field mass operator
- ❌ Complex time geometric contributions

### Actual Calculation Method:
- **Alpha:** Hardcoded experimental target (α^-1 = 137.035999) with approximation for other primes
- **Electron Mass:** Hardcoded PDG experimental value (m_e = 0.51099895) with QED corrections

## Conclusion

The values in the CSV files are **NOT** derived from UBT theory. They are:
- **Alpha:** Experimental target value (hardcoded)
- **Electron mass:** PDG experimental value (hardcoded)

The calculations provide:
- Proper QED corrections
- Proper precision handling
- Beta function extrapolation
- But NOT first-principles UBT derivations

This should be clearly documented to avoid misleading claims about "fit-free" or "proper" calculations.
