class Solution:
    # 704. Binary Search / Easy / 9 minutes / (https://leetcode.com/problems/binary-search/)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1 
            else:
                return mid
        return -1

    # 74. Search a 2D Matrix / Medium / 21:28 minutes / (https://leetcode.com/problems/search-a-2d-matrix/)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                mid_l, mid_r = 0, len(matrix[mid]) - 1
                while mid_l <= mid_r:
                    m = (mid_l + mid_r) //2
                    if target > matrix[mid][m]:
                        mid_l  = m + 1
                    elif target < matrix[mid][m]:
                        mid_r = m - 1
                    else: 
                        return True 
                break
        return False

    # 875. Koko Eating Bananas / Medium / 47 minutes / (https://leetcode.com/problems/koko-eating-bananas/) -- Review
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
               res = min(res, k)
               r = k - 1
            else:
                l = k + 1
        return res
    
    # 153. Find Minimum in Rotated Sorted Array / Medium / 4:37 minutes / (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[r]

    # 33. Search in Rotated Sorted Array / Medium / 60+ minutes (Fell asleep) / (https://leetcode.com/problems/search-in-rotated-sorted-array/)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]: # Don't miss target at beginning
                    r = mid - 1
                else:
                    l = mid + 1
            else: 
                if nums[mid] < target <= nums[r]: # Don't miss target at end
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    # 981. Time Based Key-Value Store / Medium / 19 minutes / (https://leetcode.com/problems/time-based-key-value-store/)
    class TimeMap:
        def __init__(self):
            # key: [value, timestamp]
            self.store = {}

        def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.store:
                self.store[key] = [] # Initialize empty value, timestamp
            # Populate with values
            self.store[key].append([value, timestamp])

        def get(self, key: str, timestamp: int) -> str:
            res = "" # Empty string to return in case of no result
            values = self.store.get(key, []) # Or empty list if no results 
            
            l, r = 0, len(values) - 1

            while l <= r:
                m = (l + r) // 2
                if values[m][1] <= timestamp:
                    res = values[m][0]
                    l = m + 1 # To find largest prev_t associated with t
                else:
                    r = m - 1
            return res
    

    