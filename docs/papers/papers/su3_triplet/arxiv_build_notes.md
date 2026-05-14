<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# arXiv Build Notes — SU(3) Triplet Paper

**File:** `papers/su3_triplet/arxiv_version.tex`  
**Date:** 2026-03-02  
**Target:** arXiv math-ph (MSC 17A35, 22E70, 81R05)

---

## Standalone Status

`arxiv_version.tex` is **self-contained**:

- Uses `\documentclass[12pt,a4paper]{article}` — no external class file required.
- Packages: `amsmath`, `amssymb`, `amsthm`, `hyperref`, `geometry` — all standard
  CTAN packages included in any TeX Live / MikTeX distribution.
- **No `\input` or `\include` directives** — all content is inline.
- Bibliography uses `\begin{thebibliography}{99}` — no `.bib` file or BibTeX needed.
- Does **not** use `tcolorbox` (used in companion `local_gauge_extension.tex` but
  not in the arXiv submission).
- Does **not** reference any repo-internal paths; companion-document references
  appear only in Open Problems text (not as `\input`).

---

## Compilation Instructions

```bash
# From the papers/su3_triplet/ directory (run twice for cross-references):
pdflatex -interaction=nonstopmode arxiv_version.tex
pdflatex -interaction=nonstopmode arxiv_version.tex
```

Or with latexmk:
```bash
latexmk -pdf arxiv_version.tex
```

Expected output: `arxiv_version.pdf` with no errors or unresolved references.

---

## Abstract Conservative Check

The abstract (`arxiv_version.tex`, lines 55–76) references:
- ✅ Pure algebra: $\mathbb{C}\otimes\mathbb{H}$, involutions, Hermitian form
- ✅ Classical results: $\mathrm{Aut}(\mathbb{H})\cong\mathrm{SO}(3)$, Dixon, Furey
- ❌ No reference to Standard Model
- ❌ No reference to particle masses
- ❌ No reference to cosmology
- ❌ No reference to General Relativity
- ❌ No physical interpretation claims

---

## Open Problems — Explicit Labels

The Open Problems section (§ Open Problems) explicitly labels:

1. **Dynamical symmetry — not proved.** The global SU(3) invariance of the
   *free* kinetic term is proved, but extension to interacting or dynamical
   operators is unresolved.
2. **Local gauge extension — candidate only.** The Yang-Mills gauge construction
   is a candidate; no new derivation is made.
3. Canonicality of $V_c$ under $\mathrm{Aut}_\mathbb{R}(\mathcal{B})$ — open.
4. Physical interpretation — not claimed.

---

## Dependency Audit

| Dependency | Present | Required |
|------------|---------|----------|
| `\documentclass` | ✅ article | ✅ |
| `amsmath` | ✅ | ✅ |
| `amssymb` | ✅ | ✅ |
| `amsthm` | ✅ | ✅ |
| `hyperref` | ✅ | ✅ (hyperlinks) |
| `geometry` | ✅ | ✅ (margins) |
| `tcolorbox` | ❌ not used | — |
| `\input` / `\include` | ❌ none | — |
| External `.bib` | ❌ not used | — |
| Internal `\ref` to other files | ❌ none | — |

---

## Known Issues

- None for standalone compilation.
- The `\newcommand{\C}{\mathbb{C}}` conflicts with some package definitions
  (e.g., `complexity`); no such package is loaded here so there is no conflict.

---

## arXiv Submission Notes

- Submit `arxiv_version.tex` as a single `.tex` file.
- No supplementary files needed.
- MSC codes are embedded in the file (lines after abstract).
- Keywords are embedded.
