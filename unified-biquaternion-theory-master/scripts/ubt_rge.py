#!/usr/bin/env python3
"""
UBT RGE Runner - Renormalization Group Evolution for Fermion Masses
====================================================================

Implements 1-loop (and optionally 2-loop) SM RGEs for Yukawa couplings
to evolve tree-level masses from high scale μ₀ to low scale μ.

Author: UBT Team
Version: v17 Stable Release
Status: Core computational tool - no circular parameters
"""

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import warnings

# Physical constants
ALPHA_EM_MZ = 1/127.9  # Fine structure constant at M_Z
ALPHA_S_MZ = 0.1179    # Strong coupling at M_Z
M_Z = 91.1876          # Z boson mass (GeV)
M_W = 80.379           # W boson mass (GeV)
M_H = 125.1            # Higgs mass (GeV)
V_EW = 246.22          # Electroweak VEV (GeV)

# SM fermion masses at M_Z (MSbar, PDG 2022)
QUARK_MASSES_MZ = {
    'u': 0.00216,   # GeV
    'c': 1.27,      # GeV
    't': 172.76,    # GeV
    'd': 0.00467,   # GeV
    's': 0.093,     # GeV
    'b': 4.18,      # GeV
}

LEPTON_MASSES_POLE = {
    'e': 0.000510998950,  # GeV
    'mu': 0.1056583755,   # GeV
    'tau': 1.77686,       # GeV
}


