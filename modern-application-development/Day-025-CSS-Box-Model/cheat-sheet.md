# ⚡ Day 025 — CSS Box Model Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 📦 CSS Box Model

Every HTML element can be understood as a box.

The four components from inside to outside are:

Content → Padding → Border → Margin

---

## 🧩 Box Model Structure

    ┌─────────────────────────────────┐
    │             Margin              │
    │   ┌─────────────────────────┐   │
    │   │         Border          │   │
    │   │   ┌─────────────────┐   │   │
    │   │   │     Padding     │   │   │
    │   │   │   ┌───────────┐ │   │   │
    │   │   │   │  Content  │ │   │   │
    │   │   │   └───────────┘ │   │   │
    │   │   └─────────────────┘   │   │
    │   └─────────────────────────┘   │
    └─────────────────────────────────┘

---

## 📄 Content

The actual content of an element.

    width: 300px;
    height: 200px;

---

## 🟦 Padding

Space between content and border.

    padding: 20px;

Individual sides:

    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 30px;
    padding-left: 40px;

---

## 📐 Padding Shorthand

### One Value

    padding: 20px;

    Top = 20px
    Right = 20px
    Bottom = 20px
    Left = 20px

### Two Values

    padding: 10px 20px;

    Top + Bottom = 10px
    Left + Right = 20px

### Three Values

    padding: 10px 20px 30px;

    Top = 10px
    Left + Right = 20px
    Bottom = 30px

### Four Values

    padding: 10px 20px 30px 40px;

    Top = 10px
    Right = 20px
    Bottom = 30px
    Left = 40px

Memory:

    T → R → B → L
    Top → Right → Bottom → Left

---

## 🟥 Border

Border surrounds the content and padding.

Basic syntax:

    border: 2px solid black;

Structure:

    border: width style color;

Example:

    border: 3px solid blue;

---

## 🎨 Border Properties

    border-width: 2px;
    border-style: solid;
    border-color: black;

Common border styles:

    solid
    dashed
    dotted
    double
    groove
    ridge
    inset
    outset
    none

---

## 🔵 Border Radius

Creates rounded corners.

    border-radius: 10px;

Circle:

    width: 100px;
    height: 100px;
    border-radius: 50%;

---

## 🟩 Margin

Space outside the border.

    margin: 20px;

Individual sides:

    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 30px;
    margin-left: 40px;

---

## 📐 Margin Shorthand

### One Value

    margin: 20px;

All four sides = 20px

### Two Values

    margin: 10px 20px;

    Top + Bottom = 10px
    Left + Right = 20px

### Three Values

    margin: 10px 20px 30px;

    Top = 10px
    Left + Right = 20px
    Bottom = 30px

### Four Values

    margin: 10px 20px 30px 40px;

    Top = 10px
    Right = 20px
    Bottom = 30px
    Left = 40px

---

## 🎯 Centering a Block

A common technique:

    width: 400px;
    margin: 0 auto;

This commonly centers a fixed-width block horizontally.

---

## 📏 Width and Height

    width: 300px;
    height: 200px;

Minimum:

    min-width: 300px;
    min-height: 200px;

Maximum:

    max-width: 1000px;
    max-height: 600px;

---

## 📦 Box Sizing

### Default

    box-sizing: content-box;

### Alternative

    box-sizing: border-box;

---

## 🆚 `content-box` vs `border-box`

### `content-box`

Declared width applies to content.

    width: 300px;
    padding: 20px;
    border: 5px solid black;

Total width:

    300 + 20 + 20 + 5 + 5
    = 350px

### `border-box`

Declared width includes:

    Content + Padding + Border

Example:

    width: 300px;
    padding: 20px;
    border: 5px solid black;
    box-sizing: border-box;

Total width:

    300px

---

## ⭐ Recommended Global Rule

    * {
        box-sizing: border-box;
    }

This makes element sizing more predictable.

---

## 🧮 Content-Box Width Formula

    Total Width =
    Content Width
    + Left Padding
    + Right Padding
    + Left Border
    + Right Border

---

## 🧮 Content-Box Height Formula

    Total Height =
    Content Height
    + Top Padding
    + Bottom Padding
    + Top Border
    + Bottom Border

---

## 🚨 Important

Margin is outside the box.

It is NOT included in the content-box or border-box width.

---

## 🆚 Padding vs Margin

    Padding = Inside the border
    Margin  = Outside the border

Quick memory:

    Content
       ↓
    Padding
       ↓
    Border
       ↓
    Margin

---

## 🔄 Margin Collapsing

Vertical margins between some block-level elements can collapse.

Example:

    .first {
        margin-bottom: 30px;
    }

    .second {
        margin-top: 20px;
    }

The resulting vertical gap may be 30px instead of 50px.

---

## 💡 Common Card Pattern

    * {
        box-sizing: border-box;
    }

    .card {
        width: 300px;
        padding: 20px;
        border: 2px solid black;
        margin: 20px auto;
        border-radius: 10px;
    }

---

## 📊 Quick Reference

| Property | Purpose |
|---|---|
| `width` | Controls width |
| `height` | Controls height |
| `min-width` | Minimum width |
| `max-width` | Maximum width |
| `min-height` | Minimum height |
| `max-height` | Maximum height |
| `padding` | Internal spacing |
| `border` | Border around the box |
| `border-radius` | Rounded corners |
| `margin` | External spacing |
| `box-sizing` | Controls size calculation |

---

## 🧠 One-Line Memory Trick

    Padding = Inside
    Border  = Boundary
    Margin  = Outside

---

## 🚀 Most Important Properties to Remember

    width
    height
    padding
    border
    border-radius
    margin
    box-sizing
    min-width
    max-width
    min-height
    max-height

---

## ✅ Day 025 Quick Revision

    Box Model
    ↓
    Content
    ↓
    Padding
    ↓
    Border
    ↓
    Margin

    content-box → Width excludes padding and border

    border-box → Width includes padding and border

    margin: 0 auto → Common horizontal centering technique

    * {
        box-sizing: border-box;
    }