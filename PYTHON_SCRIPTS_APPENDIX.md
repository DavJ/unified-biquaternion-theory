## Appendix: Complete Python Scripts Inventory

This section lists all 104 Python scripts in the repository.

### Directory: `alpha_core_repro/`

#### __init__.py

**Path:** `alpha_core_repro/__init__.py`

---

#### alpha_two_loop.py

**Path:** `alpha_core_repro/alpha_two_loop.py`

**Comment:** alpha_core_repro/alpha_two_loop.py SPDX-License-Identifier: MIT

**Features:** Generates CSV

---

#### export_alpha_csv.py

**Path:** `alpha_core_repro/export_alpha_csv.py`

**Description:** Exports two-loop strict alpha values to CSV for TeX inclusion.

**Features:** Generates CSV

---

#### run_grid.py

**Path:** `alpha_core_repro/run_grid.py`

**Comment:** alpha_core_repro/run_grid.py

---

#### two_loop.py

**Path:** `alpha_core_repro/two_loop.py`

**Description:** Dynamic shim to resolve `alpha_from_ubt_two_loop_strict(mu: float) -> float`

---

#### two_loop_core.py

**Path:** `alpha_core_repro/two_loop_core.py`

**Description:** Strict two-loop forwarder for α:

---

### Directory: `alpha_core_repro/tests/`

#### test_alpha_one_loop.py

**Path:** `alpha_core_repro/tests/test_alpha_one_loop.py`

**Comment:** Document expectation: RUBT must be 1 + O(α), not a scale-independent constant

---

#### test_alpha_two_loop.py

**Path:** `alpha_core_repro/tests/test_alpha_two_loop.py`

**Comment:** alpha_core_repro/tests/test_alpha_two_loop.py SPDX-License-Identifier: MIT

---

### Directory: `alpha_two_loop/symbolics/`

#### ct_two_loop.py

**Path:** `alpha_two_loop/symbolics/ct_two_loop.py`

---

### Directory: `automorphic/`

#### hecke_l_route.py

**Path:** `automorphic/hecke_l_route.py`

**Description:** Variant C: Automorphic / L-function route.

---

### Directory: `automorphic/tests/`

#### test_hecke_l_route.py

**Path:** `automorphic/tests/test_hecke_l_route.py`

**Comment:** automorphic/tests/test_hecke_l_route.py

---

### Directory: `cern_findings_and_ubt/`

#### analyze_cern_ubt_signatures.py

**Path:** `cern_findings_and_ubt/analyze_cern_ubt_signatures.py`

**Description:** UBT Signature Analysis for CERN/LHC Data

---

### Directory: `consolidation_project/alpha_two_loop/`

#### sketch_R_UBT.py

**Path:** `consolidation_project/alpha_two_loop/sketch_R_UBT.py`

**Description:** Two-loop computation skeleton for R_UBT(μ) in the complex-time scheme.

---

#### demo_qed_limit.py

**Path:** `consolidation_project/alpha_two_loop/demo_qed_limit.py`

**Comment:** Sanity: beta ~ α^2 + α^3 — tiny number at α≈1/137

---

#### validate_ct_baseline.py

**Path:** `consolidation_project/alpha_two_loop/validate_ct_baseline.py`

**Description:** Validation tests for CT Two-Loop Baseline R_UBT = 1

---

### Directory: `consolidation_project/alpha_two_loop/symbolics/`

#### __init__.py

**Path:** `consolidation_project/alpha_two_loop/symbolics/__init__.py`

**Description:** Symbolic computations for 2-loop alpha derivation in Complex Time (CT) scheme.

---

#### ct_two_loop_eval.py

**Path:** `consolidation_project/alpha_two_loop/symbolics/ct_two_loop_eval.py`

**Description:** CT Two-Loop Vacuum Polarization Evaluation.

---

#### ibp_system.py

**Path:** `consolidation_project/alpha_two_loop/symbolics/ibp_system.py`

**Description:** Integration-By-Parts (IBP) reduction system for 2-loop vacuum polarization.

---

#### master_integrals.py

