<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Prime-Stable Solutions: Full Structural Scan

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Status**: Computational verification — [L0]; analytic argument — [L1 partial]  
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

---

## 11. Gamma-Function Entropy Reformulation

See `canonical/alpha/prime_stability_set.tex` §S8–S9 for full derivation.

### 11.1 Entropy definitions

The original entropy $S_\text{lead}(q) = q\ln q$ is only the leading asymptotic of
$\ln\Gamma(q+1)$.  Three models are compared:

| Model | Entropy $S(q)$ |
|-------|---------------|
| Leading (original) | $q \ln q$ |
| Stirling-truncated | $q\ln q - q + \tfrac{1}{2}\ln(2\pi q)$ |
| Exact $\Gamma$ | $\ln\Gamma(q+1)$ |

### 11.2 Complete stable sets under each model

Exhaustive search, $p \leq 10{,}000$, $q \leq 100{,}000$:

| Model | Stable set $\mathcal{S}$ |
|-------|:-------------------------|
| Leading | $\{2,\;127,\;137,\;139,\;151,\;157\}$ |
| Stirling-truncated | $\{2,\;389,\;397,\;401,\;409,\;421\}$ |
| Exact $\Gamma$ | $\{2,\;389,\;397,\;401,\;409,\;421\}$ |

**The original set is not robust.**  Adding the Stirling correction $-q$ shifts the
stability window from $\ln p < 5$ ($p \lesssim e^5 \approx 148$) to $\ln p < 6$
($p \lesssim e^6 \approx 403$), relocating the entire stable set.

### 11.3 Why the window shifts

| Model | Stationarity $B^*(p)$ | Crossover |
|-------|----------------------|-----------|
| Leading | $2p/(\ln p + 1)$ | $\ln p \approx 5$, $p \approx e^5 \approx 148$ |
| Exact $\Gamma$ | $2p/\psi(p+1) \approx 2p/\ln p$ | $\ln p \approx 6$, $p \approx e^6 \approx 403$ |

### 11.4 Exact Gamma stability bounds for the original candidates

| $p$ | $B(p)$ | $B_\text{low}^\Gamma$ | $B_\text{high}^\Gamma$ | Stable? |
|----:|-------:|-----------------------:|-----------------------:|:--------|
| 2   | 1.000  | $-\infty$              | 4.551 | **Yes** |
| 127 | 42.667 | 50.093 | 53.047 | **No** ($B < B_\text{low}$ by 7.43) |
| 137 | 46.000 | 54.677 | 55.974 | **No** ($B < B_\text{low}$ by 8.68) |
| 139 | 46.667 | 55.974 | 57.912 | **No** ($B < B_\text{low}$ by 9.31) |
| 151 | 50.667 | 59.833 | 61.110 | **No** ($B < B_\text{low}$ by 9.17) |
| 157 | 52.667 | 61.110 | 63.014 | **No** ($B < B_\text{low}$ by 8.44) |

---

## 12. Continuous Extension and Stationary Points near $1/\alpha$

See `reports/continuous_gamma_entropy_scan.md` for the full scan.  Summary:

$$V(x;\,B) = x^2 - B\,\ln\Gamma(x+1), \qquad V'(x;\,B) = 2x - B\,\psi(x+1).$$

Setting $V'(1/\alpha;\, B^*) = 0$ at $1/\alpha = 137.036$:

$$B^* = \frac{2 \times 137.036}{\psi(138.036)} \approx 55.662.$$

### 12.1 Nearest-prime projection

| Model / $B$ | $x^*$ | Projects to |
|-------------|------:|:-----------:|
| Leading, $B = B(137) = 46$ | 135.99 | **137** |
| Exact $\Gamma$, $B = B(137) = 46$ | 107.74 | 107 |
| Exact $\Gamma$, $B = B^* = 55.662$ | 137.036 | **137** |

Under both the original leading model (where $B(137) \approx B^*_\text{lead}$)
and the exact Gamma model (with the shifted coupling $B^*$), the continuous
minimum near $1/\alpha$ projects to $p = \mathbf{137}$.

The prime $p = 137$ achieves $V(137;\, B^*) - V(x^*;\, B^*) = +0.001$; the next
candidate, 139, yields $+3.08$ — a ratio of $\approx 3000$.

