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
        nums.sort()
        incr_count = 0
        for i in range(len(nums) - 1):
            while nums[i + 1] <= nums[i]:
                nums[i + 1] += 1
                incr_count += 1
        return incr_count
        # Test


def test_cases():
    return [
        # Example: (inputs, expected_output)
        ([[3, 2, 1, 2, 1, 7]], [6]),
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
