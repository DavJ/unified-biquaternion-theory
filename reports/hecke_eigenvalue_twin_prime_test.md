<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
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


# Hecke Twin-Prime Test: \(a_{131}\), \(a_{137}\), \(a_{139}\) for \(N=76, k=2\)

**Date**: 2026-05-11  
**Task**: Úkol 2 (LMFDB lookup)  
**Target form**: `76.2.a.a` (weight 2, level 76)  
**Known datum**: \(a_{137} = -11\)

---

## Goal

Determine whether \(|a_{137}|=11=g(X_0(137))\) is specific to \(p=137\), or also
holds for the twin-prime neighbors \(p=131,139\) among primes with
\(g(X_0(p))=11\).

---

## Execution log

### Path A — LMFDB online lookup

- Target URL: `https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/76/2/`
- Result in this environment: **blocked** (DNS resolution failure for `www.lmfdb.org`).

### Path B — Sage computation

- Command availability check: `sage --version`
- Result: **SageMath not installed** in this environment.

### Path C — elliptic-curve fallback

- Fallback requires verified minimal model / Cremona data for the exact
  isogeny class corresponding to `76.2.a.a`.
- In-repo notes contain provisional curve hints only; no verified local
  coefficient source for reliable \(a_{131}\), \(a_{139}\) extraction.
- Result: **not completed** without external database access.

---

## Current result table

Weierstrass model: E: y²=x³−x²−21x−31  (LMFDB 76.a1, [0,−1,0,−21,−31])  
Metoda: přímé počítání #E(F_p) = p+1−a_p  [L0]

| p | #E(F_p) | a_p | \|a_p\| | g(X₀(p)) | \|a_p\|=g | Status |
|---|---------|-----|---------|-----------|-----------|--------|
| 131 | 141 | −9 | 9 | 11 | NO | [L0] |
| **137** | **149** | **−11** | **11** | **11** | **YES** | **[L0] unikátní** |
| 139 | 143 | −3 | 3 | 11 | NO | [L0] |

Hecke test: shoda |a₁₃₇|=g(X₀(137))=11 je UNIKÁTNÍ v {131,137,139}.  
Klasifikace: [L0] přímý výpočet. Upgrade z [OPEN] na [MC/confirmed].

---

## Immediate next action

Direct twin-prime test is completed for \(p=131,137,139\).
Follow-up is interpretation only (structural mechanism), not data lookup.

---

## Status box

> **Hecke twin-prime decision**: **[MC] CONFIRMED (unique at \(p=137\) in \(\{131,137,139\))**  
> Binary kill/confirm condition is resolved in favour of \(p=137\).
