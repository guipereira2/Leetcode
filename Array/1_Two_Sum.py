# 1. Two Sum
#
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
#
# You may assume that each input would have exactly *one solution*, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


def twoSum_forca_bruta(nums, target):
    arr = []
    for i, valor_1 in enumerate(nums):
        for j, valor_2 in enumerate(nums):
            if valor_1 + valor_2 == target and ([j, i]) not in arr and i != j:
                arr.append([i, j])
    for i in arr:
        return arr.pop()


nums_1 = [2, 7, 11, 15]
target_1 = 9
print(twoSum_forca_bruta(nums_1, target_1))  # [0, 1]
