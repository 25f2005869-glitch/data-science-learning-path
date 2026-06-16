# Day 77 – Bit Masking

## Objective

The goal of this session is to understand Bit Masking and how it is used to efficiently represent and manipulate sets using binary numbers.

---

## What is Bit Masking?

Bit Masking is a technique that uses bits to store and manipulate information.

Each bit represents a state:

0 → OFF

1 → ON

---

## Why Use Bit Masking?

Traditional Approach:

Store multiple boolean values separately.

Example:

is_admin = True

is_verified = False

is_active = True

---

Bit Masking:

Store all information in a single integer.

Example:

101

This saves memory and allows very fast operations.

---

## Binary Representation

Decimal:

13

Binary:

1101

Position:

8 4 2 1

Bits:

1 1 0 1

---

## What is a Mask?

A mask is a binary pattern used to manipulate specific bits.

Example:

Mask:

0001

Used to access the last bit.

---

## Common Operations

### Set a Bit

Turn a bit ON.

Formula:

number | (1 << position)

Example:

Number:

5

Binary:

0101

Set Bit 1

Mask:

0010

Result:

0111

=

7

---

### Clear a Bit

Turn a bit OFF.

Formula:

number & ~(1 << position)

Example:

7

Binary:

0111

Clear Bit 1

Result:

0101

=

5

---

### Toggle a Bit

Change:

0 → 1

1 → 0

Formula:

number ^ (1 << position)

Example:

5

Binary:

0101

Toggle Bit 1

Result:

0111

=

7

---

### Check a Bit

Determine whether a bit is ON.

Formula:

number & (1 << position)

Example:

5

Binary:

0101

Check Bit 2

Result:

True

---

## Example

Number:

10

Binary:

1010

---

Bit Positions:

3 2 1 0

1 0 1 0

---

Check Bit 1:

ON

---

Check Bit 2:

OFF

---

## Representing Sets

Suppose:

A = 1

B = 2

C = 4

D = 8

---

Set:

A C

Binary:

0101

Decimal:

5

---

Set:

A B D

Binary:

1011

Decimal:

11

---

## Applications

### Competitive Programming

Subset generation.

---

### Dynamic Programming

Bitmask DP.

---

### Permission Systems

User roles and access control.

---

### Operating Systems

Flag management.

---

### Networking

Protocol flags.

---

## Advantages

- Fast Operations
- Memory Efficient
- Easy State Representation
- Useful for Large Combinations

---

## Time Complexity

Set Bit:

O(1)

Clear Bit:

O(1)

Toggle Bit:

O(1)

Check Bit:

O(1)

---

## Key Concepts Learned

- Bit Masking
- Set Bit
- Clear Bit
- Toggle Bit
- Check Bit
- Binary Representation

---

## Summary

Bit Masking is a powerful technique that uses binary bits to efficiently store and manipulate information. It is widely used in competitive programming, operating systems, networking, and advanced Dynamic Programming problems.