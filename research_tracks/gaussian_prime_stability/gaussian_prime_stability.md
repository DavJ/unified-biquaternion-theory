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


# Gaussian Prime Stability — 2D Extension of the Prime Stability Model

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Track**: T3_ALPHA — Fine Structure Constant  
**Status**: Research track — NOT canonical; exploration only  
**Related files**:
- `canonical/alpha/prime_stability_set.tex` — formal 1D derivation (canonical)
- `reports/prime_stability_scan.md` — 1D numerical scan with Gamma consistency check

---

## Epistemic Notice

> ⚠️ **This document is exploratory, not a proof.**
>
> No new physical claims are asserted here beyond the canonical 1D model.
> The purpose is to define a self-consistent 2D extension of the prime stability
> framework to Gaussian integers, identify the natural analogues of the 1D
> quantities, and establish the baseline ($\lambda = 0$) result before any
> parameter is introduced.

---

## 1. Recap: Canonical 1D Model

The canonical potential is
$$V(q;\,B) = q^2 - B\,q\ln q, \qquad B(p) = \frac{p+1}{3}.$$
A prime $p$ is **prime-stable** iff $V(p;\,B(p)) < V(q;\,B(p))$ for all primes
$q \neq p$.  The complete stable set is
$$\mathcal{S} = \{2,\;127,\;137,\;139,\;151,\;157\}.$$

This section defines a 2D analogue by replacing integer primes with Gaussian primes,
with the 2D potential driven by the **norm** of the Gaussian prime.

---

## 2. Gaussian Primes and Norms

The Gaussian integers are $\mathbb{Z}[i] = \{a + bi \mid a, b \in \mathbb{Z}\}$.
The **norm** is $N(z) = a^2 + b^2$ for $z = a + bi$.

A Gaussian integer $z$ is a **Gaussian prime** iff one of:

| Case | Condition | Type | Example |
|------|-----------|------|---------|
| $a = 0$ or $b = 0$ | $|{\rm nonzero\ part}|$ is a rational prime $\equiv 3 \pmod{4}$ | inert | $3i$ |
| $a \neq 0$, $b \neq 0$ | $N(z) = a^2 + b^2$ is a rational prime | split | $4 + 11i$ ($N = 137$) |
| $z = 1+i$ (and associates) | $N(z) = 2$ | ramified | $1+i$ |

The **set of Gaussian prime norms** is:
$$\mathcal{N} = \{2\} \cup \{p : p \equiv 1 \pmod 4,\ p\ {\rm prime}\}
  \cup \{p^2 : p \equiv 3 \pmod 4,\ p\ {\rm prime}\}.$$

### 2.1 Degeneracy: $r_2(n)$

The number of representations $n = a^2 + b^2$ (signed, ordered) is $r_2(n)$.
For a prime $p$:

| $p$ | $p \bmod 4$ | $r_2(p)$ | Gaussian type |
|----:|------------:|----------:|---------------|
|   2 |     2       |     4     | ramified       |
| $\equiv 1 \pmod 4$ | 1 | 8 | split |
| $\equiv 3 \pmod 4$ | 3 | 0 | inert |

The 8-fold degeneracy for split primes reflects the symmetry group of $\mathbb{Z}[i]$
(4 associates × 2 conjugate representations).

**Gaussian prime classification of the 1D canonical stable primes:**

| $p$ | $p \bmod 4$ | Type | $r_2(p)$ | Representation |
|----:|:-----------:|------|:--------:|---------------|
|   2 |     2       | ramified | 4  | $1^2 + 1^2$ |
| 127 |     3       | inert    | 0  | — |
| 137 |     1       | split    | 8  | $4^2 + 11^2$ |
| 139 |     3       | inert    | 0  | — |
| 151 |     3       | inert    | 0  | — |
| 157 |     1       | split    | 8  | $6^2 + 11^2$ |

The stable set $\mathcal{S}$ contains both split primes (137, 157) and inert primes
(127, 139, 151), so Gaussian type alone does not predict membership in $\mathcal{S}$.

---

## 3. 2D Potential

