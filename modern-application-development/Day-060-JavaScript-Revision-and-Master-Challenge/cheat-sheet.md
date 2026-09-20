# ⚡ Day 060 — JavaScript Revision and Master Challenge Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 060  
**Topic:** JavaScript Revision and Master Challenge

---

# 🔹 Variables

    let score = 90;
    const course = "MAD 1";

---

# 🔹 Data Types

    string
    number
    boolean
    undefined
    null
    bigint
    symbol
    object

Check:

    typeof value

---

# 🔹 Conditions

    if (condition) {
        // code
    }

    if (condition) {
        // code
    } else {
        // code
    }

Ternary:

    condition ? value1 : value2

---

# 🔹 Loops

    for
    while
    do...while

Control:

    break
    continue

---

# 🔹 Functions

    function add(a, b) {
        return a + b;
    }

Arrow:

    const add = (a, b) => a + b;

---

# 🔹 Strings

    value.length
    value.toUpperCase()
    value.toLowerCase()
    value.trim()
    value.includes()
    value.startsWith()
    value.endsWith()
    value.slice()
    value.replace()
    value.split()

Template literal:

    `Hello ${name}`

---

# 🔹 Arrays

    push()
    pop()
    shift()
    unshift()
    slice()
    splice()

Useful methods:

    forEach()
    map()
    filter()
    find()
    findIndex()
    some()
    every()
    reduce()

---

# 🔹 Objects

    const student = {
        name: "Saloni",
        marks: 90
    };

Access:

    student.name
    student["name"]

Methods:

    Object.keys()
    Object.values()
    Object.entries()

---

# 🔹 ES6

    let
    const
    =>
    `${}`
    destructuring
    spread
    rest
    for...of
    optional chaining
    ??

---

# 🔹 DOM

    document.querySelector()
    document.querySelectorAll()

    textContent
    innerHTML
    classList
    style

Create:

    document.createElement()

---

# 🔹 Events

    click
    input
    change
    submit
    keydown
    keyup
    focus
    blur

Listener:

    element.addEventListener(
        "click",
        callback
    );

---

# 🔹 Forms

    required
    minlength
    maxlength
    min
    max
    pattern

JavaScript:

    checkValidity()
    reportValidity()
    setCustomValidity()

Stop submission:

    event.preventDefault()

---

# 🔹 localStorage

    localStorage.setItem(
        "key",
        "value"
    );

    localStorage.getItem("key");

    localStorage.removeItem("key");

    localStorage.clear();

---

# 🔹 sessionStorage

    sessionStorage.setItem(
        "key",
        "value"
    );

    sessionStorage.getItem("key");

---

# 🔹 JSON

Object → String:

    JSON.stringify(object)

String → Object:

    JSON.parse(string)

---

# 🔹 Error Handling

    try {
        // risky code
    } catch (error) {
        console.error(error);
    }

---

# 🔹 Grade Calculator

    90+  → A+
    80+  → A
    70+  → B
    60+  → C
    50+  → D
    <50  → F

---

# 🏆 Master Challenge Flow

    Input
      ↓
    Event
      ↓
    Validation
      ↓
    Function
      ↓
    Array/Object
      ↓
    DOM
      ↓
    Storage

---

# 🧠 Most Important Methods

    querySelector()
    addEventListener()
    textContent
    classList
    createElement()
    push()
    map()
    filter()
    find()
    reduce()
    checkValidity()
    preventDefault()
    JSON.stringify()
    JSON.parse()
    localStorage.setItem()
    localStorage.getItem()