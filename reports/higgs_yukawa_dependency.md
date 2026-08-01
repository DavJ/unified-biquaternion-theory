<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# higgs_yukawa_dependency.md — T2_GAUGE Higgs and Yukawa Dependency Map

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Map every SM result whose derivation in UBT depends on the
Higgs/SSB sector or Yukawa couplings. These results are NOT part of the
gauge algebra derivation and must not be claimed in the gauge paper.  
**Sources**: `research_tracks/T2_GAUGE/missing_axioms.md`,
`research_tracks/research/higgs_yukawa_scan.md`,
`canonical/symmetry/effective_vs_fundamental_breaking.tex`

---

## Why This Document Exists

The T2_GAUGE gauge paper can claim:
- Gauge group structure: SU(3)_c × SU(2)_L × U(1)_Y derived from ℂ⊗ℍ
- Anomaly cancellation: proved or motivated (see `reports/anomaly_gap.md`)
- Chirality: SU(2)_L from ψ-parity (see `reports/chirality_gap.md`)

The gauge paper **cannot** claim (without a dedicated Higgs/Yukawa paper):
- Gauge boson masses (W, Z)
- Fermion masses (quarks, leptons)
- CKM matrix (quark mixing)
- PMNS matrix (neutrino mixing)
- Higgs boson mass

This document maps the exact boundary.

---

## Dependency Table

### Results that depend on the Higgs sector (not in gauge paper scope)

| Claim | Why Higgs-dependent | Gap | UBT status |
|-------|--------------------|----|------------|
| W± mass M_W = g v/2 | Requires Higgs VEV v | HY-1 | OPEN |
| Z mass M_Z = M_W/cos θ_W | Requires v and θ_W | HY-1 + EW-1 | OPEN |
| Higgs boson mass m_h = √(2λ) v | Requires Higgs potential λ | HY-2 | OPEN |
| SU(2)_L × U(1)_Y → U(1)_EM breaking | Requires SSB mechanism and doublet VEV | HY-3 | CANDIDATE — Θ₀ as doublet |
| Goldstone boson identification | Requires Goldstone theorem applied to SSB | HY-4 | MOTIVATED |

### Results that depend on Yukawa couplings (not in gauge paper scope)

| Claim | Why Yukawa-dependent | Gap | UBT status |
|-------|---------------------|-----|------------|
| Up-quark mass m_u | Requires Yukawa coupling y_u from S[Θ] | YK-1 | OPEN |
| Down-quark mass m_d | Requires y_d | YK-1 | OPEN |
| Electron mass m_e | Requires y_e | YK-1 | OPEN |
| Neutrino mass (Majorana/Dirac) | Requires Majorana mass term or y_ν | YK-2 | OPEN |
| CKM quark mixing matrix | Requires complex Yukawa structure | YK-3 | OPEN |
| PMNS neutrino mixing matrix | Requires Yukawa + Majorana structure | YK-3 | OPEN |
| CP violation (δ_CKM) | Requires complex phases in Yukawa | YK-4 | OPEN |

---

## Gap Definitions

### HY-1 — Higgs VEV from UBT

**Statement needed**: Show that the UBT field Θ₀ (or a component thereof) has a
non-zero vacuum expectation value v = ⟨Θ₀⟩ ≠ 0 with specific magnitude.

**Current state**: The Θ₀ VEV is a candidate for the Higgs VEV (static ansatz
Θ₀ from the GR paper). However, the magnitude v = 246 GeV is not derived;
it requires identifying v with the Fermi scale G_F = 1/(√2 v²).

**What would close it**: Show that S[Θ] has a minimum with |⟨Θ⟩| = v, where
v is fixed by the UBT action parameters (not the Fermi scale input).

---

### HY-2 — Higgs Potential from S[Θ]

**Statement needed**: Derive the effective Higgs potential V(|Θ|) = −μ²|Θ|² + λ|Θ|⁴
from the UBT action.

**Current state**: The UBT action S[Θ] = ∫ Re[Tr(∇†∇Θ·𝒯)] is a kinetic term.
The quartic potential term has not been derived.

