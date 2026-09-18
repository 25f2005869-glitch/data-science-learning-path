# 📚 Day 036 — CSS Media Queries Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 036  
**Topic:** CSS Media Queries

---

## 1. What is a Media Query?

A CSS Media Query allows CSS rules to be applied only when specific conditions are true.

Media Queries are commonly used for responsive web design.

Example:

    @media (max-width: 600px) {
        body {
            font-size: 0.9rem;
        }
    }

When the viewport width is 600px or less, the rule is applied.

---

## 2. Basic Syntax

General syntax:

    @media (condition) {
        selector {
            property: value;
        }
    }

Example:

    @media (max-width: 700px) {
        .container {
            width: 95%;
        }
    }

---

## 3. Why Media Queries Are Used

Media Queries allow a website to adapt to different environments.

They can change:

- Layout
- Font size
- Spacing
- Navigation
- Number of columns
- Element visibility
- Direction of Flexbox
- Grid structure

---

## 4. Viewport Width

The most common Media Query condition is viewport width.

Example:

    @media (max-width: 600px) {
        ...
    }

This applies when the viewport is 600px wide or less.

---

## 5. `max-width`

`max-width` means:

**Apply these styles up to this maximum viewport width.**

Example:

    @media (max-width: 600px) {
        .cards {
            grid-template-columns: 1fr;
        }
    }

This is commonly used in desktop-first designs.

---

## 6. `min-width`

`min-width` means:

**Apply these styles when the viewport is at least this wide.**

