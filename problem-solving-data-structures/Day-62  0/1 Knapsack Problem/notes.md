# Day 62 – 0/1 Knapsack Problem

## Objective

The goal of this session is to understand the 0/1 Knapsack Problem and solve it using Dynamic Programming.

---

## What is the 0/1 Knapsack Problem?

You are given:

- A knapsack with limited capacity.
- Items with:
  - Weight
  - Value

The objective is:

Maximize Total Value

without exceeding the knapsack capacity.

---

## Why is it called 0/1?

For each item there are only two choices:

Take the item → 1

Do not take the item → 0

Fractional selection is NOT allowed.

---

## Example

Capacity = 5

Items:

| Item | Weight | Value |
|--------|--------|--------|
| A | 1 | 6 |
| B | 2 | 10 |
| C | 3 | 12 |

---

## Possible Selections

Take A + B

Weight:

1 + 2 = 3

Value:

6 + 10 = 16

---

Take A + C

Weight:

1 + 3 = 4

Value:

18

---

Take B + C

Weight:

2 + 3 = 5

Value:

22

✅ Best Choice

---

## Key Observation

For every item:

Two options exist.

Option 1:

Do not take item

Option 2:

Take item

Choose the better option.

---

## Recurrence Relation

If weight[i] > capacity

dp[i][w]

=

dp[i−1][w]

---

Otherwise

dp[i][w]

=

max(

dp[i−1][w],

value[i] + dp[i−1][w−weight[i]]

)

---

## Dynamic Programming Table

Capacity = 5

Items = 3

DP Table:

| Item | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 6 | 6 | 6 | 6 | 6 |
| B | 0 | 6 | 10 | 16 | 16 | 16 |
| C | 0 | 6 | 10 | 16 | 18 | 22 |

Final Answer:

22

---

## Algorithm

1. Create DP table.
2. Process items one by one.
3. For each capacity:
   - Take item.
   - Skip item.
4. Store maximum value.
5. Return final answer.

---

## Applications

- Cargo Loading
- Budget Planning
- Resource Allocation
- Investment Selection
- Project Scheduling

---

## Time Complexity

O(n × W)

Where:

n = Number of Items

W = Capacity

---

## Space Complexity

O(n × W)

---

## Key Concepts Learned

- Dynamic Programming
- 0/1 Knapsack
- Optimization Problem
- State Transition
- DP Table

---

## Summary

The 0/1 Knapsack Problem is one of the most important Dynamic Programming problems. It teaches how to make optimal decisions when each item can either be selected completely or not selected at all.