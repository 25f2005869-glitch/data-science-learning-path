# 📚 Day 031 — CSS Flexbox Basics Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 031  
**Topic:** CSS Flexbox Basics

---

## 1. What is Flexbox?

Flexbox is a CSS layout system designed to arrange elements in one dimension.

One dimension means:

- Row
- Column

Flexbox makes alignment and spacing easier than traditional layout techniques.

---

## 2. Flex Container

An element becomes a flex container when:

    display: flex;

Example:

    .container {
        display: flex;
    }

The direct children of this element become flex items.

---

## 3. Flex Items

The direct children of a flex container are called flex items.

Example:

    <div class="container">
        <div>Item 1</div>
        <div>Item 2</div>
        <div>Item 3</div>
    </div>

Here:

- `.container` → Flex container
- Item 1 → Flex item
- Item 2 → Flex item
- Item 3 → Flex item

---

## 4. Main Axis

The main axis is the primary direction in which flex items are arranged.

With:

    flex-direction: row;

The main axis is horizontal.

With:

    flex-direction: column;

The main axis is vertical.

---

## 5. Cross Axis

The cross axis is perpendicular to the main axis.

For a row layout:

    Main axis   → Horizontal
    Cross axis  → Vertical

For a column layout:

    Main axis   → Vertical
    Cross axis  → Horizontal

Understanding these two axes is very important for Flexbox.

---

## 6. `flex-direction`

`flex-direction` controls the direction of flex items.

### Row

    flex-direction: row;

Items are arranged from left to right.

### Row Reverse

    flex-direction: row-reverse;

Items are arranged from right to left.

### Column

    flex-direction: column;

Items are arranged from top to bottom.

### Column Reverse

    flex-direction: column-reverse;

Items are arranged from bottom to top.

---

## 7. `justify-content`

`justify-content` controls how items are distributed along the main axis.

Common values:

    flex-start
    flex-end
    center
    space-between
    space-around
    space-evenly

Example:

    .container {
        display: flex;
        justify-content: center;
    }

The items are placed in the center of the main axis.

---

## 8. `align-items`

`align-items` controls alignment along the cross axis.

Common values:

    stretch
    flex-start
    flex-end
    center
    baseline

Example:

    .container {
        display: flex;
        align-items: center;
    }

Items are centered on the cross axis.

---

## 9. `flex-wrap`

By default, flex items try to remain on one line.

Use:

    flex-wrap: wrap;

to allow items to move to another line when there is not enough space.

Other values:

    nowrap
    wrap
    wrap-reverse

---

## 10. `flex-flow`

`flex-flow` is shorthand for:

    flex-direction
    flex-wrap

Example:

    flex-flow: row wrap;

This means:

- Direction → row
- Wrapping → enabled

---

## 11. `gap`

`gap` creates space between flex items.

Example:

    .container {
        display: flex;
        gap: 20px;
    }

You can also use:

    row-gap: 20px;
    column-gap: 30px;

---

## 12. `align-content`

`align-content` controls the spacing between multiple flex lines when wrapping is enabled.

Common values:

    flex-start
    flex-end
    center
    space-between
    space-around
    space-evenly
    stretch

It is mainly useful when there are multiple rows or columns of flex items.

---

## 13. `justify-content` vs `align-items`

This is one of the most important Flexbox concepts.

For:

    flex-direction: row;

Usually:

    justify-content → main axis → horizontal
    align-items     → cross axis → vertical

For:

    flex-direction: column;

Usually:

    justify-content → main axis → vertical
    align-items     → cross axis → horizontal

Always think in terms of axes rather than simply memorizing horizontal and vertical.

---

## 14. Centering with Flexbox

A common pattern for centering an item:

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

This centers items along both axes.

---

## 15. Flexbox Navigation

Flexbox is commonly used for navigation menus.

Example:

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
    }

---

## 16. Flexbox Cards

Cards can be arranged using:

    .cards {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }

This allows cards to move to another line when required.

---

## 17. Responsive Flexbox

A responsive layout can combine Flexbox with percentages and `max-width`.

Example:

    .cards {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }

    .card {
        width: 30%;
        min-width: 200px;
    }

This allows the layout to adapt to different screen sizes.

---

## 18. Flexbox vs Normal Flow

Normal document flow places elements according to their default block and inline behavior.

Flexbox gives explicit control over:

- Direction
- Alignment
- Spacing
- Wrapping
- Distribution

---

## 19. Common Mistakes

### Mistake 1

Using `align-items` when you actually need main-axis alignment.

Remember:

    justify-content → main axis
    align-items → cross axis

### Mistake 2

Forgetting `display: flex`.

Flexbox properties do not work as expected unless the parent is a flex container.

### Mistake 3

Confusing `align-content` with `align-items`.

`align-items` works with items on the cross axis.

`align-content` controls multiple flex lines.

### Mistake 4

Forgetting wrapping.

If items should move to another line, use:

    flex-wrap: wrap;

---

## 20. Flexbox Mental Model

Think of Flexbox as:

    Flex Container
          |
          +---- Flex Item
          +---- Flex Item
          +---- Flex Item

Then ask:

1. What is the direction?
2. What is the main axis?
3. What is the cross axis?
4. How should items be distributed?
5. Should items wrap?
6. How much gap is required?

---

## 📌 Key Takeaway

Flexbox is mainly used for arranging and aligning elements in one dimension.

Remember:

    display: flex
    flex-direction
    justify-content
    align-items
    flex-wrap
    gap

The most important concept is understanding the **main axis and cross axis**.