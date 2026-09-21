import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A, T, S = np.array(A), np.array(T), np.array(S)

	try:
		T_inv, S_inv = np.linalg.inv(T), np.linalg.inv(S)
		return (T_inv @ A @ S).tolist()
	except:
		return -1