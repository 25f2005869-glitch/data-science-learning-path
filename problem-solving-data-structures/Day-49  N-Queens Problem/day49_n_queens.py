# ==========================================================
# Author      : Saloni Tiwari
# Topic       : N-Queens Problem
# Day         : 49
# Description : Solving the 4-Queens Problem using
#               Backtracking.
# ==========================================================

N = 4


def is_safe(board, row, col):

    # Check Column
    for i in range(row):

        if board[i][col] == 1:

            return False

    # Check Upper Left Diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:

            return False

        i -= 1
        j -= 1

    # Check Upper Right Diagonal
    i = row
    j = col

    while i >= 0 and j < N:

        if board[i][j] == 1:

            return False

        i -= 1
        j += 1

    return True


def solve(board, row):

    if row == N:

        for r in board:

            print(r)

        return True

    for col in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(board, row + 1):

                return True

            board[row][col] = 0

    return False


board = [[0] * N for _ in range(N)]

print("4-Queens Solution:\n")

solve(board, 0)