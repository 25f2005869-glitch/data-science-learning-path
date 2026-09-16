# 📘 Day 028 — CSS Position and Z-Index — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 028  
**Topic:** CSS Position and Z-Index

---

## 1. Introduction

CSS positioning allows you to control the location of elements on a webpage.

The `position` property determines how an element is placed in relation to:

- The normal document flow
- Its normal position
- A containing block
- The viewport

The `z-index` property controls the stacking order of overlapping elements.

These concepts are useful for:

- Navigation bars
- Sticky headers
- Floating buttons
- Badges
- Tooltips
- Overlays
- Dropdowns
- Modals
- Cards with positioned elements

---

# 2. The CSS Position Property

The `position` property defines the positioning method used for an element.

Common values are:

    position: static;
    position: relative;
    position: absolute;
    position: fixed;
    position: sticky;

Each value behaves differently.

---

# 3. Position Static

`static` is the default positioning behavior for elements.

Example:

    .box {
        position: static;
    }

A static element follows the normal document flow.

The offset properties do not reposition a statically positioned element:

    top
    right
    bottom
    left

For example:

    .box {
        position: static;
        top: 20px;
    }

The `top` value does not move the element because its position is static.

---

# 4. Normal Document Flow

Before understanding positioning, it is important to understand normal document flow.

In normal flow, the browser places elements according to their normal layout rules.

For example:

    <div>Box 1</div>
    <div>Box 2</div>
    <div>Box 3</div>

Block elements normally appear one after another.

CSS positioning can change how an element participates in this flow.

---

# 5. Position Relative

`position: relative` keeps the element in the normal document flow.

Example:

    .box {
        position: relative;
        top: 20px;
        left: 30px;
    }

The element is visually moved from its normal position.

However, its original layout space is preserved.

This is an important difference between relative and absolute positioning.

---

# 6. Relative Positioning and Offsets

Relative positioning can use:

    top
    right
    bottom
    left

Example:

    .box {
        position: relative;
        top: 10px;
        left: 20px;
    }

The element is shifted from its normal position.

The original position still participates in the layout.

---

# 7. Position Absolute

`position: absolute` removes the element from normal document flow.

Example:

    .box {
        position: absolute;
        top: 20px;
        right: 20px;
    }

The element is positioned relative to its containing block.

Because the element is removed from normal flow, other elements can occupy the space it would otherwise have used.

---

# 8. Containing Block

A containing block is the reference area used for positioning an element.

For an absolutely positioned element, the containing block is generally established by the appropriate positioned ancestor.

A common pattern is:

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
        top: 10px;
        right: 10px;
    }

Here, `.child` is positioned relative to `.parent`.

---

# 9. Parent Relative + Child Absolute

This is one of the most important practical positioning patterns.

HTML:

    <div class="card">
        <span class="badge">New</span>
        <h2>Student Card</h2>
    </div>

CSS:

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

The parent establishes a positioning context.

The badge can then be placed at the top-right corner of the card.

---

# 10. Position Fixed

`position: fixed` positions an element relative to the viewport in typical browser layouts.

Example:

    .button {
        position: fixed;
        right: 20px;
        bottom: 20px;
    }

The element generally remains in that viewport position while the page is scrolled.

Common uses include:

- Floating action buttons
- Help buttons
- Back-to-top buttons
- Fixed navigation elements

---

# 11. Fixed Position and Document Flow

A fixed element is removed from the normal document flow.

Example:

    .help-button {
        position: fixed;
        right: 20px;
        bottom: 20px;
    }

The surrounding content does not reserve normal layout space for the fixed element.

Therefore, fixed elements may overlap other content if the layout is not designed carefully.

---

# 12. Position Sticky

`position: sticky` combines aspects of relative positioning with sticky behavior during scrolling.

Example:

    header {
        position: sticky;
        top: 0;
    }

The element participates in normal flow and can become attached to the specified edge when the scrolling threshold is reached.

Sticky behavior depends on the relevant scrolling container and surrounding layout.

---

# 13. Sticky Header

A common example:

    header {
        position: sticky;
        top: 0;
        z-index: 10;
    }

The header can remain visible near the top while scrolling.

The `z-index` is often used so the sticky header appears above other content.

---

# 14. Top, Right, Bottom and Left

The following properties specify offsets for positioned elements:

    top
    right
    bottom
    left

