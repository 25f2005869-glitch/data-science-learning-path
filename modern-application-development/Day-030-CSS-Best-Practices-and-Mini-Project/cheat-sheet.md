# ⚡ Day 030 — CSS Best Practices and Mini Project Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 030  
**Topic:** CSS Best Practices and Mini Project

---

## 🎯 Core Principles

| Practice | Recommendation |
|---|---|
| Naming | Use meaningful class names |
| Formatting | Keep indentation consistent |
| Reusability | Create reusable classes |
| Specificity | Keep selectors simple |
| `!important` | Avoid unless necessary |
| Units | Prefer suitable responsive units |
| CSS | Keep presentation separate from HTML |
| Accessibility | Maintain readability and focus |
| Responsive Design | Use flexible widths and media queries |
| Maintenance | Avoid unnecessary repetition |

---

## 🏷️ Good Class Names

    .student-card
    .profile-image
    .project-list
    .contact-form

Avoid:

    .box1
    .abc
    .red

---

## 📐 Useful Units

    px      → Fixed unit
    %       → Parent-relative
    em      → Current font-relative
    rem     → Root font-relative
    vw      → Viewport width
    vh      → Viewport height
    vmin    → Smaller viewport dimension
    vmax    → Larger viewport dimension

---

## 📦 Useful Box Model

    width
    padding
    border
    margin

Recommended:

    * {
        box-sizing: border-box;
    }

---

## 📱 Responsive CSS

    img {
        max-width: 100%;
        height: auto;
    }

    .container {
        width: 90%;
        max-width: 1000px;
        margin: auto;
    }

---

## 🎯 Specificity

Low → High:

    Element
    Class
    ID
    Inline style

Example:

    p { }
    .text { }
    #title { }

---

## 🚫 Avoid

    !important
    excessive IDs
    overly complex selectors
    repeated CSS
    unnecessary fixed widths
    inline styling everywhere

---

## ♻️ Reusable Pattern

    .card {
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 10px;
    }

---

## 🔍 Final Checklist

- Clean code
- Meaningful names
- Reusable styles
- Responsive layout
- Good contrast
- Simple selectors
- Proper units
- Minimal repetition
- Accessible interaction

---

## ⭐ Formula

**Good CSS = Clean + Reusable + Responsive + Accessible + Maintainable**