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


# Prime-Stable Solutions: Full Structural Scan

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Status**: Computational verification — [L0]; analytic argument — [L1 partial];
Gamma sanity check — [L0] ($S_{\text{ren}}$ gives same stable set, non-canonical
~400 cluster excluded; see §11)  
**Companion files**:
- `canonical/alpha/prime_stability_set.tex` — formal derivation
- `canonical/alpha/veff_corrected.tex` — V_eff derivation
- `canonical/alpha/modular_prime_attractor_theorem.tex` — B-coefficient context

---

## 1. Problem Statement

Identify all primes $p$ that are **prime-stable**: $p$ minimizes
$$V(q;\,B(p)) = q^2 - B(p)\,q\ln q$$
over all primes $q$, where $B(p) = (p+1)/3$.

This is a *structural* question: find the complete set, not just verify one prime.

---

## 2. Stability Condition

A prime $p$ is prime-stable iff
$$B_{\text{low}}(p) < \frac{p+1}{3} < B_{\text{high}}(p)$$

where the bounds are set by the nearest primes $p_-$ (largest prime below $p$) and
$p_+$ (smallest prime above $p$):

$$B_{\text{low}}(p) = \frac{p^2 - p_-^2}{p\ln p - p_-\ln p_-}, \qquad
  B_{\text{high}}(p) = \frac{p_+^2 - p^2}{p_+\ln p_+ - p\ln p}$$

**Nearest-prime dominance** (verified numerically for all stable primes): the
tightest lower/upper constraints always come from $p_-$ and $p_+$, not from
distant primes.

---

## 3. Complete Table of Stable Primes

Exhaustive search over all primes $p \leq 10{,}000$, with $V(q; B(p))$ evaluated
for all primes $q \leq 100{,}000$.

| $p$ | $p_-$ | $p_+$ | $B(p)$ | $B_{\text{low}}$ | $B_{\text{high}}$ | $\Delta_-$ | $\Delta_+$ |
|----:|------:|------:|-------:|-----------------:|------------------:|-----------:|-----------:|
| 2   | —     | 3     | 1.0000 | $-\infty$        | 2.6184            | $\infty$   | 1.6184     |
| 127 | 113   | 131   | 42.6667| 41.4728          | 44.0290           | 1.1939     | 1.3623     |
| 137 | 131   | 139   | 46.0000| 45.4410          | 46.5646           | 0.5590     | 0.5646     |
| 139 | 137   | 149   | 46.6667| 46.5646          | 48.2443           | 0.1020     | 1.5777     |
| 151 | 149   | 157   | 50.6667| 49.9116          | 51.0197           | 0.7551     | 0.3530     |
| 157 | 151   | 163   | 52.6667| 51.0197          | 52.6739           | 1.6470     | **0.0072** |

**Complete stable set**: $\mathcal{S} = \{2,\;127,\;137,\;139,\;151,\;157\}$  
**$|\mathcal{S}| = 6$**

---

## 4. Near-Misses

Primes that fail stability by a small margin on one side:

| $p$ | $B(p)$ | $B_{\text{low}}$ | $B_{\text{high}}$ | Failure | Margin |
|----:|-------:|-----------------:|------------------:|---------|-------:|
| 131 | 44.000 | 44.029           | 45.441            | lower   | −0.029 |
| 149 | 50.000 | 48.244           | 49.912            | upper   | −0.088 |
| 163 | 54.667 | 52.674           | 54.046            | upper   | −0.621 |

---

## 5. V-Difference Tables

### $p = 137$, $B = 46.000$

| $q$ | $V(q; 46) - V(137; 46)$ |
|----:|------------------------:|
| 113 | +432.76                 |
| 127 | +65.98                  |
| 131 | +19.78                  |
| **137** | **0** (minimum)     |
| 139 | +6.69                   |
| 149 | +140.67                 |
| 151 | +187.69                 |

### $p = 157$, $B = 52.667$ (smallest upper margin)

| $q$ | $V(q; 52.667) - V(157; 52.667)$ |
|----:|--------------------------------:|
| 149 | +92.78                          |
| 151 | +59.66                          |
| **157** | **0** (minimum)             |
| 163 | **+0.26** ← nearest competitor  |
| 167 | +33.95                          |

