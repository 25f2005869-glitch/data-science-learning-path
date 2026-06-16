# Day 66 – Matrix Chain Multiplication (MCM)

## Objective

The goal of this session is to understand the Matrix Chain Multiplication (MCM) problem and solve it using Dynamic Programming.

---

## What is Matrix Chain Multiplication?

Matrix Chain Multiplication is an optimization problem.

Given a sequence of matrices:

A₁ × A₂ × A₃ × ... × Aₙ

The objective is:

Find the most efficient order of multiplication.

---

## Important Note

Matrix multiplication is associative.

Example:

(A × B) × C

=

A × (B × C)

Both produce the same result.

However:

Number of operations may be different.

---

## Matrix Multiplication Cost

If:

A = p × q

B = q × r

Then:

A × B

requires:

p × q × r

multiplications.

---

## Example

Three matrices:

A = 10 × 30

B = 30 × 5

C = 5 × 60

---

## Option 1

(A × B) × C

Step 1:

A × B

Cost:

10 × 30 × 5

= 1500

Result Matrix:

10 × 5

---

Step 2:

(AB) × C

Cost:

10 × 5 × 60

= 3000

---

Total Cost:

1500 + 3000

= 4500

---

## Option 2

A × (B × C)

Step 1:

B × C

Cost:

30 × 5 × 60

= 9000

Result Matrix:

30 × 60

---

Step 2:

A × (BC)

Cost:

10 × 30 × 60

= 18000

---

Total Cost:

9000 + 18000

= 27000

---

## Best Choice

(A × B) × C

Cost:

4500

✅ Minimum

---

## Why Dynamic Programming?

For large matrix chains:

Many subproblems repeat.

Dynamic Programming stores previously computed costs and avoids recomputation.

---

## Key Idea

Try every possible split.

Choose the split with minimum cost.

---

## Recurrence Relation

Let:

dp[i][j]

=

Minimum cost of multiplying matrices from i to j.

For every split k:

Cost

=

dp[i][k]

+

dp[k+1][j]

+

(matrix multiplication cost)

Take the minimum among all possible splits.

---

## Algorithm

1. Create DP table.
2. Start with chains of length 2.
3. Compute minimum cost for larger chains.
4. Store results.
5. Return dp[1][n].

---

## Applications

### Compiler Optimization

Optimize expression evaluation.

### Scientific Computing

Efficient matrix operations.

### Graphics Processing

Transformation calculations.

### Machine Learning

Large matrix computations.

---

## Time Complexity

O(n³)

---

## Space Complexity

O(n²)

---

## Key Concepts Learned

- Matrix Chain Multiplication
- Dynamic Programming
- Optimization Problem
- Interval DP
- Parenthesization

---

## Summary

Matrix Chain Multiplication is a classic Dynamic Programming problem where the goal is to determine the most efficient order of matrix multiplication to minimize computation cost.