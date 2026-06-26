# 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = []
        left_sum = ''
        right_sum = ''
        right = []
        head_left = l1
        head_right = l2
        while head_right:
            right.append(head_right.val)
            head_right = head_right.next
        while head_left:
            left.append(head_left.val)
            head_left = head_left.next

        while len(left) != 0:
            left_sum += str(left.pop())

        while len(right) != 0:
            right_sum += str(right.pop())

        sum = int(left_sum) + int(right_sum)
        sum_arr = list(str(sum))
        sum_arr.reverse()

        for i in range(len(sum_arr)):
            sum_arr[i] = int(sum_arr[i])

        return criar_lista(sum_arr)

def criar_lista(valores):
    head = ListNode(valores[0])
    atual = head
    for valor in valores[1:]:
        atual.next = ListNode(valor)
        atual = atual.next
    return head

def imprimir_lista(head):
    valores = []
    atual = head
    while atual:
        valores.append(atual.val)
        atual = atual.next
    print(valores)

def main():
    solution = Solution()
    l1 = criar_lista([2, 4, 3])
    l2 = criar_lista([5, 6, 4])
    imprimir_lista(solution.addTwoNumbers(l1, l2))  # [7, 0, 8]

main()
