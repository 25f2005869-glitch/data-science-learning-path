# ⚡ Day 023 — Colors and Backgrounds Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 🎨 Text Color

    color: red;

    color: #ff0000;

    color: rgb(255, 0, 0);

    color: rgba(255, 0, 0, 0.5);

    color: hsl(0, 100%, 50%);

    color: hsla(0, 100%, 50%, 0.5);

---

# 🔢 Color Formats

| Format | Example |
|---|---|
| Name | `red` |
| HEX | `#ff0000` |
| RGB | `rgb(255, 0, 0)` |
| RGBA | `rgba(255, 0, 0, 0.5)` |
| HSL | `hsl(0, 100%, 50%)` |
| HSLA | `hsla(0, 100%, 50%, 0.5)` |

---

# 🎨 Background Color

    body {
        background-color: #f4f6f8;
    }

---

# 🖼️ Background Image

    body {
        background-image: url("background.jpg");
    }

---

# 🔁 Background Repeat

    background-repeat: repeat;

    background-repeat: repeat-x;

    background-repeat: repeat-y;

    background-repeat: no-repeat;

---

# 📍 Background Position

    background-position: center;

    background-position: top;

    background-position: bottom;

    background-position: left;

    background-position: right;

---

# 📐 Background Size

    background-size: cover;

    background-size: contain;

---

# 📜 Background Attachment

    background-attachment: scroll;

    background-attachment: fixed;

---

# 🌈 Linear Gradient

    background: linear-gradient(
        to right,
        blue,
        purple
    );

---

# 🌈 Gradient with Three Colors

    background: linear-gradient(
        to right,
        blue,
        purple,
        pink
    );

---

# 🔄 Radial Gradient

    background: radial-gradient(
        circle,
        blue,
        white
    );

---

# 🔲 Transparent Background

    background-color:
        rgba(0, 0, 0, 0.5);

---

# 🧩 Background Shorthand

    background:
        #f4f6f8
        url("background.jpg")
        no-repeat
        center
        / cover;

---

# 🖼️ Multiple Backgrounds

    background-image:
        url("foreground.png"),
        url("background.jpg");

---

# 🧠 Important Properties

| Property | Purpose |
|---|---|
| `color` | Text color |
| `background-color` | Background color |
| `background-image` | Background image |
| `background-repeat` | Repetition |
| `background-position` | Position |
| `background-size` | Size |
| `background-attachment` | Scroll behavior |
| `background` | Shorthand |

---

# ⭐ Remember

    color
        ↓
    Text Color

    background-color
        ↓
    Background Color

    background-image
        ↓
    Background Image

    cover
        ↓
    Fill Element

    contain
        ↓
    Fit Complete Image

---

# 🏆 Day 023 Core Concepts

    Named Colors
    HEX
    RGB
    RGBA
    HSL
    HSLA
    Background Color
    Background Image
    Background Repeat
    Background Position
    Background Size
    Background Attachment
    Linear Gradient
    Radial Gradient
    Transparency
    Color Contrast