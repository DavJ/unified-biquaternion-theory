# © 2026 Ing. David Jaroš — MIT License
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
Numerické ověření Besselovy trasy pro Gap G137-B.

Počítá B_Bessel z heat kernelu T³ přes K_{3/2} a porovnává s B_phenom.

Theoretical basis:
    The scalar heat kernel on T^3 with equal radii R after Poisson resummation
    gives a Mellin representation involving K_{3/2}(x) = sqrt(pi/(2x)) * e^{-x} * (1 + 1/x).
    The functional determinant coefficient B_Bessel is extracted as:
        B_Bessel = (N_eff / (4*pi)^{3/2}) * sum_{n>=1} d_3(n) * K_{3/2}(2*pi*n*m_psi)
    where d_3(n) is the number of representations of n as a sum of three integer
    squares, and m_psi = 1/(2*R_psi) is the NS-sector mass gap (m_psi = 1/2 at
    self-dual point R_psi = 1).

    Reference: G. N. Watson, A Treatise on the Theory of Bessel Functions (1944),
    Chapter 6.22; E. Elizalde, Ten Physical Applications of Spectral Zeta Functions
    (1994), Chapter 3.

Result: B_Bessel << B_phenom — Route 7 NO-GO.
"""

import math
import sys


B_PHENOM = 46.2979   # target value — n*(B) = 137 conditional result


def eta_i():
    """Dedekind eta function at tau = i: eta(i) = q^{1/12} prod_{k>=1}(1-q^{2k}), q=e^{-pi}.

    Reference: NIST DLMF 20.9.3 and 23.6.2.
    """
    q = math.exp(-math.pi)
    prod = 1.0
    for k in range(1, 500):
        factor = 1.0 - q ** (2 * k)
        prod *= factor
    return q ** (1.0 / 12.0) * prod


def compute_B_ram():
    """B_Ram = 12^{3/2} * (2*eta(i))^{1/4} — algebraic identity [L0], [OBS] match to B_phenom."""
    return 12.0 ** 1.5 * (2.0 * eta_i()) ** 0.25


def d3(n):
    """Number of representations of n as a sum of three integer squares.

    Counts (a, b, c) in Z^3 with a^2 + b^2 + c^2 = n.
    """
    count = 0
    sq = int(math.isqrt(n)) + 1
    for a in range(-sq, sq + 1):
        a2 = a * a
        if a2 > n:
            continue
        for b in range(-sq, sq + 1):
            b2 = b * b
            if a2 + b2 > n:
                continue
            c2 = n - a2 - b2
            c = int(math.isqrt(c2))
            if c * c == c2:
                count += 1
    return count


def K32(x):
    """K_{3/2}(x) = sqrt(pi/(2x)) * exp(-x) * (1 + 1/x).

    Modified Bessel function of the second kind, order 3/2.
    This is an elementary closed-form expression — no special functions needed.
    Reference: NIST DLMF 10.39.2.
    """
    return math.sqrt(math.pi / (2.0 * x)) * math.exp(-x) * (1.0 + 1.0 / x)


def compute_B_bessel(N_eff=12, m_psi=0.5, R=1.0, n_max=200):
    """Compute B_Bessel from the T^3 heat kernel via K_{3/2}.

    Evaluates:
        B_Bessel = (N_eff / (4*pi)^{3/2}) * sum_{n=1}^{n_max} d_3(n) * K_{3/2}(2*pi*n*m_psi*R)

    Parameters
    ----------
    N_eff : int
        Effective degree-of-freedom count (12 from SU(2)-twist sector [L1]).
    m_psi : float
        NS-sector mass gap; m_psi = 1/(2*R_psi), equals 0.5 at self-dual point R_psi=1.
    R : float
        T^3 radius (set to 1 at self-dual point).
    n_max : int
        Truncation of the d_3(n) lattice sum.

    Returns
    -------
    float
        B_Bessel coefficient.
    """
    total = 0.0
    for n in range(1, n_max + 1):
        arg = 2.0 * math.pi * n * m_psi * R
        total += d3(n) * K32(arg)
    prefactor = N_eff / (4.0 * math.pi) ** 1.5
    return prefactor * total


def main():
    B_ram = compute_B_ram()
    B_bessel = compute_B_bessel()
    ratio = B_bessel / B_PHENOM
    deviation_pct = abs(ratio - 1.0) * 100.0

    print(f"B_phenom  = {B_PHENOM:.6f}")
    print(f"B_Ram     = {B_ram:.6f}  (algebraic identity [L0]/[OBS])")
    print(f"B_Bessel  = {B_bessel:.6f}")
    print(f"Poměr B_Bessel/B_phenom = {ratio:.6f}")
    print(f"Poměr B_Bessel/B_Ram    = {B_bessel / B_ram:.6f}")
    print(f"Odchylka  = {deviation_pct:.2f}%")
    print()

    if deviation_pct < 0.1:
        print("VÝSLEDEK: B_Bessel ≈ B_phenom (< 0.1%) — kandidát na uzavření G137-B!")
        return 0
    elif deviation_pct < 1.0:
        print("VÝSLEDEK: B_Bessel blízko B_phenom (< 1%) — prověřit algebraicky")
        return 0
    elif deviation_pct < 5.0:
        print(f"VÝSLEDEK: B_Bessel blízko B_phenom (< 5%, odchylka {deviation_pct:.1f}%) — "
              "zapsat jako Route 7 (částečný výsledek)")
        return 0
    else:
        print(f"VÝSLEDEK: NO-GO — odchylka {deviation_pct:.1f}% — Route 7 NO-GO, trasa uzavřena")
        return 1


if __name__ == "__main__":
    sys.exit(main())
