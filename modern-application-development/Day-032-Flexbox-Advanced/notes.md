# 📚 Day 032 — CSS Flexbox Advanced Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 032  
**Topic:** CSS Flexbox Advanced

---

## 1. Flexbox Container vs Flex Item Properties

Flexbox properties are divided into two major groups.

### Container Properties

These are applied to the parent:

    display
    flex-direction
    flex-wrap
    flex-flow
    justify-content
    align-items
    align-content
    gap

### Item Properties

These are applied to the children:

    flex-grow
    flex-shrink
    flex-basis
    flex
    order
    align-self

---

## 2. `flex-grow`

`flex-grow` controls how a flex item receives available extra space.

Example:

    .item {
        flex-grow: 1;
    }

If multiple items have:

    flex-grow: 1;

they can share available extra space.

Example:

    .item-one {
        flex-grow: 1;
    }

    .item-two {
        flex-grow: 2;
    }

The second item receives twice the growth share of the first item, assuming the other sizing conditions are equivalent.

---

## 3. `flex-shrink`

`flex-shrink` controls how an item can shrink when there is not enough space.

Example:

    .item {
        flex-shrink: 1;
    }

The default value is:

    1

An item with:

    flex-shrink: 0;

does not shrink because of the flex shrinking algorithm.

---

## 4. `flex-basis`

`flex-basis` defines the initial main-size of a flex item before remaining space is distributed.

Example:

    .item {
        flex-basis: 200px;
    }

For a row layout, this generally relates to the item's initial width.

For a column layout, it generally relates to the item's initial height.

---

## 5. `flex` Shorthand

The `flex` property is a shorthand for:

    flex-grow
    flex-shrink
    flex-basis

Example:

    flex: 1 1 200px;

This means:

    grow  = 1
    shrink = 1
    basis = 200px

---

## 6. Understanding `flex: 1`

A very common pattern is:

    flex: 1;

It is useful when multiple flex items should share available space.

For example:

    .card {
        flex: 1;
    }

Multiple cards can expand to use available space.

---

## 7. `order`

The `order` property changes the visual order of flex items.

Example:

    .item-one {
        order: 2;
    }

    .item-two {
        order: 1;
    }

Item two appears before item one visually.

The default value is:

    0

Items with lower order values appear earlier.

Important:

`order` changes visual presentation. It does not change the underlying HTML/DOM order.

For accessibility, HTML should still be arranged in a meaningful logical order.

---

## 8. `align-self`

`align-self` overrides the parent's `align-items` value for an individual flex item.

Example:

    .container {
        display: flex;
        align-items: center;
    }

    .special-item {
        align-self: flex-start;
    }

The special item is aligned differently from the other items.

Common values:

    auto
    flex-start
    flex-end
    center
    baseline
    stretch

---

## 9. `align-self` vs `align-items`

`align-items` controls all flex items.

    .container {
        align-items: center;
    }

`align-self` controls one particular flex item.

    .item {
        align-self: flex-end;
    }

---

## 10. Free Space

Flexbox distributes available space according to the flex properties.

Consider a container with extra space.

If items have:

    flex-grow: 1;

they can grow to consume available space.

If the container is too small:

    flex-shrink: 1;

allows items to shrink.

---

## 11. Growth Example

Suppose three items have:

    flex-grow: 1;

They can share available extra space equally.

If:

    Item A → 1
    Item B → 2
    Item C → 1

the growth proportions are:

    1 : 2 : 1

Item B gets twice the growth share of A or C, assuming comparable conditions.

---

## 12. Shrinking Example

Suppose the container cannot fit all flex items at their initial sizes.

With:

    flex-shrink: 1;

items are allowed to shrink.

With:

    flex-shrink: 0;

the item is prevented from shrinking by the flex-shrink factor.

---

## 13. `flex-basis` vs `width`

For a row flex container, `flex-basis` generally controls the initial main size.

Example:

    .item {
        flex-basis: 250px;
    }

This is different from simply treating `width` as the final size because Flexbox can subsequently distribute or remove space.

Think of `flex-basis` as the starting point for the flex sizing algorithm.

---

## 14. Responsive Cards

A common responsive pattern is:

    .cards {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }

    .card {
        flex: 1 1 250px;
    }

This means the card can:

- Grow
- Shrink
- Start with a basis of approximately 250px

This is useful for responsive layouts.

---

## 15. Navigation Layout

A navigation container can use:

    display: flex;
    justify-content: space-between;
    align-items: center;

Individual elements can then receive different flex values.

Example:

    .logo {
        flex: 1;
    }

    .menu {
        flex: 2;
    }

---

## 16. Common Flexbox Pattern

A flexible layout:

    .container {
        display: flex;
        gap: 20px;
    }

    .item {
        flex: 1 1 200px;
    }

This is one of the most useful Flexbox patterns for responsive cards.

---

## 17. Common Mistakes

### Mistake 1: Confusing `flex-grow` with width

`flex-grow` controls distribution of available extra space. It is not simply another form of `width`.

### Mistake 2: Forgetting the flex container

Item properties require the element to participate as a flex item.

### Mistake 3: Misusing `order`

Do not use `order` to create a completely different reading sequence if the HTML order is logically important.

### Mistake 4: Confusing `align-items` and `align-self`

    align-items → Parent controls all items
    align-self  → Individual item overrides alignment

### Mistake 5: Using fixed widths everywhere

Responsive layouts usually benefit from flexible sizing.

---

## 18. Flexbox Item Property Summary

    flex-grow
        Controls growth.

    flex-shrink
        Controls shrinking.

    flex-basis
        Defines initial main size.

    flex
        Shorthand for grow, shrink and basis.

    order
        Changes visual order.

    align-self
        Changes cross-axis alignment of one item.

---

## 19. Practical Card Formula

For a flexible card layout:

    .card {
        flex: 1 1 250px;
    }

Interpretation:

    1 → Can grow
    1 → Can shrink
    250px → Initial basis

Combined with:

    flex-wrap: wrap;

this can produce a responsive card layout.

---

## 20. Key Mental Model

For Flexbox items, remember:

**Grow → Shrink → Basis → Flex → Order → Align Self**

And always remember:

    Container → controls the layout
    Item → controls its individual behavior

---

## 📌 Key Takeaway

Advanced Flexbox gives you control over how individual items behave inside a flexible container.

The most important properties are:

    flex-grow
    flex-shrink
    flex-basis
    flex
    order
    align-self

The pattern:

    flex: 1 1 250px;

is especially useful for responsive card layouts.