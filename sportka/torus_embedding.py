# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/torus_embedding.py — Torus embedding for lottery number features.

Numbers 1–49 are embedded on a torus T^2 = S^1 × S^1 using two circular
coordinates.  This gives a periodic geometry that respects the cyclic
structure of number relationships.

Two factorizations are provided:
    - 7 × 7 torus (natural for 49 numbers)
    - coprime factorization using periods suggested by UBT torus geometry
"""
from __future__ import annotations

import math
from typing import Tuple

import numpy as np

from sportka.features import N_NUMBERS

# ---------------------------------------------------------------------------
# Torus embedding
# ---------------------------------------------------------------------------

def torus_embed_7x7(
    numbers: np.ndarray,
    n: int = N_NUMBERS,
) -> np.ndarray:
    """
    Embed lottery numbers on a 7×7 torus using (sin, cos) × 2.

    Each number k (1-indexed) maps to coordinates:
        row = (k-1) // 7
        col = (k-1) %  7
        θ_row = 2π row / 7
        θ_col = 2π col / 7
    Output: [sin(θ_row), cos(θ_row), sin(θ_col), cos(θ_col)]

    Parameters
    ----------
    numbers : 1-D array of lottery numbers (1..49).

    Returns
    -------
    embeddings : shape (len(numbers), 4)
    """
    k = np.asarray(numbers, dtype=np.float64) - 1.0  # 0-indexed
    row = k // 7
    col = k % 7
    theta_row = 2 * math.pi * row / 7
    theta_col = 2 * math.pi * col / 7
    return np.stack([
        np.sin(theta_row),
        np.cos(theta_row),
        np.sin(theta_col),
        np.cos(theta_col),
    ], axis=1).astype(np.float32)


def torus_embed_primes(
    numbers: np.ndarray,
    p1: int = 7,
    p2: int = 43,
) -> np.ndarray:
    """
    Embed numbers on a coprime-period torus (p1, p2).

    Uses mod-p1 and mod-p2 periodicity to create two independent angular
    coordinates.  Coprime periods guarantee coverage of all residues.

    Parameters
    ----------
    numbers : 1-D array of lottery numbers.
    p1, p2 : Periods for the two torus dimensions.

    Returns
    -------
    embeddings : shape (len(numbers), 4)
    """
    k = np.asarray(numbers, dtype=np.float64)
    theta1 = 2 * math.pi * (k % p1) / p1
    theta2 = 2 * math.pi * (k % p2) / p2
    return np.stack([
        np.sin(theta1),
        np.cos(theta1),
        np.sin(theta2),
        np.cos(theta2),
    ], axis=1).astype(np.float32)


def build_torus_feature_matrix(
    n: int = N_NUMBERS,
    embed_fn=None,
) -> np.ndarray:
    """
    Build a torus embedding matrix for all numbers 1..N_NUMBERS.

    Parameters
    ----------
    n : Pool size (default 49).
    embed_fn : Embedding function. Defaults to torus_embed_7x7.

    Returns
    -------
    mat : shape (n, 4) — one embedding vector per number.
    """
    if embed_fn is None:
        embed_fn = torus_embed_7x7
    numbers = np.arange(1, n + 1)
    return embed_fn(numbers)


def aggregate_draw_torus_features(
    draw_numbers: list,
    embed_fn=None,
) -> np.ndarray:
    """
    Aggregate torus embeddings of drawn numbers into a single feature vector.

    Takes the mean embedding of all drawn numbers.

    Parameters
    ----------
    draw_numbers : List of drawn numbers in a single draw.
    embed_fn : Embedding function.

    Returns
    -------
    vec : shape (4,)
    """
    if not draw_numbers:
        return np.zeros(4, dtype=np.float32)
    emb = build_torus_feature_matrix(embed_fn=embed_fn)
    idxs = [n - 1 for n in draw_numbers if 1 <= n <= N_NUMBERS]
    if not idxs:
        return np.zeros(4, dtype=np.float32)
    return emb[idxs].mean(axis=0).astype(np.float32)


def build_draw_torus_matrix(df, embed_fn=None) -> np.ndarray:
    """
    Build torus-embedding feature matrix for a DataFrame of draws.

    Returns
    -------
    mat : shape (len(df), 4)
    """
    return np.array(
        [aggregate_draw_torus_features(nums, embed_fn=embed_fn)
         for nums in df["numbers"]],
        dtype=np.float32,
    )
