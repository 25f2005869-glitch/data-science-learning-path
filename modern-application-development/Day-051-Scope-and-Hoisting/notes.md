# 📝 Day 051 — Scope and Hoisting — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 051  
**Topic:** Scope and Hoisting

---

# 1. What is Scope?

Scope determines where a variable, function, or identifier can be accessed in a JavaScript program.

In simple terms:

> Scope defines the visibility and accessibility of variables.

Example:

    let name = "Saloni";

    console.log(name);

Here, `name` is accessible because it is defined in the current scope.

---

# 2. Types of Scope

JavaScript mainly has:

1. Global Scope
2. Function Scope
3. Block Scope
4. Lexical Scope

---

# 3. Global Scope

A variable declared outside functions and blocks generally belongs to the global scope.

Example:

    let studentName = "Saloni";

    function showName() {
        console.log(studentName);
    }

    showName();

The function can access `studentName` because the variable is available in an outer scope.

---

# 4. Function Scope

Variables declared with `var` inside a function are function-scoped.

Example:

    function test() {
        var score = 90;
        console.log(score);
    }

    test();

`score` cannot normally be accessed outside the function.

---

# 5. Block Scope

A block is code enclosed inside `{ }`.

Examples include:

- `if`
- `for`
- `while`
- standalone blocks

Variables declared using `let` and `const` are block-scoped.

Example:

    if (true) {
        let marks = 95;
        const grade = "A";
        console.log(marks);
        console.log(grade);
    }

`marks` and `grade` are not accessible outside the block.

---

# 6. var vs let vs const Scope

| Keyword | Scope |
|---|---|
| `var` | Function scope |
| `let` | Block scope |
| `const` | Block scope |

Example:

    if (true) {
        var a = 10;
        let b = 20;
        const c = 30;
    }

`a` can be accessed outside the block if the block is inside the same function/global context.

`b` and `c` cannot be accessed outside the block.

---

# 7. Lexical Scope

Lexical scope means that scope is determined by where code is written.

Example:

    let course = "MAD 1";

    function outer() {
        let topic = "JavaScript";

        function inner() {
            console.log(course);
            console.log(topic);
        }

        inner();
    }

    outer();

`inner()` can access variables from its own scope and outer scopes.

---

# 8. Scope Chain

When JavaScript searches for a variable, it starts from the current scope.

If the variable is not found, JavaScript searches the outer scope.

This continues until the global scope is reached.

Example:

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

Search order:

    inner scope
        ↓
    outer scope
        ↓
    global scope

---

# 9. Inner Scope Access

An inner scope can generally access variables from its outer scope.

Example:

    let name = "Saloni";

    function student() {
        console.log(name);
    }

    student();

---

# 10. Outer Scope Cannot Access Inner Variables

The reverse does not work.

Example:

    function student() {
        let marks = 95;
    }

    console.log(marks);

This produces a `ReferenceError` because `marks` belongs to the function scope.

---

# 11. Variable Shadowing

Shadowing occurs when an inner scope declares a variable with the same name as an outer variable.

Example:

    let name = "Global";

    function test() {
        let name = "Local";
        console.log(name);
    }

    test();

Output:

    Local

The inner variable shadows the outer variable.

---

# 12. Scope and var

`var` is function-scoped.

Example:

    function example() {
        if (true) {
            var value = 100;
        }

        console.log(value);
    }

    example();

The variable is accessible because `var` does not create block scope.

---

# 13. Scope and let

`let` is block-scoped.

Example:

    if (true) {
        let value = 100;
        console.log(value);
    }

The variable cannot be accessed outside the block.

---

# 14. Scope and const

`const` is also block-scoped.

Example:

    if (true) {
        const course = "MAD 1";
        console.log(course);
    }

The variable is limited to that block.

---

# 15. What is Hoisting?

Hoisting refers to JavaScript's behavior of processing certain declarations before executing the code.

It is important to understand that JavaScript does not literally move every line of code to the top.

