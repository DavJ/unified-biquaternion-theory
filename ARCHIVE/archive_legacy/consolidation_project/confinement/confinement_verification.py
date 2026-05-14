#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
confinement_verification.py — Numerical verification of algebraic confinement.

Track: CORE — SU(3) color sector, confinement
Date: 2026-03-07

Verifies the algebraic confinement conjecture from
consolidation_project/confinement/algebraic_confinement.tex:

  For every color-neutral hadron state |ψ⟩:
      ⟨ψ| C₂ |ψ⟩ = 0   (colour Casimir vanishes on singlet)

  where C₂ = Σ_a G_a²,  G_a = T_a^{(total)} acting on the full
  multi-particle colour space with correct quark/antiquark generators.

  For an isolated quark |c⟩ (c ∈ {r,g,b}):
      ⟨c| C₂^{(1)} |c⟩ = 4/3  ≠ 0   (not a colour singlet)

Representation conventions
--------------------------
  Quarks     (q):    T_a = λ_a / 2   (fundamental representation)
  Antiquarks (q̄):   T̄_a = -λ_a* / 2  (conjugate representation)

  Each colour state lives in a 3-dimensional space (r=0, g=1, b=2).
  An N-particle system lives in a 3^N-dimensional tensor product space.

States checked
--------------
  Baryon      |B⟩   particle types: q q q        (3 quarks, 27-dim space)
  Meson       |M⟩   particle types: q q̄           (1 quark + 1 antiquark, 9-dim)
  Tetraquark  |T⟩   particle types: q q̄ q q̄      (2 quarks + 2 antiquarks, 81-dim)
  Pentaquark  |P⟩   particle types: q q q q q̄    (4 quarks + 1 antiquark, 243-dim)
  Free quark  |r⟩   particle types: q              (1 quark, 3-dim)
