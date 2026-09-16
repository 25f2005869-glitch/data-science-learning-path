# 📍 Day 028 — CSS Position and Z-Index

![CSS](https://img.shields.io/badge/Technology-CSS-blue)
![Day](https://img.shields.io/badge/Day-028-orange)
![Topic](https://img.shields.io/badge/Topic-Position%20%7C%20Z--Index-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 📖 Introduction

CSS positioning allows you to control the location of elements on a webpage.

The `position` property determines how an element is positioned in relation to the normal document flow, its containing block, or the viewport.

The `z-index` property controls the stacking order of overlapping elements.

Understanding positioning and stacking is essential for creating navigation bars, badges, overlays, floating buttons, tooltips, headers, and other practical web layouts.

---

## 🎯 Learning Objectives

By the end of Day 028, you will be able to:

- Understand the CSS `position` property.
- Understand `position: static`.
- Understand `position: relative`.
- Understand `position: absolute`.
- Understand `position: fixed`.
- Understand `position: sticky`.
- Use `top`, `right`, `bottom`, and `left`.
- Understand normal document flow.
- Position an element relative to its parent.
- Understand containing blocks.
- Create overlapping elements.
- Use the `z-index` property.
- Understand stacking order.
- Control which element appears above another.
- Create practical positioned components.
- Avoid common positioning mistakes.

---

## 📚 Topics Covered

### 1. CSS Position Property

The `position` property specifies how an element is positioned.

Common values:

    position: static;
    position: relative;
    position: absolute;
    position: fixed;
    position: sticky;

---

### 2. Position Static

`static` is the default positioning behavior.

Example:

    .box {
        position: static;
    }

A statically positioned element follows the normal document flow.

The `top`, `right`, `bottom`, and `left` properties do not reposition a static element.

---

### 3. Position Relative

`relative` keeps the element in the normal document flow while allowing it to be visually offset.

Example:

    .box {
        position: relative;
        top: 20px;
        left: 30px;
    }

The original space occupied by the element is preserved.

---

### 4. Position Absolute

`absolute` removes the element from the normal document flow.

Example:

    .box {
        position: absolute;
        top: 20px;
        right: 20px;
    }

An absolutely positioned element is positioned relative to its containing block.

A common pattern is:

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
        top: 0;
        right: 0;
    }

The relatively positioned parent establishes the positioning context for the child.

---

### 5. Position Fixed

`fixed` positions an element relative to the viewport in typical browser layouts.

Example:

    .button {
        position: fixed;
        right: 20px;
        bottom: 20px;
    }

The element generally remains in the same viewport position while the page is scrolled.

Common uses:

- Floating action buttons
- Fixed navigation
- Support buttons
- Back-to-top controls

---

### 6. Position Sticky

`sticky` combines characteristics of relative and fixed positioning.

Example:

    .header {
        position: sticky;
        top: 0;
    }

The element participates in normal flow until its sticky threshold is reached, after which it can remain attached to that edge while scrolling within its scrolling context.

Sticky positioning depends on the surrounding layout and scrolling container.

---

## 📐 7. Top, Right, Bottom and Left

These properties are commonly used with positioned elements.

Example:

    position: relative;
    top: 10px;
    left: 20px;

Common properties:

    top
    right
    bottom
    left

They specify offsets from the relevant containing block or viewport, depending on the positioning scheme.

---

## 🔄 8. Normal Document Flow

Normally, HTML elements are arranged according to the document flow.

For example:

    <div>Box 1</div>
    <div>Box 2</div>
    <div>Box 3</div>

Each block element normally appears according to the standard flow.

Positioning can change how an element participates in this flow.

---

## 📦 9. Relative vs Absolute

| Feature | Relative | Absolute |
|---|---|---|
| Normal space preserved | Yes | No |
| Can use offsets | Yes | Yes |
| Positioned relative to | Its normal position | Containing block |
| Common use | Small adjustments/context | Overlays and positioned children |

---

## 📌 10. Absolute Positioning with a Parent

A common pattern is:

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

The parent establishes a positioning context, allowing the badge to be placed precisely inside the card.

---

## 📱 11. Fixed Positioning

Fixed elements are positioned relative to the viewport.

Example:

    .help-button {
        position: fixed;
        right: 20px;
        bottom: 20px;
    }

This can be useful for elements that should remain accessible while scrolling.

---

## 📌 12. Sticky Positioning

Example:

    nav {
        position: sticky;
        top: 0;
    }

A sticky element needs an appropriate offset such as `top`, `bottom`, `left`, or `right` to define when the sticky behavior takes effect.

---

# 🧱 13. Z-Index

`z-index` controls the stacking order of overlapping elements.

Example:

    .box {
        position: relative;
        z-index: 2;
    }

A larger stacking level generally places an element above another overlapping element within the same stacking context.

---

## 🔢 14. Z-Index Values

Examples:

    z-index: 1;
    z-index: 5;
    z-index: 10;
    z-index: 100;

Negative values are also possible:

    z-index: -1;

The exact visual result also depends on stacking contexts and the elements involved.

---

## 🥞 15. Stacking Order

Imagine overlapping elements as layers.

For example:

    z-index: 1;
    z-index: 2;
    z-index: 3;

Generally:

    3 → Top
    2 → Middle
    1 → Bottom

When elements overlap within the same stacking context, the appropriate stacking order determines which one appears above the other.

---

## 🎯 16. Practical Z-Index Example

    .box-one {
        position: absolute;
        z-index: 1;
    }

    .box-two {
        position: absolute;
        z-index: 2;
    }

Here, `.box-two` is generally placed above `.box-one` when they overlap in the same stacking context.

---

## 🧩 17. Stacking Context

A stacking context is an independent layering context used by the browser when determining how elements are painted.

`z-index` does not always compare elements globally.

Properties such as positioning combined with `z-index`, as well as certain other CSS properties, can create stacking contexts.

Therefore, a child with a very large `z-index` cannot necessarily appear above an element in a different stacking context.

---

## 🛠️ 18. Common Practical Patterns

### Badge on a Card

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

### Floating Button

    .button {
        position: fixed;
        right: 20px;
        bottom: 20px;
    }

### Sticky Header

    header {
        position: sticky;
        top: 0;
    }

### Centered Absolute Element

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

---

## ⚠️ 19. Common Mistakes

### Mistake 1: Using Absolute Positioning Everywhere

Excessive absolute positioning can make layouts difficult to maintain and responsive behavior harder to manage.

---

### Mistake 2: Forgetting the Parent Position

If an absolutely positioned child should be positioned inside a specific parent, the parent commonly needs:

    position: relative;

---

### Mistake 3: Expecting Static Elements to Respond to Offsets

This does not reposition a static element:

    position: static;
    top: 20px;

Use an appropriate non-static positioning value.

---

### Mistake 4: Using Extremely Large Z-Index Values

Avoid unnecessary values such as:

    z-index: 999999999;

Use a simple, organized layering system when possible.

---

### Mistake 5: Sticky Position Not Working

Sticky positioning can be affected by:

- Missing offset such as `top`
- Parent or ancestor scrolling behavior
- Container dimensions
- Overflow settings
- Available scrolling space

---

## 🌐 20. Positioning and Responsive Design

Positioning should be tested at different screen sizes.

Avoid depending on many hard-coded coordinates such as:

    left: 437px;
    top: 286px;

Prefer flexible layouts and use positioning only when it solves a specific layout requirement.

---

## 🚀 Skills Developed

After completing Day 028, you will be able to:

- Position elements using different CSS positioning modes.
- Understand normal document flow.
- Offset elements using directional properties.
- Position children inside a parent.
- Create floating elements.
- Create sticky components.
- Create fixed components.
- Control overlapping elements.
- Use `z-index` effectively.
- Understand basic stacking contexts.

---

## 📂 Repository Contents

    Day-028-CSS-Position-and-Z-Index/
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

**Previous:** Day 027 — CSS Width, Height and Display

**Current:** Day 028 — CSS Position and Z-Index

**Next:** Day 029 — CSS Flexbox

---

## ⭐ About this Repository

This repository is part of a structured **100-Day Modern Application Development learning journey** for the IIT Madras BS Degree Programme.

Day 028 focuses on CSS positioning and stacking. These concepts provide the foundation for placing elements precisely and managing overlapping components in modern web interfaces.

---

## 🎯 Day 028 Goal

Build a strong understanding of **CSS positioning and stacking order** so that you can confidently control where elements appear and how overlapping elements are layered on a webpage.

---

**Happy Learning! 🚀**