The natural 2D generalisation replaces the 1D prime $q$ with a Gaussian prime $z$
and the entropy $q\ln q$ with a function of the norm $N(z)$:

$$V_G(z;\,B) = A\,N(z)^2 - B\,N(z)\ln N(z) + C.$$

Equivalently, letting $n = N(z)$:
$$V_G(n;\,B) = A\,n^2 - B\,n\ln n + C.$$

With $A = 1$, $C = 0$, and $B = B(p) = (p+1)/3$, this reduces exactly to the
canonical 1D potential evaluated at the norm $n$.

**Key rule**: The 2D model treats stability as a property of **norms**, not of
individual Gaussian integers.  The associates $z, iz, -z, -iz$ (and conjugates
for split primes) all have the same norm and hence the same $V_G$.

### 3.1 Continuous 2D Potential

For the continuous model on $\mathbb{R}^2$, with $r^2 = x^2 + y^2$:
$$V_G(x,y;\,B) = A\,(x^2 + y^2)^2 - B\,(x^2+y^2)\ln(x^2+y^2) + C,$$
which is radially symmetric.  The continuous minimum over radius satisfies the same
stationarity condition as the 1D model with $q \mapsto r^2$.

---

## 4. Entropy Extension with Degeneracy Weight

A more refined entropy accounts for the degeneracy $r_2(n)$ of the norm:

$$S_G(n;\,\lambda) \;:=\; n\ln n \;+\; \lambda\,\ln r_2(n),
  \qquad V_G(n;\,B,\lambda) = n^2 - B\,S_G(n;\,\lambda).$$

**Constraint**: $\lambda$ must **not** be tuned to force specific primes into the
stable set.  The $\lambda = 0$ baseline must be tested first.

### 4.1 $\lambda = 0$ Baseline

At $\lambda = 0$, $S_G(n; 0) = n\ln n = $ canonical entropy.  The 2D model
reduces identically to the 1D model on norms, giving stable norms
$= \{2, 127, 137, 139, 151, 157\}$.

This is the required baseline: **the 2D model must reproduce the 1D result at $\lambda = 0$**.

### 4.2 Effect of $\lambda \neq 0$

For split primes ($r_2(p) = 8$, $\ln r_2 = \ln 8 \approx 2.079$), the entropy
$S_G$ is shifted relative to inert primes ($r_2(p) = 0$, but we use $\ln r_2 \to 0$
by convention for inert primes).  Thus $\lambda > 0$ increases the entropy of split
primes, potentially stabilising them further.

| $p \in \mathcal{S}$ | $p\ln p$ | $r_2(p)$ | $\ln r_2$ | $S_G(\lambda=1)$ |
|--------------------:|:--------:|:--------:|:---------:|:----------------:|
| 127 | 615.21 |   0 |  0.000 | 615.21 |
| 137 | 674.04 |   8 |  2.079 | 676.12 |
| 139 | 685.89 |   0 |  0.000 | 685.89 |
| 151 | 757.61 |   0 |  0.000 | 757.61 |
| 157 | 793.83 |   8 |  2.079 | 795.91 |

The $\lambda$-correction is at most $\approx 2.1$ out of entropy values $\sim 700$,
so its effect on stability margins is $\sim B \times 2.1 \approx 46 \times 2.1 \approx
97$ in $V$-units — comparable to stability margins listed in the canonical table.
Any use of $\lambda \neq 0$ must therefore be accompanied by a full prime scan.

---

## 5. Inert Primes and Dimensional Consistency

> **Problem**: The norm-only 2D model is incomplete for inert primes. Inert primes
> cannot be represented as $a^2 + b^2$, so they are not Gaussian prime norms.
> The norm-only model loses them entirely.

Of the six canonical stable primes, three are **inert** ($p \equiv 3 \pmod 4$):

| $p$ | $p \bmod 4$ | Gaussian type | $r_2(p)$ |
|----:|:-----------:|:-------------:|:--------:|
| 127 | 3 | inert | 0 |
| 139 | 3 | inert | 0 |
| 151 | 3 | inert | 0 |

