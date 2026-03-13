<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Particle Spectrum

UBT predicts three fermion generations from the ψ-winding mode structure of Θ,
and recovers Standard Model quantum numbers from the gauge algebra.

**Canonical source**: [`experiments/research_tracks/three_generations/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/experiments/research_tracks/three_generations)  
**Topic index**: [`canonical/THEORY/topic_indexes/hecke_index.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/THEORY/topic_indexes/hecke_index.md)

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

| Result | Status |
|--------|--------|
| ψ-modes as independent B-fields | **Proved [L0]** |
| Modes carry same SU(3) quantum numbers | **Proved [L0]** |
| ψ-parity forbids even↔odd mixing | **Proved [L0]** |
| Identification Θ₀/Θ₁/Θ₂ ↔ e/μ/τ | **Conjecture** |
| Mass ratios reproduced | **Open Hard Problem** |

**File**: [`st3_complex_time_generations.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/experiments/research_tracks/three_generations/st3_complex_time_generations.tex)

---

## Mass Ratios — Status

Three approaches to reproducing lepton mass ratios have been explored:

| Option | Approach | Status |
|--------|----------|--------|
| A | Linear mixing of ψ-modes | **Dead End** — max ratio ~461, far below 3477 |
| B | Linear Yukawa coupling | **Dead End** — ratio 1:2:3 only |
| C | ψ-instantons | **Open Hard Problem** — calibrated to muon; tau off by factor ~6 |

Mass ratio reproduction is an **open hard problem**.  
Script: [`tools/reproduce_lepton_ratios.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/tools/reproduce_lepton_ratios.py)

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
