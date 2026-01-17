"""Syndrome computations for RS(n,k) over GF(256).

This module does NOT decode. It only computes syndromes
S_j = sum_i c_i * alpha^(i*j) for j=1..(n-k).

For RS(255,201): n-k = 54, t = 27.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

from .gf256 import add, mul, pow_alpha


@dataclass(frozen=True)
class RSParams:
    n: int = 255
    k: int = 201

    @property
    def nsym(self) -> int:
        return self.n - self.k


def syndromes(codeword: Sequence[int], params: RSParams = RSParams()) -> List[int]:
    """Compute RS syndromes for a length-n codeword.

    Returns list S[1..nsym] as length nsym with indices 0..nsym-1.
    """
    if len(codeword) != params.n:
        raise ValueError(f"codeword length must be {params.n}, got {len(codeword)}")

    out: List[int] = [0] * params.nsym
    for j in range(1, params.nsym + 1):
        sj = 0
        for i, c in enumerate(codeword):
            if c:
                sj = add(sj, mul(c, pow_alpha(i * j)))
        out[j - 1] = sj
    return out


def syndrome_zero_count(codeword: Sequence[int], params: RSParams = RSParams()) -> int:
    """Count how many syndromes are exactly zero."""
    s = syndromes(codeword, params)
    return sum(1 for x in s if x == 0)
