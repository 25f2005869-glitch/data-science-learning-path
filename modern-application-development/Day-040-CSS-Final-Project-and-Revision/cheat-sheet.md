# ⚡ Day 040 — CSS Final Revision Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 040  
**Topic:** CSS Final Project and Revision

---

## 🎯 CSS Syntax

    selector {
        property: value;
    }

---

## 🎯 Selectors

| Selector | Meaning |
|---|---|
| `*` | Universal |
| `p` | Element |
| `.card` | Class |
| `#main` | ID |
| `h1, h2` | Group |
| `section p` | Descendant |
| `section > p` | Direct child |
| `input[type="email"]` | Attribute |
| `a:hover` | Pseudo-class |

---

## 🎨 Colors

    color: red;
    color: #2563eb;
    color: rgb(37, 99, 235);
    color: rgba(37, 99, 235, 0.8);
    color: hsl(217, 75%, 53%);

---

## 🖼️ Background

    background-color
    background-image
    background-repeat
    background-position
    background-size
    background-attachment

Common:

    background-size: cover;

---

## 🔤 Fonts

    font-family
    font-size
    font-weight
    font-style
    line-height

---

## ✍️ Text

    text-align
    text-decoration
    text-transform
    text-indent
    letter-spacing
    word-spacing
    text-shadow

---

## 📦 Box Model

    Content
       ↓
    Padding
       ↓
    Border
       ↓
    Margin

Recommended:

    box-sizing: border-box;

---

## 📏 Sizing

    width
    height
    min-width
    max-width
    min-height
    max-height

Responsive:

    max-width: 100%;

---

## 📌 Display

    display: block;
    display: inline;
    display: inline-block;
    display: none;

`display: none` → removed from layout.

`visibility: hidden` → hidden but space remains.

---

## 📍 Position

    position: static;
    position: relative;
    position: absolute;
    position: fixed;
    position: sticky;

Offsets:

    top
    right
    bottom
    left

Stacking:

    z-index: 10;

---

## 📐 Units

Absolute:

    px, cm, mm, in, pt, pc

Relative:

    %, em, rem, vw, vh, vmin, vmax, ch

Common choices:

    px  → borders/small fixed details
    rem → typography
    %   → parent-relative sizing
    vw/vh → viewport-relative sizing

---

## 🚧 Overflow

    overflow: visible;
    overflow: hidden;
    overflow: scroll;
    overflow: auto;

Text:

    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

---

## 📦 Flexbox

Container:

    display: flex;

Main properties:

    flex-direction
    flex-wrap
    justify-content
    align-items
    align-content
    gap

Center:

    display: flex;
    justify-content: center;
    align-items: center;

---

## 🧱 Grid

    display: grid;

Useful:

    grid-template-columns
    grid-template-rows
    gap
    grid-column
    grid-row

Responsive:

    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));

---

## 📱 Media Query

    @media (min-width: 768px) {
        ...
    }

Common strategy:

    Mobile
      ↓
    Tablet
      ↓
    Desktop

---

## ✨ Transition

    transition: property duration timing-function delay;

Example:

    transition: transform 0.3s ease;

---

## 🔄 Transform

    transform: translateY(-5px);
    transform: scale(1.05);
    transform: rotate(5deg);

---

## 🎬 Animation

    @keyframes name {
        from {
            ...
        }

        to {
            ...
        }
    }

    animation: name 2s ease infinite;

---

## ♿ Accessibility

Use:

- Good color contrast
- Visible focus states
- Semantic HTML
- Responsive text
- Meaningful labels
- `:focus-visible`
- Reduced-motion support

Example:

    @media (prefers-reduced-motion: reduce) {
        * {
            animation: none !important;
            transition: none !important;
        }
    }

---

## ⭐ CSS Final Formula

    Select
      +
    Style
      +
    Box Model
      +
    Layout
      +
    Responsive Design
      +
    Interaction
      =
    Complete CSS Page