# ⚡ Day 045 — Loops — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 045  
**Topic:** Loops

---

## 🔄 Basic Loop Types

| Loop | Best Use |
|---|---|
| `for` | Known/repeatable iteration structure |
| `while` | Condition-controlled repetition |
| `do...while` | Must execute at least once |

---

## 🔁 for Loop

    for (let i = 0; i < 5; i++) {
        console.log(i);
    }

Structure:

    for (initialization; condition; update)

---

## 🔁 while Loop

    let i = 0;

    while (i < 5) {
        console.log(i);
        i++;
    }

---

## 🔁 do...while

    let i = 0;

    do {
        console.log(i);
        i++;
    } while (i < 5);

The body executes at least once.

---

## ⛔ break

Stops the complete loop.

    for (let i = 1; i <= 10; i++) {
        if (i === 5) {
            break;
        }
    }

---

## ⏭️ continue

Skips the current iteration.

    for (let i = 1; i <= 5; i++) {
        if (i === 3) {
            continue;
        }

        console.log(i);
    }

---

## 📦 Array Loop

    const subjects = ["DBMS", "PDSA", "MLF"];

    for (let i = 0; i < subjects.length; i++) {
        console.log(subjects[i]);
    }

---

## 🔤 String Loop

    const text = "Hello";

    for (let i = 0; i < text.length; i++) {
        console.log(text[i]);
    }

---

## 🔢 Reverse Loop

    for (let i = 5; i >= 1; i--) {
        console.log(i);
    }

---

## ➕ Custom Increment

    for (let i = 0; i <= 10; i += 2) {
        console.log(i);
    }

---

## 🔂 Nested Loop

    for (let i = 1; i <= 3; i++) {
        for (let j = 1; j <= 3; j++) {
            console.log(i, j);
        }
    }

---

## ⚠️ Infinite Loop

Avoid:

    let i = 1;

    while (i <= 5) {
        console.log(i);
    }

Correct:

    let i = 1;

    while (i <= 5) {
        console.log(i);
        i++;
    }

---

## 🧠 Key Difference

| Keyword | Action |
|---|---|
| `break` | Exit loop |
| `continue` | Skip current iteration |

---

## 📌 Remember

- `for` → initialization + condition + update
- `while` → condition first
- `do...while` → body first
- `break` → stop
- `continue` → skip
- `array.length` → number of elements
- Loop counter usually starts at `0` for arrays
- Ensure every loop can terminate