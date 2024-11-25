def canJump(self, nums: List[int]) -> bool:
    i = 0
    while i < len(nums):
        if nums[i] >= ((len(nums) - 1) - i):
            return True
        best_jump = 0
        for j in range(nums[i]):
            best_jump = max(nums[j] + j, best_jump)
        i = best_jump
    return False
