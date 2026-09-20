# 🧪 Day 053 — Error Handling — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 053  
**Topic:** Error Handling

---

# 🎯 Practice Objectives

Practice:

- Syntax errors
- Runtime errors
- Logical errors
- `try...catch`
- `finally`
- `throw`
- Error objects
- Built-in error types
- Input validation
- Error propagation

---

# 🟢 Level 1 — Basics

## Q1

What is an error in JavaScript?

---

## Q2

What is a syntax error?

---

## Q3

What is a runtime error?

---

## Q4

What is a logical error?

---

## Q5

Why is error handling important?

---

# 🟡 Level 2 — try...catch

## Q6

Write the basic syntax of `try...catch`.

---

## Q7

What is the purpose of the `catch` block?

---

## Q8

What information can the error object provide?

---

## Q9

What is the purpose of `finally`?

---

## Q10

When should `finally` typically be used?

---

# 🟠 Level 3 — Predict the Result

## Q11

What happens?

    try {
        console.log(unknownVariable);
    } catch (error) {
        console.log("Error handled");
    }

---

## Q12

What is the output?

    try {
        console.log("Start");
    } catch (error) {
        console.log("Error");
    } finally {
        console.log("Finished");
    }

---

## Q13

What happens?

    try {
        throw new Error("Invalid score");
    } catch (error) {
        console.log(error.message);
    }

---

## Q14

What type of error is expected?

    console.log(unknownVariable);

---

## Q15

What type of error is expected?

    const student = null;
    console.log(student.name);

---

# 🔴 Level 4 — Error Types

## Q16

Match the error with its typical cause:

- `ReferenceError`
- `TypeError`
- `RangeError`
- `SyntaxError`

Causes:

- Invalid JavaScript syntax
- Unknown variable
- Invalid operation for a value's type
- Value outside an allowed range

---

## Q17

What error can invalid JSON parsing produce?

---

## Q18

What is the difference between `error.name` and `error.message`?

---

# 🧠 Conceptual Questions

## Q19

What does `throw` do?

---

## Q20

What is error propagation?

---

## Q21

Why should errors not be silently ignored?

---

## Q22

Why should exceptions generally not be used for normal program flow?

---

## Q23

Why is input validation important?

---

## Q24

Why is `console.error()` useful?

---

# 💻 Coding Practice

## Task 1 — Safe Division

Create a function that divides two numbers.

If the divisor is zero, throw an error.

Handle the error using `try...catch`.

---

## Task 2 — Marks Validation

Create a function:

    checkMarks(marks)

Rules:

- Marks must be between 0 and 100.
- Invalid marks should throw an `Error`.
- Valid marks should return a success message.

---

## Task 3 — JSON Parsing

Try to parse an invalid JSON string.

Use `try...catch` to handle the error.

Display a user-friendly message.

---

## Task 4 — Student Data

Create a function that receives a student object.

Check whether:

- Name exists.
- Course exists.
- Score is between 0 and 100.

Throw meaningful errors for invalid data.

---

## Task 5 — finally

Create a program that:

1. Starts an operation.
2. Attempts the operation.
3. Handles an error.
4. Executes cleanup in `finally`.

---

# ⭐ Final Challenge

Create an interactive Student Result Checker.

The program should:

- Accept student name.
- Accept marks.
- Validate the marks.
- Throw an error for invalid marks.
- Catch the error.
- Display a user-friendly message.
- Use `finally`.
- Log technical errors using `console.error()`.

---

# ✅ Self-Check

Before moving to Day 054, make sure you can explain:

- [ ] Syntax Error
- [ ] Runtime Error
- [ ] Logical Error
- [ ] `try`
- [ ] `catch`
- [ ] `finally`
- [ ] `throw`
- [ ] `Error`
- [ ] `ReferenceError`
- [ ] `TypeError`
- [ ] `RangeError`
- [ ] `SyntaxError`
- [ ] `error.name`
- [ ] `error.message`
- [ ] Error propagation
- [ ] Defensive programming

---

## 📌 Goal

Learn to identify errors, handle expected failures, and write JavaScript that fails safely and predictably.