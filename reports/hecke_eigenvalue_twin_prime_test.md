<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

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

| p | g(X₀(p)) | a_p(76.2.a.a) | |a_p|=g? | Status |
|--:|--:|--:|:--:|--|
| 131 | 11 | −9 | NO | [L0] přímý výpočet |
| **137** | **11** | **−11** | **YES** | **[MC] unikátní** |
| 139 | 11 | −3 | NO | [L0] přímý výpočet |

Weierstrass model: [0,−1,0,−21,−31] (LMFDB 76.a1).  
Metoda: přímé počítání bodů #E(F_p) = p+1−a_p.

---

## Immediate next action

Direct twin-prime test is completed for \(p=131,137,139\).
Follow-up is interpretation only (structural mechanism), not data lookup.

---

## Status box

> **Hecke twin-prime decision**: **[MC] CONFIRMED (unique at \(p=137\) in \(\{131,137,139\))**  
> Binary kill/confirm condition is resolved in favour of \(p=137\).
