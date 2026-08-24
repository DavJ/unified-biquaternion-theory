from tools.verify_theta_potential_stability import D, H, witnesses
from fractions import Fraction


def test_exact_witness_rays():
    t = Fraction(3)
    nilpotent, phase_diag, identity, flat = witnesses(t)
    assert H(*nilpotent) == -t * t
    assert D(*nilpotent) == 0
    assert H(*phase_diag) == 0
    assert D(*phase_diag) == t**4
    assert H(*identity) == 2 * t * t
    assert D(*identity) == t**4
    assert H(*flat) == 0
    assert D(*flat) == 0


def test_flat_direction_is_noncompact():
    for t in map(Fraction, [0, 1, 2, 5, 11]):
        flat = witnesses(t)[3]
        assert H(*flat) == 0
        assert D(*flat) == 0
