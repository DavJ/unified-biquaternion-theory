<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Unified Biquaternion Theory (UBT)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**Author**: Ing. David Jaroš  
**Status**: First external release preparation (2026-04-28)

---

## What Is UBT?

UBT derives General Relativity, Standard Model gauge structure, and three
particle generations from one algebraic object: the biquaternion algebra
**ℂ⊗ℍ** (complex quaternions), extended to complex time **τ = t + iψ**.

The fundamental field **Θ(q,τ)** satisfies a single field equation.
Everything else — spacetime metric, curvature, gauge interactions — is derived.

---

## What Has Been Proved (as of 2026-04-28)

**Complete proofs.** No hand-waving.

### General Relativity (Track T1_GR)

| Result | Level |
|--------|-------|
| Metric $g_{\mu\nu}$ derived from Θ (not postulated) | [L1] |
| Lorentzian signature (−,+,+,+) proved from AXIOM-B | [L1] |
| Non-degeneracy det(g) ≠ 0 | [L1] |
| Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ from Hilbert variation | [L1] |
| Schwarzschild metric recovered, spatial components verified < 10⁻¹⁵ | [L1]+[NUM] |
| Regge-Wheeler equation (odd-parity graviton) derived | [L1] |

→ **Paper**: `papers/UBT_GR_Submission.tex` (submit-ready)

### Standard Model Gauge Structure (Track T2_GAUGE)

| Result | Level |
|--------|-------|
| SU(3)_c from ℤ₂×ℤ₂×ℤ₂ involutions in ℂ⊗ℍ | [L0] |
| Quarks in **3**, gluons in **8**, EW/strong decoupling | [L0] |
| SU(2)_L × U(1)_Y × U(1)_EM from ℂ⊗ℍ | [L0] |
| Left-chirality of SU(2)_L (W couples to left-chiral doublets) | [L1] |
| Three generations from ψ-winding modes | [L0] |
| Hypercharge quantisation from Dirac condition on ψ-circle | [L0] |

→ **Status**: Paper draft in progress; target submission ~6 weeks.

### Fine Structure Constant (Track T3_ALPHA)

| Result | Level |
|--------|-------|
| N_eff = 12 is a motivated mode-counting candidate, currently OPEN/[MC] under critical audit; see canonical/n_eff/step2_AUDIT.tex. | OPEN/[MC] |
| α⁻¹_bare = 137 (integer) conditional on Gap G137-B | [L1] (conditional) |

→ **Status**: Conditional result. One gap open (Gap G137-B: derive effective
coupling B from UBT action). See `canonical/alpha/PRIMARY_ROUTE.md`, `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`, and `reports/gamma_entropy_alpha_interpolation_audit.md`.

→ **Audit note**: `B_Ram` is **OBS only, not derived from S[Theta]**. `lambda_exact`
and `lambda_frac` are **OBS only, no derivation currently known**.

---

## What Is NOT Proved

UBT is honest about its limits.

| Topic | Status |
|-------|--------|
| Weinberg angle sin²θ_W | **Dead end** — algebra cannot fix g'/g |
| W/Z boson masses | Open (Higgs mechanism deferred) |
| Fermion mass spectrum | Open-hard |
| Zerilli equation (even-parity graviton) | Open GAP-Z |
| Dynamical colour confinement | Clay Millennium Problem |
| Full α = 1/137.036 (not just integer 137) | Open — Gap G137-B |

Full list: [`WHAT_IS_PROVED.md`](WHAT_IS_PROVED.md)

---

## 5-Minute Navigation

| Want to know | Go here |
|-------------|---------|
| Is the GR paper ready to submit? | [`STATUS.md`](STATUS.md) |
| What is actually proved? | [`WHAT_IS_PROVED.md`](WHAT_IS_PROVED.md) |
| What happens next? | [`ROADMAP.md`](ROADMAP.md) |
| Read the GR paper | [`papers/UBT_GR_Submission.tex`](papers/UBT_GR_Submission.tex) |
| Gauge sector status | [`reports/gauge_truth_matrix.md`](reports/gauge_truth_matrix.md) |
| Alpha route decision | [`canonical/alpha/PRIMARY_ROUTE.md`](canonical/alpha/PRIMARY_ROUTE.md) |
| All canonical proofs | [`canonical/`](canonical/) |
| Open problems | [`reports/`](reports/) |
| Full derivation index | [`DERIVATION_INDEX.md`](DERIVATION_INDEX.md) |

---

## Repository Structure

```
canonical/          Core theory — algebra, fields, geometry, interactions
papers/             Submission-ready papers
reports/            Honest status reports and gap analyses
research_tracks/    Active open-problem research
speculative_extensions/  Speculative ideas (clearly labelled)
tools/              Numerical verification scripts
ARCHIVE/            Historical material (not deleted, not primary)
```

---

## License

Theory documents (LaTeX, Markdown): **CC BY-NC-ND 4.0**  
Code and scripts: **MIT License**  
Author: Ing. David Jaroš — see [`LICENSE.md`](LICENSE.md)
