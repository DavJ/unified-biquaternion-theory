# UBT Fix Pack — v2 (with dynamic shim)

## What changed vs v1
- Added `alpha_core_repro/two_loop.py` **dynamic shim** that tries multiple import paths to find
  `alpha_from_ubt_two_loop_strict` in your repo.
- Added `alpha_core_repro/__init__.py` so Python treats the folder as a package.

## Quick usage
```bash
# from repo root
rsync -av ubt_fix_pack_v2/ ./
export PYTHONPATH="$(pwd):$PYTHONPATH"

# generate alpha CSV
python -m alpha_core_repro.export_alpha_csv
# or (if you prefer direct path)
python ubt_fix_pack_v2/alpha_core_repro/export_alpha_csv.py
```

If it still says it can't find the provider, locate it with:
```bash
rg -n "def alpha_from_ubt_two_loop_strict" -g '!venv' -g '!*build*' -g '!*.ipynb_checkpoints*'
# or:
git grep -n "def alpha_from_ubt_two_loop_strict"
```
Then add the discovered module path into `_CANDIDATES` inside `alpha_core_repro/two_loop.py`.

Finally add to your TeX (once) to show CSV-fed values:
```tex
\input{tex/snippets_insert.tex}
```
and build:
```bash
latexmk -pdf emergent_alpha_from_ubt.tex
```
