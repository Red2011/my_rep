"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"
>>> line = [['o', 'x', 'o'],['x', 'o', 'o'],['o', 'o', 'x']]
>>> print(tic_tac_toe_checker(line))
o wins!
>>> line = [['-', '-', 'o'],['-', 'x', 'o'],['x', 'o', 'x']]
>>> print(tic_tac_toe_checker(line))
draw!
>>> line = [['o', 'x', 'o'],['o', 'x', 'o'],['x', 'o', 'x']]
>>> print(tic_tac_toe_checker(line))
unfinished!

"""
from typing import List


def count_lines(tictac: List[List], player: str) -> bool:
    count_l = 0
    count_c = 0
    lines = [''] * len(tictac)
    for i in range(len(tictac)):
        # creating an empty two-dimensional list
        lines[i] = [''] * len(tictac)
    # create empty lists
    lines_lef = [''] * 3
    lines_rig = [''] * 3
    for i in range(len(tictac)):
        count_un = tictac[i].count(player)
        # check the number of occurrences in the strings of the list
        if count_un > count_l:
            count_l = count_un
        for j in range(len(tictac)):
            # turn columns into rows
            lines[i][j] = tictac[j][i]
            # select the elements of the main diagonal
            lines_lef[i] = tictac[i][i]
            # select the elements of the secondary diagonal
            if j == len(tictac) - 1 - i:
                lines_rig[i] = tictac[i][j]
    for i in range(len(tictac)):
        # find the number of occurrences in rows (previously columns)
        count_un = lines[i].count(player)
        if count_un > count_c:
            count_c = count_un
        # as a result, we return True if the row, column or diagonal is completely filled
    return count_l == len(tictac) or count_c == len(tictac) \
           or lines_lef.count(player) == len(tictac) \
           or lines_rig.count(player) == len(tictac)


def tic_tac_toe_checker(board: List[List]) -> str:
    # check for missing entries
    count = 0
    for i in board:
        count += i.count('-')

    if count_lines(board, 'x'):
        return "x wins!"
    elif count_lines(board, 'o'):
        return "o wins!"
    elif count > 0:
        return "draw!"
    else:
        return "unfinished!"


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
