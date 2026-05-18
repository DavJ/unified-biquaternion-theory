<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Unified Biquaternion Theory (UBT)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**Author**: Ing. David Jaroš  
**Status**: First external release preparation (2026-05-13)

---

## What Is UBT?

UBT is a biquaternionic field framework that aims to recover
general-relativistic geometry and explore possible links to gauge structure
and particle-generation structure from the algebra **ℂ⊗ℍ**, extended by
complex time **τ = t + iψ**.

The present release focuses on the GR-sector claim: emergent Lorentzian metric
geometry and real-sector recovery of the classical general-relativistic chain
from the field **Θ(q,τ)**. Gauge, alpha, consciousness, CTC, and other
speculative extensions are not part of the core claim of this release.

---

## UBT in Plain Language

UBT starts from one mathematical object: the biquaternion.
A biquaternion is like a quaternion used for 3D rotations, but with complex coefficients; equivalently, it can be represented as a 2×2 complex matrix.
UBT says that spacetime, matter, and forces are all encoded in one field, called **Θ**.
That field depends on position and carries the full physical content of the theory.
Instead of postulating gravity, particles, and gauge forces separately, UBT treats them as different aspects of the same underlying structure.
Its main equation is **∇†∇Θ = κ𝒯**.
The left-hand side says how the Θ field propagates and bends.
The right-hand side says what sources it through matter and energy.
From this single equation, UBT claims to recover Einstein’s equations of general relativity.
It also claims to recover the gauge symmetries behind the strong, weak, and electromagnetic interactions.
It further claims a derivation of the existence of three fermion generations.
The Weinberg angle is only conditional at present, not fully closed.
The fine-structure constant **α** remains an open problem rather than a finished derivation.
So the basic idea is simple even though the details are technical: one algebra, one field, one master equation, many physical sectors.

*For the technical details, see the sections below.*

---

## What Has Been Proved (as of 2026-05-13)

The current proof status is tracked explicitly below using proof levels.

Note: suffix ``-C'' in a level label (e.g., [L1-C]) means ``proved within the
stated projection convention''.

### General Relativity (Track T1_GR)

| Result | Level |
|--------|-------|
| Metric $g_{\mu\nu}$ derived from Θ (not postulated) | [L1] |
| Lorentzian signature in the admissible projected GR sector (AXIOM-B + Lorentzian projection/admissibility) | [L1-C] |
| Non-degeneracy det(g) ≠ 0 | [L1] |
| Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ from Hilbert variation | [L1] |
| Schwarzschild recovery: spatial components verified < 10⁻¹⁵; temporal component recovered analytically via complex-time phase sector | [L1]+[NUM/AN] |
| Regge-Wheeler equation (odd-parity graviton) derived | [L1] |
| Zerilli equation (even-parity graviton) derived | [L1] |

→ **Paper**: `papers/UBT_GR_Submission.tex` (**current canonical GR manuscript**, submit-ready)

The GR result is an induced-metric / on-shell sector result: UBT in its minimal
complex-time projection induces a Lorentzian metric sector whose real projection
reproduces the classical GR chain. A full off-shell $\\Theta$-only closure remains GAP-10.

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

→ **Audit note**: `B_Ram` is **OBS only, not derived from the UBT action functional S[Theta]**. `lambda_exact`
and `lambda_frac` are **OBS only, no derivation currently known**.

---

## What Is NOT Proved

UBT is honest about its limits.

| Topic | Status |
|-------|--------|
| Weinberg angle sin²θ_W | **Conditional open** — pure-algebra route is dead end; EW-1b (EW1+RG) is tracked conditionally |
| W/Z boson masses | Open (Higgs mechanism deferred) |
| Fermion mass spectrum | Open-hard |
| Dynamical colour confinement | Clay Millennium Problem |
| Full α = 1/137.036 (not just integer 137) | Open — Gap G137-B |

Full list: [`WHAT_IS_PROVED.md` ("What Is NOT Claimed as Proved")](WHAT_IS_PROVED.md#what-is-not-claimed-as-proved)

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
