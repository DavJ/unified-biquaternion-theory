#!/usr/bin/env python3
"""
UBT Data Analysis Suite - Cosmic Microwave Background
======================================================

This script analyzes Planck satellite CMB power spectrum data and compares
it with the UBT multiverse projection prediction from Appendix W.

UBT Prediction:
--------------
C_ℓ^UBT = C_ℓ^ΛCDM × [1 - A_MV × exp(-ℓ / ℓ_decohere)]

where:
  A_MV = 0.08 ± 0.03 (multiverse amplitude)
  ℓ_decohere = 35 ± 10 (decoherence scale)

This script:
1. Loads Planck 2018 power spectrum data (simulated in this example)
2. Compares observations with ΛCDM predictions
3. Fits UBT multiverse projection model
4. Assesses statistical significance

Author: UBT Research Team
Date: November 2025

Note: This script uses simulated data for demonstration. For actual analysis,
download real Planck data from: https://pla.esac.esa.int/
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2

# UBT Parameters (from Appendix W)
A_MV_PREDICTED = 0.08  # Multiverse amplitude
A_MV_ERROR = 0.03
L_DECOHERE_PREDICTED = 35  # Decoherence scale
L_DECOHERE_ERROR = 10

def ubt_suppression_factor(ell, A_MV, l_decohere):
    """
    Calculate UBT multiverse suppression factor.
    
    Parameters:
    -----------
    ell : array-like
        Multipole moment ℓ
    A_MV : float
        Multiverse amplitude (dimensionless)
    l_decohere : float
        Decoherence scale (multipole)
    
    Returns:
    --------
    factor : array-like
        Suppression factor [1 - A_MV × exp(-ℓ / ℓ_decohere)]
    """
    return 1.0 - A_MV * np.exp(-ell / l_decohere)

def generate_simulated_planck_data():
    """
    Generate simulated Planck-like CMB power spectrum data.
    
    In real analysis, this would be replaced with actual Planck data.
    
    Returns:
    --------
    ell : array
        Multipole moments
    Cl_obs : array
        Observed C_ℓ values (simulated)
    Cl_lcdm : array
        ΛCDM theoretical predictions
    sigma_Cl : array
        Uncertainties (cosmic variance + instrumental noise)
    """
    
    # Multipole range
    ell = np.arange(2, 101)  # Focus on large scales (ℓ < 100)
    
    # Simplified ΛCDM power spectrum (not realistic, just for demonstration)
    # Real analysis would use CAMB/CLASS output
    Cl_lcdm = 6000.0 * (ell / 10.0)**(-0.5) * np.exp(-ell / 800.0)
    
    # Add UBT suppression to create "observed" data
    # For demonstration, add suppression with slightly different parameters
    A_MV_sim = 0.10  # Slightly larger than predicted
    l_decohere_sim = 30  # Slightly smaller than predicted
    suppression = ubt_suppression_factor(ell, A_MV_sim, l_decohere_sim)
    
    # Cosmic variance uncertainty: σ(C_ℓ) ≈ C_ℓ × √[2/(2ℓ+1)]
    cosmic_variance = Cl_lcdm * np.sqrt(2.0 / (2.0 * ell + 1.0))
    
    # Add instrumental noise (simplified)
    instrumental_noise = 0.05 * Cl_lcdm  # 5% instrumental uncertainty
    
    # Total uncertainty
    sigma_Cl = np.sqrt(cosmic_variance**2 + instrumental_noise**2)
    
    # Generate "observed" data with noise
    np.random.seed(42)  # For reproducibility
    Cl_obs = Cl_lcdm * suppression + np.random.normal(0, sigma_Cl)
    
    return ell, Cl_obs, Cl_lcdm, sigma_Cl

def load_real_planck_data():
    """
    Load real Planck 2018 power spectrum data.
    
    In actual analysis, this would read from downloaded Planck data files:
    - COM_PowerSpect_CMB-TT-full_R3.01.txt
    - COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.00.txt
    
    For now, returns simulated data.
    """
    print("\n⚠️  NOTE: Using simulated data for demonstration.")
    print("   For real analysis, download Planck data from:")
    print("   https://pla.esac.esa.int/pla/\n")
    
    return generate_simulated_planck_data()

def fit_ubt_model(ell, Cl_obs, Cl_lcdm, sigma_Cl):
    """
    Fit UBT multiverse projection model to residuals.
    
    Parameters:
    -----------
    ell, Cl_obs, Cl_lcdm, sigma_Cl : arrays
        CMB power spectrum data
    
    Returns:
    --------
    params : tuple
        Fitted (A_MV, l_decohere)
    errors : tuple
        Parameter uncertainties
    """
    
    # Calculate residuals
    residuals = (Cl_obs - Cl_lcdm) / Cl_lcdm
    residual_errors = sigma_Cl / Cl_lcdm
    
    # Define model for residuals: -A_MV × exp(-ℓ / ℓ_decohere)
    def model(ell, A_MV, l_decohere):
        return -A_MV * np.exp(-ell / l_decohere)
    
    # Initial guess
    p0 = [A_MV_PREDICTED, L_DECOHERE_PREDICTED]
    
    # Fit model (weight by inverse variance)
    try:
        popt, pcov = curve_fit(model, ell, residuals, p0=p0, 
                               sigma=residual_errors, absolute_sigma=True,
                               bounds=([0, 5], [0.5, 100]))
        perr = np.sqrt(np.diag(pcov))
        return popt, perr
    except Exception as e:
        print(f"Fitting failed: {e}")
        return None, None

def plot_cmb_analysis(ell, Cl_obs, Cl_lcdm, sigma_Cl, fit_params=None):
    """
    Create comprehensive CMB analysis plots.
    """
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    
    # --- Top Panel: Power Spectrum ---
    ax1 = axes[0]
    
    # Plot ΛCDM prediction
    ax1.plot(ell, Cl_lcdm, 'k-', linewidth=2, label='ΛCDM Best-Fit', alpha=0.7)
    
    # Plot UBT prediction if fit succeeded
    if fit_params is not None:
        A_MV_fit, l_decohere_fit = fit_params
        Cl_ubt = Cl_lcdm * ubt_suppression_factor(ell, A_MV_fit, l_decohere_fit)
        ax1.plot(ell, Cl_ubt, 'r--', linewidth=2, 
                label=f'UBT Fit: A_MV={A_MV_fit:.3f}, ℓ_d={l_decohere_fit:.1f}')
    
    # Plot with predicted UBT parameters
    Cl_ubt_predicted = Cl_lcdm * ubt_suppression_factor(ell, A_MV_PREDICTED, L_DECOHERE_PREDICTED)
    ax1.plot(ell, Cl_ubt_predicted, 'r:', linewidth=2, 
            label=f'UBT Prediction: A_MV={A_MV_PREDICTED}, ℓ_d={L_DECOHERE_PREDICTED}')
    
    # Plot observed data with error bars
    ax1.errorbar(ell, Cl_obs, yerr=sigma_Cl, fmt='bo', markersize=4, 
                alpha=0.6, label='Planck 2018 (simulated)')
    
    ax1.set_xlabel('Multipole ℓ', fontsize=12)
    ax1.set_ylabel('C_ℓ [μK²]', fontsize=12)
    ax1.set_title('CMB Temperature Power Spectrum: UBT vs ΛCDM', 
                 fontsize=14, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 105)
    
    # --- Bottom Panel: Residuals ---
    ax2 = axes[1]
    
    residuals = (Cl_obs - Cl_lcdm) / Cl_lcdm
    residual_errors = sigma_Cl / Cl_lcdm
    
    # Plot residuals
    ax2.errorbar(ell, residuals, yerr=residual_errors, fmt='bo', 
                markersize=4, alpha=0.6, label='(Data - ΛCDM) / ΛCDM')
    
    # Plot UBT prediction
    ubt_residuals_predicted = -A_MV_PREDICTED * np.exp(-ell / L_DECOHERE_PREDICTED)
    ax2.plot(ell, ubt_residuals_predicted, 'r:', linewidth=2, 
            label='UBT Prediction')
    
    # Plot fit if available
    if fit_params is not None:
        A_MV_fit, l_decohere_fit = fit_params
        ubt_residuals_fit = -A_MV_fit * np.exp(-ell / l_decohere_fit)
        ax2.plot(ell, ubt_residuals_fit, 'r--', linewidth=2, label='UBT Fit')
    
    # Add zero line
    ax2.axhline(0, color='k', linestyle='-', linewidth=1, alpha=0.5)
    
    # Add ±1σ cosmic variance bands
    cosmic_var = np.sqrt(2.0 / (2.0 * ell + 1.0))
    ax2.fill_between(ell, -cosmic_var, cosmic_var, alpha=0.2, color='gray', 
                     label='±1σ Cosmic Variance')
    
    ax2.set_xlabel('Multipole ℓ', fontsize=12)
    ax2.set_ylabel('Fractional Residual', fontsize=12)
    ax2.set_title('Residuals: Testing UBT Multiverse Projection', 
                 fontsize=14, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 105)
    ax2.set_ylim(-0.4, 0.2)
    
    plt.tight_layout()
    plt.savefig('ubt_cmb_analysis.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as: ubt_cmb_analysis.png")
    
    return fig, axes

def calculate_chi_squared(ell, Cl_obs, Cl_model, sigma_Cl):
    """
    Calculate χ² goodness-of-fit statistic.
    """
    chi_sq = np.sum(((Cl_obs - Cl_model) / sigma_Cl)**2)
    dof = len(ell) - 2  # Degrees of freedom (N_data - N_params)
    p_value = 1 - chi2.cdf(chi_sq, dof)
    return chi_sq, dof, p_value

def statistical_analysis(ell, Cl_obs, Cl_lcdm, sigma_Cl, fit_params):
    """
    Perform statistical analysis of UBT vs ΛCDM models.
    """
    
    print("\n" + "="*70)
    print("STATISTICAL ANALYSIS")
    print("="*70 + "\n")
    
    # ΛCDM model
    chi_sq_lcdm, dof_lcdm, p_lcdm = calculate_chi_squared(ell, Cl_obs, Cl_lcdm, sigma_Cl)
    
    print("ΛCDM Model:")
    print(f"  χ² = {chi_sq_lcdm:.2f}")
    print(f"  DoF = {dof_lcdm}")
    print(f"  χ²/DoF = {chi_sq_lcdm/dof_lcdm:.3f}")
    print(f"  p-value = {p_lcdm:.4f}")
    
    if fit_params is not None:
        A_MV_fit, l_decohere_fit = fit_params
        Cl_ubt = Cl_lcdm * ubt_suppression_factor(ell, A_MV_fit, l_decohere_fit)
        chi_sq_ubt, dof_ubt, p_ubt = calculate_chi_squared(ell, Cl_obs, Cl_ubt, sigma_Cl)
        
        print("\nUBT Model (fitted):")
        print(f"  A_MV = {A_MV_fit:.3f}")
        print(f"  ℓ_decohere = {l_decohere_fit:.1f}")
        print(f"  χ² = {chi_sq_ubt:.2f}")
        print(f"  DoF = {dof_ubt}")
        print(f"  χ²/DoF = {chi_sq_ubt/dof_ubt:.3f}")
        print(f"  p-value = {p_ubt:.4f}")
        
        # Model comparison
        delta_chi_sq = chi_sq_lcdm - chi_sq_ubt
        print(f"\nModel Comparison:")
        print(f"  Δχ² (ΛCDM - UBT) = {delta_chi_sq:.2f}")
        if delta_chi_sq > 6:
            print(f"  → UBT provides SIGNIFICANTLY better fit (>2σ)")
        elif delta_chi_sq > 0:
            print(f"  → UBT provides marginally better fit")
        else:
            print(f"  → ΛCDM provides better fit")
        
        # Compare with predicted values
        print(f"\nComparison with UBT Prediction:")
        print(f"  Predicted A_MV: {A_MV_PREDICTED} ± {A_MV_ERROR}")
        print(f"  Fitted A_MV: {A_MV_fit:.3f}")
        A_MV_sigma = abs(A_MV_fit - A_MV_PREDICTED) / A_MV_ERROR
        print(f"  Discrepancy: {A_MV_sigma:.1f}σ")
        
        print(f"\n  Predicted ℓ_decohere: {L_DECOHERE_PREDICTED} ± {L_DECOHERE_ERROR}")
        print(f"  Fitted ℓ_decohere: {l_decohere_fit:.1f}")
        l_sigma = abs(l_decohere_fit - L_DECOHERE_PREDICTED) / L_DECOHERE_ERROR
        print(f"  Discrepancy: {l_sigma:.1f}σ")
    
    print("\n" + "="*70 + "\n")

def analyze_low_multipoles(ell, Cl_obs, Cl_lcdm, sigma_Cl):
    """
    Focus on low-ℓ anomalies (ℓ < 30).
    """
    
    print("\n" + "="*70)
    print("LOW-ℓ ANOMALY ANALYSIS (ℓ < 30)")
    print("="*70 + "\n")
    
    # Select low-ℓ range
    mask = ell < 30
    ell_low = ell[mask]
    Cl_obs_low = Cl_obs[mask]
    Cl_lcdm_low = Cl_lcdm[mask]
    
    # Calculate power deficit
    print(f"{'ℓ':<6} {'C_ℓ (obs)':<15} {'C_ℓ (ΛCDM)':<15} {'Deficit (%)':<15}")
    print("-" * 60)
    
    for i in range(len(ell_low)):
        deficit = 100 * (1 - Cl_obs_low[i] / Cl_lcdm_low[i])
        print(f"{ell_low[i]:<6} {Cl_obs_low[i]:<15.1f} {Cl_lcdm_low[i]:<15.1f} {deficit:<15.1f}")
    
    # Average deficit
    avg_deficit = 100 * np.mean(1 - Cl_obs_low / Cl_lcdm_low)
    print(f"\nAverage power deficit (ℓ < 30): {avg_deficit:.1f}%")
    print(f"UBT prediction (A_MV = 0.08): ~6-8% deficit at ℓ < 30")
    
    if abs(avg_deficit) > 10:
        print("\n⚠️  Observed deficit LARGER than UBT prediction")
        print("   → UBT provides partial explanation, but not complete")
    elif abs(avg_deficit) > 3:
        print("\n✅ Observed deficit consistent with UBT prediction")
    else:
        print("\n❌ Observed deficit SMALLER than UBT prediction")
        print("   → Data does not support UBT multiverse suppression")
    
    print("\n" + "="*70 + "\n")

def main():
    """
    Main CMB analysis routine.
    """
    
    print("\n" + "="*70)
    print("UBT COSMIC MICROWAVE BACKGROUND ANALYSIS")
    print("Testing Multiverse Projection Signature")
    print("="*70 + "\n")
    
    # Load data (simulated for now)
    ell, Cl_obs, Cl_lcdm, sigma_Cl = load_real_planck_data()
    
    print(f"Loaded CMB power spectrum data:")
    print(f"  Multipole range: ℓ = {ell.min()} to {ell.max()}")
    print(f"  Number of data points: {len(ell)}")
    
    # Fit UBT model
    print("\nFitting UBT multiverse projection model...")
    fit_params, fit_errors = fit_ubt_model(ell, Cl_obs, Cl_lcdm, sigma_Cl)
    
    if fit_params is not None:
        print(f"  A_MV = {fit_params[0]:.3f} ± {fit_errors[0]:.3f}")
        print(f"  ℓ_decohere = {fit_params[1]:.1f} ± {fit_errors[1]:.1f}")
    
    # Generate plots
    print("\nGenerating analysis plots...")
    plot_cmb_analysis(ell, Cl_obs, Cl_lcdm, sigma_Cl, fit_params)
    
    # Statistical analysis
    if fit_params is not None:
        statistical_analysis(ell, Cl_obs, Cl_lcdm, sigma_Cl, fit_params)
    
    # Low-multipole analysis
    analyze_low_multipoles(ell, Cl_obs, Cl_lcdm, sigma_Cl)
    
    print("\n" + "="*70)
    print("CONCLUSIONS")
    print("="*70)
    print("\n⚠️  This analysis used SIMULATED data for demonstration.")
    print("\nFor real analysis, you need:")
    print("  1. Download Planck 2018 power spectrum data")
    print("  2. Use proper likelihood code (PlanckLikelihood)")
    print("  3. Account for all systematic uncertainties")
    print("  4. Consider foreground contamination at low-ℓ")
    print("  5. Properly handle cosmic variance covariance")
    print("\nWith real data, this analysis can definitively test")
    print("the UBT multiverse projection prediction.")
    print("="*70 + "\n")
    
    print("Analysis complete!")
    print("Output: ubt_cmb_analysis.png\n")

if __name__ == "__main__":
    main()
