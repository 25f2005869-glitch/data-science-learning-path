# ⚡ Day 039 — Responsive Cards and Layouts Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 039  
**Topic:** Building Responsive Cards and Layouts

---

## 🃏 Basic Card

    .card {
        padding: 1.5rem;
        border: 1px solid #ccc;
        border-radius: 10px;
    }

---

## 📦 Responsive Container

    .container {
        width: 90%;
        max-width: 1100px;
        margin: auto;
    }

---

## 🧩 Basic Grid

    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
    }

---

## 📱 Mobile Grid

    .cards {
        grid-template-columns: 1fr;
    }

---

## 📲 Tablet

    @media (min-width: 700px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

---

## 🖥️ Desktop

    @media (min-width: 1000px) {
        .cards {
            grid-template-columns: repeat(3, 1fr);
        }
    }

---

## ⭐ Automatic Responsive Grid

    .cards {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(220px, 1fr));
        gap: 1rem;
    }

---

## 🔄 `auto-fit`

    repeat(auto-fit, minmax(220px, 1fr))

Existing items can expand after empty tracks collapse.

---

## 🔄 `auto-fill`

    repeat(auto-fill, minmax(220px, 1fr))

Can preserve empty tracks when there are fewer items than available tracks.

---

## 📐 `minmax()`

    minmax(220px, 1fr)

Minimum:

    220px

Maximum:

    1fr

---

## 🖼️ Responsive Image

    img {
        max-width: 100%;
        height: auto;
    }

---

## 🧱 Card with Flexbox

    .card {
        display: flex;
        flex-direction: column;
    }

---

## 🔘 Button at Bottom

    .card-button {
        margin-top: auto;
    }

---

## ↔️ Flexbox Cards

    .cards {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .card {
        flex: 1 1 220px;
    }

---

## 🖱️ Card Hover

    .card {
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

---

## 📌 Sidebar Layout

    .layout {
        display: grid;
        grid-template-columns: 240px 1fr;
        gap: 1rem;
    }

---

## 📱 Mobile Sidebar

    .layout {
        grid-template-columns: 1fr;
    }

---

## 🚫 Avoid

    Large fixed widths
    Unnecessary fixed heights
    Non-responsive images
    Too many breakpoints
    Horizontal overflow

---

## 🧠 Remember

    Grid    → Card/page layout
    Flexbox → Internal alignment
    gap     → Consistent spacing
    minmax  → Flexible track size
    auto-fit → Fit available columns
    max-width → Prevent excessive width

**Responsive Card = Flexible Size + Grid/Flexbox + Responsive Content**