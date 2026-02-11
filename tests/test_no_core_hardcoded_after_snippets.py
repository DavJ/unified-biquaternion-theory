# tests/test_no_core_hardcoded_after_snippets.py
import re, pathlib

FATAL_PATTERNS = [
    r"137\.0359990\d+",
    r"\b0\.5109989\d{2,}\b",
    r"\b105\.6583\d{2,}\b",
    r"\b1776\.8\d{2,}\b",
]

def is_core_tex(p: pathlib.Path) -> bool:
    parts = set(p.parts)
    # Exclude build/tooling directories
    if any(seg in parts for seg in (".git","venv",".venv","build","dist","_build","__pycache__","tools","tests","scripts","validation","docs","archive","reports")):
        return False
    # Exclude speculative and auxiliary content (not canonical)
    if any(seg in parts for seg in ("speculative_extensions","speculative","appendices","notes","drafts")):
        return False
    return p.suffix.lower() == ".tex"

def test_no_fatal_literals_in_core_tex():
    root = pathlib.Path(__file__).resolve().parents[1]
    problems = []
    for p in root.rglob("*.tex"):
        if not is_core_tex(p):
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for pat in FATAL_PATTERNS:
            if re.search(pat, txt):
                problems.append((str(p), pat))
    assert not problems, f"Hard-coded precise constants remain in core TeX: {problems}"
