import heapq
import math


def kClosest(points, k):
    distances = []
    for i, point in enumerate(points):
        x_d = (point[0] - 0) ** 2
        y_d = (point[1] - 0) ** 2

        distance = math.sqrt(x_d + y_d)

        distances.append((distance, i))
    distances.sort()

    res = []
    for i in range(k):
        res.append(points[distances[i][1]])

    return res


res = kClosest([[0, 1], [1, 0]], 2)
print(res)
