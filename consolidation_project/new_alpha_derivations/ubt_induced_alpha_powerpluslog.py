# SPDX-License-Identifier: CC-BY-4.0
# Copyright (c) 2025 David Jaroš
# This file is part of the Unified Biquaternion Theory project.
# Licensed under Creative Commons Attribution 4.0 International License.

# UBT: Induced alpha from 5D power-law + 4D KK logs with heat-kernel C5 coefficients
import math, json
from pathlib import Path
import numpy as np
import mpmath as mp

pi = math.pi

# Default C5 values from Appendix C (to be checked for conventions)
C5_scalar_default = 1.0 / (6.0 * (4.0*pi)**2.5)
C5_dirac_default  = 1.0 / (3.0 * (4.0*pi)**2.5)

def kk_masses(L, theta_H, q, delta, m0, cutoff):
    masses = []
    nmax = int(math.ceil(cutoff * L / (2*pi))) + 5
    a = q * theta_H / (2*pi) + delta
    for n in range(-nmax, nmax+1):
        ppsi = (2*pi / L) * (n + a)
        m = math.sqrt(m0**2 + ppsi**2)
        if m <= cutoff and m > 0:
            masses.append(m)
    return masses

def alpha_induced_with_C5(L, theta_H, fields, cutoff, Z, C5_scalar=C5_scalar_default, C5_dirac=C5_dirac_default):
    # Compute induced 1/alpha at scale ~cutoff from 5D power-law term + 4D KK logs
    # fields: list of dicts with keys {kind, q, delta, m0, mult}
    # Returns a dict with inv_alpha_total, alpha_total and breakdown.
    inv_alpha_logs = 0.0
    detail = []
    Q2_dirac = 0.0
    Q2_scalar = 0.0

    for f in fields:
        masses = kk_masses(L, theta_H, f['q'], f.get('delta', 0.0), f.get('m0', 0.0), cutoff)
        coeff = (2.0 / (3.0 * pi) if f['kind']=='dirac' else 1.0 / (6.0 * pi)) * (f['q']**2)
        mult = f.get('mult', 1)
        sum_logs = sum(math.log(cutoff / m) for m in masses if m > 0)
        inv_alpha_logs += mult * coeff * sum_logs
        if f['kind']=='dirac':
            Q2_dirac += mult * (f['q']**2)
        else:
            Q2_scalar += mult * (f['q']**2)
        detail.append({'field': f, 'n_modes': len(masses), 'sum_logs': sum_logs, 'coeff_per_mode': coeff})

    # 5D power-law
    power_term = Z * cutoff * (C5_dirac * Q2_dirac + C5_scalar * Q2_scalar)
    inv_alpha_total = power_term + inv_alpha_logs
    alpha_total = 1.0 / inv_alpha_total if inv_alpha_total > 0 else None

    return {
        'inv_alpha_total': inv_alpha_total,
        'alpha_total': alpha_total,
        'inv_alpha_logs': inv_alpha_logs,
        'power_term': power_term,
        'Q2_dirac': Q2_dirac,
        'Q2_scalar': Q2_scalar,
        'C5_dirac': C5_dirac,
        'C5_scalar': C5_scalar,
        'Z': Z,
        'cutoff': cutoff,
        'L': L,
        'theta_H': theta_H,
        'detail': detail
    }

if __name__ == '__main__':
    # Example usage with placeholders
    L = 1.2
    theta_H = 0.0
    Z = L  # flat zero-mode
    cutoff = 5.0 / L

    fields = [
        {'kind': 'dirac',  'q': 1.0, 'delta': 0.5, 'm0': 0.20, 'mult': 1},
        {'kind': 'scalar', 'q': 1.0, 'delta': 0.0, 'm0': 0.35, 'mult': 1},
        {'kind': 'scalar', 'q': 1.0, 'delta': 0.0, 'm0': 1.00, 'mult': 1},
    ]

    res = alpha_induced_with_C5(L, theta_H, fields, cutoff, Z)
    print(json.dumps(res, indent=2))
