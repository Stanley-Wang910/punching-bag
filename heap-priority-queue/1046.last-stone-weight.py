import heapq


def lastStoneWeight(self, stones: List[int]) -> int:

    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        # Remember the negative insert
        if second > first:
            # first - second because we want the proper negative value to be inserted in max-heap
            heapq.heappush(stones, first - second)

    return abs(stones[0]) if len(stones) != 0 else 0
