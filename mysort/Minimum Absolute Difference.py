"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]


Constraints:

2 <= arr.length <= 105
-106 <= arr[i] <= 106
   Hide Hint #1
Find the minimum absolute difference between two elements in the array.
   Hide Hint #2
The minimum absolute difference must be a difference between two consecutive elements in the sorted array.

"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        self.counting_sort(arr)
        min_dis = max(arr)
        for i in range(1, len(arr)):
            if 0 < arr[i] - arr[i - 1] < min_dis:
                min_dis = arr[i] - arr[i - 1]
        lst = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_dis:
                lst.append([arr[i - 1], arr[i]])
        return lst

    def counting_sort(self, lst: List[int]) -> None:
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
    nums = [1, 3, 6, 10, 15]
    solution = Solution()
    ans = solution.minimumAbsDifference(nums)
    print(ans)
