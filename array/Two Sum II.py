"""
Given an array of integers numbers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]


Constraints:

2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in increasing order.
-1000 <= target <= 1000
Only one valid answer exists.
"""
from typing import List


# key point: sorted numbers


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, large = 0, len(numbers) - 1

        while small < large:
            target_sum = numbers[small] + numbers[large]
            if target_sum == target:
                return [small + 1, large + 1]
            if target_sum > target:
                large -= 1
            else:
                small += 1


if __name__ == '__main__':
    solution = Solution()

    numbers = [2, 7, 11, 15, 102, 107, 111, 115, 302, 307, 311, 315]
    target = 209
    # numbers = [2, 2, 11, 15]
    # target = 4
    numbers = [-1, 0]
    target = -1

    answer = solution.twoSum(numbers, target)
    print(answer)
    # print(numbers[answer[0] - 1], numbers[answer[1] - 1])