**What would close it**: Show that quantum corrections to S[Θ] generate an
effective potential of the Mexican hat form.

---

### HY-3 — SSB Pattern SU(2)_L × U(1)_Y → U(1)_EM

**Statement needed**: The spontaneous symmetry breaking pattern is exactly
SU(2)_L × U(1)_Y → U(1)_EM, not any other subgroup.

**Current state**: MOTIVATED — the Θ₀ static ansatz has U(1)_EM as its
stabiliser (rotation symmetry of the spherically symmetric solution). This
motivates the correct SSB pattern but does not prove it in the electroweak sector.

**What would close it**: Show that the Θ₀ EW VEV leaves exactly Q = T₃ + Y/2 = 0
unbroken, and that the residual symmetry is U(1)_EM.

---

### HY-4 — Goldstone Boson Identification

**Statement needed**: After SSB of SU(2)_L × U(1)_Y → U(1)_EM, three Goldstone
bosons appear; they are absorbed by W±, Z (Higgs mechanism). The physical Higgs H
is the remaining scalar.

**Current state**: Standard Goldstone theorem applies once HY-3 is proved.

---

### YK-1 — Yukawa Couplings from UBT

**Statement needed**: The Yukawa coupling Lagrangian L_Y = y_ij Q̄_iL Θ u_jR + h.c.
follows from UBT with specific coupling matrix y_ij.

**Current state**: OPEN HARD — the coupling matrix y_ij is not determined by the
gauge structure alone. It requires understanding the matter-field coupling to Θ
beyond the kinetic term.

---

### YK-3 — Fermion Mixing from UBT

**Statement needed**: The CKM and PMNS matrices follow from the Yukawa structure.

**Current state**: NOT ATTEMPTED — depends on YK-1.

---

### YK-4 — CP Violation

**Statement needed**: The CP-violating phase δ ≈ 70° in the CKM matrix follows
from the complex structure of UBT (complex time τ = t + iψ).

**Current state**: CANDIDATE — the ψ-direction provides a natural source of
complex phases. No derivation exists.

---

## Scope Statement for the T2_GAUGE Paper

**Correct scope** (what the gauge paper can claim):

> The T2_GAUGE paper establishes that the gauge group SU(3)_c × SU(2)_L × U(1)_Y
> arises algebraically from the biquaternion algebra ℂ⊗ℍ. It proves the group
> structure, chirality motivation, and anomaly cancellation (for derived results).
> It explicitly defers mass generation, fermion mixing, and CP violation to a
> future Higgs/Yukawa paper.

**What must NOT be claimed in the gauge paper** (even if the author believes it):
- Particle masses
- Mixing angles (CKM, PMNS)
- The value of sin²θ_W (EW-1 is open)
- Fermion hypercharge values (HY-3, YK-1 needed)

---

## Connection to the α Programme

The Weinberg angle sin²θ_W (the target of the T3_ALPHA programme) falls in the
**boundary zone**: it requires the SSB pattern (HY-3) but not the particle masses
(HY-1, YK-1). It is the minimal element needed from the Higgs sector before α
can be derived.

Priority dependency chain:

```
T2_GAUGE: SU(2)_L × U(1)_Y structure derived
    ↓
HY-3: SSB pattern SU(2)_L × U(1)_Y → U(1)_EM
    ↓
EW-1: g'/g ratio fixed (or via polyhedral route)
    ↓
sin²θ_W derived (T3_ALPHA target)
    ↓
α = g² sin²θ_W / (4π) derived
```

---

## References

- `research_tracks/T2_GAUGE/missing_axioms.md` — axiom/gap inventory
- `research_tracks/research/higgs_yukawa_scan.md` — Higgs/Yukawa scan
- `canonical/symmetry/effective_vs_fundamental_breaking.tex` — SSB analysis
- `reports/gauge_status_matrix.md` — full gauge status matrix
- `canonical/alpha/ew_mixing_gap_map.md` — EW mixing gaps
