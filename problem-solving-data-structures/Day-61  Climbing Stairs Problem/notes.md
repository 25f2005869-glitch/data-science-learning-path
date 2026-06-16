# Day 61 – Climbing Stairs Problem

## Objective

The goal of this session is to understand how Dynamic Programming can be used to solve the Climbing Stairs Problem.

---

## Problem Statement

You are climbing a staircase.

Each time you can climb:

- 1 step
- 2 steps

Find the number of distinct ways to reach the top.

---

## Example 1

Number of Steps:

n = 2

Possible Ways:

1. 1 + 1
2. 2

Answer:

2

---

## Example 2

Number of Steps:

n = 3

Possible Ways:

1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1

Answer:

3

---

## Observing the Pattern

For n = 4

Ways to reach step 4:

From Step 3:

ways(3)

plus

From Step 2:

ways(2)

Therefore:

ways(4)

=

ways(3) + ways(2)

---

## Recurrence Relation

ways(n)

=

ways(n−1)

+

ways(n−2)

This is exactly the same recurrence used in the Fibonacci sequence.

---

## Base Cases

ways(1) = 1

ways(2) = 2

---

## Recursive View

For n = 5

ways(5)

=

ways(4)

+

ways(3)

=

5 + 3

=

8

---

## Why Dynamic Programming?

Recursive solution repeatedly computes the same values.

Example:

ways(3)

appears multiple times.

Dynamic Programming stores computed answers and reuses them.

---

## DP Table Example

n = 5

Step 1 → 1 way

Step 2 → 2 ways

Step 3 → 3 ways

Step 4 → 5 ways

Step 5 → 8 ways

---

## Algorithm

1. Handle base cases.
2. Create DP array.
3. Store answers for smaller steps.
4. Build answers iteratively.
5. Return answer for step n.

---

## Time Complexity

O(n)

---

## Space Complexity

O(n)

---

## Optimized Space

Only previous two values are needed.

Space Complexity can be reduced to:

O(1)

---

## Applications

- Dynamic Programming Basics
- Path Counting Problems
- Robot Movement Problems
- Grid Traversal Problems

---

## Key Concepts Learned

- Dynamic Programming
- Fibonacci Pattern
- State Transition
- Recurrence Relation
- Optimization

---

## Summary

The Climbing Stairs Problem is one of the most famous beginner Dynamic Programming problems. It demonstrates how larger solutions can be built using solutions to smaller subproblems.