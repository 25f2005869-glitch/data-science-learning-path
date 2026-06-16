# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Sudoku Solver
# Day         : 50
# Description : Solving Sudoku using Backtracking.
# ==========================================================

board = [

    [5, 3, 0, 0, 7, 0, 0, 0, 0],

    [6, 0, 0, 1, 9, 5, 0, 0, 0],

    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],

    [4, 0, 0, 8, 0, 3, 0, 0, 1],

    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],

    [0, 0, 0, 4, 1, 9, 0, 0, 5],

    [0, 0, 0, 0, 8, 0, 0, 7, 9]

]


def find_empty():

    for row in range(9):

        for col in range(9):

            if board[row][col] == 0:

                return row, col

    return None


def is_safe(row, col, num):

    # Row Check
    if num in board[row]:

        return False

    # Column Check
    for i in range(9):

        if board[i][col] == num:

            return False

    # 3x3 Box Check
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):

        for j in range(start_col, start_col + 3):

            if board[i][j] == num:

                return False

    return True


def solve():

    empty = find_empty()

    if not empty:

        return True

    row, col = empty

    for num in range(1, 10):

        if is_safe(row, col, num):

            board[row][col] = num

            if solve():

                return True

            board[row][col] = 0

    return False


if solve():

    print("Solved Sudoku:\n")

    for row in board:

        print(row)

else:

    print("No Solution Exists")