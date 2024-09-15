 # Sliding Window
class SlidingWindow:
    # 121. Best Time to Buy and Sell Stock / Easy / 9 minutes / (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0 
        for right in range(len(prices)):
            if  prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left]) 
        return max_profit

    # 3. Longest Substring Without Repeating Characters / Medium / 43 minutes / (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_ss = 0
        l = 0 
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_ss = max(max_ss, r-l+1)
        return max_ss
    
    # 424. Longest Repeating Character Replacement / Medium / 46 minutes / (https://leetcode.com/problems/longest-repeating-character-replacement/)
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        long_sub_s = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while k <  r - l + 1 - max(seen.values()): # The number of needed replacements
                seen[s[l]] -= 1
                l += 1
            long_sub_s = max(long_sub_s, r-l+1)
        return long_sub_s

    # 567. Permutation in String / Medium / 37 minutes / (https://leetcode.com/problems/permutation-in-string/)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        count2 = {}
        left = right = 0
        while right < len(s2):
            count2[s2[right]] = count2.get(s2[right], 0 ) + 1

            if right - left + 1 == len(s1): 
                if count1 == count2:
                    return True
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    count2.pop(s2[left])
                left += 1
            right += 1
        return False
