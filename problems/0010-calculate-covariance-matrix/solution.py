def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n = len(vectors[0])
	temp = [[(item - sum(vec) / n) for item in vec] for vec in vectors]
	temp = matrixmul(temp, list(zip(*temp)))
	return [[item / (n - 1) for item in vec] for vec in temp]

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    m, mid, n, vec_b = len(a), len(a[0]), len(b[0]), list(zip(*b))
    if mid != len(b):
        return -1

    result = [[] for _ in range(m)]
    for it in range(m * n):
        result[it // n].append(sum(x * y for x, y in zip(a[it // n], vec_b[it % n])))
        
    return result