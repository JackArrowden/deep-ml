def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	cols = len(matrix[0])
	if mode == 'column':
		return [sum(col) / len(matrix) for col in zip(*matrix)]
	else:
		return [sum(col) / cols for col in matrix]
	# return means