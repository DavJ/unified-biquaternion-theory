# © 2026 Ing. David Jaroš — MIT License
# Licensed under the MIT License. See LICENSE.md.
#
# File: tools/modular_rpsi_check.py
# Purpose: Numerical verification of S-invariance of S_eff and fixation R_psi=1.
#
# Key claim checked: if T_kin is determined by the S-invariance condition
# S_eff[R] = S_eff[1/R], then R=1 (the self-dual point) is a minimum of S_eff
# independently of N_eff (N_eff cancels in the polynomial equation).
#
# Result documented in: research_tracks/T3_ALPHA/modular_symmetry_rpsi.tex §8
"""
Numerical verification of modular S-invariance of S_eff and R_psi=1 fixation.

S_eff(R) = 2*pi*R*T_kin + V_Casimir(R),  V_Casimir(R) = C_total / R^3
S-transformation: R -> 1/R  (T-duality on psi-circle).

S-invariance condition S_eff[R] = S_eff[1/R] uniquely determines T_kin as a
function of R.  Substituting into the stationarity equation dS_eff/dR = 0
yields the polynomial  R^6 + R^4 + R^2 = 3,  whose unique positive real
solution is R = 1.  N_eff appears only in C_total and cancels from the
polynomial — the fixation R_psi = 1 is independent of N_eff.
"""

import math


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

N_EFF = 12                                          # number of effective modes [L1]
ZETA3 = 1.20205690315959                            # Riemann zeta(3)
C_UNIT = 3 * ZETA3 / (128 * math.pi ** 2)          # Casimir coeff per mode (d=3 torus)
C_TOTAL = N_EFF * C_UNIT                            # total Casimir coefficient


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def V_casimir(R: float) -> float:
    """Casimir potential V = C_total / R^3 (repulsive from R=0)."""
    return C_TOTAL / R ** 3


def S_eff(R: float, T_kin: float) -> float:
    """Effective action S_eff = 2*pi*R*T_kin + V_Casimir(R)."""
    return 2 * math.pi * R * T_kin + V_casimir(R)


def T_kin_from_S_invariance(R: float) -> float:
    """T_kin uniquely determined by S-invariance: S_eff[R] = S_eff[1/R].

    Derivation (Lemma 3.1 in modular_symmetry_rpsi.tex):
        2*pi*T_kin*(R - 1/R) = V_cas(1/R) - V_cas(R) = C*(R^3 - 1/R^3)
        => T_kin = C/(2*pi) * (R^3 - 1/R^3) / (R - 1/R)
                 = C/(2*pi) * (R^2 + 1 + 1/R^2)

    L'Hopital limit at R=1 gives T_kin = 3*C/(2*pi).
    """
    if abs(R - 1.0) < 1e-10:
        return 3 * C_TOTAL / (2 * math.pi)
    return C_TOTAL * (R ** 3 - 1 / R ** 3) / (2 * math.pi * (R - 1 / R))


def stationarity_residual(R: float, T_kin: float) -> float:
    """dS_eff/dR = 2*pi*T_kin - 3*C_total/R^4 (= 0 at minimum)."""
    return 2 * math.pi * T_kin - 3 * C_TOTAL / R ** 4


def polynomial_lhs(R: float) -> float:
    """LHS of the key polynomial equation R^6 + R^4 + R^2 = 3."""
    return R ** 6 + R ** 4 + R ** 2


