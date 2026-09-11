# 📝 Day 011 — HTML Tables Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development (MAD 1)

---

# 1. Introduction to HTML Tables

HTML tables are used to display structured data in rows and columns.

Tables are useful when information has a natural relationship between rows and columns.

Common examples include:

- Student records
- Marks
- Course information
- Exam schedules
- Product details
- Employee records
- Timetables

---

# 2. The `<table>` Element

The `<table>` element is used to create an HTML table.

All table-related rows and cells are placed inside the `<table>` element.

Basic structure:

    <table>
        ...
    </table>

---

# 3. The `<tr>` Element

`<tr>` stands for **Table Row**.

It is used to create a row inside a table.

Example:

    <tr>
        <td>Saloni</td>
        <td>MAD 1</td>
    </tr>

---

# 4. The `<th>` Element

`<th>` stands for **Table Header**.

It is used to define a header cell.

Example:

    <th>Name</th>

Headers describe the information contained in a column or row.

For example:

    Name | Course | Status

Here, `Name`, `Course`, and `Status` can be table headers.

---

# 5. The `<td>` Element

`<td>` stands for **Table Data**.

It is used to define a normal data cell.

Example:

    <td>Saloni</td>

A `<td>` element normally contains the actual data of the table.

---

# 6. Basic HTML Table

A simple HTML table uses:

- `<table>` for the complete table
- `<tr>` for rows
- `<th>` for headers
- `<td>` for data

Example:

    <table>

        <tr>
            <th>Name</th>
            <th>Course</th>
        </tr>

        <tr>
            <td>Saloni</td>
            <td>MAD 1</td>
        </tr>

    </table>

---

# 7. Rows and Columns

Consider:

    Name       Age       Course
    Saloni     18        MAD
    Rahul      20        PDSA

The table contains:

- 3 columns
- 3 rows if the header row is included

### Columns

`Name`, `Age`, and `Course` represent columns.

### Rows

Each horizontal group of cells represents a row.

---

# 8. The `<caption>` Element

The `<caption>` element provides a title or description for a table.

Example:

    <table>

        <caption>Student Details</caption>

        ...

    </table>

A meaningful caption helps users understand what the table represents.

---

# 9. The `<thead>` Element

`<thead>` is used to group the header rows of a table.

Example:

    <thead>

        <tr>
            <th>Name</th>
            <th>Course</th>
            <th>Status</th>
        </tr>

    </thead>

It makes the table structure more meaningful and organized.

---

# 10. The `<tbody>` Element

`<tbody>` contains the main data rows of a table.

Example:

    <tbody>

        <tr>
            <td>Saloni</td>
            <td>MAD 1</td>
            <td>Learning</td>
        </tr>

        <tr>
            <td>Rahul</td>
            <td>PDSA</td>
            <td>Learning</td>
        </tr>

    </tbody>

---

# 11. The `<tfoot>` Element

`<tfoot>` is used for footer or summary information.

Example:

    <tfoot>

        <tr>
            <td>Total</td>
            <td>2</td>
            <td>Students</td>
        </tr>

    </tfoot>

It can be useful for:

- Totals
- Averages
- Summaries
- Final information

---

# 12. Complete Table Structure

A well-structured table can contain:

- `<caption>`
- `<thead>`
- `<tbody>`
- `<tfoot>`

Example:

    <table>

        <caption>Student Details</caption>

        <thead>

            <tr>
                <th>Name</th>
                <th>Course</th>
            </tr>

        </thead>

        <tbody>

            <tr>
                <td>Saloni</td>
                <td>MAD 1</td>
            </tr>

            <tr>
                <td>Rahul</td>
                <td>PDSA</td>
            </tr>

        </tbody>

        <tfoot>

            <tr>
                <td>Total Students</td>
                <td>2</td>
            </tr>

        </tfoot>

    </table>

---

# 13. Understanding `colspan`

The `colspan` attribute allows one table cell to span multiple columns.

Example:

    <th colspan="3">
        Student Information
    </th>

If `colspan="3"` is used, the cell occupies the space of three columns.

Conceptually:

    +--------------------------------+
    |       Student Information      |
    +------------+--------+----------+
    | Name       | Age    | Course   |
    +------------+--------+----------+

The first cell spans all three columns.

---

# 14. Understanding `rowspan`

The `rowspan` attribute allows one table cell to span multiple rows.

Example:

    <td rowspan="2">
        Saloni
    </td>

The cell occupies the space of two rows.

Conceptually:

    +----------+----------+
    | Saloni   | MAD 1    |
    |          +----------+
    |          | DBMS     |
    +----------+----------+

---

# 15. `colspan` vs `rowspan`

The easiest way to remember them is:

    colspan → columns
    rowspan → rows

### `colspan`

Spans horizontally across columns.

Example:

    <td colspan="3">

### `rowspan`

Spans vertically across rows.

Example:

    <td rowspan="3">

---

# 16. The `scope` Attribute

The `scope` attribute helps define what a table header applies to.

It is especially useful for table accessibility.

Two common values are:

    scope="col"
    scope="row"

---

# 17. `scope="col"`

`scope="col"` indicates that a header applies to a column.

Example:

    <th scope="col">Name</th>
    <th scope="col">Course</th>
    <th scope="col">Status</th>

These headers describe the columns below them.

---

# 18. `scope="row"`

`scope="row"` indicates that a header applies to a row.

Example:

    <th scope="row">DBMS</th>
    <td>85</td>
    <td>A</td>

Here, `DBMS` identifies the row.

---

# 19. Table Accessibility

Tables should be structured so that their information is understandable to different users and assistive technologies.

Good practices include:

