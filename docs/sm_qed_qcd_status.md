<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# SM / QED / QCD Status in UBT

**Architecture:** Dual-track research program.

- **Track A:** Purely associative (ℂ⊗ℍ) internal symmetry analysis.
- **Track B:** Octonionic extension as explicit hypothesis (ℂ⊗𝕆 completion).

---

## Derived (from ℂ⊗ℍ associative sector)

| Item | Source | Notes |
|------|--------|-------|
| SU(2) candidate | Left-multiplication action on ℂ⊗ℍ | Quaternionic structure; chiral choice gives SU(2)_L |
| U(1) phase symmetry | Aut(ℂ) ≅ U(1) | Global → local via minimal coupling |

---

## Embedded (standard QFT in UBT notation)

| Item | File | Notes |
|------|------|-------|
| QED Lagrangian | `canonical/interactions/qed.tex` | Standard QED in biquaternionic notation; U(1) coupling |
| QCD Lagrangian | `canonical/interactions/qcd.tex` | Standard QCD in biquaternionic notation; SU(3) assumed |

---

## Hypothesis (requires proof of necessity)

| Item | Track | Condition |
|------|-------|-----------|
| SU(3) via ℂ⊗𝕆 | B | ℂ⊗ℍ extended to ℂ⊗𝕆; SU(3) ⊂ G₂ = Aut(𝕆); necessity not yet proven |

See `research_tracks/octonionic_completion/hypothesis.md` for required justification
conditions.

---

## Open Questions

| Item | Status | Track |
|------|--------|-------|
| Hypercharge assignment | Not derived | Open |
| Chirality (L/R asymmetry) | Not derived | Open |
| Three generations | Not derived | Open (octonionic triality is a hint, not a proof) |
| SU(3) without octonions | Scan complete: not found in Aut(ℂ⊗ℍ) | A |
| Necessity of ℂ⊗𝕆 | Not proven | B |

---

## Cross-references

- `research_tracks/associative_su3/strategy.md` — Track A plan
- `research_tracks/octonionic_completion/hypothesis.md` — Track B hypothesis
- `reports/associative_su3_scan.md` — Track A computational results
- `consolidation_project/appendix_E2_SM_geometry.tex` — Mathematical detail
- `canonical/interactions/qcd.tex` — Canonical QCD
- `canonical/interactions/qed.tex` — Canonical QED