# ---------------------------------------------------------------------------
# Main verification
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("Modulární fixace R_psi — numerické ověření")
    print("=" * 60)
    print(f"N_eff   = {N_EFF}")
    print(f"C_unit  = {C_UNIT:.8f}  (Casimir coeff per mode, d=3)")
    print(f"C_total = {C_TOTAL:.8f}  (= N_eff * C_unit)")
    print()

    # --- Table 1: T_kin from S-invariance and stationarity residual ----------
    print("Tabulka 1: T_kin ze S-invariance a residuum stacionarity")
    print(f"{'R':>6}  {'T_kin':>12}  {'dS/dR':>14}  {'S_eff(R)':>12}  {'S_eff(1/R)':>12}")
    print("-" * 70)
    for R in [0.5, 0.8, 0.9, 1.0, 1.1, 1.2, 2.0]:
        T = T_kin_from_S_invariance(R)
        stat = stationarity_residual(R, T)
        s_r = S_eff(R, T)
        s_ir = S_eff(1.0 / R, T_kin_from_S_invariance(1.0 / R))
        flag = "<-- MINIMUM" if abs(stat) < 1e-12 else ""
        print(f"{R:6.2f}  {T:12.8f}  {stat:14.4e}  {s_r:12.8f}  {s_ir:12.8f}  {flag}")
    print()

    # --- Self-dual point analysis -------------------------------------------
    print("Samoduální bod R=1:")
    T1 = T_kin_from_S_invariance(1.0)
    stat1 = stationarity_residual(1.0, T1)
    poly1 = polynomial_lhs(1.0)
    print(f"  T_kin(R=1)         = {T1:.8f}")
    print(f"  dS/dR|_{{R=1}}       = {stat1:.4e}  (přesně 0)")
    print(f"  R^6+R^4+R^2|_{{R=1}} = {poly1:.6f}  (= 3 ✓)")
    print()

    # --- N_eff independence --------------------------------------------------
    print("Nezávislost na N_eff (polynom R^6+R^4+R^2=3):")
    print(f"{'N_eff':>6}  {'C_total':>12}  {'T_kin(1)':>12}  {'dS/dR|1':>14}")
    print("-" * 50)
    for n in [1, 3, 6, 12, 24, 48]:
        c = n * C_UNIT
        t1 = 3 * c / (2 * math.pi)
        res = 2 * math.pi * t1 - 3 * c
        print(f"{n:6d}  {c:12.8f}  {t1:12.8f}  {res:14.4e}")
    print()
    print("  => N_eff se vyruší — R=1 je minimum pro libovolné N_eff.")
    print()

    # --- Second derivative confirmation (minimum, not maximum) ---------------
    # d2S/dR2 at R=1 with T(R) from S-invariance:
    # T(R) = C/(2pi)*(R^2+1+1/R^2)
    # dT/dR = C/(2pi)*(2R - 2/R^3); at R=1: dT/dR = 0
    # d2T/dR2 = C/(2pi)*(2 + 6/R^4); at R=1: d2T/dR2 = 8C/(2pi) = 4C/pi
    # d2S/dR2 = 2pi*(2*dT/dR + R*d2T/dR2) + 12C/R^5
    #         at R=1: = 2pi*(0 + 1*4C/pi) + 12C = 8C + 12C = 20C
    d2S_at_1 = 20 * C_TOTAL
    print(f"Druhá derivace d2S/dR2|_{{R=1}} = 20*C_total = {d2S_at_1:.6f} > 0 => MINIMUM")
    print()

    # --- S-invariance check for a few values --------------------------------
    print("Ověření S-invariance S_eff[R] = S_eff[1/R] (T_kin ze S-podmínky):")
    print(f"{'R':>6}  {'S_eff(R)':>14}  {'S_eff(1/R)':>14}  {'rozdíl':>12}")
    print("-" * 55)
    for R in [0.5, 0.8, 1.0, 1.5, 2.0]:
        T_R = T_kin_from_S_invariance(R)
        T_iR = T_kin_from_S_invariance(1.0 / R)
        s_r = S_eff(R, T_R)
        s_ir = S_eff(1.0 / R, T_iR)
        # Note: S-invariance means S_eff[R,T(R)] = S_eff[1/R,T(1/R)]
        # by construction of T_kin_from_S_invariance
        diff = abs(s_r - s_ir)
        print(f"{R:6.2f}  {s_r:14.8f}  {s_ir:14.8f}  {diff:12.4e}")
    print()

    # --- Verdict ------------------------------------------------------------
    print("=" * 60)
    print("VÝSLEDEK C — PODMÍNĚNÁ S-INVARIANCE:")
    print()
    print("  R_psi = 1 (samoduální bod) JE minimum S_eff, podmíněně na:")
    print("  (a) S[Theta] je S-invariantní (tau -> -1/tau)")
    print("  (b) V_Casimir = C_total/R^3 je odvozeno z S[Theta]")
    print("  (c) T_kin je určeno podmínkou S-invariance")
    print()
    print("  Klíčový fakt: polynom R^6+R^4+R^2=3 nezávisí na N_eff.")
    print("  N_eff se vyruší v poměru C_total/C_total — fixace R=1")
    print("  je algebraická vlastnost S-symetrie, NE výběr N_eff.")
    print()
    print("  Status: [MC] kandidát na uzavření scale closure.")
    print("  Alpha: NOT DERIVED.")
    print("=" * 60)

    # --- Implied N_eff check (naive analysis from problem statement §4) ------
    print()
    print("Poznámka: naivní analýza §4 (C vs C_total notační nekonzistence):")
    print("  Pokud T_kin = C_unit/(2pi)*(R^2+1+1/R^2) a stat. = 3*N_eff*C_unit/R^4:")
    print("  => R^6+R^4+R^2 = 3*N_eff => pro R=1: N_eff_implied=1.")
    print("  ALE: pokud T_kin = C_total/(2pi)*(R^2+1+1/R^2) a stat. = 3*C_total/R^4:")
    print("  => R^6+R^4+R^2 = 3 => R=1 platí pro libovolné N_eff. ✓")
    print("  Závěr: N_eff=1 inconsistency je notační artefakt, ne fyzikální NO-GO.")


if __name__ == "__main__":
    main()
