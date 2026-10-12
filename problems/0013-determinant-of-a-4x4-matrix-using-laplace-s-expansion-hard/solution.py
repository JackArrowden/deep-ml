def remove(matrix: list[list[int | float]], row: int, col: int):
	del matrix[row]
	return [row[:col] + row[col + 1:] for row in matrix]

def detRecursive(matrix: list[list[int | float]], size: int) -> float:
	if size == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	
	return sum(((-1) ** i) * matrix[i][0] * detRecursive(remove(matrix.copy(), i, 0), len(matrix) - 1) for i in range(len(matrix)))

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	return detRecursive(matrix, len(matrix))	