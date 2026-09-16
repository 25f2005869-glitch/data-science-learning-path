# ⚡ Day 022 — CSS Selectors Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🎯 Basic Syntax

    selector {
        property: value;
    }

---

## ⭐ Basic Selectors

### Universal

    * {
        box-sizing: border-box;
    }

### Element

    p {
        color: blue;
    }

### Class

    .box {
        color: blue;
    }

### ID

    #title {
        color: red;
    }

### Grouping

    h1, h2, h3 {
        color: blue;
    }

---

# 🔗 Combinators

### Descendant

    section p {
        color: blue;
    }

Means:

    Any p inside section

---

### Child

    section > p {
        color: green;
    }

Means:

    Direct p child of section

---

### Adjacent Sibling

    h2 + p {
        color: red;
    }

Means:

    First p immediately after h2

---

### General Sibling

    h2 ~ p {
        color: green;
    }

Means:

    Matching p siblings after h2

---

# 🎯 Attribute Selectors

### Has Attribute

    [required] {
        border: 1px solid red;
    }

### Exact Value

    input[type="email"] {
        background-color: lightblue;
    }

### Starts With

    a[href^="https"] {
        color: green;
    }

### Ends With

    img[src$=".png"] {
        border: 1px solid black;
    }

### Contains

    a[href*="github"] {
        font-weight: bold;
    }

---

# 🖱️ Pseudo-Classes

### Hover

    a:hover {
        color: red;
    }

### Focus

    input:focus {
        background-color: lightyellow;
    }

### First Child

    li:first-child {
        font-weight: bold;
    }

### Last Child

    li:last-child {
        color: red;
    }

### nth Child

    li:nth-child(2) {
        color: blue;
    }

### Odd

    li:nth-child(odd) {
        background-color: lightgray;
    }

### Even

    li:nth-child(even) {
        background-color: white;
    }

### Checked

    input:checked {
        accent-color: green;
    }

### Disabled

    input:disabled {
        background-color: lightgray;
    }

---

# 🔥 Combining Selectors

Element + Class:

    p.highlight {
        color: red;
    }

Two Classes:

    .card.featured {
        border: 2px solid blue;
    }

Class + Descendant:

    .card p {
        color: gray;
    }

Element + ID:

    section#about {
        background-color: lightgray;
    }

---

# 🧠 Specificity

Simplified order:

    ID
    ↓
    Class / Attribute / Pseudo-class
    ↓
    Element

Example:

    #title
    .title
    h1

Priority:

    #title > .title > h1

---

# 📌 Symbols

| Symbol | Meaning |
|---|---|
| `*` | Universal |
| `.` | Class |
| `#` | ID |
| `,` | Group |
| Space | Descendant |
| `>` | Child |
| `+` | Adjacent sibling |
| `~` | General sibling |
| `[]` | Attribute |
| `:` | Pseudo-class |

---

# ⚠️ Best Practices

- Use classes for reusable styles.
- Keep IDs unique.
- Avoid overly complex selectors.
- Use meaningful class names.
- Avoid unnecessary `!important`.
- Keep selectors readable.

---

# 🏆 Most Important

    p
    .class
    #id
    *
    h1, h2
    div p
    div > p
    h2 + p
    h2 ~ p
    [required]
    input[type="email"]
    a:hover
    input:focus
    li:first-child
    li:nth-child(2)

---

## 🧠 Remember

    Selector
        ↓
    Select HTML Element
        ↓
    Apply CSS Rule