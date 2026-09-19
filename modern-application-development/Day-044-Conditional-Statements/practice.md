# 🧪 Day 044 — Conditional Statements Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 044  
**Topic:** Conditional Statements

---

# 🎯 Practice Objectives

- Practice JavaScript decision-making.
- Use `if`, `else if` and `else`.
- Practice logical conditions.
- Practice `switch`.
- Understand truthy and falsy values.
- Use the ternary operator.
- Solve real-world decision problems.

---

# Part A — Concept Questions

### 1. What is a conditional statement?

### 2. Why are conditional statements required?

### 3. What is the purpose of `if`?

### 4. What is the purpose of `else`?

### 5. When should `else if` be used?

### 6. What is a nested `if`?

### 7. What is the purpose of `switch`?

### 8. What is a `case`?

### 9. Why is `break` commonly used in a `switch`?

### 10. What is `default`?

### 11. How does `switch` compare a value with a case?

### 12. What is a truthy value?

### 13. What is a falsy value?

### 14. Name the common falsy values in JavaScript.

### 15. When should you use a ternary operator?

### 16. Why is `===` preferred over `==` in most comparisons?

### 17. What is short-circuit evaluation?

### 18. Why can too much nested `if` code be problematic?

### 19. When is `switch` better than `if...else`?

### 20. Why is condition order important?

---

# Part B — Predict the Output

### 21.

    let age = 20;

    if (age >= 18) {
        console.log("Adult");
    }

### 22.

    let age = 16;

    if (age >= 18) {
        console.log("Adult");
    } else {
        console.log("Minor");
    }

### 23.

    let marks = 85;

    if (marks >= 90) {
        console.log("A");
    } else if (marks >= 75) {
        console.log("B");
    } else {
        console.log("C");
    }

### 24.

    console.log(Boolean("Hello"));

### 25.

    console.log(Boolean(""));

### 26.

    console.log(Boolean(0));

### 27.

    console.log(Boolean(100));

### 28.

    console.log(Boolean(null));

### 29.

    console.log(Boolean([]));

### 30.

    let value = 5;

    if (value === "5") {
        console.log("String");
    } else {
        console.log("Not a string");
    }

---

# Part C — Write Conditions

### 31.

Write a condition that checks whether `age` is at least 18.

### 32.

Write a condition that checks whether `marks` are less than 40.

### 33.

Write a condition that checks whether `score` is between 40 and 100.

### 34.

Write a condition that checks whether a user is both:

- At least 18 years old
- Has an ID

### 35.

Write a condition that checks whether a user is either:

- A student
- A teacher

---

# Part D — `if...else`

### 36.

Write a program that checks whether a number is positive or negative.

### 37.

Write a program that checks whether a number is even or odd.

### 38.

Write a program that checks whether a student has passed.

Passing marks:

    40

### 39.

Write a program that checks whether a person is eligible to vote.

Assume the minimum age is:

    18

### 40.

Write a program that checks whether a number is zero or non-zero.

---

# Part E — `else if`

### 41.

Create a grade system:

    90+ → A
    75–89 → B
    60–74 → C
    40–59 → D
    Below 40 → Fail

### 42.

Create a temperature classification:

    35+ → Hot
    25–34 → Warm
    15–24 → Moderate
    Below 15 → Cold

### 43.

Create an age classification:

    0–12 → Child
    13–17 → Teenager
    18–59 → Adult
    60+ → Senior

---

# Part F — `switch`

### 44.

Create a `switch` statement for:

    1 → Monday
    2 → Tuesday
    3 → Wednesday
    4 → Thursday
    5 → Friday
    6 → Saturday
    7 → Sunday

### 45.

Create a `switch` for these roles:

    "student"
    "teacher"
    "admin"

### 46.

Create a `switch` for a calculator menu:

    1 → Add
    2 → Subtract
    3 → Multiply
    4 → Divide

Include `default`.

---

# Part G — Ternary Operator

### 47.

Use a ternary operator to determine:

    Adult
    Minor

### 48.

Use a ternary operator to determine:

    Pass
    Fail

### 49.

Use a ternary operator to determine whether a number is:

    Even
    Odd

---

# Part H — Debugging

### 50. Find the error.

    if (age = 18) {
        console.log("Adult");
    }

### 51. Find the error.

    if (marks >= 40) {
        console.log("Pass");
    } else if (marks >= 90) {
        console.log("Excellent");
    }

Why is the order problematic?

### 52. Find the error.

    if (40 <= marks <= 100) {
        console.log("Valid");
    }

Write the correct condition.

### 53. Find the problem.

    switch (choice) {
        case 1:
            console.log("One");

        case 2:
            console.log("Two");
    }

What happens if `choice` is `1`?

### 54. Improve this condition:

    if (isLoggedIn === true) {
        console.log("Welcome");
    }

---

# Part I — Mini Challenge

## 🎓 Student Grade and Eligibility System

Create a JavaScript program that stores:

- Student name
- Age
- Marks
- Student status
- ID availability

The program should:

1. Check whether the student is an adult.
2. Check whether the student passed.
3. Calculate a grade.
4. Check whether the student is eligible for a particular activity.
5. Display the result in the browser.
6. Print all decisions to the console.

Use:

- `if`
- `else if`
- `else`
- `&&`
- `||`
- `===`
- Ternary operator

Also create a `switch` example for the student's role.

---

# 🏆 Final Challenge

Build a simple **Student Result Checker** webpage.

The user should enter:

- Name
- Age
- Marks

JavaScript should determine:

- Adult or Minor
- Pass or Fail
- Grade
- Eligibility status

Display the result dynamically on the webpage.

---

# ✅ Final Checklist

- [ ] I understand `if`.
- [ ] I understand `if...else`.
- [ ] I understand `else if`.
- [ ] I can create nested conditions.
- [ ] I can combine conditions.
- [ ] I understand truthy values.
- [ ] I understand falsy values.
- [ ] I can use `switch`.
- [ ] I understand `case`.
- [ ] I understand `break`.
- [ ] I understand `default`.
- [ ] I can use the ternary operator.
- [ ] I can write grade conditions.
- [ ] I can solve eligibility problems.
- [ ] I can debug conditional statements.

---

## Navigation

⬅️ Previous: Day 043 — Operators and Expressions  
➡️ Next: Day 045 — Loops