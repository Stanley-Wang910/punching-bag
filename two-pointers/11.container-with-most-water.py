class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                max_area = max(height[l]*(r-l), max_area)
                l += 1
            else:
                max_area = max(height[r]*(r-l), max_area)
                r -= 1
        return max_area
