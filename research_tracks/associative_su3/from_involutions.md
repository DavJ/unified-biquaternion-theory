<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Track A: SU(3) Candidate via Z2×Z2×Z2 Involutions on ℬ

**Status:** Candidate construction — Track A, conservative framing.  
**Related files:**
- `canonical/algebra/involutions_Z2xZ2xZ2.tex` — formal lemmas
- `tools/involutions_triplet_projectors.py` — computational verification
- `reports/involutions_triplet_report.md` — auto-generated signature table

---

## 1. Setup and Notation

Let **ℬ = ℂ⊗ℍ** be the biquaternion algebra.  We view ℬ as an
8-dimensional **real** vector space with ordered basis

    B = {1, I, J, K,  i, iI, iJ, iK}

where:
- `i` is the imaginary unit of ℂ (complex factor), with i² = −1
- `I, J, K` are the standard quaternion units (quaternion factor), satisfying
  `I² = J² = K² = −1`, `IJ = K`, `JK = I`, `KI = J`
- Elements of the form `i·X` (X ∈ {1, I, J, K}) span the "imaginary" half of ℬ

The complex unit `i` lies in the **centre** of ℬ (it commutes with I, J, K),
so multiplication by `i` is a well-defined ℝ-linear map on ℬ.

---

## 2. Three Commuting Involutions

We define three real-linear maps P1, P2, P3 : ℬ → ℬ by their action on B:

| Basis element | P1 (complex conj.) | P2 (quat. conj.) | P3 (axis-flip ∥ I) |
|---|:---:|:---:|:---:|
| 1  | +1 | +1 | +1 |
| I  | +1 | −1 | +1 |
| J  | +1 | −1 | −1 |
| K  | +1 | −1 | −1 |
| i  | −1 | +1 | +1 |
| iI | −1 | −1 | +1 |
| iJ | −1 | −1 | −1 |
| iK | −1 | −1 | −1 |

**Explicit definitions:**

