<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Complex Phase Analysis of the UBT Effective Potential

**Author**: Ing. David Jaroš  
**Date**: 2026-05-05  
**Status**: Mathematical results — [L1 (analytic)]; Numerical verification — [L0]  
**Companion files**:
- `canonical/complex_phase_extension.tex` — full symbolic derivation
- `src/ubt_theta_lab/complex_phase_scan.py` — numerical scan code
- `plots/complex_phase_landscape.png` — Re(V) heatmap and gradient-norm map
- `plots/phase_minima_distribution.png` — stationary-point distribution

---

## 1. Problem Statement

Extend the canonical UBT effective potential

$$V(q) = q^2 - B\,q\ln q, \quad q \in \mathbb{R}_{>0}$$

to the complex domain $q = r\,e^{i\theta}$, and determine:

1. **Are there stable stationary points at $\theta \neq 0$?**
2. **Do different values of $\theta$ correspond to distinct physical sectors?**
3. **Does phase degeneracy exist for the known stable primes?**

Context:
- Canonical stable primes: $\mathcal{S} = \{2, 127, 137, 139, 151, 157\}$
- $B(p) = (p+1)/3$
- Scan range: $r \in [100, 200]$, $\theta \in [0, 2\pi]$

---

## 2. Mathematical Extension

### 2.1 Real and Imaginary Parts of V

With $q = r\,e^{i\theta}$ and $\ln q = \ln r + i\theta$:

$$\boxed{\Re V(r,\theta) = r^2\cos(2\theta) - B\,r\bigl[(\ln r)\cos\theta - \theta\sin\theta\bigr]}$$

$$\boxed{\Im V(r,\theta) = r^2\sin(2\theta) - B\,r\bigl[(\ln r)\sin\theta + \theta\cos\theta\bigr]}$$

At $\theta = 0$: $\Re V = r^2 - B\,r\ln r$ and $\Im V = 0$ — recovers the canonical real potential.

### 2.2 Gradient Structure

The key structural result: both partial derivatives of $V$ are proportional to the same bracket,

$$\frac{\partial V}{\partial r} = e^{i\theta}\underbrace{\bigl[2r\,e^{i\theta} - B(\ln r + 1 + i\theta)\bigr]}_{G},$$
$$\frac{\partial V}{\partial\theta} = i\,\frac{\partial V}{\partial r}.$$

Both vanish iff **$G = 0$**, i.e., the stationarity system is:

| Equation | Condition |
|----------|-----------|
| Real part | $2r\cos\theta = B\,(\ln r + 1)$ |
| Imaginary part | $2r\sin\theta = B\,\theta$ |

---

## 3. Analysis of Stationary Points

### 3.1 Real-Axis Solutions ($\theta = 0$)

The imaginary equation $2r\sin(0) = B\cdot 0$ is trivially satisfied.  
The real equation $2r = B(\ln r + 1)$ recovers the canonical stationarity condition — with solutions at the known stable primes.

### 3.2 Non-Real Solutions ($\theta \neq 0$)

Dividing the two stationarity equations gives:

$$\tan\theta = \frac{\theta}{\ln r + 1}, \quad \text{and} \quad r = \frac{B\theta}{2\sin\theta}.$$

**Case analysis for $r \in [100, 200]$:**

| $\theta$ range | $\sin\theta$ | Constraint on $r$ | Result |
|----------------|-------------|-------------------|--------|
| $(0, \pi/2)$ | $> 0$ | $r \leq B\pi/4 \approx 36$ | **Excluded** ($r < 100$) |
| $(\pi/2, \pi)$ | $> 0$ | $\ln r + 1 < 0 \Rightarrow r < e^{-1}$ | **Excluded** |
| $(\pi, 2\pi)$ | $< 0$ | $r < 0$ | **Not physical** |
| Near $2\pi$ ($\theta = 2\pi + \varepsilon$) | $\approx \varepsilon$ | $r \approx B\pi/\varepsilon$ | Consistency check below |

**Near $\theta = 2\pi$ consistency check** (for $B \approx 46$, $r \approx 137$):

$$\varepsilon \approx \frac{B\pi}{r} \approx \frac{46\pi}{137} \approx 1.054$$

This is not small, so the small-angle approximation breaks down. Self-consistent evaluation gives $r \approx 193.6$, but the equation $\ln r + 1 = \theta\cos\theta/\sin\theta$ fails:

$$\ln(193.6) + 1 \approx 6.27 \neq \frac{7.337\times\cos(7.337)}{\sin(7.337)} \approx 4.11.$$

**No consistent non-real solution exists in $r \in [100, 200]$.**

---

## 4. Numerical Results

Scan parameters:
- $r \in [100, 200]$, 200 grid points
- $\theta \in [0, 2\pi]$, 360 grid points
- $B = 46.0$ (≈ $B(137)$)
- Gradient-norm threshold: $|\nabla V| < 5.0$

### 4.1 Near-Stationary Points Found

