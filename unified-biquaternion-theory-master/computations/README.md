# UBT Computational Tools

This directory contains all computational scripts for Unified Biquaternion Theory calculations and validations.

## Organization

### Core Calculations
- **`alpha/`** - Fine structure constant α calculations
  - Fit-free UBT baseline: α⁻¹ = 137 (exact)
  - Two-loop QED/UBT matching
  - P-adic sector variations
  
- **`masses/`** - Fermion mass calculations
  - Lepton masses (electron, muon, tau)
  - Quark masses  
  - Neutrino masses
  - **Status**: Currently uses experimental inputs with QED corrections (placeholder for full UBT derivation)

### Supporting Tools
- **`validation/`** - Verification and consistency checks
- **`analysis/`** - Phenomenology and predictions
- **`padic/`** - P-adic extensions
- **`tools/`** - Development utilities

## Calculation Status Summary

### Fit-Free Calculations (From UBT First Principles)

| Observable | Value | Status | Notes |
|------------|-------|--------|-------|
| α⁻¹ (baseline) | 137.000... | ✅ Derived | R_UBT = 1 theorem, no parameters |

### Calculations Using Experimental Inputs

| Observable | Value | Status | Notes |
|------------|-------|--------|-------|
| m_e (pole) | 0.51099895 MeV | ⚠️ Input | PDG 2024 experimental value |
| m_e (MSbar) | ~0.5099 MeV | ⚠️ Derived | From pole mass via QED correction |

## Current Location of Computational Scripts

**Note**: This directory is being populated. Current script locations:

- Alpha calculations: `../alpha_core_repro/`
- Mass calculations: `../ubt_masses/`
- Validation scripts: `../scripts/validate_*.py`
- Analysis scripts: `../scripts/analyze_*.py`

Scripts will be moved here incrementally with proper documentation.

## Documentation

### What is Calculated vs. What is Input

**Fully Derived (No Free Parameters)**:
- α⁻¹ = 137 baseline from complex time topology
- R_UBT = 1 from Ward identities
- Geometric constants: N_eff = 12, R_ψ = 1

**Partially Derived (Uses Experimental Anchors)**:
- Electron mass: Uses PDG pole mass, applies QED corrections
- Quark and lepton mixing matrices: Fitted to experimental data

## References

- **Alpha Derivation**: `../consolidation_project/alpha_two_loop/FIT_FREE_ALPHA_README.md`
- **Mass Status**: `../FITTED_PARAMETERS.md`

---

**Last Updated**: 2025-11-10  
**Status**: Initial documentation, organization in progress
