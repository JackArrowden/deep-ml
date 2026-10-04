import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(A.shape[0])
	inv_diag = 1 / np.diag(A)

	for _ in range(n):
		x += inv_diag * (b - A @ x)

	return np.round(x, 4).tolist()