import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	#### Way 1
	# result = [[] for _ in range(new_shape[0])]
	# m, n = len(a), len(a[0])
	
	# if m * n != new_shape[0] * new_shape[1]:
	# 	return []

	# for i in range(new_shape[0]):
	# 	for j in range(new_shape[1]):
	# 		pos = i * new_shape[1] + j
	# 		result[i].append(a[pos // n][pos % n])

	# return result

	#### Way 2
	try:
		return np.array(a).reshape(new_shape).tolist()
	except:
		return []
	# return result.tolist() if result.all != [] else []
