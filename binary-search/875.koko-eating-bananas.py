class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            count = 0
            hours = sum(math.ceil(pile / m) for pile in piles)
            print(m)
            print(hours)
            if hours > h:
                l = m + 1

            else:
                r = m - 1
        return l