**Path:** `consolidation_project/alpha_two_loop/symbolics/master_integrals.py`

**Description:** Master Integrals (MI) for 2-loop vacuum polarization in CT scheme.

---

### Directory: `consolidation_project/alpha_two_loop/tests/`

#### __init__.py

**Path:** `consolidation_project/alpha_two_loop/tests/__init__.py`

**Comment:** This file makes the tests directory a Python package

---

#### test_Neff_uniqueness.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_Neff_uniqueness.py`

**Description:** Test uniqueness and gauge/scheme independence of N_eff.

---

#### test_Rpsi_independence.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_Rpsi_independence.py`

**Description:** Test independence of R_psi from physical parameters.

---

#### test_ct_ward_and_limits.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_ct_ward_and_limits.py`

**Description:** Test Ward identity and Thomson limit using REAL computations (no stubs).

---

#### test_ibp_reduction.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_ibp_reduction.py`

**Description:** Test suite for IBP reduction to master integrals.

---

#### test_no_placeholders_and_ct_logic.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_no_placeholders_and_ct_logic.py`

**Description:** Test suite to ensure no placeholder/pending/1.84 references remain near R_UBT

---

#### test_no_stubs_left.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_no_stubs_left.py`

**Description:** Hygiene gate test: ensure no stub patterns remain in 2-loop code.

---

#### test_overview_masses_wording.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_overview_masses_wording.py`

**Comment:** Should NOT claim electron mass was derived FROM a fitted parameter Look for patterns that suggest it WAS fitted (not "not fitted") Positive assertions

---

#### test_readme_bq_ct_alpha_necessity.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_readme_bq_ct_alpha_necessity.py`

---

#### test_readme_causality_and_score.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_readme_causality_and_score.py`

---

#### test_repo_hygiene_readme.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_repo_hygiene_readme.py`

---

#### test_two_loop_invariance_sweep.py

**Path:** `consolidation_project/alpha_two_loop/tests/test_two_loop_invariance_sweep.py`

**Description:** Test invariance of R_UBT across gauge parameter ξ and renormalization scale μ.

**Features:** Generates CSV

---

### Directory: `consolidation_project/masses/tests/`

#### __init__.py

**Path:** `consolidation_project/masses/tests/__init__.py`

**Comment:** Test suite for fermion/quark mass program

---

#### test_masses_placeholders.py

**Path:** `consolidation_project/masses/tests/test_masses_placeholders.py`

---

### Directory: `consolidation_project/new_alpha_derivations/`

#### ubt_alpha_minimizer.py

**Path:** `consolidation_project/new_alpha_derivations/ubt_alpha_minimizer.py`

**Comment:** SPDX-License-Identifier: CC-BY-4.0 Copyright (c) 2025 David Jaroš This file is part of the Unified Biquaternion Theory project. Licensed under Creativ

---

#### ubt_induced_alpha_powerpluslog.py

**Path:** `consolidation_project/new_alpha_derivations/ubt_induced_alpha_powerpluslog.py`

**Comment:** SPDX-License-Identifier: CC-BY-4.0 Copyright (c) 2025 David Jaroš This file is part of the Unified Biquaternion Theory project. Licensed under Creativ

---

### Directory: `consolidation_project/scripts/`

#### biquaternion_vs_complex_time_analysis.py

**Path:** `consolidation_project/scripts/biquaternion_vs_complex_time_analysis.py`

**Description:** Biquaternion Time vs Complex Time Analysis for UBT

---

#### fix_latex_preambles.py

**Path:** `consolidation_project/scripts/fix_latex_preambles.py`

**Description:** Fix LaTeX consolidation_project so it compiles without a build/ mirror.

---

#### holographic_verlinde_desitter_derivations.py

**Path:** `consolidation_project/scripts/holographic_verlinde_desitter_derivations.py`

**Description:** Rigorous Computational Derivations for UBT Connections to:

---

#### tag_speculative_headers.py

**Path:** `consolidation_project/scripts/tag_speculative_headers.py`

**Description:** Insert a SPECULATIVE header into LaTeX files listed in MANIFEST_SPECULATIVE.txt.

