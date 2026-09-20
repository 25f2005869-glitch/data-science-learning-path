# 📝 Day 052 — ES6 Features — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 052  
**Topic:** ES6 Features

---

# 1. What is ES6?

ES6 stands for ECMAScript 2015.

It is a major version of the JavaScript language specification released in 2015.

ES6 introduced many features that made JavaScript more modern, readable, and powerful.

Important ES6 features include:

- `let`
- `const`
- Arrow functions
- Template literals
- Default parameters
- Destructuring
- Spread operator
- Rest parameters
- Classes
- Modules
- Promises
- `for...of`

---

# 2. let and const

ES6 introduced `let` and `const`.

Example:

    let score = 80;
    score = 90;

    const course = "MAD 1";

`let` allows reassignment.

`const` does not allow reassignment.

Both are block-scoped.

---

# 3. Arrow Functions

Arrow functions provide shorter syntax for writing functions.

Traditional function:

    function add(a, b) {
        return a + b;
    }

Arrow function:

    const add = (a, b) => {
        return a + b;
    };

For a single expression, the return can be implicit:

    const add = (a, b) => a + b;

---

# 4. Single Parameter Arrow Function

Parentheses can be omitted when there is exactly one parameter.

Example:

    const square = x => x * x;

However, parentheses are still allowed:

    const square = (x) => x * x;

---

# 5. Arrow Functions and this

Arrow functions do not create their own `this`.

They use `this` from the surrounding lexical scope.

This is one important difference between arrow functions and regular functions.

Example:

    const student = {
        name: "Saloni",

        greet() {
            const message = () => {
                console.log(this.name);
            };

            message();
        }
    };

    student.greet();

The arrow function gets `this` from the surrounding `greet()` method.

---

# 6. Template Literals

Template literals use backticks.

Example:

    const name = "Saloni";

    const message = `Hello, ${name}!`;

Template literals make string interpolation easier.

---

# 7. Expressions in Template Literals

Expressions can be placed inside `${}`.

Example:

    const marks = 90;

    const message = `Marks: ${marks}`;
    const result = `Total: ${80 + 10}`;

Function calls can also be used:

    const name = "saloni";

    console.log(`Name: ${name.toUpperCase()}`);

---

# 8. Multiline Template Literals

Template literals can contain multiple lines.

Example:

    const message = `
    Welcome to MAD 1.
    Today we are learning ES6.
    `;

This is useful when constructing formatted text.

---

# 9. Default Parameters

A function can have default values for parameters.

Example:

    function greet(name = "Student") {
        return `Hello, ${name}`;
    }

    console.log(greet());

If no argument is provided, `"Student"` is used.

---

# 10. Destructuring

Destructuring allows values to be extracted from arrays or objects into variables.

There are two major forms:

- Array destructuring
- Object destructuring

---

# 11. Array Destructuring

Example:

    const marks = [90, 85, 95];

    const [first, second, third] = marks;

Now:

    first = 90
    second = 85
    third = 95

---

# 12. Skipping Array Values

Values can be skipped using commas.

Example:

    const numbers = [10, 20, 30];

    const [first, , third] = numbers;

Result:

    first = 10
    third = 30

---

# 13. Rest with Array Destructuring

Example:

    const numbers = [10, 20, 30, 40];

    const [first, ...remaining] = numbers;

Now:

    first = 10

    remaining = [20, 30, 40]

---

# 14. Object Destructuring

Example:

    const student = {
        name: "Saloni",
        age: 17,
        course: "MAD 1"
    };

    const { name, age, course } = student;

The properties are extracted into variables.

---

# 15. Renaming During Object Destructuring

Example:

    const student = {
        name: "Saloni"
    };

    const { name: studentName } = student;

The variable is called `studentName`.

---

# 16. Default Values in Destructuring

Example:

    const student = {
        name: "Saloni"
    };

    const { name, score = 0 } = student;

Because `score` does not exist, its default value is `0`.

---

# 17. Spread Operator

The spread operator is written as `...`.

It expands iterable values or object properties.

Example:

    const numbers = [10, 20, 30];

    const copy = [...numbers];

The elements of `numbers` are copied into a new array.

---

# 18. Combining Arrays with Spread

Example:

    const frontend = ["HTML", "CSS"];
    const programming = ["JavaScript", "Python"];

    const skills = [...frontend, ...programming];

Result:

    ["HTML", "CSS", "JavaScript", "Python"]

---

# 19. Spread with Objects

