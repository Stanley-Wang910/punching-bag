
class ArraysHashing:
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

    # 1. Two Sum / Easy / 5 minutes / (https://leetcode.com/problems/two-sum/)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            if target - n in seen:
                return [i, seen[target-n]]
            seen[n] = i

    # 49. Group Anagrams / Medium / 14 minutes / (https://leetcode.com/problems/group-anagrams/)
    # Review 49, 13:21 min 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in string_dict.keys():
                string_dict[key].append(s)
            else:
                string_dict[key] = [s] #initialize as list
        return list(string_dict.values())

    # 347. Top K Frequent Elements / Medium / 13 minutes / (https://leetcode.com/problems/top-k-frequent-elements/)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_values = {}
        for num in nums:
            if num in seen_values:
                seen_values[num] += 1
            else: seen_values[num] = 1
        sorted_dict = dict(sorted(seen_values.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]

        # Review 347 10 minutes
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            seen = {}
            for n in nums:
                seen[n] = seen.get(n, 0) + 1
            
            res = []
            while k:
                max_val = max(seen.values())
                for key,val in seen.items():
                    if val == max_val:
                        res.append(key)
                        k -= 1
                        break
                del seen[key]
            return res

    # Encode and decode strings / Medium / 21 minutes / (https://neetcode.io/problems/string-encode-and-decode)
    def encode(self, strs: List[str]) -> str:
        #['hello', 'world']
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + '#' + ''.join(s)
        return encoded_string    
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print(i)
            length = int(s[i:j])
        
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
    
    # 238. Product of Array Except Self / Medium / 30 minutes / (https://leetcode.com/problems/product-of-array-except-self/)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initiate prefix / suffix arrays : pop. with 1's to fill during loop
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range (1, len(nums)): # no need to fill [0], as no prod. of elements before
            prefix[i] = prefix[i-1] * nums[i-1] 
        for i in range(len(nums)-2, -1, -1): # reverse traverse to 0
            suffix[i] = suffix[i+1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(len(nums))]
        return answer

    # 36. Valid Sudoku / Medium / 20 minutes / (https://leetcode.com/problems/valid-sudoku/)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set) # key = (r/3 , c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # If empty spot
                    continue
                # if the current value has been seen in the rows hashset at key[r]     
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in square[(r // 3, c //3)]): 
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r // 3, c //3)].add(board[r][c])
        return True

    # 128. Longest Consecutive Sequence / Medium / 13 minutes / (https://leetcode.com/problems/longest-consecutive-sequence/)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] != nums[i-1]:
                count = 1
            max_count = max(max_count, count)
        return max_count





                
