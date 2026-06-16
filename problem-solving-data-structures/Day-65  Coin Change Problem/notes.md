# Day 65 – Coin Change Problem

## Objective

The goal of this session is to understand the Coin Change Problem and solve it using Dynamic Programming.

---

## What is the Coin Change Problem?

Given:

- A set of coin denominations.
- A target amount.

The objective is:

Find the minimum number of coins required to make the target amount.

---

## Example

Coins:

1, 2, 5

Target Amount:

11

Possible Solution:

5 + 5 + 1

Number of Coins:

3

---

## Why Not Use Greedy?

Consider:

Coins:

1, 3, 4

Target:

6

Greedy Choice:

4 + 1 + 1

Coins Used:

3

---

Optimal Solution:

3 + 3

Coins Used:

2

---

Greedy fails.

Dynamic Programming gives the optimal answer.

---

## Key Observation

To make amount:

A

Try every coin.

For each coin:

coin

Remaining Amount:

A − coin

If we already know the answer for:

A − coin

then we can build the answer for:

A

---

## Dynamic Programming State

Define:

dp[i]

=

Minimum coins needed to make amount i

---

## Base Case

Amount:

0

Needs:

0 coins

Therefore:

dp[0] = 0

---

## Recurrence Relation

For each coin:

dp[i]

=

min(

dp[i],

1 + dp[i − coin]

)

---

## Example

Coins:

1, 2, 5

Target:

11

DP Table:

Amount:

0 1 2 3 4 5 6 7 8 9 10 11

Coins:

0 1 1 2 2 1 2 2 3 3 2 3

Answer:

3

---

## Algorithm

1. Create DP array.
2. Initialize with infinity.
3. Set dp[0] = 0.
4. Process every amount.
5. Try every coin.
6. Update minimum coins.
7. Return dp[target].

---

## Applications

### ATM Systems

Minimum currency notes.

### Cash Management

Optimal coin usage.

### Resource Allocation

Minimum resources required.

### Financial Software

Payment optimization.

---

## Time Complexity

O(amount × number_of_coins)

---

## Space Complexity

O(amount)

---

## Key Concepts Learned

- Coin Change
- Dynamic Programming
- Optimization
- State Transition
- Minimum Coins

---

## Summary

The Coin Change Problem is a classic Dynamic Programming problem where previously computed answers are reused to find the minimum number of coins needed for a target amount.