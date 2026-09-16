# 📏 Day 027 — CSS Width, Height and Display

![CSS](https://img.shields.io/badge/Technology-CSS-blue)
![Day](https://img.shields.io/badge/Day-027-orange)
![Topic](https://img.shields.io/badge/Topic-Width%20%7C%20Height%20%7C%20Display-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 📖 Introduction

CSS provides properties to control the **size and display behavior** of HTML elements.

In this day, we learn how to control an element's width and height and understand how the `display` property determines how an element participates in the page layout.

Understanding these concepts is essential for creating structured, responsive, and well-organized web pages.

---

## 🎯 Learning Objectives

By the end of Day 027, you will be able to:

- Understand CSS `width` and `height`.
- Use `min-width` and `max-width`.
- Use `min-height` and `max-height`.
- Understand the `auto` value.
- Understand block-level elements.
- Understand inline elements.
- Understand inline-block elements.
- Use `display: block`.
- Use `display: inline`.
- Use `display: inline-block`.
- Use `display: none`.
- Understand `visibility: hidden`.
- Differentiate `display: none` and `visibility: hidden`.
- Understand how width and height behave with different display values.
- Use `box-sizing` with width and height.
- Create responsive containers using `max-width`.

---

## 📚 Topics Covered

### 1. Width

The `width` property controls the horizontal size of an element.

Common values include:

- `px`
- `%`
- `em`
- `rem`
- `vw`
- `auto`

Example:

    width: 300px;

---

### 2. Height

The `height` property controls the vertical size of an element.

Example:

    height: 200px;

---

### 3. Minimum and Maximum Width

CSS provides:

    min-width

    max-width

These properties control the minimum and maximum allowed width of an element.

Example:

    min-width: 200px;
    max-width: 800px;

---

### 4. Minimum and Maximum Height

CSS also provides:

    min-height

    max-height

Example:

    min-height: 100px;
    max-height: 500px;

---

### 5. Auto

The `auto` value allows the browser to determine the appropriate size based on the layout and available space.

Example:

    width: auto;
    height: auto;

---

## 🧱 6. Display Property

The `display` property controls how an element behaves in the layout.

Common values:

    display: block;

    display: inline;

    display: inline-block;

    display: none;

---

## 🟦 7. Block Elements

Block-level elements generally:

- Start on a new line.
- Take available horizontal space by default.
- Allow width and height to be applied.

Examples:

    <div>
    <p>
    <h1>
    <section>
    <header>
    <footer>

---

## 🟩 8. Inline Elements

Inline elements generally:

- Stay in the same line when space is available.
- Take only the space required by their content.
- Do not behave like block elements for width and height.

Examples:

    <span>
    <a>
    <strong>
    <em>

---

## 🟨 9. Inline-Block

`inline-block` combines important characteristics of inline and block elements.

An inline-block element:

- Can appear alongside other elements.
- Allows width and height.
- Allows padding and borders.

Example:

    display: inline-block;

---

## 🚫 10. Display None

`display: none` removes an element from the layout.

Example:

    display: none;

The element:

- Is not displayed.
- Does not occupy layout space.

---

## 👻 11. Visibility Hidden

`visibility: hidden` hides an element while keeping its layout space.

Example:

    visibility: hidden;

---

## ⚖️ 12. Display None vs Visibility Hidden

| Property | Element Visible? | Space Occupied? |
|---|---|---|
| `display: none` | No | No |
| `visibility: hidden` | No | Yes |

---

## 📦 13. Width, Height and Box Sizing

The `box-sizing` property affects how the declared width and height are calculated.

Example:

    box-sizing: border-box;

With `border-box`, the declared width includes:

    Content + Padding + Border

This makes element sizing easier to control.

---

## 📱 14. Responsive Width

A common responsive pattern is:

    width: 100%;
    max-width: 800px;

This allows an element to shrink on smaller screens while preventing it from becoming excessively wide on larger screens.

---

## 💻 15. Practical Examples

### Fixed Container

    .container {
        width: 800px;
        height: 300px;
    }

### Responsive Container

    .container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }

### Inline-Block Cards

    .card {
        display: inline-block;
        width: 250px;
        height: 200px;
    }

### Hidden Element

    .hidden {
        display: none;
    }

---

## 🚀 Skills Developed

After completing Day 027, you will be able to:

- Control element dimensions.
- Create fixed-size containers.
- Create flexible containers.
- Set minimum and maximum dimensions.
- Understand block and inline behavior.
- Convert elements between display types.
- Hide elements correctly.
- Build simple card layouts.
- Create more responsive page structures.

---

## 📂 Repository Contents

    Day-027-Width-Height-and-Display/
    │
    ├── README.md
    ├── notes.md
    ├── cheat-sheet.md
    ├── practice.md
    └── code/
        └── index.html

---

## 💻 Technologies Used

- HTML5
- CSS3
- Visual Studio Code
- Live Server
- Web Browser

---

## 📌 Navigation

**Previous:** Day 026 — CSS Margin, Padding and Border

**Current:** Day 027 — CSS Width, Height and Display

**Next:** Day 028 — CSS Positioning

---

## ⭐ About this Repository

This repository is part of a structured **100-Day Modern Application Development learning journey** for the IIT Madras BS Degree Programme.

Day 027 focuses on controlling element dimensions and understanding how CSS display modes affect webpage layout.

The goal is to build strong CSS fundamentals before progressing to more advanced layout and positioning concepts.

---

## 🎯 Day 027 Goal

Build a strong understanding of **CSS dimensions and display behavior** and learn how different display values affect the layout, size, and visibility of HTML elements.

---

**Happy Learning! 🚀**