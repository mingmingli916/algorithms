"""
Given a list of daily temperatures T, return a list such that, f
or each day in the input, tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        # init
        # Store temperatures and it's index.
        stack = [(temperatures[length - 1], length - 1)]
        temperatures[length - 1] = 0

        for i in range(length - 2, -1, -1):
            if temperatures[i] < stack[-1][0]:
                stack.append((temperatures[i], i))
                # Because the last put element is the nearest.
                temperatures[i] = 1
                continue
            # Only need to store the nearest maximum elements.
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            value = temperatures[i]  # avoid value overwrite
            if not stack:
                temperatures[i] = 0
            else:
                temperatures[i] = stack[-1][1] - i
            stack.append((value, i))

        return temperatures


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    T = [73, 74, 75, 71, 69, 72, 76, 73, 100, 100, 100, 30, 100, 50, 30]

    s = Solution()
    r = s.dailyTemperatures(T)
    print(r)
