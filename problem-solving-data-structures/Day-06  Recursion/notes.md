# Day 06 – Recursion

## Objective

The goal of this session is to understand how a function can call itself to solve a problem.

---

## What is Recursion?

Recursion is a technique in which a function calls itself.

A recursive solution breaks a large problem into smaller versions of the same problem.

---

## Components of Recursion

### 1. Base Case

The condition that stops recursion.

### 2. Recursive Case

The part where the function calls itself.

---

## Example: Factorial

Mathematical Definition:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Recursive Definition:

```text
n! = n × (n - 1)!

1! = 1
```

---

## Working

Example:

```text
factorial(5)

5 × factorial(4)
4 × factorial(3)
3 × factorial(2)
2 × factorial(1)

Result = 120
```

---

## Advantages

* Simple and elegant solution
* Useful for tree and graph problems
* Reduces code complexity in some cases

---

## Disadvantages

* Uses more memory
* Can be slower than iteration
* Incorrect recursion may cause infinite calls

---

## Key Concepts Learned

* Recursion
* Recursive Function
* Base Case
* Recursive Case
* Factorial Problem

---

## Summary

Recursion allows a function to solve a problem by repeatedly calling itself until a base condition is reached.
