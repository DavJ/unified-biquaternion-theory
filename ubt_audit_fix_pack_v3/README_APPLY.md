# UBT Audit Fix Pack v3

This pack helps you eliminate remaining **FATAL** issues from the audit:
- generate macros from CSV (`tex/snippets_generated.tex`)
- replace precise literals in core `.tex` with those macros
- provide a pytest guard to keep them out

## Steps

1) **Generate α grid CSV** (if missing)
```bash
export PYTHONPATH="$(pwd):$PYTHONPATH"
python -m alpha_core_repro.export_alpha_csv
# should create data/alpha_two_loop_grid.csv
```

2) **Optional**: ensure `data/leptons.csv` exists (electron/muon/tau).

3) **Create LaTeX macros from CSV**
```bash
python tools/generate_tex_snippets_from_csv.py
# writes tex/snippets_generated.tex with \AlphaInvBest, \ElectronMassMeV, ...
```

4) **Replace hard-coded literals in core `.tex`**
```bash
# dry run (shows which files would be touched)
python tools/replace_core_literals_with_macros.py --root .

# apply changes
python tools/replace_core_literals_with_macros.py --root . --apply
```

This also injects `\input{tex/snippets_generated.tex}` into `emergent_alpha_from_ubt.tex` if missing.

5) **Re-run audit**
```bash
python tools/audit_computed_not_reference.py --root .
# should PASS or only WARN for non-core files
```

6) **CI guard**
```bash
pytest -q tests/test_no_core_hardcoded_after_snippets.py
```

**Note**: The replacement patterns are conservative. If you keep a precise number in a math discussion doc, move it to a `docs/` or `archive/` path (WARN). Core derivation `.tex` should always reference macros or CSV tables.
