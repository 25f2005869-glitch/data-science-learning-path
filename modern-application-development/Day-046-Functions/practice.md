# 📝 Day 046 — Functions — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 046  
**Topic:** Functions

---

# Part A — Basic Questions

1. What is a function?
2. Why are functions useful?
3. What is a function declaration?
4. What is a function call?
5. What is a parameter?
6. What is an argument?
7. What does `return` do?
8. What is a default parameter?
9. What is a function expression?
10. What is an arrow function?
11. What is the difference between `console.log()` and `return`?
12. What is function scope?
13. What is a global variable?
14. Why should unnecessary global variables be avoided?
15. Why should functions have meaningful names?

---

# Part B — Predict the Output

## Question 1

    function greet() {
        console.log("Hello");
    }

    greet();

Write the output.

---

## Question 2

    function add(a, b) {
        return a + b;
    }

    console.log(add(10, 20));

Write the output.

---

## Question 3

    function square(x) {
        return x * x;
    }

    console.log(square(5));

Write the output.

---

## Question 4

    function greet(name = "Student") {
        return "Hello " + name;
    }

    console.log(greet());
    console.log(greet("Saloni"));

Write the output.

---

## Question 5

    const multiply = (a, b) => a * b;

    console.log(multiply(4, 5));

Write the output.

---

# Part C — Basic Coding

## Task 1

Create a function named `greet()` that prints a welcome message.

## Task 2

Create a function that accepts a name and prints a greeting.

## Task 3

Create a function that accepts two numbers and returns their sum.

## Task 4

Create functions for:

- Addition
- Subtraction
- Multiplication
- Division

## Task 5

Create a function that returns the square of a number.

## Task 6

Create a function that returns the cube of a number.

## Task 7

Create a function that checks whether a number is even or odd.

## Task 8

Create a function that checks whether a student has passed.

Assume marks greater than or equal to 40 are passing.

---

# Part D — Functions and Loops

## Task 9

Create a function that prints numbers from 1 to 10.

## Task 10

Create a function that prints even numbers from 1 to 50.

## Task 11

Create a function that calculates the sum from 1 to `n`.

## Task 12

Create a function that prints the multiplication table of a given number.

Example:

    multiplicationTable(7)

---

# Part E — Functions and Arrays

## Task 13

Create a function that calculates the total of:

    const marks = [80, 75, 90, 85, 70];

## Task 14

Create a function that calculates the average of an array.

## Task 15

Create a function that finds the largest number in an array.

## Task 16

Create a function that counts passing marks.

Use 40 as the passing mark.

---

# Part F — Function Expressions

## Task 17

Create an `add` function expression.

## Task 18

Create a `square` function expression.

## Task 19

Create a `checkAge` function expression that returns:

    "Adult"

or:

    "Minor"

---

# Part G — Arrow Functions

## Task 20

Convert this function into an arrow function:

    function square(x) {
        return x * x;
    }

## Task 21

Create an arrow function that adds two numbers.

## Task 22

Create an arrow function that checks whether a number is positive.

## Task 23

Create an arrow function that calculates the area of a rectangle.

---

# Part H — Challenge

## Challenge 1 — Student Result Analyzer

Create reusable functions for:

- Total marks
- Average marks
- Highest marks
- Lowest marks
- Pass/fail status
- Grade calculation

Use:

    const marks = [85, 90, 78, 92, 88];

---

## Challenge 2 — Calculator

Create separate functions for:

- Addition
- Subtraction
- Multiplication
- Division

Then create one function that displays the result.

---

## Challenge 3 — Factorial

Create a function that calculates factorial using a loop.

Example:

    factorial(5)

Expected result:

    120

---

## Challenge 4 — Prime Number

Create a function that checks whether a number is prime.

---

## Challenge 5 — Reverse String

Create a function that reverses a string using a loop.

Example:

    reverseString("JavaScript")

---

# 🎯 Revision Checklist

- [ ] I understand function declarations.
- [ ] I can call a function.
- [ ] I understand parameters and arguments.
- [ ] I can use `return`.
- [ ] I understand default parameters.
- [ ] I can create function expressions.
- [ ] I can create arrow functions.
- [ ] I understand local and global scope.
- [ ] I can combine functions with loops.
- [ ] I can combine functions with arrays.
- [ ] I can build reusable functions.