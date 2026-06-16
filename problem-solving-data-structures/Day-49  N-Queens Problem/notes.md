📘 Day 49 – N-Queens Problem
notes.md
Day 49 – N-Queens Problem
Objective

The goal of this session is to understand the N-Queens Problem and solve it using Backtracking.

What is the N-Queens Problem?

The N-Queens Problem asks:

Place N queens on an N × N chessboard

such that:

No two queens are in the same row.
No two queens are in the same column.
No two queens are on the same diagonal.
4-Queens Example

Board Size:

4 × 4

Goal:

Place 4 Queens Safely
Invalid Placement
Q . . .
. Q . .
. . Q .
. . . Q

Problem:

Queens attack diagonally.

❌ Invalid

Valid Placement
. Q . .

. . . Q

Q . . .

. . Q .

No queens attack each other.

✅ Valid

Why Backtracking?

For every row:

Try a column

If placement is safe:

Move to next row

If placement becomes invalid:

Backtrack

and try another column.

Backtracking Strategy
Place queen in current row.
Check if position is safe.
If safe:
Move to next row.
If not safe:
Try another column.
If no column works:
Backtrack.
Safe Position Check

Before placing a queen:

Check:

Same Column
↑
Upper Left Diagonal
↖
Upper Right Diagonal
↗

If none contain a queen:

Safe Position
Example Solution
. Q . .

. . . Q

Q . . .

. . Q .

Coordinates:

(0,1)

(1,3)

(2,0)

(3,2)
Pseudocode
SOLVE(row)

IF row == N

    PRINT solution

    RETURN

FOR each column

    IF position safe

        Place Queen

        SOLVE(row + 1)

        Remove Queen
Applications
Constraint Satisfaction Problems
Scheduling Problems
Artificial Intelligence
Puzzle Solving
Search Algorithms
Time Complexity

Worst Case:

O(N!)

because many arrangements must be explored.

Space Complexity
O(N)

for recursion stack.

Key Concepts Learned
N-Queens
Chessboard Constraints
Safe Position
Backtracking
Recursive Search
Summary

The N-Queens Problem is a classic Backtracking problem where queens are placed one row at a time while ensuring that no two queens attack each other.