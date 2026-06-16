# Day 76 – Bit Manipulation Basics

## Objective

The goal of this session is to understand Bit Manipulation, one of the most powerful techniques in programming and competitive coding.

---

## What is Bit Manipulation?

Bit Manipulation means performing operations directly on binary bits.

Computers internally store data as:

0s and 1s

Example:

Decimal:

5

Binary:

101

---

## Why Learn Bit Manipulation?

Bit operations are:

- Fast
- Memory Efficient
- Frequently Asked in Interviews
- Useful in Competitive Programming

---

## Binary Representation

Decimal:

5

Binary:

101

---

Decimal:

10

Binary:

1010

---

Decimal:

13

Binary:

1101

---

## Bitwise Operators

### AND (&)

Rule:

1 & 1 = 1

Otherwise:

0

Example:

5 = 101

3 = 011

Result:

001

=

1

---

### OR (|)

Rule:

If either bit is 1

Result = 1

Example:

5 = 101

3 = 011

Result:

111

=

7

---

### XOR (^)

Rule:

Different Bits → 1

Same Bits → 0

Example:

5 = 101

3 = 011

Result:

110

=

6

---

### NOT (~)

Flips all bits.

Example:

5

Binary:

101

Result:

~5

=

-6

---

## Shift Operators

### Left Shift (<<)

Shifts bits left.

Example:

5 << 1

Binary:

101

↓

1010

Result:

10

---

Rule:

x << n

=

x × 2ⁿ

---

### Right Shift (>>)

Shifts bits right.

Example:

10 >> 1

Binary:

1010

↓

0101

Result:

5

---

Rule:

x >> n

=

x ÷ 2ⁿ

---

## Common Tricks

### Check Even or Odd

Number:

n

Condition:

n & 1

Result:

0 → Even

1 → Odd

---

Example

8 & 1

=

0

Even

---

9 & 1

=

1

Odd

---

### Swap Two Numbers

Using XOR

a = a ^ b

b = a ^ b

a = a ^ b

---

### Multiply by 2

n << 1

---

### Divide by 2

n >> 1

---

## Applications

### Competitive Programming

Fast calculations.

---

### Cryptography

Encryption algorithms.

---

### Graphics Programming

Pixel operations.

---

### Operating Systems

Memory management.

---

### Networking

Packet processing.

---

## Time Complexity

Bit Operations:

O(1)

Constant Time

---

## Advantages

- Extremely Fast
- Low Memory Usage
- Efficient Computation
- Useful in Optimization Problems

---

## Key Concepts Learned

- Binary Numbers
- AND Operator
- OR Operator
- XOR Operator
- NOT Operator
- Left Shift
- Right Shift

---

## Summary

Bit Manipulation allows direct operations on binary data and is one of the fastest techniques available in programming. Understanding bitwise operators is essential for interviews, competitive programming, and system-level development.