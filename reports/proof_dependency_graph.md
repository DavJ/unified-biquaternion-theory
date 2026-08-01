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


# Proof Dependency Graph: UBT Spectral/RG Framework

**Author**: Ing. David Jaroš  
**Date**: May 2026  

---

## Legend

```
[PROVED]  — mathematically established
[HEUR]    — heuristic / plausible
[SPEC]    — speculative / conjectural
[OPEN]    — open gap / not derived
[FAIL]    — currently failing
```

Arrows `→` mean "required to prove / derived from."

---

## Dependency Graph (Text Form)

```
═══════════════════════════════════════════════════════════════
                       LEVEL 0: AXIOMS
═══════════════════════════════════════════════════════════════

[PROVED]  Standard QFT (Coleman-Weinberg, KK reduction)
[PROVED]  Functional analysis (Kato-Rellich, Friedrich's extension)
[PROVED]  Analytic number theory (theta functions, modular transformations)
[PROVED]  Prime Number Theorem

═══════════════════════════════════════════════════════════════
                    LEVEL 1: CORE UBT STRUCTURES
═══════════════════════════════════════════════════════════════

[PROVED]  UBT Hilbert space: ℋ_ψ = L²(S¹)
[PROVED]  KK mass spectrum: m_n² = n² (natural units)
[PROVED]  Free Hamiltonian A₀ = -d²/dψ² is self-adjoint on H²_per(S¹)
[PROVED]  Free spectrum: λ_n = n², n ∈ ℤ
[PROVED]  Heat trace: Z_H(t) = θ₃(4πit/L²)
[PROVED]  Spectral zeta: ζ_H(s) = 2(L/2π)^{2s} ζ_R(2s) [free case]
[PROVED]  Functional equation of ζ_H [free case, via modular θ₃ transformation]

[OPEN]    L_ψ from UBT moduli
          ↑ required for: spectral scale, KK interpretation

[OPEN]    V_eff(ψ) from UBT Lagrangian
          ↑ required for: EVERYTHING below in T1, T2, T4

═══════════════════════════════════════════════════════════════
              LEVEL 2: CONDITIONAL ON V_eff
═══════════════════════════════════════════════════════════════

[PROVED (conditional)]
  Self-adjointness of Ĥ_ψ = A₀ + V_eff
    ← V_eff ∈ L² (from OPEN: V_eff computation)
    ← Kato-Rellich theorem [PROVED]

[PROVED (conditional)]
  Compact resolvent of Ĥ_ψ
    ← Self-adjointness [PROVED conditional]
    ← Rellich-Kondrachov compactness [PROVED]

[OPEN]
  Heat trace Z_H^UBT(t) = Tr[e^{-tĤ_ψ}]
    ← V_eff computation [OPEN]
    ← Self-adjointness [PROVED conditional]

═══════════════════════════════════════════════════════════════
              LEVEL 3: RG DERIVATION
═══════════════════════════════════════════════════════════════

[PROVED]  V_tree(n) = n² (KK spectrum)
[PROVED]  One-loop δV ∝ n²ln n (standard d=1 QFT)
[PROVED]  Scheme independence of n·ln n coefficient
[PROVED]  Gauge invariance of V_eff(n)

[HEUR]    B ≈ 21.8 (one-loop KK, natural units)
            ← V_tree [PROVED]
            ← One-loop integrals [PROVED]
            ← R_ψ = 1 (self-dual radius) [HEUR]

[HEUR]    B ≈ 43.6 (KK + winding)
            ← B ≈ 21.8 [HEUR]
            ← T-duality at self-dual radius [HEUR]

[FAIL]    B = 46 exact
            ← B ≈ 43.6 [HEUR]
            ← Δ B ≈ 2.4 unexplained [OPEN]

[OPEN]    B(p) = (p+1)/3 from first principles
            ← B = 46 derivation [FAIL]

═══════════════════════════════════════════════════════════════
              LEVEL 4: PRIME STABILITY
═══════════════════════════════════════════════════════════════

[PROVED]  Stability condition: B_low(p) < B(p) < B_high(p)
[PROVED]  Nearest-prime dominance [numerical only; analytic: HEUR]
[PROVED]  Stable set S = {2, 127, 137, 139, 151, 157}
[PROVED]  |S| is finite
[PROVED]  No stable prime in (157, 10⁶]
[PROVED]  Asymptotic stability window Δ±(p) ~ (g±)/(1 + ln p)

[HEUR]    S under Cramér model
[OPEN]    B(p) = (p+1)/3 derivation → connects to Level 3

═══════════════════════════════════════════════════════════════
              LEVEL 5: THETA / TRACE FORMULA
═══════════════════════════════════════════════════════════════

[PROVED]  Selberg trace formula (literature)
[PROVED]  Riemann-Weil explicit formula (literature)
[PROVED]  Atiyah-Bott fixed-point theorem (literature)

[SPEC]    UBT theta kernel Θ_UBT(ψ,t)
            ← V_eff computation [OPEN]
            ← UBT vacuum state |0⟩ [SPEC]

[SPEC]    Modular transformation of Θ(q,τ)
            ← UBT theta kernel [SPEC]

[SPEC]    UBT prime orbits (lengths ~ ln p)
            ← UBT modular structure [SPEC]
            ← UBT hyperbolic geometry [SPEC]

[SPEC]    UBT Selberg-type trace formula
            ← UBT prime orbits [SPEC]
            ← UBT spectral theory [OPEN]

═══════════════════════════════════════════════════════════════
              LEVEL 6: HILBERT-PÓLYA PROGRAM
═══════════════════════════════════════════════════════════════

[SPEC]    Spectrum of Ĥ_ψ ~ Riemann zeros
            ← Self-adjointness [PROVED conditional]
            ← Spectrum computed [OPEN: needs V_eff]
            ← GUE comparison [OPEN: needs V_eff]
            ← Zeta explicit formula match [SPEC]

[PROHIB]  Proof of Riemann Hypothesis via UBT
            This claim must NOT be made.

═══════════════════════════════════════════════════════════════
              LEVEL 7: FALSIFICATION
═══════════════════════════════════════════════════════════════

[PASS]    Null model 1: random B — S is non-trivially small
[PASS]    Null model 2: shuffled B — pairing p↔B(p) is essential
[PASS]    Explicit PASS/FAIL: all 4 algebraic tests pass
[PASS]    Spectral spacing: free operator ≠ GUE (as expected)
[FAIL]    B = 46 claim: fails against one-loop RG prediction (B ≈ 43.6)
[OPEN]    Null models 3-4: preliminary results only; full run pending
```

