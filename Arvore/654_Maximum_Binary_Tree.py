# 654. Maximum Binary Tree

# You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.

# Example 1:

# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
#     - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
#         - Empty array, so no child.
#         - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
#             - Empty array, so no child.
#             - Only one element, so child is a node with value 1.
#     - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
#         - Only one element, so child is a node with value 0.
#         - Empty array, so no child.

# Example 2:

# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: list[int]) -> TreeNode | None:

    if not nums:
        return

    root_value = max(nums)

    left = []
    right = []
    flag = True
    root = TreeNode(root_value)

    for i in nums:
        if i == root_value:
            flag = False
            continue
        if flag:
            left.append(i)
        if not flag:
            right.append(i)

    root.left = constructMaximumBinaryTree(left)
    root.right = constructMaximumBinaryTree(right)

    print(
        f"{root.val}: left={root.left.val if root.left else None}, right={root.right.val if root.right else None}"
    )

    return root


constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
