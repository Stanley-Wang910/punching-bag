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










