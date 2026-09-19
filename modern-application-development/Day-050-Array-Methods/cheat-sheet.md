# ⚡ Day 050 — Array Methods — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 050  
**Topic:** Array Methods

---

## 🔁 forEach()

Perform an action for every element.

    numbers.forEach(number => {
        console.log(number);
    });

Returns:

    undefined

---

## 🔄 map()

Transform every element.

    const doubled = numbers.map(number => number * 2);

Returns:

    New array

---

## 🔍 filter()

Keep elements that satisfy a condition.

    const passed = marks.filter(mark => mark >= 40);

Returns:

    New array

---

## 🎯 find()

Find the first matching element.

    const result = numbers.find(number => number > 50);

Returns:

    Element or undefined

---

## 🔎 findIndex()

Find the first matching index.

    const index = numbers.findIndex(number => number > 50);

Returns:

    Index or -1

---

## ❓ some()

Checks whether at least one element satisfies a condition.

    numbers.some(number => number > 50);

Returns:

    true / false

---

## ✅ every()

Checks whether every element satisfies a condition.

    numbers.every(number => number > 0);

Returns:

    true / false

---

## 📊 reduce()

Reduce an array to one value.

    const total = numbers.reduce(
        (sum, number) => sum + number,
        0
    );

---

## 🔢 sort()

Ascending numbers:

    numbers.sort((a, b) => a - b);

Descending:

    numbers.sort((a, b) => b - a);

---

## 🔄 reverse()

    numbers.reverse();

Reverses the array.

---

## 🔍 includes()

    numbers.includes(50);

Returns:

    true / false

---

## 🔎 indexOf()

    numbers.indexOf(50);

Returns:

    Index or -1

---

## 🔗 Method Chaining

    const result = numbers
        .filter(number => number % 2 === 0)
        .map(number => number * 2);

---

## 🧠 Main Difference

| Method | Use |
|---|---|
| `forEach()` | Perform action |
| `map()` | Transform |
| `filter()` | Select |
| `find()` | First match |
| `findIndex()` | First matching index |
| `some()` | Any match |
| `every()` | All match |
| `reduce()` | One final value |
| `sort()` | Sort |
| `reverse()` | Reverse |

---

## 🔥 Mutating Methods

    push()
    pop()
    shift()
    unshift()
    splice()
    sort()
    reverse()

These can modify the original array.

---

## 🟢 Common Non-Mutating Methods

    map()
    filter()
    find()
    findIndex()
    some()
    every()
    includes()
    indexOf()
    slice()

---

## 📌 Remember

- `map()` → new transformed array.
- `filter()` → new selected array.
- `find()` → first matching element.
- `findIndex()` → first matching index.
- `some()` → at least one.
- `every()` → all.
- `reduce()` → one final value.
- Numeric `sort()` needs `(a, b) => a - b`.
- `forEach()` is for actions, not transformation.