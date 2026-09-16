
### `notes.md`

```markdown
# 📚 Day 021 — Introduction to CSS Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. What is CSS?

CSS stands for Cascading Style Sheets.

CSS is used to control the presentation and visual appearance of HTML webpages.

CSS can control:

- Colors
- Fonts
- Text appearance
- Backgrounds
- Spacing
- Borders
- Sizes
- Layout
- Responsive design
- Animations

HTML creates the structure.

CSS styles the structure.

---

# 2. HTML vs CSS

HTML and CSS have different responsibilities.

### HTML

HTML defines the structure and content.

Example:

    <h1>My Portfolio</h1>
    <p>Welcome to my portfolio.</p>

### CSS

CSS controls how that content looks.

Example:

    h1 {
        color: blue;
    }

    p {
        color: gray;
    }

---

# 3. Simple Example

HTML:

    <h1>Welcome</h1>

CSS:

    h1 {
        color: blue;
    }

The HTML creates the heading.

The CSS changes its text color.

---

# 4. Why Do We Need CSS?

Without CSS, webpages mainly contain default browser styling.

CSS allows developers to create:

- Better visual design
- Consistent styling
- Better spacing
- Attractive layouts
- Responsive webpages
- Reusable styles
- Better user experiences

---

# 5. CSS Syntax

A basic CSS rule looks like this:

    selector {
        property: value;
    }

Example:

    p {
        color: blue;
    }

Here:

- `p` is the selector.
- `color` is the property.
- `blue` is the value.

---

# 6. CSS Declaration

A property and its value together form a declaration.

Example:

    color: blue;

The complete rule is:

    p {
        color: blue;
    }

---

# 7. Declaration Block

The declarations inside `{ }` form a declaration block.

Example:

    p {
        color: blue;
        background-color: lightgray;
    }

There are two declarations:

    color: blue;

    background-color: lightgray;

---

# 8. Selector

A selector tells CSS which HTML element should be styled.

Example:

    h1 {
        color: red;
    }

The selector is:

    h1

This rule applies to `<h1>` elements.

---

# 9. Property

A property defines what aspect of an element should be changed.

Examples:

    color

    background-color

    font-size

    text-align

    width

    height

---

# 10. Value

A value defines how the property should be applied.

Example:

    color: blue;

Here:

- Property = `color`
- Value = `blue`

Another example:

    font-size: 24px;

Here:

- Property = `font-size`
- Value = `24px`

---

# 11. CSS Comments

CSS comments are written using:

    /* This is a CSS comment */

Comments are ignored by the browser.

They are useful for documenting CSS code.

---

# 12. Inline CSS

Inline CSS is written directly inside an HTML element using the `style` attribute.

Example:

    <h1 style="color: blue;">
        Welcome
    </h1>

Another example:

    <p style="background-color: lightgray;">
        This is a paragraph.
    </p>

### Advantages

- Easy for quick testing.
- Directly styles one element.

### Disadvantages

- Difficult to maintain.
- Repeated styles create unnecessary code.
- Separates content and presentation poorly.

Inline CSS should generally not be used for large webpages.

---

# 13. Internal CSS

Internal CSS is written inside a `<style>` element in the HTML `<head>`.

Example:

    <head>

        <style>

            h1 {
                color: blue;
            }

            p {
                color: gray;
            }

        </style>

    </head>

Internal CSS is useful when styles are specific to a single HTML document.

---

# 14. External CSS

External CSS is stored in a separate `.css` file.

Example HTML:

    <link rel="stylesheet"
          href="style.css">

Example CSS:

    h1 {
        color: blue;
    }

    p {
        color: gray;
    }

External CSS is generally preferred for larger projects because it keeps structure and styling separate.

---

# 15. Three Ways to Apply CSS

CSS can be applied using:

| Method | Location |
|---|---|
| Inline | `style` attribute |
| Internal | `<style>` element |
| External | Separate `.css` file |

---

# 16. Inline CSS Example

    <p style="color: red;">
        Hello World
    </p>

Only that element receives the inline style.

---

# 17. Internal CSS Example

    <style>

        p {
            color: red;
        }

    </style>

Every matching paragraph in the document can receive the style.

---

# 18. External CSS Example

HTML:

    <link rel="stylesheet"
          href="style.css">

CSS file:

    p {
        color: red;
    }

The CSS can be reused across multiple HTML pages.

---

# 19. CSS Colors

CSS can change text color using the `color` property.

Example:

    h1 {
        color: blue;
    }

Background color can be changed using:

    body {
        background-color: lightgray;
    }

---

# 20. Color Values

CSS supports different ways to represent colors.

### Color Name

    color: red;

### Hexadecimal

    color: #ff0000;

### RGB

    color: rgb(255, 0, 0);

### RGBA

    color: rgba(255, 0, 0, 0.5);

### HSL

    color: hsl(0, 100%, 50%);

At the beginner level, color names and hexadecimal values are useful starting points.

---

# 21. Text Color

The `color` property changes text color.

Example:

    p {
        color: green;
    }

---

# 22. Background Color

The `background-color` property changes the background color.

Example:

    body {
        background-color: #f5f5f5;
    }

Another example:

    h1 {
        background-color: lightblue;
    }

---

# 23. Font Size

The `font-size` property controls the size of text.

Example:

    h1 {
        font-size: 36px;
    }

Example:

    p {
        font-size: 18px;
    }

---

# 24. Text Alignment

The `text-align` property controls horizontal text alignment.

Example:

    h1 {
        text-align: center;
    }

Possible values include:

- left
- center
- right
- justify

---

# 25. Multiple Properties

One selector can contain multiple declarations.

Example:

    h1 {
        color: blue;
        background-color: lightgray;
        font-size: 32px;
        text-align: center;
    }

CSS applies all valid declarations.

---

# 26. CSS and HTML Relationship

Think of HTML as the structure of a house.

CSS is the design and decoration of the house.

HTML defines:

- Walls
- Rooms
- Doors
- Windows

CSS defines:

- Colors
- Sizes
- Spacing
- Appearance
- Layout

---

# 27. Cascading

The word "Cascading" in CSS refers to the process used by the browser to determine which styles apply when multiple rules affect the same element.

CSS considers factors such as:

- Importance
- Specificity
- Source order

These concepts will be studied in greater detail later.

---

# 28. CSS Best Practices

Follow these practices:

1. Prefer external CSS for larger projects.
2. Keep CSS organized.
3. Use meaningful selectors.
4. Avoid unnecessary inline styles.
5. Use consistent formatting.
6. Use comments where useful.
7. Avoid repeating the same styles unnecessarily.
8. Keep HTML structure separate from CSS presentation.

---

# 29. Basic CSS Mental Model

Remember:

    Selector
        ↓
    Property
        ↓
    Value

Example:

    p {
        color: blue;
    }

    p     → Selector
    color → Property
    blue  → Value

---

# 30. First CSS Practice

Create an HTML page containing:

- One heading
- Two paragraphs
- One list

Then apply CSS to:

- Change heading color.
- Change paragraph color.
- Change background color.
- Change heading size.
- Center the heading.

---

# 31. Important Terms

| Term | Meaning |
|---|---|
| CSS | Cascading Style Sheets |
| Selector | Selects HTML elements |
| Property | Defines what to change |
| Value | Defines how to change it |
| Declaration | Property + value |
| Declaration Block | Declarations inside `{ }` |
| Inline CSS | CSS inside `style` |
| Internal CSS | CSS inside `<style>` |
| External CSS | CSS in separate file |

---

# 32. Final Revision

The most important concepts from Day 021 are:

    CSS = Cascading Style Sheets

    HTML = Structure

    CSS = Presentation

    Selector = What to style

    Property = What to change

    Value = How to change it

    Inline CSS = style attribute

    Internal CSS = <style>

    External CSS = .css file

---

**End of Day 021 Notes**