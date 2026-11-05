import numpy as np

theta = np.deg2rad(30)
c, s = np.cos(theta), np.sin(theta)

Rz = np.array([
    [c, -s, 0],
    [s, c, 0],
    [0, 0, 1]
])

print(Rz)
print(Rz.T @ Rz)
print(np.linalg.det(Rz))

print("Orthagonal: ", np.allclose(Rz.T @ Rz, np.eye(3)))
print("Determinant is +1:", np.isclose(np.linalg.det(Rz), 1.0))