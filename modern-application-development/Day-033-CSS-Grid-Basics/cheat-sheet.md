# ⚡ Day 033 — CSS Grid Basics Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 033  
**Topic:** CSS Grid Basics

---

## 🧩 Start Grid

    .container {
        display: grid;
    }

Direct children become grid items.

---

## 📊 Columns

    grid-template-columns: 1fr 1fr;

Two equal columns.

    grid-template-columns: repeat(3, 1fr);

Three equal columns.

---

## 📏 Rows

    grid-template-rows: 100px 200px;

Two explicit rows.

---

## ⭐ `fr`

`fr` = fraction of available grid space.

    1fr 1fr

Equal distribution.

    1fr 2fr

1:2 flexible distribution.

---

## 🔁 `repeat()`

Instead of:

    1fr 1fr 1fr 1fr

Use:

    repeat(4, 1fr)

---

## ↔️ Gap

    gap: 20px;

Or:

    row-gap: 20px;
    column-gap: 30px;

---

## 📐 Mixed Columns

    grid-template-columns: 200px 1fr 2fr;

Fixed + flexible tracks.

---

## 📱 Responsive Grid

    grid-template-columns:
        repeat(auto-fit, minmax(200px, 1fr));

Useful for responsive cards.

---

## 📦 Important Terms

    Grid Container → Parent
    Grid Item      → Direct child
    Grid Line      → Boundary line
    Grid Track     → Row or column
    Grid Cell      → Single grid unit
    Grid Area      → One or more cells

---

## 🔄 Grid vs Flexbox

    Flexbox → One dimension
    Grid    → Two dimensions

---

## 🎯 Common Card Pattern

    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }

---

## ⭐ Remember

**CSS Grid = Rows + Columns**

Start with:

    display: grid
    grid-template-columns
    grid-template-rows
    gap
    fr
    repeat()