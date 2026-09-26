# 🎨 Day 097 — CSS Complete Revision Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 097  
**Topic:** CSS Complete Revision

---

## 🧱 CSS Syntax

    selector {
        property: value;
    }

---

## 🎯 Selectors

    *               Universal
    p               Element
    .card           Class
    #profile        ID
    h1, h2          Grouping
    section p       Descendant
    section > p     Child
    h2 + p          Adjacent sibling
    h2 ~ p          General sibling

---

## 🔎 Attribute Selectors

    [required]
    [type="email"]
    [href^="https"]
    [src$=".png"]
    [href*="github"]

---

## 🖱️ Pseudo-Classes

    :hover
    :focus
    :focus-visible
    :first-child
    :last-child
    :nth-child()
    :checked
    :disabled

---

## 🧠 Specificity

General priority:

    Inline
      ↓
    ID
      ↓
    Class / Attribute / Pseudo-class
      ↓
    Element

Avoid unnecessary:

    !important

---

## 🎨 Colors

    color
    background-color
    background-image

Formats:

    named
    HEX
    RGB
    RGBA
    HSL
    HSLA

---

## 🖼️ Background

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

---

## 📏 Spacing

    margin
    padding
    border

Center block:

    margin: 0 auto;

---

## 📐 Box Sizing

Recommended common pattern:

    *,
    *::before,
    *::after {
        box-sizing: border-box;
    }

---

## 📏 Sizing

    width
    height
    min-width
    max-width
    min-height
    max-height

Responsive image:

    max-width: 100%;
    height: auto;

---

## 🧩 Display

    block
    inline
    inline-block
    none

Difference:

    display: none
    → removed from layout

    visibility: hidden
    → space remains

---

## 📐 Units

Absolute:

    px
    cm
    mm
    in
    pt
    pc

Relative:

    %
    em
    rem
    vw
    vh
    vmin
    vmax
    ch

---

## 📦 Overflow

    overflow
    overflow-x
    overflow-y

Values:

    visible
    hidden
    scroll
    auto

Text:

    white-space
    overflow
    text-overflow
    overflow-wrap
    word-break

---

## 📍 Position

    static
    relative
    absolute
    fixed
    sticky

Positioning:

    top
    right
    bottom
    left

Stacking:

    z-index

---

## 📦 Flexbox

Container:

    display: flex;

Main properties:

    flex-direction
    justify-content
    align-items
    align-content
    flex-wrap
    gap

Item properties:

    flex
    flex-grow
    flex-shrink
    flex-basis
    order
    align-self

---

## 🧮 Grid

    display: grid;

Important:

    grid-template-columns
    grid-template-rows
    gap
    grid-column
    grid-row

Responsive:

    repeat(auto-fit, minmax(250px, 1fr))

---

## 📱 Responsive Design

Use:

    Flexible layouts
    Flexbox
    Grid
    Relative units
    Media queries
    Responsive images

Viewport:

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

---

## 📺 Media Query

    @media (max-width: 600px) {
        ...
    }

Other conditions:

    min-width
    max-width
    orientation

---

## ✨ Transition

    transition-property
    transition-duration
    transition-timing-function
    transition-delay

Shorthand:

    transition: transform 0.3s ease;

---

## 🔄 Transform

    translate()
    scale()
    rotate()

---

## 🎬 Animation

    @keyframes

Properties:

    animation-name
    animation-duration
    animation-delay
    animation-iteration-count
    animation-direction
    animation-fill-mode
    animation-play-state

---

## ♿ Accessibility

Remember:

    Good contrast
    Visible focus
    Keyboard usability
    Touch-friendly controls
    Reduced motion support
    Do not rely only on hover

---

## ⭐ CSS Formula

**Selectors → Styling → Box Model → Layout → Responsive Design → Animation**