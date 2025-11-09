# tests/test_no_hardcoded_constants.py
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
GLOBS = ["**/*.tex", "**/*.md", "**/*.py"]

PATTERNS = [
    r"137\.0359990\d+",        # alpha^{-1} precise value
    r"\b0\.5109989\d{2,}\b",   # m_e ~ 0.51099895...
    r"\b105\.6583\d{2,}\b",    # m_mu ~ 105.658375...
    r"\b1776\.8\d{2,}\b",      # m_tau ~ 1776.86...
]

WHITELIST = {
    "UBT_alpha_per_sector_patch.tex",   # allow in generated TeX only
    # add other generated artefacts if needed, e.g., "tex/generated/constants.tex"
}

def iter_files():
    for g in GLOBS:
        for p in ROOT.glob(g):
            if not p.is_file():
                continue
            if p.name in WHITELIST:
                continue
            if any(seg in p.parts for seg in (".git", ".venv", "venv", "build", "dist", "_build")):
                continue
            yield p

def test_no_magic_constants_in_source():
    bad = []
    for p in iter_files():
        text = p.read_text(errors="ignore")
        for rgx in PATTERNS:
            if re.search(rgx, text):
                bad.append((str(p), rgx))
    assert not bad, "Hard-coded constants found:\n" + "\n".join(f"{f} :: {pat}" for f, pat in bad)
