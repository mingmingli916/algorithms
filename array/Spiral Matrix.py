"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Hide Hint #1
Well for some problems, the best way really is to come up with some algorithms for simulation.
Basically, you need to simulate what the problem asks us to do.

Hide Hint #2
We go boundary by boundary and move inwards. That is the essential operation.
First row, last column, last row, first column and then we move inwards by 1 and then repeat.
That's all, that is all the simulation that we need.

Hide Hint #3
Think about when you want to switch the progress on one of the indexes. If you progress on
i
out of
[i, j]
, you'd be shifting in the same column. Similarly, by changing values for
j
, you'd be shifting in the same row.
Also, keep track of the end of a boundary so that you can move inwards and then keep repeating.
It's always best to run the simulation on edge cases like a single column or a single row to see
if anything breaks or not.
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        last_row = len(matrix) - 1
        last_col = len(matrix[0]) - 1

        row = 0
        col = last_col

        # There is a circle to iterate.
        while 2 * row < last_row and 2 * col > last_col:
            # From left to right.
            for j in range(last_col - col, col + 1):
                result.append(matrix[row][j])
            # From top to down.
            for i in range(row + 1, last_row - row + 1):
                result.append(matrix[i][col])
            # From right to left.
            for j in range(col - 1, last_col - col - 1, -1):
                result.append(matrix[last_row - row][j])
            # From down to top.
            for i in range(last_row - row - 1, row, -1):
                result.append(matrix[i][last_col - col])
            # Begin the inner circle iterate.
            row += 1
            col -= 1

        # This is the situation like one row.
        if 2 * row == last_row:
            # From left to right.
            for j in range(last_col - col, col + 1):
                result.append(matrix[row][j])
        # This is the situation like one column.
        elif 2 * col == last_col:
            for i in range(row, last_row - row + 1):
                result.append(matrix[i][col])

        return result


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expect = [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # expect = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    matrix = [[5]]
    expect = [5]

    matrix = [[5, 6, 7]]
    expect = [5, 6, 7]

    # matrix = [[1], [2], [3]]
    # expect = [1, 2, 3]

    # matrix = [[1, 2], [3, 4]]
    # expect = [1, 2, 4, 3]
    result = solution.spiralOrder(matrix)
    print(result, expect, sep='\n')
