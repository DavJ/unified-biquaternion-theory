<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Standard Model Coupling Inventory

**Task**: `map_stable_prime_sectors_to_coupling_constants` — Target 1  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-10  
**Status**: Reference compilation — values taken from published sources  
**Mode**: hypothesis_test_no_numerology  

---

## Purpose

Build a clean table of Standard Model couplings and their inverse values at
standard energy scales.  This inventory is constructed before any comparison
with stable primes, to ensure no reverse-engineering from prime values.

All values below are taken from the Particle Data Group (PDG) Review 2022/2024
and standard textbooks.  No stable-prime integer is used as input to any entry.

---

## 1. Conventions

Gauge couplings are defined via:

$$\alpha_i \;=\; \frac{g_i^2}{4\pi}, \qquad \alpha_i^{-1} \;=\; \frac{4\pi}{g_i^2}.$$

The three gauge groups of the Standard Model are:

| Index | Group | Coupling |
|-------|-------|---------|
| 1 | U(1)_Y (hypercharge) | g₁ (or g′, GUT-normalised √(5/3)·g′) |
| 2 | SU(2)_L (weak isospin) | g₂ |
| 3 | SU(3)_c (strong/QCD) | g₃ = g_s |

For the electromagnetic coupling α_em, at low energy:

$$\alpha_{\rm em} = \frac{e^2}{4\pi}, \qquad e = g_2 \sin\theta_W = g_1\cos\theta_W.$$

GUT normalisation of the hypercharge coupling:

$$\alpha_1^{\rm GUT} = \frac{5}{3}\,\frac{e^2}{4\pi\cos^2\theta_W}.$$

---

## 2. Electromagnetic Coupling α_em^{-1} at Multiple Scales

The electromagnetic coupling runs with energy scale μ via the QED/SM beta
function.  Reference values:

| Scale μ | Physical context | α_em^{-1}(μ) | Source |
|---------|-----------------|--------------|--------|
| μ → 0 (Thomson limit) | Classical / long-wavelength | **137.036** | CODATA 2018; PDG α |
| μ = m_e = 0.511 MeV | Electron mass | 137.036 | Essentially identical to Thomson |
| μ = m_μ = 105.66 MeV | Muon mass | ≈ 136.0 | PDG, computed; see Note 1 |
| μ = m_τ = 1777 MeV | Tau mass | ≈ 133.5 | PDG, computed |
| μ = M_Z = 91.19 GeV | Z-boson mass | **127.9** | LEP precision; PDG α(M_Z) |
| μ = m_t ≈ 173 GeV | Top quark mass | ≈ 126.7 | Extrapolated |

**Note 1**: The running below the muon threshold is governed by QED with only
the electron.  Above each fermion threshold, that fermion's contribution to
the vacuum polarization activates.

**Data sources**:
- PDG 2022, Table of Physical Constants, α = 1/137.036
- PDG 2022, electroweak review: α(M_Z)^{MS-bar} = 1/127.9
- Jegerlehner, F. (2003), "Hadronic vacuum polarization," hep-ph/0312372
- Steinberger, J. et al. (LEP Electroweak Working Group)

---

## 3. Weinberg Angle and Gauge Couplings at M_Z

| Quantity | Value at M_Z | Definition |
|---------|--------------|------------|
| sin²θ_W (MS-bar) | **0.2312** | θ_W: weak mixing angle |
| cos²θ_W | 0.7688 | = 1 − sin²θ_W |
| α_em(M_Z)^{-1} | 127.9 | = g_1²/(4π) · cos²θ_W / cos²θ_W ... see below |
| α₂(M_Z)^{-1} | **≈ 29.6** | = 4π/g₂² = α_em/(sin²θ_W) inverted |
| α₁(M_Z)^{-1} (GUT norm.) | **≈ 58.7** | = (3/5) · 4π cos²θ_W/e² |
| α₃(M_Z)^{-1} | **≈ 8.47** | = 4π/g_s², αs(M_Z) ≈ 0.1181 |

Derivation of entries:

```
α_em(M_Z) = 1/127.9

α₂(M_Z) = α_em(M_Z) / sin²θ_W
         = (1/127.9) / 0.2312
         ≈ 0.03381
         → α₂^{-1} ≈ 29.58

α₁(M_Z)^{GUT} = (5/3) · α_em(M_Z) / cos²θ_W
              = (5/3) · (1/127.9) / 0.7688
              ≈ 0.01703
              → α₁^{-1} ≈ 58.72

α₃(M_Z) = αs(M_Z) = 0.1181
         → α₃^{-1} ≈ 8.47
```

**Data sources**:
- PDG 2022, electroweak model review; sin²θ_W = 0.23121 ± 0.00003
- PDG 2022, αs = 0.1179 ± 0.0010 at M_Z (world average)

