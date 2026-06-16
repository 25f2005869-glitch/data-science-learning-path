# Day 79 – Bitmask Dynamic Programming

## Objective

The goal of this session is to understand Bitmask Dynamic Programming and how it is used to solve problems involving subsets and state compression.

---

## What is Bitmask Dynamic Programming?

Bitmask Dynamic Programming is a technique that combines:

- Bit Masking
- Dynamic Programming

to efficiently solve problems involving subsets.

---

## Why Do We Need Bitmask DP?

Consider a set:

A B C D

Total Subsets:

2⁴

=

16

For larger values:

n = 20

Total Subsets:

2²⁰

=

1,048,576

Managing subsets normally becomes difficult.

Bitmasks provide compact storage.

---

## State Compression

Suppose:

n = 4

Elements:

A B C D

Represent subset using bits.

Example:

1010

Meaning:

A = Selected

B = Not Selected

C = Selected

D = Not Selected

---

## DP State

Instead of storing complete subsets:

Store only bitmasks.

Example:

dp[mask]

represents

Answer for subset represented by mask.

---

## Example

Elements:

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

Total:

8 states

---

## Common Pattern

State:

dp[mask]

Transition:

Add one element to current subset.

Example:

Current:

001

Add:

010

New State:

011

---

## Example Problem

Count number of ways to form subsets.

Elements:

1 2 3

States:

000

001

010

011

100

101

110

111

Each state represents a unique subset.

---

## Traveling Salesman Problem (TSP)

One of the most famous Bitmask DP problems.

State:

dp[mask][city]

Meaning:

Minimum cost to visit cities in mask and end at city.

---

## Why Bitmask DP is Powerful?

Instead of storing:

Selected Elements

Store:

Single Integer Mask

This greatly reduces memory usage.

---

## Applications

### Traveling Salesman Problem

State compression.

---

### Assignment Problems

Job allocation.

---

### Hamiltonian Path

Graph traversal.

---

### Subset Problems

Efficient subset handling.

---

### Competitive Programming

Advanced optimization.

---

## Example State

Elements:

A B C D

Mask:

1101

Meaning:

A Selected

B Not Selected

C Selected

D Selected

---

## Time Complexity

Typical Bitmask DP:

O(n × 2ⁿ)

---

## Space Complexity

O(2ⁿ)

---

## Advantages

- Compact State Representation
- Faster Computation
- Reduced Memory Usage
- Powerful for Subset Problems

---

## Key Concepts Learned

- Bitmask DP
- State Compression
- Subset Representation
- Dynamic Programming
- Optimization

---

## Summary

Bitmask Dynamic Programming combines the efficiency of bitwise operations with Dynamic Programming to solve subset-based problems efficiently. It is widely used in advanced algorithmic challenges and competitive programming.