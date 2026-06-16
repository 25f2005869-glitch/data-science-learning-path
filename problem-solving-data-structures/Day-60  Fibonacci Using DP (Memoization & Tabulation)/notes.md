# Day 60 – Fibonacci Using DP (Memoization & Tabulation)

## Objective

The goal of this session is to understand the two major Dynamic Programming approaches:

1. Memoization (Top-Down)
2. Tabulation (Bottom-Up)

using the Fibonacci problem.

---

## Fibonacci Sequence

The Fibonacci sequence is defined as:

F(0) = 0

F(1) = 1

F(n) = F(n−1) + F(n−2)

Example:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...

---

## Problem with Recursion

Recursive Fibonacci repeatedly solves the same subproblems.

Example:

F(5)

├── F(4)
│   ├── F(3)
│   └── F(2)
│
└── F(3)
    ├── F(2)
    └── F(1)

Notice:

- F(3) is calculated multiple times.
- F(2) is calculated multiple times.

This creates unnecessary work.

Time Complexity:

O(2^n)

---

## Memoization (Top-Down)

Memoization stores answers after they are computed.

When the same problem appears again:

Use stored result instead of recomputing.

Process:

Problem
↓
Recursive Call
↓
Store Answer
↓
Reuse Answer

---

## Memoization Example

F(5)

First Computation:

F(4)
F(3)
F(2)

Stored in memory.

Future calls use stored values.

No repeated calculations.

---

## Tabulation (Bottom-Up)

Tabulation starts from base cases.

Builds answers step by step.

Process:

F(0)
↓
F(1)
↓
F(2)
↓
F(3)
↓
...
↓
F(n)

---

## Tabulation Example

For n = 10

dp[0] = 0

dp[1] = 1

dp[2] = 1

dp[3] = 2

dp[4] = 3

dp[5] = 5

...

dp[10] = 55

---

## Comparison

| Feature | Memoization | Tabulation |
|----------|----------|----------|
| Approach | Top-Down | Bottom-Up |
| Uses Recursion | Yes | No |
| Uses Table | Yes | Yes |
| Easy to Write | Yes | Moderate |
| Stack Usage | Yes | No |

---

## Complexity

### Memoization

Time Complexity:

O(n)

Space Complexity:

O(n)

---

### Tabulation

Time Complexity:

O(n)

Space Complexity:

O(n)

---

## Applications

- Fibonacci Numbers
- Climbing Stairs
- Coin Change
- Knapsack Problem
- Longest Common Subsequence
- Dynamic Programming Problems

---

## Key Concepts Learned

- Dynamic Programming
- Memoization
- Tabulation
- State Storage
- Optimization

---

## Summary

Memoization and Tabulation are the two fundamental Dynamic Programming techniques. Both avoid repeated computations and significantly improve efficiency compared to plain recursion.