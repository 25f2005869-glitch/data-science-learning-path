# 📝 Day 050 — Array Methods — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 050  
**Topic:** Array Methods

---

# Part A — Basic Questions

1. What are array methods?
2. What is a callback function?
3. What does `forEach()` do?
4. What does `map()` do?
5. What does `filter()` do?
6. What does `find()` return?
7. What does `findIndex()` return?
8. What is the difference between `find()` and `filter()`?
9. What does `some()` check?
10. What does `every()` check?
11. What does `reduce()` do?
12. What is an accumulator in `reduce()`?
13. Why is a comparison function needed for numerical `sort()`?
14. What does `reverse()` do?
15. What is method chaining?
16. Which common array methods mutate the original array?

---

# Part B — Predict the Output

## Question 1

    const numbers = [1, 2, 3];

    const result = numbers.map(number => number * 2);

    console.log(result);

Write the output.

---

## Question 2

    const numbers = [10, 20, 30, 40];

    const result = numbers.filter(number => number >= 25);

    console.log(result);

Write the output.

---

## Question 3

    const numbers = [10, 20, 30, 40];

    const result = numbers.find(number => number > 15);

    console.log(result);

Write the output.

---

## Question 4

    const numbers = [10, 20, 30];

    console.log(numbers.some(number => number > 25));

Write the output.

---

## Question 5

    const numbers = [10, 20, 30];

    console.log(numbers.every(number => number > 5));

Write the output.

---

## Question 6

    const numbers = [10, 20, 30];

    const total = numbers.reduce(
        (sum, number) => sum + number,
        0
    );

    console.log(total);

Write the output.

---

# Part C — forEach()

## Task 1

Use `forEach()` to print every element of:

    ["DBMS", "PDSA", "MLF"]

## Task 2

Use `forEach()` to print every element with its index.

## Task 3

Use `forEach()` to print:

    Subject 1: DBMS
    Subject 2: PDSA
    Subject 3: MLF

---

# Part D — map()

## Task 4

Double every number:

    [1, 2, 3, 4, 5]

## Task 5

Square every number:

    [2, 4, 6, 8]

## Task 6

Add 5 marks to every mark:

    [70, 75, 80, 85]

## Task 7

Convert the following names to uppercase:

    ["saloni", "asha", "riya"]

---

# Part E — filter()

## Task 8

Find all even numbers:

    [1, 2, 3, 4, 5, 6, 7, 8]

## Task 9

Find all numbers greater than 50:

    [20, 75, 45, 90, 60]

## Task 10

Find passing marks from:

    [35, 45, 67, 30, 89, 40]

Use 40 as the passing mark.

---

# Part F — find() and findIndex()

## Task 11

Find the first number greater than 50.

    [20, 40, 65, 80, 90]

## Task 12

Find the index of the first number greater than 50.

## Task 13

Find the first student whose marks are greater than or equal to 90.

    [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 92 },
        { name: "Neha", marks: 88 }
    ]

---

# Part G — some() and every()

## Task 14

Check whether at least one mark is greater than 90.

## Task 15

Check whether every mark is greater than or equal to 40.

## Task 16

Check whether at least one student scored exactly 100.

---

# Part H — reduce()

## Task 17

Calculate the total:

    [10, 20, 30, 40]

## Task 18

Calculate the product:

    [2, 3, 4]

## Task 19

Calculate the total marks:

    [85, 90, 78, 92, 88]

## Task 20

Calculate the average using `reduce()` and `length`.

---

# Part I — sort() and reverse()

## Task 21

Sort:

    [40, 10, 30, 20]

in ascending order.

## Task 22

Sort the same array in descending order.

## Task 23

Sort:

    ["MLF", "DBMS", "PDSA", "MAD1"]

alphabetically.

## Task 24

Reverse:

    [1, 2, 3, 4, 5]

---

# Part J — Method Chaining

## Task 25

From:

    [1, 2, 3, 4, 5, 6]

select even numbers and then double them.

## Task 26

From:

    [10, 15, 20, 25, 30]

select numbers greater than 15 and then square them.

## Task 27

From the following students, select students who passed and return only their names:

    [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 35 },
        { name: "Neha", marks: 72 }
    ]

---

# Part K — Challenge

## Challenge 1 — Student Marks Analyzer

Use:

    const marks = [85, 90, 38, 72, 95, 65];

Use array methods to calculate:

- Total
- Average
- Highest
- Lowest
- Passing marks
- Number of passing students
- Whether everyone passed
- Whether anyone scored above 90

---

## Challenge 2 — Student Database

Use:

    const students = [
        { name: "Asha", marks: 85 },
        { name: "Riya", marks: 92 },
        { name: "Neha", marks: 35 },
        { name: "Pooja", marks: 78 },
        { name: "Kiran", marks: 95 }
    ];

Perform:

- Get all names using `map()`.
- Get passing students using `filter()`.
- Find the first student scoring above 90.
- Find the index of the first student scoring above 90.
- Check whether anyone scored 95.
- Check whether everyone passed.
- Calculate total marks using `reduce()`.

---

## Challenge 3 — Course Processing

Use:

    const courses = [
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "SQLite"
    ];

Use array methods to:

- Convert all courses to uppercase.
- Find courses containing `"Script"`.
- Check whether `"Flask"` exists.
- Find the index of `"JavaScript"`.
- Create a numbered list using `map()`.

---

## Challenge 4 — Product Analyzer

Create an array of product objects containing:

- Name
- Price
- Category

Use array methods to:

- Find products above a given price.
- Find the first product in a category.
- Calculate total price.
- Extract all product names.
- Check whether every product has a positive price.

---

# 🎯 Revision Checklist

- [ ] I understand callback functions.
- [ ] I can use `forEach()`.
- [ ] I can use `map()`.
- [ ] I can use `filter()`.
- [ ] I can use `find()`.
- [ ] I can use `findIndex()`.
- [ ] I understand `some()`.
- [ ] I understand `every()`.
- [ ] I can use `reduce()`.
- [ ] I can sort numbers correctly.
- [ ] I understand `reverse()`.
- [ ] I understand mutating methods.
- [ ] I can chain array methods.
- [ ] I can process arrays of objects.