package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	merged := []int{}

	for i := 0; i < m; i++ {
		merged = append(merged, nums1[i])
	}
	for j := 0; j < n; j++ {
		merged = append(merged, nums2[j])
	}

	for k := 0; k < m+n; k++ {
		for l := k + 1; l < m+n; l++ {
			if merged[k] > merged[l] {
				temp := merged[k]
				merged[k] = merged[l]
				merged[l] = temp
			}
		}
	}

	copy(nums1, merged)
	fmt.Println(merged)
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	merge(nums1, 3, nums2, 3)
}
