# 2389. Longest Subsequence With Limited Sum
#
# You are given an integer array nums of length n, and an integer array queries of length m.
#
# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
# Example 1:
# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
#
# Example 2:
# Input: nums = [2,3,4,5], queries = [1]
# Output: [0]
# Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        arr_query = []
        arr_result = []
        nums.sort()

        # arr[i] -> arr_query[i]: sum(arr_query) + i <= query AND len(arr_query) < len(nums)? Se sim, append

        while queries:
            query = queries.pop(0)
            arr_query.clear()
            print(f"query: {query}")
            for i in nums:
                if i + sum(arr_query) <= query and len(arr_query) < len(nums):
                    arr_query.append(i)
                    print(arr_query)
            arr_result.append(len(arr_query))

        return arr_result


def main():
    solution = Solution()
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    print(solution.answerQueries(nums, queries))
    nums_ = [2,3,4,5]
    queries_ = [1]
    print(solution.answerQueries(nums_, queries_))


main()
