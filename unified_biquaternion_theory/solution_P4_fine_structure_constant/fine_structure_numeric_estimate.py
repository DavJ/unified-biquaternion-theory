# Estimate of the fine-structure constant using physical constants
from scipy.constants import elementary_charge as e
from scipy.constants import hbar, c, epsilon_0
import numpy as np

alpha = e**2 / (4 * np.pi * epsilon_0 * hbar * c)
print(f"Calculated fine-structure constant: {alpha:.12f}")
