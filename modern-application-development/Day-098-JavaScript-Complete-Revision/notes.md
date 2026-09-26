# ⚡ Day 098 — JavaScript Complete Revision Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 098  
**Topic:** JavaScript Complete Revision

---

# 1. What is JavaScript?

JavaScript is a programming language commonly used to add behavior and interactivity to webpages.

Basic mental model:

    HTML → Structure
    CSS → Presentation
    JavaScript → Behavior

JavaScript can run in browsers and can also be used in other environments.

---

# 2. Adding JavaScript

## Inline JavaScript

    <button onclick="showMessage()">Click</button>

## Internal JavaScript

    <script>
        console.log("Hello");
    </script>

## External JavaScript

    <script src="script.js"></script>

For scripts that should execute after HTML parsing, `defer` is commonly useful:

    <script src="script.js" defer></script>

---

# 3. JavaScript Syntax

JavaScript is case-sensitive.

Example:

    const studentName = "Saloni";

Statements commonly end with semicolons, although JavaScript also has automatic semicolon insertion.

Comments:

    // Single-line comment

    /*
       Multi-line comment
    */

---

# 4. Variables

Variables store references to values.

Main declarations:

    let
    const
    var

Prefer `const` by default and use `let` when reassignment is required.

Example:

    const name = "Saloni";
    let score = 85;

---

# 5. Variable Naming

Rules include:

- Names can contain letters, digits, `_`, and `$`.
- Names cannot start with a digit.
- Reserved words cannot be used as identifiers.
- JavaScript is case-sensitive.

Preferred style:

    studentName
    totalMarks
    courseName

Use descriptive names.

---

# 6. Data Types

Primitive types include:

- String
- Number
- BigInt
- Boolean
- Undefined
- Null
- Symbol

JavaScript also has objects, including:

- Objects
- Arrays
- Functions

Check a value's type with:

    typeof value

Remember that:

    typeof null

returns `"object"` due to a historical JavaScript behavior.

---

# 7. Dynamic Typing

JavaScript is dynamically typed.

A variable can be assigned different types of values during execution.

Example:

    let value = 10;
    value = "Hello";

Prefer predictable code and avoid unnecessary type changes.

---

# 8. Operators

Major operator categories:

- Arithmetic
- Assignment
- Comparison
- Logical
- Unary
- Ternary

---

# 9. Arithmetic Operators

Common operators:

    +
    -
    *
    /
    %
    **
    ++
    --

Example:

    const total = 10 + 20;

---

# 10. Assignment Operators

Examples:

    =
    +=
    -=
    *=
    /=
    %=

Example:

    let score = 50;
    score += 10;

The final value becomes `60`.

---

# 11. Comparison Operators

Examples:

    >
    <
    >=
    <=
    ==
    ===
    !=
    !==

Prefer strict comparison:

    ===
    !==

Strict equality checks value and type without performing the coercion associated with loose equality.

---

# 12. Logical Operators

Main operators:

    &&
    ||
    !

Example:

    age >= 18 && hasID

Logical operators can also return operands and participate in short-circuit evaluation.

---

# 13. Truthy and Falsy

Values that behave as false in boolean contexts include:

    false
    0
    -0
    0n
    ""
    null
    undefined
    NaN

Most other values are truthy.

---

# 14. Ternary Operator

Syntax:

    condition ? valueIfTrue : valueIfFalse

Example:

    const status = marks >= 40 ? "Pass" : "Fail";

Use ternary expressions for concise conditional values.

---

# 15. Operator Precedence

When multiple operators are used, precedence determines evaluation order.

Parentheses can make the intended order explicit.

Example:

    (10 + 5) * 2

Prefer readable expressions instead of relying on complicated precedence rules.

---

# 16. Conditional Statements

## if

    if (condition) {
        ...
    }

## if...else

    if (condition) {
        ...
    } else {
        ...
    }

## else if

Used for multiple conditions.

---

# 17. switch

Basic structure:

    switch (value) {
        case "student":
            ...
            break;

        case "admin":
            ...
            break;

        default:
            ...
    }

`switch` uses strict matching for case comparison.

---

# 18. Loops

Loops repeat code.

Main loops:

    for
    while
    do...while

---

# 19. for Loop

Structure:

    for (initialization; condition; update) {
        ...
    }

Example:

    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }

---

# 20. while Loop

