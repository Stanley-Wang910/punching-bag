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
                






