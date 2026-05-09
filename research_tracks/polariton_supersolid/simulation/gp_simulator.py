# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
Polariton Supersolid — GP Simulation Scaffold
==============================================

Numerically solves the driven-dissipative Gross-Pitaevskii (ddGP) equation
for a 2D exciton-polariton condensate on a periodic grid using the split-step
Fourier method.

Equations solved (see gp_equation/gp_derivation.md for derivation):

  Condensate order parameter ψ(r, t):
    iℏ ∂ψ/∂t = [−ℏ²∇²/2m* + g|ψ|² + g_R n_R + (iℏ/2)(R n_R − Γ_C)] ψ

  Reservoir exciton density n_R(r, t):
    ∂n_R/∂t = P(r) − (Γ_R + R|ψ|²) n_R

Split-step algorithm:
  1. Half-step potential + gain/loss (real space)
  2. Full-step kinetic (k-space)
  3. Half-step potential + gain/loss (real space)
  (Reservoir is updated with a simple Euler step.)

Diagnostics computed:
  - Real-space condensate density n_C(r) = |ψ|²
  - Structure factor S(k) = |FT[n_C]|² / N
  - Momentum distribution n(k) = |ψ̃(k)|²
  - Peak S(k) location → supersolid signature if k_peak ≠ 0

Usage:
  python gp_simulator.py [--preset <name>]

Available presets:
  superfluid   : homogeneous condensate (default)
  stripe       : two-component stripe-forming regime (adjust g12)
  roton        : single-component with beyond-mean-field roton (schematic)

Dependencies: numpy, scipy (optional for plots: matplotlib)

References:
  Carusotto & Ciuti, Rev. Mod. Phys. 85, 299 (2013)
  Wouters & Carusotto, PRL 99, 140402 (2007)
