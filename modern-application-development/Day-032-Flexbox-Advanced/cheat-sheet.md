# ⚡ Day 032 — CSS Flexbox Advanced Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 032  
**Topic:** CSS Flexbox Advanced

---

## 📦 Flex Item Properties

    flex-grow
    flex-shrink
    flex-basis
    flex
    order
    align-self

---

## 📈 `flex-grow`

Controls how an item receives extra space.

    flex-grow: 0;
    flex-grow: 1;
    flex-grow: 2;

Default:

    0

---

## 📉 `flex-shrink`

Controls shrinking when space is insufficient.

    flex-shrink: 0;
    flex-shrink: 1;
    flex-shrink: 2;

Default:

    1

---

## 📏 `flex-basis`

Initial main size:

    flex-basis: 200px;
    flex-basis: 30%;
    flex-basis: auto;

---

## 🔧 `flex` Shorthand

    flex: grow shrink basis;

Example:

    flex: 1 1 200px;

---

## ⭐ Common Pattern

    .card {
        flex: 1 1 250px;
    }

Meaning:

    Grow  → 1
    Shrink → 1
    Basis → 250px

---

## 🔢 `order`

Default:

    order: 0;

Example:

    .first {
        order: 1;
    }

    .second {
        order: 0;
    }

Lower order values appear first visually.

---

## 🎯 `align-self`

Controls one flex item on the cross axis.

    align-self: auto;
    align-self: flex-start;
    align-self: flex-end;
    align-self: center;
    align-self: baseline;
    align-self: stretch;

---

## 🔄 `align-items` vs `align-self`

    align-items → All items
    align-self  → One item

---

## 📱 Responsive Cards

    .cards {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }

    .card {
        flex: 1 1 250px;
    }

---

## 🧠 Important

    flex-grow   → Extra space
    flex-shrink → Less space
    flex-basis  → Starting main size
    flex        → Shorthand
    order       → Visual order
    align-self  → Individual cross-axis alignment

---

## ⭐ Remember

**Container controls layout.**

**Item controls individual behavior.**