Example:

    .box {
        position: absolute;
        top: 20px;
        right: 30px;
    }

The exact reference depends on the element's positioning method and containing block.

---

# 15. Top

`top` specifies an offset from the relevant top edge.

Example:

    position: relative;
    top: 20px;

For relative positioning, this visually shifts the element downward by 20px.

---

# 16. Right

`right` specifies an offset from the relevant right edge.

Example:

    position: absolute;
    right: 20px;

This can place an absolutely positioned element 20px from the right side of its containing block.

---

# 17. Bottom

`bottom` specifies an offset from the relevant bottom edge.

Example:

    position: fixed;
    bottom: 20px;

This can place an element 20px above the bottom edge of the viewport.

---

# 18. Left

`left` specifies an offset from the relevant left edge.

Example:

    position: absolute;
    left: 20px;

This can place an absolutely positioned element 20px from the left side of its containing block.

---

# 19. Position Types Comparison

| Position | Normal Flow | Reference |
|---|---|---|
| `static` | Yes | Normal layout |
| `relative` | Yes | Its normal position |
| `absolute` | No | Containing block |
| `fixed` | No | Viewport in typical cases |
| `sticky` | Yes | Scroll position and containing/scrolling context |

---

# 20. Relative vs Absolute

### Relative

    position: relative;

- Remains in normal flow.
- Original layout space is preserved.
- Can be visually offset.
- Can establish a positioning context for descendants.

### Absolute

    position: absolute;

- Removed from normal flow.
- Positioned relative to its containing block.
- Useful for overlays and badges.
- Often used inside a relative parent.

---

# 21. Fixed vs Sticky

### Fixed

    position: fixed;

The element is positioned relative to the viewport and generally stays in that location during scrolling.

### Sticky

    position: sticky;

The element participates in normal flow and becomes sticky when its threshold is reached within its scrolling context.

---

# 22. Centering an Absolute Element

A common technique for centering an absolutely positioned element is:

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

Explanation:

- `top: 50%` moves the child's top edge to the middle.
- `left: 50%` moves the child's left edge to the middle.
- `transform: translate(-50%, -50%)` shifts the child back by half of its own dimensions.

---

# 23. CSS Z-Index

`z-index` controls the stacking order of elements when they overlap.

Example:

    .box {
        position: relative;
        z-index: 2;
    }

A larger stacking level generally places an element above another overlapping element when they are being compared within the same stacking context.

---

# 24. Z-Index Values

Examples:

    z-index: 1;
    z-index: 2;
    z-index: 10;

Negative values are also possible:

    z-index: -1;

The visual result depends on stacking contexts and the surrounding layout.

---

# 25. Understanding Stacking Order

Think of overlapping elements as layers.

Example:

    .bottom {
        z-index: 1;
    }

    .middle {
        z-index: 2;
    }

    .top {
        z-index: 3;
    }

Conceptually:

    3 → Top Layer
    2 → Middle Layer
    1 → Bottom Layer

---

# 26. Z-Index and Positioning

A common example is:

    .box-one {
        position: absolute;
        z-index: 1;
    }

    .box-two {
        position: absolute;
        z-index: 2;
    }

If the elements overlap and belong to the same relevant stacking context, `.box-two` generally appears above `.box-one`.

---

# 27. Stacking Context

A stacking context is an independent layering context used by the browser when painting elements.

`z-index` values are not always compared globally across the entire page.

Certain CSS properties and combinations can create stacking contexts.

Therefore, a child with:

    z-index: 9999;

does not automatically appear above every element on the page.

The stacking contexts containing the elements also matter.

---

# 28. Z-Index with Sticky Headers

A sticky header can overlap page content.

Example:

    header {
        position: sticky;
        top: 0;
        z-index: 10;
    }

The `z-index` helps keep the header above other overlapping content within the applicable stacking context.

---

# 29. Practical Badge Example

HTML:

    <div class="card">
        <span class="badge">New</span>
        <h2>CSS Course</h2>
    </div>

CSS:

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 2;
    }

This creates a badge positioned inside the card.

---

# 30. Practical Floating Button

Example:

    .floating-button {
        position: fixed;
        right: 20px;
        bottom: 20px;
        z-index: 100;
    }

This is useful for a floating action or support button.

---

# 31. Practical Sticky Navigation

Example:

    nav {
        position: sticky;
        top: 0;
        z-index: 20;
    }

