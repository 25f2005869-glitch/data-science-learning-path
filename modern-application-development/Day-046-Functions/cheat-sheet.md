# ⚡ Day 046 — Functions — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 046  
**Topic:** Functions

---

## 🔧 Function Declaration

    function greet() {
        console.log("Hello");
    }

---

## ▶️ Function Call

    greet();

---

## 📥 Parameter

    function greet(name) {
        console.log(name);
    }

`name` is a parameter.

---

## 📤 Argument

    greet("Saloni");

`"Saloni"` is an argument.

---

## ➕ Multiple Parameters

    function add(a, b) {
        return a + b;
    }

    add(10, 20);

---

## ↩️ return

    function add(a, b) {
        return a + b;
    }

    const result = add(10, 20);

`return` sends a value back.

---

## ⚙️ Default Parameter

    function greet(name = "Student") {
        console.log(name);
    }

---

## 📦 Function Expression

    const add = function(a, b) {
        return a + b;
    };

---

## ➡️ Arrow Function

    const add = (a, b) => {
        return a + b;
    };

Short form:

    const add = (a, b) => a + b;

---

## 🔹 One Parameter

    const square = x => x * x;

---

## 🔁 Function with Loop

    function printNumbers(limit) {
        for (let i = 1; i <= limit; i++) {
            console.log(i);
        }
    }

---

## 🔀 Function with Condition

    function checkResult(marks) {
        if (marks >= 40) {
            return "Pass";
        }

        return "Fail";
    }

---

## 🌍 Scope

Local:

    function test() {
        let x = 10;
    }

Global:

    const x = 10;

    function test() {
        console.log(x);
    }

---

## 🧠 Parameter vs Argument

| Parameter | Argument |
|---|---|
| In function definition | In function call |
| Placeholder variable | Actual value |

---

## 📌 Remember

- Define → create the function.
- Call → execute the function.
- Parameter → receives input.
- Argument → provides input.
- `return` → sends output.
- Function expression → function stored in variable.
- Arrow function → concise function syntax.
- Keep functions reusable and focused.