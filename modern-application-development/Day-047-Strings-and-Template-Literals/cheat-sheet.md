# ⚡ Day 047 — Strings and Template Literals — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 047  
**Topic:** Strings and Template Literals

---

## 🧵 Creating Strings

    const a = "Hello";
    const b = 'Hello';
    const c = `Hello`;

---

## 🔢 Indexing

    const word = "Hello";

    word[0];    // H
    word[1];    // e

Indexes start from `0`.

---

## 📏 length

    const word = "Hello";

    word.length;    // 5

Last character:

    word[word.length - 1];

---

## ➕ Concatenation

    const name = "Saloni";
    const course = "MAD 1";

    const message = name + " - " + course;

---

## 🔤 Uppercase

    "hello".toUpperCase();

Result:

    "HELLO"

---

## 🔡 Lowercase

    "HELLO".toLowerCase();

Result:

    "hello"

---

## 🧹 trim()

    "  Saloni  ".trim();

Result:

    "Saloni"

---

## 🔎 includes()

    "JavaScript".includes("Script");

Result:

    true

---

## ▶️ startsWith()

    "JavaScript".startsWith("Java");

Result:

    true

---

## ⏹️ endsWith()

    "index.html".endsWith(".html");

Result:

    true

---

## 🔍 indexOf()

    "JavaScript".indexOf("Script");

Returns the starting index.

Not found:

    -1

---

## ✂️ slice()

    const text = "JavaScript";

    text.slice(0, 4);

Result:

    "Java"

---

## ✂️ substring()

    const text = "JavaScript";

    text.substring(0, 4);

Result:

    "Java"

---

## 🔄 replace()

    "I like Python".replace("Python", "JavaScript");

Result:

    "I like JavaScript"

---

## 📦 split()

    "DBMS,PDSA,MLF".split(",");

Result:

    ["DBMS", "PDSA", "MLF"]

---

## 🧩 Template Literal

    const name = "Saloni";

    const message = `Hello ${name}`;

---

## 🔀 Interpolation

    const a = 10;
    const b = 20;

    `Total = ${a + b}`;

Result:

    "Total = 30"

---

## 📝 Multiline

    const message = `Line one
    Line two
    Line three`;

---

## 🔧 Function in Template Literal

    function square(x) {
        return x * x;
    }

    `Square = ${square(5)}`;

---

## 🧠 Key Difference

| Feature | Example |
|---|---|
| Concatenation | `"Hello " + name` |
| Interpolation | `` `Hello ${name}` `` |
| Multiline | Backtick string |
| Index | Starts at `0` |
| Length | Number of characters |

---

## 📌 Remember

- String index starts at `0`.
- `length` gives character count.
- Strings are immutable.
- `slice(start, end)` excludes `end`.
- `includes()` returns `true` or `false`.
- `indexOf()` returns `-1` when not found.
- Template literals use backticks.
- `${}` inserts variables or expressions.