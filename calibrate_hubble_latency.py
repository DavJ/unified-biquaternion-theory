
H0_planck = 67.4
H0_local = 73.0

delta = 1.0 - (H0_planck / H0_local)
F = 256
O = delta * F

print("delta =", delta)
print("Overhead O =", O)
