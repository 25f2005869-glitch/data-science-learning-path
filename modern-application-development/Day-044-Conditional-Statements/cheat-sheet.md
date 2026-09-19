# ⚡ Day 044 — Conditional Statements Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 044  
**Topic:** Conditional Statements

---

## 🟨 `if`

    if (condition) {
        // code
    }

Runs when the condition is truthy.

---

## 🟨 `if...else`

    if (condition) {
        // true
    } else {
        // false
    }

---

## 🟨 `else if`

    if (condition1) {
        ...
    } else if (condition2) {
        ...
    } else {
        ...
    }

Conditions are checked from top to bottom.

---

## 🧱 Nested `if`

    if (condition1) {
        if (condition2) {
            ...
        }
    }

Avoid unnecessary deep nesting.

---

## 🔍 Comparison Operators

    >
    <
    >=
    <=
    ===
    !==

Prefer:

    ===
    !==

---

## 🔗 Logical Operators

### AND

    &&

Both conditions must be truthy.

### OR

    ||

At least one condition must be truthy.

### NOT

    !

Reverses truthiness.

---

## ✅ Truthy Examples

    true
    "hello"
    100
    []
    {}

---

## ❌ Falsy Values

    false
    0
    -0
    0n
    ""
    null
    undefined
    NaN

---

## 🔄 `switch`

    switch (value) {
        case 1:
            ...
            break;

        case 2:
            ...
            break;

        default:
            ...
    }

---

## 🛑 `break`

Stops the current `switch` case sequence.

Without `break`, fall-through can occur.

---

## ⭐ `default`

Runs when no `case` matches.

---

## 🎯 `switch` Matching

`switch` case matching uses strict comparison semantics.

Example:

    switch (5) {
        case "5":
            // no match
            break;

        case 5:
            // match
            break;
    }

---

## ⚡ Ternary

    condition ? trueValue : falseValue

Example:

    const result =
        marks >= 40 ? "Pass" : "Fail";

Use for simple decisions.

---

## 📊 Grade Example

    if (marks >= 90) {
        grade = "A";
    } else if (marks >= 75) {
        grade = "B";
    } else if (marks >= 50) {
        grade = "C";
    } else if (marks >= 40) {
        grade = "D";
    } else {
        grade = "Fail";
    }

---

## 🔐 Multiple Conditions

    if (age >= 18 && hasID) {
        console.log("Allowed");
    }

---

## ⚠️ Avoid

Assignment:

    if (age = 18)

Prefer:

    if (age === 18)

Incorrect range:

    40 <= marks <= 100

Correct:

    marks >= 40 && marks <= 100

---

## 🧠 When to Use What?

    if
    ↓
    General conditions

    else if
    ↓
    Multiple conditions / ranges

    switch
    ↓
    One value + known alternatives

    ternary
    ↓
    Simple two-way value selection