"""

import numpy as np

# ── Gell-Mann matrices ───────────────────────────────────────────────────────
def gell_mann():
    """Return list of 8 Gell-Mann matrices λ_a."""
    lam = [None] * 8
    lam[0] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    lam[1] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    lam[2] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    lam[3] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    lam[4] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    lam[5] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    lam[6] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    lam[7] = (np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex)
              / np.sqrt(3))
    return lam


# Pre-compute quark and antiquark generators once
_lam   = gell_mann()
T_q    = [l / 2 for l in _lam]          # fundamental rep:  T_a = λ_a / 2
T_qbar = [-np.conj(l) / 2 for l in _lam]  # conjugate rep: -λ_a* / 2
I3     = np.eye(3, dtype=complex)


# ── Casimir operator for mixed quark/antiquark system ───────────────────────
def casimir_operator(particle_types):
    """
    Build the second-order Casimir C₂ = Σ_a G_a² for a system of quarks
    and antiquarks.

    Parameters
    ----------
    particle_types : list of str
        Each element is 'q' (quark, fundamental rep) or
        'qbar' (antiquark, conjugate rep).

    Returns
    -------
    C2 : ndarray, shape (3^N, 3^N)
    """
    n   = len(particle_types)
    dim = 3**n
    C2  = np.zeros((dim, dim), dtype=complex)

    for a in range(8):
        # Build G_a = Σ_k  I⊗…⊗T_a^{(k)}⊗…⊗I
        G_a = np.zeros((dim, dim), dtype=complex)
        for k, ptype in enumerate(particle_types):
            ta  = T_q[a] if ptype == 'q' else T_qbar[a]
            op_k = np.array([[1.0+0j]], dtype=complex)
            for j, pt_j in enumerate(particle_types):
                op_k = np.kron(op_k, ta if j == k else I3)
            G_a += op_k
        C2 += G_a @ G_a

    return C2


# ── colour singlet states ────────────────────────────────────────────────────
def baryon_singlet():
    """
    Fully antisymmetric baryon colour singlet (three quarks).

    |B⟩ = (1/√6) ε_{ijk} |i⟩|j⟩|k⟩
         = (1/√6)(|rgb⟩ - |rbg⟩ + |gbr⟩ - |grb⟩ + |brg⟩ - |bgr⟩)

    State index: c1*9 + c2*3 + c3  (each c ∈ {0=r, 1=g, 2=b}).
    Particle types: q q q  (27-dimensional space).
    """
    psi = np.zeros(27, dtype=complex)
    # Levi-Civita tensor ε_{ijk} for (r=0, g=1, b=2)
    eps = [
        (0, 1, 2, +1),  # rgb
        (0, 2, 1, -1),  # rbg
        (1, 2, 0, +1),  # gbr
        (1, 0, 2, -1),  # grb
        (2, 0, 1, +1),  # brg
        (2, 1, 0, -1),  # bgr
    ]
    for c1, c2, c3, sign in eps:
        psi[c1 * 9 + c2 * 3 + c3] += sign
    psi /= np.linalg.norm(psi)
    return psi  # particle types: q q q


def meson_singlet():
    """
    Meson colour singlet (one quark + one antiquark).

    |M⟩ = (1/√3)(|rr̄⟩ + |gḡ⟩ + |bb̄⟩)
         = (1/√3) Σ_c |c⟩_q ⊗ |c⟩_q̄

    State index: c_q * 3 + c_qbar  (each c ∈ {0=r, 1=g, 2=b}).
    Particle types: q q̄  (9-dimensional space).
    """
    psi = np.zeros(9, dtype=complex)
    for c in range(3):
        psi[c * 3 + c] = 1.0
    psi /= np.linalg.norm(psi)
    return psi  # particle types: q qbar


def tetraquark_singlet():
    """
    Tetraquark colour singlet (two quarks + two antiquarks).

    Constructed as the tensor product of two meson singlets:
    |T⟩ = |M⟩_{q₁q̄₁} ⊗ |M⟩_{q₂q̄₂}

    Particle ordering: q₁ q̄₁ q₂ q̄₂  (81-dimensional space).
    Particle types: q qbar q qbar.
    """
    m   = meson_singlet()       # 9-dim, types: q qbar
    psi = np.kron(m, m)         # 81-dim, types: q qbar q qbar
    psi /= np.linalg.norm(psi)
    return psi  # particle types: q qbar q qbar


def pentaquark_singlet():
    """
    Pentaquark colour singlet (four quarks + one antiquark).

    Constructed as baryon ⊗ meson:
    |P⟩ = |B⟩_{q₁q₂q₃} ⊗ |M⟩_{q₄q̄}

    Particle ordering: q₁ q₂ q₃ q₄ q̄  (243-dimensional space).
    Particle types: q q q q qbar.
    """
    bary = baryon_singlet()       # 27-dim, types: q q q
    mes  = meson_singlet()        #  9-dim, types: q qbar
    psi  = np.kron(bary, mes)    # 243-dim, types: q q q q qbar
    psi /= np.linalg.norm(psi)
    return psi  # particle types: q q q q qbar


# ── helper ───────────────────────────────────────────────────────────────────
def expval(psi, op):
    """Return real part of ⟨ψ|op|ψ⟩ for normalised |ψ⟩."""
    return float(np.real(psi.conj() @ op @ psi))


# ── main verification ────────────────────────────────────────────────────────
def main():
    print("=" * 68)
    print("Algebraic Confinement — Colour-Singlet Numerical Verification")
    print("UBT / Ing. David Jaroš, 2026-03-07")
    print("=" * 68)
    print()
    print("Method: compute ⟨ψ|C₂|ψ⟩ where C₂ = Σ_a G_a²,")
    print("  G_a uses fundamental rep for quarks and conjugate rep for antiquarks.")
    print()
    print("  ⟨C₂⟩ = 0   → colour singlet  → ADMISSIBLE in H_phys")
    print("  ⟨C₂⟩ ≠ 0   → not a singlet   → INADMISSIBLE (confined)")
    print()

    # ── test cases ────────────────────────────────────────────────────────
    test_cases = [
        # (label, state_fn, particle_types, expect_singlet)
        ("Baryon     (qqq)      ",   baryon_singlet,     ['q', 'q', 'q'],              True),
        ("Meson      (qq̄)       ",   meson_singlet,      ['q', 'qbar'],                True),
        ("Tetraquark (qq̄qq̄)    ",   tetraquark_singlet, ['q','qbar','q','qbar'],       True),
        ("Pentaquark (qqqq q̄)  ",   pentaquark_singlet, ['q','q','q','q','qbar'],      True),
        ("Free quark |r⟩        ",   None,               ['q'],                         False),
        ("Free quark |g⟩        ",   None,               ['q'],                         False),
        ("Free quark |b⟩        ",   None,               ['q'],                         False),
    ]

    # States for free quarks (no state function; build directly)
    free_quark_states = [
        np.array([1, 0, 0], dtype=complex),
        np.array([0, 1, 0], dtype=complex),
        np.array([0, 0, 1], dtype=complex),
    ]

    print(f"  {'State':<28}  {'⟨C₂⟩':>10}  {'Singlet?':>9}  {'Admissible?':>13}")
    print("  " + "-" * 68)

    all_pass = True
    fq_idx   = 0

    for label, state_fn, ptypes, expect_singlet in test_cases:
        if state_fn is not None:
            psi = state_fn()
        else:
            psi    = free_quark_states[fq_idx]
            fq_idx += 1

        C2 = casimir_operator(ptypes)
        ev = expval(psi, C2)

        is_singlet  = abs(ev) < 1e-10
        admit_str   = "YES" if is_singlet else "NO  ← confined"
        singlet_str = "YES" if is_singlet else "NO"

        print(f"  {label:<28}  {ev:>10.6f}  {singlet_str:>9}  {admit_str:>13}")

        # Assertion
        if expect_singlet and not is_singlet:
            print(f"    *** FAIL: {label.strip()} should be a colour singlet! ***")
            all_pass = False
        elif not expect_singlet and is_singlet:
            print(f"    *** FAIL: {label.strip()} should NOT be a singlet! ***")
            all_pass = False

    print()
    if all_pass:
        print("✓  All assertions passed.")
        print("   Hadrons: ⟨C₂⟩ = 0 — colour singlets  (admissible in H_phys).")
        print("   Free quarks: ⟨C₂⟩ = 4/3 — not singlets (algebraically confined).")
    else:
        print("✗  One or more assertions FAILED — review output above.")

    print()
    print("Physical interpretation:")
    print("  A free quark has ⟨C₂⟩ = 4/3, the Casimir eigenvalue of the")
    print("  fundamental 3 representation.  It is not a colour singlet")
    print("  and therefore cannot be an element of H_phys = Im(Π_color).")
    print("  All colour-neutral hadrons satisfy ⟨C₂⟩ = 0 exactly.")
    print()
    print("Status: CONJECTURED [L0] — see algebraic_confinement.tex")
    print("=" * 68)

    return 0 if all_pass else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
