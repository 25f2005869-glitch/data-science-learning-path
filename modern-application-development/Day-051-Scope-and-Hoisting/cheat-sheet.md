# ⚡ Day 051 — Scope and Hoisting — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 051  
**Topic:** Scope and Hoisting

---

# 🔹 Scope

Scope = the area where a variable can be accessed.

## Types

| Scope | Meaning |
|---|---|
| Global | Available from global scope |
| Function | Available inside a function |
| Block | Available inside `{ }` |
| Lexical | Scope determined by where code is written |

---

# 🔹 var vs let vs const

| Feature | `var` | `let` | `const` |
|---|---|---|---|
| Function scoped | ✅ | ❌ | ❌ |
| Block scoped | ❌ | ✅ | ✅ |
| Can reassign | ✅ | ✅ | ❌ |
| TDZ | ❌ | ✅ | ✅ |
| Recommended today | Usually no | ✅ | ✅ |

---

# 🔹 Scope Chain

Variable lookup:

    Current Scope
         ↓
    Outer Scope
         ↓
    Global Scope

JavaScript searches outward until it finds the variable.

---

# 🔹 Shadowing

An inner variable can have the same name as an outer variable.

    let name = "Global";

    {
        let name = "Local";
        console.log(name);
    }

Output:

    Local

---

# 🔹 Hoisting

Hoisting describes how JavaScript processes declarations before execution.

It does not mean that all code is physically moved to the top.

---

# 🔹 var Hoisting

    console.log(x);
    var x = 10;

Output:

    undefined

Conceptually:

    var x;
    console.log(x);
    x = 10;

---

# 🔹 let / const

    console.log(x);
    let x = 10;

Result:

    ReferenceError

The same applies to `const`.

---

# 🔹 Temporal Dead Zone

TDZ = period between entering a scope and initialization of a `let` or `const` variable.

    console.log(score);
    let score = 90;

Result:

    ReferenceError

---

# 🔹 Function Declaration

Function declarations are hoisted.

    greet();

    function greet() {
        console.log("Hello");
    }

This works.

---

# 🔹 Function Expression

    greet();

    const greet = function () {
        console.log("Hello");
    };

This causes a `ReferenceError`.

---

# 🔹 Arrow Function

    greet();

    const greet = () => {
        console.log("Hello");
    };

This also causes a `ReferenceError`.

---

# 🔹 Quick Comparison

| Declaration | Hoisted | Usable Before Declaration |
|---|---|---|
| `var` | Yes | Yes, gives `undefined` |
| `let` | Yes | No |
| `const` | Yes | No |
| Function declaration | Yes | Yes |
| Function expression with `const` | Variable is hoisted but uninitialized | No |
| Arrow function with `const` | Variable is hoisted but uninitialized | No |

---

# 🔹 Golden Rules

1. Prefer `const`.
2. Use `let` when reassignment is required.
3. Avoid unnecessary `var`.
4. Keep variables in the smallest required scope.
5. Avoid unnecessary globals.
6. Declare variables before using them.
7. Do not depend on hoisting.
8. Remember the TDZ for `let` and `const`.

---

# 🧠 Remember

    Scope → Where can I use it?

    Hoisting → How are declarations processed?

    var → Function Scope

    let → Block Scope + TDZ

    const → Block Scope + TDZ

    Function Declaration → Hoisted

    Function Expression → Not callable before initialization