---

#### verify_biquaternion_inner_product.py

**Path:** `consolidation_project/scripts/verify_biquaternion_inner_product.py`

**Description:** Symbolic verification of biquaternionic inner product properties.

---

#### verify_integration_measure.py

**Path:** `consolidation_project/scripts/verify_integration_measure.py`

**Description:** Integration Measure and Volume Form - Mathematical Verification Script

---

#### verify_lorentz_in_HC.py

**Path:** `consolidation_project/scripts/verify_lorentz_in_HC.py`

**Description:** Verification script for Lorentz structure in complexified quaternions H_C.

---

### Directory: `consolidation_project/scripts/padic/`

#### alpha_p_computation.py

**Path:** `consolidation_project/scripts/padic/alpha_p_computation.py`

**Comment:** SPDX-License-Identifier: CC-BY-4.0 Copyright (c) 2025 David Jaroš This file is part of the Unified Biquaternion Theory project. Licensed under Creativ

---

### Directory: `insensitivity/`

#### observables.py

**Path:** `insensitivity/observables.py`

**Comment:** insensitivity/observables.py

---

#### sweep.py

**Path:** `insensitivity/sweep.py`

**Comment:** insensitivity/sweep.py

**Features:** Generates CSV

---

### Directory: `insensitivity/tests/`

#### test_insensitivity.py

**Path:** `insensitivity/tests/test_insensitivity.py`

**Comment:** insensitivity/tests/test_insensitivity.py

**Features:** Reads CSV

---

### Directory: `p_universes/`

#### sector_ff.py

**Path:** `p_universes/sector_ff.py`

**Comment:** p_universes/sector_ff.py SPDX-License-Identifier: MIT

---

### Directory: `scripts/`

#### analyze_cmb_power_spectrum.py

**Path:** `scripts/analyze_cmb_power_spectrum.py`

**Description:** UBT Data Analysis Suite - Cosmic Microwave Background

---

#### analyze_dark_matter_limits.py

**Path:** `scripts/analyze_dark_matter_limits.py`

**Description:** UBT Data Analysis Suite - Dark Matter Direct Detection

---

#### dimensional_lint.py

**Path:** `scripts/dimensional_lint.py`

**Description:** Dimensional Consistency Linter for UBT LaTeX Files

---

#### emergent_alpha_calculator.py

**Path:** `scripts/emergent_alpha_calculator.py`

**Description:** Emergent Alpha Constant Calculator

---

#### fit_flavour_minimal.py

**Path:** `scripts/fit_flavour_minimal.py`

**Description:** UBT Flavor Fitting - Minimal Texture Parameter Optimization

---

#### lint_complex_time_usage.py

**Path:** `scripts/lint_complex_time_usage.py`

**Description:** Lint Complex Time Usage in UBT LaTeX Files

---

#### padic_alpha_calculator.py

**Path:** `scripts/padic_alpha_calculator.py`

**Description:** P-adic Alpha Constant Calculator for Alternate Realities

---

#### demo_padic_alpha.py

**Path:** `scripts/demo_padic_alpha.py`

**Description:** Validation Tests for P-adic Alpha Derivation

---

#### demo_symbolic_alpha.py

**Path:** `scripts/demo_symbolic_alpha.py`

**Description:** Symbolic Alpha Derivation Tests

---

#### ubt_complete_fermion_derivation.py

**Path:** `scripts/ubt_complete_fermion_derivation.py`

**Description:** Complete UBT Fermion Mass Calculator: All 12 Fermions

---

#### ubt_fermion_mass_calculator.py

**Path:** `scripts/ubt_fermion_mass_calculator.py`

**Description:** UBT Fermion Mass Calculator from First Principles

---

#### ubt_neutrino_mass_derivation.py

**Path:** `scripts/ubt_neutrino_mass_derivation.py`

**Description:** UBT Neutrino Mass Derivation: See-Saw Mechanism in Complex Time

---

#### ubt_quark_mass_derivation.py

**Path:** `scripts/ubt_quark_mass_derivation.py`

