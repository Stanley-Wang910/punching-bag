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
    