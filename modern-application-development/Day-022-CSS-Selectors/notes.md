
### `notes.md`

```markdown
# 📚 Day 022 — CSS Selectors Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. What is a CSS Selector?

A CSS selector identifies the HTML elements to which CSS rules should be applied.

Basic structure:

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

The browser selects all matching `<p>` elements and applies the rule.

---

# 2. Why Are Selectors Important?

Selectors allow us to control exactly which elements receive a style.

For example, suppose a page contains:

    <h1>Portfolio</h1>
    <h2>Skills</h2>
    <p>HTML is a markup language.</p>
    <p>CSS is a styling language.</p>

We can style all paragraphs using:

    p {
        color: blue;
    }

We can style only the heading using:

    h1 {
        color: red;
    }

Selectors provide control over styling.

---

# 3. Universal Selector

The universal selector is:

    *

It selects all elements.

Example:

    * {
        box-sizing: border-box;
    }

Another example:

    * {
        color: black;
    }

Be careful when using the universal selector because it affects every element.

---

# 4. Element Selector

An element selector selects all elements of a particular HTML type.

Example:

    p {
        color: blue;
    }

This selects every `<p>` element.

Another example:

    h1 {
        color: red;
    }

This selects every `<h1>` element.

---

# 5. Class Selector

A class selector begins with a dot:

    .

Example:

    .highlight {
        color: red;
    }

HTML:

    <p class="highlight">
        Important information.
    </p>

The class selector can be reused on multiple elements.

Example:

    <p class="highlight">
        First paragraph.
    </p>

    <p class="highlight">
        Second paragraph.
    </p>

Both elements receive the `.highlight` style.

---

# 6. ID Selector

An ID selector begins with:

    #

Example:

    #main-title {
        color: blue;
    }

HTML:

    <h1 id="main-title">
        My Portfolio
    </h1>

An ID should identify one unique element within a page.

---

# 7. Class vs ID

Class:

    .card {
        background-color: lightgray;
    }

ID:

    #profile {
        background-color: lightblue;
    }

Important difference:

- A class can be reused.
- An ID should be unique within the document.

Classes are generally preferred for reusable styling.

---

# 8. Grouping Selector

Multiple selectors can be grouped using commas.

Example:

    h1, h2, h3 {
        color: blue;
    }

This applies the same style to all three heading types.

Without grouping:

    h1 {
        color: blue;
    }

    h2 {
        color: blue;
    }

    h3 {
        color: blue;
    }

Grouping makes the CSS shorter and easier to maintain.

---

# 9. Descendant Selector

A descendant selector uses a space between selectors.

Example:

    section p {
        color: blue;
    }

This selects all `<p>` elements inside a `<section>`.

HTML:

    <section>

        <p>
            This paragraph is selected.
        </p>

    </section>

The paragraph can be nested at any level inside the section.

---

# 10. Child Selector

The child selector uses:

    >

Example:

    section > p {
        color: green;
    }

This selects only paragraphs that are direct children of the section.

Example:

    <section>

        <p>
            Direct child.
        </p>

        <div>

            <p>
                Not a direct child.
            </p>

        </div>

    </section>

The first paragraph is selected.

The second paragraph is not selected by `section > p`.

---

# 11. Descendant vs Child Selector

Descendant:

    section p

Means:

    Any p inside section

Child:

    section > p

Means:

    Direct p child of section

This difference is very important.

---

# 12. Adjacent Sibling Selector

The adjacent sibling selector uses:

    +

Example:

    h2 + p {
        color: red;
    }

This selects the first `<p>` immediately following an `<h2>`.

HTML:

    <h2>Introduction</h2>

    <p>
        This paragraph is selected.
    </p>

---

# 13. General Sibling Selector

The general sibling selector uses:

    ~

Example:

    h2 ~ p {
        color: green;
    }

This selects all matching sibling paragraphs that appear after the `<h2>`.

---

# 14. Adjacent vs General Sibling

Adjacent sibling:

    h2 + p

Means:

    The immediately following p

General sibling:

    h2 ~ p

Means:

    Matching siblings appearing later

---

# 15. Attribute Selector

Attribute selectors select elements based on their attributes.

Basic syntax:

    [attribute]

Example:

    [required] {
        border: 2px solid red;
    }

This selects elements containing the `required` attribute.

---

# 16. Attribute Value Selector

Syntax:

    [attribute="value"]

Example:

    input[type="email"] {
        background-color: lightblue;
    }

This selects input elements whose type is exactly `email`.

---

# 17. Starts With Attribute Selector

Syntax:

    [attribute^="value"]

Example:

    a[href^="https"] {
        color: green;
    }

This selects links whose `href` starts with `https`.

---

# 18. Ends With Attribute Selector

Syntax:

    [attribute$="value"]

Example:

    img[src$=".png"] {
        border: 2px solid black;
    }

This selects images whose source ends with `.png`.

---

# 19. Contains Attribute Selector

Syntax:

    [attribute*="value"]

Example:

    a[href*="github"] {
        font-weight: bold;
    }

This selects links whose `href` contains `github`.

---

# 20. Pseudo-Class

A pseudo-class represents a special state of an element.

Pseudo-classes begin with:

    :

Example:

    a:hover {
        color: red;
    }

The style is applied when the user moves the mouse over the link.

---

# 21. :hover

`:hover` applies when the pointer is over an element.

Example:

    button:hover {
        background-color: lightblue;
    }

---

# 22. :focus

`:focus` applies when an element receives focus.

Example:

    input:focus {
        background-color: lightyellow;
    }

This is especially useful for form controls.

---

# 23. :first-child

`:first-child` selects an element if it is the first child of its parent.

Example:

    li:first-child {
        font-weight: bold;
    }

---

# 24. :last-child

`:last-child` selects an element if it is the last child of its parent.

Example:

    li:last-child {
        color: red;
    }

---

# 25. :nth-child()

`:nth-child()` allows selection based on the position of an element.

Example:

    li:nth-child(2) {
        color: blue;
    }

This selects the second child.

Another example:

    li:nth-child(odd) {
        background-color: lightgray;
    }

Another example:

    li:nth-child(even) {
        background-color: white;
    }

---

# 26. :checked

`:checked` selects checked radio buttons and checkboxes.

Example:

    input:checked {
        accent-color: green;
    }

---

# 27. :disabled

`:disabled` selects disabled form controls.

Example:

    input:disabled {
        background-color: lightgray;
    }

---

# 28. Combining Selectors

Selectors can be combined.

Example:

    p.highlight {
        color: red;
    }

This selects only `<p>` elements having the `highlight` class.

HTML:

    <p class="highlight">
        Selected paragraph.
    </p>

---

# 29. Element + Class

Example:

    h1.title {
        color: blue;
    }

This means:

    h1 element
    +
    title class

It does not select a `<p class="title">`.

---

# 30. Class + Class

Example:

    .card.featured {
        border: 2px solid blue;
    }

This selects elements that have both:

    card

and:

    featured

classes.

---

# 31. Descendant with Class

Example:

    .card p {
        color: gray;
    }

This selects paragraphs inside elements having the `card` class.

---

# 32. ID with Element

Example:

    section#about {
        background-color: lightgray;
    }

This selects a `<section>` element whose ID is `about`.

---

# 33. CSS Specificity

When multiple CSS rules target the same element, the browser needs to determine which rule has greater priority.

One important factor is specificity.

A simplified order is:

    Element
       ↓
    Class / Attribute / Pseudo-class
       ↓
    ID

For example:

    p {
        color: blue;
    }

    .text {
        color: green;
    }

    #special {
        color: red;
    }

If the same paragraph has:

    <p id="special" class="text">
        Hello
    </p>

The ID selector has higher specificity than the class and element selector.

Therefore the text will be red.

---

# 34. Specificity Mental Model

Think of specificity approximately as:

    ID
    >
    Class / Attribute / Pseudo-class
    >
    Element

This is a simplified model.

CSS also considers source order and `!important`.

Detailed specificity will be studied later.

---

# 35. Source Order

If two selectors have equal specificity, the rule appearing later can win.

Example:

    p {
        color: blue;
    }

    p {
        color: green;
    }

The second rule wins because it appears later.

---

# 36. The !important Rule

CSS supports:

    !important

Example:

    p {
        color: red !important;
    }

It can override normal declarations.

However, `!important` should not be used unnecessarily because it makes CSS harder to maintain.

---

# 37. Selector Best Practices

Follow these practices:

1. Prefer classes for reusable styling.
2. Keep IDs unique.
3. Avoid unnecessarily complex selectors.
4. Use meaningful class names.
5. Avoid excessive use of `!important`.
6. Keep selectors readable.
7. Use grouping when the same style applies to multiple elements.
8. Use semantic HTML together with appropriate selectors.

---

# 38. Common Selector Symbols

| Symbol | Meaning |
|---|---|
| `*` | Universal |
| `.` | Class |
| `#` | ID |
| `,` | Grouping |
| ` ` | Descendant |
| `>` | Direct child |
| `+` | Adjacent sibling |
| `~` | General sibling |
| `[]` | Attribute |
| `:` | Pseudo-class |

---

# 39. Selector Revision

Remember:

    *        → Everything

    p        → All paragraphs

    .box     → Elements with class box

    #title   → Element with ID title

    h1, h2   → h1 and h2

    div p    → p inside div

    div > p  → Direct child p

    h2 + p   → Immediately following p

    h2 ~ p   → Later sibling p

    [required] → Elements with required

    a:hover  → Hovered links

---

# 40. Final Mental Model

CSS selector answers one question:

    "Which HTML element should I style?"

Then the CSS declaration answers:

    "What style should I apply?"

Example:

    .student {
        color: blue;
    }

    .student
        ↓
    Which element?

    color
        ↓
    What property?

    blue
        ↓
    What value?

---

**End of Day 022 Notes**