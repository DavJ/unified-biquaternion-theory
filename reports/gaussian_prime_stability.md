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


# Gaussian Prime Stability: Extension to ℤ[i]

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Status**: Computational verification — [L0]  
**Companion files**:
- `canonical/alpha/prime_stability_set.tex` — integer prime stability derivation (§S8–S9)
- `reports/prime_stability_scan.md` — integer prime stability tables
- `reports/continuous_gamma_entropy_scan.md` — continuous Gamma-entropy scan
- `reports/gaussian_prime_stability_lattice.png` — lattice visualization

---

## 1. Problem Statement

Extend the prime-stability potential from integer primes to Gaussian integers
$z = a + bi \in \mathbb{Z}[i]$.

**Model**:

$$V(z) \;=\; N(z)^2 \;-\; B\,\ln\Gamma(N(z)+1), \qquad N(z) = a^2+b^2$$

with the self-referential coupling $B = B(N(z)) = (N(z)+1)/3$, matching the
Gamma-entropy integer model from §S8 of `prime_stability_set.tex`.

**Stability**: A Gaussian prime $z$ is *GP-stable* if

$$V(N(z);\,B(N(z))) \;<\; V(N(w);\,B(N(z))) \qquad \forall\; w \in \mathcal{GP},\; N(w) \neq N(z)$$

where $\mathcal{GP}$ denotes the set of all Gaussian primes (exhaustive, not just
nearest neighbors).  Since $V$ depends only on the norm, stability reduces to a
condition on the **norm** $n = N(z)$.

---

## 2. Gaussian Prime Norms

### 2.1 Classification

Every Gaussian prime $\pi \in \mathbb{Z}[i]$ (up to units $\{1,i,-1,-i\}$) falls
into one of three classes:

| Class | Condition | Representative | Norm |
|-------|-----------|----------------|------|
| Special | $p = 2$ | $1+i$ | $N=2$ |
| **Complex** | $p \equiv 1\pmod{4}$ prime | $a+bi$, $a^2+b^2=p$ | $N = p$ |
| **Axis** | $p \equiv 3\pmod{4}$ prime | $p + 0\cdot i$ | $N = p^2$ |

For $N < 50{,}000$:

| Type | Count | Description |
|------|------:|-------------|
| Complex GP norms | 2550 | $\{2\} \cup \{p \text{ prime}: p \equiv 1 \pmod{4},\; p < 50000\}$ |
| Axis GP norms | 26 | $\{p^2: p \equiv 3 \pmod{4}$ prime$,\; p^2 < 50000\}$, i.e.\ prime $p \leq 223$ |
| **Total** | **2576** | |

### 2.2 Thinning effect

The GP-norm set is strictly sparser than the integer prime set.  Integer primes
$p \equiv 3 \pmod{4}$ — which include 127, 131, 139, 149, 151 — contribute norms
$p^2$ (very large), not $p$ itself.  This **removes** these primes from the
neighborhood of 137 in the norm set:

| Integer prime | mod 4 | GP-norm value | Near 137? |
|----:|-------:|--------------|:-------:|
| 113 | 1 | 113 | ✓ |
| 127 | 3 | 16129 | ✗ (far) |
| 131 | 3 | 17161 | ✗ (far) |
| **137** | **1** | **137** | **✓** |
| 139 | 3 | 19321 | ✗ (far) |
| 149 | 1 | 149 | ✓ |
| 151 | 3 | 22801 | ✗ (far) |
| 157 | 1 | 157 | ✓ |

GP-norms in $[100, 200]$: $\{101, 109, 113, 121, 137, 149, 157, 173, 181, 193, 197\}$

The nearest GP-norms to 137 are **121** (below, gap 16) and **149** (above, gap 12) —
compared to 131 (below, gap 6) and 139 (above, gap 2) in the integer prime set.

---

## 3. Degeneracy $r_2(n)$

The degeneracy $r_2(n)$ counts all representations $n = a^2 + b^2$ over $\mathbb{Z}$
(including signs and order):

$$r_2(n) = 4\bigl(d_1(n) - d_3(n)\bigr)$$

where $d_k(n) = \#\{d \mid n : d \equiv k \pmod{4}\}$.

For GP-norm types:

| GP-norm type | $r_2(n)$ | $S(n) = \ln r_2(n)$ | Associates in $\mathbb{Z}[i]$ |
|--------------|:--------:|:-------------------:|:-----------------------------:|
| $n = 2$ | 4 | $\ln 4 \approx 1.386$ | 4 |
| $n = p \equiv 1\pmod{4}$ (prime) | 8 | $\ln 8 \approx 2.079$ | 8 (if $a \neq b$) |
| $n = p^2$, $p \equiv 3\pmod{4}$ | 4 | $\ln 4 \approx 1.386$ | 4 |

