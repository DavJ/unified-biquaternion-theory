"""
Reed–Solomon syndrome utilities (GF(256)) used by spectral_parity_test.

This module intentionally implements only what's needed for the forensic fingerprint pipeline:
- RSParams: holds (n, k, nsym) and precomputed power table for fast syndrome evaluation
- syndrome_zero_count(codeword, rs_params): returns count of zero syndromes among S_1..S_nsym

Notes
-----
- Field: GF(256) with primitive polynomial 0x11d (x^8 + x^4 + x^3 + x^2 + 1), standard in RS(255,*).
- We compute syndromes for a codeword c[0..n-1] as:
    S_j = sum_{i=0..n-1} c_i * alpha^(j*i),   j = 1..nsym
  and count how many of these S_j equal 0.
- This does NOT perform decoding or correction (not needed for this test).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

# Primitive polynomial for GF(256) (used by many RS codecs)
_PRIM = 0x11D
_ALPHA = 0x02  # generator element for exp/log tables


def _build_gf_tables(prim: int = _PRIM):
    # exp table length 512 for easy wrap; log length 256
    gf_exp = [0] * 512
    gf_log = [0] * 256
    x = 1
    for i in range(0, 255):
        gf_exp[i] = x
        gf_log[x] = i
        x <<= 1
        if x & 0x100:
            x ^= prim
        x &= 0xFF
    # duplicate for wraparound: exp[i+255] = exp[i]
    for i in range(255, 512):
        gf_exp[i] = gf_exp[i - 255]
    return gf_exp, gf_log


_GF_EXP, _GF_LOG = _build_gf_tables()


def gf_mul(a: int, b: int) -> int:
    """Multiply two GF(256) elements."""
    a &= 0xFF
    b &= 0xFF
    if a == 0 or b == 0:
        return 0
    return _GF_EXP[_GF_LOG[a] + _GF_LOG[b]]


def gf_pow(alpha: int, power: int) -> int:
    """alpha^power in GF(256) for alpha=2 with our tables."""
    if power < 0:
        power %= 255
    return _GF_EXP[power % 255]


@dataclass(frozen=True)
class RSParams:
    n: int = 255
    k: int = 201
    nsym: int = 54  # parity symbols = n-k

    # Precomputed alpha^(j*i) table:
    # pow_table[j-1][i] = alpha^(j*i) for j in 1..nsym, i in 0..n-1
    pow_table: List[List[int]] = None  # type: ignore[assignment]

    def __post_init__(self):
        object.__setattr__(self, "nsym", int(self.n - self.k) if self.nsym is None else int(self.nsym))
        n = int(self.n)
        nsym = int(self.nsym)
        # Precompute table for alpha=2
        table: List[List[int]] = []
        for j in range(1, nsym + 1):
            row = [0] * n
            # alpha^(j*i) = exp[(j*i) mod 255]
            for i in range(n):
                row[i] = _GF_EXP[(j * i) % 255]
            table.append(row)
        object.__setattr__(self, "pow_table", table)


def syndrome_zero_count(codeword: Sequence[int], rs_params: RSParams) -> int:
    """
    Compute RS syndromes S_1..S_nsym and count how many are exactly zero.

    Parameters
    ----------
    codeword:
        Iterable of ints (0..255), expected length rs_params.n (255).
    rs_params:
        RSParams with precomputed power table.

    Returns
    -------
    int:
        Number of j in [1..nsym] where syndrome S_j == 0.
    """
    n = rs_params.n
    nsym = rs_params.nsym
    if len(codeword) != n:
        # Be strict: this should always be 255 in the pipeline.
        raise ValueError(f"codeword length {len(codeword)} != n={n}")

    zeros = 0
    # For each syndrome j, compute sum c_i * alpha^(j*i)
    # Use XOR as field addition.
    for j in range(nsym):
        s = 0
        row = rs_params.pow_table[j]
        # localize for speed
        for i, c in enumerate(codeword):
            c &= 0xFF
            if c:
                s ^= gf_mul(c, row[i])
        if s == 0:
            zeros += 1
    return zeros
