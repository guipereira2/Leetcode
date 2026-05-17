// 1. Two Sum
//
// Given an array of integers `nums` and an integer `target`, return indices of the
// two numbers such that they add up to `target`.
//
// You may assume that each input would have exactly *one solution*, and you may not
// use the same element twice.
//
// You can return the answer in any order.
//
// Example 1:
// - Input: nums = [2,7,11,15], target = 9
// - Output: [0,1]
// - Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
//
// Example 2:
// - Input: nums = [3,2,4], target = 6
// - Output: [1,2]
//
// Example 3:
// - Input: nums = [3,3], target = 6
// - Output: [0,1]

package main

import "fmt"

// Solução por força bruta
// - Abordagem: Usar força bruta para percorrer todos itens e comparar a soma com o target
func twoSum(nums []int, target int) []int {
	// Cria uma slice para armazenar os índices
	pos := []int{}
	// Percorre a slice usando força bruta comparando todos os valores
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			// Verifica se a soma dos valores corresponde ao target
			if nums[i]+nums[j] == target {
				// Adiciona os índices na slice
				pos = append(pos, i, j)
			}
		}
	}
	return pos
}

// - Complexidade: O(n^2)

func main() {
	// Exemplo 1:
	resultado := twoSum([]int{2, 7, 11, 15}, 9)
	fmt.Println(resultado) // [0 1]
}
