# arXiv Submission Checklist — Gravity Paper

**Title**: Schwarzschild Metric and Twistor Correspondence in Biquaternionic Field Theory
**Author**: Ing. David Jaroš
**Target**: gr-qc (primary), hep-th (cross-list)
**File**: `docs/publication/ubt_gravity_paper.tex`
**Lines**: 455 (complete, 0 TODO/PLACEHOLDER)

---

## Pre-submission

- [x] License in comments (`% © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0`)
- [x] Higgs mechanism section added (§7: Electroweak Symmetry Breaking via Hosotani Mechanism)
- [ ] Abstract ≤ 1920 characters (check with `wc -c` on abstract text)
- [ ] Author affiliation line: "Independent Researcher, Czech Republic"
- [ ] Bibliography complete (check all `\bibitem` resolve)
- [ ] Replace any `\usepackage{tcolorbox}` with `\usepackage{mdframed}` if present
- [ ] All `\label` / `\ref` cross-references resolve without warnings

## Compilation

- [ ] `pdflatex -interaction=nonstopmode ubt_gravity_paper.tex` — 0 errors
- [ ] Second pass (for references): run `pdflatex` twice
- [ ] No undefined references (`grep 'Undefined control' *.log`)
- [ ] No overfull hboxes in key equations

## arXiv Metadata

- **Categories**: gr-qc (primary), hep-th (cross-list)
- **MSC classes**: 83C05, 53C28
- **Title** (arXiv): Schwarzschild Metric and Twistor Correspondence in Biquaternionic Field Theory
- **Authors**: David Jaroš
- **Comments**: 10 pages; companion paper to arXiv:2501.XXXXX (fine structure constant)

## Content Cross-Check

- [x] §1 Introduction: motivates biquaternion framework; cite{UBTAlpha} cross-ref present
- [ ] §2 UBT action and covariant derivative
- [ ] §3 Schwarzschild background Θ₀^(S) derived
- [x] §4 Graviton dispersion and V_eff(r); **Regge-Wheeler exact match [L1] added (v69)**
- [x] §4 Regge-Wheeler result: `thm:regge_wheeler` references canonical/ theorem (added v69)
- [x] §5 (was Regge-Wheeler open): now Zerilli even-parity (Gap L2: OPEN — v71 explicit computation confirms rational denominator; leading terms match; two-component Ansatz needed)
- [ ] §6 Twistor correspondence
- [x] §7 Electroweak Symmetry Breaking via Hosotani Mechanism (added v68)
- [ ] References: Regge & Wheeler (1957), Zerilli (1970), Penrose (1976), UBT Alpha paper

## Post-submission

- [ ] Add arXiv ID to `CITATION.cff`
- [ ] Add arXiv link to `DERIVATION_INDEX.md` gravitational section
- [ ] Update `docs/publication/arxiv_submission_checklist.md` with cross-ref
- [ ] Announce in repository README.md

## Notes

- Gap L2 (Regge-Wheeler full coefficient match) remains OPEN pending angular
  decomposition (spin-weighted spherical harmonics); see
  `research_tracks/research/graviton_schwarzschild.tex` §5.
- After angular decomposition closes Gap L2, upgrade paper and resubmit as v2.
