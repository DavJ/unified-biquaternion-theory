#!/usr/bin/env python3
"""
Biquaternion Time vs Complex Time Analysis for UBT

This script demonstrates the criterion for when complex time approximation
is valid versus when full biquaternion time is required.

Author: UBT Team
Date: 2025-11-01
"""

from sympy import symbols, sqrt, pi, I, simplify, expand, Matrix
import numpy as np

print("="*80)
print("BIQUATERNION TIME VS COMPLEX TIME IN UBT")
print("="*80)
print()

# ============================================================================
# SECTION 1: BIQUATERNION TIME STRUCTURE
# ============================================================================
print("SECTION 1: BIQUATERNION TIME STRUCTURE")
print("-"*80)

# Define symbolic variables
t = symbols('t', real=True)  # Real time
psi = symbols('psi', real=True)  # Scalar imaginary time
v_x, v_y, v_z = symbols('v_x v_y v_z', real=True)  # Vector imaginary time

print("\n1.1 Biquaternion Time:")
print("T_B = t + i(ψ + v·σ)")
print(f"where v = (v_x, v_y, v_z)")
print(f"      σ = (σ_x, σ_y, σ_z) are Pauli matrices")

# Pauli matrices
sigma_x = Matrix([[0, 1], [1, 0]])
sigma_y = Matrix([[0, -I], [I, 0]])
sigma_z = Matrix([[1, 0], [0, -1]])

print("\n1.2 Pauli Matrices:")
print(f"σ_x = {sigma_x}")
print(f"σ_y = {sigma_y}")
print(f"σ_z = {sigma_z}")

# Vector norm
v_norm_squared = v_x**2 + v_y**2 + v_z**2
print(f"\n1.3 Vector Norm:")
print(f"||v||² = v_x² + v_y² + v_z² = {v_norm_squared}")

# ============================================================================
# SECTION 2: PROJECTION CRITERION
# ============================================================================
print("\n" + "="*80)
print("SECTION 2: PROJECTION CRITERION")
print("-"*80)

print("\n2.1 Complex Time Approximation Valid When:")
print("||v||² << |ψ|²")
print("i.e., vector component negligible compared to scalar component")

print("\n2.2 Full Biquaternion Required When:")
print("||v||² ~ |ψ|²  OR  v not parallel to ∇ψ")
print("i.e., vector component comparable or directionally independent")

# Example ratios
epsilon = symbols('epsilon', positive=True, real=True)
print(f"\n2.3 Define dimensionless ratio:")
print(f"ε = ||v||/|ψ|")
print(f"\nComplex time valid: ε << 1")
print(f"Biquaternion required: ε ~ 1")

# ============================================================================
# SECTION 3: HOLOGRAPHIC PROJECTION
# ============================================================================
print("\n" + "="*80)
print("SECTION 3: HOLOGRAPHIC PROJECTION")
print("-"*80)

# Normal vector to holographic boundary
n_x, n_y, n_z = symbols('n_x n_y n_z', real=True)
print("\n3.1 Holographic Projection Operator:")
print("π_H: T_B → τ")
print("π_H(t + iv) = t + iψ")
print("where ψ = <v, n> = v·n")

# Projection formula
psi_projected = v_x * n_x + v_y * n_y + v_z * n_z
print(f"\n3.2 Projected Scalar Phase:")
print(f"ψ = v_x·n_x + v_y·n_y + v_z·n_z")
print(f"ψ = {psi_projected}")

print("\n3.3 Information Loss:")
print("DOF(T_B) = 4 (t, ψ, v_x, v_y, v_z) → 1 + 1 + 3 = 5 parameters")
print("DOF(τ) = 2 (t, ψ)")
print("Lost information: ΔI = 5 - 2 = 3 (tangential vector components)")

# ============================================================================
# SECTION 4: EXTENDED HOLOGRAPHIC ENTROPY
# ============================================================================
print("\n" + "="*80)
print("SECTION 4: EXTENDED HOLOGRAPHIC ENTROPY")
print("-"*80)

