# ⚡ Day 021 — Introduction to CSS Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🎨 CSS

CSS = Cascading Style Sheets

CSS controls webpage presentation.

    HTML → Structure
    CSS  → Presentation
    JS   → Behaviour

---

## 🧱 Basic Syntax

    selector {
        property: value;
    }

Example:

    p {
        color: blue;
    }

---

## 🔑 CSS Terms

    p {
        color: blue;
    }

    p     → Selector
    color → Property
    blue  → Value

    color: blue;
    → Declaration

---

## 🎯 Common Selectors

Element selector:

    p {
        color: blue;
    }

Class selector:

    .box {
        color: blue;
    }

ID selector:

    #title {
        color: blue;
    }

---

## 📝 Inline CSS

    <h1 style="color: blue;">
        Hello
    </h1>

---

## 📝 Internal CSS

    <style>

        h1 {
            color: blue;
        }

    </style>

---

## 📄 External CSS

HTML:

    <link rel="stylesheet"
          href="style.css">

CSS:

    h1 {
        color: blue;
    }

---

## 🌈 Colors

Color name:

    color: red;

Hex:

    color: #ff0000;

RGB:

    color: rgb(255, 0, 0);

RGBA:

    color: rgba(255, 0, 0, 0.5);

HSL:

    color: hsl(0, 100%, 50%);

---

## 🖌️ Text Color

    p {
        color: green;
    }

---

## 🎨 Background

    body {
        background-color: lightgray;
    }

---

## 🔠 Font Size

    h1 {
        font-size: 32px;
    }

---

## 📐 Text Alignment

    h1 {
        text-align: center;
    }

Values:

    left
    center
    right
    justify

---

## 💬 CSS Comment

    /* This is a CSS comment */

---

## 🔥 Multiple Properties

    h1 {
        color: blue;
        background-color: lightgray;
        font-size: 32px;
        text-align: center;
    }

---

## 🧠 Three CSS Methods

| Method | Syntax |
|---|---|
| Inline | `style=""` |
| Internal | `<style>` |
| External | `.css` file |

---

## ⭐ Recommended Approach

For larger projects:

    HTML → Structure

    CSS → Separate stylesheet

Example:

    index.html
    style.css

---

## 🔑 Remember

    Selector
        ↓
    Property
        ↓
    Value

Example:

    h1 {
        color: red;
    }

---

## 📌 Important Properties

    color
    background-color
    font-size
    text-align

---

## 🏆 Day 021 Goal

Understand:

    CSS
    ↓
    Syntax
    ↓
    Selectors
    ↓
    Properties
    ↓
    Values
    ↓
    Styling HTML