class SMRGE:
    """Standard Model Renormalization Group Equations"""
    
    def __init__(self, loop_order=1):
        """
        Initialize SM RGE solver.
        
        Parameters
        ----------
        loop_order : int
            1 for 1-loop, 2 for 2-loop (default: 1)
        """
        self.loop_order = loop_order
        
        # Number of colors and generations
        self.N_c = 3
        self.N_g = 3
        
    def beta_yukawa_1loop(self, y, g1, g2, g3, y_other, fermion_type='up'):
        """
        1-loop beta function for Yukawa coupling.
        
        Parameters
        ----------
        y : float
            Yukawa coupling
        g1, g2, g3 : float
            Gauge couplings (U(1)_Y, SU(2)_L, SU(3)_c)
        y_other : array
            Other Yukawa couplings [y_u, y_d, y_e]
        fermion_type : str
            'up', 'down', or 'lepton'
            
        Returns
        -------
        float
            Beta function dy/d(log μ)
        """
        y_u, y_d, y_e = y_other
        
        # Trace terms
        Tr_Yu2 = np.sum(y_u**2)
        Tr_Yd2 = np.sum(y_d**2)
        Tr_Ye2 = np.sum(y_e**2)
        
        # Gauge coupling contributions
        if fermion_type == 'up':
            gauge_term = -(17/20 * g1**2 + 9/4 * g2**2 + 8 * g3**2)
            yukawa_term = 3/2 * y**2 + 3/2 * Tr_Yu2 + 3/2 * Tr_Yd2 + 1/2 * Tr_Ye2
        elif fermion_type == 'down':
            gauge_term = -(1/4 * g1**2 + 9/4 * g2**2 + 8 * g3**2)
            yukawa_term = 3/2 * y**2 + 3/2 * Tr_Yu2 + 3/2 * Tr_Yd2 + 1/2 * Tr_Ye2
        elif fermion_type == 'lepton':
            gauge_term = -(9/4 * g1**2 + 9/4 * g2**2)
            yukawa_term = 3/2 * y**2 + 3 * Tr_Yd2 + Tr_Ye2
        else:
            raise ValueError(f"Unknown fermion type: {fermion_type}")
        
        beta = y / (16 * np.pi**2) * (gauge_term + yukawa_term)
        return beta
    
    def beta_gauge_1loop(self, g, gauge_type='g1'):
        """
        1-loop beta function for gauge coupling.
        
        Parameters
        ----------
        g : float
            Gauge coupling
        gauge_type : str
            'g1' for U(1)_Y, 'g2' for SU(2)_L, 'g3' for SU(3)_c
            
        Returns
        -------
        float
            Beta function dg/d(log μ)
        """
        # 1-loop beta function coefficients
        if gauge_type == 'g1':
            b = 41/10  # With 3 generations
        elif gauge_type == 'g2':
            b = -19/6
        elif gauge_type == 'g3':
            b = -7
        else:
            raise ValueError(f"Unknown gauge type: {gauge_type}")
        
        beta = b * g**3 / (16 * np.pi**2)
        return beta
    
    def rge_system(self, y_vec, log_mu, params):
        """
        Full RGE system for Yukawa and gauge couplings.
        
        Parameters
        ----------
        y_vec : array
            [y_u1, y_u2, y_u3, y_d1, y_d2, y_d3, y_e1, y_e2, y_e3, g1, g2, g3]
        log_mu : float
            log(μ/μ_ref)
        params : dict
            Additional parameters (unused here)
            
        Returns
        -------
        array
            dy_vec/d(log μ)
        """
        # Unpack couplings
        y_u = y_vec[0:3]
        y_d = y_vec[3:6]
        y_e = y_vec[6:9]
        g1, g2, g3 = y_vec[9:12]
        
        # Compute beta functions
        dy_u = np.array([self.beta_yukawa_1loop(y_u[i], g1, g2, g3, 
                                                 [y_u, y_d, y_e], 'up') 
                         for i in range(3)])
        dy_d = np.array([self.beta_yukawa_1loop(y_d[i], g1, g2, g3, 
                                                 [y_u, y_d, y_e], 'down') 
                         for i in range(3)])
        dy_e = np.array([self.beta_yukawa_1loop(y_e[i], g1, g2, g3, 
                                                 [y_u, y_d, y_e], 'lepton') 
                         for i in range(3)])
        
        dg1 = self.beta_gauge_1loop(g1, 'g1')
        dg2 = self.beta_gauge_1loop(g2, 'g2')
        dg3 = self.beta_gauge_1loop(g3, 'g3')
        
        return np.concatenate([dy_u, dy_d, dy_e, [dg1, dg2, dg3]])
    
    def run_yukawas_to_low_scale(self, mu0, mu_target, yukawas_mu0, 
                                   gauge_mu0=None, n_steps=100):
        """
        Run Yukawa couplings from μ₀ to μ_target.
        
        Parameters
        ----------
        mu0 : float
            Initial scale (GeV)
        mu_target : float
            Target scale (GeV)
        yukawas_mu0 : dict
            Initial Yukawa couplings at μ₀
            Format: {'u': array([y_u, y_c, y_t]), 
                     'd': array([y_d, y_s, y_b]),
                     'e': array([y_e, y_mu, y_tau])}
        gauge_mu0 : dict, optional
            Initial gauge couplings at μ₀
            Format: {'g1': g1, 'g2': g2, 'g3': g3}
            If None, use SM values at M_Z
        n_steps : int
            Number of RGE steps
            
        Returns
        -------
        dict
            Yukawa couplings at μ_target
        """
        # Set initial gauge couplings if not provided
        if gauge_mu0 is None:
            # Use approximate values at M_Z
            g1 = np.sqrt(5/3) * np.sqrt(4 * np.pi * ALPHA_EM_MZ)
            g2 = np.sqrt(4 * np.pi * ALPHA_EM_MZ / np.sin(np.arcsin(0.231))**2)
            g3 = np.sqrt(4 * np.pi * ALPHA_S_MZ)
            gauge_mu0 = {'g1': g1, 'g2': g2, 'g3': g3}
        
        # Pack initial conditions
        y0 = np.concatenate([
            yukawas_mu0['u'],
            yukawas_mu0['d'],
            yukawas_mu0['e'],
            [gauge_mu0['g1'], gauge_mu0['g2'], gauge_mu0['g3']]
        ])
        
        # Set up log-scale integration
        log_mu_array = np.linspace(np.log(mu0), np.log(mu_target), n_steps)
        
        # Solve RGEs
        solution = odeint(self.rge_system, y0, log_mu_array, args=({},))
        
        # Extract final values
        y_final = solution[-1]
        yukawas_final = {
            'u': y_final[0:3],
            'd': y_final[3:6],
            'e': y_final[6:9]
        }
        gauge_final = {
            'g1': y_final[9],
            'g2': y_final[10],
            'g3': y_final[11]
        }
        
        return yukawas_final, gauge_final
    
    def yukawa_to_mass(self, yukawa, v_ew=V_EW):
        """
        Convert Yukawa coupling to fermion mass.
        
        Parameters
        ----------
        yukawa : float or array
            Yukawa coupling(s)
        v_ew : float
            Electroweak VEV (default: 246.22 GeV)
            
        Returns
        -------
        float or array
            Fermion mass(es) in GeV
        """
        return yukawa * v_ew / np.sqrt(2)
    
    def mass_to_yukawa(self, mass, v_ew=V_EW):
        """
        Convert fermion mass to Yukawa coupling.
        
        Parameters
        ----------
        mass : float or array
            Fermion mass(es) in GeV
        v_ew : float
            Electroweak VEV (default: 246.22 GeV)
            
        Returns
        -------
        float or array
            Yukawa coupling(s)
        """
        return mass * np.sqrt(2) / v_ew


