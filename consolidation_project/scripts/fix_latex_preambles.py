#!/usr/bin/env python3
"""
Fix LaTeX consolidation_project so it compiles without a build/ mirror.

Actions:
1) Strip preambles from appendix_*.tex (remove \documentclass, and content before \begin{document}; remove content after \end{document}).
2) In appendix_T_theta_resonator_experiments.tex, comment out missing \input{appendix_E_theta_resonator_experiments.tex} if present.
Safe: creates .bak backups once.
"""
import re, os, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

def strip_preamble(tex: str) -> str:
    start = re.search(r"\\begin{document}", tex)
    if start: tex = tex[start.end():]
    end = re.search(r"\\end{document}", tex)
    if end: tex = tex[:end.start()]
    return tex.strip() + "\n"

changed = []

for p in ROOT.glob("appendix_*.tex"):
    t = p.read_text(encoding="utf-8", errors="ignore")
    if "\\documentclass" in t or "\\begin{document}" in t or "\\end{document}" in t:
        cleaned = strip_preamble(t)
        bak = p.with_suffix(p.suffix + ".bak")
        if not bak.exists():
            bak.write_text(t, encoding="utf-8")
        p.write_text(cleaned, encoding="utf-8")
        changed.append(p.name)

tfile = ROOT / "appendix_T_theta_resonator_experiments.tex"
if tfile.exists():
    tt = tfile.read_text(encoding="utf-8", errors="ignore")
    target = "\\input{appendix_E_theta_resonator_experiments.tex}"
    if target in tt:
        tt = tt.replace(target, "% NOTE: Missing file removed to allow build.\n% " + target)
        tfile.write_text(tt, encoding="utf-8")
        changed.append(tfile.name + " (removed missing include)")

print("Modified files:", ", ".join(changed) if changed else "(none)")
print("Done.")
