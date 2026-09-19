# 📝 Day 047 — Strings and Template Literals — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 047  
**Topic:** Strings and Template Literals

---

# Part A — Basic Questions

1. What is a string?
2. What are the three common ways to create strings?
3. What is string indexing?
4. From which number does string indexing start?
5. What does the `length` property return?
6. How can you access the last character of a string?
7. What does it mean that strings are immutable?
8. What is string concatenation?
9. What is a template literal?
10. Which character is used to create a template literal?
11. What is string interpolation?
12. What is the purpose of `${}`?
13. What does `trim()` do?
14. What does `includes()` return?
15. What does `indexOf()` return when text is not found?

---

# Part B — Predict the Output

## Question 1

    const word = "JavaScript";

    console.log(word[0]);
    console.log(word[word.length - 1]);

Write the output.

---

## Question 2

    const name = "saloni";

    console.log(name.toUpperCase());

Write the output.

---

## Question 3

    const text = "  Hello World  ";

    console.log(text.trim());

Write the output.

---

## Question 4

    const text = "JavaScript";

    console.log(text.includes("Script"));

Write the output.

---

## Question 5

    const text = "JavaScript";

    console.log(text.slice(0, 4));

Write the output.

---

## Question 6

    const name = "Saloni";
    const course = "MAD 1";

    console.log(`Name: ${name}, Course: ${course}`);

Write the output.

---

# Part C — String Practice

## Task 1

Create a string containing your name and print it.

## Task 2

Print the length of your name.

## Task 3

Print the first character of your name.

## Task 4

Print the last character of your name.

## Task 5

Convert your name to uppercase.

## Task 6

Convert your name to lowercase.

## Task 7

Create a string containing extra spaces and remove them using `trim()`.

## Task 8

Check whether the string contains the word `"JavaScript"`.

---

# Part D — String Methods

## Task 9

Use `startsWith()` to check whether:

    "Modern Application Development"

starts with `"Modern"`.

## Task 10

Use `endsWith()` to check whether:

    "index.html"

ends with `".html"`.

## Task 11

Find the position of `"Script"` in:

    "JavaScript"

using `indexOf()`.

## Task 12

Extract `"Java"` from:

    "JavaScript"

using `slice()`.

## Task 13

Replace `"Python"` with `"JavaScript"` in:

    "I am learning Python"

## Task 14

Convert:

    "DBMS,PDSA,MLF,MAD1"

into an array using `split()`.

---

# Part E — Template Literals

## Task 15

Create variables for:

- Name
- Age
- Programme

Use a template literal to display all three.

## Task 16

Create a template literal that calculates:

    10 + 20

inside `${}`.

## Task 17

Create a multiline message using a template literal.

## Task 18

Create a function that returns a greeting using a template literal.

Example:

    greet("Saloni")

Expected style:

    Hello Saloni, welcome to JavaScript!

---

# Part F — Functions and Strings

## Task 19

Create a function that accepts a name and returns the name in uppercase.

## Task 20

Create a function that accepts a string and returns its length.

## Task 21

Create a function that checks whether a string contains `"JavaScript"`.

## Task 22

Create a function that extracts the first five characters of a string.

---

# Part G — Loops and Strings

## Task 23

Print every character of:

    "JavaScript"

using a `for` loop.

## Task 24

Count the number of vowels in:

    "JavaScript"

## Task 25

Count the number of spaces in:

    "Modern Application Development"

## Task 26

Reverse a string using a loop.

Example:

    "Hello"

Expected:

    "olleH"

---

# Part H — Challenge

## Challenge 1 — Student Profile

Create:

    const name = "Saloni Tiwari";
    const programme = "IIT Madras BS Degree";
    const course = "Modern Application Development";
    const day = 47;

Use a template literal to generate a complete profile message.

---

## Challenge 2 — Text Analyzer

Create a program that accepts a sentence and displays:

- Original text
- Number of characters
- Uppercase text
- Lowercase text
- Whether it contains `"JavaScript"`
- First character
- Last character

---

## Challenge 3 — Email Checker

Create a function that checks whether an email:

- Contains `"@"`
- Ends with a valid-looking domain such as `".com"` or `".in"`

Return an appropriate message.

---

## Challenge 4 — Student Result Message

Create a function that accepts:

- Student name
- Marks
- Subject

Return a template literal such as:

    Saloni scored 85 marks in PDSA.

---

## Challenge 5 — Course List

Create an array of courses and use a loop with template literals to display:

    Course 1: DBMS
    Course 2: PDSA
    Course 3: MLF
    Course 4: MAD1

---

# 🎯 Revision Checklist

- [ ] I understand strings.
- [ ] I understand string indexing.
- [ ] I can use `length`.
- [ ] I can concatenate strings.
- [ ] I can use common string methods.
- [ ] I understand `slice()`.
- [ ] I understand `split()`.
- [ ] I understand template literals.
- [ ] I can use `${}` interpolation.
- [ ] I can create multiline strings.
- [ ] I can combine strings with functions.
- [ ] I can combine strings with loops.