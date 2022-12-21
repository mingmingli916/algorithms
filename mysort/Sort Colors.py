"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?

   Hide Hint #1
A rather straight forward solution is a two-pass algorithm using counting sort.
   Hide Hint #2
Iterate the array counting number of 0's, 1's, and 2's.
   Hide Hint #3
Overwrite array with the total number of 0's, then 1's and followed by 2's.
"""
from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        idx = 0
        for i in range(3):
            for j in range(counter[i]):
                nums[idx] = i
                idx += 1

    def sortColors2(self, lst: List[int]) -> None:
        """
        Sorts a list of integers (handles shifting of integers to range 0 to K)
        """
        shift = min(lst)
        K = max(lst) - shift
        counts = [0] * (K + 1)
        for elem in lst:
            counts[elem - shift] += 1

        # we now overwrite our original counts with the starting index
        # of each element in the final sorted array
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            sorted_lst[counts[elem - shift]] = elem
            # since we have placed an item in index counts[elem], we need to
            # increment counts[elem] index by 1 so the next duplicate element
            # is placed in appropriate index
            counts[elem - shift] += 1

        # common practice to copy over sorted list into original lst
        # it's fine to just return the sorted_lst at this point as well
        for i in range(len(lst)):
            lst[i] = sorted_lst[i]
        return lst


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    print(nums)
