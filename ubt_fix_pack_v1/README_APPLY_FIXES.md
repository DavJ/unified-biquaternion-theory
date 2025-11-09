# UBT Fix Pack — Computed‑not‑Hardcoded

This pack provides:
- `alpha_core_repro/export_alpha_csv.py` — exports strict two‑loop alpha grid to `data/alpha_two_loop_grid.csv`
- `tests/*` — tests proving we present computed, not hard‑coded data
- `tex/snippets_insert.tex` — TeX snippet to include CSV tables in the paper

## How to apply

1. Copy the contents of this ZIP to the **root** of your UBT repo (it won't overwrite existing files).
2. Generate alpha CSV:
   ```bash
   python -m alpha_core_repro.export_alpha_csv
   ```
   You should now have `data/alpha_two_loop_grid.csv`.
3. In `emergent_alpha_from_ubt.tex`, add near the end (or where suitable):
   ```tex
   \input{tex/snippets_insert.tex}
   ```
   Ensure you have:
   ```tex
   \usepackage{pgfplotstable}
   \usepackage{booktabs}
   ```
4. Run tests:
   ```bash
   pytest -q
   ```
5. Build the PDF:
   ```bash
   latexmk -pdf emergent_alpha_from_ubt.tex
   ```

## Notes
- If your pipeline generates a different CSV path or column names, adjust the snippet and tests accordingly.
- Tighten `tests/test_electron_mass_precision.py` tolerance to `1e-5` once you add the 2‑loop QED conversion for pole ↔ MSbar.
- Whitelist only **generated** TeX artefacts in `test_no_hardcoded_constants.py`.
