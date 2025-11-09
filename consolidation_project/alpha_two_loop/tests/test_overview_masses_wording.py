import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
ov = (ROOT/"OVERVIEW.md").read_text(encoding="utf-8", errors="ignore").lower()

def test_overview_acknowledges_masses_not_derived():
    assert "masses" in ov and ("not yet derived" in ov or "not yet from first principles" in ov), \
        "OVERVIEW should state clearly that fermion masses are not yet derived from first UBT principles."

def test_overview_no_fitted_param_for_me():
    # Should NOT claim electron mass was derived FROM a fitted parameter
    # Look for patterns that suggest it WAS fitted (not "not fitted")
    # Positive assertions like "fitted", "from fitted", etc. without "not" prefix
    bad = re.search(r"electron mass[^n]*\b(formula coefficients fitted|derived.*fitted|computed.*fitted parameter[^s])", ov)
    if not bad:
        # Also check for old caveat pattern
        bad = re.search(r"\*\*caveat:\*\*.*formula coefficients fitted", ov)
    assert not bad, "Remove/replace claim that electron mass was computed using a fitted parameter."
