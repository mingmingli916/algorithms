"""
MegaMaid is a robot whose function is to move through a matrix and clean all of its dirty cells. It's positioned in some cell of an  matrix of dirty (d) and clean (-) cells. It can perform five types of operations:

LEFT: Move one cell to the left.
RIGHT: Move one cell to the right.
UP: Move one cell up.
DOWN: Move one cell down.
CLEAN: Clean the cell.
Given the robot's current location and the configuration of dirty and clean cells in the matrix, print the next operation MegaMaid will perform (e.g., UP, CLEAN, etc.) on a new line.

Input Format

The first line contains two space-separated integers describing the respective  (row) and  (column) coordinates of MegaMaid's initial location.
The second line contains two space-separated integers describing the respective height, , and width, , of the matrix.
Each line  of the  subsequent lines contains a string of  characters describing row  in the matrix; each character  describes the character at location  according to the following key:

b denotes MegaMaid's location (in a clean cell).
d denotes a dirty cell.
- denotes a clean cell.
Note: If MegaMaid is initially located in a dirty cell, the cell will be marked with a d (not a b).

Constraints

Output Format

Print the next operation MegaMaid will perform (i.e., LEFT, RIGHT, UP, DOWN, CLEAN). It's important to only print the next operation, because your program will be called iteratively after performing each operation.

Sample Input

0 0
5 5
b---d
-d--d
--dd-
--d--
----d
Sample Output

RIGHT
Explanation

MegaMaid's next move would be to move RIGHT, resulting in the following next state:

-b--d
-d--d
--dd-
--d--
----d
"""


def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy] == 'd':
        print('CLEAN')

    # Get all dirty position.
    lst = []
    for r in range(dimx):
        for c in range(dimy):
            if board[r][c] == 'd':
                lst.append((r, c))

    if lst:
        near_r, near_c = lst[0]
        for r, c in lst:
            if abs(posx - r) + abs(posy - c) < abs(posx - near_r) + abs(posy - near_c):
                near_r = r
                near_c = c
        if near_r > posx:
            print('DOWN')
        elif near_r < posx:
            print('UP')
        elif near_c > posy:
            print('RIGHT')
        elif near_c < posy:
            print('LEFT')


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
