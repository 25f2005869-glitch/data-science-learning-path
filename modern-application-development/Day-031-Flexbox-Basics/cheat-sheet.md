# ⚡ Day 031 — CSS Flexbox Basics Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 031  
**Topic:** CSS Flexbox Basics

---

## 📦 Start Flexbox

    .container {
        display: flex;
    }

Direct children become flex items.

---

## ↔️ Flex Direction

    flex-direction: row;
    flex-direction: row-reverse;
    flex-direction: column;
    flex-direction: column-reverse;

Default:

    row

---

## 🎯 Main Axis

    row     → Horizontal
    column  → Vertical

---

## ✚ Cross Axis

Cross axis is perpendicular to the main axis.

    row:
    main  → Horizontal
    cross → Vertical

    column:
    main  → Vertical
    cross → Horizontal

---

## 📍 Main Axis Alignment

    justify-content: flex-start;
    justify-content: flex-end;
    justify-content: center;
    justify-content: space-between;
    justify-content: space-around;
    justify-content: space-evenly;

---

## 📐 Cross Axis Alignment

    align-items: stretch;
    align-items: flex-start;
    align-items: flex-end;
    align-items: center;
    align-items: baseline;

---

## 🔄 Wrapping

    flex-wrap: nowrap;
    flex-wrap: wrap;
    flex-wrap: wrap-reverse;

---

## 🔧 Shorthand

    flex-flow: row wrap;

Equivalent to:

    flex-direction: row;
    flex-wrap: wrap;

---

## ↔️ Spacing

    gap: 20px;

Or:

    row-gap: 20px;
    column-gap: 30px;

---

## 📚 Multiple Flex Lines

    align-content: center;
    align-content: space-between;
    align-content: space-around;
    align-content: space-evenly;

---

## 🎯 Center an Item

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

---

## 🧠 Important Difference

    justify-content → Main axis
    align-items     → Cross axis
    align-content   → Multiple flex lines

---

## 📱 Responsive Pattern

    .cards {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }

---

## ⭐ Remember

**Flexbox = One-dimensional layout**

Always identify:

**Direction → Main Axis → Cross Axis → Alignment → Wrapping → Gap**