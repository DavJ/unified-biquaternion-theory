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

# Adelic valuation and rational-revival audit

**Track:** `research_tracks/prime_fock_operator`  
**Status:** classical local-to-global construction established; UBT origin and Hilbert--Pólya step open  
**Proof level:** standard/exact mathematics plus deterministic checks; `LEAN-PENDING`  
**Scope:** research audit; no canonical UBT status change and no RH claim

<a id="apd-purpose"></a>
## 1. Purpose and decision boundary

This note replaces a sequence of small theta-operator extensions by one local-to-global audit. It answers three questions:

1. what the prime-Fock construction represents in genuinely (p)-adic language;
2. whether rational theta revivals canonically split into prime-power blocks;
3. which part of the resulting structure is standard arithmetic and which part is still absent from canonical UBT.

The result is mixed but decisive. The radial multi-prime construction is exact, its logarithmic Hamiltonian is self-adjoint, and rational revival phases factor exactly through Chinese-remainder idempotents. However, the construction still starts from integer denominators or prime-labelled local places. It does not derive those arithmetic inputs from the UBT action and does not produce a Hilbert--Pólya operator.

<a id="apd-prior-audit"></a>
## 2. Audit of the preceding theta--Mellin route

| Stage | Established result | Remaining obstruction |
|---|---|---|
| scalar theta constants | one zeta zero channel in the open critical strip | no independent zero-location constraint |
| multiplicative characters modulo (5) | four Dirichlet channels | no canonical mixing of the principal channel with the primitive block |
| additive residues and elliptic derivatives | canonical even/odd Weil sectors and sector metrics | no constant even--odd intertwiner |
| local Jacobi operators | explicit graded Dirac map | polynomial spectra have the wrong counting law |
| infinite functional calculus | nonlocal symbols can match the smooth counting law | interpolation by individual zeros is circular |
| regulated prime phase | bounded self-adjoint correction for (sigma>1) | prime labels and (log p) were arithmetic inputs |

The appropriate reset is therefore not another function of the Jacobi derivative. It is the restricted product of all finite places together with the real place.

<a id="apd-radial-space"></a>
## 3. Radial valuation space

For every prime (p), let

\[
\mathcal H_p^{\mathrm{rad}}=\ell^2(\mathbb N_0),
\qquad
N_p|m\rangle_p=m|m\rangle_p.
\]

Use the vacuum vector (|0\rangle_p) to form the restricted tensor product

\[
\mathcal H_{\mathrm{rad}}
=\bigotimes_p'\bigl(\mathcal H_p^{\mathrm{rad}},|0\rangle_p\bigr).
\]

Its standard orthonormal basis consists of finite-support occupation vectors (mathbf m=(m_p)_p). Unique factorization defines a bijection

\[
\mathbf m\longleftrightarrow
n(\mathbf m)=\prod_p p^{m_p},
\qquad
|\mathbf m\rangle\longleftrightarrow|n\rangle.
\]

It extends to a unitary map

\[
U:\mathcal H_{\mathrm{rad}}\longrightarrow\ell^2(\mathbb N).
\]

Define the logarithmic Hamiltonian initially on finite-support vectors by

\[
H_{\log}=\sum_p(\log p)N_p.
\]

Then

\[
UH_{\log}U^{-1}|n\rangle=(\log n)|n\rangle.
\]

**Theorem APD-1 (self-adjoint logarithmic Hamiltonian).** The closure of (H_{\log}) is the positive self-adjoint multiplication operator with domain

\[
\mathcal D(H_{\log})
=\left\{c\in\ell^2(\mathbb N):
\sum_{n\ge1}(\log n)^2|c_n|^2<\infty\right\}.
\]

Finite-support vectors form a core because coefficient truncations converge in the graph norm. Thus the former prime-Fock gap F5 is closed at the classical operator level.

<a id="apd-local-trace"></a>
## 4. Local traces and the Euler product

For (Re s>0), the single-place trace is

\[
\operatorname{Tr}_{\mathcal H_p^{\mathrm{rad}}}
\bigl(p^{-sN_p}\bigr)
=\sum_{m\ge0}p^{-ms}
=\frac1{1-p^{-s}}.
\]

For a finite set (P) of primes,

\[
\operatorname{Tr}\exp\left(-s\sum_{p\in P}(\log p)N_p\right)
=\prod_{p\in P}\frac1{1-p^{-s}}.
\]

The full trace converges exactly in the usual half-plane:

