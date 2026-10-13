import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	Xnp, ynp = np.array(X), np.array(y)
	return (np.linalg.pinv(X) @ y).tolist()