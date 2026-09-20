# 📚 Day 060 — JavaScript Revision and Master Challenge

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 060  
**Topic:** JavaScript Revision and Master Challenge

---

# 🧠 Part 1 — JavaScript Fundamentals

## 1. Variables

JavaScript variables store values.

    let score = 90;

    const course = "MAD 1";

Use:

- `let` when reassignment is required.
- `const` when the variable binding should not be reassigned.
- Avoid `var` in modern code unless there is a specific reason.

---

## 2. Data Types

Primitive types include:

- String
- Number
- Boolean
- Undefined
- Null
- BigInt
- Symbol

JavaScript also works with objects, arrays, and functions.

Check a value's type:

    typeof value

---

## 3. Operators

Important operators:

### Arithmetic

    +
    -
    *
    /
    %
    **

### Comparison

    ===
    !==
    >
    <
    >=
    <=

### Logical

    &&
    ||
    !

### Assignment

    =
    +=
    -=
    *=
    /=

---

# 🔀 Part 2 — Conditions

## if

    if (marks >= 50) {
        console.log("Passed");
    }

## if...else

    if (marks >= 50) {
        console.log("Passed");
    } else {
        console.log("Failed");
    }

## else if

Useful for multiple conditions.

    if (marks >= 90) {
        grade = "A+";
    } else if (marks >= 80) {
        grade = "A";
    } else {
        grade = "F";
    }

## Ternary Operator

    const result =
        marks >= 50 ? "Passed" : "Failed";

---

# 🔁 Part 3 — Loops

Loops repeat code.

Common loops:

    for

    while

    do...while

Example:

    for (let i = 0; i < 5; i++) {
        console.log(i);
    }

Important control statements:

    break
    continue

---

# 🧩 Part 4 — Functions

Functions contain reusable logic.

    function add(a, b) {
        return a + b;
    }

Call:

    add(10, 20);

Arrow function:

    const add = (a, b) => a + b;

Important concepts:

- Parameters
- Arguments
- Return value
- Default parameters
- Function scope
- Function expressions
- Arrow functions

---

# 🔤 Part 5 — Strings

Strings represent text.

    const name = "Saloni";

Useful methods:

    length
    toUpperCase()
    toLowerCase()
    trim()
    includes()
    startsWith()
    endsWith()
    indexOf()
    slice()
    substring()
    replace()
    split()

Template literals:

    `Hello, ${name}`

---

# 📦 Part 6 — Arrays

Arrays store collections of values.

    const courses = [
        "MAD 1",
        "DBMS",
        "PDSA"
    ];

Important methods:

    push()
    pop()
    shift()
    unshift()
    slice()
    splice()
    includes()
    indexOf()

Iteration methods:

    forEach()
    map()
    filter()
    find()
    findIndex()
    some()
    every()
    reduce()

---

# 🧮 Part 7 — Array Methods

## map()

Creates a new array by transforming elements.

    const doubled =
        numbers.map(
            number => number * 2
        );

## filter()

Creates a new array containing elements that satisfy a condition.

    const passed =
        marks.filter(
            mark => mark >= 50
        );

## find()

Returns the first matching element.

## some()

Checks whether at least one element satisfies a condition.

## every()

Checks whether all elements satisfy a condition.

## reduce()

Combines array values into one result.

    const total =
        marks.reduce(
            (sum, mark) => sum + mark,
            0
        );

---

# 🧑‍🎓 Part 8 — Objects

Objects store related information as key-value pairs.

    const student = {
        name: "Saloni",
        course: "MAD 1",
        marks: 90
    };

Access:

    student.name

or:

    student["name"]

Useful methods:

    Object.keys()
    Object.values()
    Object.entries()

---

# 🔗 Part 9 — Scope

Important scope types:

- Global scope
- Function scope
- Block scope
- Lexical scope

`let` and `const` are block-scoped.

`var` is function-scoped.

JavaScript searches through the scope chain when resolving variables.

---

# ⬆️ Part 10 — Hoisting

Hoisting describes how JavaScript processes declarations during execution setup.

`var` declarations are hoisted and initialized with `undefined`.

`let` and `const` declarations are also processed before execution reaches their declaration, but they cannot be accessed before initialization because of the Temporal Dead Zone.

Function declarations can be called before their declaration in suitable contexts.

---

# 🆕 Part 11 — ES6 Features

Important modern JavaScript features include:

- `let`
- `const`
- Arrow functions
- Template literals
- Default parameters
- Destructuring
- Spread syntax
- Rest parameters
- Enhanced object literals
- `for...of`
- Optional chaining
- Nullish coalescing
- Classes
- Modules

Example:

    const student = {
        name: "Saloni",
        course: "MAD 1"
    };

    const { name, course } = student;

---

# ⚠️ Part 12 — Error Handling

JavaScript errors can be handled with:

    try
    catch
    finally

Example:

    try {
        const data = JSON.parse(value);
    } catch (error) {
        console.error(error);
    }

Custom errors:

    throw new Error("Invalid data");

---

# 🌳 Part 13 — DOM

The DOM represents an HTML document as a tree of objects.

Select an element:

    document.querySelector("#title");

Select multiple elements:

    document.querySelectorAll(".card");

Change text:

    element.textContent = "Hello";

Change classes:

    element.classList.add("active");

Create an element:

    const item =
        document.createElement("li");

---

# ⚡ Part 14 — Events

Events allow JavaScript to respond to user actions.

Examples:

    click
    input
    change
    submit
    keydown
    focus
    blur

Add a listener:

    button.addEventListener(
        "click",
        handleClick
    );

---

# 📝 Part 15 — Form Validation

HTML provides built-in validation:

    required
    minlength
    maxlength
    min
    max
    pattern

JavaScript can use:

    checkValidity()

    reportValidity()

    setCustomValidity()

Stop default submission:

    event.preventDefault();

---

# 💾 Part 16 — localStorage

Store:

    localStorage.setItem(
        "name",
        "Saloni"
    );

Read:

    localStorage.getItem("name");

Remove:

    localStorage.removeItem("name");

Clear:

    localStorage.clear();

---

# ⏳ Part 17 — sessionStorage

Store temporary session information:

    sessionStorage.setItem(
        "course",
        "MAD 1"
    );

Read:

    sessionStorage.getItem("course");

---

# 🔄 Part 18 — JSON

Web Storage stores strings.

Objects can be converted into JSON strings.

    JSON.stringify(student);

Convert JSON back to an object:

    JSON.parse(data);

---

# 🏆 Part 19 — Master Challenge Architecture

The Master Challenge follows this structure:

    User Input
        ↓
    Event Listener
        ↓
    Validation
        ↓
    JavaScript Function
        ↓
    Data Processing
        ↓
    Object / Array
        ↓
    DOM Update
        ↓
    localStorage / sessionStorage

---

# 🎓 Part 20 — Student Academic Management Dashboard

The project contains:

### Profile

- Name
- Email
- Course
- Marks

### Result

- Grade
- Pass/Fail

### Courses

- Add
- Remove
- Search/filter

### Progress

- Increase
- Decrease
- Reset

### Storage

- Save student
- Load student
- Delete student
- Save session course

### UI

- Light theme
- Dark theme
- Dynamic DOM updates

---

# 🧠 Final Revision Principle

JavaScript becomes powerful when individual concepts are combined.

    Variables
        +
    Functions
        +
    Arrays
        +
    Objects
        +
    DOM
        +
    Events
        +
    Validation
        +
    Storage
        =
    Interactive Web Application

This is the core skill developed during the JavaScript section of MAD 1.