\[
\boxed{
\operatorname{Tr}_{\mathcal H_{\mathrm{rad}}}(e^{-sH_{\log}})
=\sum_{n\ge1}n^{-s}
=\prod_p\frac1{1-p^{-s}}
=\zeta(s),
\qquad \Re s>1.
}
\]

**Theorem APD-2 (radial trace identity).** The prime-Fock partition function is unitarily equivalent to the Dirichlet trace of the multiplication operator (log n). It is the Euler product in operator notation, not a new analytic continuation and not a zero-spectrum theorem.

<a id="apd-padic-integral"></a>
## 5. Exact (p)-adic meaning

Normalize multiplicative Haar measure by

\[
\operatorname{vol}_{d^\times x}(\mathbb Z_p^\times)=1.
\]

The radial shell decomposition is

\[
\mathbb Z_p\setminus\{0\}
=\bigsqcup_{m\ge0}p^m\mathbb Z_p^\times.
\]

Since (|x|_p=p^{-m}) on the (m)-th shell, the unramified local Tate integral is

\[
\boxed{
\int_{\mathbb Q_p^\times}
\mathbf1_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
=\sum_{m\ge0}p^{-ms}
=\operatorname{Tr}(p^{-sN_p})
=\frac1{1-p^{-s}}.
}
\]

**Theorem APD-3 (radial Tate equivalence).** The local prime-Fock oscillator is exactly the radial, trivial-character sector of the (p)-adic local zeta integral.

It is not the whole local field. One has

\[
\mathbb Q_p^\times\cong p^{\mathbb Z}\times\mathbb Z_p^\times.
\]

The space (ell^2(\mathbb N_0)) retains only nonnegative valuations selected by (mathbf1_{\mathbb Z_p}). Ramified characters, Gauss sums, and Dirichlet (L)-factors require the unit sector (mathbb Z_p^\times). The earlier channels modulo (5) are therefore naturally reinterpreted as a finite quotient of the unit sector at the place (p=5), not as four independent global fields.

<a id="apd-archimedean"></a>
## 6. Archimedean correction

With the standard normalization

\[
\vartheta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},
\]

the Mellin identity is

\[
\boxed{
\frac12\int_0^\infty
\bigl(\vartheta(t)-1\bigr)t^{s/2}\frac{dt}{t}
=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \Re s>1.
}
\]

The theta Mellin transform already contains both the finite Euler product and the real-place gamma factor. The local adelic factorization is

\[
Z_\infty(s)=\pi^{-s/2}\Gamma(s/2),
\qquad
Z_p(s)=\frac1{1-p^{-s}},
\qquad
\Lambda(s)=Z_\infty(s)\prod_p Z_p(s).
\]

Consequently, an independent heat-trace product of the form (artheta(t)^d\zeta(t)) may define a valid partition function in its convergence region, but it is not the completed zeta function and does not supply its functional equation. Treating it as the adelic completion would double-count the finite zeta factor relative to the theta Mellin identity.

<a id="apd-crt"></a>
## 7. Rational revivals and prime-power blocks

Let

\[
q=\prod_{j=1}^r q_j,
\qquad
q_j=p_j^{k_j},
\qquad
\gcd(q_i,q_j)=1\quad(i\ne j).
\]

Set

\[
Q_j=q/q_j,
\qquad
u_j=Q_j^{-1}\pmod{q_j},
\qquad
e_j=Q_ju_j\pmod q.
\]

The (e_j) are orthogonal idempotents with

\[
e_i e_j=\delta_{ij}e_j\pmod q,
\qquad
\sum_j e_j=1\pmod q.
\]

Every residue has the unique reconstruction

\[
r=\sum_j r_je_j\pmod q,
\qquad
r_j=r\pmod{q_j}.
\]

The quadratic revival phase then factorizes exactly:

\[
e^{2\pi i a r^2/q}
=\prod_j e^{2\pi i a u_j r_j^2/q_j}.
\]

Therefore the quadratic Gauss sum satisfies

\[
\boxed{
g(a,q)=\prod_j g(a u_j,q_j).
}
\]

**Theorem APD-4 (finite local factorization).** Under the CRT unitary permutation, the rational revival operator on (ell^2(\mathbb Z/q\mathbb Z)) is a tensor product of operators on the prime-power spaces (ell^2(\mathbb Z/p_j^{k_j}\mathbb Z)), with the explicit inverse twists (u_j).

This is the finite-level precursor of

\[
\widehat{\mathbb Z}=\prod_p\mathbb Z_p.
\]

It explains why prime powers, rather than an arbitrary modulus such as (5), are the correct local blocks.

<a id="apd-factorization-gate"></a>
## 8. Corrected noncircularity gate