---

## 4. Running of Individual Gauge Couplings: α_i^{-1} vs Energy Scale

Below M_Z, only the electromagnetic coupling α_em is physical (after EW
symmetry breaking).  Above M_Z in the unbroken SM:

| μ | α_em^{-1} | α₂^{-1} | α₁^{-1} (GUT) | α₃^{-1} |
|---|-----------|---------|--------------|---------|
| m_e | 137.0 | — | — | — |
| m_μ | 136.0 | — | — | — |
| m_τ | 133.5 | — | — | — |
| M_Z | 127.9 | 29.6 | 58.7 | 8.47 |
| 1 TeV | ≈ 125.8 | ≈ 28.4 | ≈ 56.0 | ≈ 7.0 |
| 10 TeV | ≈ 124.1 | ≈ 27.4 | ≈ 53.8 | ≈ 5.9 |
| M_GUT ≈ 2×10¹⁶ GeV | ≈ 24.3 | ≈ 24.3 | ≈ 24.3 | ≈ 24.3 |

Note: GUT unification values are model-dependent estimates for supersymmetric
SM (MSSM).  Non-SUSY SM does not achieve exact unification.

One-loop running formulas (MS-bar):

$$\alpha_i^{-1}(\mu) = \alpha_i^{-1}(M_Z) - \frac{b_i}{2\pi}\ln\frac{\mu}{M_Z}$$

| Group | b_i coefficient (SM, one-loop) |
|-------|-------------------------------|
| U(1)_Y | b₁ = −41/10 = −4.1 |
| SU(2)_L | b₂ = +19/6 ≈ +3.17 |
| SU(3)_c | b₃ = +7 |

Sign convention: d α_i^{-1}/d ln μ = b_i/(2π).  With the above signs:
- α_em^{-1} decreases with μ (QED anti-screening)
- α₂^{-1} increases with μ (non-Abelian asymptotic freedom)
- α₃^{-1} increases with μ (QCD asymptotic freedom)

**Data source**: Peskin & Schroeder, QFT §18.3; PDG electroweak review

---

## 5. Possible Unification-Scale Quantities

GUT-normalised coupling at unification (non-SUSY SM, one-loop):

| Quantity | Estimate |
|---------|---------|
| Approx. M_GUT (non-SUSY, partial unification) | ~ 10^{15} GeV |
| α_GUT^{-1} (three couplings do not precisely meet) | ~ 40–50 (range) |
| α_GUT^{-1} (MSSM, precise meeting) | ≈ 24–25 |

These are not precise because unification is not exact in the minimal SM.

---

## 6. Summary Table: All Inverse Couplings in Comparable Form

| Coupling | Scale | α^{-1} value | Notes |
|---------|-------|--------------|-------|
| α_em | μ → 0 | **137.036** | Thomson; CODATA |
| α_em | m_e | 137.036 | no change at threshold |
| α_em | m_μ | ~136.0 | 1-loop QED + threshold |
| α_em | m_τ | ~133.5 | 1-loop QED + thresholds |
| α_em | M_Z | **127.9** | LEP measurement |
| α₂ (weak SU(2)) | M_Z | **≈ 29.6** | = α_em/sin²θ_W |
| α₁ (hyper-U(1), GUT norm.) | M_Z | **≈ 58.7** | = (5/3)α_em/cos²θ_W |
| α₃ (strong SU(3)) | M_Z | **≈ 8.47** | = αs(M_Z) |
| α_W (Fermi constant basis) | m_μ | ≈ 29.5 | ≈ α₂ at EW scale |
| α_s (QCD) | 1 GeV | ≈ 0.49 → α_s^{-1}≈2.0 | not large integer |

---

## 7. Data Quality and Precision

| Quantity | Precision | Status |
|---------|-----------|-------|
| α_em(0)^{-1} = 137.036 | ppm level | High precision; CODATA |
| α_em(M_Z)^{-1} = 127.9 | ~0.05% | LEP electroweak fit |
| sin²θ_W(M_Z) = 0.2312 | 0.01% | LEP+SLD+Tevatron |
| αs(M_Z) = 0.1181 | ~0.8% | World average |

---

## 8. Stable Prime Set (for Reference Only)

The stable prime set from the UBT prime stability framework is:

$$\mathcal{S} = \{2,\; 127,\; 137,\; 139,\; 151,\; 157\}$$

This set is **not used to derive or adjust** any value in this document.
It is listed here to allow subsequent reports to compare against this inventory.

---

**Deliverable**: This document is `reports/coupling_inventory.md`.  
**Used by**: `reports/stable_prime_coupling_comparison.md`, `reports/rg_prime_checkpoint_verdict.md`
