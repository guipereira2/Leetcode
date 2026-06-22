// 2574. Left and Right Sum Differences
//
// You are given a 0-indexed integer array nums of size n.
//
// Define two arrays leftSum and rightSum where:
//
// leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
// rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
// Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
//
// Example 1:
//
// Input: nums = [10,4,8,3]
// Output: [15,1,11,22]
// Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
// The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
//
// Example 2:
//
// Input: nums = [1]
// Output: [0]
// Explanation: The array leftSum is [0] and the array rightSum is [0].
// The array answer is [|0 - 0|] = [0].

package main

import (
	"fmt"
	"slices"
)

func leftRightDifference(nums []int) []int {
	leftSum := []int{}
	rightSum := []int{}
	leftSum = append(leftSum, 0)
	rightSum = append(rightSum, 0)
	left_sum := 0
	right_sum := 0
	sum := make([]int, len(nums))

	for i := range nums {
		if i == len(nums)-1 {
			break
		}
		left_sum = left_sum + nums[i]
		leftSum = append(leftSum, left_sum)
	}

	for i := len(nums) - 1; i >= 1; i-- {
		right_sum = right_sum + nums[i]
		rightSum = append(rightSum, right_sum)
	}
	slices.Sort(rightSum)    // in place
	slices.Reverse(rightSum) // in place

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	for i := range nums {
		sum[i] = abs(leftSum[i] - rightSum[i])
	}

	return sum
}

func main() {
	nums := []int{10, 4, 8, 3}
	result := leftRightDifference(nums)
	fmt.Println(result)
}