### $p = 139$, $B = 46.667$ (smallest lower margin)

| $q$ | $V(q; 46.667) - V(139; 46.667)$ |
|----:|--------------------------------:|
| 131 | +44.58                          |
| **137** | **+1.21** ← nearest competitor  |
| **139** | **0** (minimum)             |
| 149 | +94.18                          |

---

## 6. Asymptotic Analysis

### 6.1 Leading-order condition

To leading order in $p$, the upper stability condition becomes:
$$\frac{p+1}{3} < \frac{2p}{\ln p + 1} \;\Longleftrightarrow\; \ln p < 5 \;\Longleftrightarrow\; p < e^5 \approx 148.4$$

### 6.2 $B(p)$ vs stationarity value $B^*(p) = 2p/(\ln p + 1)$

| $p$  | $B(p)$  | $B^*(p)$ | $B(p)/B^*(p)$ | Regime |
|-----:|--------:|---------:|--------------:|--------|
| 100  | 33.667  | 35.681   | 0.944         | $B < B^*$ |
| 127  | 42.667  | 43.462   | 0.982         | $B < B^*$ |
| 137  | 46.000  | 46.284   | **0.994**     | closest |
| 149  | 50.000  | 49.634   | 1.007         | crossover |
| 157  | 52.667  | 51.847   | 1.016         | $B > B^*$ |
| 200  | 67.000  | 63.509   | 1.055         | $B > B^*$ |
| 500  | 167.000 | 138.608  | 1.205         | $B \gg B^*$ |

The crossover ($B(p) = B^*(p)$) occurs near $p \approx 144$–$148$.  This is
where the stability window closes for growing $p$.

### 6.3 Required prime gap for stability beyond $e^5$

For $p > e^5$, a prime $p$ can still be stable if the gap above it is unusually large:
$$g_+ \;\gtrsim\; \frac{p(\ln p - 5)}{2}$$

| $p$  | $g_{\text{required}}$ | typical gap $\ln p$ | ratio |
|-----:|----------------------:|--------------------:|------:|
| 157  | 4.4                   | 5.1                 | 0.9 ✓ (gap = 6) |
| 200  | 29.8                  | 5.3                 | 5.6 ✗ |
| 300  | 105.6                 | 5.7                 | 18.5 ✗ |
| 1000 | 953.9                 | 6.9                 | 138 ✗ |

For $p \geq 300$, the required gap exceeds even Cramér-conjectured maximal gaps
($\sim \ln^2 p \lesssim 40$).

### 6.4 Conclusion on finiteness

**The set $\mathcal{S}$ is finite.**  No prime beyond 157 can be prime-stable.
The argument is tight: 157 survives only because $\ln 157 \approx 5.056 \approx 5$
and it happens to have a local gap of 6 above it (to 163), giving a margin of 0.0072.

---

## 7. Pattern Detection

### 7.1 Residue classes

| $p$ | $\bmod 6$ | $\bmod 12$ | $\bmod 24$ | $\bmod 30$ |
|----:|----------:|-----------:|-----------:|-----------:|
| 2   | 2         | 2          | 2          | 2          |
| 127 | 1         | 7          | 7          | 7          |
| 137 | 5         | 5          | 17         | 17         |
| 139 | 1         | 7          | 19         | 19         |
| 151 | 1         | 7          | 7          | 1          |
| 157 | 1         | 1          | 13         | 7          |

**No modular pattern detected.** The residues are distributed across multiple
classes.  The concentration in $\{127, \ldots, 157\}$ reflects the finiteness
window, not arithmetic structure.

### 7.2 Prime gaps around stable primes

| $p$ | gap below | gap above |
|----:|----------:|----------:|
| 127 | 14        | 4         |
| 137 | 6         | 2         |
| 139 | 2         | 10        |
| 151 | 2         | 6         |
| 157 | 6         | 6         |

Note: 137 and 139 are a twin prime pair ($\text{gap} = 2$), and 149–151 are
another twin pair.  The stability of both elements of each twin pair arises
because the small gap (2) between them places each barely inside the other's
stability window.

---

## 8. Modular Reformulation

Since $\mu(\Gamma_0(p)) = p+1$ for prime $p$, we have $B(p) = \mu(\Gamma_0(p))/3$.
The stability condition is:
$$\mu(\Gamma_0(p)) \cdot (\ln p + 1) < 6p$$

