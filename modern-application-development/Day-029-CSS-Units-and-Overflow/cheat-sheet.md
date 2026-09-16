# 📌 Day 029 — CSS Units and Overflow — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 029  
**Topic:** CSS Units and Overflow

---

## 📏 1. CSS Units

CSS units define sizes such as:

- Width
- Height
- Font size
- Margin
- Padding

Two main categories:

    Absolute Units
    Relative Units

---

## 🔹 2. Absolute Units

Common absolute units:

    px
    cm
    mm
    in
    pt
    pc

Most commonly used:

    px

Example:

    width: 300px;

---

## 🔄 3. Relative Units

Common relative units:

    %
    em
    rem
    vw
    vh
    vmin
    vmax
    ch

Useful for responsive designs.

---

## 📊 4. Important Units

| Unit | Based On | Common Use |
|---|---|---|
| `px` | CSS pixel | Fixed sizes |
| `%` | Containing value | Flexible layouts |
| `em` | Element/context font size | Relative sizing |
| `rem` | Root font size | Typography/spacing |
| `vw` | Viewport width | Viewport sizing |
| `vh` | Viewport height | Viewport sizing |
| `vmin` | Smaller viewport dimension | Responsive sizing |
| `vmax` | Larger viewport dimension | Responsive sizing |
| `ch` | Character width approximation | Text width |

---

## 🔤 5. em vs rem

    em
    → Relative to the relevant element/context font size

    rem
    → Relative to the root element's font size

Example:

    html {
        font-size: 16px;
    }

    p {
        font-size: 1.5rem;
    }

Result:

    1.5 × 16px = 24px

---

## 📐 6. Percentage

    width: 50%;

Percentage values are generally calculated relative to a relevant containing value.

Useful for:

    Flexible widths
    Responsive containers
    Parent-relative layouts

---

## 🖥️ 7. Viewport Units

### `vw`

    1vw = 1% of viewport width

Example:

    width: 50vw;

### `vh`

    1vh = 1% of viewport height

Example:

    height: 50vh;

### `vmin`

    1vmin = 1% of the smaller viewport dimension

### `vmax`

    1vmax = 1% of the larger viewport dimension

---

## 0️⃣ 8. Unitless Values

Some properties accept unitless values.

Example:

    line-height: 1.5;
    z-index: 10;

For zero, a unit is normally unnecessary:

    margin: 0;
    padding: 0;
    top: 0;

---

# 🌊 9. CSS Overflow

Overflow occurs when content is larger than the available space.

Main properties:

    overflow
    overflow-x
    overflow-y

---

## 👁️ 10. Overflow Values

### Visible

    overflow: visible;

Content can extend outside the element.

### Hidden

    overflow: hidden;

Overflowing content is clipped.

### Scroll

    overflow: scroll;

Scrolling mechanisms are provided.

### Auto

    overflow: auto;

Scrolling is provided when necessary.

---

## ↔️ 11. Overflow-X

Controls horizontal overflow.

    overflow-x: auto;

Useful for:

    Wide tables
    Long content
    Horizontal scrolling

---

## ↕️ 12. Overflow-Y

Controls vertical overflow.

    overflow-y: auto;

Useful for:

    Long lists
    Fixed-height containers
    Scrollable panels

---

## 📝 13. Text Overflow

Common combination:

    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

This can produce truncated text such as:

    Modern Application De...

---

## 🔤 14. Long Words and URLs

Useful properties:

    overflow-wrap: break-word;

    word-break: break-word;

These can help prevent long unbroken strings from causing horizontal overflow.

---

## 📱 15. Responsive Container

Common pattern:

    .container {
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
    }

This allows the container to shrink while limiting its maximum width.

---

## 🖼️ 16. Responsive Image

    img {
        max-width: 100%;
        height: auto;
    }

Prevents the image from becoming wider than its container while maintaining its aspect ratio.

---

## 📦 17. Scrollable Box

    .box {
        width: 300px;
        height: 200px;
        overflow: auto;
    }

The box becomes scrollable when its content does not fit.

---

## 🎨 18. Rounded Container with Clipping

    .card {
        border-radius: 12px;
        overflow: hidden;
    }

Useful when images or child content should remain inside rounded corners.

---

## ⚖️ 19. Overflow Comparison

| Value | Behavior |
|---|---|
| `visible` | Content can extend outside |
| `hidden` | Overflow is clipped |
| `scroll` | Scrolling mechanism is provided |
| `auto` | Scroll when needed |

---

## ⚡ 20. Quick Syntax

    width: 300px;
    height: 200px;

    width: 50%;
    width: 10rem;
    width: 50vw;

    overflow: hidden;
    overflow: auto;

    overflow-x: auto;
    overflow-y: auto;

    white-space: nowrap;
    text-overflow: ellipsis;

    overflow-wrap: break-word;

---

## 🧠 21. Remember

    px
    → Fixed CSS pixel size

    %
    → Relative to containing value

    em
    → Element/context based

    rem
    → Root based

    vw
    → Viewport width

    vh
    → Viewport height

    overflow: hidden
    → Clip overflow

    overflow: auto
    → Scroll when needed

    max-width: 100%
    → Helps prevent horizontal overflow

---

## 🎯 Key Takeaway

Use **relative units** when flexibility and responsiveness are important, and use **overflow properties** when content may exceed the available space.

A useful responsive combination is:

    width: 100%;
    max-width: 900px;
    overflow: auto;

---

## 🔗 Navigation

Previous: Day 028 — CSS Position and Z-Index

Current: Day 029 — CSS Units and Overflow

Next: Day 030 — CSS Flexbox Basics

---

**Happy Learning! 🚀**