The previous requirement asked for the prime-power blocks of (q) without factoring (q). Taken literally, that requirement is impossible to distinguish from factorization.

**Theorem APD-5 (factorization-output gate).** Any procedure that outputs the maximal prime powers

\[
\{p^{v_p(q)}:p\mid q\}
\]

also outputs the prime factorization of (q): take the unique prime base of every reported prime power and its exponent. Conversely, the prime factorization immediately gives those blocks.

The physically meaningful gate is therefore not an algorithm that hides integer factorization. It is:

1. derive the rational denominators (q), or the equivalent profinite/local state space, from UBT dynamics without using an Euler product;
2. allow standard CRT/Sylow arithmetic to decompose the resulting finite sectors;
3. derive the Hamiltonian and grading on those sectors from the same reduction.

At present, step 1 and the dynamical part of step 3 remain open. APD-4 does not close the UBT prime-origin gap.

<a id="apd-claim-control"></a>
## 9. Claim control and gap ledger

| ID | Statement | Status |
|---|---|---|
| APD-1 | self-adjoint closure and finite-support core of (H_{\log}) | **[STD/PROVED]** |
| APD-2 | prime-Fock trace equals (zeta(s)) for (Re s>1) | **[STD/PROVED]** |
| APD-3 | radial Fock trace equals the unramified local Tate integral | **[STD/PROVED]** |
| APD-4 | rational revival operator and Gauss sum factor over prime powers | **[STD/PROVED]** |
| APD-5 | recovering maximal prime-power blocks is equivalent to factoring the output | **[L1 elementary theorem]** |
| APD-UBT-1 | derive rational/profinite local sectors from the canonical UBT action | **[OPEN]** |
| APD-UBT-2 | derive (log p), unit characters, and any fermionic grading dynamically | **[OPEN]** |
| APD-HP | construct a self-adjoint operator or trace pairing whose spectral side is the nontrivial zero set | **[OPEN]** |

The construction yields zeta as a thermal trace. Analytic continuation zeros are not eigenvalues of the positive operator (H_{\log}). This limitation is already visible in the Bost--Connes partition-function framework and is not removed by attaching a theta heat trace.

<a id="apd-next"></a>
## 10. Next admissible experiment

The next experiment should add the unit sector without inventing another global channel family:

1. realize (mathbb Q_p^\times\cong p^{\mathbb Z}\times\mathbb Z_p^\times) as radial valuation times local units;
2. identify the existing modulo-(5) multiplicative characters with characters of (mathbb Z_5^\times/(1+5\mathbb Z_5));
3. compute the corresponding local Tate integrals and local Fourier/root-number maps;
4. test compatibility of the finite revival blocks as (p^k) grows toward (mathbb Z_p);
5. stop if the result is only the standard Tate factorization with no UBT-derived operator or positive trace pairing.

This preserves the useful mod-(5) calculations while replacing their arbitrary global interpretation by a local one.

<a id="apd-verification"></a>
## 11. Verification

| Claim | Artifact/tool | Result | Scope | Limitation | Lean status |
|---|---|---|---|---|---|
| APD-1 finite-core consequences | `tools/verify_adelic_prime_decomposition.py`, Python (3.12) | pass | graph-norm truncations for a deterministic domain vector | numerical tail check supplements the analytic multiplication-operator proof | `LEAN-PENDING` — Lean is unavailable in the runtime |
| APD-2 and APD-3 | same artifact | pass | valuation reconstruction, local geometric traces, finite tensor traces | finite/numerical checks do not prove analytic continuation | `LEAN-PENDING` |
| APD-4 | same artifact | pass | exact CRT idempotents and residue bijections; numerical phases and Gauss sums for composite moduli | finite test set supplements the analytic CRT proof | `LEAN-PENDING` |
| archimedean Mellin normalization | same artifact | pass at (s=2) with relative tolerance (2\times10^{-8}) | independent quadrature using Jacobi inversion | one numerical checkpoint is not a general Mellin proof | `LEAN-PENDING` |
| APD-5 | same artifact | exact pass for (2\le q<1000) plus analytic proof | reconstruction of prime bases and exponents from maximal prime powers | finite enumeration supplements the elementary implication | `LEAN-PENDING` |

No check derives the local places, the rational denominators, or a spectral zero operator from UBT.

<a id="apd-references"></a>
## 12. Primary references

- J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, in *Algebraic Number Theory*, 1967, pp. 305--347.
- J.-B. Bost and A. Connes, [*Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*](https://doi.org/10.1007/BF01589495), 1995.
- A. Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068), 1998/1999.

