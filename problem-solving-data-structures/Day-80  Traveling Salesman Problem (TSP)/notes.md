# Day 80 – Traveling Salesman Problem (TSP)

## Objective

The goal of this session is to understand the Traveling Salesman Problem (TSP) and solve it using Bitmask Dynamic Programming.

---

## What is the Traveling Salesman Problem?

A salesman must:

1. Visit every city exactly once.
2. Return to the starting city.
3. Minimize the total travel cost.

The objective is:

Find the Minimum Possible Tour Cost.

---

## Example

Cities:

A, B, C, D

Distance Matrix:

      A  B  C  D

A     0 10 15 20

B    10  0 35 25

C    15 35  0 30

D    20 25 30  0

---

## Possible Tour

A → B → C → D → A

Cost:

10 + 35 + 30 + 20

=

95

---

## Better Tour

A → B → D → C → A

Cost:

10 + 25 + 30 + 15

=

80

✅ Better

---

## Why Is TSP Difficult?

For:

n cities

Total Possible Tours:

(n − 1)!

Example:

4 Cities:

3!

=

6 Tours

---

10 Cities:

9!

=

362,880 Tours

---

20 Cities:

19!

Very Large

Brute Force becomes impractical.

---

## Bitmask DP Solution

Represent visited cities using a bitmask.

Example:

Cities:

A B C D

Mask:

1101

Meaning:

A Visited

B Not Visited

C Visited

D Visited

---

## DP State

dp[mask][city]

Meaning:

Minimum cost to visit all cities in mask and finish at city.

---

## State Transition

Current City:

i

Try visiting:

j

If city j is not visited:

New Mask:

mask | (1 << j)

Update:

dp[new_mask][j]

---

## Example

Cities:

A B C

Masks:

000

001

010

011

100

101

110

111

Each mask represents a unique set of visited cities.

---

## Base Case

Starting City:

A

Mask:

0001

Cost:

0

---

## Final Answer

When:

All cities visited

Mask:

1111

Return to starting city.

Minimum cost obtained is the answer.

---

## Applications

### Route Optimization

Delivery systems.

---

### Logistics

Transportation planning.

---

### Robotics

Path planning.

---

### Circuit Design

Optimization problems.

---

### Scheduling

Efficient traversal.

---

## Time Complexity

Bitmask DP:

O(n² × 2ⁿ)

---

## Space Complexity

O(n × 2ⁿ)

---

## Comparison

| Method | Complexity |
|----------|----------|
| Brute Force | O(n!) |
| Bitmask DP | O(n² × 2ⁿ) |

---

## Advantages

- Much Faster Than Brute Force
- Efficient State Compression
- Optimal Solution Guaranteed

---

## Key Concepts Learned

- Traveling Salesman Problem
- Bitmask Dynamic Programming
- State Compression
- Graph Optimization
- Route Planning

---

## Summary

The Traveling Salesman Problem is one of the most famous optimization problems in computer science. Bitmask Dynamic Programming significantly reduces computation by storing visited-city states efficiently.