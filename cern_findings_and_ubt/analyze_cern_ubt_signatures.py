#!/usr/bin/env python3
"""
UBT Signature Analysis for CERN/LHC Data

This script provides tools to analyze LHC data for signatures predicted by
Unified Biquaternion Theory (UBT), including:
1. Quantized mass spectrum (M = n × m_e)
2. Semi-visible jet characteristics
3. SUEP multiplicity patterns
4. Dark photon resonance searches

Author: David Jaroš
Date: November 5, 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from typing import Dict

# Physical constants
M_ELECTRON = 0.511  # MeV/c²
HBAR_C = 197.327  # MeV·fm
ALPHA = 1.0 / 137.036  # Fine structure constant

# UBT-specific parameters
CHARACTERISTIC_SCALE_FM2 = 1.0  # Natural scale for imaginary-time suppression (fm²)


class UBTSignatureAnalyzer:
    """Analyzer for UBT-specific signatures in particle physics data."""
    
    def __init__(self, r_psi: float = 2.43e-15):
        """
        Initialize UBT analyzer.
        
        Parameters
        ----------
        r_psi : float
            Imaginary time compactification radius in meters.
            Default: Compton wavelength ℏ/(m_e c) ≈ 2.43 fm
        """
        self.r_psi = r_psi  # meters
        self.r_psi_fm = r_psi * 1e15  # femtometers
        
    def ubt_mass_spectrum(self, n_max: int = 100) -> np.ndarray:
        """
        Generate UBT predicted mass spectrum.
        
        M_n = n × m_e (first-order approximation)
        
        Parameters
        ----------
        n_max : int
            Maximum winding number
            
        Returns
        -------
        masses : ndarray
            Array of predicted masses in MeV
        """
        n = np.arange(1, n_max + 1)
        masses = n * M_ELECTRON
        return masses
    
    def check_mass_quantization(self, 
                                measured_masses: np.ndarray,
                                uncertainties: np.ndarray,
                                tolerance: float = 3.0) -> Dict:
        """
        Check if measured masses are consistent with UBT quantization M = n × m_e.
        
        Parameters
        ----------
        measured_masses : ndarray
            Measured particle masses in MeV
        uncertainties : ndarray
            Measurement uncertainties in MeV
        tolerance : float
            Number of sigma for consistency check
            
        Returns
        -------
        results : dict
            Dictionary with analysis results including:
            - 'consistent': list of masses consistent with quantization
            - 'winding_numbers': corresponding n values
            - 'chi_squared': chi-squared statistic
            - 'p_value': statistical significance
        """
        results = {
            'consistent': [],
            'winding_numbers': [],
            'residuals': [],
            'significance': []
        }
        
        for i, (mass, unc) in enumerate(zip(measured_masses, uncertainties)):
            # Find nearest integer multiple of m_e
            n_best = np.round(mass / M_ELECTRON)
            m_predicted = n_best * M_ELECTRON
            
            # Calculate residual and significance
            residual = mass - m_predicted
            significance = abs(residual) / unc
            
            # Check consistency
            if significance < tolerance:
                results['consistent'].append(mass)
                results['winding_numbers'].append(int(n_best))
            
            results['residuals'].append(residual)
            results['significance'].append(significance)
        
        # Calculate overall chi-squared
        residuals = np.array(results['residuals'])
        chi_squared = np.sum((residuals / uncertainties)**2)
        dof = len(measured_masses) - 1
        results['chi_squared'] = chi_squared
        results['dof'] = dof
        results['p_value'] = 1.0 - stats.chi2.cdf(chi_squared, dof)
        
        return results
    
    def semi_visible_fraction(self, 
                              delta_m: float, 
                              T_dark: float = 1000.0) -> float:
        """
        Calculate visible fraction in semi-visible jets.
        
        From UBT: f_vis = 1 / (1 + exp(Δm/T_dark))
        
        Parameters
        ----------
        delta_m : float
            Mass difference between dark and SM hadrons (MeV)
        T_dark : float
            Dark sector temperature (MeV), default ~1 GeV
            
        Returns
        -------
        f_visible : float
            Fraction of visible energy (0 to 1)
        """
        f_visible = 1.0 / (1.0 + np.exp(delta_m / T_dark))
        return f_visible
    
    def suep_multiplicity(self, 
                         E_collision: float, 
                         Lambda_dark: float = 1000.0) -> float:
        """
        Predict track multiplicity in SUEP events.
        
        From UBT: N = (E / Λ_dark) × correction_factor
        
        Parameters
        ----------
        E_collision : float
            Collision energy in MeV
        Lambda_dark : float
            Dark confinement scale in MeV (default ~1 GeV)
            
        Returns
        -------
        N_tracks : float
            Expected number of tracks
        """
        # Base multiplicity from energy
        N_base = E_collision / Lambda_dark
        
        # UBT correction from imaginary-time suppression
        correction = np.exp(-self.r_psi_fm**2 / CHARACTERISTIC_SCALE_FM2)
        
        N_tracks = N_base * correction
        return N_tracks
    
    def dark_photon_mass_prediction(self, 
                                     n: int, 
                                     Q_H: int = 1) -> float:
        """
        Predict dark photon mass from UBT.
        
        M = n × m_e × exp(-α × |Q_H|^(3/4))
        
        Parameters
        ----------
        n : int
            Winding number around imaginary time circle
        Q_H : int
            Hopf topological charge
            
        Returns
        -------
        mass : float
            Predicted mass in MeV
        """
        hopf_suppression = np.exp(-ALPHA * abs(Q_H)**(3.0/4.0))
        mass = n * M_ELECTRON * hopf_suppression
        return mass
    
    def plot_mass_spectrum_comparison(self, 
                                     measured_masses: np.ndarray,
                                     uncertainties: np.ndarray,
                                     n_max: int = 100,
                                     filename: str = None):
        """
        Plot comparison between UBT predictions and measurements.
        
        Parameters
        ----------
        measured_masses : ndarray
            Measured masses in MeV
        uncertainties : ndarray
            Measurement uncertainties in MeV
        n_max : int
            Maximum winding number to plot
        filename : str, optional
            If provided, save plot to this file
        """
        # Generate UBT predictions
        ubt_masses = self.ubt_mass_spectrum(n_max)
        
        # Create figure
        _, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Top panel: Full spectrum
        ax1.scatter(measured_masses, 
                   np.ones_like(measured_masses), 
                   c='red', s=100, marker='o', 
                   label='Measured masses', zorder=5)
        ax1.errorbar(measured_masses, 
                    np.ones_like(measured_masses),
                    xerr=uncertainties, 
                    fmt='none', ecolor='red', alpha=0.5)
        
        # Plot UBT predictions as vertical lines
        for i, mass in enumerate(ubt_masses[:20]):  # First 20 for clarity
            ax1.axvline(mass, color='blue', alpha=0.3, linewidth=1)
            if i % 5 == 0:
                ax1.text(mass, 0.95, f'n={i+1}', 
                        rotation=90, va='top', fontsize=8)
        
        ax1.set_xlabel('Mass (MeV)', fontsize=12)
        ax1.set_ylabel('Arbitrary units', fontsize=12)
        ax1.set_title('UBT Mass Quantization: M = n × m_e', fontsize=14, fontweight='bold')
        ax1.set_ylim([0.8, 1.2])
        ax1.legend(fontsize=10)
        ax1.grid(True, alpha=0.3)
        
        # Bottom panel: Residuals
        results = self.check_mass_quantization(measured_masses, uncertainties)
        residuals = np.array(results['residuals'])
        significance = np.array(results['significance'])
        
        colors = ['green' if s < 3 else 'orange' if s < 5 else 'red' 
                 for s in significance]
        
        ax2.scatter(measured_masses, residuals, c=colors, s=100, marker='o')
        ax2.errorbar(measured_masses, residuals, yerr=uncertainties,
                    fmt='none', ecolor='gray', alpha=0.5)
        ax2.axhline(0, color='blue', linestyle='--', linewidth=2, label='UBT prediction')
        ax2.axhline(3*uncertainties.mean(), color='red', linestyle=':', 
                   label='3σ boundary')
        ax2.axhline(-3*uncertainties.mean(), color='red', linestyle=':')
        
        ax2.set_xlabel('Mass (MeV)', fontsize=12)
        ax2.set_ylabel('Residual: M_measured - n×m_e (MeV)', fontsize=12)
        ax2.set_title('Residuals from UBT Quantization', fontsize=14)
        ax2.legend(fontsize=10)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if filename:
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {filename}")
        else:
            plt.show()
    
    def analyze_suep_event(self, 
                          tracks: np.ndarray,
                          pt_threshold: float = 1.0) -> Dict:
        """
        Analyze a SUEP candidate event.
        
        Parameters
        ----------
        tracks : ndarray
            Array of track transverse momenta (GeV)
        pt_threshold : float
            Minimum pT for track counting (GeV)
            
        Returns
        -------
        analysis : dict
            Dictionary with event characteristics
        """
        # Filter tracks above threshold
        valid_tracks = tracks[tracks > pt_threshold]
        
        # Handle empty track array
        if len(valid_tracks) == 0:
            return {
                'n_tracks': 0,
                'mean_pt': 0.0,
                'median_pt': 0.0,
                'total_pt': 0.0,
                'pt_std': 0.0,
                'sphericity': 0.0,
                'is_suep_candidate': False
            }
        
        analysis = {
            'n_tracks': len(valid_tracks),
            'mean_pt': np.mean(valid_tracks),
            'median_pt': np.median(valid_tracks),
            'total_pt': np.sum(valid_tracks),
            'pt_std': np.std(valid_tracks),
            'sphericity': self._calculate_sphericity(tracks)
        }
        
        # Check if consistent with SUEP
        is_suep = (analysis['n_tracks'] > 50 and 
                  analysis['mean_pt'] < 10.0 and  # Soft
                  analysis['sphericity'] > 0.7)  # Isotropic
        
        analysis['is_suep_candidate'] = is_suep
        
        return analysis
    
    def _calculate_sphericity(self, tracks: np.ndarray) -> float:
        """
        Calculate event sphericity (simplified 1D version).
        
        Parameters
        ----------
        tracks : ndarray
            Track momenta
            
        Returns
        -------
        sphericity : float
            Sphericity measure (0 = jet-like, 1 = spherical)
        """
        if len(tracks) < 2:
            return 0.0
        
        # Simplified: use variance as proxy
        normalized_variance = np.std(tracks) / (np.mean(tracks) + 1e-10)
        sphericity = 1.0 / (1.0 + normalized_variance)
        
        return sphericity


def demonstration():
    """Demonstrate UBT signature analysis."""
    
    print("=" * 70)
    print("UBT Signature Analysis for CERN/LHC Data")
    print("=" * 70)
    print()
    
    # Initialize analyzer
    analyzer = UBTSignatureAnalyzer()
    
    # Example 1: Check mass quantization
    print("Example 1: Mass Quantization Check")
    print("-" * 70)
    
    # Simulate some "measured" masses (for demonstration)
    # In reality, these would come from LHC data
    true_n = np.array([100, 250, 500, 1000, 2000, 5000, 10000])
    measured_masses = true_n * M_ELECTRON + np.random.normal(0, 5, len(true_n))
    uncertainties = np.ones_like(measured_masses) * 5.0
    
    results = analyzer.check_mass_quantization(measured_masses, uncertainties)
    
    print(f"Number of consistent masses: {len(results['consistent'])}")
    print(f"Chi-squared: {results['chi_squared']:.2f}")
    print(f"Degrees of freedom: {results['dof']}")
    print(f"P-value: {results['p_value']:.4f}")
    print()
    
    for i, (mass, n, sig) in enumerate(zip(results['consistent'], 
                                           results['winding_numbers'],
                                           results['significance'][:len(results['consistent'])])):
        print(f"  Mass {mass:.2f} MeV → n = {n}, significance = {sig:.2f}σ")
    print()
    
    # Example 2: Semi-visible jet fraction
    print("Example 2: Semi-Visible Jet Predictions")
    print("-" * 70)
    
    delta_masses = np.array([0, 100, 500, 1000, 2000])  # MeV
    for dm in delta_masses:
        f_vis = analyzer.semi_visible_fraction(dm)
        print(f"  Δm = {dm:4d} MeV → Visible fraction: {f_vis:.3f}")
    print()
    
    # Example 3: SUEP multiplicity
    print("Example 3: SUEP Track Multiplicity")
    print("-" * 70)
    
    collision_energies = np.array([500, 1000, 2000, 5000, 10000])  # GeV
    for E in collision_energies:
        N = analyzer.suep_multiplicity(E * 1000)  # Convert to MeV
        print(f"  E = {E:5d} GeV → Expected tracks: {N:.1f}")
    print()
    
    # Example 4: Dark photon masses
    print("Example 4: Dark Photon Mass Predictions")
    print("-" * 70)
    
    winding_numbers = [1, 10, 100, 1000, 10000, 100000, 1000000]
    for n in winding_numbers:
        mass = analyzer.dark_photon_mass_prediction(n)
        if mass < 1000:
            print(f"  n = {n:7d} → M = {mass:.3f} MeV")
        else:
            print(f"  n = {n:7d} → M = {mass/1000:.3f} GeV")
    print()
    
    # Example 5: Create visualization
    print("Example 5: Creating Mass Spectrum Visualization")
    print("-" * 70)
    
    try:
        analyzer.plot_mass_spectrum_comparison(
            measured_masses, 
            uncertainties,
            n_max=50,
            filename='ubt_mass_spectrum_analysis.png'
        )
        print("  ✓ Visualization created successfully")
    except Exception as e:
        print(f"  ⚠ Could not create plot: {e}")
    print()
    
    # Example 6: SUEP event analysis
    print("Example 6: SUEP Event Analysis")
    print("-" * 70)
    
    # Simulate a SUEP-like event
    suep_tracks = np.random.exponential(3.0, 150)  # Soft pT distribution
    normal_tracks = np.random.exponential(20.0, 30)  # Normal event
    
    for label, tracks in [("SUEP candidate", suep_tracks), 
                          ("Normal event", normal_tracks)]:
        analysis = analyzer.analyze_suep_event(tracks)
        print(f"\n  {label}:")
        print(f"    Tracks: {analysis['n_tracks']}")
        print(f"    Mean pT: {analysis['mean_pt']:.2f} GeV")
        print(f"    Median pT: {analysis['median_pt']:.2f} GeV")
        print(f"    Sphericity: {analysis['sphericity']:.3f}")
        print(f"    SUEP candidate: {'YES' if analysis['is_suep_candidate'] else 'NO'}")
    print()
    
    print("=" * 70)
    print("Analysis complete!")
    print("=" * 70)


if __name__ == "__main__":
    demonstration()
