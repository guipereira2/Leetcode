// 3895. Count Digit Appearances
// You are given an integer array nums and an integer digit.
// Return the total number of times digit appears in the decimal representation of all elements in nums.
//
// Example 1:
// Input: nums = [12,54,32,22], digit = 2
// Output: 4
// Explanation:
// The digit 2 appears once in 12 and 32, and twice in 22. Thus, the total number of times digit 2 appears is 4.
//
// Example 2:
// Input: nums = [1,34,7], digit = 9
// Output: 0
// Explanation:
// The digit 9 does not appear in the decimal representation of any element in nums, so the total number of times digit 9 appears is 0.

package main

import (
	"fmt"
	"strings"
)

func countDigitOccurrences(nums []int, digit int) int {
	counter := 0
	digit_string := fmt.Sprintf("%d", digit)
	nums_string := make([]string, len(nums))
	for i, v := range nums {
		nums_string[i] = fmt.Sprintf("%d", v)
	}

	for _, v := range nums_string {
		for _, splited := range strings.Split(v, "") {
			if splited == digit_string {
				counter++
			}
		}
	}

	return counter
}

func main() {
	fmt.Println(countDigitOccurrences([]int{12, 54, 32, 22}, 2)) // 4
	fmt.Println(countDigitOccurrences([]int{1, 34, 7}, 9))       // 0
}
