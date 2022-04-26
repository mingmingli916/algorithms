"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        up = True
        exit_up = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False

            if up:
                if arr[i] < arr[i - 1]:
                    up = False
                else:
                    exit_up = True
            else:
                if arr[i] > arr[i - 1]:
                    return False
        if not up and exit_up:
            return True


if __name__ == '__main__':
    arr = [0, 3, 2, 1]
    solution = Solution()
    solution.validMountainArray(arr)
