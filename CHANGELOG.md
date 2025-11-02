# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Merged master branch updates** (commits ec1376e and d73012e)
  - P-adic α derivation: `consolidation_project/appendix_ALPHA_padic_derivation.tex`
  - Executive summaries: `alpha_padic_executive_summary.tex`, `ALPHA_PADIC_README.md`
  - Scientific rating document: `UBT_SCIENTIFIC_RATING_2025.md`
  - Integration assessments: `HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md`, `AHARONOV_TSVF_ANALYSIS.md`
  - Comprehensive evaluation summaries and verification checklists
  - Enhanced B constant derivation based on gauge structure (N_eff = 12)
  - P-adic calculator scripts: `scripts/padic_alpha_calculator.py`, `scripts/test_padic_alpha.py`

- **Symbolic derivation of the B constant** in `emergent_alpha_from_ubt.tex`
  - Mathematical derivation showing B arises from one-loop vacuum fluctuations
  - Based on gauge structure: B = N_eff × (2π/σ) ≈ 46.3 for SU(3)×SU(2)×U(1)
  - Result consistent with empirical constant used in α derivation

- **Python verification script** `scripts/verify_B_integral.py`
  - Symbolic and numerical verification of the B constant integral using SymPy and SciPy
  - Confirms phase fluctuation integral I ≈ 0.904 for σ = 7.35
  - Shows renormalization factor β_renorm ≈ 8.15 connects I to B ≈ 46.27
  - Verifies that B = 46.27 correctly selects n = 137 as minimum of effective potential
  - Includes parameter scan and visualization of B(σ) relationship
  - Generates verification plot: `scripts/B_constant_verification.png`

### Changed

- **Lamb shift numerical prediction** corrected in multiple files
  - `consolidation_project/appendix_W_testable_predictions.tex`: Updated n=2 correction from ~10 kHz to ~1 kHz
  - `UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md`: Updated precision requirements (100× → 1000× improvement)
  - `DATA_ANALYSIS_ACTION_ITEMS.md`: Marked Lamb shift issue as resolved
  - Added comprehensive explanation document: `LAMB_SHIFT_EXPLANATION.md`
  - Root cause: Documentation error (formula was correct, stated value incorrect)
  - Impact: No conflict with experiments; still testable with next-gen spectroscopy (5-10 year timeline)

### Fixed

- Corrected numerical discrepancy in Lamb shift prediction (factor of ~10 error in stated value)
- Updated testability timeline for Lamb shift from 2-5 years to 5-10 years (more realistic for 1 kHz precision)

## [2025-11-02] - Lamb Shift Correction

### Fixed
- Lamb shift prediction numerical values corrected throughout documentation
- Added detailed calculation notes for transparency

### Documentation
- Created `LAMB_SHIFT_EXPLANATION.md` with comprehensive analysis
- Updated `UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md` with corrected precision requirements
- Updated `UBT_VS_OTHER_THEORIES_COMPARISON.md` with clarified error description

---

## Notes

- **UBT Version**: Development version
- **Repository**: https://github.com/DavJ/unified-biquaternion-theory
- **License**: See LICENSE.md