A `while` loop continues while its condition is true.

Example:

    let i = 1;

    while (i <= 5) {
        console.log(i);
        i++;
    }

---

# 21. do...while

A `do...while` loop executes its body at least once before checking the condition.

Example:

    let i = 1;

    do {
        console.log(i);
        i++;
    } while (i <= 5);

---

# 22. break and continue

`break` exits the loop.

    break;

`continue` skips the current iteration and continues with the next iteration.

    continue;

Avoid accidentally creating infinite loops.

---

# 23. Functions

Functions are reusable blocks of code.

Declaration:

    function add(a, b) {
        return a + b;
    }

Call:

    const result = add(10, 20);

---

# 24. Parameters and Arguments

Parameters are variables defined in the function.

    function greet(name) {
        ...
    }

Arguments are values passed during the function call.

    greet("Saloni");

---

# 25. return

`return` sends a value back to the caller.

Example:

    function square(number) {
        return number * number;
    }

Code after an executed `return` in that function does not run.

---

# 26. Default Parameters

Example:

    function greet(name = "Student") {
        return `Hello ${name}`;
    }

Default parameters are used when the corresponding argument is `undefined`.

---

# 27. Function Expressions

Example:

    const add = function (a, b) {
        return a + b;
    };

The function is stored in a variable.

---

# 28. Arrow Functions

Example:

    const add = (a, b) => {
        return a + b;
    };

Concise form:

    const square = number => number * number;

Arrow functions have lexical `this` behavior and do not have their own `this`.

---

# 29. Scope

Scope determines where a variable can be accessed.

Important types:

- Global scope
- Function scope
- Block scope
- Lexical scope

`let` and `const` are block-scoped.

`var` is function-scoped.

---

# 30. Hoisting

Hoisting describes how declarations are processed before execution of their surrounding code.

### var

A `var` declaration is hoisted and initialized with `undefined`.

### let and const

Their declarations are hoisted but remain in the Temporal Dead Zone until execution reaches their declaration.

### Function declarations

Function declarations can generally be called before their declaration in the same scope.

---

# 31. Strings

Strings can use:

    "Hello"
    'Hello'
    `Hello`

Useful properties and methods:

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

---

# 32. String Immutability

Strings are immutable.

Methods return new strings rather than modifying the original string.

Example:

    const name = "saloni";
    const upper = name.toUpperCase();

---

# 33. Template Literals

Template literals use backticks.

Example:

    const name = "Saloni";
    const message = `Hello, ${name}!`;

Expressions can be placed inside:

    ${expression}

Template literals also support multiline strings.

---

# 34. Arrays

Arrays store ordered collections.

Example:

    const courses = ["DBMS", "PDSA", "MLF"];

Indexing starts at:

    0

Access:

    courses[0]

Length:

    courses.length

---

# 35. Array Mutation Methods

Common methods:

    push()
    pop()
    unshift()
    shift()
    splice()
    reverse()
    sort()

These methods can modify the original array.

---

# 36. Array Non-Mutating Methods

Common methods:

    slice()
    includes()
    indexOf()
    join()

Some higher-order methods return new arrays or values without modifying the original array.

---

# 37. Array Methods

Important methods:

    forEach()
    map()
    filter()
    find()
    findIndex()
    some()
    every()
    reduce()
    sort()

Understand whether a method:

- Returns a value
- Returns a new array
- Mutates the original array

---

# 38. map()

`map()` creates a new array by transforming each element.

Example:

    const marks = [70, 80, 90];

    const updated = marks.map(mark => mark + 5);

---

# 39. filter()

`filter()` creates a new array containing elements that satisfy a condition.

Example:

    const passed = marks.filter(mark => mark >= 40);

---

# 40. find()

`find()` returns the first element satisfying the condition.

Example:

    const result = students.find(student => student.id === 2);

---

# 41. some() and every()

`some()` checks whether at least one element satisfies a condition.

`every()` checks whether all elements satisfy a condition.

---

# 42. reduce()

`reduce()` combines array elements into a single accumulated result.

Example:

    const total = marks.reduce(
        (sum, mark) => sum + mark,
        0
    );

---

# 43. Objects

Objects store related data using key-value pairs.

Example:

    const student = {
        name: "Saloni",
        course: "MAD 1",
        marks: 85
    };

---

# 44. Accessing Object Properties

Dot notation:

    student.name

