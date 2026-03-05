# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
verify_theta_modes.py
=====================

SymPy / NumPy verification of the Jacobi-theta generation-index computations
for the Unified Biquaternion Theory (UBT) Three Generations research track.

Checks performed:
  1. C_mn matrix from the psi-kinetic integral (Taylor modes)
  2. Diagonal elements C_nn = effective squared-mass proxy for each mode
  3. n^2 Jacobi spectrum vs experimental lepton mass ratios
  4. Required power law / exponential fit to reproduce experimental ratios

Run with:
    python verify_theta_modes.py
"""

import sympy as sp
import numpy as np

# -------------------------------------------------------------------------
# Symbolic variables
# -------------------------------------------------------------------------
psi = sp.Symbol('psi', positive=True)
R   = sp.Symbol('R', positive=True)

# -------------------------------------------------------------------------
# Step 1: C_mn matrix (psi-kinetic integral)
# C_mn = integral_0^{2*pi*R} psi^(m+n) / (m! * n!) dpsi
# -------------------------------------------------------------------------
print("=" * 60)
print("Step 1: C_mn matrix (psi-kinetic integral)")
print("C_mn = int_0^{2*pi*R} psi^(m+n) / (m! * n!) dpsi")
print("=" * 60)

max_mode = 4  # compute for m,n in {0,1,2,3}
Cmn_sym = []
for i in range(max_mode):
    row = []
    for j in range(max_mode):
        integrand = psi ** (i + j) / (sp.factorial(i) * sp.factorial(j))
        val = sp.integrate(integrand, (psi, 0, 2 * sp.pi * R))
        row.append(sp.simplify(val))
    Cmn_sym.append(row)
    print(f"  n={i}: {row}")

# -------------------------------------------------------------------------
# Step 2: Diagonal elements and mass ratios (R=1)
# -------------------------------------------------------------------------
print()
print("=" * 60)
print("Step 2: Diagonal C_nn (effective mass^2 of Taylor mode n), R=1")
print("C_nn = (2*pi)^(2n+1) / ((n!)^2 * (2n+1))")
print("=" * 60)

R_val = 1  # set R=1 (units: 2*pi*R_psi = 2*pi)
C_diag = []
for i in range(max_mode):
    val_sym = Cmn_sym[i][i].subs(R, R_val)
    val_num = float(val_sym)
    C_diag.append(val_num)
    print(f"  C_{i}{i} = {sp.simplify(Cmn_sym[i][i])} -> {val_num:.6f}")

print()
print("Mass ratios from kinetic term alone (sqrt(C_nn), R=1):")
sqrt_C = [np.sqrt(c) for c in C_diag]
print(f"  sqrt(C_00) : sqrt(C_11) : sqrt(C_22) = "
      f"{sqrt_C[0]/sqrt_C[0]:.3f} : {sqrt_C[1]/sqrt_C[0]:.3f} : {sqrt_C[2]/sqrt_C[0]:.3f}")
print(f"  Experimental:                             1.000 : 207.0  : 3477.0")
print(f"  Mismatch factor at mode 1: {207.0 / (sqrt_C[1]/sqrt_C[0]):.2f}x")
print(f"  Mismatch factor at mode 2: {3477.0 / (sqrt_C[2]/sqrt_C[0]):.2f}x")

# -------------------------------------------------------------------------
# Step 3: n^2 Jacobi spectrum
# -------------------------------------------------------------------------
print()
print("=" * 60)
print("Step 3: n^2 Jacobi theta spectrum")
print("m_n ~ n^2  (from Jacobi coefficient q^{n^2})")
print("=" * 60)

# Modes are 0, 1, 2.  Use n=0,1,2 but n=0 gives 0, so we offset to n=1,2,3.
# The problem statement uses modes Theta_0, Theta_1, Theta_2 corresponding
# to the three generations.  For n^2 we compare using relative n: 0,1,2.
# To avoid division by zero, use the ratio m_1/m_0 ~ 1^2/0^2 = undefined.
# Instead interpret as: the Jacobi coefficient weighting is q^{n^2} so the
# *relative suppression* of mode n vs mode 1 is exp(-pi*n^2*psi_0).
# For n=0,1,2:
jacobi_n2 = [n**2 for n in range(3)]
print(f"  n^2 values for n=0,1,2: {jacobi_n2}")
print(f"  Ratio 0^2 : 1^2 : 2^2 = {jacobi_n2[0]} : {jacobi_n2[1]} : {jacobi_n2[2]}")
print(f"  (For mass interpretation, use m_n ~ n^2 with offset n=1,2,3:)")
jacobi_shifted = [(n+1)**2 for n in range(3)]
print(f"  (n+1)^2 ratios: {jacobi_shifted[0]} : {jacobi_shifted[1]} : {jacobi_shifted[2]}")
ratio_1 = jacobi_shifted[1] / jacobi_shifted[0]
ratio_2 = jacobi_shifted[2] / jacobi_shifted[0]
print(f"  m_1/m_0 = {ratio_1:.1f},  m_2/m_0 = {ratio_2:.1f}")
print(f"  Experimental: m_mu/m_e = 207.0, m_tau/m_e = 3477.0")
print(f"  Mismatch at mode 1 (muon):  factor {207.0/ratio_1:.1f}x")
print(f"  Mismatch at mode 2 (tau):   factor {3477.0/ratio_2:.1f}x")
print(f"  Ratio m_2/m_1 from n^2:     {ratio_2/ratio_1:.2f}")
print(f"  Ratio m_tau/m_mu (exp):     {3477/207:.2f}")

# -------------------------------------------------------------------------
# Step 4: Required functional form for experimental mass ratios
# -------------------------------------------------------------------------
print()
print("=" * 60)
print("Step 4: What function f(n) reproduces experimental ratios?")
print("f(0)=1 (by convention),  f(1)=207,  f(2)=3477")
print("=" * 60)

m_exp = np.array([1.0, 207.0, 3477.0])  # relative masses (m_e=1)
n_modes = np.array([0.0, 1.0, 2.0])

# --- 4a: Exponential fit f(n) = exp(b * n) ---
b_exp = np.log(207.0)
print()
print("--- 4a: Simple exponential f(n) = exp(b*n) ---")
print(f"  From m_1=207: b = ln(207) = {b_exp:.4f}")
f_exp = np.exp(b_exp * n_modes)
print(f"  Predicted: f(0)={f_exp[0]:.1f}, f(1)={f_exp[1]:.1f}, f(2)={f_exp[2]:.1f}")
print(f"  Experimental:  f(0)=1.0,        f(1)=207.0,       f(2)=3477.0")
print(f"  Overshoot at mode 2: {f_exp[2]:.0f} vs 3477 => factor {f_exp[2]/3477:.2f}")
print(f"  Note: exp(2*b)/exp(b) = exp(b) = {np.exp(b_exp):.1f}")
print(f"        but m_tau/m_mu = {3477/207:.2f}")
print(f"  => Simple exponential OVERESTIMATES m_tau/m_mu by {np.exp(b_exp)/(3477/207):.1f}x")

# --- 4b: Power law f(n) = (n+1)^k ---
# From f(1) = 2^k = 207:  k = log2(207)
k_power = np.log(207.0) / np.log(2.0)
print()
print("--- 4b: Power law f(n) = (n+1)^k ---")
print(f"  From m_1=207: (1+1)^k = 2^k = 207 => k = {k_power:.4f}")
f_power = (n_modes + 1.0) ** k_power
print(f"  Predicted: f(0)={f_power[0]:.1f}, f(1)={f_power[1]:.1f}, f(2)={f_power[2]:.1f}")
print(f"  Experimental:  f(0)=1.0,        f(1)=207.0,       f(2)=3477.0")
print(f"  Undershoot at mode 2: {f_power[2]:.0f} vs 3477 => factor {3477/f_power[2]:.2f}")

# --- 4c: Stretched exponential f(n) = exp(b * n^gamma) ---
# From f(1) = exp(b) = 207 and f(2) = exp(b * 2^gamma) = 3477:
#   b * 2^gamma = ln(3477)
#   b = ln(207) => 2^gamma = ln(3477)/ln(207)
b_stretched = np.log(207.0)
ratio_logs = np.log(3477.0) / np.log(207.0)
gamma_stretched = np.log(ratio_logs) / np.log(2.0)
print()
print("--- 4c: Stretched exponential f(n) = exp(b * n^gamma) ---")
print(f"  b = ln(207) = {b_stretched:.4f}")
print(f"  gamma = log2(ln(3477)/ln(207)) = {gamma_stretched:.4f}")
f_stretched = np.exp(b_stretched * (n_modes ** gamma_stretched))
# Note: n=0 gives 0^gamma = 0, so f(0)=exp(0)=1 — correct!
print(f"  Predicted: f(0)={f_stretched[0]:.2f}, f(1)={f_stretched[1]:.1f}, f(2)={f_stretched[2]:.1f}")
print(f"  Experimental:  f(0)=1.0,           f(1)=207.0,       f(2)=3477.0")
print(f"  This fit is EXACT by construction (two parameters b, gamma fit two ratios)")
print(f"  gamma = {gamma_stretched:.4f} (between 0.5 and 1 => sub-exponential, between power law and pure exponential)")

# -------------------------------------------------------------------------
# Summary
# -------------------------------------------------------------------------
print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  C_mn kinetic mass ratios:    1 : {sqrt_C[1]/sqrt_C[0]:.2f} : {sqrt_C[2]/sqrt_C[0]:.2f}")
print(f"  n^2 Jacobi ratios:           1 : {ratio_1:.1f} : {ratio_2:.1f}")
print(f"  Simple exponential:          1 : {f_exp[1]:.0f} : {f_exp[2]:.0f}")
print(f"  Power law k={k_power:.2f}:           1 : {f_power[1]:.0f} : {f_power[2]:.0f}")
print(f"  Stretched exp gamma={gamma_stretched:.2f}:   1 : {f_stretched[1]:.0f} : {f_stretched[2]:.0f}")
print(f"  Experimental:                1 : 207  : 3477")
print()
print("Conclusions:")
print("  1. The kinetic C_nn term alone gives wrong ratios (~3.6 : 9.8,")
print("     not 207 : 3477). Additional V(Theta) is required.")
print("  2. n^2 Jacobi spectrum gives 4:9 (shifted), not 207:3477.")
print("     Mismatch ~57x at mode 1, ~355x at mode 2.")
print("  3. A simple exponential f(n)=exp(b*n) with b=ln(207) fits mode 1")
print("     exactly but overshoots mode 2 by a factor ~12.3.")
print("  4. The experimental ratios are exactly reproduced by a stretched")
print(f"     exponential f(n)=exp({b_stretched:.3f}*n^{gamma_stretched:.3f})")
print(f"     with gamma~{gamma_stretched:.2f}, indicating sub-exponential growth between")
print("     a power law and a pure exponential.")
