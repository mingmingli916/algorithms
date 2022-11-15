"""
Maze Escape is a popular 1 player game where a bot is trapped in a maze and is expected to find its way out.
In this version of the game, 2 bots whose positions are not visible to each other are placed at random points
in the maze. the first bot to find its way out of the maze wins the game.

The visibility of the bot is restricted to its 8 adjacent cells as shown in the figure below

---
-b-
---
where b is the bot. Bots can be facing any of the 4 directions. To make this game more interesting,
the orientation of both the bots are randomly chosen at the start of the game and the map visible to them also changes
according to the orientation.

If the actual map is as shown below,

#######
#--#-b#
#--#--#
#--#--#
e-----#
#-----#
#######
and your bot is positioned at (1,5) and is facing the RIGHT side of the maze, the input will be

###
#b-
#--
If your bot is facing UP, your input will be

###
-b#
--#
If your bot is facing LEFT, your input will be

--#
-b#
###
And if your bot is facing DOWN, your input will be

#--
#b-
###
It is to be noted that your bot faces the direction in which it chooses to make its next move.

Input Format

The walls are represented by character # ( ascii value 35), empty cells are represented by - (ascii value 45),
the maze door which is the indication of the way out is represented by e (ascii value 101)

The input contains 4 lines, the first line being the player id (1 or 2) and followed by 3 lines,
each line containing 3 of the above mentioned characters which represents the 8 adjacent cells of the bot.
The visible maze given as input always has the bot at the center.

Constraints

5 <= r,c <= 30 where r, c is the number of rows and columns of the maze.

Output Format

Output UP, DOWN, LEFT or RIGHT which is the next move of the bot.

Sample Input

1
###
#--
#--
Sample Output

RIGHT
Explanation

Considering the maze given above. If the input is as given below with the bot initially facing the RIGHT side
of the maze, if the bot chooses to go RIGHT, the new position of the bot in the maze would be

#######
#--#--#
#--#-b#
#--#--#
e-----#
#-----#
#######
The bot moves 1 step DOWN w.r.t the maze. As the bot is facing DOWN side of the maze, his next input would be

#--
#--
#--
with the bot at the center.

Timelimits

Timelimits for each move is given here
"""
import pickle

# 5 <= r,c <= 30 where r, c is the number of rows and columns of the maze.
# Use a large memory where the first bot is position in the center.
rows, cols = 61, 61

# full board with non visibility.
board = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append('o')
    board.append(row)


def save_board(board, player):
    """
    Save board to memory according to the player.
    :param board:
    :param player:
    :return:
    """
    filename = f'maze_memory_player{player}.pk'
    with open(filename, 'wb') as fh:
        pickle.dump(board, fh)


def load_board(player):
    """
    Load board from memory according to player.
    :param player:
    :return:
    """
    filename = f'maze_memory_player{player}.pk'
    with open(filename, 'rb') as fh:
        return pickle.load(fh)


def save_pre_pos(pos, player):
    """
    Save previous position.
    :param pos:
    :param player:
    :return:
    """
    filename = f'pos_player{player}.pk'
    with open(filename, 'wb') as fh:
        pickle.dump(pos, fh)


def load_pre_pos(player):
    """
    Load previous position.
    :param player:
    :return:
    """
    filename = f'pos_player{player}.pk'
    with open(filename, 'rb') as fh:
        pos = pickle.load(fh)
        return pos


if __name__ == '__main__':

    player = int(input())
    visible = []
    for _ in range(3):
        visible.append(list(input()))
    print(visible)

    save_board(visible, player)
    print(load_board(player))
