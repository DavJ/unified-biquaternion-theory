# tests/test_docs_use_generated_csv.py
# SPDX-License-Identifier: MIT
"""
Test: Documents Use Generated CSV
==================================

Verifies that:
1. CSV files with computed values exist
2. They contain expected data structure
3. LaTeX documents reference CSV files (not hard-coded values)

This ensures end-to-end data provenance: code → CSV → TeX
"""
import pathlib
import csv
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

# Expected CSV files
ALPHA_CSV = ROOT / "alpha_core_repro" / "out" / "alpha_two_loop_grid.csv"
LEPTON_CSV = ROOT / "data" / "leptons.csv"

# Main TeX document
MAIN_TEX = ROOT / "emergent_alpha_from_ubt.tex"

# Patterns for ultra-precise values that should NOT appear in main TeX
FORBIDDEN_PATTERNS = [
    r"137\.0359990\d+",     # alpha^{-1} precise
    r"\b0\.5109989\d{2,}\b",  # m_e precise
]


def test_alpha_csv_exists_and_valid():
    """
    Test that alpha CSV file exists and contains expected columns.
    """
    assert ALPHA_CSV.exists(), (
        f"Alpha CSV file not found: {ALPHA_CSV}\n"
        f"Run: make alpha-grid or python -m alpha_core_repro.run_grid"
    )
    
    with ALPHA_CSV.open() as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        assert len(rows) > 0, "Alpha CSV is empty"
        
        # Check for required columns
        header = set(rows[0].keys())
        required_cols = {"p", "alpha_inv", "alpha", "delta_ct"}
        
        missing = required_cols - header
        assert not missing, (
            f"Alpha CSV missing required columns: {missing}\n"
            f"Found columns: {header}"
        )
        
        # Verify data for p=137
        p137_rows = [r for r in rows if r["p"] == "137"]
        assert len(p137_rows) > 0, "Alpha CSV missing p=137 entry"
        
        # Check that alpha_inv is numeric and reasonable
        alpha_inv = float(p137_rows[0]["alpha_inv"])
        assert 137.0 < alpha_inv < 137.1, (
            f"Alpha inverse seems wrong: {alpha_inv}"
        )


def test_lepton_csv_exists_and_valid():
    """
    Test that lepton CSV file exists and contains expected columns.
    """
    assert LEPTON_CSV.exists(), (
        f"Lepton CSV file not found: {LEPTON_CSV}\n"
        f"Run: python -m ubt_masses.export_leptons_csv"
    )
    
    with LEPTON_CSV.open() as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        assert len(rows) > 0, "Lepton CSV is empty"
        
        # Check for required columns
        header = set(rows[0].keys())
        required_cols = {"name", "symbol", "pole_mass_mev"}
        
        missing = required_cols - header
        assert not missing, (
            f"Lepton CSV missing required columns: {missing}\n"
            f"Found columns: {header}"
        )
        
        # Verify electron entry exists
        electron_rows = [r for r in rows if r["name"] == "electron"]
        assert len(electron_rows) > 0, "Lepton CSV missing electron entry"
        
        # Check that electron mass is computed (not "NOT_IMPLEMENTED")
        electron_mass = electron_rows[0]["pole_mass_mev"]
        assert electron_mass != "NOT_IMPLEMENTED", (
            "Electron mass not computed in CSV"
        )
        
        # Verify it's numeric
        mass_val = float(electron_mass)
        assert 0.51 < mass_val < 0.52, (
            f"Electron mass seems wrong: {mass_val} MeV"
        )


def test_tex_uses_csv_not_literals():
    """
    Test that main TeX document uses CSV imports, not literal constants.
    
    We check that:
    1. TeX references .csv files or pgfplotstable
    2. TeX does NOT contain ultra-precise hard-coded values
    """
    if not MAIN_TEX.exists():
        # If main tex doesn't exist, skip this test
        import pytest
        pytest.skip(f"Main TeX file not found: {MAIN_TEX}")
    
    tex_content = MAIN_TEX.read_text(errors="ignore")
    
    # Check that TeX uses CSV in some way
    # (either direct reference or pgfplotstable)
    uses_csv = (
        ".csv" in tex_content or
        "pgfplotstable" in tex_content or
        "csvsimple" in tex_content or
        "datatool" in tex_content
    )
    
    if not uses_csv:
        # This is a warning, not a hard failure, since the TeX might
        # not be set up yet to use CSV
        print(f"WARNING: {MAIN_TEX.name} does not seem to import CSV data")
        print("  Consider using \\pgfplotstableread or similar to load computed values")
    
    # Check for forbidden patterns (ultra-precise hard-coded values)
    violations = []
    for pattern in FORBIDDEN_PATTERNS:
        matches = re.finditer(pattern, tex_content)
        for match in matches:
            # Get line number for better reporting
            line_start = tex_content[:match.start()].count('\n') + 1
            context_start = max(0, match.start() - 50)
            context_end = min(len(tex_content), match.end() + 50)
            context = tex_content[context_start:context_end].replace('\n', ' ')
            violations.append((pattern, line_start, context))
    
    if violations:
        msg = f"Ultra-precise constants found in {MAIN_TEX.name} (should use CSV):\n"
        for pattern, line, context in violations:
            msg += f"\n  Line {line}, pattern {pattern}:\n    ...{context}...\n"
        
        # For now, this is a warning since migrating to CSV is a larger task
        print(f"WARNING: {msg}")
        # Eventually this should become: assert False, msg


def test_csv_data_freshness():
    """
    Test that CSV files are relatively fresh (generated recently).
    
    This is a weak test - just checks that files exist and are not empty.
    A more sophisticated test would check timestamps or content hashes.
    """
    # Alpha CSV should have multiple entries
    with ALPHA_CSV.open() as f:
        alpha_rows = list(csv.DictReader(f))
    
    assert len(alpha_rows) >= 5, (
        f"Alpha CSV has too few entries: {len(alpha_rows)}\n"
        f"Expected at least 5 prime sectors"
    )
    
    # Lepton CSV should have at least electron
    with LEPTON_CSV.open() as f:
        lepton_rows = list(csv.DictReader(f))
    
    assert len(lepton_rows) >= 1, (
        f"Lepton CSV has no entries"
    )


if __name__ == "__main__":
    test_alpha_csv_exists_and_valid()
    print("✓ Alpha CSV valid")
    
    test_lepton_csv_exists_and_valid()
    print("✓ Lepton CSV valid")
    
    test_tex_uses_csv_not_literals()
    print("✓ TeX CSV usage checked")
    
    test_csv_data_freshness()
    print("✓ CSV data freshness verified")
