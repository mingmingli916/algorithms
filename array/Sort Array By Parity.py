"""
Given an array A of non-negative integers,
return an array consisting of all the even elements of A,
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        Move odd number to last.
        :param A:
        :return:
        """
        length = len(A)
        i = 0
        last = length - 1
        while i < last:  # termination condition
            if A[i] % 2 == 1:  # odd
                if A[last] % 2 == 0:  # even
                    tmp = A[last]
                    A[last] = A[i]
                    A[i] = tmp
                    last -= 1
                    i += 1
                else:
                    last -= 1
            else:
                i += 1
        return A
