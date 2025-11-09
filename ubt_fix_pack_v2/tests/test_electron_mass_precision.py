# tests/test_electron_mass_precision.py
import math

# adjust reference consistent with your scheme/source; this is a representative target
M_E_REF = 0.51099895  # MeV
TOL = 1e-4            # tighten to 1e-5 after adding 2-loop QED conversion

def test_electron_mass_precision():
    from ubt_masses.core import compute_lepton_msbar_mass, pole_from_msbar_lepton, ubt_alpha_msbar
    mbar = compute_lepton_msbar_mass("e", mu=None)  # μ = mbar (self-consistent)
    alpha_mu = ubt_alpha_msbar(mbar)
    m_pole = pole_from_msbar_lepton(mbar, mu=mbar, alpha_mu=alpha_mu)
    rel_err = abs(m_pole - M_E_REF) / M_E_REF
    assert rel_err < TOL, f"m_e off by {rel_err:.2e}; add 2-loop QED conversion to tighten"
