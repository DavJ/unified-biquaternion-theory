# Riemann Zeta Function: Fock-Space / Operator Formulation
## Personal Reference — Hilbert–Pólya Program

<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

---

## 1. Core Idea

The Riemann zeta function can be written as an **operator trace**:

$$
\zeta(s) = \operatorname{Tr}\!\bigl(e^{-sH}\bigr) = \sum_{n=1}^{\infty} e^{-s\log n} = \sum_{n=1}^{\infty} n^{-s}, \quad \operatorname{Re}(s) > 1.
$$

The Hamiltonian $H$ is chosen so that its spectrum is

$$
\operatorname{Spec}(H) = \{\log n : n \in \mathbb{N}_{\geq 1}\}.
$$

**Key translation**: The multiplicative structure of the integers (factorization) becomes
an *additive* structure of energies via the logarithm,

$$
\log(n) = \sum_p v_p(n)\,\log p,
$$

where $v_p(n)$ is the $p$-adic valuation of $n$.  This is the arithmetic that
the Fock-space construction makes explicit.

---

## 2. Fock-Space Construction

### 2.1 Single-mode spaces

For each prime $p$, introduce a single harmonic-oscillator mode with
**fundamental energy** $\log p$.  The Hilbert space for this mode is

$$
\mathcal{H}_p = \ell^2(\mathbb{N}_0),
$$

spanned by occupation-number states $|k\rangle_p$, $k = 0, 1, 2, \ldots$

### 2.2 Full Fock space

The total Hilbert space is the **restricted tensor product** over all primes:

$$
\mathcal{F} = \bigotimes_p \mathcal{H}_p
\;=\; \bigotimes_p \ell^2(\mathbb{N}_0).
$$

An orthonormal basis is labelled by sequences $(k_2, k_3, k_5, k_7, \ldots)$
with all but finitely many $k_p = 0$:

$$
|\mathbf{k}\rangle = |k_2\rangle_2 \otimes |k_3\rangle_3 \otimes |k_5\rangle_5 \otimes \cdots
$$

### 2.3 Correspondence with integers

The bijection

$$
|\mathbf{k}\rangle \;\longleftrightarrow\; n = \prod_p p^{k_p}
$$

identifies each basis state with the unique positive integer having prime
factorization $n = 2^{k_2} 3^{k_3} 5^{k_5}\cdots$  (Fundamental Theorem of
Arithmetic).  The vacuum $|\mathbf{0}\rangle$ corresponds to $n = 1$.

### 2.4 Hamiltonian

Define the number operator for prime $p$ as $N_p = a_p^\dagger a_p$, acting
as $N_p|k\rangle_p = k|k\rangle_p$.  The total Hamiltonian is

$$
\boxed{H = \sum_p \log(p)\; N_p.}
$$

Its eigenvalue on $|\mathbf{k}\rangle$ is

$$
H|\mathbf{k}\rangle = \Bigl(\sum_p k_p \log p\Bigr)|\mathbf{k}\rangle = \log n\;|\mathbf{k}\rangle,
$$

recovering exactly the required spectrum $\{\log n\}$.

---

## 3. Why the Trace Becomes the Euler Product

### 3.1 Trace as sum over basis

$$
\operatorname{Tr}(e^{-sH})
= \sum_{\mathbf{k}} \langle \mathbf{k}|e^{-sH}|\mathbf{k}\rangle
= \sum_{\mathbf{k}} e^{-s\log n(\mathbf{k})}
= \sum_{n=1}^{\infty} n^{-s} = \zeta(s).
$$

### 3.2 Factorization of the trace

Because $H = \sum_p \log(p)\,N_p$ and the modes are independent (tensor
product structure), the exponential factorizes:

$$
e^{-sH} = \bigotimes_p e^{-s\log(p)\,N_p}.
$$

For a single mode the partial trace is a geometric series:

$$
\operatorname{Tr}_p\!\bigl(e^{-s\log(p)\,N_p}\bigr)
= \sum_{k=0}^{\infty} e^{-sk\log p}
= \sum_{k=0}^{\infty} p^{-sk}
= \frac{1}{1 - p^{-s}}.
$$

Taking the product over all primes:

$$
\boxed{
\operatorname{Tr}(e^{-sH})
= \prod_p \frac{1}{1 - p^{-s}}
= \zeta(s).
}
$$

This is nothing but the **Euler product**, derived here from the independence
(commutativity / tensor-product structure) of the prime modes.

---

## 4. Bra–Ket Interpretation

### 4.1 Trace definition

For any operator $A$ on $\mathcal{F}$:

$$
\operatorname{Tr}(A) = \sum_{n=1}^{\infty} \langle n | A | n \rangle,
$$

where $|n\rangle$ denotes the basis state corresponding to integer $n$.