An inert prime $p \equiv 3 \pmod 4$ is **not representable** as $a^2 + b^2$ in $\mathbb{Z}$,
so it is not itself a Gaussian prime norm.  A strict norm-only Gaussian stability model
applied to $\{a^2 + b^2 : (a,b) \in \mathbb{Z}^2\}$ would therefore **exclude** 127, 139,
and 151 — leaving only $\{2, 137, 157\}$ of the canonical set.

This is the fundamental consistency problem of the 2D extension.

### 5.1 Proposed Resolution: Split/Inert Classification

Define two classes of canonical stable primes:

| Class | Description | Members of $\mathcal{S}$ | Mechanism |
|-------|-------------|:------------------------:|-----------|
| **Bulk modes** | Split primes ($p \equiv 1 \pmod 4$); expressible as $a^2+b^2$ | 137, 157 | Gaussian norm stability |
| **Boundary modes** | Inert primes ($p \equiv 3 \pmod 4$); not norms of Gaussian primes | 127, 139, 151 | 1D rational prime stability |
| Ramified | $p=2$ | 2 | Both: $N(1+i)=2$ |

This mirrors the split/inert/ramified decomposition of rational primes in $\mathbb{Z}[i]$.

### 5.2 Extended Potential V\_total (Canonical Fix)

To accommodate both classes, define the **total potential**:

$$V_{\text{total}}(p) \;:=\;
\begin{cases}
  V_G(p;\,B(p)) & \text{if } p \equiv 1 \pmod 4 \text{ (split — Gaussian norm model)}, \\
  V_{1D}(p;\,B(p)) & \text{if } p \equiv 3 \pmod 4 \text{ (inert — 1D rational prime model)},
\end{cases}$$

where $V_G(n;B) = n^2 - B\,n\ln n$ (the 2D norm potential) and
$V_{1D}(p;B) = p^2 - B\,p\ln p$ (the canonical 1D potential).

> **Rationale**: Inert primes ($p \equiv 3 \pmod 4$) are not representable as
> $a^2 + b^2$ and hence cannot be Gaussian prime norms.  Applying a strict
> norm-only Gaussian model to all primes would silently exclude 127, 139, and
> 151 from the canonical stable set $\mathcal{S}$.  The $V_{\text{total}}$
> definition resolves this by routing inert primes through the 1D model.

For $p = 2$ (ramified), both branches agree: $V_G(2;B) = V_{1D}(2;B)$.

**Key property**: Since $V_G(n;B) = V_{1D}(n;B)$ at $n = p$ (both evaluate the same
function at the same integer), $V_{\text{total}}$ reduces to the canonical 1D model for
all six primes in $\mathcal{S}$ at $\lambda = 0$.  The distinction becomes relevant only
when degeneracy weights ($\lambda \neq 0$) or Gaussian neighbours are considered.

### 5.3 Stability Definition with V\_total

A rational prime $p$ is **$V_{\text{total}}$-stable** iff:
$$V_{\text{total}}(p) \;<\; V_G(n;\,B(p)) \;\text{ for all Gaussian prime norms } n \neq p$$
$$\text{and} \quad V_{\text{total}}(p) \;<\; V_{1D}(q;\,B(p)) \;\text{ for all rational primes } q \neq p.$$

At $\lambda = 0$ this recovers the canonical 1D stable set exactly.

### 5.4 Open Questions

| Question | Status |
|----------|--------|
| Does $V_{\text{total}}$ have a natural algebraic derivation from $\mathbb{Z}[i]$ structure? | **[Open]** |
| Do inert boundary modes have a distinct physical interpretation in UBT? | **[Speculative]** |
| Is the split/inert classification preserved under Hecke operators? | **[Open]** |

---

## 6. Stability Definition for Gaussian Primes (revised)

**Definition (norm-stability)**: A rational prime $p$ (that is a Gaussian prime norm)
is *norm-stable* under $V_G(\cdot;\,B, \lambda)$ iff
$$V_G(p;\,B(p),\lambda) < V_G(n;\,B(p),\lambda)$$
for all Gaussian prime norms $n \neq p$.

