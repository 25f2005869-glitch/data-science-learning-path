# ⚡ Day 042 — Variables and Data Types Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 042  
**Topic:** Variables and Data Types

---

## 📦 Variables

    let name = "Saloni";
    const age = 17;

---

## 🟨 `let`

Use when the value can change.

    let score = 80;
    score = 90;

---

## 🟩 `const`

Use when the variable binding should not be reassigned.

    const pi = 3.14159;

Cannot:

    pi = 4;

---

## 🟥 `var`

Older variable declaration.

    var name = "Saloni";

Prefer `let` and `const` in modern JavaScript.

---

## 📌 Quick Rule

    const → default choice
    let   → when reassignment is needed
    var   → generally avoid

---

## 📝 Declaration

    let name;

---

## 🎬 Initialization

    let name = "Saloni";

---

## 🔄 Assignment

    let score = 80;
    score = 95;

---

## 🔤 Valid Identifiers

    studentName
    totalMarks
    score2
    _count
    $price

Invalid:

    2score
    student name
    let

---

## 🧬 Primitive Data Types

    String
    Number
    BigInt
    Boolean
    Undefined
    Null
    Symbol

---

## 🔤 String

    "Hello"
    'Hello'
    `Hello`

---

## 🔢 Number

    10
    25.5
    -5

Special values:

    Infinity
    -Infinity
    NaN

---

## ✅ Boolean

    true
    false

---

## ❓ Undefined

    let result;

    console.log(result);

Result:

    undefined

---

## ⭕ Null

    let user = null;

Means intentional absence of a value.

---

## 🔢 BigInt

    12345678901234567890n

Use `n` at the end of a BigInt literal.

---

## 🔑 Symbol

    const id = Symbol("id");

Creates a unique primitive value.

---

## 📦 Object

    const student = {
        name: "Saloni",
        age: 17
    };

---

## 📚 Array

    const skills = [
        "Python",
        "SQL",
        "HTML"
    ];

---

## ⚙️ Function

    function greet() {
        console.log("Hello");
    }

---

## 🔍 `typeof`

    typeof "Hello"
    → "string"

    typeof 100
    → "number"

    typeof true
    → "boolean"

    typeof undefined
    → "undefined"

Important:

    typeof null
    → "object"

This is a historical JavaScript behavior.

---

## 🔄 Type Conversion

    Number("100")
    String(100)
    Boolean(1)

---

## 🔀 Dynamic Typing

    let value = 100;

    value = "Hello";

    value = true;

JavaScript allows this.

---

## 📌 Scope

    let    → block scope
    const  → block scope
    var    → function scope

---

## ⭐ Mental Model

    Variable
       ↓
    Value
       ↓
    Data Type

Example:

    let age = 17;

    age → 17 → number

---

## 🚀 Best Practice

    const → use by default
    let   → use when value changes
    var   → generally avoid