### 4.2 Matrix elements of the heat kernel

The heat kernel $e^{-sH}$ is **diagonal** in the $|n\rangle$ basis:

$$
\langle m | e^{-sH} | n \rangle = e^{-s\log n}\,\delta_{mn} = n^{-s}\,\delta_{mn}.
$$

Hence the trace is:

$$
\operatorname{Tr}(e^{-sH}) = \sum_n \langle n|e^{-sH}|n\rangle = \sum_n n^{-s} = \zeta(s).
$$

### 4.3 Off-diagonal operators and Mellin transforms

For a diagonal operator $f(H)$ with $f(\lambda) = \lambda^{-s}$ we recover
$\zeta(s)$.  More generally, inserting a multiplicative character
$\chi(n)$ gives Dirichlet $L$-functions:

$$
L(s,\chi) = \operatorname{Tr}(\chi \cdot e^{-sH}) = \sum_n \chi(n)\,n^{-s}.
$$

---

## 5. Hilbert–Pólya Program

### 5.1 Statement

The **Hilbert–Pólya conjecture** proposes that there exists a self-adjoint
operator $\mathcal{L}$ on some Hilbert space such that its eigenvalues
$\{\lambda_n\}$ are related to the non-trivial zeros of $\zeta(s)$ by

$$
\zeta\!\left(\tfrac{1}{2} + i\lambda_n\right) = 0.
$$

If such an operator exists, the Riemann Hypothesis (all zeros on the critical
line $\operatorname{Re}(s) = \tfrac{1}{2}$) follows immediately from the
self-adjointness of $\mathcal{L}$ (real spectrum).

### 5.2 Relation to the Fock construction

The Hamiltonian $H$ constructed in Section 2 encodes the integers but is
**not** the conjectured operator $\mathcal{L}$.  It has spectrum
$\{\log n\}$, which is real and purely describes the arithmetic structure.
The zeros of $\zeta$ live at $s = \tfrac{1}{2} + i\gamma$ and are a
**spectral property of $\zeta$ itself**, not of $H$.

The standard route attempts to construct $\mathcal{L}$ as a perturbation or
modification of the number-theoretic Hamiltonian, e.g. via:

- **Berry–Keating**: $\mathcal{L} = xp$ (classical Hamiltonian on $\mathbb{R}^+$,
  semi-classical quantization).
- **Connes**: operator on an adelic space; $H_p$ on $L^2(\mathbb{Q}_p)$ for each
  prime.
- **Montgomery–Odlyzko law**: statistical distribution of zeros mimics
  eigenvalue spacings of a GUE random matrix.

All of these are **conjectures or analogies**, not proofs.

### 5.3 What is established

| Fact | Status |
|------|--------|
| $\zeta(s) = \operatorname{Tr}(e^{-sH})$ with $H = \sum_p \log p\,N_p$ | ✓ Rigorous (for $\operatorname{Re}(s)>1$) |
| Euler product from independent prime modes | ✓ Rigorous |
| Zeros lie on $\operatorname{Re}(s) = \tfrac{1}{2}$ (RH) | ✗ Open problem |
| Self-adjoint $\mathcal{L}$ with zeros as eigenvalues | ✗ Conjectural |

---

## 6. Summary of Key Formulas

$$
\mathcal{F} = \bigotimes_p \ell^2(\mathbb{N}_0), \qquad
H = \sum_p \log p \cdot N_p, \qquad
\operatorname{Spec}(H) = \{\log n : n \geq 1\}.
$$

$$
\zeta(s)
= \operatorname{Tr}_{\mathcal{F}}\!\bigl(e^{-sH}\bigr)
= \sum_{n=1}^\infty n^{-s}
= \prod_p (1-p^{-s})^{-1}, \qquad \operatorname{Re}(s) > 1.
$$

**Analytic continuation** extends $\zeta(s)$ to $\mathbb{C}\setminus\{1\}$;
the operator-trace representation is formal outside the region of absolute
convergence.

---

## References

- **B. Riemann** (1859): "Über die Anzahl der Primzahlen unter einer gegebenen Größe."
- **D. Hilbert / G. Pólya** (independent, ca. 1910–1920): oral conjecture (mathematical folklore; see A. Odlyzko's account in "The 10^{22}-nd zero of the Riemann zeta function", 1992, for historical notes), operator approach to RH.
- **M.V. Berry & J.P. Keating** (1999): "The Riemann zeros and eigenvalue asymptotics." *SIAM Rev.* 41(2), 236–266.
- **A. Connes** (1999): "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function." *Selecta Math.* 5, 29–106.
- **H. Montgomery** (1973): pair correlation of zeros and GUE.  *Proc. Symp. Pure Math.* 24, 181–193.
- **A. Odlyzko** (1987–2001): numerical verification of GUE statistics for zeros.