At $\lambda = 0$ this coincides exactly with prime-stability in the 1D model.

**Note on inert primes**: Inert primes ($p \equiv 3 \pmod 4$) are not Gaussian prime
norms; the 2D extension requires $V_{\text{total}}$ (§5.2) to accommodate them.
See §5 for the resolution via split/inert classification.

---

## 7. Outputs and Next Steps

### 7.1 Required outputs from this track

- [x] $\lambda = 0$ baseline verified: norm-stable set matches 1D canonical set
- [x] Inert-prime consistency issue identified and proposed resolution (§5)
- [x] $\lambda$ scan: $\lambda \in [-1,1]$ in steps of 0.1 (see `reports/gaussian_lambda_scan.md`)
- [ ] Lattice visualisation: plot Gaussian primes $a + bi$ with $N(z) \in [100, 200]$, highlight those with norms in $\mathcal{S}$
- [ ] Comparison table: 1D stable primes vs split/inert classification

### 7.2 Open questions (not claims)

| Question | Status |
|----------|--------|
| Does including $r_2$ degeneracy stabilise additional primes? | **[Open]** — requires $\lambda$-scan |
| Do inert stable primes (127, 139, 151) survive in a strict Gaussian norm model? | **[Open]** — modelling choice |
| Is there a natural modular interpretation of the split/inert distinction for $\mathcal{S}$? | **[Open]** |
| Does the 2D potential have a deeper connection to UBT gauge structure? | **[Speculative]** |


---

## 8. Computation Sketch

```python
import math

def sieve(n):
    is_p = [True]*(n+1); is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_p[i]:
            for j in range(i*i, n+1, i): is_p[j] = False
    return [i for i in range(2, n+1) if is_p[i]]

def r2(n):
    """Number of representations n = a^2 + b^2, signed ordered."""
    count = 0
    for a in range(-int(n**0.5)-1, int(n**0.5)+2):
        b2 = n - a*a
        if b2 < 0: continue
        b = round(b2**0.5)
        if b*b == b2:
            count += 1
            if b > 0: count += 1
    return count

def S_G(n, lam=0.0):
    if n <= 1: return 0.0
    rr = r2(n)
    entropy = n * math.log(n)
    if lam != 0 and rr > 0:
        entropy += lam * math.log(rr)
    return entropy

def V_G(n, B, lam=0.0):
    return n**2 - B * S_G(n, lam)

def B_of(p): return (p + 1) / 3.0

primes = sieve(100_000)

def is_norm_stable(p, primes_list, lam=0.0):
    B = B_of(p)
    Vp = V_G(p, B, lam)
    return all(V_G(q, B, lam) > Vp for q in primes_list if q != p)

# Baseline: lambda=0 must reproduce canonical stable set
stable_G0 = [p for p in primes if p <= 10_000 and is_norm_stable(p, primes, lam=0.0)]
# Expected: [2, 127, 137, 139, 151, 157]
print("lambda=0:", stable_G0)

# Lambda scan (exploratory, not tuning to force results)
for lam in [-1.0, -0.5, 0.0, 0.5, 1.0]:
    stable = [p for p in primes if p <= 10_000 and is_norm_stable(p, primes, lam=lam)]
    print(f"lambda={lam:+.1f}: {stable}")
```

---

## 9. Warnings

- Stability applies to **norms**, not individual Gaussian integers.  Associates
  ($\pm z$, $\pm iz$) and conjugates of split primes all share the same norm and
  hence the same stability.
- The degeneracy term $\lambda \ln r_2(n)$ must **not** be tuned to force any
  particular prime into the stable set.  The $\lambda = 0$ baseline must always
  be reported first.
- Inert primes ($p \equiv 3 \pmod 4$) appear in the 1D canonical stable set
  (127, 139, 151) but have $r_2(p) = 0$; the 2D extension must handle this
  boundary case explicitly.
- No claims about the Riemann Hypothesis, fine structure constant, or other
  deep results should be inferred from this model without full analytic derivation.
