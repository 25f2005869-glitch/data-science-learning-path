# ⚡ Day 034 — CSS Grid Advanced Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 034  
**Topic:** CSS Grid Advanced

---

## 📍 Grid Placement

    grid-column: 1 / 3;

Start at column line 1 and end at line 3.

    grid-row: 1 / 3;

Start at row line 1 and end at line 3.

---

## ➡️ Individual Properties

    grid-column-start: 1;
    grid-column-end: 3;

    grid-row-start: 1;
    grid-row-end: 3;

---

## 📦 Span

    grid-column: span 2;

Spans two columns.

    grid-row: span 2;

Spans two rows.

---

## 🧩 `grid-area`

Syntax:

    grid-area: row-start / column-start / row-end / column-end;

Example:

    grid-area: 1 / 1 / 3 / 3;

---

## 🏷️ Named Areas

    grid-template-areas:
        "header header"
        "sidebar main"
        "footer footer";

Then:

    .header {
        grid-area: header;
    }

---

## 📐 `minmax()`

    minmax(200px, 1fr)

Minimum:

    200px

Maximum:

    1fr

---

## 📱 Responsive Grid

    grid-template-columns:
        repeat(auto-fit, minmax(220px, 1fr));

---

## 🔄 Auto Fit vs Auto Fill

    auto-fit  → Empty tracks collapse
    auto-fill → Empty fitting tracks can remain

---

## 🎯 Item Alignment

    justify-items: center;
    align-items: center;

Shorthand:

    place-items: center;

---

## 📦 Grid Alignment

    justify-content
    align-content

These control the Grid tracks as a whole.

---

## 🧠 Remember

    justify-items   → Items horizontally
    align-items     → Items vertically
    place-items     → Both

    justify-content → Grid horizontally
    align-content   → Grid vertically

---

## ⭐ Useful Patterns

Featured item:

    grid-column: span 2;

Tall item:

    grid-row: span 2;

Responsive cards:

    repeat(auto-fit, minmax(220px, 1fr))

Named layout:

    grid-template-areas:
        "header header"
        "sidebar main"
        "footer footer"

---

## 📌 Core Formula

**row-start / column-start / row-end / column-end**

for:

    grid-area