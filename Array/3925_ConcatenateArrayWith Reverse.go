// 3925. Concatenate Array With Reverse
//
// You are given an integer array nums of length n.
//
// Construct a new array ans of length 2 * n such that the first n elements are
// the same as nums, and the next n elements are the elements of nums in reverse order.
//
// Formally, for 0 <= i <= n - 1:
// - ans[i] = nums[i]
// - ans[i + n] = nums[n - i - 1]
// Return an integer array ans.
//
// Example 1:
// - Input: nums = [1,2,3]
// - Output: [1,2,3,3,2,1]
// - Explanation:
//   The first n elements of ans are the same as nums.
//   For the next n = 3 elements, each element is taken from nums in reverse order:
//   ans[3] = nums[2] = 3, ans[4] = nums[1] = 2, ans[5] = nums[0] = 1
//   Thus, ans = [1, 2, 3, 3, 2, 1].
//
// Example 2:
// - Input: nums = [1]
// - Output: [1,1]
// - Explanation: The array remains the same when reversed. Thus, ans = [1, 1].

package main

import "fmt"

func concatWithReverse(nums []int) []int {
	concat := []int{}
	reverse := []int{}

	for i := len(nums) - 1; i >= 0; i-- {
		reverse = append(reverse, nums[i])
	}

	for _, v := range nums {
		concat = append(concat, v)
	}

	for _, j := range reverse {
		concat = append(concat, j)
	}

	return concat
}

func main() {
	fmt.Println(concatWithReverse([]int{1, 2, 3})) // [1 2 3 3 2 1]
	fmt.Println(concatWithReverse([]int{1}))       // [1 1]
}
