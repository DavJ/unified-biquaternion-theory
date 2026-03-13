#!/usr/bin/env python3
"""
replace_core_literals_with_macros.py
Scans core .tex files for precise literals (alpha^{-1}, lepton masses) and replaces them by macros
defined in tex/snippets_generated.tex. Dry-run by default; use --apply to write changes.

Patterns replaced:
  137.0359990...     -> \AlphaInvBest
  0.51099895...      -> \ElectronMassMeV
  105.658375...      -> \MuonMassMeV
  1776.86...         -> \TauMassMeV

Usage:
  python tools/replace_core_literals_with_macros.py --root . [--apply]
"""
from __future__ import annotations
import re, sys, argparse
from pathlib import Path

PATTERNS = [
    (re.compile(r"137\.0359990\d+"), r"\\AlphaInvBest"),
    (re.compile(r"\b0\.5109989\d+"), r"\\ElectronMassMeV"),
    (re.compile(r"\b105\.6583\d+"), r"\\MuonMassMeV"),
    (re.compile(r"\b1776\.8\d+"), r"\\TauMassMeV"),
]

def is_core_tex(p: Path) -> bool:
    parts = set(p.parts)
    if any(seg in parts for seg in (".git","venv",".venv","build","dist","_build","__pycache__","tools","tests","scripts","validation","docs","archive","reports")):
        return False
    return p.suffix.lower() == ".tex"

def process_file(p: Path, apply: bool) -> int:
    s = p.read_text(encoding="utf-8", errors="ignore")
    orig = s
    for rgx, repl in PATTERNS:
        s = rgx.sub(repl, s)
    if s != orig:
        if apply:
            p.write_text(s, encoding="utf-8")
            print(f"[write] {p}")
        else:
            print(f"[diff] {p}")
            # minimal unified diff-like preview
            print("  ...replacements made (use --apply to write)")
        return 1
    return 0

def ensure_input_snippet(root: Path, apply: bool) -> None:
    # insert \input{tex/snippets_generated.tex} near top of main TeX if missing
    main = root / "emergent_alpha_from_ubt.tex"
    if not main.exists():
        return
    t = main.read_text(encoding="utf-8")
    if "\\input{tex/snippets_generated.tex}" in t:
        return
    insert_after = "\\begin{document}"
    idx = t.find(insert_after)
    ins = "\n% auto: macros from CSV\n\\input{tex/snippets_generated.tex}\n"
    if idx >= 0:
        new = t[:idx+len(insert_after)] + ins + t[idx+len(insert_after):]
    else:
        new = t + ins
    if apply:
        main.write_text(new, encoding="utf-8")
        print(f"[write] injected \\input{{tex/snippets_generated.tex}} into {main}")
    else:
        print(f"[plan] would inject \\input{{tex/snippets_generated.tex}} into {main}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root")
    ap.add_argument("--apply", action="store_true", help="Write changes")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    ensure_input_snippet(root, args.apply)

    changed = 0
    for p in root.rglob("*.tex"):
        if not is_core_tex(p):
            continue
        changed += process_file(p, args.apply)

    print(f"[summary] files touched: {changed} (apply={args.apply})")
    if not args.apply and changed > 0:
        print("Re-run with --apply to write changes.")

if __name__ == "__main__":
    main()
