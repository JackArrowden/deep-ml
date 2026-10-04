import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(len(A[0]))
	diag = [1 / A[i][i] for i in range(len(A))]

	for i in range(n):
		x = x + diag * (b - A @ x)
	return np.round(x, 4)