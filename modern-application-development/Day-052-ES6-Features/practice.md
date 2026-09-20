# 🧪 Day 052 — ES6 Features — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 052  
**Topic:** ES6 Features

---

# 🎯 Practice Objectives

Practice:

- `let` and `const`
- Arrow functions
- Template literals
- Default parameters
- Destructuring
- Spread operator
- Rest parameters
- Object shorthand
- `for...of`
- Optional chaining
- Nullish coalescing
- Classes

---

# 🟢 Level 1 — Basics

## Q1

What does ES6 stand for?

---

## Q2

When should you use `const` instead of `let`?

---

## Q3

Convert this function into an arrow function:

    function square(x) {
        return x * x;
    }

---

## Q4

Create a template literal that prints a student's name and score.

---

## Q5

Create a function with a default parameter called `name`.

---

# 🟡 Level 2 — Destructuring

## Q6

Extract the first and second values:

    const marks = [90, 85, 95];

---

## Q7

Extract `name` and `course`:

    const student = {
        name: "Saloni",
        course: "MAD 1",
        score: 95
    };

---

## Q8

Rename the destructured property `name` to `studentName`.

---

## Q9

Use a default value of `0` for a missing `score` property.

---

# 🟠 Level 3 — Spread and Rest

## Q10

Combine these arrays using spread:

    const frontend = ["HTML", "CSS"];
    const backend = ["Python", "Flask"];

---

## Q11

Create a copy of an array using spread.

---

## Q12

Add a new property to an existing object using object spread.

---

## Q13

Create a function that accepts any number of numbers using a rest parameter.

---

## Q14

Explain the difference between spread and rest.

---

# 🟠 Level 4 — Predict the Output

## Q15

What is the output?

    const name = "Saloni";
    console.log(`Hello, ${name}!`);

---

## Q16

What is the output?

    const numbers = [10, 20, 30];

    const [first, ...remaining] = numbers;

    console.log(first);
    console.log(remaining);

---

## Q17

What is the output?

    const value = 0;

    console.log(value || 100);
    console.log(value ?? 100);

---

## Q18

What happens?

    const student = {
        profile: {
            name: "Saloni"
        }
    };

    console.log(student.address?.city);

---

# 🔴 Level 5 — Conceptual Questions

## Q19

What is destructuring?

---

## Q20

What is the spread operator?

---

## Q21

What is a rest parameter?

---

## Q22

What is the difference between `for...of` and `for...in`?

---

## Q23

What is optional chaining?

---

## Q24

What is nullish coalescing?

---

## Q25

What is the difference between `||` and `??`?

---

# 💻 Coding Practice

## Task 1 — Student Profile

Create a student object containing:

- Name
- Age
- Course
- Score
- Skills

Use object destructuring to extract the values.

---

## Task 2 — Skill Combination

Create two arrays:

- Frontend skills
- Programming skills

Combine them into one array using the spread operator.

---

## Task 3 — Total Marks

Create a function using rest parameters that accepts any number of marks and returns their total.

---

## Task 4 — Student Message

Use a template literal to generate:

    Student: <name>
    Course: <course>
    Score: <score>

---

## Task 5 — Optional Data

Create a student object where `address` may not exist.

Use optional chaining to safely access the city.

---

## Task 6 — Default Score

Use `??` to assign `0` when a student's score is `null` or `undefined`.

---

## Task 7 — Class

Create a `Student` class with:

- `name`
- `course`
- `score`
- `greet()` method
- `getResult()` method

---

# ⭐ Final Challenge

Create a Student Management example using at least six ES6 features.

Your program should include:

- `const` / `let`
- Arrow function
- Template literal
- Destructuring
- Spread operator
- Rest parameter
- `for...of`
- Optional chaining or `??`

---

# ✅ Self-Check

Before moving to Day 053, make sure you can explain:

- [ ] ES6
- [ ] `let`
- [ ] `const`
- [ ] Arrow functions
- [ ] Template literals
- [ ] Default parameters
- [ ] Array destructuring
- [ ] Object destructuring
- [ ] Spread operator
- [ ] Rest parameters
- [ ] Object shorthand
- [ ] `for...of`
- [ ] Optional chaining
- [ ] Nullish coalescing
- [ ] Classes
- [ ] Modules basics

---

## 📌 Goal

Write modern JavaScript confidently instead of only memorizing ES6 syntax.