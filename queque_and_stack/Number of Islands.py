"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        columns = len(grid)
        rows = len(grid[0])
        count = 0

        q = collections.deque()
        d = collections.defaultdict(int)

        # store all 1s in dictionary
        for row in range(rows):
            for column in range(columns):
                if grid[column][row] == '1':
                    d[(row, column)] = 1

        # there is some elements in d
        while d:
            # Get one element randomly in d
            root = tuple(d.keys())[0]
            q.append(root)
            count += 1
            # Remove all the neighboring root
            while q:
                node = q.popleft()
                for i in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    n_r = node[0] + i[0]
                    n_c = node[1] + i[1]
                    if 0 <= n_r <= rows - 1 and 0 <= n_c <= columns - 1 and d.get((n_r, n_c), 0) == 1:
                        q.append((n_r, n_c))
                        d.pop((n_r, n_c))
                if d.get(node, 0) == 1:
                    d.pop(node)
        return count

    def numIslandsDFS(self, grid):
        columns = len(grid)
        rows = len(grid[0])
        s = set()
        for i in range(rows):
            for j in range(columns):
                if grid[j][i] == '1':
                    s.add((j, i))

        def helper(node, s):
            s.remove(node)
            for c, r in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nc = node[0] + c
                nr = node[1] + r
                if 0 <= nr <= rows - 1 and 0 <= nc <= columns - 1 and (nc, nr) in s:
                    helper((nc, nr), s)

        count = 0
        while s:
            count += 1
            node = s.pop()
            s.add(node)
            helper(node, s)

        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grid = [["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
            ["0", "1", "0", "1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "1", "0", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]

    sol = Solution()
    num = sol.numIslands(grid)
    print(num)
