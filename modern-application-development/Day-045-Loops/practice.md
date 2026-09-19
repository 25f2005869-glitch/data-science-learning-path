# 📝 Day 045 — Loops — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 045  
**Topic:** Loops

---

# Part A — Basic Questions

1. What is a loop?
2. Why are loops useful?
3. Name three basic JavaScript loops.
4. What are the three parts of a `for` loop?
5. What is the purpose of the loop condition?
6. What is the purpose of the update expression?
7. What is the difference between `while` and `do...while`?
8. Which loop always executes its body at least once?
9. What does `break` do?
10. What does `continue` do?

---

# Part B — Predict the Output

### Question 1

    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }

Write the output.

### Question 2

    for (let i = 5; i >= 1; i--) {
        console.log(i);
    }

Write the output.

### Question 3

    for (let i = 0; i <= 10; i += 2) {
        console.log(i);
    }

Write the output.

### Question 4

    let i = 1;

    while (i <= 3) {
        console.log(i);
        i++;
    }

Write the output.

### Question 5

    for (let i = 1; i <= 5; i++) {
        if (i === 3) {
            continue;
        }

        console.log(i);
    }

Write the output.

---

# Part C — Coding Practice

## Task 1

Print numbers from 1 to 20 using a `for` loop.

## Task 2

Print numbers from 20 to 1.

## Task 3

Print all even numbers from 1 to 50.

## Task 4

Print all odd numbers from 1 to 50.

## Task 5

Calculate the sum of numbers from 1 to 100.

## Task 6

Print the multiplication table of 7.

## Task 7

Print the multiplication tables from 1 to 5 using nested loops.

## Task 8

Find the sum of all elements in:

    const marks = [80, 75, 90, 85, 70];

## Task 9

Find the largest value in:

    const numbers = [12, 45, 7, 89, 23];

## Task 10

Count the number of vowels in:

    const word = "JavaScript";

---

# Part D — break and continue

## Task 11

Print numbers from 1 to 10 but stop when the number becomes 6.

## Task 12

Print numbers from 1 to 10 but skip 5.

## Task 13

Print numbers from 1 to 20 but skip all even numbers.

---

# Part E — while and do...while

## Task 14

Print numbers from 1 to 10 using `while`.

## Task 15

Create a countdown from 10 to 1 using `while`.

## Task 16

Create a `do...while` loop that prints numbers from 1 to 5.

## Task 17

Create a `do...while` example that demonstrates that the loop executes at least once.

---

# Part F — Array Practice

## Task 18

Print every subject:

    const subjects = ["DBMS", "PDSA", "MLF", "MAD1"];

## Task 19

Calculate the total marks:

    const marks = [85, 90, 78, 92, 88];

## Task 20

Calculate the average marks.

## Task 21

Find the highest mark.

## Task 22

Count how many marks are greater than or equal to 80.

---

# Part G — Challenge

## Challenge 1

Create a program that prints:

    1
    12
    123
    1234
    12345

Use nested loops.

## Challenge 2

Create a program that calculates the factorial of a number.

Example:

    5! = 120

## Challenge 3

Check whether a number is prime using a loop.

## Challenge 4

Reverse a string using a loop.

## Challenge 5

Create a Student Marks Analyzer that:

- Stores marks in an array.
- Calculates total marks.
- Calculates average marks.
- Finds highest marks.
- Finds lowest marks.
- Counts passing marks.
- Displays the results on the webpage.

---

# 🎯 Revision Checklist

- [ ] I understand loops.
- [ ] I can write a `for` loop.
- [ ] I can write a `while` loop.
- [ ] I can write a `do...while` loop.
- [ ] I understand `break`.
- [ ] I understand `continue`.
- [ ] I can create nested loops.
- [ ] I can iterate through arrays.
- [ ] I can iterate through strings.
- [ ] I can avoid infinite loops.
- [ ] I can solve basic loop problems.