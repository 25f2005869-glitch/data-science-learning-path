📘 Day 48 – Recursion Backtracking
notes.md
Day 48 – Recursion Backtracking
Objective

The goal of this session is to understand Backtracking, a powerful problem-solving technique built on recursion.

What is Backtracking?

Backtracking is an algorithmic technique that:

Try → Explore → Undo → Try Again

It builds a solution step by step and abandons a path as soon as it determines that the path cannot lead to a valid solution.

Relationship with Recursion

Backtracking is an extension of recursion.

Recursion:

Function calls itself

Backtracking:

Recursion + Undo Choices
Simple Example

Suppose you want to move through a maze.

Possible moves:

Right
Down
Left
Up

If a move leads to a dead end:

Go Back

and try another path.

This process is called:

Backtracking
General Strategy
Choose an option.
Explore recursively.
If solution found → Stop.
If solution fails → Undo choice.
Try next option.
Backtracking Tree

Example:

          Start
         /     \
        A       B
       / \     / \
      C   D   E   F

If path:

Start → A → C

fails,

Backtrack to:

A

Then try:

A → D
Template
BACKTRACK(solution)

IF solution complete

    PRINT solution

    RETURN

FOR each choice

    Make Choice

    BACKTRACK(solution)

    Undo Choice
Example: Generate Numbers

Choices:

1
2
3

Possible outputs:

123

132

213

231

312

321

Backtracking explores every possibility.

Applications
N-Queens Problem

Place queens safely on a chessboard.

Sudoku Solver

Fill cells while satisfying constraints.

Maze Solving

Find a path from start to destination.

Permutations

Generate all possible arrangements.

Subsets

Generate all possible subsets.

Time Complexity

Depends on number of choices.

Commonly:

O(bⁿ)

Where:

b = branching factor

n = depth
Space Complexity

Recursion Stack:

O(n)
Recursion vs Backtracking
Feature	Recursion	Backtracking
Self Calls	✅	✅
Undo Choice	❌	✅
Explore Alternatives	❌	✅
Search Space Problems	❌	✅
Key Concepts Learned
Recursion
Backtracking
Decision Tree
Undo Choice
Search Space
Recursive Exploration
Summary

Backtracking is a recursive technique that explores all possible solutions by making choices, exploring them, and undoing them when necessary.