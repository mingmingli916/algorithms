"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.


Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_max = 0  # storing maximum in this window
        global_max = 0  # storing maximum in the array
        for i in nums:
            if i == 1:
                window_max += 1  # window starts or continues
            else:  # window stop
                if window_max > global_max:
                    global_max = window_max
                window_max = 0
        return max(global_max, window_max)
