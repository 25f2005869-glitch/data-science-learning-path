# ⚡ Day 052 — ES6 Features — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 052  
**Topic:** ES6 Features

---

# 🔹 ES6

ES6 = ECMAScript 2015.

It introduced many modern JavaScript features.

---

# 🔹 let and const

    let score = 90;
    score = 95;

    const course = "MAD 1";

`let` → reassignment allowed.

`const` → reassignment not allowed.

Both → block scoped.

---

# 🔹 Arrow Function

Traditional:

    function add(a, b) {
        return a + b;
    }

Arrow:

    const add = (a, b) => a + b;

Single parameter:

    const square = x => x * x;

---

# 🔹 Template Literal

    const name = "Saloni";

    const message = `Hello, ${name}!`;

Uses backticks.

Interpolation uses:

    ${expression}

---

# 🔹 Default Parameter

    function greet(name = "Student") {
        return `Hello ${name}`;
    }

---

# 🔹 Array Destructuring

    const marks = [90, 80, 95];

    const [a, b, c] = marks;

---

# 🔹 Object Destructuring

    const student = {
        name: "Saloni",
        score: 95
    };

    const { name, score } = student;

---

# 🔹 Spread Operator

Expand values.

    const a = [1, 2];
    const b = [3, 4];

    const result = [...a, ...b];

Result:

    [1, 2, 3, 4]

---

# 🔹 Rest Parameter

Collect values.

    function total(...numbers) {
        return numbers;
    }

    total(10, 20, 30);

Result:

    [10, 20, 30]

---

# 🔹 Spread vs Rest

    Spread → Expand

    Rest → Collect

---

# 🔹 Object Shorthand

Instead of:

    const name = "Saloni";

    const student = {
        name: name
    };

Write:

    const student = {
        name
    };

---

# 🔹 Method Shorthand

    const student = {
        greet() {
            return "Hello";
        }
    };

---

# 🔹 for...of

Iterates over values.

    for (const item of items) {
        console.log(item);
    }

---

# 🔹 for...in

Iterates over property keys.

    for (const key in object) {
        console.log(key);
    }

---

# 🔹 Optional Chaining

    student.profile?.name

Returns `undefined` instead of throwing an error when an intermediate value is `null` or `undefined`.

---

# 🔹 Nullish Coalescing

    const score = value ?? 0;

Fallback is used only when `value` is:

- `null`
- `undefined`

---

# 🔹 Classes

    class Student {
        constructor(name) {
            this.name = name;
        }

        greet() {
            return `Hello ${this.name}`;
        }
    }

---

# 🔹 Modules

Export:

    export const course = "MAD 1";

Import:

    import { course } from "./course.js";

---

# 🔹 Important Comparison

| Feature | Purpose |
|---|---|
| `let` | Block-scoped variable |
| `const` | Block-scoped constant binding |
| `=>` | Arrow function |
| `` ` ` `` | Template literal |
| `...` | Spread or rest |
| Destructuring | Extract values |
| `for...of` | Iterate values |
| `?.` | Safe property access |
| `??` | Nullish fallback |
| `class` | Class syntax |
| `import/export` | Modules |

---

# 🧠 Golden Rules

1. Prefer `const`.
2. Use `let` when reassignment is needed.
3. Use template literals for interpolation.
4. Remember: Spread expands, Rest collects.
5. Destructuring extracts values.
6. `for...of` gives values.
7. `for...in` gives keys.
8. `?.` handles optional access.
9. `??` handles nullish values.
10. Prefer readability over unnecessarily short syntax.