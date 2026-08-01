# tests/test_no_hardcoded_constants.py
# SPDX-License-Identifier: MIT
"""
Test: No Hard-Coded Constants
==============================

Ensures that precise values for α^{-1}, m_e, m_μ, m_τ are NOT hard-coded
in source files. All values must be computed or loaded from generated CSV.

This test scans .tex, .md, and .py files for patterns matching ultra-precise
constants that should only appear in generated/output files, not source code.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
GLOBS = ["**/*.tex", "**/*.md", "**/*.py"]

# Patterns for ultra-precise constants that should NOT be hard-coded.
# The alpha pattern intentionally covers both CODATA 2018 (137.035999084)
# and CODATA 2022 (137.035999177), rather than baking in one edition digit.
PATTERNS = {
    "alpha_inv": r"\b137\.03599\d{4,}\b",
    "electron_mass_mev": r"\b0\.5109989\d{2,}\b",
    "muon_mass_mev": r"\b105\.6583\d{2,}\b",
    "tau_mass_mev": r"\b1776\.8\d{2,}\b",
}

# Existing active documents and comparison utilities that intentionally quote a
# CODATA alpha^{-1} value. Exemptions are exact repository-relative paths so a
# same-named file elsewhere is not silently exempted. New files must either load
# the provenance-tracked reference data or be added here with review.
ALPHA_REFERENCE_ALLOWLIST = {
    # Submission/status ledgers and provenance documentation.
    "STATUS_OF_UBT.md": "status ledger comparison value",
    "WHAT_IS_PROVED.md": "proved-claims comparison value",
    "PATCH_NOTES_ALPHA_LAYER2_PROJECTION.md": "historical patch note",
    "PATCH_NOTES_ALPHA_LAYER2_KERNEL_REFINEMENT.md": "historical patch note",
    "docs/UBT_MAP.md": "repository map comparison value",
    "docs/ALPHA_FROM_ME_ANALYSIS.md": "analysis comparison value",
    "docs/PROOFKIT_ALPHA.md": "proof-kit comparison value",
    "docs/PROVENANCE_TESTS_README.md": "provenance-test documentation",
    "docs/predictions/experimental_tests.md": "experimental comparison value",
    # Active TeX derivations that visibly compare their result with CODATA.
    "speculative_extensions/prime_resonance_channels/prime_resonance_channels.tex": "explicit comparison in speculative derivation",
    "docs/papers/papers/generated/ubt_action_and_alpha.tex": "generated derivation comparison",
    "research_tracks/EW/ew_final_status_note.tex": "status comparison",
    "research_tracks/EW/lepton_mass_ratios_ubt.tex": "comparison input",
    "research_tracks/BRIDGE_CLOSURE/B2_alpha_layer2_bridge_status.tex": "bridge-status comparison",
    "research_tracks/BRIDGE_CLOSURE/G137B_AUDIT/A4_su2_twist_uniqueness_theorem.tex": "audit comparison",
    "research_tracks/BRIDGE_CLOSURE/G137B_AUDIT/G137B_full_closure.tex": "audit comparison",
    "research_tracks/T3_ALPHA/alpha_weinberg_final_status.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/em_modular_coupling_identification.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/alpha_conditions_closure.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/alpha_final_closure.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/information_loss_alpha_self_consistency.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/alpha_bridge_b1_closure.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/layer2_kernel_derivation.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/alpha_derivation_complete.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/gap_A_proof.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/alpha_l1_proof.tex": "alpha-track comparison",
    "research_tracks/T3_ALPHA/gap_A_rho_derivation.tex": "alpha-track comparison",
    # Comparison-only numerical utilities. These are not derivation inputs.
    "tools/verify_qed_phi_const.py": "CODATA comparison utility",
    "tools/compute_dalpha_dphi.py": "CODATA comparison and plot reference",
    "tools/alpha_selfconsistency.py": "calibrated comparison utility",
    "tools/compute_h_munu_vacuum.py": "CODATA comparison utility",
    "tools/m0_from_torus.py": "CODATA comparison utility",
    "experiments/constants_derivation/derive_fine_structure.py": "comparison/export only; excluded from derivation chain",
    "experiments/alpha_information_loss/reproduce_info_loss_alpha.py": "reproduction comparison target",
}

PATTERN_PATH_ALLOWLIST = {
    "alpha_inv": ALPHA_REFERENCE_ALLOWLIST,
}

# Files that are allowed to contain these values (generated files, etc.)
WHITELIST = {
    "UBT_alpha_per_sector_patch.tex",   # Generated TeX patch file
    "alpha_two_loop_grid.csv",           # Generated CSV output
    "leptons.csv",                       # Generated lepton mass CSV
    "test_no_hardcoded_constants.py",    # This test file (contains patterns)
    "test_electron_mass_precision.py",   # Contains reference values
    # Legacy/documentation files (for comparison with experimental values)
    "emergent_alpha_executive_summary.tex",
    "emergent_alpha_from_ubt.tex",       # Main TeX document (will migrate to CSV)
    "UBT_HeckeWorlds_theta_zeta_primes_appendix.tex",
    "emergent_alpha_calculations.tex",
    "alpha_final_derivation.tex",
    "fermion_mass_derivation_complete.tex",
    "appendix_K2_fundamental_constants_consolidated.tex",
    "appendix_K_fundamental_constants_consolidated.tex",
    "appendix_N_mass_predictions_consolidated.tex",
    "appendix_ALPHA_torus_theta.tex",  # Appendix with experimental comparison
    "ubt_alpha_noncommutative_renormalization.tex",  # Contains experimental comparison
    "appendix_A2_geometrical_derivation_of_fine_structure_constant.tex",  # Contains experimental comparison
    "ubt_osf_publication.tex",
    "final_electron_mass_prediction_UBT.tex",
    "unified_biquaternion_theory.tex",
    "main.tex",
    "validate_alpha_constant.py",
    "validate_electron_mass.py",
    # Tool scripts (contain reference values for replacement/auditing)
    "replace_core_literals_with_macros.py",
    "audit_computed_not_reference.py",
    # Documentation/README files (contain reference values)
    "README.md",
    "OVERVIEW.md",
    "ELECTRON_MASS_IMPLEMENTATION.md",
    "UBT_SCIENTIFIC_RATING_2025.md",
    "UBT_COMPREHENSIVE_REVIEW_DEC_2025.md",
    "UBT_COMPREHENSIVE_REVIEW_DEC_2025_draft.md",
    "UBT_VS_OTHER_THEORIES_COMPARISON.md",
    "GLOSSARY_OF_SYMBOLS.md",
    "FITTED_PARAMETERS.md",
    "TESTABILITY_AND_FALSIFICATION.md",
    "FERMION_MASS_COMPLETE_REPORT.md",
    "EMERGENT_ALPHA_README.md",
    "UBT_REEVALUATION_2025.md",
    "verification_checklist.md",
    "DATA_PROVENANCE.md",  # Contains example CSV outputs
    "PYTHON_SCRIPTS_REPORT.md",  # Documentation of scripts and CSV files
    "PYTHON_SCRIPTS_APPENDIX.md",  # Complete inventory of all scripts
    "CSV_AND_DOCUMENTATION_POLICY.md",  # Policy document explaining CSV usage
    "UBT_VERIFICATION_REPORT.tex",  # Verification document (contains reference values for comparison)
    # Additional audit/summary documents in root
    "HARD_CODE_AUDIT.md",
    "HARD_CODE_AUDIT.txt",
    "N_EFF_32_RESULTS.md",
    "FINAL_SUMMARY.md",
    "ALPHA_DERIVATION_EXPLAINED.md",
    "IMPLEMENTATION_SUMMARY_TORUS_THETA_ALPHA.md",
    "ALPHA_CXH_COMPARISON.md",
    "NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md",
    "VERIFICATION_CHECKLIST_TORUS_THETA_ALPHA.md",
    "VERIFICATION_CHECKLIST.md",    # Docs checklist with experimental comparison values
    "reference_constants.tex",      # TeX file with CODATA reference constants for comparison
    "COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md",
    "APPENDIX_A2_INTEGRATION_SUMMARY.md",
    "SCRIPT_INTEGRATION_REPORT.md",
    "UPDATE_SUMMARY_2025_11_10.md",
    "CALCULATION_STATUS_ANALYSIS.md",
    "TORUS_THETA_ALPHA_REPORT.md",
    "UBT_COPILOT_INSTRUCTIONS.md",  # Reference document with comparison values
    "FILE_REORGANIZATION_2026-01-10.md",  # Documentation of reorganization (contains before/after values)
    "CURRENT_STATUS.md",  # Status document with experimental comparison values
    "generate_reference_constants.py",  # Tool that generates reference constants
    "validate_alpha_renormalization.py",  # Validation script with reference values
    "STATUS_ALPHA.md",  # Status report with experimental comparison values
    "STATUS_THEORY_ASSESSMENT.md",  # Theory assessment with experimental values
    "STATUS_FERMIONS.md",  # Fermion status report with PDG comparison values
    "INTEGRATION_SUMMARY_LEPTON_QUARK_ISSUES.md",  # Integration summary with reference values
    "REVIEW_COMPLETE_ADDRESS_LEPTON_QUARK_ISSUES.md",  # Review document with reference values
    "reproduce_lepton_ratios.py",  # Lepton ratio tool (uses reference masses for comparison)
    "verify_N_eff.py",             # N_eff verification script (uses CODATA α⁻¹ as reference)
}

# Directory segments to skip
SKIP_DIRS = {".venv", "venv", "build", "dist", ".git", "__pycache__", 
             ".pytest_cache", "out", "alpha_core_repro/out", "data",
             "archive",  # Historical documentation (lowercase legacy)
             "ARCHIVE",  # Historical documentation (uppercase current)
             "archived",  # Historical documentation
             "osf_release",  # Published versions (frozen)
             "osf_release_not_released",  # Draft publications
             "scripts",  # Utility scripts (often have reference values for comparison)
             "old",  # Archived versions
             "ubt_strict_fix",  # Audit/fix documentation
             "ubt_strict_minimal",  # Minimal strict implementation
             "ubt_audit_pack_v1",  # Audit documentation
             "ubt_audit_pack_v2",  # Audit documentation
             "ubt_with_chronofactor",  # subpackage / legacy implementation (contains reference values)
             "reports",  # Generated reports and audit results
             "FINGERPRINTS",  # Fingerprint results directory
             "DOCS",  # Documentation directory
}


def iter_files():
    """Iterate over relevant source files, skipping whitelisted and generated files."""
    for g in GLOBS:
        for p in ROOT.glob(g):
            if not p.is_file():
                continue
            
            # Skip whitelisted files
            if p.name in WHITELIST:
                continue
            
            # Skip excluded directories using repository-relative components.
            # Using p.parts directly makes the result depend on the checkout path
            # (for example, every file under /mnt/data would be skipped).
            relative_path = p.relative_to(ROOT)
            if any(seg in relative_path.parts for seg in SKIP_DIRS):
                continue

            yield p


def test_no_magic_constants_in_source():
    """
    Test that ultra-precise constants are not hard-coded in source files.
    
    This ensures data provenance: all precise values must be computed
    from UBT formulas and stored in generated CSV files, not hard-coded.
    """
    bad = []
    
    for p in iter_files():
        try:
            text = p.read_text(errors="ignore")
        except Exception:
            continue
            
        relative_path = p.relative_to(ROOT).as_posix()
        for label, rgx in PATTERNS.items():
            if relative_path in PATTERN_PATH_ALLOWLIST.get(label, {}):
                continue
            matches = re.finditer(rgx, text)
            for match in matches:
                # Get context around the match for better error reporting
                start = max(0, match.start() - 40)
                end = min(len(text), match.end() + 40)
                context = text[start:end].replace('\n', ' ')
                bad.append((relative_path, label, rgx, context))

    if bad:
        msg = "Hard-coded constants found (load provenance data or add an exact reviewed exemption):\n"
        for file, label, pattern, context in bad:
            msg += (
                f"\n  {file}\n"
                f"    Constant: {label}\n"
                f"    Pattern: {pattern}\n"
                f"    Context: ...{context}...\n"
            )
        assert False, msg


def test_alpha_pattern_covers_codata_2018_and_2022():
    """Guard against another silent CODATA-edition regex regression."""
    rgx = PATTERNS["alpha_inv"]
    assert re.search(rgx, "137.035999084")
    assert re.search(rgx, "137.035999177")
    assert re.search(rgx, "137.035999177549")


if __name__ == "__main__":
    # Allow running this test standalone
    test_no_magic_constants_in_source()
    print("✓ No hard-coded constants found in source files")