The navigation can remain visible near the top while scrolling.

---

# 32. Negative Z-Index

Negative values can place an element behind other content within the relevant stacking context.

Example:

    .background {
        position: absolute;
        z-index: -1;
    }

Negative `z-index` should be used carefully because stacking contexts and parent backgrounds can affect the final result.

---

# 33. Positioning with Percentages

Offsets can use percentages.

Example:

    .box {
        position: absolute;
        left: 50%;
    }

For an absolutely positioned element, percentage offsets are generally calculated relative to the corresponding dimension of its containing block.

Percentages are useful for creating flexible layouts.

---

# 34. Positioning with `transform`

Transforms are often combined with positioning.

Example:

    .box {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

This is a common method for centering an absolutely positioned element.

---

# 35. Positioning and Responsive Design

Positioning should be used carefully in responsive layouts.

Avoid excessive hard-coded coordinates such as:

    top: 350px;
    left: 500px;

Such values can cause problems when the viewport changes.

Prefer flexible layouts and use positioning when it solves a specific layout requirement.

---

# 36. Common Mistake — Absolute Without the Correct Parent

Suppose you have:

    .card {
        /* no positioning context */
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

The badge may be positioned relative to a different containing block than expected.

A common solution is:

    .card {
        position: relative;
    }

---

# 37. Common Mistake — Using Fixed Everywhere

Fixed positioning removes the element from normal flow.

Using it excessively can cause:

- Overlapping content
- Poor mobile layouts
- Difficult scrolling behavior
- Accessibility problems

Use fixed positioning only when the element genuinely needs viewport-based positioning.

---

# 38. Common Mistake — Excessive Z-Index

Avoid automatically using very large values:

    z-index: 999999;

Large numbers do not solve stacking-context problems.

A simple layering system is easier to understand and maintain.

For example:

    z-index: 1;
    z-index: 10;
    z-index: 20;
    z-index: 100;

---

# 39. Common Mistake — Sticky Not Working

Possible reasons include:

- Missing offset such as `top: 0`.
- The relevant scrolling container is different from what you expected.
- An ancestor's overflow or layout affects sticky behavior.
- There is insufficient scrolling space.
- The surrounding layout prevents the expected sticky behavior.

---

# 40. Positioning Best Practices

- Understand normal document flow before using positioning.
- Use `relative` for small visual offsets.
- Use `relative` on a parent when it should establish a positioning context.
- Use `absolute` for overlays, badges, and precisely positioned children.
- Use `fixed` for viewport-based floating components.
- Use `sticky` for elements that should stick during scrolling.
- Use `z-index` only when layering is required.
- Keep z-index values organized.
- Test positioned layouts at different screen sizes.
- Avoid excessive hard-coded coordinates.

---

# 41. Quick Mental Model

    static
    → Normal positioning

    relative
    → Stay in flow + move visually

    absolute
    → Remove from flow + position within containing block

    fixed
    → Remove from flow + position relative to viewport

    sticky
    → Stay in flow + stick during scrolling

    z-index
    → Control stacking order

---

# 42. Practical Layout Pattern

A common card structure is:

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

    .floating-button {
        position: fixed;
        right: 20px;
        bottom: 20px;
    }

    .navigation {
        position: sticky;
        top: 0;
        z-index: 10;
    }

This combines several important positioning concepts.

---

# 43. Revision Table

| Concept | Key Point |
|---|---|
| `static` | Default positioning |
| `relative` | Remains in flow and can be offset |
| `absolute` | Removed from flow and positioned relative to containing block |
| `fixed` | Positioned relative to viewport in typical cases |
| `sticky` | Sticks after reaching a scrolling threshold |
| `top` | Top offset |
| `right` | Right offset |
| `bottom` | Bottom offset |
| `left` | Left offset |
| `z-index` | Controls stacking order |

---

# 44. Key Takeaway

CSS positioning allows you to control **where elements appear**, while `z-index` helps control **which overlapping element appears on top**.

The most important pattern to remember is:

    Parent:
        position: relative;

    Child:
        position: absolute;

This pattern is widely used for badges, icons, overlays, labels, and other positioned components.

---

## 🔗 Navigation

Previous: Day 027 — CSS Width, Height and Display

Current: Day 028 — CSS Position and Z-Index

Next: Day 029 — CSS Flexbox

---

**Happy Learning! 🚀**