Example:

    const student = {
        name: "Saloni",
        course: "MAD 1"
    };

    const updatedStudent = {
        ...student,
        score: 95
    };

The new object contains the existing properties plus `score`.

---

# 20. Rest Parameters

Rest parameters also use `...`.

They collect multiple arguments into an array.

Example:

    function total(...numbers) {
        return numbers.reduce((sum, number) => sum + number, 0);
    }

    console.log(total(10, 20, 30));

Result:

    60

---

# 21. Spread vs Rest

The syntax is the same, but the purpose is different.

Spread:

    const numbers = [10, 20, 30];

    console.log(...numbers);

It expands values.

Rest:

    function total(...numbers) {
        console.log(numbers);
    }

It collects values.

Remember:

    Spread → Expand

    Rest → Collect

---

# 22. Enhanced Object Literals

ES6 provides shorter syntax for objects.

Instead of:

    const name = "Saloni";

    const student = {
        name: name
    };

You can write:

    const name = "Saloni";

    const student = {
        name
    };

This is called property shorthand.

---

# 23. Method Shorthand

Traditional syntax:

    const student = {
        greet: function () {
            return "Hello";
        }
    };

ES6 syntax:

    const student = {
        greet() {
            return "Hello";
        }
    };

---

# 24. Computed Property Names

Object property names can be created dynamically.

Example:

    const key = "score";

    const student = {
        [key]: 95
    };

The resulting object contains:

    {
        score: 95
    }

---

# 25. for...of

`for...of` is useful for iterating over iterable values such as arrays and strings.

Example:

    const courses = ["HTML", "CSS", "JavaScript"];

    for (const course of courses) {
        console.log(course);
    }

---

# 26. for...of vs for...in

`for...of` generally iterates over values.

    const numbers = [10, 20, 30];

    for (const number of numbers) {
        console.log(number);
    }

`for...in` iterates over property keys.

    for (const index in numbers) {
        console.log(index);
    }

Use the appropriate loop for the task.

---

# 27. Optional Chaining

Optional chaining uses `?.`.

It allows safe access to properties that may not exist.

Example:

    const student = {
        profile: {
            name: "Saloni"
        }
    };

    console.log(student.profile?.name);

If an intermediate property is `null` or `undefined`, optional chaining prevents a property-access error.

Example:

    console.log(student.address?.city);

If `address` does not exist, the result is `undefined`.

---

# 28. Nullish Coalescing

The nullish coalescing operator is `??`.

It provides a fallback only when the left side is `null` or `undefined`.

Example:

    const score = null;

    const finalScore = score ?? 0;

Result:

    0

---

# 29. ?? vs ||

These operators are not identical.

Example:

    const value = 0;

    console.log(value || 100);

Result:

    100

But:

    console.log(value ?? 100);

Result:

    0

`||` considers many falsy values.

`??` only checks for `null` or `undefined`.

---

# 30. Classes

ES6 introduced class syntax.

Example:

    class Student {
        constructor(name) {
            this.name = name;
        }

        greet() {
            return `Hello, ${this.name}`;
        }
    }

    const student = new Student("Saloni");

Classes provide a cleaner syntax for creating objects and working with prototypes.

---

# 31. Modules

ES6 introduced JavaScript modules.

Export:

    export const course = "MAD 1";

Import:

    import { course } from "./course.js";

Modules allow code to be divided into reusable files.

---

# 32. Why ES6 Matters

ES6 features make JavaScript:

- More readable
- More concise
- Easier to maintain
- Better for large applications
- More expressive
- Easier to organize

Modern JavaScript uses many of these features regularly.

---

# 33. Best Practices

- Prefer `const` when reassignment is not required.
- Use `let` when reassignment is needed.
- Use arrow functions for concise callbacks.
- Use template literals instead of complex string concatenation.
- Use destructuring when it improves readability.
- Use spread to create shallow copies.
- Use rest parameters for variable-length function arguments.
- Use `for...of` when you need iterable values.
- Use optional chaining for safely accessing optional properties.
- Use `??` when the fallback should apply only to `null` or `undefined`.
- Keep modern syntax readable rather than using it only to make code shorter.

---

# 34. ES6 Quick Mental Model

    let / const
        ↓
    Modern variable declarations

    Arrow Functions
        ↓
    Shorter functions

    Template Literals
        ↓
    Better strings

    Destructuring
        ↓
    Extract values

    Spread
        ↓
    Expand values

    Rest
        ↓
    Collect values

    for...of
        ↓
    Iterate over values

    ?. 
        ↓
    Safe property access

    ??
        ↓
    Nullish fallback