All complex GP-norms (primes $\equiv 1 \pmod{4}$) have $r_2 = 8$; axis GP-norms
$p^2$ have $r_2 = 4$.

### $r_2$ for GP-norms near 137

| $n$ | type | $r_2(n)$ | $S(n) = \ln r_2$ | GP-stable? |
|----:|:----:|:--------:|:----------------:|:----------:|
| 101 | complex | 8 | 2.079 | — |
| 109 | complex | 8 | 2.079 | — |
| 113 | complex | 8 | 2.079 | — |
| 121 | axis ($11^2$) | 4 | 1.386 | — |
| **137** | **complex** | **8** | **2.079** | **—** |
| 149 | complex | 8 | 2.079 | — |
| 157 | complex | 8 | 2.079 | — |
| 173 | complex | 8 | 2.079 | — |

The Gaussian prime with $N(z) = 137$ is $z = 11 + 4i$ (and its 7 associates:
$\{11+4i, 4+11i, -11+4i, \ldots\}$).

---

## 4. GP-Stable Norms

### 4.1 Exhaustive search results

Exhaustive search over all 2576 GP-norms $\leq 50{,}000$, testing stability
against all other GP-norms.

**Complete GP-stable norm set:**

$$\mathcal{S}_{\mathrm{GP}} = \{2,\; 373,\; 389,\; 397,\; 401,\; 409,\; 421,\; 433,\; 461,\; 49993\}$$

### 4.2 Stability bounds table

| Norm | $B(n)$ | $B_{\text{low}}$ | $B_{\text{high}}$ | $\Delta_-$ | $\Delta_+$ | type | GP rep | $r_2$ |
|-----:|-------:|-----------------:|------------------:|-----------:|-----------:|:----:|:------:|:-----:|
| 2 | 1.000 | $-\infty$ | 5.129 | $+\infty$ | 4.129 | complex | $1+i$ | 4 |
| 373 | 124.667 | 124.266 | 128.196 | 0.401 | 3.529 | complex | $18+7i$ | 8 |
| 389 | 130.000 | 128.196 | 131.547 | 1.804 | 1.547 | complex | $17+10i$ | 8 |
| 397 | 132.667 | 131.547 | 133.217 | 1.120 | 0.551 | complex | $19+6i$ | 8 |
| 401 | 134.000 | 133.217 | 134.885 | 0.783 | 0.885 | complex | $20+1i$ | 8 |
| 409 | 136.667 | 134.885 | 137.658 | 1.781 | 0.991 | complex | $20+3i$ | 8 |
| 421 | 140.667 | 137.658 | 140.972 | 3.009 | 0.306 | complex | $15+14i$ | 8 |
| 433 | 144.667 | 140.972 | 144.825 | 3.694 | 0.158 | complex | $17+12i$ | 8 |
| 461 | 154.000 | 149.752 | 156.837 | 4.248 | 2.837 | complex | $19+10i$ | 8 |
| 49993 | 16664.667 | 9238.131 | $+\infty$ | 7426.536 | $+\infty$ | complex | $213+68i$ | 8 |

The norm 49993 is stable only because it is the largest GP-norm in the search range
(no upper competitor); it is a boundary artefact.

### 4.3 Near-misses

| $n$ | $B(n)$ | $B_{\text{low}}$ | $B_{\text{high}}$ | Failure |
|----:|-------:|-----------------:|------------------:|:--------|
| 353 | 118.000 | 119.750 | 121.447 | lower ($-1.750$) |
| 449 | 150.000 | 144.825 | 148.112 | upper ($-1.888$) |
| 457 | 152.667 | 148.112 | 149.752 | upper ($-2.915$) |

---

## 5. Comparison with Integer Stable Sets

### 5.1 Three-model comparison

| Model | Potential | Stable set |
|-------|-----------|:-----------|
| Integer, leading | $V = p^2 - B\,p\ln p$ | $\{2,\;127,\;137,\;139,\;151,\;157\}$ |
| Integer, exact Γ | $V = p^2 - B\,\ln\Gamma(p+1)$ | $\{2,\;389,\;397,\;401,\;409,\;421\}$ |
| **GP, exact Γ** | $V = n^2 - B\,\ln\Gamma(n+1)$ | $\{2,\;373,\;389,\;397,\;401,\;409,\;421,\;433,\;461,\ldots\}$ |

