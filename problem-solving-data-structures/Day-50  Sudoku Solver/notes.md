Day 50 – Sudoku Solver
Objective

The goal of this session is to understand how Backtracking can be used to solve a Sudoku puzzle.

What is Sudoku?

Sudoku is a logic-based puzzle played on a:

9 × 9 Grid

The objective is to fill empty cells so that:

Every row contains numbers 1–9.
Every column contains numbers 1–9.
Every 3 × 3 subgrid contains numbers 1–9.
Example Sudoku Board
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .

---------------------

8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6

---------------------

. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

. represents an empty cell.

Why Backtracking?

For every empty cell:

Try Numbers 1 → 9

If a number satisfies Sudoku rules:

Place Number

Move to the next empty cell.

If no valid number exists:

Backtrack

Remove the previously placed number and try another option.

Sudoku Rules Check

Before placing a number:

Check Row
Number must not already exist in the row.
Check Column
Number must not already exist in the column.
Check 3 × 3 Box
Number must not already exist inside the box.
Example

Trying to place:

5

at position:

(row = 0, col = 2)

Check:

Row ✔

Column ✔

Box ✔

Safe Position ✅

Backtracking Strategy
Find an empty cell.
Try digits 1–9.
If valid:
Place digit.
Solve remaining board.
If solution fails:
Remove digit.
Try next digit.
Continue until board is complete.
Pseudocode
SOLVE(board)

Find Empty Cell

IF no empty cell

    RETURN True

FOR num = 1 to 9

    IF safe

        Place num

        IF SOLVE(board)

            RETURN True

        Remove num

RETURN False
Applications
Puzzle Solving
Artificial Intelligence
Constraint Satisfaction Problems
Scheduling Systems
Search Algorithms
Time Complexity

Worst Case:

O(9^(n))

where:

n = Number of Empty Cells
Space Complexity
O(n)

for recursion stack.

Key Concepts Learned
Sudoku
Constraint Satisfaction
Backtracking
Recursive Search
Safe Placement
Summary

Sudoku Solver is a classic Backtracking application where numbers are placed one by one while maintaining all Sudoku constraints.