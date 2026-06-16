# Day 64 – Longest Increasing Subsequence (LIS)

## Objective

The goal of this session is to understand the Longest Increasing Subsequence (LIS) problem and solve it using Dynamic Programming.

---

## What is a Subsequence?

A subsequence is a sequence obtained by removing zero or more elements without changing the order of the remaining elements.

Example:

Array:

10 20 30 40

Possible Subsequences:

10 20

10 30

20 40

10 20 30

10 20 30 40

---

## What is an Increasing Subsequence?

A subsequence in which every next element is greater than the previous element.

Example:

10 20 30

Increasing ✅

---

30 20 10

Increasing ❌

---

## What is LIS?

The Longest Increasing Subsequence (LIS) is the longest subsequence whose elements are in strictly increasing order.

---

## Example

Array:

10 22 9 33 21 50 41 60

Possible Increasing Subsequences:

10 22 33 50 60

10 22 33 41 60

10 22 33 50

---

Longest Increasing Subsequence:

10 22 33 50 60

Length:

5

---

## Key Observation

For every element:

Look at all previous elements.

If previous element is smaller:

Current element can extend that subsequence.

---

## Dynamic Programming Idea

Define:

dp[i]

=

Length of LIS ending at index i

Initially:

dp[i] = 1

because every element alone is an increasing subsequence of length 1.

---

## Recurrence Relation

For every pair:

j < i

If:

arr[j] < arr[i]

Then:

dp[i]

=

max(

dp[i],

dp[j] + 1

)

---

## Example

Array:

10 22 9 33

Initial DP:

1 1 1 1

After Processing:

1 2 1 3

Explanation:

22 extends 10

33 extends 22

---

## DP Table

Array:

10 22 9 33 21 50 41 60

DP:

1 2 1 3 2 4 4 5

Maximum Value:

5

---

## Algorithm

1. Create DP array.
2. Initialize all values as 1.
3. Compare each element with previous elements.
4. Update DP values.
5. Maximum DP value is the LIS length.

---

## Applications

### Stock Market Analysis

Identify growth trends.

### Data Analysis

Pattern recognition.

### Bioinformatics

DNA sequence comparison.

### Machine Learning

Sequence optimization.

---

## Time Complexity

O(n²)

---

## Space Complexity

O(n)

---

## Optimized Approach

Using Binary Search:

Time Complexity:

O(n log n)

---

## Key Concepts Learned

- Longest Increasing Subsequence
- Dynamic Programming
- Subsequences
- State Transition
- Optimization

---

## Summary

The Longest Increasing Subsequence problem finds the longest subsequence in which elements are arranged in increasing order. It is one of the most important Dynamic Programming problems and appears frequently in interviews and competitive programming.