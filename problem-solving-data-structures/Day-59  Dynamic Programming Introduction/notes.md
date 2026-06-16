# Day 59 – Dynamic Programming Introduction

## Objective

The goal of this session is to understand Dynamic Programming (DP), one of the most important problem-solving techniques in computer science.

---

## What is Dynamic Programming?

Dynamic Programming (DP) is an optimization technique used to solve problems by breaking them into smaller overlapping subproblems.

Instead of solving the same subproblem repeatedly, DP stores previously computed results and reuses them.

---

## Why Dynamic Programming?

Consider Fibonacci Numbers.

F(5)

F(5)
├── F(4)
│   ├── F(3)
│   └── F(2)
│
└── F(3)
    ├── F(2)
    └── F(1)

Notice:

- F(3) appears multiple times
- F(2) appears multiple times

Repeated calculations waste time.

Dynamic Programming solves each subproblem only once.

---

## Two Important Properties

### 1. Overlapping Subproblems

The same subproblem appears repeatedly.

Example:

- F(3)
- F(2)

appear many times in Fibonacci recursion.

---

### 2. Optimal Substructure

The optimal solution can be built from optimal solutions of smaller subproblems.

Example:

F(n) = F(n−1) + F(n−2)

---

## Approaches in Dynamic Programming

### Memoization (Top-Down)

Uses recursion.

Stores answers after computation.

Process:

Problem
↓
Recursive Calls
↓
Store Result

---

### Tabulation (Bottom-Up)

Starts from smallest subproblems.

Builds solution step by step.

Process:

Base Cases
↓
Small Problems
↓
Large Problems

---

## Fibonacci Example

Base Cases:

F(0) = 0

F(1) = 1

Recurrence Relation:

F(n) = F(n−1) + F(n−2)

---

## Complexity Comparison

Without Dynamic Programming:

Time Complexity:

O(2^n)

With Dynamic Programming:

Time Complexity:

O(n)

---

## Applications of Dynamic Programming

### Optimization Problems

- Knapsack Problem
- Matrix Chain Multiplication

### Sequence Problems

- Longest Common Subsequence
- Longest Increasing Subsequence

### Graph Problems

- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm

### Counting Problems

- Fibonacci Numbers
- Climbing Stairs

---

## Steps to Solve DP Problems

1. Identify the subproblems.
2. Find the recurrence relation.
3. Define base cases.
4. Store computed results.
5. Build the final solution.

---

## Time Complexity

Depends on the number of unique states.

Common examples:

- O(n)
- O(n²)
- O(n³)

---

## Space Complexity

Usually:

O(n)

Depends on the number of stored states.

---

## Key Concepts Learned

- Dynamic Programming
- Overlapping Subproblems
- Optimal Substructure
- Memoization
- Tabulation
- State Storage

---

## Summary

Dynamic Programming is a technique used to avoid repeated computations by storing solutions of smaller subproblems and reusing them whenever needed. It transforms many exponential-time recursive solutions into efficient polynomial-time solutions.