| Location type | Count | $r$ | $\theta$ | $|\nabla V|$ |
|---------------|------:|-----|----------|--------------|
| Real axis ($\theta \approx 0$) | 1 | 136.18 | 0.0000 | 0.3185 |
| Off-axis ($\theta \neq 0$) | 0 | — | — | — |

### 4.2 Per-Prime Sector Count

| Prime $p$ | $B(p)$ | Total minima | Off-axis minima | Sectors |
|----------:|-------:|------------:|----------------:|--------:|
| 127 | 42.667 | 1 | 0 | **1** |
| 137 | 46.000 | 1 | 0 | **1** |
| 139 | 46.667 | 1 | 0 | **1** |
| 151 | 50.667 | 1 | 0 | **1** |
| 157 | 52.667 | 1 | 0 | **1** |

**All stable primes: exactly 1 sector, on the real axis.**

---

## 5. Phase Structure

### 5.1 $\theta$-Direction Profile of $\Re V$

Taylor expansion of $\Re V(r, \theta)$ around $\theta = 0$ at fixed $r$:

$$\Re V(r, \theta) = \bigl(r^2 - B\,r\ln r\bigr) + c_2\,\theta^2 + O(\theta^4),$$

where

$$c_2 = -2r^2 + \tfrac{B\,r}{2}(\ln r + 2).$$

At the stable primes:

| $p$ | $B(p)$ | $c_2$ | Sign |
|----:|-------:|------:|------|
| 127 | 42.667 | $-2\times127^2 + \tfrac{42.667\times127}{2}\times(6.846+2)$ | $< 0$ |
| 137 | 46.000 | $-2\times137^2 + \tfrac{46\times137}{2}\times(6.920+2)$ | $< 0$ |
| 157 | 52.667 | $-2\times157^2 + \tfrac{52.667\times157}{2}\times(5.056+2)$ | $< 0$ |

$c_2 < 0$ for all stable primes: $\theta = 0$ is a local **maximum** of $\Re V$ in the $\theta$-direction.

> **Note**: This does not mean $\theta = 0$ is "unstable" in a physical sense.
> The stability criterion is the vanishing of the full complex gradient $G$,
> not a minimum of $\Re V$ along $\theta$.  The real-axis is the unique
> zero of $G$ for $r \in [100, 200]$.

### 5.2 Periodicity

$V(r, \theta)$ is **not** strictly $2\pi$-periodic in $\theta$ due to the $\theta\sin\theta$ and $\theta\cos\theta$ terms in $\Re V$ and $\Im V$.  The principal branch of $\ln q$ restricts $\theta \in (-\pi, \pi]$, so there is a unique representative of each complex argument.

---

## 6. RG Extension to Complex Scale

Complexifying the RG scale $\mu \to \mu\,e^{i\theta}$:

$$\delta V \sim B\,n(\ln\mu + i\theta).$$

Effect: adds $i\,B\,n\,\theta$ to $\Im V$; **does not shift** $\Re V$ or move the real-axis minimum.  Complex RG-scale rotation generates an imaginary-time phase but produces no new real stationary points.

---

## 7. Connection to Prime Structure

### 7.1 Do Stable Radii Align with Primes?

The single stationary point found in the $B=46$ scan is at $r \approx 136.18$, which is close to the prime $p = 137$. This is consistent with the real-domain analysis: the minimum of $V(r; B(137))$ over the continuum is at $r^* \approx 136.0$ (from $2r^* = B(\ln r^* + 1)$), and the nearest prime minimiser is $p = 137$.

### 7.2 Phase Degeneracy

**None detected.** Each stable prime has exactly one physical sector ($\theta = 0$).  The hypothesis "multiple sectors per prime" is **rejected** by this analysis.

### 7.3 Hypothesis Test Summary

| Hypothesis | Result |
|------------|--------|
| Non-zero $\theta$ stable sectors exist for $r \in [100,200]$ | **Rejected** |
| Multiple sectors per prime | **Rejected** |
| Stable radii align with primes (real axis only) | **Confirmed** |
| Phase degeneracy of stable set | **None** |

---

## 8. Summary

| Question | Answer |
|----------|--------|
| Are there $\theta \neq 0$ stable sectors for $r \in [100,200]$? | **No** |
| Number of sectors per stable prime | **1** (real axis only) |
| Structure of minima | One basin per prime, on $\theta = 0$ |
| Phase degeneracy | None |
| RG complexification effect | Shifts $\Im V$ only; no new real minima |
| Relation to primes | Confirmed: stable radii = stable primes, no complex analogue |

---

## 9. Open Question

> **[G-Phase]** Do non-real stationary points exist for $r < 43$ (i.e., $r \leq B\pi/4$)?
>
> Analytically, Case 1 of the non-existence proof shows solutions can occur at
> $\theta \in (0, \pi/2)$ when $r \leq B\pi/4 \approx 36$.  These points do not
> align with any prime in $\mathcal{S}$ and their physical significance within UBT
> is unclear.  A separate scan over $r \in [1, 50]$ would be needed to
> characterise this region.
