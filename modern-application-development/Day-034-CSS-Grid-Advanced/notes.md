# 📚 Day 034 — CSS Grid Advanced Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 034  
**Topic:** CSS Grid Advanced

---

## 1. Grid Lines

Grid lines are the boundaries that create rows and columns.

For example, a three-column Grid has four vertical grid lines.

    Line 1 | Column 1 | Line 2 | Column 2 | Line 3 | Column 3 | Line 4

Grid lines are used to position items.

---

## 2. Grid Tracks

A grid track is the space between two adjacent grid lines.

There are two types:

    Column track
    Row track

Example:

    grid-template-columns: repeat(3, 1fr);

This creates three column tracks.

---

## 3. `grid-column`

`grid-column` controls where an item starts and ends across columns.

Example:

    .item {
        grid-column: 1 / 3;
    }

The item starts at column line 1 and ends at column line 3.

Therefore, it occupies two column tracks.

---

## 4. `grid-row`

`grid-row` controls where an item starts and ends across rows.

Example:

    .item {
        grid-row: 1 / 3;
    }

The item occupies the space between row lines 1 and 3.

Therefore, it spans two row tracks.

---

## 5. `grid-column-start`

Defines the starting column line.

Example:

    grid-column-start: 2;

---

## 6. `grid-column-end`

Defines the ending column line.

Example:

    grid-column-end: 4;

Together:

    grid-column-start: 2;
    grid-column-end: 4;

This can also be written as:

    grid-column: 2 / 4;

---

## 7. `grid-row-start`

Defines the starting row line.

Example:

    grid-row-start: 1;

---

## 8. `grid-row-end`

Defines the ending row line.

Example:

    grid-row-end: 3;

Together:

    grid-row: 1 / 3;

---

## 9. `span`

The `span` keyword tells Grid how many tracks an item should occupy.

Example:

    grid-column: span 2;

The item spans two columns from its automatically determined starting position.

Another example:

    grid-row: span 2;

The item spans two rows.

---

## 10. Column Spanning

Consider:

    grid-template-columns: repeat(3, 1fr);

A normal item occupies one column.

To make an item occupy two columns:

    grid-column: span 2;

This is useful for featured cards and dashboard sections.

---

## 11. Row Spanning

Example:

    grid-row: span 2;

The item occupies two row tracks.

This is useful for layouts where one section needs to be taller than surrounding items.

---

## 12. `grid-area`

`grid-area` can specify an item's placement.

Example:

    .item {
        grid-area: 1 / 1 / 3 / 3;
    }

The four values represent:

    row-start
    column-start
    row-end
    column-end

So:

    grid-area: row-start / column-start / row-end / column-end;

---

## 13. Named Grid Areas

Grid can assign names to areas.

Example:

    .layout {
        display: grid;
        grid-template-areas:
            "header header"
            "sidebar main"
            "footer footer";
    }

Then items can use:

    .header {
        grid-area: header;
    }

    .sidebar {
        grid-area: sidebar;
    }

    .main {
        grid-area: main;
    }

    .footer {
        grid-area: footer;
    }

This is very useful for page layouts.

---

## 14. `minmax()`

`minmax()` defines a minimum and maximum size for a grid track.

Example:

    grid-template-columns:
        repeat(3, minmax(200px, 1fr));

This allows each column to be flexible while maintaining a minimum track size of 200px.

---

## 15. `auto-fit`

`auto-fit` allows Grid to fit as many columns as possible and collapse empty tracks.

Common pattern:

    grid-template-columns:
        repeat(auto-fit, minmax(200px, 1fr));

This is useful for responsive card layouts.

---

## 16. `auto-fill`

`auto-fill` creates as many tracks as can fit into the available space, while empty tracks may remain part of the grid.

Example:

    grid-template-columns:
        repeat(auto-fill, minmax(200px, 1fr));

---

## 17. `auto-fit` vs `auto-fill`

Both are commonly used with:

    repeat()
    minmax()

