import heapq


def findKthLargest(nums, k):
    nums = [-num for num in nums]
    heapq.heapify(nums)

    while k > 0:
        target = heapq.heappop(nums)
        k -= 1
    return abs(target) if target != None else None
