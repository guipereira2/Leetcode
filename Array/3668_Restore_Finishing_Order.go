// 3668. Restore Finishing Order
//
// You are given an integer array order of length n and an integer array friends.
//
// order contains every integer from 1 to n exactly once, representing the IDs
// of the participants of a race in their finishing order.
// friends contains the IDs of your friends in the race sorted in strictly
// increasing order. Each ID in friends is guaranteed to appear in the order array.
//
// Return an array containing your friends' IDs in their finishing order.
//
// Example 1:
// Input: order = [3,1,2,5,4], friends = [1,3,4]
// Output: [3,1,4]
// Explanation: The finishing order is [3, 1, 2, 5, 4].
//   Therefore, the finishing order of your friends is [3, 1, 4].
//
// Example 2:
// Input: order = [1,4,5,3,2], friends = [2,5]
// Output: [5,2]
// Explanation: The finishing order is [1, 4, 5, 3, 2].
//   Therefore, the finishing order of your friends is [5, 2].

package main

import "fmt"

func recoverOrder(order []int, friends []int) []int {
	slice := []int{}
	for _, i := range order {
		for _, j := range friends {
			if i == j {
				slice = append(slice, i)
			}

		}
	}
	return slice
}

func main() {
	fmt.Println(recoverOrder([]int{3, 1, 2, 5, 4}, []int{1, 3, 4})) // [3 1 4]
	fmt.Println(recoverOrder([]int{1, 4, 5, 3, 2}, []int{2, 5}))    // [5 2]
}
