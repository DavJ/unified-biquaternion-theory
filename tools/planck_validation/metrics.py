# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License

from __future__ import annotations

import math

import numpy as np
from scipy.stats import chi2


def sigma_deviation(prediction: float, observation: float, sigma: float) -> float:
    return (prediction - observation) / sigma


def chi2_single(prediction: float, observation: float, sigma: float) -> float:
    z = sigma_deviation(prediction, observation, sigma)
    return z * z


def chi2_vector(predictions, observations, sigmas) -> float:
    p = np.asarray(predictions, dtype=float)
    o = np.asarray(observations, dtype=float)
    s = np.asarray(sigmas, dtype=float)
    z = (p - o) / s
    return float(np.sum(z**2))


def success_criterion(z_scores, threshold: float = 1.0) -> bool:
    return all(abs(float(z)) <= threshold for z in z_scores)


def chi2_pvalue(chi2_value: float, dof: int) -> float:
    if dof <= 0:
        raise ValueError("dof must be positive")
    return float(chi2.sf(chi2_value, dof))
