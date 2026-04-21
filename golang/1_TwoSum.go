package main

import "fmt"

func twoSum(nums []int, target int) []int {
	pos := []int{}
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				pos = append(pos, i, j)
			}
		}
	}
	return pos
}

func main() {
	resultado := twoSum([]int{2, 7, 11, 15}, 9)
	fmt.Println(resultado)
}
