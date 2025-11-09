import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
MASSES_DIR = ROOT / "masses"
BAD = re.compile(r"\b(TODO|placeholder|pending)\b", re.I)

def test_no_placeholders_in_masses_docs():
    """Ensure masses documentation contains no TODO/placeholder/pending markers."""
    for name in ["yukawa_in_HC.tex", "ct_two_loop_renorm.tex", "sum_rules_and_ratios.tex", "absolute_scale_anchor.tex"]:
        filepath = MASSES_DIR / name
        assert filepath.exists(), f"Missing masses doc: {name}"
        
        txt = filepath.read_text(encoding="utf-8", errors="ignore")
        match = BAD.search(txt)
        assert not match, f"Remove placeholders from masses doc: {name} (found: {match.group()})"
