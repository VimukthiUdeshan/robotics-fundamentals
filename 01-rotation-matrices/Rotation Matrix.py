import numpy as np

theta = np.deg2rad(30)
c, s = np.cos(theta), np.sin(theta)

Rz = np.array([
    [c, -s, 0],
    [s, c, 0],
    [0, 0, 1]
])

print(Rz)