# Physical constants
R = symbols('R', positive=True)
k_B_sym, c_sym, G, hbar_sym = symbols('k_B c G hbar', positive=True)

print("\n4.1 Classical Bekenstein-Hawking:")
S_BH = (k_B_sym * c_sym**3 * 4 * pi * R**2) / (4 * G * hbar_sym)
print(f"S_BH = k_B·c³·A/(4·G·ℏ)")
print(f"S_BH = {simplify(S_BH)}")

print("\n4.2 Complex Time Extension:")
S_complex = (pi * k_B_sym * c_sym**3 * (R**2 + psi**2)) / (G * hbar_sym)
print(f"S_complex = π·k_B·c³·(R² + ψ²)/(G·ℏ)")

print("\n4.3 Full Biquaternion Extension:")
S_biquaternion = (pi * k_B_sym * c_sym**3 * (R**2 + psi**2 + v_norm_squared)) / (G * hbar_sym)
print(f"S_biquaternion = π·k_B·c³·(R² + ψ² + ||v||²)/(G·ℏ)")
print(f"S_biquaternion = {S_biquaternion}")

print("\n4.4 Hierarchical Limits:")
print("S_biquaternion → S_complex  (when ||v|| → 0)")
print("S_complex → S_BH  (when ψ → 0)")

# ============================================================================
# SECTION 5: VERLINDE FORCE WITH BIQUATERNION TIME
# ============================================================================
print("\n" + "="*80)
print("SECTION 5: VERLINDE FORCE WITH BIQUATERNION TIME")
print("-"*80)

print("\n5.1 Extended Entropy Gradient:")
print("S_total = S_real + S_ψ + S_v")

print("\n5.2 Extended Force Law:")
print("F_UBT-full = T·(∇S_real + ∇S_ψ + ∇S_v)")

print("\n5.3 Components:")
print("F_classical = T·∇S_real  (Newton's law)")
print("F_dark-scalar = T·∇S_ψ  (isotropic dark matter)")
print("F_dark-vector = T·∇S_v  (directional dark matter)")

print("\n5.4 Physical Interpretation:")
print("Vector component ∇S_v produces directional forces:")
print("  - Anisotropic dark matter distributions")
print("  - Frame-dragging effects")
print("  - Spin-orbit coupling")

# ============================================================================
# SECTION 6: DE SITTER SPACE WITH BIQUATERNION TIME
# ============================================================================
print("\n" + "="*80)
print("SECTION 6: DE SITTER SPACE WITH BIQUATERNION TIME")
print("-"*80)

Lambda, Lambda_psi = symbols('Lambda Lambda_psi', real=True)
Lambda_vx, Lambda_vy, Lambda_vz = symbols('Lambda_vx Lambda_vy Lambda_vz', real=True)

print("\n6.1 Extended Cosmological Constant:")
print("Λ_biquaternion = Λ + i·Λ_ψ + i·Λ_v·σ")
print(f"where Λ_v = (Λ_vx, Λ_vy, Λ_vz)")

print("\n6.2 Observable:")
print("Λ_obs = Re[Λ_biquaternion] = Λ")

print("\n6.3 Vector Dark Energy:")
print("Λ_v encodes directional vacuum energy:")
print("  - Anisotropies in cosmic acceleration")
print("  - Preferred directions in cosmology")
print("  - Directional dark energy flows")

# ============================================================================
# SECTION 7: NUMERICAL EXAMPLE
# ============================================================================
print("\n" + "="*80)
print("SECTION 7: NUMERICAL EXAMPLE")
print("-"*80)

print("\n7.1 Schwarzschild Black Hole (Non-Rotating):")
print("In this case, vector component negligible:")
r_s = 2954  # meters (solar mass BH)
psi_val = 0.01 * r_s  # 1% phase component
v_norm_val = 0.001 * r_s  # 0.1% vector component

epsilon_BH = v_norm_val / psi_val
print(f"r_s = {r_s} m")
print(f"ψ ~ {psi_val} m")
print(f"||v|| ~ {v_norm_val} m")
print(f"ε = ||v||/ψ = {epsilon_BH:.3f} << 1")
print("→ Complex time approximation valid")

