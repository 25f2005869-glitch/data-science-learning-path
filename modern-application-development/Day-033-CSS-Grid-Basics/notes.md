# 📚 Day 033 — CSS Grid Basics Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 033  
**Topic:** CSS Grid Basics

---

## 1. What is CSS Grid?

CSS Grid is a two-dimensional CSS layout system.

It allows us to arrange elements using:

- Rows
- Columns

Grid is especially useful for complete page layouts, dashboards, galleries and card-based interfaces.

---

## 2. One-Dimensional vs Two-Dimensional Layout

Flexbox is mainly designed for one-dimensional layouts.

    Flexbox → Row OR Column

Grid is designed for two-dimensional layouts.

    Grid → Rows AND Columns

This is the basic difference between Flexbox and Grid.

---

## 3. Grid Container

An element becomes a grid container using:

    display: grid;

Example:

    .container {
        display: grid;
    }

The direct children of the container become grid items.

---

## 4. Grid Items

The direct children of a grid container are called grid items.

Example:

    <div class="container">
        <div>Item 1</div>
        <div>Item 2</div>
        <div>Item 3</div>
    </div>

Here:

    container → Grid container
    Item 1   → Grid item
    Item 2   → Grid item
    Item 3   → Grid item

---

## 5. Grid Rows and Columns

A Grid layout is made from rows and columns.

Example:

    grid-template-columns: 1fr 1fr 1fr;

This creates three columns.

Visual idea:

    Column 1 | Column 2 | Column 3
    --------------------------------
       Item  |   Item   |   Item
       Item  |   Item   |   Item

---

## 6. `grid-template-columns`

This property defines the columns of a grid.

Example:

    .grid {
        display: grid;
        grid-template-columns: 200px 200px 200px;
    }

This creates three columns, each initially sized at 200px.

---

## 7. Fractional Unit `fr`

The `fr` unit represents a fraction of the available grid space.

Example:

    grid-template-columns: 1fr 1fr;

This creates two equal columns.

Example:

    grid-template-columns: 1fr 2fr;

The available space is divided in a 1:2 proportion, subject to the grid sizing rules.

---

## 8. Three Equal Columns

Example:

    grid-template-columns: 1fr 1fr 1fr;

Or using `repeat()`:

    grid-template-columns: repeat(3, 1fr);

Both create three equal flexible columns.

---

## 9. `repeat()`

`repeat()` reduces repetition in Grid definitions.

Instead of:

    grid-template-columns: 1fr 1fr 1fr 1fr;

Use:

    grid-template-columns: repeat(4, 1fr);

This creates four equal columns.

---

## 10. `grid-template-rows`

This property defines explicit row sizes.

Example:

    grid-template-rows: 100px 200px;

The first row has an initial size of 100px and the second row has an initial size of 200px.

---

## 11. Grid Gap

`gap` creates space between grid rows and columns.

Example:

    .grid {
        display: grid;
        gap: 20px;
    }

You can also specify them separately:

    row-gap: 20px;
    column-gap: 30px;

---

## 12. Fixed Grid

A grid can use fixed sizes.

Example:

    grid-template-columns: 200px 300px;

This creates two columns with those track sizes.

Fixed grids can be useful when exact dimensions are required, but they should be used carefully in responsive designs.

---

## 13. Flexible Grid

A flexible grid can use `fr`.

Example:

    grid-template-columns: 1fr 1fr 1fr;

The columns share available space.

This is usually more adaptable than using only fixed pixel widths.

---

## 14. Mixed Grid

Grid can combine different units.

Example:

    grid-template-columns: 200px 1fr 2fr;

The first column has a fixed track size while the remaining available space is distributed between the flexible tracks according to their fractions.

---

## 15. Grid with `minmax()`

`minmax()` defines a minimum and maximum track size.

Example:

    grid-template-columns: repeat(3, minmax(200px, 1fr));

This says that each track should not normally become smaller than 200px while remaining space can be distributed up to the flexible maximum.

---

## 16. Basic Responsive Grid

A common responsive pattern is:

    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

This allows the browser to fit as many suitable columns as possible and adjust the number of columns according to available space.

---

## 17. Grid Alignment

Grid also supports alignment.

Common properties include:

    justify-items
    align-items
    place-items

These can be used to align grid items inside their grid areas.

A detailed study of these properties comes later in the Grid section.

---

## 18. Grid Item Placement

Grid automatically places items into available cells.

Example:

    .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
    }

If there are six items, Grid normally places them across the available cells row by row.

---

## 19. Grid Lines

Grid creates lines around and between tracks.

For three columns, there are generally four vertical grid lines.

Conceptually:

    Line 1 | Column 1 | Line 2 | Column 2 | Line 3 | Column 3 | Line 4

Grid lines become important when we start positioning items manually.

---

## 20. Grid Track

A grid track is a row or column between two grid lines.

Examples:

    Column track
    Row track

For:

    grid-template-columns: 1fr 1fr;

there are two column tracks.

---

## 21. Grid Cell

A grid cell is the smallest single area created by the intersection of one row track and one column track.

For example:

    +---------+---------+
    | Cell 1  | Cell 2  |
    +---------+---------+
    | Cell 3  | Cell 4  |
    +---------+---------+

There are four cells in this 2 × 2 grid.

---

## 22. Grid Area

A grid area can contain one or more grid cells.

Later, Grid properties can be used to make an item span multiple rows or columns.

---

## 23. Grid Container vs Grid Item Properties

### Container properties

    display: grid;
    grid-template-columns;
    grid-template-rows;
    gap;
    row-gap;
    column-gap;

### Item properties

More advanced placement properties include:

    grid-column;
    grid-row;
    grid-area;

These will be studied in more detail later.

---

## 24. Grid for Cards

Grid is excellent for card layouts.

Example:

    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }

Each card is automatically placed into the grid.

---

## 25. Grid for Dashboards

A dashboard can use:

    .dashboard {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }

This creates a structured row-and-column layout.

---

## 26. Common Mistakes

### Mistake 1

Forgetting:

    display: grid;

### Mistake 2

Using too many fixed widths.

### Mistake 3

Confusing `gap` with margin.

`gap` creates spacing between grid tracks/items without adding outside margin to individual items.

### Mistake 4

Confusing Grid and Flexbox.

Remember:

    Flexbox → One dimension
    Grid    → Two dimensions

---

## 27. Flexbox vs Grid

| Feature | Flexbox | Grid |
|---|---|---|
| Dimension | One-dimensional | Two-dimensional |
| Main focus | Row or column | Rows and columns |
| Page layout | Useful | Very useful |
| Card layout | Useful | Very useful |
| Alignment | Excellent | Excellent |
| Complex 2D layout | Less suitable | Excellent |

They can also be used together in the same project.

---

## 28. Important Grid Formula

For equal columns:

    grid-template-columns: repeat(N, 1fr);

Where:

    N = number of columns

Example:

    repeat(4, 1fr)

means:

    4 equal flexible columns.

---

## 📌 Key Takeaway

CSS Grid is a powerful two-dimensional layout system.

The most important starting properties are:

    display: grid;
    grid-template-columns;
    grid-template-rows;
    gap;

Remember:

**Grid = Rows + Columns**