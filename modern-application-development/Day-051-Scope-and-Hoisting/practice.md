# 🧪 Day 051 — Scope and Hoisting — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 051  
**Topic:** Scope and Hoisting

---

# 🎯 Practice Objectives

Practice:

- Global scope
- Function scope
- Block scope
- Scope chain
- Shadowing
- `var`
- `let`
- `const`
- Hoisting
- Temporal Dead Zone
- Function hoisting

---

# 🟢 Level 1 — Scope Basics

## Q1

Identify the scope of `name`.

    let name = "Saloni";

---

## Q2

What type of scope does `var` have inside a function?

---

## Q3

What type of scope do `let` and `const` have?

---

## Q4

Can a function access a variable declared in an outer scope?

---

## Q5

Can an outer scope directly access a variable declared inside a function?

---

# 🟡 Level 2 — Predict the Output

## Q6

What is the output?

    let name = "Global";

    function show() {
        let name = "Local";
        console.log(name);
    }

    show();

---

## Q7

What happens here?

    if (true) {
        let score = 90;
    }

    console.log(score);

---

## Q8

What is the output?

    console.log(value);
    var value = 100;

---

## Q9

What happens here?

    console.log(value);
    let value = 100;

---

## Q10

What happens here?

    console.log(course);
    const course = "MAD 1";

---

# 🟠 Level 3 — Scope Chain

## Q11

Predict the output.

    let a = 10;

    function outer() {
        let b = 20;

        function inner() {
            let c = 30;

            console.log(a);
            console.log(b);
            console.log(c);
        }

        inner();
    }

    outer();

---

## Q12

Explain the scope lookup order in the previous example.

---

## Q13

Identify the variable that is shadowed.

    let course = "HTML";

    function learn() {
        let course = "JavaScript";
        console.log(course);
    }

    learn();

---

# 🔴 Level 4 — Hoisting

## Q14

Predict the output.

    greet();

    function greet() {
        console.log("Hello");
    }

---

## Q15

What happens?

    greet();

    const greet = function () {
        console.log("Hello");
    };

---

## Q16

What happens?

    show();

    const show = () => {
        console.log("Hello");
    };

---

## Q17

Explain why `var` can produce `undefined` before initialization while `let` produces a `ReferenceError`.

---

# 🧠 Conceptual Questions

## Q18

Define scope in your own words.

---

## Q19

What is lexical scope?

---

## Q20

What is the scope chain?

---

## Q21

What is variable shadowing?

---

## Q22

What is hoisting?

---

## Q23

What is the Temporal Dead Zone?

---

## Q24

Why is `const` generally preferred when reassignment is not required?

---

## Q25

Why should unnecessary global variables be avoided?

---

# 💻 Coding Practice

## Task 1 — Student Scope Demo

Create a program containing:

- A global student name
- A function
- A local score
- A block-scoped grade
- Console output demonstrating the scopes

---

## Task 2 — Scope Chain

Create three nested scopes.

The innermost function should access:

- A local variable
- A variable from the outer function
- A global variable

---

## Task 3 — Shadowing

Create a global variable called `course`.

Create another variable with the same name inside a function.

Print both values.

---

## Task 4 — Hoisting Experiment

Create separate examples demonstrating:

- `var` before declaration
- `let` before declaration
- `const` before declaration
- Function declaration before declaration

Observe the results in the browser console.

---

# ✅ Self-Check

Before moving to Day 052, make sure you can explain:

- [ ] Global scope
- [ ] Function scope
- [ ] Block scope
- [ ] Lexical scope
- [ ] Scope chain
- [ ] Variable shadowing
- [ ] `var` scope
- [ ] `let` scope
- [ ] `const` scope
- [ ] Hoisting
- [ ] Temporal Dead Zone
- [ ] Function declaration hoisting
- [ ] Function expression behavior
- [ ] Arrow function behavior

---

# ⭐ Final Challenge

Without running the code, predict the result:

    var a = 10;

    function test() {
        console.log(a);

        var a = 20;

        if (true) {
            let a = 30;
            console.log(a);
        }

        console.log(a);
    }

    test();

Then run the program in the browser console and compare your answer.

---

## 📌 Goal

Understand **why** JavaScript produces the result, not just what the result is.