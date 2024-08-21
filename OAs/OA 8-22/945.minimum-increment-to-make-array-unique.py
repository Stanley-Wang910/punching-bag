#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        incr_count = 0
        for i in range(len(nums) - 1):
            if nums[i+1] <= nums[i]:
                incr_count += nums[i] - nums[i + 1] + 1
                nums[i+1] = nums[i] + 1
        return incr_count
            
            

       
# @lc code=end

