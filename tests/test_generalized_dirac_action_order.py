from tools.verify_generalized_dirac_action_order import (
    verify_factorisation_counterexample,
    verify_kronecker_principal_hessian,
    verify_scalar_velocity_hessian,
)


def test_scalar_velocity_hessian():
    verify_scalar_velocity_hessian()


def test_factorisation_counterexample():
    verify_factorisation_counterexample()


def test_kronecker_principal_hessian():
    verify_kronecker_principal_hessian()
