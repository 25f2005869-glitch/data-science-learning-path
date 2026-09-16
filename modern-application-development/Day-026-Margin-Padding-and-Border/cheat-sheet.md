# 📌 CSS Margin, Padding and Border — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 026  
**Topic:** CSS Margin, Padding and Border

---

## 📦 1. CSS Box Model

Every HTML element is treated as a box:

    Content → Padding → Border → Margin

- **Content:** Actual text, image, or element content
- **Padding:** Space inside the element
- **Border:** Line surrounding padding/content
- **Margin:** Space outside the element

---

## 📏 2. Margin

Margin creates space **outside** an element.

    margin: 20px;

### Individual Sides

    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 15px;
    margin-left: 25px;

### Shorthand

    margin: 10px 20px 15px 25px;

Order:

    Top → Right → Bottom → Left

### Two Values

    margin: 10px 20px;

Means:

    Top/Bottom → 10px
    Left/Right → 20px

### Three Values

    margin: 10px 20px 30px;

Means:

    Top → 10px
    Left/Right → 20px
    Bottom → 30px

### Auto Margin

    margin: 0 auto;

Commonly used to horizontally center a block element with a defined width.

---

## ⚠️ 3. Negative Margin

Negative margins can move an element closer to another element or create overlap.

    margin-top: -10px;

Use carefully because excessive negative margins can make layouts difficult to maintain.

---

## 🔄 4. Margin Collapsing

Vertical margins between normal block elements can sometimes collapse.

Example:

    .box1 {
        margin-bottom: 20px;
    }

    .box2 {
        margin-top: 30px;
    }

The resulting vertical gap may be **30px**, not 50px.

Margin collapsing mainly occurs with vertical margins of block-level elements in normal document flow.

---

## 🛏️ 5. Padding

Padding creates space **inside** an element, between the content and border.

    padding: 20px;

### Individual Sides

    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 15px;
    padding-left: 25px;

### Shorthand

    padding: 10px 20px 15px 25px;

Order:

    Top → Right → Bottom → Left

### Two Values

    padding: 10px 20px;

Means:

    Top/Bottom → 10px
    Left/Right → 20px

---

## 🧱 6. Border

Border surrounds the content and padding.

Basic syntax:

    border: width style color;

Example:

    border: 2px solid black;

### Border Width

    border-width: 2px;

### Border Style

Common values:

    solid
    dashed
    dotted
    double
    groove
    ridge
    inset
    outset
    none
    hidden

### Border Color

    border-color: blue;

---

## 🎯 7. Individual Borders

    border-top: 2px solid black;
    border-right: 2px solid blue;
    border-bottom: 2px solid green;
    border-left: 2px solid red;

---

## 🔵 8. Border Radius

Rounds the corners of an element.

    border-radius: 10px;

### Circle

For a square element:

    width: 100px;
    height: 100px;
    border-radius: 50%;

---

## 📐 9. Individual Border Radius

    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;

---

## 📊 10. Margin vs Padding

| Property | Location | Background Visible? | Main Purpose |
|---|---|---|---|
| Margin | Outside border | No | Space between elements |
| Padding | Inside border | Yes | Space around content |
| Border | Around padding/content | Border itself | Visual boundary |

---

## 📦 11. Box Sizing

### content-box

Default behavior:

    box-sizing: content-box;

Declared width applies to the content only.

Actual width can become:

    Content width + Left/Right padding + Left/Right border

### border-box

    box-sizing: border-box;

Declared width includes:

    Content + Padding + Border

Recommended common reset:

    * {
        box-sizing: border-box;
    }

---

## 📏 12. Width and Height

    width: 300px;
    height: 200px;

Useful related properties:

    min-width: 200px;
    max-width: 800px;

    min-height: 100px;
    max-height: 500px;

---

## 🧮 13. Box Model Calculation

With:

    width: 300px;
    padding: 20px;
    border: 5px solid black;

Using `content-box`:

    Total width
    = 300 + 20 + 20 + 5 + 5
    = 350px

Using `border-box`:

    Total declared width
    = 300px

---

## 🎨 14. Common Card Pattern

    .card {
        width: 300px;
        padding: 20px;
        border: 1px solid #ccc;
        margin: 20px auto;
        border-radius: 10px;
        box-sizing: border-box;
    }

---

## 🔘 15. Common Button Pattern

    .button {
        padding: 10px 20px;
        border: 2px solid black;
        border-radius: 6px;
        margin: 10px;
    }

---

## 📌 16. Useful Units

### Fixed

    px

### Relative

    %

    em

    rem

    vw

    vh

For responsive layouts, prefer suitable relative units where appropriate.

---

## ⚡ 17. Quick Syntax Reference

    margin: 20px;

    padding: 20px;

    border: 2px solid black;

    border-radius: 10px;

    box-sizing: border-box;

    margin: 0 auto;

    width: 300px;

    max-width: 100%;

---

## 🧠 18. Remember

    Margin = Outside Space

    Padding = Inside Space

    Border = Boundary

    Content = Actual Content

    box-sizing: border-box = Width includes padding and border

---

## ⚠️ 19. Common Mistakes

- Confusing margin with padding
- Forgetting the four-value order
- Using excessive negative margins
- Ignoring `box-sizing`
- Using fixed widths without considering smaller screens
- Adding unnecessary borders
- Using margins when internal spacing requires padding

---

## 🎯 Quick Revision

**Q:** Space outside an element?

**A:** `margin`

**Q:** Space between content and border?

**A:** `padding`

**Q:** Line around an element?

**A:** `border`

**Q:** Property for rounded corners?

**A:** `border-radius`

**Q:** Center a fixed-width block horizontally?

**A:** `margin: 0 auto`

**Q:** Make declared width include padding and border?

**A:** `box-sizing: border-box`

---

## 🔗 Navigation

Previous: Day 025 — CSS Box Model  
Next: Day 027 — CSS Display and Visibility

---

**Happy Learning! 🚀**