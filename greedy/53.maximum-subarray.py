def maxSubArray(self, nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0

    for num in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += num
        max_sum = max(max_sum, cur_sum)
    return max_sum


"""
greedy choice of kadane's algorithm:

at each position, the algorithm makes the choice of either: 

1. starting a new subarray (cur_sum = 0) 
2. extending the existing subarray by including the current number

"if the current running sum is negative, better to start a subarray, because
it would never be optimal to start with a negative as opposed to resetting to 0"
"""
