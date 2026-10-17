# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    arr = []
    counter = 0
    counter_arr = 0
    for i in nums:
        # print(f"i: {i}, counter: {counter}, arr: {arr}")
        if i == 1:
            counter += 1
            counter_arr += 1
            if counter_arr == len(nums):
                arr.append(counter)
            continue
        arr.append(counter)
        counter_arr += 1
        counter = 0
    return max(arr)


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
