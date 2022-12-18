"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
         Kth largest element is the same as (N – K)th smallest element, where N is the size of the given array.
         Therefore, we can apply the Kth smallest approach to this problem.
        :param nums:
        :param k:
        :return:
        """

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            if left == right:
                return nums[left]

            pivot_index = left
            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)
