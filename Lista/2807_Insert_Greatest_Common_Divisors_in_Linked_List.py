# 2807. Insert Greatest Common Divisors in Linked List
#
# Given the head of a linked list `head`, in which each node contains an integer value.
#
# Between every pair of adjacent nodes, insert a new node with a value equal to
# the greatest common divisor of them.
#
# Return the linked list after insertion.
#
# The **greatest common divisor** of two numbers is the largest positive integer
# that evenly divides both numbers.
#
# Example 1:
# - Input:  head = [18,6,10,3]
# - Output: [18,6,6,2,10,1,3]
# - Explanation: The 1st diagram denotes the initial linked list and the 2nd
#   diagram denotes the linked list after inserting the new nodes (nodes in blue
#   are the inserted nodes).
#     - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
#     - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
#     - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
#     - There are no more adjacent nodes, so we return the linked list.
#
# Example 2:
# - Input:  head = [7]
# - Output: [7]
# - Explanation: The 1st diagram denotes the initial linked list and the 2nd
#   diagram denotes the linked list after inserting the new nodes.
#     - There are no pairs of adjacent nodes, so we return the initial linked list.


# Primeira solução percorrendo a lista
# - Abordagem: Percorrer a lista e para cada par de nós adjacentes, calcular o MDC
#   e inserir um novo nó com esse valor entre eles.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def criar_lista(valores):
    head = ListNode(valores[0])
    atual = head

    for valor in valores[1:]:
        atual.next = ListNode(valor)
        atual = atual.next

    return head


def insertGreatestCommonDivisors_percorrer(head):
    atual = head
    import math
    # Equanto atual.next não é None
    while atual.next != None:
        # Calcula o valor do novo nó
        novo_valor = math.gcd(atual.val, atual.next.val)
        # Cria o novo nó
        novo_no = ListNode(novo_valor)
        # Passa o next do novo nó para o next do nó atual
        novo_no.next = atual.next
        # O next do nó atual é o novo nó
        atual.next = novo_no
        # Pula pro next.next para pular o novo nó
        atual = atual.next.next
    return head
# - Complexidade: O(n)


def imprimir_lista(head):
    valores = []
    atual = head
    while atual:
        valores.append(atual.val)
        atual = atual.next
    print(valores)


# Exemplo 1
head_1 = [18, 6, 10, 3]
lista_1 = criar_lista(head_1)
insertGreatestCommonDivisors_percorrer(lista_1)
imprimir_lista(lista_1)  # [18, 6, 6, 2, 10, 1, 3]

# Exemplo 2
head_2 = [7]
lista_2 = criar_lista(head_2)
insertGreatestCommonDivisors_percorrer(lista_2)
imprimir_lista(lista_2)  # [7]


# Segunda resolução usando recursão
# - Abordagem: Percorrer a lista recursivamente e para cada par de nós adjacentes,
#   calcular o MDC e inserir um novo nó com esse valor entre eles.
def insertGreatestCommonDivisors_recursivo(head):
    # Caso base da recursão
    if head is None or head.next is None:
        return head

    import math
    # Calcula o valor do novo nó
    novo_valor = math.gcd(head.val, head.next.val)
    # Cria o novo nó
    novo_no = ListNode(novo_valor)

    # Passa o next do novo nó para o next do nó atual
    novo_no.next = head.next

    # Passa o next do atual para o novo nó
    head.next = novo_no

    # Percorre recursivamente
    insertGreatestCommonDivisors_recursivo(head.next.next)
    return head
# - Complexidade: O(n)


# Exemplo 1
head_1 = [18, 6, 10, 3]
lista_1 = criar_lista(head_1)
insertGreatestCommonDivisors_recursivo(lista_1)
imprimir_lista(lista_1)  # [18, 6, 6, 2, 10, 1, 3]

# Exemplo 2
head_2 = [7]
lista_2 = criar_lista(head_2)
insertGreatestCommonDivisors_recursivo(lista_2)
imprimir_lista(lista_2)  # [7]
