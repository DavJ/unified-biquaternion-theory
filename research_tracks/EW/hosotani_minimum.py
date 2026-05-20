import numpy as np
from scipy.optimize import minimize_scalar

def V_modified(alpha, R=1.0, N_bos=6, N_fer=6, N_terms=200):
    V_bos = 0.0
    V_fer = 0.0
    for n in range(1, N_terms+1):
        V_bos -= np.cos(n * alpha) / (n**2 * 2 * np.pi * R)
        V_fer += np.cos((n - 0.5) * alpha) / ((n-0.5)**2 * 2*np.pi * R)
    return N_bos * V_bos + N_fer * V_fer

alpha_vals = np.linspace(0, 2*np.pi, 2000)
V_vals = [V_modified(a) for a in alpha_vals]
idx_min = np.argmin(V_vals)
alpha_min = alpha_vals[idx_min]

print(f"Min: alpha = {alpha_min:.6f} rad = {alpha_min/np.pi:.6f}*pi")
print(f"V_min = {V_vals[idx_min]:.8f}")
print(f"SSB (alpha != 0,2pi): {0.1 < alpha_min < 2*np.pi - 0.1}")

g_W = 0.653
M_W = g_W * alpha_min / (2 * np.pi)
print(f"M_W/M_Pl = {M_W:.8f}")
if M_W != 0:
    print(f"Pro M_W=80 GeV: M_Pl={80/M_W:.3e} GeV (vs 1.22e19)")
else:
    print("M_W = 0, nelze spočítat poměr k M_Pl")
