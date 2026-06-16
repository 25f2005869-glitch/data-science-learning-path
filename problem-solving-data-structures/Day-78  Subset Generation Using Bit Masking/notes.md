# Day 78 – Subset Generation Using Bit Masking

## Objective

The goal of this session is to understand how Bit Masking can be used to generate all possible subsets of a set efficiently.

---

## What is a Subset?

A subset is a collection of elements selected from a set.

Example:

Set:

A B C

Possible Subsets:

{}

{A}

{B}

{C}

{A,B}

{A,C}

{B,C}

{A,B,C}

Total:

8 Subsets

---

## Number of Subsets

For a set containing:

n elements

Total Subsets:

2ⁿ

Example:

n = 3

Total:

2³

=

8

---

## Bit Masking Idea

Each bit represents whether an element is present or absent.

Bit Value:

0 → Element Not Selected

1 → Element Selected

---

## Example

Set:

A B C

Indexes:

0 1 2

---

Mask:

000

Subset:

{}

---

Mask:

001

Subset:

{A}

---

Mask:

010

Subset:

{B}

---

Mask:

011

Subset:

{A,B}

---

Mask:

100

Subset:

{C}

---

Mask:

101

Subset:

{A,C}

---

Mask:

110

Subset:

{B,C}

---

Mask:

111

Subset:

{A,B,C}

---

## Visualization

Elements:

A B C

Masks:

000 → {}

001 → {A}

010 → {B}

011 → {A,B}

100 → {C}

101 → {A,C}

110 → {B,C}

111 → {A,B,C}

---

## Algorithm

1. Let n be the number of elements.
2. Iterate from 0 to (2ⁿ − 1).
3. Convert number into binary mask.
4. Check every bit position.
5. If bit is 1:
   Include corresponding element.
6. Print subset.

---

## Example

Array:

1 2 3

n = 3

Range:

0 to 7

Binary Masks:

000

001

010

011

100

101

110

111

Generate all subsets.

---

## Applications

### Competitive Programming

Subset enumeration.

---

### Dynamic Programming

Bitmask DP.

---

### Backtracking Optimization

State representation.

---

### Combinatorics

Power set generation.

---

### Search Problems

State-space exploration.

---

## Time Complexity

Total Subsets:

2ⁿ

For each subset:

n checks

Overall:

O(n × 2ⁿ)

---

## Space Complexity

O(n)

excluding output storage.

---

## Advantages

- Simple Implementation
- Fast Subset Generation
- Efficient State Representation
- Useful in Advanced DP

---

## Key Concepts Learned

- Bit Masking
- Subset Generation
- Power Set
- Binary Representation
- State Compression

---

## Summary

Bit Masking provides an elegant way to generate all possible subsets of a set by representing selections using binary numbers. It is one of the most important techniques in competitive programming and advanced Dynamic Programming.