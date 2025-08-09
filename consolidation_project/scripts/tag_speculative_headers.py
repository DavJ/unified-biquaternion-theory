#!/usr/bin/env python3
"""
Insert a SPECULATIVE header into LaTeX files listed in MANIFEST_SPECULATIVE.txt.
Safe: creates .bak backups.
"""
import sys, os, io

root = os.path.dirname(os.path.dirname(__file__))
spec_list = os.path.join(root, "MANIFEST_SPECULATIVE.txt")

header = (
    "%% ================================================\n"
    "%% SPECULATIVE / WIP SECTION — NOT PART OF CORE\n"
    "%% Do not cite as established results.\n"
    "%% ================================================\n"
)

with open(spec_list, "r", encoding="utf-8") as f:
    files = [line.strip() for line in f if line.strip() and not line.startswith("#")]

for rel in files:
    path = os.path.join(root, rel)
    if not os.path.isfile(path):
        print(f"[WARN] Missing: {rel}")
        continue
    with open(path, "r", encoding="utf-8") as fr:
        content = fr.read()
    if "SPECULATIVE / WIP SECTION" in content:
        print(f"[SKIP] Already tagged: {rel}")
        continue
    with open(path + ".bak", "w", encoding="utf-8") as fb:
        fb.write(content)
    with open(path, "w", encoding="utf-8") as fw:
        fw.write(header + content)
    print(f"[OK] Tagged: {rel}")
