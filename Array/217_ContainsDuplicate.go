// 217. Contains Duplicate
//
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
//
// Example 1:
// - Input: nums = [1,2,3,1]
// - Output: true
// - The element 1 occurs at the indices 0 and 3.
//
// Example 2:
// - Input: nums = [1,2,3,4]
// - Output: false
// - All elements are distinct.
//
// Example 3:
// - Input: nums = [1,1,1,3,3,4,3,2,4,2]
// - Output: true

package main

import (
	"fmt"
	"sort"
)

func containsDuplicate(nums []int) bool {
	if len(nums) == 0 || len(nums) == 1 {
		return false
	}
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))                   // true
	fmt.Println(containsDuplicate([]int{1, 2, 3, 4}))                   // false
	fmt.Println(containsDuplicate([]int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2})) // true
	fmt.Println(containsDuplicate([]int{2, 14, 18, 22, 22}))            // true
}
