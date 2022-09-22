"""
Target Sum

Solution
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        def helper(nums, target):
            nonlocal count
            if len(nums) > 1:
                helper(nums[1:], target + nums[0])
                helper(nums[1:], target - nums[0])
            else:
                if nums[0] == target:
                    count += 1
                if nums[0] == -target:
                    count += 1

        helper(nums, target)
        return count


class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # TODO
        s = sum(nums)
        # If `s` is odd, `target` must be odd.
        # If there are even odd or even numbers, the result must be even number.
        # If there are odd odd numbers, the result must be odd number.
        if s < abs(target) or (s + target) % 2:
            return 0
        #
        a = (s + target) // 2
        dp = [0] * (a + 1)
        # Because the program skip the if condition,
        # there are at least on solution, initialize it to dp[0].
        dp[0] = 1
        for n in nums:
            for i in range(a, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[-1]


if __name__ == '__main__':
    nums = [35, 25, 24, 23, 2, 47, 39, 22, 3, 7, 11, 26, 6, 30, 5, 34, 10, 43, 41, 28]
    S = 49
    s = Solution2()
    nums = [1, 2, 3]
    S = 0
    count = s.findTargetSumWays(nums, S)
    print(count)
