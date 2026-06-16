# Day 04 – Loops

## Objective

The goal of this session is to understand how repetition works in programming using loops.

---

## What is a Loop?

A loop is used to execute a block of code multiple times.

Python provides:

* for loop
* while loop

---

## for Loop

A for loop is used when the number of repetitions is known.

Example:

```python id="l01"
for i in range(1, 6):
    print(i)
```

Output:

```text id="l02"
1
2
3
4
5
```

---

## range() Function

The `range()` function generates a sequence of numbers.

Examples:

```python id="l03"
range(5)
```

Produces:

```text id="l04"
0 1 2 3 4
```

```python id="l05"
range(1, 6)
```

Produces:

```text id="l06"
1 2 3 4 5
```

---

## while Loop

A while loop executes as long as a condition remains True.

Example:

```python id="l07"
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text id="l08"
1
2
3
4
5
```

---

## Key Concepts Learned

* Repetition
* for Loop
* while Loop
* range() Function
* Loop Counter

---

## Summary

Loops help automate repetitive tasks and reduce code duplication.
