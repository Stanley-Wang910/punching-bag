#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        c_set = set()
        i, j = 0, 0
        while j < len(s):
            c = s[j]
            print(c)
            while s[j] in c_set:

                c_set.remove(s[i])
                i += 1

            c_set.add(c)

            max_length = max(max_length, j - i + 1)
            j += 1
            
        return max_length
            

# @lc code=end

