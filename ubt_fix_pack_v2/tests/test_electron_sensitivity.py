# tests/test_electron_sensitivity.py
def test_electron_mass_moves_with_alpha():
    # requires the small override hook in ubt_masses.core (set_alpha_override/clear_alpha_override)
    from ubt_masses.core import compute_lepton_msbar_mass, set_alpha_override, clear_alpha_override

    clear_alpha_override()
    m0 = compute_lepton_msbar_mass("e")

    # +1 ppm bump in alpha => mass must change (exposes hard-coded value if not)
    set_alpha_override(1.0 + 1e-6)
    m1 = compute_lepton_msbar_mass("e")
    clear_alpha_override()

    assert abs(m1 - m0) > 0.0, "Electron mass must depend on alpha; hard-coded constant suspected"