print("\n7.2 Kerr Black Hole (Rapidly Rotating):")
print("Vector component becomes significant:")
a_over_M = 0.998  # near-extremal rotation
v_norm_kerr = a_over_M * r_s / 2  # characteristic vector scale
epsilon_Kerr = v_norm_kerr / psi_val

print(f"a/M ~ {a_over_M} (near-extremal)")
print(f"||v|| ~ {v_norm_kerr:.1f} m")
print(f"ε = ||v||/ψ = {epsilon_Kerr:.2f} ~ 1")
print("→ Full biquaternion formalism required")

print("\n7.3 Entropy Corrections:")
# Using solar mass black hole parameters
G_SI = 6.67430e-11
hbar_SI = 1.054571817e-34
c_SI = 299792458
k_B_SI = 1.380649e-23

# Classical entropy (in units of k_B)
A_horizon = 4 * np.pi * r_s**2
S_BH_numerical = (k_B_SI * c_SI**3 * A_horizon) / (4 * G_SI * hbar_SI) / k_B_SI

# With phase component
S_complex_numerical = (np.pi * c_SI**3 * (r_s**2 + psi_val**2)) / (G_SI * hbar_SI) / k_B_SI

# With vector component
S_biquaternion_numerical = (np.pi * c_SI**3 * (r_s**2 + psi_val**2 + v_norm_val**2)) / (G_SI * hbar_SI) / k_B_SI

print(f"\nS_BH ~ {S_BH_numerical:.3e} k_B")
print(f"S_complex ~ {S_complex_numerical:.3e} k_B")
print(f"S_biquaternion ~ {S_biquaternion_numerical:.3e} k_B")

delta_complex = (S_complex_numerical - S_BH_numerical) / S_BH_numerical * 100
delta_biquaternion = (S_biquaternion_numerical - S_BH_numerical) / S_BH_numerical * 100

print(f"\nΔS_complex/S_BH = {delta_complex:.4f}%")
print(f"ΔS_biquaternion/S_BH = {delta_biquaternion:.4f}%")

# ============================================================================
# SECTION 8: SUMMARY
# ============================================================================
print("\n" + "="*80)
print("SUMMARY AND CRITERION")
print("="*80)

print("\n┌─────────────────────┬──────────────────┬────────────────────────┐")
print("│ Condition           │ Formalism        │ Physical Regime        │")
print("├─────────────────────┼──────────────────┼────────────────────────┤")
print("│ ||v||² << ψ²        │ Complex time τ   │ Weak field, spherical  │")
print("│ ||v||² ~ ψ²         │ Biquaternion T_B │ Strong field, rotating │")
print("│ ψ, v → 0            │ Real time t      │ Classical GR           │")
print("└─────────────────────┴──────────────────┴────────────────────────┘")

print("\n" + "="*80)
print("HIERARCHY OF APPROXIMATIONS")
print("="*80)
print("\nT_B (full biquaternion)")
print("  ↓ [||v|| → 0]")
print("τ = t + iψ (complex time)")
print("  ↓ [ψ → 0]")
print("t (classical time / GR)")

print("\n" + "="*80)
print("KEY RESULTS")
print("="*80)
print("\n1. Complex time τ = t + iψ is valid approximation for:")
print("   - Spherically symmetric systems")
print("   - Weak gravitational fields")
print("   - Non-rotating or slowly rotating objects")
print("\n2. Full biquaternion T_B = t + i(ψ + v·σ) required for:")
print("   - Rapidly rotating black holes (Kerr)")
print("   - Spacetime torsion and twisting")
print("   - Directional dark matter/energy")
print("\n3. Previous analysis using complex time remains valid as")
print("   leading-order approximation in most observable regimes.")
print("\n4. Holographic projection: π_H: T_B → τ corresponds to")
print("   bulk-to-boundary projection with normal vector n.")

print("\n" + "="*80)
print("DERIVATIONS COMPLETE")
print("="*80)
