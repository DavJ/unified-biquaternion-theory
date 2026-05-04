<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Prime-Stable Solutions: Full Structural Scan

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Status**: Computational verification — [L0]; analytic argument — [L1 partial];
Gamma extension — [L0] (numerical), [L1 partial] (analytic, see §11)  
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
| Complete stable set ($q\ln q$ model) | $\{2, 127, 137, 139, 151, 157\}$ |
| Analytic condition ($q\ln q$) | $\ln p < 5$, i.e.\ $p < e^5 \approx 148$ (with gap corrections for 151, 157) |
| Complete stable set ($\ln\Gamma$ model) | $\{2, 389, 397, 401, 409, 421\}$ — see §11 |
| Analytic condition ($\ln\Gamma$) | $\ln p < 6$, i.e.\ $p < e^6 \approx 403$ (with gap corrections for 409, 421) |
| Density of solutions | Zero (finite sets in infinite primes, for both models) |
| Structural pattern | None; set determined by local prime-gap statistics |
| Modular reformulation | $\mu(\Gamma_0(p))(\ln p + 1) < 6p$ — **[Open]** |

---

## 11. Gamma-Function Entropy Formulation

### 11.1 Motivation

The heuristic entropy $q\ln q$ used in §1–§8 is the leading term of
$\ln\Gamma(q+1) = \ln q!$.  Replacing it with the exact Gamma-function
entropy gives the potential

$$V_\Gamma(q;\,B) \;:=\; q^2 - B\,\ln\Gamma(q+1)$$

for which $\ln\Gamma(q+1) = \ln q!$ exactly for every positive integer $q$.

### 11.2 Stirling Expansion

Stirling's series:
$$\ln\Gamma(q+1) = q\ln q - q + \tfrac{1}{2}\ln(2\pi q) + \frac{1}{12q} + O(q^{-3})$$

Hence:
$$q\ln q - \ln\Gamma(q+1) = q - \tfrac{1}{2}\ln(2\pi q) - \frac{1}{12q} + O(q^{-3})$$

This difference grows without bound.  The two models are **not** asymptotically
equivalent for fixed $B$: the shift in $V$ is approximately $B \cdot (q -
\frac{1}{2}\ln 2\pi q)$, which is $O(Bq)$ and hence comparable in size to the
gradient $q^2$ for the relevant range of $B$.

| $p$ | $p\ln p$ | $\ln\Gamma(p+1)$ | $p\ln p - \ln\Gamma(p+1)$ | Stirling$_2$ error |
|----:|---------:|-----------------:|--------------------------:|-------------------:|
| 127 |  615.212 |  491.553 | 123.658 | $6.6 \times 10^{-4}$ |
| 137 |  674.037 |  540.417 | 133.620 | $6.1 \times 10^{-4}$ |
| 389 | 2331.555 | 1934.733 | 396.822 | $2.1 \times 10^{-4}$ |
| 421 | 2537.843 | 2126.889 | 410.954 | $2.0 \times 10^{-4}$ |

(Stirling$_3$, adding $+1/(12p)$, matches $\ln\Gamma(p+1)$ to better than $10^{-8}$.)

### 11.3 Stationarity and Threshold Shift

The continuous minimum of $V_\Gamma(\cdot;\,B)$ satisfies $2q = B\,\psi(q+1)$
where $\psi$ is the digamma function.  The stationarity value is
$$B^*_\Gamma(p) = \frac{2p}{\psi(p+1)} \approx \frac{2p}{\ln p} \quad\text{(large }p\text{)}$$

compared to $B^*(p) = 2p/(\ln p + 1)$ in the original model.  The upper
stability condition $B(p) < B^*_\Gamma(p)$ gives to leading order:

$$\frac{p+1}{3} < \frac{2p}{\ln p} \;\Longleftrightarrow\; \ln p < 6
  \;\Longleftrightarrow\; p < e^6 \approx 403$$

**The threshold shifts from $e^5 \approx 148$ to $e^6 \approx 403$.**

$B(p)$ vs $B^*_\Gamma(p)$ comparison:

| $p$ | $B(p)$ | $B^*_\Gamma(p) \approx 2p/\ln p$ | $B/B^*_\Gamma$ | Regime |
|----:|-------:|----------------------------------:|---------------:|--------|
| 127 | 42.667 | 52.39 | 0.814 | $B \ll B^*_\Gamma$ |
| 157 | 52.667 | 62.06 | 0.849 | $B \ll B^*_\Gamma$ |
| 300 | 100.333 | 105.16 | 0.954 | $B < B^*_\Gamma$ |
| 389 | 130.000 | 130.43 | **0.997** | near crossover |
| 397 | 132.667 | 132.66 | **1.000** | crossover |
| 421 | 140.667 | 139.32 | 1.010 | $B > B^*_\Gamma$ |
| 500 | 167.000 | 160.89 | 1.038 | $B > B^*_\Gamma$ |