- Use `<th>` for headers.
- Use `<caption>` when a table needs a title.
- Use `scope` for appropriate headers.
- Keep rows and columns logically organized.
- Use meaningful data.
- Avoid unnecessary complexity.

---

# 20. Tables Should Represent Data

HTML tables should primarily be used for **tabular data**.

Good examples:

- Student marks
- Course schedules
- Exam results
- Product information
- Employee records
- Financial data

Tables should not normally be used to create the overall layout of a webpage.

For webpage layout, CSS is the appropriate tool.

---

# 21. Student Marks Table

A student marks table may contain:

    Subject | Marks | Grade
    DBMS    | 85    | A
    PDSA    | 90    | A+
    MLF     | 82    | A

A corresponding HTML structure can be:

    <table>

        <caption>Student Marks</caption>

        <thead>

            <tr>
                <th scope="col">Subject</th>
                <th scope="col">Marks</th>
                <th scope="col">Grade</th>
            </tr>

        </thead>

        <tbody>

            <tr>
                <th scope="row">DBMS</th>
                <td>85</td>
                <td>A</td>
            </tr>

            <tr>
                <th scope="row">PDSA</th>
                <td>90</td>
                <td>A+</td>
            </tr>

        </tbody>

    </table>

---

# 22. Column Headers and Row Headers

A table can have both column headers and row headers.

### Column Header

    <th scope="col">Subject</th>

This identifies a column.

### Row Header

    <th scope="row">DBMS</th>

This identifies a row.

Using appropriate headers makes the relationship between the data and headers clearer.

---

# 23. Table Hierarchy

A structured table can be remembered as:

    <table>
    │
    ├── <caption>
    │
    ├── <thead>
    │   └── <tr>
    │       ├── <th>
    │       ├── <th>
    │       └── <th>
    │
    ├── <tbody>
    │   └── <tr>
    │       ├── <td>
    │       ├── <td>
    │       └── <td>
    │
    └── <tfoot>
        └── <tr>
            ├── <td>
            └── <td>

---

# 24. The `border` Attribute

For simple learning examples, a table can be displayed with:

    <table border="1">

This makes the table borders visible.

However, modern web development generally uses CSS for table styling.

Therefore, `border="1"` is useful for learning and demonstration, but CSS should be preferred for professional styling.

---

# 25. Common Mistakes

## Mistake 1 — Using `<td>` for Headers

Instead of:

    <td>Name</td>

Use:

    <th>Name</th>

when `Name` is a table header.

---

## Mistake 2 — Forgetting `<tr>`

Table cells should be placed inside table rows.

Correct:

    <tr>

        <td>Saloni</td>
        <td>MAD 1</td>

    </tr>

---

## Mistake 3 — Incorrect `colspan`

If a heading should cover three columns:

    <th colspan="3">
        Student Information
    </th>

The value should match the number of columns that the cell needs to span.

---

## Mistake 4 — Incorrect `rowspan`

If a cell should cover two rows:

    <td rowspan="2">
        Saloni
    </td>

---

## Mistake 5 — Using Tables for Page Layout

Tables should represent data, not the overall webpage layout.

Use CSS for layout and design.

---

# 26. Important Table Elements

    <table>    → Complete table
    <tr>       → Table row
    <th>       → Table header cell
    <td>       → Table data cell
    <caption>  → Table title
    <thead>    → Header section
    <tbody>    → Main data section
    <tfoot>    → Footer section

---

# 27. Important Table Attributes

### `colspan`

Allows a cell to span multiple columns.

    <td colspan="2">

### `rowspan`

Allows a cell to span multiple rows.

    <td rowspan="2">

### `scope`

Defines whether a header applies to a row or column.

    <th scope="col">

    <th scope="row">

---

# 28. Practical Example

Consider an IIT Madras learning progress table:

    Course | Credits | Status
    DBMS   | 4       | Learning
    PDSA   | 4       | Learning
    MLF    | 4       | Learning

This information naturally fits into an HTML table because it has rows and columns.

---

# 29. When to Use Tables

Use tables when:

- Data has rows and columns.
- Users need to compare related values.
- Information is naturally tabular.
- Structured records need to be displayed.

Examples:

    Student Records
    Exam Results
    Course Schedule
    Product Details
    Employee Data

---

# 30. When Not to Use Tables

Do not use tables just to position elements on a webpage.

For example, creating:

    Header
    Left Menu | Main Content
    Footer

using a table is not the recommended modern approach.

CSS should be used for webpage layout.

---

# 31. Day 011 Summary

In Day 011, I learned HTML Tables in detail.

Important concepts learned:

- `<table>`
- `<tr>`
- `<th>`
- `<td>`
- `<caption>`
- `<thead>`
- `<tbody>`
- `<tfoot>`
- `colspan`
- `rowspan`
- `scope`

I also learned how to create structured and accessible tables for displaying data.

---

# 🎯 Key Takeaways

    <table>   → Complete Table
    <tr>      → Table Row
    <th>      → Table Header
    <td>      → Table Data
    <caption> → Table Title
    <thead>   → Header Section
    <tbody>   → Body Section
    <tfoot>   → Footer Section

    colspan   → Spans Columns
    rowspan   → Spans Rows
    scope     → Defines Header Relationship

---

# ⭐ Final Learning Goal

By the end of Day 011, I should be able to:

- Create a table from scratch.
- Create headers and data cells.
- Organize tables using `<thead>`, `<tbody>`, and `<tfoot>`.
- Use `colspan` and `rowspan`.
- Use `scope` for table headers.
- Explain the structure of an HTML table.
- Create tables for real-world structured data.

---

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development (MAD 1)