Bracket notation:

    student["name"]

Bracket notation is useful when the property name is stored dynamically.

---

# 45. Object Modification

Add:

    student.age = 17;

Update:

    student.marks = 90;

Delete:

    delete student.age;

Objects declared with `const` can still have their properties changed.

---

# 46. Object Methods and this

Objects can contain functions.

Example:

    const student = {
        name: "Saloni",

        greet() {
            return `Hello ${this.name}`;
        }
    };

`this` in a regular object method commonly refers to the object through which the method is called.

Arrow functions do not create their own `this`.

---

# 47. Object Utility Methods

Useful methods:

    Object.keys()
    Object.values()
    Object.entries()

Example:

    Object.keys(student)

---

# 48. for...in and for...of

`for...in` iterates over enumerable property keys.

`for...of` iterates over values from an iterable.

Example:

    for (const key in student) {
        console.log(key);
    }

    for (const course of courses) {
        console.log(course);
    }

---

# 49. Destructuring

Array destructuring:

    const [first, second] = courses;

Object destructuring:

    const { name, marks } = student;

Destructuring extracts values into variables.

---

# 50. Spread Operator

Spread syntax:

    ...

Example:

    const updatedCourses = [...courses, "MAD 1"];

It can create a new array containing existing elements plus additional values.

---

# 51. Rest Parameter

Rest syntax collects remaining arguments.

Example:

    function total(...numbers) {
        return numbers.reduce((sum, n) => sum + n, 0);
    }

---

# 52. ES6 Features

Important modern JavaScript features include:

- let
- const
- Arrow functions
- Template literals
- Default parameters
- Destructuring
- Spread
- Rest
- Classes
- Modules
- Enhanced object literals

Modern JavaScript also includes features such as optional chaining and nullish coalescing.

---

# 53. Optional Chaining

Optional chaining:

    ?.

Example:

    student.profile?.city

It safely attempts property access when an earlier value may be `null` or `undefined`.

---

# 54. Nullish Coalescing

Operator:

    ??

Example:

    const name = user.name ?? "Guest";

It uses the fallback when the left side is `null` or `undefined`.

It is different from `||`, which also treats other falsy values as triggers for the fallback.

---

# 55. Error Types

Common JavaScript errors:

- SyntaxError
- ReferenceError
- TypeError
- RangeError
- URIError

Errors can be syntax-related, runtime-related, or logical.

---

# 56. try...catch

Example:

    try {
        riskyOperation();
    } catch (error) {
        console.error(error);
    }

Use `try...catch` when an operation may throw an error that the application can meaningfully handle.

---

# 57. finally

`finally` executes after the `try`/`catch` process.

Example:

    try {
        ...
    } catch (error) {
        ...
    } finally {
        ...
    }

---

# 58. throw

Custom errors can be created with `throw`.

Example:

    if (marks < 0) {
        throw new Error("Marks cannot be negative.");
    }

---

# 59. DOM

DOM stands for **Document Object Model**.

The browser represents the HTML document as a tree of objects.

JavaScript can use the DOM to:

- Select elements
- Change content
- Change styles
- Change classes
- Change attributes
- Create elements
- Remove elements
- Respond to events

---

# 60. Selecting Elements

Important methods:

    getElementById()

    querySelector()

    querySelectorAll()

Other legacy collection methods include:

    getElementsByClassName()

    getElementsByTagName()

---

# 61. Changing Content

`textContent` changes text content.

Example:

    element.textContent = "Hello";

`innerHTML` reads or sets HTML markup.

Use `innerHTML` carefully when content comes from untrusted sources.

---

# 62. Classes and Styles

Class methods:

    classList.add()
    classList.remove()
    classList.toggle()
    classList.contains()

Inline style:

    element.style.color = "blue";

Prefer CSS classes for reusable styling.

---

# 63. Attributes

Read:

    element.getAttribute("href");

Set:

    element.setAttribute("title", "Profile");

Remove:

    element.removeAttribute("title");

---

# 64. Creating Elements

Example:

    const item = document.createElement("li");

    item.textContent = "JavaScript";

    list.append(item);

Elements can also be inserted using:

    append()
    prepend()
    before()
    after()

---

# 65. Removing and Replacing

Remove:

    element.remove();

Replace:

    oldElement.replaceWith(newElement);

---

# 66. DOM Traversal

