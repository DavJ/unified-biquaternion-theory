<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# RG Prime Checkpoint Verdict

**Task**: `map_stable_prime_sectors_to_coupling_constants` — Target 3 (verdict)  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-10  
**Companion**: `research_tracks/coupling_spectrum/rg_prime_checkpoints.tex`  
**Mode**: hypothesis_test_no_numerology

---

## 1. Question

Can stable primes 127 and 137 be understood as RG checkpoints of the
electromagnetic coupling, and can the full set {127, 137, 139, 151, 157}
be interpreted as coarse-grained RG plateaus?

---

## 2. Derivation Summary

**RG equation** (one-loop QED/SM):

```
dα_em^{-1}/d ln μ = −b_em/(2π)      [b_em > 0]
```

**Direction**: DERIVED — α_em^{-1} decreases monotonically with increasing μ.

**Integrated trajectory**:

```
α_em^{-1}(μ) = α_em^{-1}(μ₀) − [b_em/(2π)] ln(μ/μ₀)
```

**Trajectory endpoints** (full SM, from data):

| Scale | α_em^{-1} | Source |
|-------|-----------|--------|
| μ → 0 (Thomson) | 137.036 | CODATA 2018 |
| μ = m_e | 137.036 | QED threshold |
| μ = m_μ | ≈ 136.0 | QED running |
| μ = M_Z | 127.9 | LEP measurement |

**Total running**: Δ(α_em^{-1}) = 137.036 − 127.9 = 9.136 over ~11 decades in energy.

---

## 3. Comparison with Stable Primes

| Prime | Nearest coupling | Distance | δ(%) | Passes through? |
|-------|-----------------|----------|------|----------------|
| 137 | α_em^{-1}(0) = 137.036 | 0.036 | 0.026% | YES (nearly exactly) |
| 127 | α_em^{-1}(M_Z) = 127.9 | 0.9 | 0.70% | YES (within ~1 unit) |
| 139 | α_em^{-1}(0) = 137.036 | 1.964 | 1.43% | NO (off by 2 units) |
| 151 | α_em^{-1}(?) | > 13 | > 10% | NO |
| 157 | α_em^{-1}(?) | > 19 | > 14% | NO |
| 2 | (structural) | N/A | N/A | N/A |

---

## 4. Can 127 and 137 Be RG Checkpoints?

**Assessment**: The electromagnetic trajectory does pass continuously through
values near 137 and 128.  Both 127 and 137 fall inside the physical running
window [127.9, 137.036].

**However**:
- The trajectory is continuous; there is no physical mechanism selecting integers.
- The actual low-energy value is 137.036, not 137.
- The actual M_Z value is 127.9, not 127.
- Offsets of 0.036 and 0.9 are physically significant and not explained by the
  prime-stability condition.
- No UBT mechanism is known that quantises α_em^{-1} at integer or prime values.

**Classification: OBSERVED_CONSISTENCY** — 127 and 137 are approximately consistent
with the endpoints of the electromagnetic running, but this is coincidental proximity,
not derivation.

---

## 5. Can All Five Primes Be RG Plateaus?

**Assessment**: For 139, 151, 157 to be RG plateaus, there would need to exist
effective coupling inverses equal to these values at physical energy scales.

No such coupling exists in the Standard Model:
- α_em^{-1}(0) = 137.036 (not 139, not 151, not 157)
- α₂^{-1}(M_Z) ≈ 29.6 (not in range)
- α₁^{-1}(M_Z) ≈ 58.7 (not in range)
- α₃^{-1}(M_Z) ≈ 8.47 (not in range)

**Classification: NO_EVIDENCE** for 139, 151, 157 as RG checkpoints.

---

## 6. Verdict

| Element | Verdict |
|---------|--------|
| 127 as α_em^{-1}(M_Z) checkpoint | OBSERVED_CONSISTENCY |
| 137 as α_em^{-1}(0) checkpoint | OBSERVED_CONSISTENCY |
| 127+137 as RG trajectory bounds | PLAUSIBLE_RG_STRUCTURE (hypothesis) |
| 139 as any RG checkpoint | NO_EVIDENCE |
| 151 as any RG checkpoint | NO_EVIDENCE |
| 157 as any RG checkpoint | NO_EVIDENCE |

**Combined verdict**: The electromagnetic RG trajectory is consistent with the
presence of 127 and 137 in the stable-prime set.  This consistency is approximate
(not exact) and does not constitute derivation.  The primes 139, 151, 157 have
no identified RG interpretation.

---

## 7. Hard-Rule Compliance

| Rule | Status |
|------|-------|
| No prime used to derive coupling | ✓ |
| No coupling adjusted to match prime | ✓ |
| Offsets (0.036, 0.9) stated and not suppressed | ✓ |
| 139, 151, 157 assessed honestly as NO_EVIDENCE | ✓ |

---

**Mandatory final sentence**:  
Stable primes do not currently map to Standard Model couplings beyond alpha-like coincidences.
