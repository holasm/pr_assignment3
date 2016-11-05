from dtw.dtw import dtw
from numpy.linalg import norm
import numpy as np



x = np.array([0, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
y = np.array([1, 1, 1, 2, 2, 2, 2, 3, 2, 0, 1, 2]).reshape(-1, 1)
dist, cost= dtw(x, y, dist=my_custom_norm)

print dist
