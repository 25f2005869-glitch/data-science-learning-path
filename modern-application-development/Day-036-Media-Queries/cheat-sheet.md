# ⚡ Day 036 — CSS Media Queries Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 036  
**Topic:** CSS Media Queries

---

## 📱 Basic Syntax

    @media (condition) {
        selector {
            property: value;
        }
    }

---

## ⬇️ `max-width`

Applies up to a maximum viewport width.

    @media (max-width: 600px) {
        ...
    }

---

## ⬆️ `min-width`

Applies from a minimum viewport width.

    @media (min-width: 700px) {
        ...
    }

---

## 📏 Height

    @media (min-height: 700px) {
        ...
    }

    @media (max-height: 500px) {
        ...
    }

---

## 🔄 Orientation

    @media (orientation: portrait) {
        ...
    }

    @media (orientation: landscape) {
        ...
    }

---

## 🖥️ Media Type

    @media screen {
        ...
    }

    @media print {
        ...
    }

---

## 🔗 Combine Conditions

    @media screen and (min-width: 700px) {
        ...
    }

---

## 📐 Width Range

    @media screen and
           (min-width: 700px) and
           (max-width: 1000px) {
        ...
    }

---

## 📱 Mobile First

    .cards {
        grid-template-columns: 1fr;
    }

    @media (min-width: 700px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (min-width: 1000px) {
        .cards {
            grid-template-columns: repeat(3, 1fr);
        }
    }

---

## 🖥️ Desktop First

    .cards {
        grid-template-columns: repeat(3, 1fr);
    }

    @media (max-width: 700px) {
        .cards {
            grid-template-columns: 1fr;
        }
    }

---

## 🧩 Responsive Flexbox

    .nav {
        display: flex;
        flex-direction: column;
    }

    @media (min-width: 700px) {
        .nav {
            flex-direction: row;
        }
    }

---

## 🧩 Responsive Grid

    .cards {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(220px, 1fr));
    }

---

## 🖨️ Print

    @media print {
        .navigation {
            display: none;
        }
    }

---

## 🚫 Avoid

    Too many breakpoints
    Device-specific assumptions
    Unnecessary Media Queries
    Fixed widths everywhere

---

## ⭐ Remember

    min-width → Start applying from this width
    max-width → Apply up to this width

**Use breakpoints based on content, not device names.**