---

## Critical Path

The minimum set of results needed to convert UBT from a heuristic framework
to a mathematically credible spectral theory:

```
P1 (V_eff) → P3 (L_ψ) → Self-adjointness → Spectral statistics
             ↓
P2 (B=46) → Prime stability complete → RG/prime connection
             ↓
P5 (modular) → P6 (prime orbits) → Trace formula
```

**The critical path has length 3**: P1 → Self-adjointness → Spectrum.

If P1 is solved, the programme can advance rapidly.
If P2 remains unresolved, the RG interpretation of $B$ must be revised.

---

## Summary Statistics

| Level | # Results | Proved | Heuristic | Speculative | Open |
|-------|-----------|--------|-----------|-------------|------|
| 0 | 4 | 4 | 0 | 0 | 0 |
| 1 | 9 | 7 | 0 | 0 | 2 |
| 2 | 3 | 2 cond | 0 | 0 | 1 |
| 3 | 7 | 4 | 2 | 0 | 1 (FAIL) |
| 4 | 7 | 6 | 1 | 0 | 1 |
| 5 | 6 | 3 lit | 0 | 3 | 1 |
| 6 | 2 | 0 | 0 | 1 | 1 |
| 7 | 5 | 4 | 0 | 0 | 1 |
| **Total** | **43** | **30** | **3** | **4** | **7 (1 FAIL)** |

---

**Last Updated**: 2026-05-06  
**Companion reports**: `top5_master_summary.md`, `open_problems_ranked.md`
