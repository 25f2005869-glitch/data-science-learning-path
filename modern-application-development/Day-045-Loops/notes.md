# 🔄 Day 045 — Loops — Detailed Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 045  
**Topic:** Loops

---

## 1. What Is a Loop?

A loop is a programming structure that repeatedly executes a block of code.

Loops are useful when the same operation needs to be performed multiple times.

Example:

    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }

Output:

    1
    2
    3
    4
    5

---

## 2. Why Use Loops?

Without loops, repeated work requires writing the same code many times.

Instead of:

    console.log(1);
    console.log(2);
    console.log(3);
    console.log(4);
    console.log(5);

We can write:

    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }

---

# 3. for Loop

The `for` loop is commonly used when the number of iterations is known.

Syntax:

    for (initialization; condition; update) {
        // code
    }

Example:

    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }

### Three Important Parts

1. Initialization
2. Condition
3. Update

Example:

    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }

Here:

- `let i = 1` → initialization
- `i <= 5` → condition
- `i++` → update

---

# 4. Execution of a for Loop

For:

    for (let i = 1; i <= 3; i++) {
        console.log(i);
    }

Execution:

1. `i` is initialized to `1`.
2. Condition `i <= 3` is checked.
3. Code executes.
4. `i++` increases the value.
5. Condition is checked again.
6. The process continues until the condition becomes false.

---

# 5. Counting Backwards

A loop can also decrease a value.

    for (let i = 5; i >= 1; i--) {
        console.log(i);
    }

Output:

    5
    4
    3
    2
    1

---

# 6. Increment by More Than One

The update expression does not have to be `i++`.

Example:

    for (let i = 0; i <= 10; i += 2) {
        console.log(i);
    }

Output:

    0
    2
    4
    6
    8
    10

---

# 7. while Loop

A `while` loop executes code as long as its condition is true.

Syntax:

    while (condition) {
        // code
    }

Example:

    let i = 1;

    while (i <= 5) {
        console.log(i);
        i++;
    }

The update must be handled inside the loop.

---

# 8. while Loop Execution

Example:

    let count = 1;

    while (count <= 3) {
        console.log(count);
        count++;
    }

Process:

1. Initialize `count`.
2. Check the condition.
3. Execute the loop body.
4. Update `count`.
5. Check the condition again.
6. Stop when the condition becomes false.

---

# 9. do...while Loop

A `do...while` loop executes its body at least once.

Syntax:

    do {
        // code
    } while (condition);

Example:

    let i = 1;

    do {
        console.log(i);
        i++;
    } while (i <= 5);

---

# 10. while vs do...while

Consider:

    let x = 10;

    while (x < 5) {
        console.log(x);
    }

The body does not execute.

But:

    let x = 10;

    do {
        console.log(x);
    } while (x < 5);

The body executes once.

### Key Difference

`while`:

    condition → body

`do...while`:

    body → condition

---

# 11. break

`break` immediately terminates a loop.

Example:

    for (let i = 1; i <= 10; i++) {
        if (i === 5) {
            break;
        }

        console.log(i);
    }

Output:

    1
    2
    3
    4

---

# 12. continue

`continue` skips the current iteration and moves to the next iteration.

Example:

    for (let i = 1; i <= 5; i++) {
        if (i === 3) {
            continue;
        }

        console.log(i);
    }

Output:

    1
    2
    4
    5

---

# 13. break vs continue

| Keyword | Purpose |
|---|---|
| `break` | Stops the entire loop |
| `continue` | Skips current iteration |

---

# 14. Nested Loops

A loop inside another loop is called a nested loop.

Example:

    for (let i = 1; i <= 3; i++) {
        for (let j = 1; j <= 3; j++) {
            console.log(i, j);
        }
    }

The inner loop completes its iterations for every iteration of the outer loop.

Nested loops are useful for:

- Tables
- Matrices
- Patterns
- Pair combinations
- Multi-dimensional data

---

# 15. Loop Through an Array

Example:

    const subjects = ["DBMS", "PDSA", "MLF"];

    for (let i = 0; i < subjects.length; i++) {
        console.log(subjects[i]);
    }

Output:

    DBMS
    PDSA
    MLF

Important:

    subjects.length

gives the number of elements.

---

# 16. Loop Through a String

Strings can also be accessed character by character.

Example:

    const word = "JavaScript";

    for (let i = 0; i < word.length; i++) {
        console.log(word[i]);
    }

---

# 17. Infinite Loop

An infinite loop never stops because its condition never becomes false.

Example:

    let i = 1;

    while (i <= 5) {
        console.log(i);
    }

The value of `i` never changes.

Therefore, the condition remains true.

Correct version:

    let i = 1;

    while (i <= 5) {
        console.log(i);
        i++;
    }

---

# 18. Common Loop Mistakes

### Mistake 1: Forgetting the update

    let i = 1;

    while (i <= 5) {
        console.log(i);
    }

This can create an infinite loop.

### Mistake 2: Wrong condition

    for (let i = 1; i >= 5; i++) {
        console.log(i);
    }

The condition is false immediately.

### Mistake 3: Wrong array boundary

Correct:

    for (let i = 0; i < array.length; i++)

Usually avoid:

    for (let i = 0; i <= array.length; i++)

because the last index is `length - 1`.

---

# 19. Choosing the Right Loop

### Use `for`

When the number of iterations or loop structure is predictable.

### Use `while`

When repetition depends mainly on a condition.

### Use `do...while`

When the code must execute at least once.

---

# 20. Practical Example

Calculate the total marks:

    const marks = [80, 75, 90, 85];
    let total = 0;

    for (let i = 0; i < marks.length; i++) {
        total += marks[i];
    }

    console.log(total);

The loop visits every element and adds it to `total`.

---

# 21. Important Concepts to Remember

- A loop repeats code.
- `for` has initialization, condition, and update.
- `while` checks the condition before execution.
- `do...while` executes at least once.
- `break` stops a loop.
- `continue` skips one iteration.
- Nested loops contain one loop inside another.
- Always make sure the loop can terminate.
- Arrays can be traversed using their indexes and `length`.

---

# 22. Best Practices

- Use meaningful variable names.
- Keep loop conditions simple.
- Avoid unnecessary nested loops.
- Always verify loop boundaries.
- Avoid accidental infinite loops.
- Use `const` for collections that are not reassigned.
- Use `let` for changing loop counters.
- Keep loop bodies readable.