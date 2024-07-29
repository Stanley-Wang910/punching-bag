
class Solution:
    # 217. Contains Duplicate / Easy / 4 minutes / (https://leetcode.com/problems/contains-duplicate/)
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False 

    # 242. Valid Anagram / Easy / 8 minutes / (https://leetcode.com/problems/valid-anagram/)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for c in s:
            if c not in s_dict.keys():
                s_dict[c] = 1
            else:
                temp = s_dict[c]
                s_dict[c] = temp + 1
        for c in t:
            if c not in t_dict.keys():
                t_dict[c] = 1
            else:
                temp = t_dict[c]
                t_dict[c] = temp + 1
        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
        return True



                