### 5.2 Why the GP set is larger

The core cluster $\{389, 397, 401, 409, 421\}$ appears in **both** the integer Γ
model and the GP model — these five norms are stable in both settings.

The GP set adds $\{373, 433, 461\}$ because the GP-norm set is sparser: integers
$p \equiv 3 \pmod{4}$ are absent as direct norms, widening the gaps around 373,
433, and 461.  Specifically:

- $373$: in the integer prime set, 373 is flanked closely by 367 and 379 (gaps 6,6);
  in the GP-norm set, 367 and 379 are absent ($\equiv 3 \bmod 4$), widening both gaps.
- $433$ and $461$: similar gap-widening allows stability.

### 5.3 Integer stable primes in the GP context

| $p$ (int.\ stable) | mod 4 | GP-norm | $B(n)$ | $B_{\text{low}}$ | $B_{\text{high}}$ | GP-stable? |
|----:|-----:|--------:|-------:|-----------------:|------------------:|:----------:|
| 2 | 2 | 2 | 1.000 | $-\infty$ | 5.129 | **Yes** |
| 127 | 3 | 16129 | 5376.7 | 3326.6 | 3330.7 | No |
| 137 | 1 | 137 | 46.000 | 53.053 | 57.591 | No |
| 139 | 3 | 19321 | 6440.7 | 3914.4 | 3916.6 | No |
| 151 | 3 | 22801 | 7600.7 | 4542.3 | 4546.0 | No |
| 157 | 1 | 157 | 52.667 | 60.792 | 64.597 | No |

**Key finding**: None of the integer-leading-stable primes (except $p=2$) are
GP-stable.  For complex-type primes (137, 157), $B(n) < B_{\text{low}}$ — the
coupling is too weak to sustain stability.  For axis-type primes (127, 139, 151),
their GP-norms are $p^2 \gg p$, giving enormous $B(p^2)$ values that far exceed
$B_{\text{high}}(p^2)$.

---

## 6. Analysis of Norm 137

### 6.1 GP representation

$$z = 11 + 4i, \qquad N(z) = 121 + 16 = 137.$$

All eight associates: $\pm 11 \pm 4i$, $\pm 4 \pm 11i$.  Degeneracy $r_2(137) = 8$.

### 6.2 Stability failure

Under $B = B(137) = 46$:

$$B_{\text{low}}(137) = 53.05 > 46.00 = B(137).$$

The coupling $B(137) = 46$ is **7.05 below** the lower stability bound.
Equivalently, V has lower values at the neighboring GP-norm 113:

| $m$ | type | $V(m;\,46) - V(137;\,46)$ |
|----:|:----:|:------------------------:|
| 97  | complex | $-598.71$ ← V lower at 97 |
| 101 | complex | $-653.13$ |
| 109 | complex | $-687.45$ |
| 113 | complex | $-666.82$ |
| **137** | **complex** | **0** (reference) |
| 149 | complex | $+690.74$ |
| 157 | complex | $+1286.38$ |

Under the GP model with $B(137)=46$, the minimum over GP-norms near 137 is at
$n = 109$ (V most negative), not at 137.

### 6.3 Why 137 was integer-leading-stable but not GP-stable

Under the **integer leading** model ($V = p^2 - B\,p\ln p$):
- The stability crossover is at $\ln p \approx 5$, i.e.\ $p \approx e^5 \approx 148$.
- $B^*_\text{lead}(137) = 2 \times 137/(\ln 137 + 1) \approx 46.28 \approx B(137)$.
- 137 is near the crossover point, making it marginally stable.

Under the **Gamma** model ($V = p^2 - B\,\ln\Gamma(p+1)$):
- The stationarity shifts to $B^*_\Gamma(137) = 2 \times 137/\psi(138) \approx 55.65 > 46$.
- The stability window for 137 requires $B \in [53.05, 57.59]$, but $B(137) = 46$.
- The same shift applies in the GP setting (the 137 norm appears in both sets).

---

## 7. Stationarity Analysis

The stationarity condition $V'(n;B) = 0$ gives $B^*_\Gamma(n) = 2n/\psi(n+1) \approx 2n/\ln n$.