Example:

    @media (min-width: 700px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

This is commonly used in mobile-first designs.

---

## 7. Mobile-First Design

Mobile-first means writing the basic CSS for small screens first.

Then larger-screen styles are added using `min-width`.

Example:

    .cards {
        display: grid;
        grid-template-columns: 1fr;
    }

    @media (min-width: 700px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (min-width: 1000px) {
        .cards {
            grid-template-columns: repeat(3, 1fr);
        }
    }

This approach progressively enhances the layout.

---

## 8. Desktop-First Design

Desktop-first starts with a large-screen layout.

Smaller layouts are created using `max-width`.

Example:

    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
    }

    @media (max-width: 700px) {
        .cards {
            grid-template-columns: 1fr;
        }
    }

---

## 9. Breakpoints

A breakpoint is a viewport condition where the layout changes.

Example:

    @media (min-width: 700px) {
        ...
    }

The exact breakpoint should be selected according to the content and layout.

Do not add breakpoints simply because a particular device has a particular screen size.

---

## 10. Multiple Breakpoints

A page can have multiple Media Queries.

Example:

    .cards {
        grid-template-columns: 1fr;
    }

    @media (min-width: 700px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (min-width: 1000px) {
        .cards {
            grid-template-columns: repeat(3, 1fr);
        }
    }

Conceptually:

    Small screen  → 1 column
    Medium screen → 2 columns
    Large screen  → 3 columns

---

## 11. `min-height`

Media Queries can also check viewport height.

Example:

    @media (min-height: 700px) {
        .hero {
            min-height: 500px;
        }
    }

---

## 12. `max-height`

Example:

    @media (max-height: 500px) {
        .hero {
            padding: 1rem;
        }
    }

This can be useful when vertical space is limited.

---

## 13. Orientation

Media Queries can detect orientation.

### Portrait

    @media (orientation: portrait) {
        ...
    }

### Landscape

    @media (orientation: landscape) {
        ...
    }

Orientation depends on the relationship between viewport width and height.

---

## 14. Media Types

A Media Query can specify a media type.

Common types include:

    screen
    print

Example:

    @media screen and (max-width: 600px) {
        ...
    }

Example for printing:

    @media print {
        .navigation {
            display: none;
        }
    }

---

## 15. `and`

The `and` operator combines conditions.

Example:

    @media screen and (min-width: 700px) {
        ...
    }

Both conditions must be satisfied.

---

## 16. Multiple Conditions

Example:

    @media screen and (min-width: 700px) and (max-width: 1000px) {
        ...
    }

This targets a viewport within the specified range.

---

## 17. `not`

`not` can negate a Media Query condition.

Example:

    @media not print {
        ...
    }

Use logical conditions carefully so the CSS remains easy to understand.

---

## 18. `or` with Commas

Media Queries can use commas to represent alternatives.

Example:

    @media (max-width: 600px), (orientation: portrait) {
        ...
    }

The styles apply when either condition matches.

---

## 19. Responsive Navigation

Example:

    .nav-list {
        display: flex;
        gap: 20px;
    }

    @media (max-width: 600px) {
        .nav-list {
            flex-direction: column;
        }
    }

The navigation changes from a row to a column on smaller screens.

---

## 20. Responsive Grid

Example:

    .cards {
        display: grid;
        grid-template-columns: 1fr;
    }

    @media (min-width: 700px) {
        .cards {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (min-width: 1000px) {
        .cards {
            grid-template-columns: repeat(3, 1fr);
        }
    }

---

## 21. Responsive Flexbox

Example:

    .container {
        display: flex;
        flex-direction: column;
    }

    @media (min-width: 700px) {
        .container {
            flex-direction: row;
        }
    }

---

## 22. Responsive Typography

Media Queries can change font sizes.

Example:

    h1 {
        font-size: 1.8rem;
    }

    @media (min-width: 900px) {
        h1 {
            font-size: 2.5rem;
        }
    }

Use this carefully. Responsive typography should remain readable at all sizes.

---

## 23. Responsive Spacing

Example:

    .section {
        padding: 1rem;
    }

    @media (min-width: 700px) {
        .section {
            padding: 2rem;
        }
    }

---

## 24. Hiding Elements

An element can be hidden at a breakpoint.

Example:

    @media (max-width: 600px) {
        .desktop-only {
            display: none;
        }
    }

However, hiding important content only to make a layout fit should be avoided.

---

## 25. Print Media Query

Media Queries can create print-specific styles.

Example:

    @media print {
        .navigation,
        .footer {
            display: none;
        }

        body {
            background: white;
        }
    }

This can make printed pages cleaner.

---

## 26. Media Queries and CSS Cascade

Media Query rules participate in the normal CSS cascade.

If two rules have the same specificity, the later applicable rule can win.

Example:

    .card {
        width: 80%;
    }

    @media (min-width: 700px) {
        .card {
            width: 60%;
        }
    }

At 700px and above, the Media Query rule applies.

---

## 27. Media Queries vs Responsive Units

Media Queries are not the only responsive technique.

Responsive design can also use:

- `%`
- `rem`
- `vw`
- `vh`
- `fr`
- `minmax()`
- `auto-fit`
- `auto-fill`
- Flexbox

Good responsive layouts often combine these techniques.

---

## 28. Avoid Too Many Breakpoints

Do not create a Media Query for every small width.

Too many breakpoints can make CSS:

- Difficult to understand
- Difficult to debug
- Difficult to maintain

Use breakpoints when the content actually needs a layout change.

---

## 29. Common Mistakes

### Mistake 1

Forgetting the `@media` syntax.

### Mistake 2

Using `max-width` when intending mobile-first progressive enhancement.

### Mistake 3

Adding too many breakpoints.

### Mistake 4

Using device names instead of content-based breakpoints.

### Mistake 5

Forgetting to test intermediate widths.

---

## 30. Testing Media Queries

Use browser developer tools to test different viewport sizes.

Check:

- Navigation
- Cards
- Images
- Text
- Tables
- Forms
- Spacing
- Horizontal overflow

Do not test only one mobile size and one desktop size.

---

## 31. Practical Mobile-First Pattern

    .layout {
        display: grid;
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    @media (min-width: 700px) {
        .layout {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (min-width: 1000px) {
        .layout {
            grid-template-columns: repeat(3, 1fr);
        }
    }

This is a simple and maintainable pattern.

---

## 32. Practical Desktop-First Pattern

    .layout {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
    }

    @media (max-width: 900px) {
        .layout {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 600px) {
        .layout {
            grid-template-columns: 1fr;
        }
    }

---

## 33. Media Query Mental Model

When writing a Media Query, ask:

1. What condition am I checking?
2. What changes when the condition is true?
3. Is the breakpoint actually necessary?
4. Does the content remain readable?
5. Does the layout work between breakpoints?

---

## 📌 Key Takeaway

Media Queries allow CSS to respond to different conditions.

The most important syntax is:

    @media (max-width: 600px) {
        ...
    }

and:

    @media (min-width: 700px) {
        ...
    }

Remember:

**Base Styles + Flexible Layout + Meaningful Breakpoints = Responsive Design**