This is a **modular index inequality**.  Whether this has a natural interpretation
in terms of Hecke eigenvalues or Atkin–Lehner involutions is **[Open]** (Gap G-Bmod).

---

## 9. Computation Code

```python
import math

def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            for j in range(i*i, n+1, i):
                is_p[j] = False
    return [i for i in range(2, n+1) if is_p[i]]

def V(q, B):
    return q**2 - B * q * math.log(q)

def B_of(p):
    return (p + 1) / 3

primes = sieve(100_000)

def is_prime_stable(p, primes_list):
    B = B_of(p)
    Vp = V(p, B)
    for q in primes_list:
        if q != p and V(q, B) <= Vp:
            return False
    return True

stable = [p for p in primes if p <= 10_000 and is_prime_stable(p, primes)]
# Result: [2, 127, 137, 139, 151, 157]
```

---

## 10. Summary

| Question | Answer |
|----------|--------|
| Does the infinite stable set exist? | **No** — the set is finite |
| Complete stable set | $\{2, 127, 137, 139, 151, 157\}$ |
| Analytic condition | $\ln p < 5$, i.e.\ $p < e^5 \approx 148$ (with gap corrections for 151, 157) |
| Density of solutions | Zero (finite set in infinite primes) |
| Approximate spacing | All in $[127, 157]$, range 30 |
| Structural pattern | None; set determined by local prime-gap statistics |
| Modular reformulation | $\mu(\Gamma_0(p))(\ln p + 1) < 6p$ — **[Open]** |
| Gamma consistency | $\mathcal{S}_{\text{ren}} = \mathcal{S}$ — unchanged under $V_{\text{ren}}$ (see §11) |

---

> ⚠️ **Warning: ~400 cluster is a non-canonical artefact**
>
> Replacing $p\ln p$ directly by $\ln\Gamma(p+1)$ (without renormalisation)
> produces a different stable set $\{2,\,389,\,397,\,401,\,409,\,421\}$ near
> $p \approx e^6 \approx 403$.  This cluster is an artefact of the
> unrenormalised Gamma entropy model.  **It must not be interpreted within the
> canonical framework** and is not a refinement of the result above.
> See §11.5 for details.

---

## 11. Gamma Entropy Sanity Check [Numerical]

### 11.1 Role of the Gamma Function

The canonical entropy in the stability model is $q\ln q$.  The Gamma function
enters only as a tool for **continuous interpolation** and **derivative
computation**: it is never used to replace $q\ln q$ directly.

Stirling's series:
$$\ln\Gamma(q+1) = q\ln q - q + \tfrac{1}{2}\ln(2\pi q) + \frac{1}{12q} + O(q^{-3})$$

The difference $q\ln q - \ln\Gamma(q+1) = q - \frac{1}{2}\ln(2\pi q) + O(q^{-1})$
grows without bound, so direct replacement would be a **non-perturbative change**
incompatible with the canonical model.

### 11.2 Renormalised Entropy $S_{\text{ren}}$

The correct continuous analogue of $q\ln q$ is the **renormalised entropy**:
$$S_{\text{ren}}(q) := \ln\Gamma(q+1) + q - \tfrac{1}{2}\ln(2\pi q)$$

By Stirling:
$$S_{\text{ren}}(q) = q\ln q + \frac{1}{12q} + O(q^{-3})$$

So $S_{\text{ren}}(q) = q\ln q + O(q^{-1})$ — matching the canonical entropy to
sub-part-per-million precision at all stable primes.

| $p$ | $p\ln p$ | $S_{\text{ren}}(p)$ | $S_{\text{ren}} - p\ln p$ | $1/(12p)$ |
|----:|---------:|--------------------:|--------------------------:|----------:|
| 127 | 615.2118 |  615.2124 | $6.56 \times 10^{-4}$ | $6.562 \times 10^{-4}$ |
| 137 | 674.0374 |  674.0380 | $6.08 \times 10^{-4}$ | $6.083 \times 10^{-4}$ |
| 139 | 685.8919 |  685.8925 | $6.00 \times 10^{-4}$ | $5.995 \times 10^{-4}$ |
| 151 | 757.6093 |  757.6098 | $5.52 \times 10^{-4}$ | $5.519 \times 10^{-4}$ |
| 157 | 793.8306 |  793.8311 | $5.31 \times 10^{-4}$ | $5.308 \times 10^{-4}$ |

