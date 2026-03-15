<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# Particle Spectrum

UBT **proposes** three fermion generations from the ψ-winding mode structure of Θ.
The identification Θ₀/Θ₁/Θ₂ ↔ e/μ/τ is a **conjecture**; lepton mass ratios
are an **open hard problem** (KK mismatch theorem).
UBT recovers Standard Model quantum numbers from the gauge algebra.

**Canonical source**: [`experiments/research_tracks/three_generations/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/experiments/research_tracks/three_generations)  
**Topic index**: [`canonical/THEORY/topic_indexes/hecke_index.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/THEORY/topic_indexes/hecke_index.md)

---

## Three Fermion Generations

### ψ-Modes as Generation Structure

The three fermion generations are proposed to correspond to three independent
ψ-winding modes of Θ:

```
Θ_0 ↔ electron (first generation)
Θ_1 ↔ muon     (second generation)
Θ_2 ↔ tau      (third generation)
```

**File**: [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex)

### Derivation Status (from DERIVATION_INDEX.md)

<!-- BEGIN GENERATED: three_generations_status -->
| Result | Status | File |
|--------|--------|------|
| ψ-modes as independent B-fields | ✅ **Proved** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| Modes carry same SU(3) quantum numbers | ✅ **Proved** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| ψ-parity forbids even↔odd mixing | ✅ **Proved** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| Quaternionic origin of three families: {i,j,k} ↔ three fermion families | ❓ **Unknown** | [`generation_structure.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/research_tracks/research/generation_structure.tex) |
| KK mismatch (ratio 1:2 vs 207:3477) | ✅ **Proved** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| Option A (linear mixing) reproduces ratios | ❌ **Dead End** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| Option B (linear Yukawa) reproduces ratios | ❌ **Dead End** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| Option C (ψ-instantons) reproduces ratios | ❌ **Open** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| Identification Θ₀/Θ₁/Θ₂ ↔ e/μ/τ | 💭 **Conjecture** | [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/st3_complex_time_generations.tex) |
| Mass ratio script (Options A/B/C) | ✅ **Proved** | [`reproduce_lepton_ratios.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/tools/reproduce_lepton_ratios.py) |
| Hecke conjecture p=137 | ⚡ **Supported** | [`hecke_lepton`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/docs/reports/hecke_lepton) |
| Hecke twin prime p=139 (mirror sector) | ⚡ **Supported** | [`mirror_world_139.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/reports/hecke_lepton/mirror_world_139.md) |
| CM k=6 forms at any level | ❌ **Dead End** | [`step5_hecke_search_results.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/step5_hecke_search_results.tex) |
| Non-CM k=6 forms, N≤4 | ❌ **Dead End** | [`step5_hecke_search_results.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/step5_hecke_search_results.tex) |
| Non-CM k=6 forms, N∈ | ❌ **Open** | [`step6_nonCM_search.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/experiments/research_tracks/three_generations/step6_nonCM_search.tex) |
| KK eigenvalue formula form E_{n,m} = (1/R)√ | 🔶 **Structural** | [`appendix_W2_lepton_spectrum.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/appendix_W2_lepton_spectrum.tex) |
| Hosotani shift δ = ½ | 🔶 **Structural** | [`appendix_W2_lepton_spectrum.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/appendix_W2_lepton_spectrum.tex) |
| R = 1/m_e (torus radius) | ⚠️ **Semi-empirical** | [`canonical_derivation.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/reports/lepton_audit/canonical_derivation.md) |
| KK mismatch (E_{0,2}/E_{0,1} ≈ 1.844 ≠ 207) | 🔶 **Structural** | [`status_summary.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/reports/lepton_audit/status_summary.md) |
| Hopfion formula form m(n) = A·n^p − B_m·n·ln(n) | 🔶 **Structural** | [`STATUS_FERMIONS.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/historical_versions/status/STATUS_FERMIONS.md) |
| *… and 5 more results* | *See [DERIVATION_INDEX.md](https://github.com/DavJ/unified-biquaternion-theory/blob/master/DERIVATION_INDEX.md)* | |
<!-- END GENERATED: three_generations_status -->

---

## Mass Ratios — Status

Three approaches to reproducing lepton mass ratios have been explored:

| Option | Approach | Status |
|--------|----------|--------|
| A | Linear mixing of ψ-modes | **Dead End** — max ratio ~461, far below 3477 |
| B | Linear Yukawa coupling | **Dead End** — ratio 1:2:3 only |
| C | ψ-instantons | **Open Hard Problem** — calibrated to muon; tau off by factor ~6 |

Mass ratio reproduction is an **open hard problem**.  
Script: [`tools/reproduce_lepton_ratios.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/tools/reproduce_lepton_ratios.py)

---

## Hecke Structure and Lepton Masses

Numerical evidence from Hecke eigenvalue computations suggests a connection
between prime p = 137 and the lepton mass ratios:

- **Set A** (p = 137): unique global minimum in prime range 50–300 matching
  (76.2, 7.4, 208.6) with μ error 0.02%, τ error 0.10%
- **Set B** (p = 139): mirror sector, distinct lepton ratios (195.2, 50.4, 54.6)

Status: **Strong Numerical Support**

→ Details: [Hecke / Modular Structure](Hecke_Modular_Structure)

---

## Quark Sector

Quarks live in the fundamental representation ℂ³ of SU(3)_c.  
The quark mass spectrum is **not yet derived** from first principles.

→ Color structure: [SU(3) Structure](SU3_Structure)

---

## Gauge Quantum Numbers

Standard Model quantum numbers (isospin, hypercharge, color) emerge from the
algebra structure of ℂ⊗ℍ. See [Gauge Structure](Gauge_Structure) for derivations.

---

## See Also

- [Gauge Structure](Gauge_Structure) — SM gauge group emergence
- [Hecke / Modular Structure](Hecke_Modular_Structure) — numerical lepton mass evidence
- [Research Tracks](Research_Tracks) — ongoing work on mass spectrum
