"""
You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:

Trim each number in nums to its rightmost trimi digits.
Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
Reset each number in nums to its original length.
Return an array answer of the same length as queries, where answer[i] is the answer to the ith query.

Note:

To trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain.
Strings in nums may contain leading zeros.


Example 1:

Input: nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]
Output: [2,2,1,0]
Explanation:
1. After trimming to the last digit, nums = ["2","3","1","4"]. The smallest number is 1 at index 2.
2. Trimmed to the last 3 digits, nums is unchanged. The 2nd smallest number is 251 at index 2.
3. Trimmed to the last 2 digits, nums = ["02","73","51","14"]. The 4th smallest number is 73.
4. Trimmed to the last 2 digits, the smallest number is 2 at index 0.
   Note that the trimmed number "02" is evaluated as 2.
Example 2:

Input: nums = ["24","37","96","04"], queries = [[2,1],[2,2]]
Output: [3,0]
Explanation:
1. Trimmed to the last digit, nums = ["4","7","6","4"]. The 2nd smallest number is 4 at index 3.
   There are two occurrences of 4, but the one at index 0 is considered smaller than the one at index 3.
2. Trimmed to the last 2 digits, nums is unchanged. The 2nd smallest number is 24.


Constraints:

1 <= nums.length <= 100
1 <= nums[i].length <= 100
nums[i] consists of only digits.
All nums[i].length are equal.
1 <= queries.length <= 100
queries[i].length == 2
1 <= ki <= nums.length
1 <= trimi <= nums[i].length


Follow up: Could you use the Radix Sort Algorithm to solve this problem? What will be the complexity of that solution?

   Hide Hint #1
Run a simulation to follow the requirement of each query.

"""

from typing import List


class Solution:
    class Solution:
        def counting_sort(self, lst: List[int], place_val: int, K: int = 10) -> None:
            """
            Sorts a list of integers where minimum value is 0 and maximum value is K
            """
            # intitialize count array of size K
            counts = [0] * K

            for elem in lst:
                digit = (elem // place_val) % 10
                counts[digit] += 1

            # we now overwrite our original counts with the starting index
            # of each digit over our group of digits
            starting_index = 0
            for i, count in enumerate(counts):
                counts[i] = starting_index
                starting_index += count

            sorted_lst = [0] * len(lst)
            for elem in lst:
                digit = (elem // place_val) % 10
                sorted_lst[counts[digit]] = elem
                # since we have placed an item in index counts[digit],
                # we need to increment counts[digit] index by 1 so the
                # next duplicate digit is placed in appropriate index
                counts[digit] += 1

            # common practice to copy over sorted list into original lst
            # it's fine to just return the sorted_lst at this point as well
            for i in range(len(lst)):
                lst[i] = sorted_lst[i]

        def radix_sort(self, lst: List[int]) -> None:
            # shift the minimum value in lst to be 0
            shift = min(lst)
            lst[:] = [num - shift for num in lst]
            max_elem = max(lst)

            # apply the radix sort algorithm
            place_val = 1
            while place_val <= max_elem:
                self.counting_sort(lst, place_val)
                place_val *= 10

            # undo the original shift
            lst[:] = [num + shift for num in lst]

    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # convert string to number
        nums = [int(i) for i in nums]
