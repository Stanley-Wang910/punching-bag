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
        target = args[1]
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > target and target < nums[r]:
                l = mid + 1
            else:
                r = mid
        return r
            





def test_cases():
    return [
        # Example: (inputs, expected_output)

        ([[4,5,6,7,0,1,2], 0], 4),    


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


            # assigned_lockers = {}
        # free_lockers = []
        # last_assigned = 0
        # next_locker = 1

        # for client in clients:
        #     if client in assigned_lockers:
        #         # Free the locker if client already has one assigned
        #         freed_locker = assigned_lockers.pop(client)
        #         free_lockers.append(freed_locker)
        #     else:
        #         # Assign the next available locker
        #         if free_lockers:
        #             min_avail = min(free_lockers)
        #             # Use a previously freed locker if available
        #             locker_to_assign = free_lockers.pop(free_lockers.index(min_avail))
        #         else:
        #             # Otherwise, use the next new locker
        #             locker_to_assign = next_locker
        #             next_locker += 1
                
        #         assigned_lockers[client] = locker_to_assign
        #         last_assigned = locker_to_assign

        # return last_assigned
                