(Three-term Stirling matches to better than $10^{-8}$.)

### 11.3 Stable Set is Unchanged under $V_{\text{ren}}$

The renormalised potential $V_{\text{ren}}(q;B) = q^2 - B\,S_{\text{ren}}(q)$
gives stability bounds differing from the canonical bounds by $O(p^{-2})$,
far below the margins $\Delta_\pm$ of any stable prime.

Stability bounds under $V_{\text{ren}}$:

| $p$ | $p_-$ | $p_+$ | $B(p)$ | $B^{\text{ren}}_{\text{low}}$ | $B^{\text{ren}}_{\text{high}}$ | $\Delta_-$ | $\Delta_+$ |
|----:|------:|------:|-------:|------------------------------:|-------------------------------:|-----------:|-----------:|
| 2   | —     | 3     | 1.0000 | $-\infty$                     | 2.6373                         | $\infty$   | 1.6373     |
| 127 | 113   | 131   | 42.6667 | 41.4729                      | 44.0291                        | 1.1938     | 1.3624     |
| 137 | 131   | 139   | 46.0000 | 45.4410                      | 46.5647                        | 0.5590     | 0.5647     |
| 139 | 137   | 149   | 46.6667 | 46.5647                      | 48.2444                        | 0.1020     | 1.5777     |
| 151 | 149   | 157   | 50.6667 | 49.9116                      | 51.0197                        | 0.7550     | 0.3530     |
| 157 | 151   | 163   | 52.6667 | 51.0197                      | 52.6739                        | 1.6470     | **0.0073** |

**Complete stable set under $V_{\text{ren}}$**: $\mathcal{S}_{\text{ren}} = \{2, 127, 137, 139, 151, 157\} = \mathcal{S}$ ✓

### 11.4 Computation Code ($V_{\text{ren}}$)

```python
import math

def S_ren(q):
    return math.lgamma(q + 1) + q - 0.5 * math.log(2 * math.pi * q)

def V_ren(q, B):
    return q**2 - B * S_ren(q)

def is_prime_stable_ren(p, primes_list):
    B = (p + 1) / 3
    Vp = V_ren(p, B)
    return all(V_ren(q, B) > Vp for q in primes_list if q != p)

stable_ren = [p for p in primes if p <= 10_000 and is_prime_stable_ren(p, primes)]
# Result: [2, 127, 137, 139, 151, 157]  ← same as canonical
```

### 11.5 Revalidation Note

> **⚠ Stable set must be revalidated under exact entropy.**
>
> The renormalised form $S_{\text{ren}}(p)$ confirms $\mathcal{S}$ unchanged — this
> is the correct [L0] consistency check.  Any alternative entropy definition that
> does **not** preserve $S(p) \sim p\ln p$ to leading order must be treated as a
> different model and validated independently with a full prime scan.  In particular,
> direct substitution $q\ln q \to \ln\Gamma(q+1)$ (without renormalisation) is
> **not** a consistency check — it defines a different canonical model and is
> **forbidden** in the UBT prime stability framework.

### 11.6 Non-canonical Gamma Variant (Excluded)

Direct substitution $q\ln q \to \ln\Gamma(q+1)$ without renormalisation shifts
the stationarity condition from $B^*(p) = 2p/(\ln p + 1)$ to
$B^*_\Gamma(p) \approx 2p/\ln p$, moving the stability window from
$\ln p < 5$ ($p \lesssim e^5 \approx 148$) to $\ln p < 6$
($p \lesssim e^6 \approx 403$).

The resulting stable set is:

$$\mathcal{S}_\Gamma = \{2,\;389,\;397,\;401,\;409,\;421\}$$

This is a **different model** with a shifted entropy scale.  It is **not** a
refinement of the canonical model.  The original set $\mathcal{S}$ is not
"non-robust" — it is the unique result of the canonical entropy $q\ln q$.

> **The ~400 cluster must not be interpreted within the canonical framework.**
> It arises only under the non-renormalised Gamma entropy and is excluded.

