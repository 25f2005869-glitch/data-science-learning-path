# 📌 Day 027 — CSS Width, Height and Display — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 027  
**Topic:** CSS Width, Height and Display

---

## 📏 1. Width and Height

    width: 300px;
    height: 200px;

- `width` → Controls horizontal size
- `height` → Controls vertical size

---

## 📐 2. Minimum and Maximum Dimensions

    min-width: 200px;
    max-width: 800px;

    min-height: 100px;
    max-height: 500px;

- `min-width` → Smallest allowed width
- `max-width` → Largest allowed width
- `min-height` → Smallest allowed height
- `max-height` → Largest allowed height

---

## 🔄 3. Auto

    width: auto;
    height: auto;

`auto` lets the browser determine the size according to the layout and content.

---

## 🧱 4. Display Property

    display: block;
    display: inline;
    display: inline-block;
    display: none;

The `display` property controls how an element participates in the layout.

---

## 🟦 5. Block

    display: block;

Characteristics:

- Starts on a new line
- Width and height can be applied
- Takes available horizontal space by default

Examples:

    <div>
    <p>
    <section>
    <h1>

---

## 🟩 6. Inline

    display: inline;

Characteristics:

- Does not normally start a new line
- Uses space required by its content
- Width and height do not behave like block boxes

Examples:

    <span>
    <a>
    <strong>
    <em>

---

## 🟨 7. Inline-Block

    display: inline-block;

Characteristics:

- Can appear beside other elements
- Width can be applied
- Height can be applied
- Padding and borders can be applied

Useful for:

    Cards
    Buttons
    Navigation items

---

## 🚫 8. Display None

    display: none;

Result:

    Element hidden
    +
    Layout space removed

---

## 👻 9. Visibility Hidden

    visibility: hidden;

Result:

    Element hidden
    +
    Layout space preserved

---

## ⚖️ 10. None vs Hidden

| Property | Visible | Takes Space |
|---|---|---|
| `display: none` | ❌ | ❌ |
| `visibility: hidden` | ❌ | ✅ |

---

## 📦 11. Box Sizing

### Default

    box-sizing: content-box;

Width applies to the content area.

### Recommended

    box-sizing: border-box;

Declared width includes:

    Content + Padding + Border

Common reset:

    * {
        box-sizing: border-box;
    }

---

## 🧮 12. Content-Box Calculation

    width: 300px;
    padding: 20px;
    border: 5px solid black;

With `content-box`:

    Total Width
    = 300 + 20 + 20 + 5 + 5
    = 350px

---

## 📦 13. Border-Box Calculation

    width: 300px;
    padding: 20px;
    border: 5px solid black;
    box-sizing: border-box;

Total outer width:

    300px

---

## 📱 14. Responsive Container

Recommended pattern:

    .container {
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
    }

This allows the container to shrink on smaller screens while limiting its maximum width.

---

## 🖼️ 15. Responsive Image

    img {
        max-width: 100%;
        height: auto;
    }

This helps prevent images from overflowing their container.

---

## 📊 16. Quick Comparison

| Property | Purpose |
|---|---|
| `width` | Element width |
| `height` | Element height |
| `min-width` | Minimum width |
| `max-width` | Maximum width |
| `min-height` | Minimum height |
| `max-height` | Maximum height |
| `display: block` | Block layout |
| `display: inline` | Inline layout |
| `display: inline-block` | Inline + controllable dimensions |
| `display: none` | Hide and remove space |
| `visibility: hidden` | Hide but preserve space |
| `box-sizing` | Controls dimension calculation |

---

## ⚡ 17. Common Patterns

### Responsive Container

    width: 100%;
    max-width: 800px;
    margin: 0 auto;

### Fixed Card

    width: 300px;
    min-height: 200px;

### Inline-Block Card

    display: inline-block;
    width: 250px;
    height: 180px;

### Hidden Element

    display: none;

### Invisible but Space Preserved

    visibility: hidden;

### Predictable Sizing

    box-sizing: border-box;

---

## 🧠 18. Remember

    width
    → Horizontal size

    height
    → Vertical size

    min-width
    → Cannot become smaller than this width

    max-width
    → Cannot become larger than this width

    block
    → New line + dimensions

    inline
    → Same line + content-sized behavior

    inline-block
    → Same line + controllable dimensions

    display: none
    → Hidden + no layout space

    visibility: hidden
    → Hidden + layout space remains

    border-box
    → Width/height includes padding and border

---

## 🔗 Navigation

Previous: Day 026 — CSS Margin, Padding and Border

Current: Day 027 — CSS Width, Height and Display

Next: Day 028 — CSS Positioning

---

**Happy Learning! 🚀**