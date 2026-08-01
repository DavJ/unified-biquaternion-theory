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
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# B-Coefficient Analysis: Why is B ≈ 46?

**Track**: `research_tracks/rg_nlogn/`  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Status**: [HEURISTIC] — numerical matching; no rigorous derivation  

---

## 1. The Problem

The prime-stability condition requires $B(p) = (p+1)/3$ to be a fixed constant
near the stable prime $p = 137$:

$$B(137) = \frac{137 + 1}{3} = \frac{138}{3} = 46.$$

The one-loop RG calculation (see `full_rg_derivation.tex`) predicts:
$$B_\text{1-loop} \approx \frac{n}{2\pi} \approx \frac{137}{6.283} \approx 21.8$$
$$B_\text{KK+winding} \approx \frac{n}{\pi} \approx \frac{137}{3.14} \approx 43.6$$

**Discrepancy**: $\Delta B = 46 - 43.6 = 2.4$, which is about 5.2% of $B$.

---

## 2. Survey of All Candidate Sources of B

### 2.1 Kaluza-Klein Tower (one-loop scalar)

$$B_\text{KK} = \frac{n}{2\pi}$$

**Status**: [HEURISTIC]  
**Evaluated at $n = 137$**: $B = 21.8$  
**Source**: $d=1$ one-loop integral; see loop_integrals_appendix.tex §2.

### 2.2 KK + Winding at Self-Dual Radius

$$B_\text{KK+wind} = \frac{n}{\pi}$$

**Status**: [HEURISTIC — requires T-duality at self-dual radius]  
**Evaluated at $n = 137$**: $B = 43.6$  
**Discrepancy from 46**: $\Delta B = 2.4$

### 2.3 Two-Loop Contribution

$$\delta B_\text{2-loop} \approx \frac{g^2 n}{16\pi^2}$$

**Status**: [HEURISTIC estimate]  
**Evaluated at $n = 137$, $g = 0.3$**: $\delta B \approx 0.05$  
**Verdict**: Negligible. Cannot explain $\Delta B = 2.4$.

### 2.4 Gauge Field Loops

In a gauge theory with group $G$, gauge bosons contribute to the one-loop
effective potential with a group-theory factor $b_0 = C(G)$ (Casimir):

$$\delta B_\text{gauge} = \frac{C(G) \cdot n}{2\pi}$$

For $\mathrm{SU}(N)$: $C(\mathrm{SU}(N)) = N$.

| Group | $C(G)$ | $\delta B$ at $n=137$ |
|-------|--------|-----------------------|
| $\mathrm{U}(1)$ | 0 | 0 |
| $\mathrm{SU}(2)$ | 2 | 43.6 |
| $\mathrm{SU}(3)$ | 3 | 65.4 |
| $\mathrm{SU}(2)\times\mathrm{U}(1)$ | 2 | 43.6 |
| $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ | 5 | 109 |

**Status**: [SPECULATIVE]  
**Verdict**: $\mathrm{SU}(2)$ gauge contribution alone gives $B \approx 43.6$.
A small additional piece ($\Delta B \approx 2.4$) from fermions or ghosts is not excluded.

### 2.5 Fermion Loops

Fermion loops contribute with a minus sign (opposite statistics):

$$\delta B_\text{fermion} = -\frac{N_f \cdot n}{2\pi}$$

For Standard Model: $N_f = 6$ quark flavours + 3 lepton families in each
generation = effectively $N_f \times$ representation dimension.

**Verdict**: Fermion loops would *reduce* $B$, not increase it.

### 2.6 Ghost Loops

In a gauge theory, Faddeev-Popov ghosts contribute with group factor $C(G)$
and fermionic statistics:

$$\delta B_\text{ghost} = +\frac{C(G) \cdot n}{4\pi}$$

(opposite sign compared to fermions, same sign as scalars).

For $\mathrm{SU}(2)$: $\delta B_\text{ghost} = 2 \times 137/(4\pi) \approx 21.8$.

**Total with ghosts**: $B_\text{KK+wind} + \delta B_\text{ghost} = 43.6 + 21.8 = 65.4$. **Too large.**

### 2.7 Summary Table