| $n$ | type | $B(n) = (n+1)/3$ | $B^*_\Gamma \approx 2n/\ln n$ | $B/B^*$ | regime |
|----:|:----:|:----------------:|:-----------------------------:|:-------:|:------:|
| 113 | complex | 38.000 | 47.762 | 0.796 | $B < B^*$ |
| 121 | axis | 40.667 | 50.418 | 0.807 | $B < B^*$ |
| 137 | complex | 46.000 | 55.650 | 0.827 | $B < B^*$ |
| 149 | complex | 50.000 | 59.513 | 0.840 | $B < B^*$ |
| 157 | complex | 52.667 | 62.062 | 0.849 | $B < B^*$ |
| 373 | complex | 124.667 | 122.074 | 1.021 | $B > B^*$ ✓ |
| 389 | complex | 130.000 | 130.431 | 0.997 | $B \approx B^*$ |
| 397 | complex | 132.667 | 132.661 | 1.000 | **crossover** |
| 401 | complex | 134.000 | 133.774 | 1.002 | $B > B^*$ |
| 409 | complex | 136.667 | 135.995 | 1.005 | $B > B^*$ |
| 421 | complex | 140.667 | 139.316 | 1.010 | $B > B^*$ |
| 433 | complex | 144.667 | 142.539 | 1.015 | $B > B^*$ |
| 461 | complex | 154.000 | 150.018 | 1.027 | $B > B^*$ |

The **crossover $B(n) = B^*_\Gamma(n)$** occurs near $n \approx 397$, consistent
with the analytic condition $\ln n \approx 6$ (i.e.\ $n \approx e^6 \approx 403$).
This is identical to the shift found in the integer Gamma model (§S8).

---

## 8. Visualization

![Gaussian prime lattice and V(n) profile](gaussian_prime_stability_lattice.png)

**Left panel**: Gaussian primes with $N(z) \leq 700$ plotted on the $\mathbb{Z}^2$
lattice.  Blue dots are complex GP (unstable), orange squares are axis GP (unstable),
red stars are stable GP norms.  Gold diamonds mark the $N=137$ family ($11+4i$
and associates).

**Right panel**: $V(n; B(n))$ for GP-norms $n \leq 700$.  The red stars show the
stable cluster near $n \approx 400$.  The gold diamond shows $N=137$, which lies
visibly below the envelope of the stable cluster.

---

## 9. Computation Code

```python
import math

def sieve(n):
    is_p = [True]*(n+1); is_p[0]=is_p[1]=False
    for i in range(2, int(n**0.5)+1):
        if is_p[i]:
            for j in range(i*i, n+1, i): is_p[j]=False
    return [i for i in range(2, n+1) if is_p[i]]

def find_complex_rep(p):
    a = int(math.isqrt(p))
    while a >= 1:
        r = p - a*a; b = int(math.isqrt(r))
        if b*b == r: return (max(a,b), min(a,b))
        a -= 1

# Build GP-norm list
NORM_LIMIT = 50_000
gp_norms = set()
for p in sieve(NORM_LIMIT):
    if p == 2:       gp_norms.add(2)
    elif p % 4 == 1: gp_norms.add(p)
    elif p*p <= NORM_LIMIT: gp_norms.add(p*p)

gp_norm_list = sorted(gp_norms)

def B_of(n): return (n+1)/3.0
def V(n, B): return n*n - B * math.lgamma(n+1)

def is_gp_stable(n):
    B = B_of(n); Vn = V(n, B)
    return all(V(m, B) > Vn for m in gp_norm_list if m != n)

stable = [n for n in gp_norm_list if is_gp_stable(n)]
# Result: [2, 373, 389, 397, 401, 409, 421, 433, 461, 49993]
```

---

## 10. Summary

| Question | Answer |
|----------|--------|
| Complete GP-stable set (norm ≤ 50000) | $\{2,\;373,\;389,\;397,\;401,\;409,\;421,\;433,\;461,\;49993\}$ |
| Matches integer Γ-stable set? | **Superset**: all 5 of $\{389,397,401,409,421\}$ plus $\{373,433,461\}$ |
| Is $N=137$ GP-stable? | **No** — $B(137)=46 < B_{\text{low}}=53.05$ |
| Why is GP-stable set larger? | GP-norm set is sparser; $p\equiv 3\pmod 4$ primes absent, widening gaps |
| Stability crossover norm | $n \approx 397$ ($\ln n \approx 6 = e^6 \approx 403$) |
| $r_2(n)$ for complex GP-norms | 8 (all primes $\equiv 1\pmod 4$) |
| $r_2(n)$ for axis GP-norms | 4 (squares of primes $\equiv 3\pmod 4$) |
| All stable GP-norms are complex? | **Yes** (all stable norms are primes $\equiv 1\pmod 4$) |
| Does thinning affect 137? | Yes: gaps 127→137 (Δ=10→16) and 137→139 (Δ=2→12) widened, but still not enough |
