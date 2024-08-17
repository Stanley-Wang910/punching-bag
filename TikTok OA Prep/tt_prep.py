class TikTokPrep:
    def minimumSwaps(arr):
        counter = 0
        for i in range(len(arr)):
            while i != arr[i] - 1:
                cur_val = arr[i]
                swap_idx = arr[i] - 1
                swap_val = arr[swap_idx]
                arr[i] = swap_val
                arr[swap_idx] = cur_val
                counter += 1
        return counter  
                
    # 66. Plus One - 8:23 - https://leetcode.com/problems/plus-one/description/
    def plusOne(self, digits: List[int]) -> List[int]:
        num_s = ''
        for i in digits:
            num_s += str(i)
        num_s = int(num_s) + 1
        num_s= str(num_s)
        res  = list(num_s)
        res = [int(i) for i in res]
        return res

    # 56. Merge Intervals - 32 - https://leetcode.com/problems/merge-intervals/description/
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
        merge = []
        intervals = intervals.sort(key = lambda x : x[0])
        for interval in intervals:
            if not merge or merge[-1][1] >= interval[0]:
                merge.append(interval)

            else: 
                # Merge current interval with last one in merge[]
                merge[1][-1] =  max(merge[1][-1], interval[1])

        return merge


    # 131. Palindrom Partition -- Yeah I don't understand jackshit here
    def partition(self, s: str) -> List[List[str]]:
        res = [] # stores all partitions
        part = [] # stores current partitions

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

        

     








