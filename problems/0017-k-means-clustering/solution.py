def cal_euclid_dis(point: tuple[float, ...], cen: tuple[float, ...]):
	return (sum((x - y) ** 2 for x, y in zip(point, cen))) ** 0.5

def cal_group(point: tuple[float, ...], centroids: list[tuple[float, ...]]):
	min_dis, group = float('inf'), float('inf')
	for i, centroid in enumerate(centroids):
		dis = cal_euclid_dis(point, centroid)
		if dis < min_dis:
			min_dis = dis
			group = i

	return group

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	cur_cent = initial_centroids
	for _ in range(max_iterations):
		groups = [tuple([0] * len(points[0])) \
			for _ in range(k)]
		num_list = [0 for _ in range(k)]

		for point in points:
			group_id = cal_group(point, cur_cent)
			num_list[group_id] += 1
			groups[group_id] = tuple(a + b \
				for (a, b) in zip(groups[group_id], point))

		cur_cent = [tuple(sump[j] / nump for j in range(len(sump))) \
			if nump != 0 else cur_cent[i] \
			for i, (sump, nump) in enumerate(zip(groups, num_list))]
	
	return cur_cent