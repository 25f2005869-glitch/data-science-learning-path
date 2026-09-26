# ⚡ Day 098 — JavaScript Complete Revision Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 098  
**Topic:** JavaScript Complete Revision

---

## 🧠 Core Model

    HTML → Structure
    CSS → Presentation
    JavaScript → Behavior

---

## 📦 Variables

    const name = "Saloni";
    let score = 85;
    var oldStyle = "Avoid when possible";

Prefer:

    const
    ↓
    let
    ↓
    avoid unnecessary var

---

## 🔤 Data Types

Primitive:

    string
    number
    bigint
    boolean
    undefined
    null
    symbol

Other values are objects, including:

    object
    array
    function

Check:

    typeof value

---

## ➕ Operators

Arithmetic:

    +  -  *  /  %  **

Comparison:

    >  <  >=  <=
    ===  !==
    ==   !=

Logical:

    &&  ||  !

Assignment:

    =  +=  -=  *=  /=

Ternary:

    condition ? yes : no

---

## 🔀 Conditions

    if
    else if
    else
    switch
    ternary

---

## 🔁 Loops

    for
    while
    do...while

Control:

    break
    continue

---

## 🛠️ Functions

    function add(a, b) {
        return a + b;
    }

Arrow:

    const add = (a, b) => a + b;

Default:

    function greet(name = "Student") {
        ...
    }

---

## 🔤 Strings

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

## 📝 Template Literal

    const message = `Hello ${name}`;

---

## 📚 Arrays

    const courses = ["DBMS", "PDSA", "MLF"];

Access:

    courses[0]

Length:

    courses.length

---

## 🔧 Array Methods

Traversal:

    forEach()

New array:

    map()
    filter()

Search:

    find()
    findIndex()

Checks:

    some()
    every()

Reduce:

    reduce()

Other:

    includes()
    indexOf()
    slice()
    splice()
    sort()
    reverse()

---

## 👤 Objects

    const student = {
        name: "Saloni",
        marks: 85
    };

Access:

    student.name
    student["name"]

Utilities:

    Object.keys()
    Object.values()
    Object.entries()

---

## 🔓 Destructuring

Array:

    const [first, second] = courses;

Object:

    const { name, marks } = student;

---

## 📦 Spread / Rest

Spread:

    const copy = [...courses];

Rest:

    function total(...numbers) {
        ...
    }

---

## ✨ Modern JavaScript

    let
    const
    =>
    template literals
    destructuring
    spread
    rest
    default parameters
    optional chaining
    nullish coalescing
    classes
    modules

---

## 🧠 Scope

    Global
    Function
    Block
    Lexical

Remember:

    let → block
    const → block
    var → function

---

## 📈 Hoisting

    var → hoisted + undefined

    let/const → hoisted but TDZ

    function declaration → callable before declaration

---

## ⚠️ Errors

    SyntaxError
    ReferenceError
    TypeError
    RangeError
    URIError

Handling:

    try
    catch
    finally
    throw

---

## 🌳 DOM

Select:

    getElementById()
    querySelector()
    querySelectorAll()

Content:

    textContent
    innerHTML

Classes:

    classList.add()
    classList.remove()
    classList.toggle()

Attributes:

    getAttribute()
    setAttribute()
    removeAttribute()

Create:

    createElement()
    append()
    prepend()

Remove:

    remove()

---

## 🖱️ Events

Common:

    click
    input
    change
    submit
    focus
    blur
    keydown
    keyup
    mouseover
    mouseout

Listener:

    addEventListener()

---

## 🎯 Event Object

    event.target
    event.currentTarget
    event.type

Control:

    event.preventDefault()
    event.stopPropagation()

---

## 📝 Validation

    checkValidity()
    reportValidity()
    validity
    validationMessage
    setCustomValidity()

---

## 💾 Web Storage

localStorage:

    setItem()
    getItem()
    removeItem()
    clear()

sessionStorage:

    setItem()
    getItem()
    removeItem()
    clear()

---

## 🔄 JSON

Object → JSON:

    JSON.stringify(object)

JSON → Object:

    JSON.parse(string)

---

## 🔐 Storage Warning

Do not treat:

    localStorage
    sessionStorage

as secure storage for passwords, tokens, or other sensitive secrets.

---

## ⭐ JavaScript Formula

**Variables → Logic → Functions → Data → DOM → Events → Validation → Storage**