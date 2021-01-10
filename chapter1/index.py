import numpy as np
from numpy import linalg
from scipy import sparse

# A = np.array([[3, -2, 1], [1, 1, -2], [-3, -2, 1]])
# b = np.array([7, -4, 1])

# print(linalg.solve(A, b))
# A = np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
# sp_A = sparse.csr_matrix(A)
# print(sp_A)

T = sparse.diags([-1, 2, -1], (-1, 0, 1), shape=(5, 5), format="csr")

print(T.toarray())