- **P1** (complex conjugation): `P1(i) = −i`; leaves I, J, K unchanged.  
  Extends by ℝ-linearity: `P1(iX) = −iX` for X ∈ {1, I, J, K}`.

- **P2** (quaternion conjugation): `P2(I) = −I, P2(J) = −J, P2(K) = −K`; leaves i unchanged.  
  Extends by ℝ-linearity: `P2(iX) = i·P2(X)`.

- **P3** (axis-flip around I): `P3(I) = I, P3(J) = −J, P3(K) = −K`; leaves i unchanged.  
  Equivalently, `P3 = conjugation by I` in ℍ extended to ℬ:
  `P3(x) = I x I⁻¹` where `I⁻¹ = −I` in ℍ.

---

## 3. Proofs of Involution and Commutativity

### 3.1 Each Pk is an involution (Pk² = id)

On every basis element b, Pk acts by a scalar eigenvalue sk ∈ {+1, −1}:

    Pk(b) = sk · b  ⟹  Pk²(b) = Pk(sk · b) = sk · Pk(b) = sk · sk · b = b

since sk² = 1 for sk ∈ {±1}.  By ℝ-linearity, Pk² = id on all of ℬ. ∎

### 3.2 Pairwise commutativity

Since each Pk acts by a scalar ±1 on every basis element, for any two
involutions Pi, Pj and any basis element b:

    Pi(Pj(b)) = Pi(sj · b) = sj · Pi(b) = sj · si · b
    Pj(Pi(b)) = Pj(si · b) = si · Pj(b) = si · sj · b

These are equal (scalars commute), so `[Pi, Pj] = 0` on all basis elements,
and by linearity `[Pi, Pj] = 0` on ℬ. ∎

---

## 4. Signatures and Sector Decomposition

The **signature** of a basis element b is the triple

    σ(b) = (s1, s2, s3) ∈ {±1}³,  where Pk(b) = sk · b.

This gives a decomposition of ℬ into simultaneous eigenspaces.  The
**projector** onto sector (s1, s2, s3) is

    Π_(s1 s2 s3) = (1/8) ∏_{k=1}^{3} (1 + sk Pk)

where `1` denotes the identity map.  These projectors satisfy

    Π_(s1 s2 s3)² = Π_(s1 s2 s3),    (idempotent)
    Σ_{(s1,s2,s3)} Π_(s1 s2 s3) = id. (completeness)

The computed sectors and their real dimensions are:

| Sector   | Basis members   | dim_ℝ |
|----------|-----------------|-------|
| (+,+,+)  | {1}             | 1     |
| (+,−,+)  | {I}             | 1     |
| (+,−,−)  | {J, K}          | 2     |
| (−,+,+)  | {i}             | 1     |
| (−,−,+)  | {iI}            | 1     |
| (−,−,−)  | {iJ, iK}        | 2     |
| (+,+,−)  | ∅               | 0     |
| (−,+,−)  | ∅               | 0     |

---

## 5. Single-Minus Sectors

The **single-minus** sectors (exactly one negative eigenvalue) are:

- **S1 = (−,+,+):** `Π_S1 ℬ = span_ℝ{i}`, dim_ℝ = 1
- **S2 = (+,−,+):** `Π_S2 ℬ = span_ℝ{I}`, dim_ℝ = 1
- **S3 = (+,+,−):** `Π_S3 ℬ = {0}`, dim_ℝ = 0  **(empty)**

### Why S3 is empty

Any element with P1 = +1 (no complex-i factor) and P2 = +1 (no
quaternion-unit factor) must be a real scalar multiple of 1.  Since
P3(1) = +1 for any algebra involution fixing the unit, that element lies
in the (+,+,+) sector, not (+,+,−).  The sector S3 = (+,+,−) is therefore
provably empty given the definitions of P1 (complex conjugation) and P2
(quaternion conjugation).

This is noted here explicitly as part of the **conservative, candidate-only
framing**.

---

## 6. Candidate 3D Complex Carrier Space

### 6.1 Definition

The direct sum of the three single-minus sectors gives only a 2D real space
(span{i, I}) and does not yield a 3D complex carrier space.  A more natural
construction uses the **P2 = −1 eigenspace**:

    Vc := Π_{(s2=−1)} ℬ = span_ℂ{I, J, K}
        = {a·I + b·J + c·K  :  a, b, c ∈ ℂ}

where ℂ acts on ℬ by left multiplication by the complex unit i.

**Claim:** Vc is a 3-dimensional complex vector space (dim_ℂ Vc = 3).

**Proof:** The six real vectors {I, iI, J, iJ, K, iK} are linearly independent
over ℝ (they are distinct basis elements of B), and every element of Vc can
be written as a·I + b·J + c·K with a, b, c ∈ ℂ, so dim_ℂ Vc = 3. ∎

### 6.2 Action of P3 on Vc

P3 restricts to a ℂ-linear involution on Vc with eigenspaces:

- **P3 = +1:** `span_ℂ{I}` (1-dimensional over ℂ)
- **P3 = −1:** `span_ℂ{J, K}` (2-dimensional over ℂ)

The S2 = (+,−,+) sector corresponds precisely to the real slice of the
P3=+1 sub-eigenspace of Vc.

### 6.3 Inner product and SU(3) candidate

Define the Hermitian inner product on Vc by

    ⟨X, Y⟩ := (1/4) Tr(X† Y)

where `X†` denotes the biquaternionic conjugate-transpose (complex conjugation
composed with quaternion conjugation), and `Tr` is the reduced trace over ℬ.

On the real basis {I, J, K} (identified with the standard basis of ℂ³ via
the isomorphism Vc ≅ ℂ³), this inner product reduces to the standard
Hermitian inner product on ℂ³.

**Candidate SU(3):**

    SU(3)_Vc := { U ∈ GL(Vc)  |  U is ℂ-linear, ⟨Ux, Uy⟩ = ⟨x,y⟩ ∀x,y ∈ Vc,
                                  det_ℂ(U) = 1 }

This is isomorphic to the standard SU(3) (unitary group of determinant 1 on
ℂ³), and acts naturally on the Θ-triplet sector extracted from ℬ.

---

## 7. Conservative Framing and Caveats

1. **Not Aut(ℬ):** The group SU(3)_Vc constructed here acts on the subspace
   Vc ⊂ ℬ; it is **not** a subgroup of the automorphism group Aut(ℬ).  The
   scan in `reports/associative_su3_scan.md` confirms that
   `Aut(ℂ⊗ℍ) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂` does not contain SU(3).

2. **Candidate only:** No claim is made that this SU(3) is the colour gauge
   group of QCD.  It is a *candidate* symmetry of the Θ-triplet subspace,
   whose physical role requires further investigation.

3. **No octonions:** The entire construction uses only the associative algebra
   ℬ = ℂ⊗ℍ.  No non-associative structures or octonions appear.

4. **S3 empty:** The involutions as defined do not populate the (+,+,−) sector.
   The 3D complex carrier space arises from P2 alone (the quaternion
   conjugation involution), not from the intersection of three single-minus
   sectors.  Future work may investigate whether a modified P3 could fill S3
   while preserving associativity.

---

## 8. Summary

| Item | Result |
|------|--------|
| Basis B | {1, I, J, K, i, iI, iJ, iK} |
| Three commuting involutions | P1 (complex conj.), P2 (quat. conj.), P3 (axis-flip) |
| P1² = P2² = P3² = id | ✓ (proved) |
| Pairwise commutativity | ✓ (proved) |
| S1 = (−,+,+) dim | 1 (spanned by i) |
| S2 = (+,−,+) dim | 1 (spanned by I) |
| S3 = (+,+,−) dim | 0 (empty — noted explicitly) |
| Candidate Vc | span_ℂ{I, J, K}, dim_ℂ = 3 |
| SU(3) candidate | Unitary det=1 transformations on Vc ≅ ℂ³ |
| Octonion-free | ✓ |

---

*See `tools/involutions_triplet_projectors.py` for the computational
verification and `canonical/algebra/involutions_Z2xZ2xZ2.tex` for the
formal LaTeX lemmas.*