General idea:

    auto-fit  → Fit available items and collapse empty tracks
    auto-fill → Create as many fitting tracks as possible

For many card layouts, `auto-fit` is a convenient choice.

---

## 18. `justify-items`

Controls the horizontal alignment of grid items inside their grid areas.

Common values:

    start
    end
    center
    stretch

Example:

    justify-items: center;

---

## 19. `align-items`

Controls the vertical alignment of grid items inside their grid areas.

Example:

    align-items: center;

---

## 20. `place-items`

`place-items` is shorthand for:

    align-items
    justify-items

Example:

    place-items: center;

This centers items along both axes inside their grid areas.

---

## 21. `justify-content`

`justify-content` controls the Grid tracks as a whole when there is extra space in the grid container.

It is different from:

    justify-items

Remember:

    justify-content → Grid as a whole
    justify-items   → Items inside their cells

---

## 22. `align-content`

`align-content` controls the grid tracks as a whole along the block direction when there is extra space.

It is different from:

    align-items

Remember:

    align-content → Grid as a whole
    align-items    → Items inside their cells

---

## 23. Advanced Responsive Grid

A very useful pattern is:

    .cards {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
    }

This allows the number of columns to adapt to the available width.

---

## 24. Dashboard Layout

Grid is particularly useful for dashboards.

Example:

    .dashboard {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
    }

A featured item can span columns:

    .featured {
        grid-column: span 2;
    }

---

## 25. Header-Sidebar-Main-Footer Layout

Named Grid areas make page layouts easy to understand.

Conceptually:

    "header header"
    "sidebar main"
    "footer footer"

This produces:

    +----------------------+
    |       Header         |
    +---------+------------+
    | Sidebar |    Main    |
    +---------+------------+
    |       Footer         |
    +----------------------+

---

## 26. Grid Item Alignment

Three useful item-alignment properties:

    justify-items
    align-items
    place-items

These control how items sit inside their grid cells.

---

## 27. Grid Container Alignment

For the entire grid:

    justify-content
    align-content

These control the grid tracks inside the container when extra space is available.

---

## 28. Important Difference

Do not confuse:

    justify-items
    justify-content

and:

    align-items
    align-content

Think:

    items    → Individual grid items
    content  → Entire grid content

---

## 29. Grid Placement Example

Suppose:

    grid-template-columns: repeat(4, 1fr);

A featured item can occupy two columns:

    .featured {
        grid-column: 1 / 3;
    }

Another item can occupy two rows:

    .large-card {
        grid-row: span 2;
    }

---

## 30. Common Mistakes

### Mistake 1

Confusing grid lines with grid tracks.

A line is a boundary.

A track is the space between lines.

### Mistake 2

Forgetting that `grid-column: 1 / 3` spans two tracks, not three.

### Mistake 3

Confusing `grid-area` value order.

Remember:

    row-start / column-start / row-end / column-end

### Mistake 4

Confusing `justify-items` and `justify-content`.

### Mistake 5

Using fixed widths everywhere instead of flexible tracks.

---

## 31. Flexbox vs Advanced Grid

Flexbox is generally better when layout is primarily one-dimensional.

Grid is especially powerful when you need:

- Rows and columns
- Item spanning
- Named page regions
- Dashboard structures
- Two-dimensional placement

Both can be combined in real applications.

---

## 32. Important Patterns

### Responsive cards

    grid-template-columns:
        repeat(auto-fit, minmax(220px, 1fr));

### Featured card

    grid-column: span 2;

### Tall card

    grid-row: span 2;

### Center items

    place-items: center;

### Named layout

    grid-template-areas:
        "header header"
        "sidebar main"
        "footer footer";

---

## 📌 Key Takeaway

Advanced Grid gives precise control over item placement and responsive layouts.

The most important properties are:

    grid-column
    grid-row
    grid-area
    span
    minmax()
    auto-fit
    auto-fill
    justify-items
    align-items
    place-items

Remember:

**Grid Lines → Tracks → Cells → Placement → Spanning → Alignment**