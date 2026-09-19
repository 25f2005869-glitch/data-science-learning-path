# ⚡ Day 048 — Arrays — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 048  
**Topic:** Arrays

---

## 📦 Create Array

    const subjects = ["DBMS", "PDSA", "MLF"];

---

## 🔢 Index

    subjects[0];    // DBMS
    subjects[1];    // PDSA

Indexes start from `0`.

---

## 📏 length

    subjects.length;

Returns the number of elements.

Last element:

    subjects[subjects.length - 1];

---

## ✏️ Update

    subjects[1] = "MAD1";

---

## ➕

### push()

Add to end:

    subjects.push("BDM");

### unshift()

Add to beginning:

    subjects.unshift("Statistics");

---

## ➖

### pop()

Remove from end:

    subjects.pop();

### shift()

Remove from beginning:

    subjects.shift();

---

## 🔍 includes()

    subjects.includes("PDSA");

Returns `true` or `false`.

---

## 🔎 indexOf()

    subjects.indexOf("PDSA");

Returns the index.

Returns `-1` if not found.

---

## 🔗 join()

    subjects.join(", ");

Converts array elements into a string.

---

## ✂️ slice()

    const result = numbers.slice(1, 4);

Extracts elements without modifying the original array.

---

## 🛠️ splice()

Remove:

    numbers.splice(1, 2);

Add:

    numbers.splice(1, 0, 100);

Replace:

    numbers.splice(1, 1, 100);

`splice()` modifies the original array.

---

## 🔁 Array Traversal

    for (let i = 0; i < subjects.length; i++) {
        console.log(subjects[i]);
    }

---

## ➕ Array Total

    let total = 0;

    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }

---

## 🔲 Nested Array

    const matrix = [
        [1, 2],
        [3, 4]
    ];

Access:

    matrix[0][1];

---

## 🧠 slice vs splice

| Method | Modifies Original? | Purpose |
|---|---|---|
| `slice()` | No | Extract/copy |
| `splice()` | Yes | Add/remove/replace |

---

## 📌 Remember

- Index starts at `0`.
- Last index = `length - 1`.
- `push()` → add end.
- `pop()` → remove end.
- `unshift()` → add beginning.
- `shift()` → remove beginning.
- `includes()` → check existence.
- `indexOf()` → find index.
- `join()` → array to string.
- `slice()` → non-mutating extraction.
- `splice()` → modifies array.
- Use `i < array.length` for normal traversal.