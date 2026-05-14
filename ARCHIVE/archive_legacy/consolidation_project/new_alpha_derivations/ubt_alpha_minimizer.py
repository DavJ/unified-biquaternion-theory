# SPDX-License-Identifier: CC-BY-4.0
# Copyright (c) 2025 David Jaroš
# This file is part of the Unified Biquaternion Theory project.
# Licensed under Creative Commons Attribution 4.0 International License.

# UBT Noether->alpha: quick massless-model V_eff minimizer for θ_H
import math
from math import pi
import mpmath as mp
import numpy as np

def V_massless(L, theta_H, fields):
    coeff = -3.0 / (2.0 * math.pi**2 * L**5)
    v = mp.mpf('0')
    for f in fields:
        sigma = f['sigma']
        d = f['d']
        q = f['q']
        delta = f.get('delta', 0.0)
        theta_j = q * theta_H + 2.0 * math.pi * delta
        z = mp.e**(1j * theta_j)
        term = sigma * d * mp.re(mp.polylog(5, z))
        v += term
    return coeff * v

def dV_dtheta(L, theta_H, fields):
    coeff = -3.0 / (2.0 * math.pi**2 * L**5)
    dv = mp.mpf('0')
    for f in fields:
        sigma = f['sigma']
        d = f['d']
        q = f['q']
        delta = f.get('delta', 0.0)
        theta_j = q * theta_H + 2.0 * math.pi * delta
        z = mp.e**(1j * theta_j)
        dv_term = sigma * d * q * mp.re(1j * mp.polylog(4, z))
        dv += dv_term
    return coeff * dv

def find_stationary_points(L, fields, n_grid=721, tol=1e-10):
    thetas = np.linspace(0.0, 2.0 * math.pi, n_grid, endpoint=False)
    dvals = [float(dV_dtheta(L, float(t), fields)) for t in thetas]
    candidates = []
    for i in range(len(thetas)):
        t1 = thetas[i]
        t2 = thetas[(i + 1) % len(thetas)]
        f1 = dvals[i]
        f2 = dvals[(i + 1) % len(dvals)]
        if f1 == 0.0:
            candidates.append(t1)
        elif f1 * f2 < 0.0:
            try:
                root = mp.findroot(lambda th: dV_dtheta(L, th, fields), (t1, t2))
                root = float((root + 2.0 * math.pi) % (2.0 * math.pi))
                candidates.append(root)
            except:
                a, b = t1, t2
                for _ in range(60):
                    m = 0.5 * (a + b)
                    fm = float(dV_dtheta(L, m, fields))
                    if f1 * fm <= 0:
                        b = m; f2 = fm
                    else:
                        a = m; f1 = fm
                candidates.append(0.5 * (a + b))
    candidates = sorted(candidates)
    uniq = []
    for t in candidates:
        if not uniq or abs(t - uniq[-1]) > 1e-6:
            uniq.append(t)
    results = []
    eps = 1e-6
    for t in uniq:
        v = float(V_massless(L, t, fields))
        dv = float(dV_dtheta(L, t, fields))
        ddv = float((dV_dtheta(L, t + eps, fields) - dV_dtheta(L, t - eps, fields)) / (2 * eps))
        kind = 'min' if ddv > 0 else ('max' if ddv < 0 else 'flat')
        results.append({'theta_H': t, 'V': v, 'dV': dv, 'ddV': ddv, 'type': kind})
    return results

if __name__ == '__main__':
    fields = [
        {'sigma': +1, 'd': 1, 'q': 1, 'delta': 0.0},
        {'sigma': -1, 'd': 4, 'q': 1, 'delta': 0.5},
    ]
    L = 1.0
    res = find_stationary_points(L, fields)
    for r in res:
        print(r)
