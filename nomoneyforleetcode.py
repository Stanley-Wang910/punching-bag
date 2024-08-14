import time
import traceback
import math

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

class Solution:
    @timer
    def solve(self, *args):
        nums = args[0]
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if nums[i-1] == n and i < len(nums):
                continue
                
            l, r = i + 1, len(nums) -1 

            while l < r:
                three_s = nums[l] + nums[r] + n
                if three_s < 0:
                    l += 1
                elif three_s > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
        return res

            





def test_cases():
    return [
        # Example: (inputs, expected_output)

        ([[-1,0,1,2,-1,-4]], [[-1,-1,2],[-1,0,1]]),     


    ]

@timer
def practice():
    solution = Solution()
    
    for i, (inputs, expected) in enumerate(test_cases(), 1):
        print(f"\nTest Case {i}:")
        print(f"Inputs: {inputs}")
        print(f"Expected Output: {expected}")
        
        try:
            result = solution.solve(*inputs)
            print(f"Your Output: {result}")
            
            if result == expected:
                print("Status: PASSED")
            else:
                print("Status: FAILED")
        except Exception as e:
            print("Status: ERROR")
            print("Exception:", str(e))
            print("Traceback:")
            print(traceback.format_exc())

if __name__ == "__main__":
    practice()
