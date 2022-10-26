"""
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.



Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109
   Hide Hint #1
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
   Hide Hint #2
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.
"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if len(nums) < 2 or indexDiff <= 0 or valueDiff < 0:
            return False

        width = valueDiff + 1
        bucket = dict()

        for i, num in enumerate(nums):
            id = self.get_id(num, width)
            if id in bucket:
                return True
            if id - 1 in bucket and abs(num - bucket[id - 1]) <= valueDiff:
                return True
            if id + 1 in bucket and abs(num - bucket[id + 1]) <= valueDiff:
                return True
            bucket[id] = num

            if i >= indexDiff:  # This ensure the requirement: abs(i - j) <= k
                del bucket[self.get_id(nums[i - indexDiff], width)]
        return False

    def get_id(self, num, width) -> int:
        return num // width


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    # True

    # nums = [1, 0, 1, 1]
    # k = 1
    # t = 2

    # nums = [1, 5, 9, 12, 13, 15]
    # k = 3
    # t = 3

    # nums = [1, 5, 9, 1, 5, 9]
    # k = 2
    # t = 3
    # False

    # nums = [-1, 2]
    # k = 2
    # t = 3
    # True

    # nums = [-3, 3]
    # k = 2
    # t = 4
    # False

    ans = solution.containsNearbyAlmostDuplicate(nums, k, t)
    print(ans)
