#!/usr/bin/env python3
"""Exact symbolic verifier for the split-jet right inverse."""
from __future__ import annotations
import sympy as sp


def symbolic_checks():
    eta = sp.diag(-1, 1, 1, 1)
    x = sp.Matrix(sp.symbols('x0:4'))
    z = sp.Matrix(sp.symbols('z0:4'))
    q = (x.T * eta * x)[0]
    xlo = eta * x
    w = sp.cancel((x.T * eta * z)[0] / q)
    zp = sp.simplify(z - w * x)
    zplo = eta * zp
    klo = sp.simplify((zplo * xlo.T - xlo * zplo.T) / q)
    kmix = eta * klo
    return {
        'K_antisymmetric': all(sp.simplify(v) == 0 for v in (klo + klo.T)),
        'Zperp_orthogonal': sp.simplify((x.T * eta * zp)[0]) == 0,
        'KX_equals_Zperp': all(sp.simplify(v) == 0 for v in (kmix * x - zp)),
        'full_decomposition': all(sp.simplify(v) == 0 for v in (kmix * x + w * x - z)),
    }


def exact_sample_checks():
    eta = sp.diag(-1,1,1,1)
    samples = [
        (sp.Matrix([2,1,0,0]), sp.Matrix([3,-2,5,1])),
        (sp.Matrix([1,0,0,2]), sp.Matrix([-1,4,2,3])),
        (sp.Matrix([3,1,-1,1]), sp.Matrix([2,0,7,-3])),
    ]
    ok=True
    for x,z in samples:
        q=(x.T*eta*x)[0]
        assert q != 0
        w=(x.T*eta*z)[0]/q
        zp=z-w*x
        klo=((eta*zp)*(eta*x).T-(eta*x)*(eta*zp).T)/q
        kmix=eta*klo
        ok = ok and kmix*x == zp and kmix*x+w*x == z
    return {'exact_nonnull_samples': ok}


def main():
    checks={**symbolic_checks(),**exact_sample_checks()}
    for k,v in checks.items(): print(f"[{'PASS' if v else 'FAIL'}] {k}")
    print('NOT TESTED: action selection, E[Theta] uniqueness, global null-patch continuation, or Newton coefficient')
    return 0 if all(checks.values()) else 1

if __name__=='__main__':
    raise SystemExit(main())
