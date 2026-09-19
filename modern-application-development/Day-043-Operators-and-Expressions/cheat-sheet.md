# ⚡ Day 043 — Operators and Expressions Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 043  
**Topic:** Operators and Expressions

---

## 🔹 Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Remainder | `10 % 3` |
| `**` | Power | `2 ** 3` |

---

## 🔹 Assignment

    =

Example:

    let score = 90;

---

## 🔹 Compound Assignment

    +=
    -=
    *=
    /=
    %=
    **=

Example:

    score += 10;

Same as:

    score = score + 10;

---

## 🔹 Comparison

    >
    <
    >=
    <=
    ==
    ===
    !=
    !==

Results are normally:

    true
    false

---

## ⭐ Equality

Loose equality:

    5 == "5"
    → true

Strict equality:

    5 === "5"
    → false

Prefer:

    ===
    !==

---

## 🔹 Logical Operators

### AND

    &&

Both conditions must be true.

### OR

    ||

At least one condition must be true.

### NOT

    !

Reverses Boolean value.

---

## 🔼 Increment

    x++

or:

    ++x

Increases by 1.

---

## 🔽 Decrement

    x--

or:

    --x

Decreases by 1.

---

## 🔤 String Concatenation

    "Hello " + name

---

## 🟨 Template Literal

    `Hello ${name}`

Uses backticks.

---

## 🔍 typeof

    typeof value

Examples:

    typeof 10
    → "number"

    typeof "Hello"
    → "string"

---

## ❓ Ternary Operator

Syntax:

    condition ? valueIfTrue : valueIfFalse

Example:

    age >= 18 ? "Adult" : "Minor"

---

## 🧮 Precedence

Simplified order:

    ()
    **
    *, /, %
    +, -
    comparisons
    &&
    ||
    ?:
    assignments

Use parentheses for clarity.

---

## ⚡ Short-Circuit

AND:

    false && anything

OR:

    true || anything

---

## ✅ Common Falsy Values

    false
    0
    -0
    0n
    ""
    null
    undefined
    NaN

---

## 🧠 Mental Model

    Operator
       +
    Operand
       ↓
    Expression
       ↓
    Result

Example:

    10 + 20
       ↓
      30