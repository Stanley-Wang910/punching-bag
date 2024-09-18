import heapq
import math


def kClosest(points, k):
    # using heap approach
    min_heap = []
    for x, y in points:
        dist = (x**2) + (
            y**2
        )  # don't need to sqrt, as the dist before ratio wise is the same
        min_heap.append([dist, x, y])

    heapq.heapify(min_heap)
    res = []
    while k > 0:
        dist, x, y = heapq.heappop(min_heap)
        res.append([x, y])
        k -= 1
    return res

    # distances = []
    # for i, point in enumerate(points):
    #     x_d = (point[0] - 0) ** 2
    #     y_d = (point[1] - 0) ** 2
    #
    #     distance = math.sqrt(x_d + y_d)
    #
    #     distances.append((distance, i))
    # distances.sort()
    #
    # res = []
    # for i in range(k):
    #     res.append(points[distances[i][1]])
    #
    # return res


#
# res = kClosest([[0, 1], [1, 0]], 2)
# print(res)
