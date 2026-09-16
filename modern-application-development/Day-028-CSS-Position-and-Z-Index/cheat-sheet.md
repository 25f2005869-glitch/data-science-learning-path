# 📌 Day 028 — CSS Position and Z-Index — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 028  
**Topic:** CSS Position and Z-Index

---

## 📍 1. Position Property

    position: static;
    position: relative;
    position: absolute;
    position: fixed;
    position: sticky;

---

## 🟦 2. Static

    position: static;

- Default positioning.
- Follows normal document flow.
- `top`, `right`, `bottom`, and `left` do not reposition it.

---

## 🟩 3. Relative

    position: relative;

- Remains in normal document flow.
- Original layout space is preserved.
- Can be moved using offsets.
- Can establish a positioning context for an absolutely positioned child.

Example:

    .box {
        position: relative;
        top: 20px;
        left: 10px;
    }

---

## 🟨 4. Absolute

    position: absolute;

- Removed from normal document flow.
- Positioned relative to its containing block.
- Commonly used for badges, overlays, icons, and positioned children.

Common pattern:

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
        top: 10px;
        right: 10px;
    }

---

## 🟧 5. Fixed

    position: fixed;

- Removed from normal document flow.
- Positioned relative to the viewport in typical browser layouts.
- Generally remains in position while scrolling.

Example:

    .button {
        position: fixed;
        right: 20px;
        bottom: 20px;
    }

---

## 🟪 6. Sticky

    position: sticky;
    top: 0;

- Participates in normal flow.
- Becomes sticky when its scroll threshold is reached.
- Behavior depends on the relevant scrolling container and surrounding layout.

Common use:

    header {
        position: sticky;
        top: 0;
    }

---

## 📐 7. Offset Properties

    top: 20px;
    right: 20px;
    bottom: 20px;
    left: 20px;

Used with positioned elements.

---

## ⚖️ 8. Position Comparison

| Position | In Normal Flow? | Main Reference |
|---|---|---|
| `static` | Yes | Normal layout |
| `relative` | Yes | Normal position |
| `absolute` | No | Containing block |
| `fixed` | No | Viewport in typical cases |
| `sticky` | Yes | Scroll position / scrolling context |

---

## 📦 9. Parent + Child Pattern

Most important pattern:

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

Think:

    Parent → relative
    Child → absolute

---

## 🎯 10. Center Absolute Element

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

---

## 🥞 11. Z-Index

Controls the stacking order of overlapping elements.

    z-index: 1;
    z-index: 2;
    z-index: 10;

Generally, a higher stacking level places an element above a lower one when they are compared within the same stacking context.

---

## 🔢 12. Z-Index Example

    .box1 {
        position: absolute;
        z-index: 1;
    }

    .box2 {
        position: absolute;
        z-index: 2;
    }

`box2` generally appears above `box1` when they overlap in the same stacking context.

---

## 🔻 13. Negative Z-Index

Negative values are possible:

    z-index: -1;

Use carefully because stacking contexts and parent backgrounds can affect the result.

---

## 🧱 14. Stacking Context

A stacking context is an independent layering context.

Important:

    z-index: 9999;

does not automatically place an element above everything on the page.

The stacking context containing the element also matters.

---

## 📌 15. Sticky Header

    header {
        position: sticky;
        top: 0;
        z-index: 10;
    }

Useful for navigation and headers that should remain visible while scrolling.

---

## 🔘 16. Floating Button

    .floating-button {
        position: fixed;
        right: 20px;
        bottom: 20px;
        z-index: 100;
    }

---

## 🏷️ 17. Badge

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

---

## 📊 18. Relative vs Absolute

| Feature | Relative | Absolute |
|---|---|---|
| Normal flow | Yes | No |
| Original space preserved | Yes | No |
| Uses offsets | Yes | Yes |
| Common use | Offset/context | Overlay/positioned child |

---

## 📊 19. Fixed vs Sticky

| Feature | Fixed | Sticky |
|---|---|---|
| Normal flow | No | Yes |
| Viewport-based | Typically yes | No |
| Scroll behavior | Stays fixed | Sticks after threshold |
| Common use | Floating buttons | Headers/navigation |

---

## ⚡ 20. Quick Reference

    static
    → Default

    relative
    → In flow + movable

    absolute
    → Out of flow + positioned in containing block

    fixed
    → Out of flow + viewport positioned

    sticky
    → In flow + sticks while scrolling

    z-index
    → Controls stacking order

---

## ⚠️ 21. Common Mistakes

- Using `absolute` for the entire page layout.
- Forgetting `position: relative` on the intended parent.
- Expecting `top` or `left` to move a static element.
- Using excessive `z-index` values.
- Using fixed positioning unnecessarily.
- Forgetting that stacking contexts affect `z-index`.
- Expecting sticky positioning to work without a suitable scroll context and offset.

---

## 🧠 22. Remember

    Relative
    → "Move me from where I normally am."

    Absolute
    → "Place me precisely inside my containing block."

    Fixed
    → "Keep me attached to the viewport."

    Sticky
    → "Let me scroll normally, then stick."

    Z-index
    → "Which layer should appear on top?"

---

## 🔗 Navigation

Previous: Day 027 — CSS Width, Height and Display

Current: Day 028 — CSS Position and Z-Index

Next: Day 029 — CSS Flexbox

---

**Happy Learning! 🚀**