import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mean, std = np.mean(data, axis = 0), np.std(data, axis = 0)
	amin, amax = np.min(data, axis = 0), np.max(data, axis = 0)

	return \
		np.round((data - mean) / std, 4), \
		np.round((data - amin) / (amax - amin), 4)