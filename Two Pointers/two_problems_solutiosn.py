class TwoPointers:
    # 125. Valid Palindrome / Easy / 10 minutes / (https://leetcode.com/problems/valid-palindrome/)
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = s.lower()
        string = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                string += c
        print (string)
        i,j = 0, (len(string) - 1)

        while  i < len(string) / 2 and i < j:
            if string[i] != string [j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    
    # 167. Two Sum II - Input array is sorted / Medium / 12 minutes / (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r] 

            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]

    # 15. 3Sum / Medium / 30  minutes / (https://leetcode.com/problems/3sum/)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

    # 11. Container With Most Water / Medium / 15 minutes / (https://leetcode.com/problems/container-with-most-water/)
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            if height[l] < height[r]:
                if height[l]*(r-l) > maxArea:
                    maxArea = height[l]*(r-l)
                l += 1
            else:
                if height[r] *(r-l) > maxArea:
                    maxArea = height[r] * (r-l)
                r -= 1
        return maxArea
    
    # 42. Trapping Rain Water / Hard / 60 minutes / (https://leetcode.com/problems/trapping-rain-water/)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right: 
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left] # Will be zero if the new height is assinged max, meaning no water can be traped in that position
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res
        