import numpy as np

# --- Physical Constants ---
# Particle masses in MeV/c^2
m_e = 0.511  # Electron
m_mu = 105.7  # Muon
m_tau = 1777   # Tauon
# Other particles would be added here (quarks, etc.)

# High energy scale where UBT predicts alpha_0 (e.g., Planck scale in MeV)
M_UBT_scale = 1.22e22 

# --- Bare value from UBT ---
alpha_inv_bare = 137.0

def calculate_running_alpha_inv(bare_alpha_inv, high_scale, target_scale):
    """
    Calculates the "running" of the constant alpha^-1 from a high scale to a target scale.
    This simplified model includes only contributions from leptons.
    A full calculation would also include quarks and bosons.
    """
    
    # List of charged leptons (name, mass, charge^2)
    # Charge is in units of the elementary charge.
    leptons = [
        ('electron', m_e, (-1)**2),
        ('muon', m_mu, (-1)**2),
        ('tau', m_tau, (-1)**2)
    ]
    
    total_correction = 0.0
    
    # We sum the contributions from all particles whose mass lies between the scales
    print(f"Calculating corrections when running from {high_scale:.2e} MeV down to {target_scale:.2e} MeV:")
    for name, mass, charge_sq in leptons:
        if target_scale < mass < high_scale:
            # Standard formula for the one-loop QED correction
            # The sign is positive because we are running from high energy to low energy (1/alpha increases)
            term = (charge_sq / (3 * np.pi)) * np.log(high_scale**2 / mass**2)
            total_correction += term
            print(f"  - Contribution from '{name}': {term:.6f}")
            
    # The value of 1/alpha increases towards lower energies
    alpha_inv_at_target_scale = bare_alpha_inv + total_correction
    
    return alpha_inv_at_target_scale

# --- Example Calculation ---
# The target scale for measuring alpha_exp is very low (q^2 -> 0)
# For illustration, we use the electron mass as the reference low scale here.
low_energy_scale = m_e

final_alpha_inv = calculate_running_alpha_inv(alpha_inv_bare, M_UBT_scale, low_energy_scale)

print("\n-------------------------------------------------------------")
print(f"Theoretical 'bare' value 1/alpha_0 from UBT: {alpha_inv_bare}")
print(f"Calculated value 1/alpha at low energy (leptons only): ~{final_alpha_inv:.6f}")
print("-------------------------------------------------------------")
print("Note: To achieve the precise experimental value of ~137.036,")
print("contributions from hadrons and electroweak bosons must also be included.")
print("This script's purpose is to demonstrate the principle.")
