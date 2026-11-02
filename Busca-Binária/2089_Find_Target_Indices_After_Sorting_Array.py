# 2089. Find Target Indices After Sorting Array

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.

# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.


def targetIndices(nums: list[int], target: int) -> list[int]:
    arr = []
    nums.sort()

    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            arr.append(mid)
            counter_right = mid + 1
            counter_left = mid - 1

            while counter_right < len(nums) and nums[counter_right] == target:
                arr.append(counter_right)
                counter_right += 1

            while counter_left >= 0 and nums[counter_left] == target:
                arr.append(counter_left)
                counter_left -= 1

            break

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    arr.sort()

    return arr


print(targetIndices([1, 2, 5, 2, 3], 2))
print(targetIndices([100, 1, 100], 100))
