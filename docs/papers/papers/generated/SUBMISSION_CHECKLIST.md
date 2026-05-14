# arXiv Submission Checklist — N_eff = 12 Paper

**Paper:** `papers/generated/neff_biquaternion.tex`  
**Prepared:** 2026-03-06  
**Target:** hep-ph (primary), hep-th, gr-qc (secondary)

---

## Content Completeness

- [x] Abstract with ΔN_eff = 0.046 prediction
- [x] N_eff = 12 derivation (complete — Section 3, Theorem 3.2)
- [x] B₀ = 8π derivation (complete — Section 4, Theorem 4.1)
- [x] Open Problem A stated honestly (Section 4, explicit boxed statement)
- [x] CMB-S4 forecast comparison (Section 5.2, threshold 0.03 cited)
- [x] All claims labelled: Proved/Predicted/Open (throughout text)

## Proof Quality

- [x] All theorems have proofs or "proof sketch"
  - Theorem 3.2: N_eff = 12 — proved by direct algebra (dim Im ℍ = 3)
  - Theorem 4.1: B₀ = 8π — proved from S_kin[Θ], zero free parameters
  - Corollary 5.1: ΔN_eff ≈ 0.046 — proved from zero-mode count
- [x] All open problems explicitly stated
  - Open Problem A: B_phenom ≈ 46.3 ≠ B₀ = 8π (ratio 1.84, unexplained)
  - Open Problem B: geometric factor R ≈ 1.114 not derived from first principles
- [x] No claim stronger than its evidence
  - α⁻¹ = 137 stated as "semi-empirical given B_phenom"
  - B_phenom explicitly called an open problem

## References

- [x] References complete (check bibtex entries in paper)
  - Planck 2018: Aghanim et al. (2020)
  - CMB-S4: Abazajian et al. (2016)
  - Standard quaternion algebra reference
  - QED running coupling reference
- [ ] DOI for UBT main paper (pending arXiv submission of this paper)
- [ ] ORCID for David Jaroš (pending registration)

## Figures

- [ ] N_eff derivation diagram (algebraic structure: 3×2×2)
  — currently absent; would strengthen Section 3
- [ ] ΔN_eff vs T_D plot (decoupling temperature dependence)
  — currently absent; would strengthen Section 5

## Reproducibility

- [x] Companion script referenced: `tools/verify_N_eff.py`
- [x] All numerical results checkable by script
- [x] No proprietary software required

## Metadata

- [x] arXiv metadata file: `papers/generated/arxiv_metadata.txt`
- [x] Title correct: "N_eff = 12 from Biquaternion Algebra and Its Cosmological Implications: ΔN_eff ≈ 0.046 as a Prediction of UBT"
- [x] Author: David Jaroš
- [x] Primary class: hep-ph
- [x] Secondary classes: hep-th, gr-qc
- [x] Keywords listed in metadata
- [ ] ORCID added (pending)
- [ ] Final read-through by David

## Final Status

| Check | Status |
|-------|--------|
| All theorems proved | ✅ |
| Open problems stated | ✅ |
| No overclaiming | ✅ |
| References complete | ⚠️ (2 pending: DOI + ORCID) |
| Figures | ⚠️ (optional but recommended) |
| Reproducibility | ✅ |
| Metadata | ✅ |

**Overall: READY FOR SUBMISSION** (pending ORCID and optional figures)