Crossover $B(p) = B^*_\Gamma(p)$ occurs near $p \approx 397$.

### 11.4 Complete Stable Set under $V_\Gamma$

Exhaustive search over all primes $p \leq 10{,}000$ with $V_\Gamma(q;\,B(p))$
evaluated for all primes $q \leq 100{,}000$.

| $p$ | $p_-$ | $p_+$ | $B(p)$ | $B^\Gamma_{\text{low}}$ | $B^\Gamma_{\text{high}}$ | $\Delta_-$ | $\Delta_+$ |
|----:|------:|------:|-------:|------------------------:|-------------------------:|-----------:|-----------:|
| 2   | —     | 3     | 1.0000 | $-\infty$               | 4.5512                   | $\infty$   | 3.5512     |
| 389 | 383   | 397   | 130.0000 | 129.5928              | 131.5467                 | 0.4072     | 1.5467     |
| 397 | 389   | 401   | 132.6667 | 131.5467              | 133.2174                 | 1.1200     | 0.5507     |
| 401 | 397   | 409   | 134.0000 | 133.2174              | 134.8852                 | 0.7826     | 0.8852     |
| 409 | 401   | 419   | 136.6667 | 134.8852              | 137.3807                 | 1.7814     | 0.7140     |
| 421 | 419   | 431   | 140.6667 | 139.0396              | 140.6965                 | 1.6271     | **0.0298** |

**Complete Gamma stable set**: $\mathcal{S}_\Gamma = \{2,\;389,\;397,\;401,\;409,\;421\}$
**$|\mathcal{S}_\Gamma| = 6$**

### 11.5 Near-Misses (Gamma Model)

| $p$ | $B(p)$ | $B^\Gamma_{\text{low}}$ | $B^\Gamma_{\text{high}}$ | Failure | Margin |
|----:|-------:|------------------------:|-------------------------:|---------|-------:|
| 383 | 128.000 | 128.194 | 129.593 | lower | −0.194 |
| 379 | 126.667 | 126.793 | 128.194 | lower | −0.127 |
| 419 | 140.000 | 137.381 | 139.040 | upper | −0.960 |
| 431 | 144.000 | 140.697 | 142.349 | upper | −1.651 |

### 11.6 V-Difference Spot-Check

#### $p = 421$, $B = 140.6667$ (smallest upper margin in $\mathcal{S}_\Gamma$)

| $q$ | $V_\Gamma(q;\,140.667) - V_\Gamma(421;\,140.667)$ |
|----:|--------------------------------------------------:|
| 419 | +19.66 |
| **421** | **0** (minimum) |
| 431 | **+1.80** ← nearest competitor |
| 433 | +22.23 |

#### $p = 397$, $B = 132.6667$ (closest to crossover)

| $q$ | $V_\Gamma(q;\,132.667) - V_\Gamma(397;\,132.667)$ |
|----:|--------------------------------------------------:|
| 389 | +53.53 |
| **397** | **0** (minimum) |
| 401 | +13.20 ← nearest competitor |
| 409 | +119.78 |

### 11.7 Finiteness and Required Gap

For $p > e^6$, stability requires gap $g_+ > p(\ln p - 6)/3$:

| $p$ | $g_{\text{required}}$ | typical gap $\ln p$ | feasible? |
|----:|----------------------:|--------------------:|-----------|
| 421 | 5.98 | 6.04 | ✓ (gap = 10) |
| 431 | 9.50 | 6.07 | ✗ (gap = 2) |
| 500 | 35.77 | 6.21 | ✗ |
| 1000 | 302.59 | 6.91 | ✗ |

**The Gamma stable set is also finite.**  The set $\mathcal{S}_\Gamma$ is
complete: no prime beyond $421$ is prime-stable under $V_\Gamma$.

### 11.8 Computation Code (Gamma Model)

```python
import math

def V_gamma(q, B):
    return q**2 - B * math.lgamma(q + 1)

def is_prime_stable_gamma(p, primes_list):
    B = (p + 1) / 3
    Vp = V_gamma(p, B)
    for q in primes_list:
        if q != p and V_gamma(q, B) <= Vp:
            return False
    return True

primes = sieve(100_000)
stable_gamma = [p for p in primes if p <= 10_000 and is_prime_stable_gamma(p, primes)]
# Result: [2, 389, 397, 401, 409, 421]
```

### 11.9 Revalidation Note

> **⚠ Stable set must be revalidated under exact entropy.**
> The two potentials $V(q;B) = q^2 - Bq\ln q$ and $V_\Gamma(q;B) = q^2 - B\ln\Gamma(q+1)$
> produce completely different stable sets.  The shift is not a perturbative
> correction: the stability window moves by $\approx 262$ in prime-index space
> (from $[127,157]$ to $[389,421]$).  Any physical interpretation must specify
> which entropy definition is used, and all modular-structure and pattern
> analysis must be repeated for $\mathcal{S}_\Gamma$.

