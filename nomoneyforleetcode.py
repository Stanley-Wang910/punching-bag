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
        arr = args[0]
        
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
                
         
     





def test_cases():
    return [
        # Example: (inputs, expected_output)

        ([[1, 3, 5, 2, 4, 6, 7]], [3]),     



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
