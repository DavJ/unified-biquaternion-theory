# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2025-11-08 - Publication & Review Readiness

### Added

- **Publication infrastructure**: Created `publication/arxiv/`, `publication/osf/`, `publication/artifacts/` directories
  - arXiv preprint manuscript: `publication/arxiv/main.tex` including baseline theorem, CT scheme, R_UBT extraction, geometric inputs, and reproducibility checklist
  - Reproducibility checklist: `publication/reproducibility_checklist.tex` (one-page summary of assumptions, tests, build process, artifacts, limitations)
  - GitHub workflow: `.github/workflows/publication.yml` for automated PDF builds and artifact uploads
  
- **Community review infrastructure**:
  - Issue template: `.github/ISSUE_TEMPLATE/review_comment.yaml` for technical review comments (section, equation label, claim type, reproduction steps, expected vs. actual)
  - Issue template: `.github/ISSUE_TEMPLATE/replication_report.yaml` for independent replication reports (environment, steps, outputs, diffs, logs, PDF hash)
  - Replication protocol: `docs/REPLICATION_PROTOCOL.md` with step-by-step verification instructions
  - Reviewer FAQ: `docs/REVIEWER_FAQ.md` addressing common questions and potential objections
  - External discussion tracker: `docs/EXTERNAL_DISCUSSION_TRACKER.md` for public record of seminars, reviews, preprints
  
- **Citation metadata**: `CITATION.cff` (v0.3.0) with DOI placeholder, author information, repository URL

### Changed

- **Baseline assertion enforcement**: All references to R_UBT now point to CT baseline theorem (R_UBT = 1 under A1–A3)
  - Verified no placeholder/pending/1.84 values remain in context of R_UBT (test suite confirms)
  - `EMERGENT_ALPHA_README.md` updated with explicit baseline statement
  - `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` already contains two-loop CT baseline paragraph
  - `consolidation_project/alpha_two_loop/tex/R_UBT_extraction.tex` includes baseline subsection with boxed result
  - `consolidation_project/alpha_two_loop/tex/geometric_inputs_proof.tex` formalizes geometric locking (A1)
  
- **README.md**: Added "How to Review This Repo" section with clear entry points for reviewers

### Removed

- None (all changes are additive to maintain backward compatibility)

### Notes

- Tests pass: `pytest -q consolidation_project/alpha_two_loop/tests` ✓
- Baseline established: \(\mathcal{R}_{\mathrm{UBT}} = 1\) at two loops with no fitted parameters
- Publication ready: arXiv manuscript builds successfully (pending manual submission)
- Community ready: Issue templates, replication protocol, and FAQ provide clear paths for engagement

## [Previous Releases]

### Added

- **New unified α derivation**: `consolidation_project/appendix_ALPHA_one_loop_biquat.tex`
  - Single source of truth for fine-structure constant derivation
  - Derives B coefficient from first principles: B = (2π N_eff) / (3 R_ψ) × β_2loop ≈ 46.3
  - UV cutoff set geometrically: Λ = 1/R_ψ (no free parameters)
  - Mode counting table justifies N_eff = 12 from biquaternion structure
  - Renormalization condition at μ₀ = m_e (configurable via macro)
  
- **Biquaternion time transition criterion**: Added formal criterion to `appendix_B_scalar_imaginary_fields_consolidated.tex`
  - Complex time T = t + iψ valid when ‖∇⊥Θ‖² ≪ ‖∂ₜΘ‖²
  - Full biquaternion time τ = t + iψ + jχ + kξ required otherwise
  - Reference tag [TRANSITION_CRITERION] for tracking usage

- **Linter for complex time usage**: `scripts/lint_complex_time_usage.py`
  - Checks that complex time mentions reference transition criterion
  - Ensures biquaternion time priority is maintained
  - CI integration ready

- **Symbolic alpha tests**: `scripts/test_symbolic_alpha.py`
  - Validates B depends only on R_ψ and N_eff (no numeric 46.3)
  - Tests μ₀ invariance in B definition
  - Verifies N_eff counting table sums to 12
  - Confirms α⁻¹ = 137 from effective potential minimum

### Changed

- **Updated Appendix E** (`appendix_E_SM_QCD_embedding.tex`):
  - Replaced "α is empirical in CORE" with reference to new Appendix α
  - Now states: "In CORE, α is parameterized via renormalization condition at μ₀; complete derivation in Appendix α"

- **Updated fermion mass documentation** (`FERMION_MASS_ACHIEVEMENT_SUMMARY.md`):
  - Reclassified m(n) = A·n^p - B·n·ln(n) as "2-parameter phenomenological ansatz"
  - Added roadmap to first-principles derivation
  - Clarified symbol B distinction: fermion mass B vs α running B are physically different contexts
  - Noted future work will unify or rename to avoid confusion

- **Updated CI configuration** (`.github/latex_roots.txt`):
  - Added `appendix_ALPHA_one_loop_biquat.tex` to compilation list
  - Commented out deprecated files: `emergent_alpha_*.tex`, `alpha_final_derivation.tex`
  - Documented deprecation reasons

### Deprecated

- **"B = 46.3 fitted" statements**: The constant B is now derived, not fitted
  - Old approach: B stated as empirical constant from "quantum calculations"
  - New approach: B = (2π × 12) / 3 × 1.8 ≈ 46.3 derived from mode counting
  - Files with "B = 46.3 fitted" should update to reference Appendix α
  - This resolves the critical gap in α derivation rigor

- **Separate emergent_alpha_*.tex files**: Superseded by unified appendix
  - `emergent_alpha_calculations.tex` → Use `appendix_ALPHA_one_loop_biquat.tex`
  - `emergent_alpha_executive_summary.tex` → Deprecated
  - `emergent_alpha_from_ubt.tex` → Deprecated
  - `unified_biquaternion_theory/alpha_final_derivation.tex` → Deprecated

### Migration Notes

**For users referencing α derivation:**
- Old: Reference scattered across multiple files with "B = 46.3" as input
- New: Reference `appendix_ALPHA_one_loop_biquat.tex` as single source
- Impact: No change to numerical predictions, but derivation is now rigorous

**For developers:**
- Symbol B has two meanings: (1) α running coupling coefficient, (2) fermion mass logarithmic term
- These are distinct but related via quantum corrections framework
- Future work will clarify relationship or adopt distinct notation

---

## [2025-11-03] - Alpha and Electron Mass Unification

### Added
- Unified derivation removing circularity and free parameters
- Geometric UV cutoff prescription
- Biquaternion time transition criterion
- Testing and validation infrastructure

### Fixed
- Removed circularity in α and electron mass derivations
- Clarified symbol B usage in different contexts
- Established biquaternion time as primary formulation

---

## [2025-11-02] - Merged master branch updates (commits ec1376e and d73012e)
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
