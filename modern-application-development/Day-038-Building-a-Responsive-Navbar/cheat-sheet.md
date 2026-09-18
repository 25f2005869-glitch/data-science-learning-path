# ⚡ Day 038 — Responsive Navbar Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 038  
**Topic:** Building a Responsive Navbar

---

## 🧭 Basic Structure

    <nav aria-label="Main navigation">
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
        </ul>
    </nav>

---

## 🧹 Remove List Defaults

    list-style: none;
    margin: 0;
    padding: 0;

---

## 📱 Mobile Navbar

    .nav-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

---

## 🖥️ Desktop Navbar

    @media (min-width: 700px) {
        .nav-list {
            flex-direction: row;
        }
    }

---

## ↔️ Horizontal Alignment

    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;

---

## 🔄 Wrapping

    flex-wrap: wrap;

Useful when links need to move onto another line.

---

## 🏷️ Link Styling

    .nav-link {
        text-decoration: none;
        padding: 8px 12px;
    }

---

## 🖱️ Hover

    .nav-link:hover {
        text-decoration: underline;
    }

---

## ⌨️ Focus

    .nav-link:focus-visible {
        outline: 2px solid currentColor;
        outline-offset: 3px;
    }

---

## 📌 Sticky Navbar

    position: sticky;
    top: 0;
    z-index: 100;

---

## 📐 Responsive Container

    width: 90%;
    max-width: 1100px;
    margin: auto;

---

## 🏷️ Accessible Navigation

    <nav aria-label="Main navigation">

Use meaningful link text.

---

## 📱 Mobile-First Pattern

    .nav-list {
        display: flex;
        flex-direction: column;
    }

    @media (min-width: 700px) {
        .nav-list {
            flex-direction: row;
        }
    }

---

## 🧠 Remember

    <nav>       → Navigation landmark
    <ul>        → List of links
    <li>        → Navigation item
    <a>         → Navigation link
    Flexbox     → Navbar layout
    @media      → Responsive behavior

**Responsive Navbar = Semantic HTML + Flexbox + Media Queries + Accessibility**