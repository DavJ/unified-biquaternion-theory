# Fermionic Fock SU(3) Decomposition on Three Qubits

**Date:** 2026-07-25  
**Status:** Kinematic representation theorem; physical UBT selection open

## Result

Interpret the three qubits as occupations of three fermionic modes. With
Jordan–Wigner annihilation operators `c_i`, define

```text
T_a = sum_{i,j=1}^3 c_i† (lambda_a/2)_{ij} c_j.
```

The operators satisfy

```text
[T_a,T_b] = i f_{abc} T_c
```

on the full eight-dimensional Hilbert space. Fixed-occupation sectors are
invariant and give

```text
H_8 = Lambda^0 C^3 ⊕ Lambda^1 C^3 ⊕ Lambda^2 C^3 ⊕ Lambda^3 C^3
    ≅ 1 ⊕ 3 ⊕ 3bar ⊕ 1.
```

In computational-basis notation:

```text
N=0:  span{|000>}                         ≅ 1
N=1:  span{|100>,|010>,|001>}             ≅ 3
N=2:  span{|011>,-|101>,|110>}            ≅ 3bar
N=3:  span{|111>}                         ≅ 1
```

The sign in the oriented `N=2` basis is the exterior-algebra orientation needed
for the standard antifundamental matrices.

## Relation to the one-hot lift

The existing one-hot construction

```text
L_a = P lambda_a P†
```

acts as the fundamental representation on `N=1` and as zero on its
five-dimensional complement:

```text
3 ⊕ 1 ⊕ 1 ⊕ 1 ⊕ 1 ⊕ 1.
```

The Fock generators agree with `L_a/2` on `N=1`, but act nontrivially on `N=2`.
Therefore these are two distinct eight-dimensional extensions of the same
fundamental triplet action.

## Coding statement

The one-hot sector detects individual computational-basis bit flips:

```text
P_W X_i P_W = 0.
```

The union `W ⊕ anti-W` does not have this property because a single `X_i` may
map a weight-1 state to an allowed weight-2 state. Phase errors `Z_i` stay inside
`W` and are not detected by the occupation-sector measurement. Consequently,
`W` is an `X`-flip leakage-detecting subspace, not a general stabilizer QEC code.

## Physical interpretation limits

The theorem proves representation content, not particle assignments.

- The six non-singlet basis states form `3 ⊕ 3bar`; they are **not** the six quark
  flavors `u,d,s,c,b,t`.
- Each quark flavor would carry its own color triplet `q_f^a`; flavor requires an
  additional spectral/dynamical label.
- `Lambda^2 3 ≅ 3bar` may be read as an antisymmetric two-mode carrier. It has
  the same color representation as an antiquark but is not automatically a
  physical antiquark; charge conjugation and all other quantum numbers must be
  specified.
- State counting (`3` versus `5`, or `6` versus `2`) does not determine dark
  matter or dark energy densities. Such ratios require a Hamiltonian/action and
  sector weights.

## Reproducibility

Run:

```bash
python tools/verify_three_qubit_su3.py
pytest research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/tests -q
```

The verifier checks canonical anticommutation relations, the full `su(3)`
algebra, the `3` and `3bar` restrictions, singlet sectors, number conservation,
and occupation-sector invariance.
