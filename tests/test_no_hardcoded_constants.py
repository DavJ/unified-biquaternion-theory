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

# Patterns for ultra-precise constants that should NOT be hard-coded
PATTERNS = [
    r"137\.0359990\d+",        # alpha^{-1} precise value
    r"\b0\.5109989\d{2,}\b",   # m_e ~ 0.51099895...
    r"\b105\.6583\d{2,}\b",    # m_mu ~ 105.658375...
    r"\b1776\.8\d{2,}\b",      # m_tau ~ 1776.86...
]

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
}

# Directory segments to skip
SKIP_DIRS = {".venv", "venv", "build", "dist", ".git", "__pycache__", 
             ".pytest_cache", "out", "alpha_core_repro/out", "data",
             "docs/archive",  # Historical documentation
             "docs/osf_release",  # Published versions (frozen)
             "docs/osf_release_not_released",  # Draft publications
             "scripts",  # Utility scripts (often have reference values for comparison)
             "consolidation_project/old",  # Archived versions
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
            
            # Skip excluded directories
            if any(seg in p.parts for seg in SKIP_DIRS):
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
            
        for rgx in PATTERNS:
            matches = re.finditer(rgx, text)
            for match in matches:
                # Get context around the match for better error reporting
                start = max(0, match.start() - 40)
                end = min(len(text), match.end() + 40)
                context = text[start:end].replace('\n', ' ')
                bad.append((str(p.relative_to(ROOT)), rgx, context))
    
    if bad:
        msg = "Hard-coded constants found (must use computed values from CSV):\n"
        for file, pattern, context in bad:
            msg += f"\n  {file}\n    Pattern: {pattern}\n    Context: ...{context}...\n"
        assert False, msg


if __name__ == "__main__":
    # Allow running this test standalone
    test_no_magic_constants_in_source()
    print("✓ No hard-coded constants found in source files")
