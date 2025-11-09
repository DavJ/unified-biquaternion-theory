# tests/test_alpha_provenance.py
import math

def test_alpha_fit_free_identity():
    # strict UBT alpha must be the same value the mass pipeline uses
    from alpha_core_repro.two_loop import alpha_from_ubt_two_loop_strict
    from ubt_masses.core import ubt_alpha_msbar

    mu = 0.511  # MeV-scale (electron)
    a_ref = alpha_from_ubt_two_loop_strict(mu=mu)
    a_m   = ubt_alpha_msbar(mu)
    assert math.isclose(a_ref, a_m, rel_tol=0.0, abs_tol=0.0), \
        "Mass pipeline must use strict UBT alpha (no mocks/fallbacks)"