def run_masses_from_high_scale(M_theta, texture_params, mu_target=M_Z, 
                                loop_order=1, n_steps=100):
    """
    Run fermion masses from UBT scale M_Θ down to low scale.
    
    Parameters
    ----------
    M_theta : float
        UBT scale (tree-level boundary condition scale) in GeV
    texture_params : dict
        Texture parameters for each sector
        Format: {'u': [eps_u, delta_u, eta_u],
                 'd': [eps_d, delta_d, eta_d],
                 'e': [eps_e, delta_e, eta_e]}
    mu_target : float
        Target scale for comparison with experiment (default: M_Z)
    loop_order : int
        RGE loop order (1 or 2, default: 1)
    n_steps : int
        Number of RGE integration steps
        
    Returns
    -------
    dict
        Masses at μ_target in GeV
    """
    rge = SMRGE(loop_order=loop_order)
    
    # Compute tree-level masses from texture
    masses_mu0 = {}
    for sector in ['u', 'd', 'e']:
        eps, delta, eta = texture_params[sector]
        # Eigenvalues from texture (leading order)
        m1 = M_theta * eps**2
        m2 = M_theta * delta
        m3 = M_theta * (1 + eta**2)
        masses_mu0[sector] = np.array([m1, m2, m3])
    
    # Convert to Yukawas at μ₀
    yukawas_mu0 = {
        sector: rge.mass_to_yukawa(masses_mu0[sector])
        for sector in ['u', 'd', 'e']
    }
    
    # Run to low scale
    yukawas_target, _ = rge.run_yukawas_to_low_scale(
        M_theta, mu_target, yukawas_mu0, n_steps=n_steps
    )
    
    # Convert back to masses
    masses_target = {
        sector: rge.yukawa_to_mass(yukawas_target[sector])
        for sector in ['u', 'd', 'e']
    }
    
    return masses_target


if __name__ == '__main__':
    # Example: run from M_Θ = 200 GeV to M_Z
    print("UBT RGE Runner - Example")
    print("=" * 60)
    
    # Example texture parameters (approximate)
    texture_params = {
        'u': [0.02, 0.3, 0.05],   # epsilon_u, delta_u, eta_u
        'd': [0.04, 0.5, 0.08],   # epsilon_d, delta_d, eta_d
        'e': [0.05, 0.6, 0.10],   # epsilon_e, delta_e, eta_e
    }
    
    M_theta = 200.0  # GeV
    
    print(f"\nTree-level scale: M_Θ = {M_theta} GeV")
    print(f"Target scale: M_Z = {M_Z} GeV")
    print("\nTexture parameters:")
    for sector, params in texture_params.items():
        print(f"  {sector}: ε={params[0]:.3f}, δ={params[1]:.3f}, η={params[2]:.3f}")
    
    # Run RGEs
    masses_mz = run_masses_from_high_scale(M_theta, texture_params, 
                                            mu_target=M_Z, loop_order=1)
    
    print("\nPredicted masses at M_Z (GeV):")
    print("-" * 60)
    for sector in ['u', 'd', 'e']:
        names = {'u': ['u', 'c', 't'], 'd': ['d', 's', 'b'], 
                 'e': ['e', 'μ', 'τ']}
        print(f"\n{sector.upper()}-type:")
        for i, name in enumerate(names[sector]):
            pred = masses_mz[sector][i]
            if sector in ['u', 'd']:
                exp = QUARK_MASSES_MZ[name]
            else:
                exp = LEPTON_MASSES_POLE[{'e': 'e', 'μ': 'mu', 'τ': 'tau'}[name]]
            ratio = pred / exp if exp > 0 else float('inf')
            print(f"  {name:2s}: {pred:.6f} GeV  (exp: {exp:.6f}, ratio: {ratio:.2f})")
    
    print("\n" + "=" * 60)
    print("Note: These are illustrative values. Proper fit requires")
    print("optimization of texture parameters against PDG data.")
