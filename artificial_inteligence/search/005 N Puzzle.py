"""
N Puzzle is a sliding blocks game that takes place on a k * k grid with ((k * k) - 1) tiles each numbered from 1 to N. Your task is to reposition the tiles to their proper order.

Input Format

The first line of the input contains an integer k, the size of the square grid. k * k lines follow each line containing an integer I on the tile starting from the top left to bottom right. The empty cell is represented by the number 0.

N = (k * k) -1
0 <= I <= N

Constraints

3 <= k <= 5

Output Format

The first line contains an integer, M, the number of moves your algorithm has taken to solve the N-Puzzle. M lines follow. Each line indicating the movement of the empty cell (0).

A grid is considered solved if it is of the following configuration.

0 1 2
3 4 5
6 7 8
Sample Input

3
0
3
8
4
1
7
2
6
5
Sample Output

70
RIGHT
DOWN
...
...
...
Explanation

The board given as input is

0 3 8
4 1 7
2 6 5
After RIGHT, the board's configuration is

3 0 8
4 1 7
2 6 5
Task

Print all the moves made from the given configuration to the final solved board configuration.

Scoring

On successfully solving the puzzle, your score will be k * k.
"""
import copy


class Node:
    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent
        self.g = self.get_g()
        self.h = self.get_h()
        self.f = self.get_f()
        self.zero = self.get_zero()

    def get_g(self):
        # g score is defined as the sum of g score of the parent node
        # and the cost to travel to that node from it's parent.
        # g(x) = g(x.parent) + cost(x.parent, x)
        if self.parent is None:
            return 0

        return self.parent.g + 1  # change the position of 0, this is the cost of 1.

    def get_h(self):
        # h is the calculated heuristic of current node
        # Here we use Manhattan heuristic.
        # Add all different positioned number manhattan distances.
        h = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    continue
                if (i, j) == goal_d[self.grid[i][j]]:
                    continue
                h += abs(i - goal_d[self.grid[i][j]][0]) + abs(j - goal_d[self.grid[i][j]][1])
        return h

    def get_f(self):
        # f = g + h
        return self.g + self.h

    def get_zero(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    return i, j

    def __eq__(self, other):
        if self.grid == other.grid:
            return True
        return False

    def __str__(self):
        return self.grid

    def __hash__(self):
        s = []
        for i in self.grid:
            for j in i:
                s.append(str(j))
        return hash(''.join(s))


def get_min(lst):
    index = 0
    for i in range(1, len(lst)):
        if lst[i].f < lst[index].f:
            index = i
    return index


def a_star(init_grid, goal_grid):
    source_node = Node(init_grid, None)
    queue = [source_node]
    visited = set()
    direction = [[-1, 0], [0, -1], [0, 1], [1, 0]]

    while queue:
        index = get_min(queue)
        node = queue.pop(index)
        visited.add(node)
        rows = len(node.grid)
        cols = len(node.grid[0])
        if node.grid == goal_grid:
            return node
        zx, zy = node.zero
        for x, y in direction:
            nx, ny = zx + x, zy + y
            # Out of range.
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            new_grid = copy.deepcopy(node.grid)
            new_grid[zx][zy], new_grid[nx][ny] = new_grid[nx][ny], new_grid[zx][zy]
            new_node = Node(new_grid, node)
            if new_node not in visited:
                visited.add(new_node)
                queue.append(new_node)


def get_direction(pt1, pt2):
    if pt1[0] > pt2[0]:
        return 'DOWN'
    if pt1[0] < pt2[0]:
        return 'UP'
    if pt1[1] > pt2[1]:
        return 'RIGHT'
    if pt1[1] < pt2[1]:
        return 'LEFT'


def get_route(node):
    route = []
    while node.parent is not None:
        route.append(get_direction(node.zero, node.parent.zero))
        node = node.parent
    return route[::-1]


if __name__ == '__main__':
    k = int(input())
    grid = []
    for i in range(k):
        row = []
        for j in range(k):
            ele = int(input())
            row.append(ele)
        grid.append(row)

    goal_grid = []
    count = 0
    for i in range(k):
        row = []
        for j in range(k):
            row.append(count)
            count += 1
        goal_grid.append(row)

    goal_d = {}
    for i in range(len(goal_grid)):
        for j in range(len(goal_grid[i])):
            goal_d[goal_grid[i][j]] = (i, j)
    node = a_star(grid, goal_grid)
    route = get_route(node)
    print(len(route))
    for _ in route:
        print(_)
