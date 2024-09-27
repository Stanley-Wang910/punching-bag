def findLHS(self, nums: List[int]) -> int:
    nums = sorted(nums)
    print(nums)
    l, r = 0, 0
    max_length = 0
    while r < len(nums):
        print(nums[l], nums[r])
        while l < r and nums[r] - nums[l] > 1:
            l += 1

        if nums[r] - nums[l] == 1:
            max_length = max(max_length, r - l + 1)
        r += 1
    return max_length
