# Minimal Patch for `consolidation_project`
**Updated:** 2025-08-09

This small patch fixes LaTeX compilation *in-place* without creating a build mirror.

## Files included
- `consolidation_project/ubt_2_main.tex` — fixed includes (CORE + selective SPECULATIVE + bibliography)
- `consolidation_project/Makefile` — `make all` builds the consolidated main; `make core` builds CORE
- `consolidation_project/scripts/fix_latex_preambles.py` — removes preambles from `appendix_*.tex` so they can be `\input`-ed

## How to apply
1. Copy these three files into your repository, overwriting the originals in `consolidation_project/`.
2. Run the fixer once:
   ```bash
   cd consolidation_project
   python3 scripts/fix_latex_preambles.py
   ```
3. Build:
   ```bash
   make all    # or: make core
   ```

If you later want to revert any appendix to standalone form, restore the `.bak` created by the fixer.
