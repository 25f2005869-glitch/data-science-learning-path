# ⚡ Day 035 — Responsive Web Design Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 035  
**Topic:** Responsive Web Design

---

## 📱 Viewport

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

---

## 📐 Flexible Container

    .container {
        width: 90%;
        max-width: 1100px;
        margin: auto;
    }

---

## 🖼️ Responsive Image

    img {
        max-width: 100%;
        height: auto;
    }

---

## 📏 Useful Units

    %       → Parent-relative
    rem     → Root font-relative
    em      → Current font-relative
    vw      → Viewport width
    vh      → Viewport height
    fr      → Grid fraction

---

## 📱 Media Query

    @media (max-width: 600px) {
        ...
    }

---

## 📲 Mobile First

    .cards {
        grid-template-columns: 1fr;
    }

    @media (min-width: 700px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

---

## 🧩 Responsive Flexbox

    .cards {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }

    .card {
        flex: 1 1 250px;
    }

---

## 🧩 Responsive Grid

    .cards {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
    }

---

## 🔄 Common Layout

    Mobile  → 1 column
    Tablet  → 2 columns
    Desktop → 3+ columns

---

## 🚫 Avoid

    Large fixed widths
    Unnecessary breakpoints
    Horizontal page overflow
    Tiny mobile text
    Non-responsive images

---

## 📊 Responsive Table

    .table-container {
        overflow-x: auto;
    }

---

## 📝 Responsive Form

    input,
    textarea,
    select {
        width: 100%;
        max-width: 100%;
    }

---

## ⭐ Core Formula

**Responsive Design = Flexible Sizing + Media Queries + Flexbox/Grid + Responsive Images**