**Description:** UBT Quark Mass Derivation from First Principles

---

#### ubt_quark_mass_optimization.py

**Path:** `scripts/ubt_quark_mass_optimization.py`

**Description:** UBT Quark Mass Optimization: Discrete Mode Search

---

#### ubt_rge.py

**Path:** `scripts/ubt_rge.py`

**Description:** UBT RGE Runner - Renormalization Group Evolution for Fermion Masses

---

#### validate_biquaternion_definitions.py

**Path:** `scripts/validate_biquaternion_definitions.py`

**Description:** Comprehensive Validation of Biquaternion Definitions in UBT

---

#### validate_electron_mass.py

**Path:** `scripts/validate_electron_mass.py`

**Description:** Electron Mass Validation Script

---

#### validate_projection_mechanisms.py

**Path:** `scripts/validate_projection_mechanisms.py`

**Description:** Validation of Projection Mechanisms from Biquaternionic Manifold to 4D Spacetime

---

#### validate_ubt_derivations_symbolic.py

**Path:** `scripts/validate_ubt_derivations_symbolic.py`

**Description:** Symbolic Validation of Key UBT Derivations

---

#### verify_B_integral.py

**Path:** `scripts/verify_B_integral.py`

---

### Directory: `tests/`

#### test_alpha_export_runs.py

**Path:** `tests/test_alpha_export_runs.py`

**Comment:** tests/test_alpha_export_runs.py

---

#### test_alpha_provenance.py

**Path:** `tests/test_alpha_provenance.py`

**Description:** Test: Alpha Provenance

---

#### test_audit_computed_not_reference.py

**Path:** `tests/test_audit_computed_not_reference.py`

**Comment:** tests/test_audit_computed_not_reference.py (v2)

---

#### test_docs_use_generated_csv.py

**Path:** `tests/test_docs_use_generated_csv.py`

**Description:** Test: Documents Use Generated CSV

**Features:** Reads CSV

---

#### test_electron_mass.py

**Path:** `tests/test_electron_mass.py`

**Description:** Electron Mass Tests - Fit-Free, Metrology-Grade

---

#### test_electron_mass_precision.py

**Path:** `tests/test_electron_mass_precision.py`

**Description:** Test: Electron Mass Precision

---

#### test_electron_sensitivity.py

**Path:** `tests/test_electron_sensitivity.py`

**Description:** Test: Electron Mass Sensitivity to Alpha

---

#### test_no_circularity.py

**Path:** `tests/test_no_circularity.py`

**Description:** Test No-Circularity in UBT Fermion Mass Derivation

---

#### test_no_core_hardcoded_after_snippets.py

**Path:** `tests/test_no_core_hardcoded_after_snippets.py`

**Comment:** tests/test_no_core_hardcoded_after_snippets.py

---

#### test_no_hardcoded_constants.py

**Path:** `tests/test_no_hardcoded_constants.py`

**Description:** Test: No Hard-Coded Constants

---

#### test_qed_limit.py

**Path:** `tests/test_qed_limit.py`

**Description:** Test QED Limit Continuity for CT Scheme

---

#### test_scheme_independence.py

**Path:** `tests/test_scheme_independence.py`

**Description:** Test Scheme Independence for B Parameter

---

#### test_texture_predictions.py

**Path:** `tests/test_texture_predictions.py`

**Description:** Test Texture Predictions in UBT Fermion Mass Framework

---

#### test_ward_id.py

**Path:** `tests/test_ward_id.py`

**Description:** Test Ward Identity Z1 = Z2 in CT Scheme

---

### Directory: `tools/`

#### alpha_audit.py

**Path:** `tools/alpha_audit.py`

**Description:** Alpha Audit Tool - Repository Scanner

---

#### apply_alpha_forwarder_patch.py

**Path:** `tools/apply_alpha_forwarder_patch.py`

**Description:** apply_alpha_forwarder_patch.py

---

#### audit_computed_not_reference.py

**Path:** `tools/audit_computed_not_reference.py`

**Description:** Audit v2: verify that LaTeX/docs present computed (pipeline-derived) values,

