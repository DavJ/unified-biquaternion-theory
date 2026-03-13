# ubt_masses/qed.py
# SPDX-License-Identifier: MIT
"""
QED Pole Mass Conversion
=========================

Conversion between MSbar and pole mass for leptons.
Uses standard QED perturbation theory.
"""
from __future__ import annotations
import math


def pole_from_msbar_lepton(m_msbar: float, mu: float, alpha_mu: float) -> float:
    """
    Convert MSbar mass to pole mass for leptons using QED self-energy.
    
    At 1-loop in QED, the on-shell (pole) mass relates to MSbar mass via:
    
        m_pole = m̄(μ) * [1 + (α/π) * (1 + (3/4) * ln(μ²/m̄²)) + O(α²)]
    
    When μ = m̄ (our default choice), the logarithm vanishes and:
    
        m_pole ≈ m̄ * [1 + α/π + O(α²)]
    
    This is the 1-loop QED self-energy correction in dimensional regularization
    with MSbar subtraction scheme.
    
    Args:
        m_msbar: MSbar mass m̄_ℓ(μ) in MeV
        mu: Renormalization scale μ in MeV
        alpha_mu: Fine structure constant α(μ) at scale μ
    
    Returns:
        Pole mass m_ℓ^pole in MeV
    
    Raises:
        ValueError: If inputs are non-positive
    
    References:
        - Chetyrkin & Steinhauser, Nucl. Phys. B 573 (2000) 617
        - Melnikov & Ritbergen, Phys. Lett. B 482 (2000) 99
    
    TODO: Implement 2-loop QED correction for target precision < 10⁻⁵:
        m_pole = m̄ * [1 + (α/π) + (α/π)² * C₂ + ...]
        where C₂ includes π² terms and higher-order logs
    """
    if mu <= 0 or m_msbar <= 0:
        raise ValueError(
            f"μ and m̄ must be positive. Got μ={mu}, m̄={m_msbar}"
        )
    
    if alpha_mu <= 0 or alpha_mu >= 1:
        raise ValueError(
            f"α(μ) must be in (0, 1). Got α={alpha_mu}"
        )
    
    # Logarithmic term: ln(μ²/m̄²)
    log_term = math.log((mu * mu) / (m_msbar * m_msbar))
    
    # 1-loop QED correction
    # The (3/4) coefficient comes from the fermion self-energy diagram
    # in dimensional regularization with MSbar scheme
    delta_1loop = (alpha_mu / math.pi) * (1.0 + 0.75 * log_term)
    
    # Pole mass
    m_pole = m_msbar * (1.0 + delta_1loop)
    
    return m_pole


def msbar_from_pole_lepton(m_pole: float, mu: float, alpha_mu: float) -> float:
    """
    Convert pole mass to MSbar mass for leptons (inverse of pole_from_msbar_lepton).
    
    This is obtained by inverting the 1-loop relation to O(α):
    
        m̄(μ) ≈ m_pole / [1 + (α/π) * (1 + (3/4) * ln(μ²/m̄²))]
        
    For μ = m̄, this simplifies to:
    
        m̄ ≈ m_pole * [1 - α/π + O(α²)]
    
    Args:
        m_pole: Pole mass in MeV
        mu: Renormalization scale μ in MeV
        alpha_mu: Fine structure constant α(μ) at scale μ
    
    Returns:
        MSbar mass m̄_ℓ(μ) in MeV
    
    Raises:
        ValueError: If inputs are non-positive
    
    Note: This is an approximate inversion valid to O(α). For higher precision,
          use iterative solution or 2-loop formula.
    """
    if mu <= 0 or m_pole <= 0:
        raise ValueError(
            f"μ and m_pole must be positive. Got μ={mu}, m_pole={m_pole}"
        )
    
    if alpha_mu <= 0 or alpha_mu >= 1:
        raise ValueError(
            f"α(μ) must be in (0, 1). Got α={alpha_mu}"
        )
    
    # For iterative solution, start with approximate formula
    # m̄ ≈ m_pole * [1 - α/π]
    mbar_approx = m_pole * (1.0 - alpha_mu / math.pi)
    
    # Refine with one iteration using the forward formula
    # This accounts for the log term properly
    log_term = math.log((mu * mu) / (mbar_approx * mbar_approx))
    delta_1loop = (alpha_mu / math.pi) * (1.0 + 0.75 * log_term)
    
    # Improved estimate: m̄ = m_pole / (1 + δ)
    mbar_refined = m_pole / (1.0 + delta_1loop)
    
    return mbar_refined
