# 1302. Deepest Leaves Sum
#
# Given the `root` of a binary tree, return the sum of values of its deepest leaves.
#
# Example 1:
# Input:  root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
#
# Example 2:
# Input:  root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19

def deepestLeavesSum(root) -> int:

    def altura(no):
        if no is None:
            return 0
        esquerda = altura(no.left)
        direita = altura(no.right)
        return max(esquerda, direita) + 1

    altura = altura(root)

    def inorder(no, contador=1, arr=None):
        if arr is None:
            arr = []
        if no and contador != altura:
            inorder(no.left, contador + 1, arr)
            inorder(no.right, contador + 1, arr)
        elif no and contador == altura:
            arr.append(no.val)
        return sum(arr)

    return inorder(root)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insereArv(root: "TreeNode", val: int) -> "TreeNode":
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insereArv(root.left, val)
    else:
        root.right = insereArv(root.right, val)
    return root

def insereLista(root: "TreeNode", valores: list[int]) -> "TreeNode":
    for i in valores:
        root = insereArv(root, i)
    return root

def main():
    arvore = insereLista(None, [5, 3, 8, 2, 4, 7, 9])
    print(deepestLeavesSum(arvore))  # 22

main()
