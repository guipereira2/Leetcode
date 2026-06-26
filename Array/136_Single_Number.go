// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
// You must implement a solution with a linear runtime complexity and use only constant extra space.

// Example 1:
// Input: nums = [2,2,1]
// Output: 1

// Example 2:
// Input: nums = [4,1,2,1,2]
// Output: 4

// Example 3:
// Input: nums = [1]
// Output: 1

package main

import (
	"fmt"
	"sort"
)

func singleNumber(nums []int) int {
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i += 2 {
		fmt.Printf("i: %d i+1: %d \n", nums[i], nums[i+1])
		if nums[i] != nums[i+1] {
			return nums[i]
		}
	}
	return nums[len(nums)-1]
}

func main() {
	fmt.Println(singleNumber([]int{2, 2, 1}))       // Expected output: 1
	fmt.Println(singleNumber([]int{4, 1, 2, 1, 2})) // Expected output: 4
}