| Source | Formula | $B$ at $n = 137$ | Status |
|--------|---------|-----------------|--------|
| KK scalar (1-loop) | $n/(2\pi)$ | 21.8 | Heuristic |
| KK+winding scalar | $n/\pi$ | 43.6 | Heuristic |
| + gauge ($\mathrm{SU}(2)$ bosons) | $+ n\cdot C/\pi$ | large | Speculative |
| + ghost loops | partial | intermediate | Speculative |
| 2-loop correction | small | +0.05 | Heuristic |
| **Target** | $(p+1)/3$ | **46.0** | Empirical |

---

## 3. Sensitivity Analysis

### 3.1 Sensitivity to $n$ (which KK level dominates?)

$B(p) = (p+1)/3$ is prime-dependent. For nearby stable primes:

| $p$ | $B(p) = (p+1)/3$ | $n/(2\pi)$ | $n/\pi$ |
|-----|------------------|------------|---------|
| 127 | 42.67 | 20.22 | 40.4 |
| 137 | 46.00 | 21.80 | 43.6 |
| 139 | 46.67 | 22.12 | 44.2 |
| 151 | 50.67 | 24.03 | 48.1 |
| 157 | 52.67 | 24.99 | 50.0 |

**Observation**: The ratio $B(p) / (n/\pi)$ varies from 1.056 (at $p=127$) to
1.053 (at $p=157$). The ratio is approximately constant at $\approx 1.054$.

This suggests a systematic factor of $\approx 1.054$ missing from the KK+winding
formula.  The origin of this factor is an open problem.

### 3.2 Sensitivity to log base

The formula $V(n) = n^2 - Bn\ln n$ uses the natural logarithm.  If a different
base $\ln_a(n) = \ln n / \ln a$ is used:

$$B_a = B \cdot \ln a.$$

For $a = e$: $B_e = B = 46$.  
For $a = 2$: $B_2 = 46 \times 0.693 = 31.9$.  
For $a = 10$: $B_{10} = 46 \times 2.303 = 105.9$.

**Verdict**: The numerical value of $B$ is tied to the natural logarithm; this
is dimensionally natural and not a free choice.

### 3.3 Sensitivity to normalization of $V(n)$

If $V(n)$ is normalized differently (e.g.\ $V(n) = n^2/R^2 - Bn\ln n / R$
for radius $R$), then $B$ rescales.  At $R = 1$, the formulas coincide.

---

## 4. The $137/(3\pi) \approx 14.5$ Coincidence

Note that $46 \approx 3\pi \times 4.88$.  Also:
$$\frac{137}{3} = 45.67 \approx 46.$$

Specifically, $B(137) = (137+1)/3 = 138/3 = 46$ is **exact** by definition of the
formula.  The question is whether the formula $B(p) = (p+1)/3$ has a physical
derivation or is phenomenological.

**Status of $B(p) = (p+1)/3$**: [HEURISTIC] — the formula reproduces the
stable primes empirically; a derivation from UBT interactions is an open gap.

---

## 5. Falsification Conditions

### 5.1 A failed derivation of $B = 46$

If a complete two-loop calculation of the UBT KK effective potential yields
$B \neq 46$ (even with all known corrections), this falsifies the RG interpretation.

### 5.2 $B$ sensitivity to $V$ perturbations

The perturbation analysis (`prime_stability/perturbation_analysis.md`) shows that
the stable set $\mathcal{S} = \{2,127,137,139,151,157\}$ depends sensitively on
$B$.  If the true $B$ differs by more than the stability window $\Delta_{\pm}(p)$
from the assumed value, the prime attractor collapses.

For $p = 157$: $\Delta_+ = 0.0072$ (very small margin).  This means $B(157) = 52.6667$
must be correct to within 0.0072 — a very tight constraint on the RG calculation.

### 5.3 Alternative non-RG origins of B

If $B(p) = (p+1)/3$ arises from modular arithmetic rather than loop integrals
(e.g., from the Bernoulli numbers or Eisenstein series), the RG interpretation
is not needed or even wrong.

---

## 6. Open Problems

1. **Derive $B(p) = (p+1)/3$ from first principles** (RG, modular forms, or other).
2. **Explain the factor $\approx 1.054$** missing from the KK+winding estimate.
3. **Determine which fields contribute** to the effective potential in the UBT KK tower.
4. **Verify gauge invariance** of the full $B$ coefficient (including gauge ghosts).

---

**Last Updated**: 2026-05-06  
**Companion documents**: `full_rg_derivation.tex`, `loop_integrals_appendix.tex`
