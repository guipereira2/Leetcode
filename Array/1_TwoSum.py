# 1. Two Sum
#
# Given an array of integers `nums` and an integer `target`, return indices of the
# two numbers such that they add up to `target`.
#
# You may assume that each input would have exactly *one solution*, and you may not
# use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
# - Input: nums = [2,7,11,15], target = 9
# - Output: [0,1]
# - Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# - Input: nums = [3,2,4], target = 6
# - Output: [1,2]
#
# Example 3:
# - Input: nums = [3,3], target = 6
# - Output: [0,1]


# Primeira solução por força bruta
# - Abordagem: Usar força bruta para percorre todos itens e comparar a soma com o target
def twoSum_forca_bruta(nums, target):
    # Cria uma array para armazenar os índices
    arr = []
    # Percorre a array usando força bruta comparando todos os valores
    for i, valor_1 in enumerate(nums):
        for j, valor_2 in enumerate(nums):
            # Verifica se a soma dos valores corresponde ao target, se os índices são diferentes e se o valor já não está na array em outra ordem
            if valor_1 + valor_2 == target and ([j, i]) not in arr and i != j:
                # Adiciona na array
                arr.append([i, j])
    # Usa o pop para retornar os valores
    for i in arr:
        return arr.pop()
# - Complexidade: O(n^2)


# Exemplo 1:
nums_1 = [2, 7, 11, 15]
target_1 = 9
print(twoSum_forca_bruta(nums_1, target_1))  # [0, 1]

# Exemplo 2:
nums_2 = [3, 2, 4]
target_2 = 6
print(twoSum_forca_bruta(nums_2, target_2))  # [1, 2]

# Exemplo 3:
nums_3 = [3, 3]
target_3 = 6
print(twoSum_forca_bruta(nums_3, target_3))  # [0, 1]


# Segunda solução
# - Abordagem: Ordernar a lista. Em seguida, armazenar os índices originais em um
#   hashmap, então dois ponteiros são utilizados: um no início e outro no final da
#   lista ordenada. É feita a comparação da soma dos elementos dos ponteiros com o
#   target. Se for igual, o hashmap é consultado para retornar os índices. Se for
#   maior, o ponteiro da direita é decrementado. Se for menor o ponteiro da
#   esquerda é incrementado.
def twoSum_hash(nums, target):
    esquerda = 0
    direita = len(nums) - 1
    hashmap_indices = {}

    # Adiciona os valores e índices no hashmap
    for indice, valor in enumerate(nums):
        if valor in hashmap_indices:
            hashmap_indices[valor].append(indice)
        else:
            hashmap_indices[valor] = [indice]
    # Ordena a array
    nums.sort()
    # Percorre a array com o uso dos ponteiros
    while esquerda != direita:
        # Se a soma é igual o target retorna os índices
        if nums[esquerda] + nums[direita] == target:
            indice_esquerda = hashmap_indices[nums[esquerda]]
            indice_direita = hashmap_indices[nums[direita]]
            return [indice_esquerda.pop(), indice_direita.pop()]
        # Se é menor que o target incrementa o ponteiro esquerda
        elif nums[esquerda] + nums[direita] < target:
            esquerda += 1
        # Se é maior que o target decrementa o ponteiro direita
        elif nums[esquerda] + nums[direita] > target:
            direita -= 1
    return []
# - Complexidade: O(n log n)


# Exemplo 1:
nums_1 = [2, 7, 11, 15]
target_1 = 9
print(twoSum_hash(nums_1, target_1))  # [0, 1]

# Exemplo 2:
nums_2 = [3, 2, 4]
target_2 = 6
print(twoSum_hash(nums_2, target_2))  # [1, 2]

# Exemplo 3:
nums_3 = [3, 3]
target_3 = 6
print(twoSum_hash(nums_3, target_3))  # [1, 0]