---

#### dependency_scan.py

**Path:** `tools/dependency_scan.py`

**Description:** Dependency Scanner - Build Symbol Dependency Graph

---

#### fill_checklist.py

**Path:** `tools/fill_checklist.py`

**Description:** Fill Alpha Checklist

---

#### generate_tex_snippets_from_csv.py

**Path:** `tools/generate_tex_snippets_from_csv.py`

**Description:** generate_tex_snippets_from_csv.py

**Features:** Reads CSV

---

#### install_two_loop_core.py

**Path:** `tools/install_two_loop_core.py`

**Description:** install_two_loop_core.py

---

#### latex_extract.py

**Path:** `tools/latex_extract.py`

**Description:** LaTeX Equation Extractor

---

#### replace_core_literals_with_macros.py

**Path:** `tools/replace_core_literals_with_macros.py`

**Description:** replace_core_literals_with_macros.py

---

### Directory: `tools/validation/`

#### alpha_symbolic_verification.py

**Path:** `tools/validation/alpha_symbolic_verification.py`

**Description:** UBT Alpha Derivation Symbolic Verification

---

### Directory: `ubt_audit_pack_v1/tests/`

#### test_audit_computed_not_reference.py

**Path:** `ubt_audit_pack_v1/tests/test_audit_computed_not_reference.py`

**Comment:** tests/test_audit_computed_not_reference.py Thin pytest wrapper that invokes the standalone auditor.

---

### Directory: `ubt_audit_pack_v1/tools/`

#### audit_computed_not_reference.py

**Path:** `ubt_audit_pack_v1/tools/audit_computed_not_reference.py`

**Description:** Audit: verify that LaTeX docs and code present computed (pipeline-derived) values,

---

### Directory: `ubt_audit_pack_v2/tests/`

#### test_audit_computed_not_reference.py

**Path:** `ubt_audit_pack_v2/tests/test_audit_computed_not_reference.py`

**Comment:** tests/test_audit_computed_not_reference.py (v2)

---

### Directory: `ubt_audit_pack_v2/tools/`

#### audit_computed_not_reference.py

**Path:** `ubt_audit_pack_v2/tools/audit_computed_not_reference.py`

**Description:** Audit v2: verify that LaTeX/docs present computed (pipeline-derived) values,

---

### Directory: `ubt_masses/`

#### __init__.py

**Path:** `ubt_masses/__init__.py`

**Description:** UBT Masses Package

---

#### core.py

**Path:** `ubt_masses/core.py`

**Description:** Core UBT Mass Calculations

---

#### export_leptons_csv.py

**Path:** `ubt_masses/export_leptons_csv.py`

**Description:** Export Lepton Masses to CSV

**Features:** Generates CSV

---

#### qed.py

**Path:** `ubt_masses/qed.py`

**Description:** QED Pole Mass Conversion

---

### Directory: `unified_biquaternion_theory/solution_P4_fine_structure_constant/`

#### alpha_running_calculator.py

**Path:** `unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_running_calculator.py`

**Comment:** SPDX-License-Identifier: CC-BY-4.0 Copyright (c) 2025 David Jaroš This file is part of the Unified Biquaternion Theory project. Licensed under Creativ

---

### Directory: `unified_biquaternion_theory/validation/`

#### validate_GR_recovery.py

**Path:** `unified_biquaternion_theory/validation/validate_GR_recovery.py`

**Description:** Validation of General Relativity Recovery from UBT Theta Field

---

#### validate_alpha_constant.py

**Path:** `unified_biquaternion_theory/validation/validate_alpha_constant.py`

**Description:** Validation of Fine Structure Constant (α) Derivation from UBT First Principles

---

#### validate_electron_mass.py

**Path:** `unified_biquaternion_theory/validation/validate_electron_mass.py`

**Description:** Validation of Electron Mass Derivation from UBT First Principles

---

#### validate_extended_GR.py

**Path:** `unified_biquaternion_theory/validation/validate_extended_GR.py`

**Description:** Validation of Extended GR: Phase Curvature and Antigravity Predictions

---