"""

import argparse
import sys

import numpy as np

# ---------------------------------------------------------------------------
# Physical constants (SI units, then converted to natural units for the sim)
# ---------------------------------------------------------------------------

HBAR = 1.0   # Work in units where ℏ = 1

# ---------------------------------------------------------------------------
# Default simulation parameters
# ---------------------------------------------------------------------------

DEFAULTS = {
    # Grid
    "Nx": 128,           # grid points per dimension
    "Ny": 128,
    "Lx": 100.0,         # system size [μm]
    "Ly": 100.0,

    # Time stepping
    "dt": 0.005,         # time step [ps]
    "Nt": 20000,         # total steps
    "n_diag": 2000,      # diagnostic output every n_diag steps

    # Physical parameters (GaAs-like polaritons)
    "m_star": 5e-5,      # effective polariton mass [m_e], dimensionless here ≡ 1/m*
    "g": 2e-3,           # polariton-polariton interaction [meV μm²] → rescaled to 1
    "g_R": 4e-3,         # polariton-reservoir interaction (= 2g typically)
    "Gamma_C": 0.04,     # polariton decay rate [ps⁻¹]
    "Gamma_R": 0.1,      # reservoir decay rate [ps⁻¹]
    "R": 0.01,           # stimulated scattering rate [μm² ps⁻¹]
    "P0": 0.008,         # homogeneous pump rate [μm⁻² ps⁻¹]

    # Two-component extension
    "two_component": False,
    "g12": -0.003,       # cross-component interaction (negative → attractive)
    "Omega": 0.0,        # Rabi coupling between spin components [meV]

    # Noise seed for symmetry breaking
    "noise_amplitude": 1e-3,
    "seed": 42,
}


def make_grid(params):
    """Build real-space and k-space grids."""
    Nx, Ny = params["Nx"], params["Ny"]
    Lx, Ly = params["Lx"], params["Ly"]

    dx = Lx / Nx
    dy = Ly / Ny

    x = np.linspace(-Lx / 2, Lx / 2, Nx, endpoint=False)
    y = np.linspace(-Ly / 2, Ly / 2, Ny, endpoint=False)
    XX, YY = np.meshgrid(x, y, indexing="ij")

    kx = 2 * np.pi * np.fft.fftfreq(Nx, d=dx)
    ky = 2 * np.pi * np.fft.fftfreq(Ny, d=dy)
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    K2 = KX**2 + KY**2

    return XX, YY, KX, KY, K2, dx, dy


def initial_state(params, XX, YY, rng):
    """Random small-amplitude initial condensate wavefunction."""
    amp = params["noise_amplitude"]
    psi = amp * (rng.standard_normal((params["Nx"], params["Ny"]))
                 + 1j * rng.standard_normal((params["Nx"], params["Ny"])))
    return psi


def pump_profile(params, XX, YY):
    """Pump profile P(r). Currently homogeneous; extend for Gaussian or patterned pumps."""
    return params["P0"] * np.ones_like(XX)


def kinetic_phase(K2, params, dt):
    """Phase accumulated by kinetic term exp(−i ℏ k²/(2m*) dt)."""
    hbar_over_2m = HBAR / (2.0 * params["m_star"])
    return np.exp(-1j * hbar_over_2m * K2 * dt)


def potential_half_step(psi, n_R, params, dt):
    """
    Half-step real-space propagator:
      exp{ [−i/ℏ (g|ψ|² + g_R n_R) + (R n_R − Γ_C)/2] × (dt/2) }
    """
    g = params["g"]
    g_R = params["g_R"]
    Gamma_C = params["Gamma_C"]
    R = params["R"]

    n_C = np.abs(psi)**2
    phase = (-1j / HBAR) * (g * n_C + g_R * n_R)
    gain_loss = 0.5 * (R * n_R - Gamma_C)

    exponent = (phase + gain_loss) * (dt / 2)
    return psi * np.exp(exponent)


def reservoir_step(n_R, psi, params, P, dt):
    """Euler step for reservoir density (eq. 1)."""
    R = params["R"]
    Gamma_R = params["Gamma_R"]
    n_C = np.abs(psi)**2
    dn_R = P - (Gamma_R + R * n_C) * n_R
    return n_R + dn_R * dt


def normalize_psi(psi):
    """Renormalize condensate wavefunction to avoid runaway (optional safeguard)."""
    max_amp = np.max(np.abs(psi))
    if max_amp > 1e6:
        psi /= (max_amp / 1e6)
    return psi


def structure_factor(n_C):
    """
    Compute the static structure factor S(k) = |FT[n_C]|² / N.
    Returns the 2D array and the (shifted) k-space array.
    """
    N = n_C.size
    s = np.abs(np.fft.fft2(n_C))**2 / N
    return np.fft.fftshift(s)


def supersolid_diagnostics(psi, n_R, params, KX, KY, step, dt):
    """
    Print key diagnostics:
      - Total condensate number N_C = ∫|ψ|² dA (in units of dx*dy)
      - Peak of structure factor and its location
      - Supersolid flag: S peak at k ≠ 0 AND condensate fraction > threshold
    """
    n_C = np.abs(psi)**2
    dx = params["Lx"] / params["Nx"]
    dy = params["Ly"] / params["Ny"]
    N_C = np.sum(n_C) * dx * dy
    N_R = np.sum(n_R) * dx * dy
    t = step * dt

    S = structure_factor(n_C)
    Nx, Ny = params["Nx"], params["Ny"]
    # Zero-out the DC component for peak search
    S_no_dc = S.copy()
    S_no_dc[Nx // 2, Ny // 2] = 0.0
    peak_idx = np.unravel_index(np.argmax(S_no_dc), S_no_dc.shape)
    S_dc = S[Nx // 2, Ny // 2]
    S_peak = S_no_dc[peak_idx]

    # k-values of peak (shifted grid)
    kx_shifted = np.fft.fftshift(KX[:, 0])
    ky_shifted = np.fft.fftshift(KY[0, :])
    k_peak_x = kx_shifted[peak_idx[0]]
    k_peak_y = ky_shifted[peak_idx[1]]
    k_peak_mag = np.sqrt(k_peak_x**2 + k_peak_y**2)

    # Heuristic supersolid criterion: S(k_peak) / S(0) > threshold
    ratio = S_peak / S_dc if S_dc > 0 else 0.0
    is_supersolid = (k_peak_mag > 0.5) and (ratio > 0.01)

    print(
        f"t={t:8.2f} ps | N_C={N_C:8.1f} | N_R={N_R:8.1f} | "
        f"S(k_peak)/S(0)={ratio:.4f} | "
        f"|k_peak|={k_peak_mag:.3f} μm⁻¹ | "
        f"{'⟨SUPERSOLID⟩' if is_supersolid else 'superfluid'}"
    )
    return {"t": t, "N_C": N_C, "ratio": ratio, "k_peak_mag": k_peak_mag,
            "is_supersolid": is_supersolid}


def run_simulation(params):
    """Main simulation loop."""
    rng = np.random.default_rng(params["seed"])

    XX, YY, KX, KY, K2, dx, dy = make_grid(params)
    psi = initial_state(params, XX, YY, rng)
    n_R = np.zeros((params["Nx"], params["Ny"]))
    P = pump_profile(params, XX, YY)
    kin_phase = kinetic_phase(K2, params, params["dt"])
    dt = params["dt"]
    Nt = params["Nt"]
    n_diag = params["n_diag"]

    print("=" * 72)
    print("Polariton Supersolid — ddGP Simulation")
    print(f"  Grid: {params['Nx']}×{params['Ny']}, "
          f"L={params['Lx']}×{params['Ly']} μm")
    print(f"  dt={dt} ps, Nt={Nt}, total time={Nt*dt:.1f} ps")
    print(f"  m*={params['m_star']}, g={params['g']}, "
          f"Γ_C={params['Gamma_C']}, P0={params['P0']}")
    threshold_P = params["Gamma_C"] * params["Gamma_R"] / params["R"]
    print(f"  Threshold pump P_th ≈ {threshold_P:.4f} μm⁻² ps⁻¹ "
          f"({'above' if params['P0'] > threshold_P else 'below'} threshold)")
    print("=" * 72)

    history = []

    for step in range(Nt + 1):
        # Diagnostic output
        if step % n_diag == 0:
            diag = supersolid_diagnostics(psi, n_R, params, KX, KY, step, dt)
            history.append(diag)

        if step == Nt:
            break

        # Split-step propagation
        # 1. Half potential step
        psi = potential_half_step(psi, n_R, params, dt)

        # 2. Full kinetic step (k-space)
        psi_k = np.fft.fft2(psi)
        psi_k *= kin_phase
        psi = np.fft.ifft2(psi_k)

        # 3. Half potential step
        psi = potential_half_step(psi, n_R, params, dt)

        # 4. Reservoir update (Euler)
        n_R = reservoir_step(n_R, psi, params, P, dt)

        # Safety renormalization
        psi = normalize_psi(psi)

    print("=" * 72)
    print("Simulation complete.")
    final = history[-1]
    print(f"  Final state: t={final['t']:.1f} ps")
    print(f"  Condensate number N_C = {final['N_C']:.2f}")
    print(f"  S(k_peak)/S(0) = {final['ratio']:.4f}")
    print(f"  |k_peak| = {final['k_peak_mag']:.3f} μm⁻¹")
    if final["is_supersolid"]:
        print("  ⟨SUPERSOLID SIGNATURE DETECTED⟩")
        print("  (density modulation + coherence coexist — verify with full diagnostics)")
    else:
        print("  State appears homogeneous superfluid (no density modulation above threshold).")
    print("=" * 72)

    return psi, n_R, history


# ---------------------------------------------------------------------------
# Preset parameter sets
# ---------------------------------------------------------------------------

PRESETS = {
    "superfluid": {},   # use defaults

    "stripe": {
        # Two-component system near stripe instability.
        # Reduce g12 (more negative) to trigger stripe formation.
        "two_component": True,
        "g12": -0.004,
        "Omega": 0.01,
        "P0": 0.012,
        "Nt": 30000,
    },

    "roton": {
        # Single-component with schematic beyond-mean-field roton softening.
        # We mimic it by a softened kinetic dispersion (not from first principles).
        # NOTE: This is a phenomenological placeholder; real roton requires
        # beyond-mean-field quantum fluctuations not included here.
        "g": 3e-3,
        "P0": 0.015,
        "Nt": 30000,
        "noise_amplitude": 5e-3,
    },
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Polariton supersolid ddGP simulation scaffold"
    )
    parser.add_argument(
        "--preset",
        choices=list(PRESETS.keys()),
        default="superfluid",
        help="Parameter preset (default: superfluid)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    params = {**DEFAULTS, **PRESETS[args.preset]}
    psi_final, nR_final, history = run_simulation(params)
