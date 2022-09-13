"""
The game Bot Clean took place in a fully observable environment, i.e., the state of every cell was visible to the bot at all times. Let us consider a variation of it where the environment is partially observable. The bot has the same actuators and sensors. But the sensors visibility is confined to its 8 adjacent cells.

Input Format
The first line contains two space separated integers which indicate the current position of the bot. The board is indexed using Matrix Convention

5 lines follow, representing the grid. Each cell in the grid is represented by any of the following 4 characters:
‘b’ (ascii value 98) indicates the bot’s current position,
‘d’ (ascii value 100) indicates a dirty cell,
‘-‘ (ascii value 45) indicates a clean cell in the grid, and
‘o’ (ascii value 111) indicates the cell that is currently not visible.

Output Format
Output is the action that is taken by the bot in the current step. It can either be any of the movements in 4 directions or the action of cleaning the cell in which it is currently located. Hence the output formats are LEFT, RIGHT, UP, DOWN or CLEAN.

Sample Input

0 0
b-ooo
-dooo
ooooo
ooooo
ooooo
Sample Output

RIGHT
Task
Complete the function next_move that takes in 3 parameters: posr and posc denote the co-ordinates of the bot’s current position, and board denotes the board state, and print the bot’s next move.

Scoring
The goal is to clean all the dirty cells in as few moves as possible. Your score is (200 - #bot moves)/25. All bots in this challenge will be given the same input. CLEAN is also considered a move.

"""


def next_move(posx, posy, board):
    if board[posx][posy] == 'd':
        print('CLEAN')




if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
