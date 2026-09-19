# 📝 Day 048 — Arrays — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 048  
**Topic:** Arrays

---

# Part A — Basic Questions

1. What is an array?
2. Why are arrays useful?
3. How do you create an array?
4. From which number does an array index start?
5. What does the `length` property return?
6. How do you access the last element?
7. How do you update an array element?
8. What does `push()` do?
9. What does `pop()` do?
10. What does `shift()` do?
11. What does `unshift()` do?
12. What does `includes()` return?
13. What does `indexOf()` return when an element is not found?
14. What is array traversal?
15. What is the difference between `slice()` and `splice()`?

---

# Part B — Predict the Output

## Question 1

    const numbers = [10, 20, 30];

    console.log(numbers[0]);
    console.log(numbers[2]);

Write the output.

---

## Question 2

    const subjects = ["DBMS", "PDSA"];

    subjects.push("MLF");

    console.log(subjects);

Write the output.

---

## Question 3

    const subjects = ["DBMS", "PDSA", "MLF"];

    subjects.pop();

    console.log(subjects);

Write the output.

---

## Question 4

    const numbers = [10, 20, 30];

    numbers[1] = 50;

    console.log(numbers);

Write the output.

---

## Question 5

    const numbers = [10, 20, 30, 40, 50];

    console.log(numbers.slice(1, 4));

Write the output.

---

# Part C — Basic Coding

## Task 1

Create an array containing five subject names.

## Task 2

Print the first element.

## Task 3

Print the last element.

## Task 4

Print the length of the array.

## Task 5

Update the second element.

## Task 6

Add an element using `push()`.

## Task 7

Remove the last element using `pop()`.

## Task 8

Add an element at the beginning using `unshift()`.

## Task 9

Remove the first element using `shift()`.

---

# Part D — Array Traversal

## Task 10

Print every element using a `for` loop.

## Task 11

Print every element with its index.

Expected style:

    0: DBMS
    1: PDSA
    2: MLF

## Task 12

Print all numbers from:

    [10, 20, 30, 40, 50]

using a loop.

---

# Part E — Array Methods

## Task 13

Check whether `"PDSA"` exists in:

    ["DBMS", "PDSA", "MLF"]

using `includes()`.

## Task 14

Find the index of `"MLF"` using `indexOf()`.

## Task 15

Convert:

    ["DBMS", "PDSA", "MLF"]

into:

    "DBMS, PDSA, MLF"

using `join()`.

## Task 16

Extract the middle elements using `slice()`.

## Task 17

Remove one element using `splice()`.

## Task 18

Insert an element using `splice()`.

## Task 19

Replace an element using `splice()`.

---

# Part F — Numerical Arrays

Use:

    const marks = [85, 90, 78, 92, 88];

## Task 20

Calculate the total marks.

## Task 21

Calculate the average marks.

## Task 22

Find the highest mark.

## Task 23

Find the lowest mark.

## Task 24

Count how many marks are greater than or equal to 80.

---

# Part G — Functions and Arrays

## Task 25

Create a function that accepts an array and returns its total.

## Task 26

Create a function that accepts an array and returns its average.

## Task 27

Create a function that finds the maximum value.

## Task 28

Create a function that checks whether a particular value exists.

---

# Part H — Nested Arrays

Use:

    const matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];

## Task 29

Print the number `5`.

## Task 30

Print all elements using nested loops.

## Task 31

Calculate the sum of all matrix elements.

---

# Part I — Challenges

## Challenge 1 — Student Marks Analyzer

Create a program using:

    const marks = [85, 90, 78, 92, 88];

Calculate:

- Total
- Average
- Highest
- Lowest
- Number of passing marks
- Number of marks above 80

---

## Challenge 2 — Course Manager

Create an array:

    ["DBMS", "PDSA", "MLF"]

Implement operations to:

- Add a course
- Remove the last course
- Add a course at the beginning
- Search for a course
- Display all courses

---

## Challenge 3 — Reverse an Array

Reverse:

    [10, 20, 30, 40, 50]

without using a built-in reverse method.

---

## Challenge 4 — Find Duplicate Values

Given:

    [10, 20, 10, 30, 20, 40]

identify the duplicate values.

---

## Challenge 5 — Student Dashboard

Create a webpage that stores student information in arrays and displays:

- Student names
- Marks
- Average
- Highest marks
- Lowest marks
- Subjects

Use loops and functions.

---

# 🎯 Revision Checklist

- [ ] I understand arrays.
- [ ] I understand array indexes.
- [ ] I can access array elements.
- [ ] I can update elements.
- [ ] I understand `length`.
- [ ] I can use `push()` and `pop()`.
- [ ] I can use `shift()` and `unshift()`.
- [ ] I understand `slice()`.
- [ ] I understand `splice()`.
- [ ] I can use `includes()` and `indexOf()`.
- [ ] I can traverse arrays with loops.
- [ ] I can pass arrays to functions.
- [ ] I can work with nested arrays.