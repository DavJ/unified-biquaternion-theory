# tests/test_docs_use_generated_csv.py
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
MAIN_TEX = ROOT / "emergent_alpha_from_ubt.tex"
ALPHA_CSV = ROOT / "data" / "alpha_two_loop_grid.csv"
LEPTON_CSV = ROOT / "data" / "leptons.csv"

def test_tex_reads_values_from_csv_and_not_literal():
    assert MAIN_TEX.exists(), "Main TeX not found"
    assert ALPHA_CSV.exists(), "alpha CSV not found (run exporter)"
    assert LEPTON_CSV.exists(), "lepton CSV not found"

    tex = MAIN_TEX.read_text(errors="ignore")
    # must reference CSV and/or pgfplotstable
    assert ".csv" in tex or "pgfplotstable" in tex, "TeX should import data tables from CSV, not literals"
    # forbid ultraprecise literals directly in main TeX
    for pat in (r"137\.0359990\d+", r"\b0\.5109989\d{2,}\b"):
        assert not re.search(pat, tex), "Literal alpha/m_e found in TeX; embed via CSV+pgfplotstable"
