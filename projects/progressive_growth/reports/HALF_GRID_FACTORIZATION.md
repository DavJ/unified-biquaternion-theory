<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Half-Grid Theta-Sector Factorization
## Milestone M2H — Exact half-grid theta-sector factorization

**Author**: Ing. David Jaroš  
**Status**: Algebraic/architectural milestone — training-performance claims are out of scope.

---

## 1. Why `V U^T W U = V` is a trivial identity

For any orthogonal matrix `U` and `W = I`, the expression

```
V U^T W U = V U^T I U = V (U^T U) = V I = V
```

inserts only a pair of inverse orthogonal transformations.  The intermediate
space is exactly the same as the input space, rotated and then un-rotated.
No new geometry is introduced; the half-grid position carries no independent
theta-sector frame.

The intended architecture is different: the intermediate frame `Phi` is
selected from a **theta segment** — a slice of the UBT canonical phi kernel —
and is generally **non-orthogonal** and **not automatically invertible**.
The factorization is exact only when the frame column rank is sufficient.

---

## 2. SVD/frame factorization

For an original weight matrix `V` of shape `[output_dim, input_dim]`:

1. Compute the compact SVD: `V = P @ diag(s) @ Qh`
2. Determine the numerical rank `r`.
3. Trim to the rank-`r` components: `P_r`, `s_r`, `Qh_r`.
4. Let `Phi` be the half-grid theta-sector frame of shape
   `[sector_width, r_or_more]` (must have column rank >= r).
5. Define:

```
sqrt_Sigma = diag(sqrt(s_r))

A = Phi[:, :r] @ sqrt_Sigma @ Qh_r     # shape [sector_width, input_dim]
B = P_r @ sqrt_Sigma @ pinv(Phi[:, :r])# shape [output_dim, sector_width]
```

**Invariant**: `B @ A == V` within documented numerical tolerance.

This is the half-grid theta-sector factorization at position `k + 1/2`.

---

## 3. Pseudoinverse rank condition

Exact reconstruction requires:

```
column_rank(Phi) >= numerical_rank(V)
```

If `Phi` does not satisfy this, the factorization raises `ValueError` and
reports `SECTOR_INSUFFICIENT_FOR_EXACT_TRANSFER`.

The pseudoinverse residual is defined as:

```
max_abs(pinv(Phi) @ Phi - I)
```

For an orthonormal frame this is machine epsilon.  For a non-orthogonal
phi-segment frame it may be significantly larger, proportional to the frame
condition number.  Reconstruction error scales accordingly.

---

## 4. Exact paired-ReLU identity

For real-valued matrices, the identity

```
relu(z) - relu(-z) = z    for all real z
```

gives an exact ReLU insertion.  Define:

```
A_pm = cat([A, -A], dim=0)    # shape [2*sector_width, input_dim]
B_pm = cat([B, -B], dim=1)    # shape [output_dim, 2*sector_width]
```

Then for any real input batch `x`:

```
B_pm @ relu(A_pm @ x) = B @ (relu(A@x) - relu(-A@x))
                       = B @ (A @ x)
                       = V @ x
```

This is exact (up to floating-point arithmetic), not an approximation.
The outer activation (if any) is preserved unchanged outside the module.

The ReLU factorization is defined only for real inputs.  Complex ReLU is
not a standard function and is **not implemented**; complex weight matrices
use the purely linear factorization.

---

## 5. Theta segments at `k + 1/2`

The integer layers of a network sit at positions `k = 0, 1, 2, ...`.
The half-grid theta-sector frames are inserted at positions `k + 1/2`:

```
[original layer 0] ---(theta segment at 1/2)--- [original layer 1]
[original layer 1] ---(theta segment at 3/2)--- [original layer 2]
...
```

A `HalfGridSectorSchedule(segment_ids=("phi_A", "phi_B", ...))` names
the segment at each half-integer position.  Different positions may carry
different frames; this is the central design of half-grid theta-sector
interleaving.

The neuron-duplication baseline (widening by repeating neurons) occupies
no specific theta-sector geometry.  It remains the reference for
parameter-matched comparisons but is not the intended architecture.

---

## 6. Canonical phi-segment frame results

All tests use small lattice sizes for speed.  Key findings:

| Segment | phis | Lattice | Rank | Cond number | Gram eigs | Notes |
|---------|------|---------|------|-------------|-----------|-------|
| phi_low | 0.1, 0.2, 0.3 | 3 | 3 | moderate | all positive | well-conditioned |
| phi_mid | 0.5, 1.0, 1.5 | 3 | 3 | moderate | all positive | well-conditioned |
| phi_high | 2.0, 3.0, 4.0 | 3 | 3 | moderate | all positive | well-conditioned |
| phi_vhigh | 100, 200, 300 | 3 | <3 | ≫1 | near-degenerate | SECTOR_INSUFFICIENT_FOR_EXACT_TRANSFER |

High-phi segments cause rapid Gaussian decay; the kernel vectors become
nearly identical (all weight concentrated at `r2=0`) and the frame loses
rank.  This is reported honestly, not patched.

Different phi segments (e.g., low vs. high) span measurably different
subspaces.  The principal-angle test confirms `||P_A - P_B||_F > 0` for
well-separated phi ranges.

---

## 7. Unresolved questions

1. **Action-level selection**: Which phi segment should be inserted at
   each half-grid position is not derived from the UBT action.  This is
   `GAP-10T-DYN` territory; it requires a canonical torsion/connection
   dynamics derivation.

2. **Global continuation**: The local factorization is exact on any
   single layer.  Composition across many layers with different frames
   has not been analyzed for error accumulation.

3. **Torsion interpretation**: The non-orthogonality of the phi frame
   corresponds geometrically to a non-flat connection in the half-grid
   space.  Whether this is related to physical torsion in the UBT sense
   is open.

4. **Training dynamics after insertion**: Once parameters are released,
   the factored layers will evolve away from the exact-preservation point.
   The trajectory and stability are outside this milestone.

5. **Complex extension of ReLU path**: The paired `relu(z)-relu(-z)=z`
   identity requires real arithmetic.  A complex extension would need a
   different splitting; this is not pursued here.

---

**Summary**: The half-grid theta-sector factorization is algebraically
verified.  The phrase **half-grid theta-sector interleaving** describes
the architecture.  This is not claimed to be a proven Theta Grid speedup.
