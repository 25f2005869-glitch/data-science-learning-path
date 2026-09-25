# ⚡ Day 091 — Responsive UI Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 091  
**Topic:** Responsive UI  

---

## 🔹 Viewport

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

---

## 🔹 Responsive Container

    .container {
        width: 92%;
        max-width: 1200px;
        margin: 0 auto;
    }

---

## 🔹 Responsive Image

    img {
        max-width: 100%;
        height: auto;
    }

---

## 🔹 Flexbox

    .layout {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }

---

## 🔹 Responsive Grid

    .cards {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
    }

---

## 🔹 Mobile-First

    Mobile
      ↓
    Tablet
      ↓
    Desktop

---

## 🔹 Media Query

    @media (max-width: 700px) {
        .layout {
            grid-template-columns: 1fr;
        }
    }

---

## 🔹 Desktop Enhancement

    @media (min-width: 768px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

---

## 🔹 Responsive Form

    .form {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }

    @media (max-width: 700px) {
        .form {
            grid-template-columns: 1fr;
        }
    }

---

## 🔹 Responsive Table

    .table-container {
        overflow-x: auto;
    }

---

## 🔹 Sidebar

    Desktop:
    Sidebar | Main

    Mobile:
    Main

---

## 🔹 Responsive Units

    %
    rem
    em
    vw
    vh
    fr

---

## 🔹 Avoid

    width: 1200px;

Prefer:

    width: 100%;
    max-width: 1200px;

---

## 🔹 Touch Controls

    button {
        padding: 12px 16px;
    }

---

## 🔹 Accessibility

    ✓ Semantic HTML
    ✓ Labels
    ✓ Keyboard navigation
    ✓ Visible focus
    ✓ Readable text
    ✓ Good contrast
    ✓ No hover-only functionality

---

## 🔹 Reduced Motion

    @media (prefers-reduced-motion: reduce) {
        * {
            animation: none;
            transition: none;
        }
    }

---

## 🔹 Responsive Testing

    Mobile
    Tablet
    Laptop
    Desktop

Check:

    Navigation
    Cards
    Forms
    Tables
    Images
    Buttons
    Search
    CRUD

---

## 🔹 Golden Rule

    Flexible Layout
          +
    Media Queries
          +
    Accessible Controls
          =
    Responsive UI