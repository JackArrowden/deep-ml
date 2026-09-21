def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    m, mid, n = len(a), len(a[0]), len(b[0])
    if mid != len(b):
        return -1

    result = [[] for _ in range(m)]
    for it in range(m * n):
        result[it // n].append(sum(x * y for x, y in zip(a[it // n], list(zip(*b))[it % n])))
        
    return result