#!/usr/bin/env python3
"""Numerical probes for the 2026-08-19 theta/Mellin/zeta/revival working note.

This script verifies standard identities used by the UBT bridge note.  Passing it
is not evidence for a UBT physical claim.
"""
from __future__ import annotations

import cmath
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 50


def theta_positive(u: mp.mpf, nmax: int = 5000) -> mp.mpf:
    """sum_{n>=1} exp(-pi*u*n^2), using Jacobi inversion for small u."""
    u = mp.mpf(u)
    if u < 1:
        # theta(u)=u^{-1/2} theta(1/u); subtract the n=0 mode and divide by 2.
        dual = mp.mpf("0")
        for n in range(1, nmax + 1):
            term = mp.e ** (-mp.pi * n * n / u)
            dual += term
            if abs(term) < mp.mpf("1e-55"):
                break
        return mp.mpf("0.5") * (u ** (-mp.mpf("0.5")) - 1) + u ** (-mp.mpf("0.5")) * dual

    total = mp.mpf("0")
    for n in range(1, nmax + 1):
        term = mp.e ** (-mp.pi * u * n * n)
        total += term
        if abs(term) < mp.mpf("1e-55"):
            break
    return total


def mellin_theta_numeric(s: complex) -> complex:
    """Numerical Mellin integral of the positive theta trace."""
    f = lambda u: (u ** (s - 1)) * theta_positive(u)
    return mp.quad(f, [0, 1, mp.inf])


def mellin_theta_closed(s: complex) -> complex:
    return mp.gamma(s) * mp.pi ** (-s) * mp.zeta(2 * s)


def ztheta_direct(s: complex, t: float, nmax: int = 50000) -> complex:
    """Direct truncated quadratic-twist Dirichlet series."""
    total = 0j
    for n in range(1, nmax + 1):
        total += cmath.exp(1j * math.pi * t * n * n) / (n ** (2 * s))
    return total


def ztheta_hurwitz(s: complex, a: int, q: int) -> complex:
    """Exact rational-time Hurwitz-zeta decomposition, M=2q."""
    M = 2 * q
    total = 0j
    for r in range(1, M + 1):
        c = cmath.exp(1j * math.pi * a * r * r / q)
        total += c * complex(mp.zeta(2 * s, mp.mpf(r) / M))
    return (M ** (-2 * s)) * total


def gauss(a: int, q: int) -> complex:
    return sum(cmath.exp(2j * math.pi * a * r * r / q) for r in range(q))


def assert_close(name: str, x: complex, y: complex, tol: float) -> None:
    err = abs(complex(x) - complex(y))
    print(f"{name:38s} |delta|={err:.3e}")
    if err > tol:
        raise AssertionError(f"{name}: {err} > {tol}")


def main() -> None:
    print("A. Mellin(theta) = Gamma(s) pi^-s zeta(2s)")
    for s in (mp.mpf("1.0"), mp.mpf("1.5"), mp.mpf("2.0")):
        assert_close(f"s={s}", mellin_theta_numeric(s), mellin_theta_closed(s), 2e-12)

    print("\nB. Present slice and special t")
    s = 2.0
    # t=0: zeta(2s)
    assert_close("Z_theta(s;0)=zeta(2s)", ztheta_direct(s, 0.0, 50000), mp.zeta(2 * s), 2e-11)
    # t=1: -eta(2s)
    eta = (1 - 2 ** (1 - 2 * s)) * mp.zeta(2 * s)
    assert_close("Z_theta(s;1)=-eta(2s)", ztheta_direct(s, 1.0, 50000), -eta, 2e-11)

    print("\nC. Rational t Hurwitz decomposition")
    for a, q in ((1, 3), (1, 5), (2, 5), (3, 7)):
        direct = ztheta_direct(s, a / q, 50000)
        hz = ztheta_hurwitz(s, a, q)
        assert_close(f"t={a}/{q}", direct, hz, 2e-11)

    print("\nD. Noncollision of prime log frequencies (finite check)")
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    seen: dict[float, tuple[int, int]] = {}
    # Numerical finite sanity check only; exact proof is unique factorization.
    vals = []
    for p in primes:
        for k in range(1, 8):
            vals.append((2 * k * math.log(p), p, k))
    vals.sort()
    min_gap = min(vals[i + 1][0] - vals[i][0] for i in range(len(vals) - 1))
    print(f"minimum finite frequency gap = {min_gap:.6e} > 0")
    if min_gap <= 0:
        raise AssertionError("unexpected frequency collision")

    print("\nE. Exact Gauss-sum CRT checks")
    for q1, q2 in ((3, 5), (4, 9), (5, 7), (7, 11), (7, 13)):
        lhs = gauss(1, q1 * q2)
        rhs = gauss(q2, q1) * gauss(q1, q2)
        assert_close(f"g CRT q={q1}*{q2}", lhs, rhs, 3e-12)

    print("\nF. Gram conditioning for a 12-template bank")
    psis = np.linspace(0.02, 0.40, 12)
    n = np.arange(1, 200, dtype=float)
    G = np.empty((len(psis), len(psis)), dtype=float)
    for i, psi_i in enumerate(psis):
        for j, psi_j in enumerate(psis):
            G[i, j] = np.exp(-math.pi * (psi_i + psi_j) * n * n).sum()
    eig = np.linalg.eigvalsh(G)
    cond_scale = eig[-1] / max(abs(eig[0]), np.finfo(float).eps)
    ridge = eig[-1] * 1e-8
    eig_r = np.linalg.eigvalsh(G + ridge * np.eye(len(psis)))
    cond_r = eig_r[-1] / eig_r[0]
    print(f"lambda_min={eig[0]:.3e}, lambda_max={eig[-1]:.6f}, cond-scale={cond_scale:.3e}")
    print(f"ridge/lambda_max=1e-8 -> cond={cond_r:.3e}")
    if cond_scale < 1e15 or not (5e7 < cond_r < 2e8):
        raise AssertionError("unexpected Gram conditioning")

    print("\nG. Deterministic noisy matched-filter recovery")
    rng = np.random.default_rng(20260819)
    nt = 2048
    ts = np.linspace(0.0, 2.0, nt, endpoint=False)
    modes = np.arange(1, 40, dtype=float)[:, None]
    psi_grid = np.linspace(0.02, 0.40, 381)

    def template(psi: float) -> np.ndarray:
        return np.exp(-math.pi * psi * modes**2 + 1j * math.pi * modes**2 * ts[None, :]).sum(axis=0)

    bank = np.asarray([template(float(psi)) for psi in psi_grid])
    bank_norm = np.linalg.norm(bank, axis=1)
    for psi0 in (0.05, 0.12, 0.30):
        signal = template(psi0)
        rms = np.sqrt(np.mean(np.abs(signal) ** 2))
        noise = (rng.normal(size=nt) + 1j * rng.normal(size=nt)) / np.sqrt(2.0)
        observed = signal + noise * (rms / 3.0)
        score = np.abs(bank.conj() @ observed) ** 2 / (bank_norm**2 * np.linalg.norm(observed) ** 2)
        estimate = float(psi_grid[int(np.argmax(score))])
        error = abs(estimate - psi0)
        print(f"psi0={psi0:.3f}, estimate={estimate:.3f}, |error|={error:.3e}")
        if error > 0.0010000001:
            raise AssertionError("matched-filter recovery exceeded one grid step")

    print("\nAll theta/zeta bridge probes passed.")


if __name__ == "__main__":
    main()