Different declarations behave differently during initialization.

---

# 16. var Hoisting

Declarations made using `var` are hoisted and initialized with `undefined`.

Example:

    console.log(value);
    var value = 50;

Conceptually, the behavior is similar to:

    var value;
    console.log(value);
    value = 50;

Output:

    undefined

---

# 17. let and const Hoisting

`let` and `const` declarations are also processed before execution, but they are not initialized in the same way as `var`.

Accessing them before their declaration causes a `ReferenceError`.

Example:

    console.log(score);
    let score = 90;

This results in a `ReferenceError`.

---

# 18. Temporal Dead Zone (TDZ)

The Temporal Dead Zone is the period between entering a scope and the point where a `let` or `const` variable is initialized.

Example:

    console.log(score);
    let score = 90;

The variable exists in the scope but cannot be accessed before its declaration is initialized.

This period is called the TDZ.

---

# 19. const and TDZ

`const` also has a Temporal Dead Zone.

Example:

    console.log(course);
    const course = "MAD 1";

This produces a `ReferenceError`.

---

# 20. Function Declaration Hoisting

Function declarations are hoisted.

Example:

    greet();

    function greet() {
        console.log("Hello");
    }

The function can be called before its declaration.

---

# 21. Function Expression

Function expressions behave differently.

Example:

    greet();

    const greet = function () {
        console.log("Hello");
    };

This causes a `ReferenceError` because `greet` is declared using `const` and is in the TDZ.

---

# 22. Arrow Functions and Hoisting

Arrow functions assigned to `let` or `const` variables are not callable before their initialization.

Example:

    show();

    const show = () => {
        console.log("Hello");
    };

This produces a `ReferenceError`.

---

# 23. Hoisting Comparison

| Declaration | Hoisted | Initialized Before Declaration |
|---|---|---|
| `var` | Yes | Yes, with `undefined` |
| `let` | Yes | No |
| `const` | Yes | No |
| Function declaration | Yes | Yes |
| Function expression | Depends on variable declaration | No |
| Arrow function | Depends on variable declaration | No |

---

# 24. Scope Chain Example

    let country = "India";

    function outer() {
        let state = "Jharkhand";

        function inner() {
            let city = "Jamshedpur";

            console.log(country);
            console.log(state);
            console.log(city);
        }

        inner();
    }

    outer();

`inner()` can access:

- `city` from its own scope
- `state` from the outer scope
- `country` from the global scope

---

# 25. Global Scope Pollution

Creating too many global variables can make programs difficult to maintain.

Example:

    let name = "Saloni";
    let age = 17;
    let course = "MAD 1";
    let score = 90;

Large programs should avoid unnecessary global variables.

---

# 26. Best Practices

- Prefer `const` when a variable will not be reassigned.
- Use `let` when reassignment is required.
- Avoid `var` in modern JavaScript unless there is a specific reason.
- Keep variables in the smallest necessary scope.
- Avoid unnecessary global variables.
- Declare variables before using them.
- Do not rely on hoisting behavior.
- Use meaningful variable names.
- Understand the Temporal Dead Zone.
- Use function declarations or expressions intentionally.

---

# 27. Common Mistakes

### Mistake 1 — Accessing a block variable outside its block

    if (true) {
        let score = 90;
    }

    console.log(score);

This causes a `ReferenceError`.

### Mistake 2 — Assuming let behaves like var

    console.log(score);
    let score = 90;

This does not print `undefined`.

It produces a `ReferenceError`.

### Mistake 3 — Calling an arrow function before initialization

    show();

    const show = () => {
        console.log("Hello");
    };

This produces a `ReferenceError`.

---

# 28. Key Idea

Remember:

    Scope = Where can I access this variable?

    Hoisting = How does JavaScript process declarations before execution?

    var = Function scoped

    let = Block scoped

    const = Block scoped

    Function declaration = Hoisted and callable before declaration

    let/const before initialization = Temporal Dead Zone