Useful properties:

    parentElement
    children
    firstElementChild
    lastElementChild
    nextElementSibling
    previousElementSibling

Traversal allows JavaScript to move through related DOM elements.

---

# 67. Events

Events represent actions or occurrences such as:

- Click
- Keyboard input
- Mouse movement
- Form submission
- Focus
- Change

---

# 68. Event Listeners

Preferred approach:

    element.addEventListener("click", function (event) {
        ...
    });

The callback runs when the event occurs.

---

# 69. Event Object

The event object provides information about the event.

Common properties:

    event.target
    event.currentTarget
    event.type

---

# 70. preventDefault()

`preventDefault()` stops the browser's default action for a cancelable event.

Example:

    form.addEventListener("submit", function (event) {
        event.preventDefault();
    });

---

# 71. Event Propagation

Events can propagate through the DOM.

Important concepts:

    Capturing
    Target
    Bubbling

Event delegation can use bubbling to handle events from multiple child elements efficiently.

---

# 72. Event Delegation

Instead of attaching listeners to many similar child elements, a listener can sometimes be attached to a parent.

The event target can then be inspected.

This is useful for dynamically created lists and tables.

---

# 73. Form Validation

JavaScript can perform custom validation.

Useful browser APIs:

    checkValidity()
    reportValidity()
    validity
    validationMessage
    setCustomValidity()

Example:

    if (!form.checkValidity()) {
        form.reportValidity();
    }

---

# 74. Client-Side vs Server-Side Validation

Client-side validation:

- Fast feedback
- Better user experience
- Runs in the browser

Server-side validation:

- Runs on the server
- Must not be skipped
- Protects application logic and data integrity

Client-side validation does not replace server-side validation.

---

# 75. localStorage

`localStorage` stores string data associated with the browser origin and persists across browser sessions unless cleared.

Methods:

    setItem()
    getItem()
    removeItem()
    clear()
    key()

Example:

    localStorage.setItem("name", "Saloni");

Read:

    localStorage.getItem("name");

---

# 76. sessionStorage

`sessionStorage` also stores strings, but its lifetime is associated with the current page session.

Example:

    sessionStorage.setItem("course", "MAD 1");

---

# 77. JSON with Storage

Storage APIs store strings.

Objects can be converted using:

    JSON.stringify(object)

Read back:

    JSON.parse(string)

Example:

    localStorage.setItem(
        "student",
        JSON.stringify(student)
    );

---

# 78. localStorage vs sessionStorage

| Feature | localStorage | sessionStorage |
|---|---|---|
| Data type | Strings | Strings |
| Persistence | Across browser sessions | Current page session |
| API | Web Storage | Web Storage |
| Common use | Preferences | Temporary session data |

Neither should be treated as a secure place for sensitive secrets.

---

# 79. JSON

JSON stands for **JavaScript Object Notation**.

JavaScript methods:

    JSON.stringify()
    JSON.parse()

`JSON.stringify()` converts a JavaScript value to a JSON string.

`JSON.parse()` converts valid JSON text back into a JavaScript value.

---

# 80. JavaScript Best Practices

- Prefer `const` unless reassignment is needed.
- Use meaningful names.
- Prefer strict equality.
- Keep functions focused.
- Avoid unnecessary global variables.
- Avoid excessive DOM manipulation.
- Validate user input.
- Handle expected errors.
- Keep sensitive data out of browser storage.
- Use event listeners instead of inline handlers.
- Separate HTML, CSS, and JavaScript.
- Keep code readable.
- Avoid unnecessary complexity.

---

# 81. Final JavaScript Revision Checklist

- [ ] JavaScript fundamentals
- [ ] Variables
- [ ] Data types
- [ ] Operators
- [ ] Conditions
- [ ] Loops
- [ ] Functions
- [ ] Strings
- [ ] Template literals
- [ ] Arrays
- [ ] Array methods
- [ ] Objects
- [ ] Scope
- [ ] Hoisting
- [ ] ES6
- [ ] Error handling
- [ ] DOM
- [ ] DOM manipulation
- [ ] Events
- [ ] Event propagation
- [ ] Form validation
- [ ] JSON
- [ ] localStorage
- [ ] sessionStorage

---

# 82. Final Takeaway

JavaScript connects webpage structure with interactive behavior.

A strong JavaScript implementation should be:

**Readable + Reusable + Interactive + Validated + Maintainable**