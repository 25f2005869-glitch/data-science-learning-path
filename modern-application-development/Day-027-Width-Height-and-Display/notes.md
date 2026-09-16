# 📘 Day 027 — CSS Width, Height and Display — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 027  
**Topic:** CSS Width, Height and Display

---

## 1. Introduction

CSS provides properties to control the **size, dimensions, visibility, and layout behavior** of HTML elements.

The most important concepts covered in this day are:

- `width`
- `height`
- `min-width`
- `max-width`
- `min-height`
- `max-height`
- `display`
- `block`
- `inline`
- `inline-block`
- `none`
- `visibility: hidden`
- `box-sizing`
- Responsive width

---

# 2. CSS Width

The `width` property controls the horizontal size of an element.

Example:

    .box {
        width: 300px;
    }

The width can be specified using different units.

### Common Units

    width: 300px;
    width: 50%;
    width: 20rem;
    width: 50vw;
    width: auto;

---

## 3. Width in Pixels

Pixels provide a fixed size.

Example:

    .box {
        width: 300px;
    }

The element attempts to have a width of 300 pixels.

Fixed widths can be useful for specific components, but they should be used carefully in responsive layouts.

---

# 4. Width in Percentage

Percentage widths are calculated relative to the containing block.

Example:

    .box {
        width: 50%;
    }

If the parent has a width of 800px, the child may have a width of approximately 400px, subject to the surrounding layout and box model.

---

# 5. Width with Auto

`auto` allows the browser to determine the appropriate width.

Example:

    .box {
        width: auto;
    }

For block elements, `width: auto` commonly allows the element to use the available horizontal space.

---

# 6. CSS Height

The `height` property controls the vertical size of an element.

Example:

    .box {
        height: 200px;
    }

Common units include:

    px
    %
    rem
    vh
    auto

---

# 7. Height in Pixels

Example:

    .box {
        height: 200px;
    }

The element gets a specified height of 200 pixels, subject to the box-sizing model and other constraints.

---

# 8. Height in Percentage

Percentage height depends on the height of the containing block.

Example:

    .parent {
        height: 400px;
    }

    .child {
        height: 50%;
    }

The child can have a height of 200px because 50% of 400px is 200px.

Percentage heights can behave unexpectedly when the parent does not have a definite height.

---

# 9. Height with Auto

Example:

    .box {
        height: auto;
    }

`auto` allows the browser to determine the height based on the content and layout.

This is commonly useful when content can have different amounts of text.

---

# 10. Minimum Width

The `min-width` property specifies the smallest width an element is allowed to have.

Example:

    .box {
        min-width: 200px;
    }

The element should not become narrower than the specified minimum, subject to other layout constraints.

---

# 11. Maximum Width

The `max-width` property specifies the largest width an element is allowed to have.

Example:

    .container {
        max-width: 800px;
    }

A common responsive pattern is:

    .container {
        width: 100%;
        max-width: 800px;
    }

This allows the container to shrink on smaller screens while limiting its maximum width.

---

# 12. Minimum Height

The `min-height` property specifies the minimum height of an element.

Example:

    .card {
        min-height: 200px;
    }

The element can become taller if its content requires additional space.

---

# 13. Maximum Height

The `max-height` property limits the maximum height of an element.

Example:

    .box {
        max-height: 400px;
    }

If the content exceeds the available height, additional overflow handling may be required.

Example:

    .box {
        max-height: 400px;
        overflow: auto;
    }

---

# 14. Width and Height Together

Example:

    .box {
        width: 300px;
        height: 200px;
    }

This creates an element with specified dimensions.

Remember that padding and borders can affect the final rendered dimensions depending on the `box-sizing` property.

---

# 15. The Display Property

The `display` property controls how an element participates in the layout.

Common values include:

    display: block;
    display: inline;
    display: inline-block;
    display: none;

The display type strongly affects:

- Line placement
- Width
- Height
- Spacing
- Layout behavior

---

# 16. Display Block

`display: block` makes an element behave as a block-level element.

Example:

    .box {
        display: block;
    }

Typical characteristics:

- Starts on a new line.
- Usually occupies the available horizontal space by default.
- Width and height can be applied.
- Margin and padding can be applied.

Common block elements include:

    <div>
    <p>
    <h1>
    <section>
    <header>
    <footer>

---

# 17. Display Inline

`display: inline` makes an element participate in the current line of text.

Example:

    .text {
        display: inline;
    }

Typical characteristics:

- Does not normally start on a new line.
- Takes only the space needed by its content.
- `width` and `height` do not behave like they do on block-level boxes.
- Horizontal padding, borders, and margins can affect the inline box, but inline layout has different behavior from block layout.

Common inline elements include:

    <span>
    <a>
    <strong>
    <em>

---

# 18. Display Inline-Block

`display: inline-block` combines characteristics of inline and block formatting.

Example:

    .card {
        display: inline-block;
        width: 250px;
        height: 200px;
    }

Typical characteristics:

- Can appear beside other inline-level content when space is available.
- Width can be specified.
- Height can be specified.
- Padding and borders can be applied.

It is useful for simple horizontal card layouts and navigation items.

---

# 19. Display None

`display: none` removes an element from the layout.

Example:

    .hidden {
        display: none;
    }

The element:

- Is not rendered as a box.
- Does not occupy layout space.

Example:

    <p class="hidden">This text is hidden.</p>

The surrounding content behaves as though that element is not present in the layout.

---

# 20. Visibility Hidden

`visibility: hidden` makes an element invisible while preserving its layout space.

Example:

    .hidden {
        visibility: hidden;
    }

The element:

- Is not visually visible.
- Still occupies its layout space.

---

# 21. Display None vs Visibility Hidden

| Feature | `display: none` | `visibility: hidden` |
|---|---|---|
| Visible | No | No |
| Occupies layout space | No | Yes |
| Removed from normal layout | Yes | No |
| Can preserve element position | No | Yes |

Remember:

    display: none
    → Hide and remove layout space

    visibility: hidden
    → Hide but preserve layout space

---

# 22. Changing Display Type

CSS can change the display behavior of an element.

Example:

    span {
        display: block;
    }

Now the `span` behaves as a block-level box.

Another example:

    div {
        display: inline;
    }

Now the `div` participates in inline formatting.

This demonstrates that the default HTML display behavior can be changed with CSS.

---

# 23. Width and Display

Different display types behave differently when width is applied.

### Block

    .box {
        display: block;
        width: 300px;
    }

The width can be applied.

### Inline

    .text {
        display: inline;
        width: 300px;
    }

Width and height do not control the inline box in the same way as they do for block-level or inline-block boxes.

### Inline-Block

    .box {
        display: inline-block;
        width: 300px;
    }

The width can be applied while the element can remain alongside other inline-level content.

---

# 24. Box Sizing

The `box-sizing` property controls how the declared width and height are calculated.

Two important values are:

    content-box

    border-box

---

# 25. Content-Box

`content-box` is the default value.

Example:

    .box {
        box-sizing: content-box;
        width: 300px;
        padding: 20px;
        border: 5px solid black;
    }

The declared width applies to the content area.

For the horizontal dimension:

    Total width
    = content width
    + left padding
    + right padding
    + left border
    + right border

Therefore:

    300 + 20 + 20 + 5 + 5 = 350px

---

# 26. Border-Box

With `border-box`, the declared width includes content, padding, and border.

Example:

    .box {
        box-sizing: border-box;
        width: 300px;
        padding: 20px;
        border: 5px solid black;
    }

The total outer width remains:

    300px

The available content area becomes smaller to accommodate padding and border.

---

# 27. Common Box-Sizing Reset

A common CSS practice is:

    * {
        box-sizing: border-box;
    }

This makes width and height calculations easier to reason about because padding and borders are included within the declared dimensions.

---

# 28. Responsive Width

A fixed width can create horizontal overflow on small screens.

Instead of:

    width: 800px;

A responsive approach can be:

    width: 100%;
    max-width: 800px;

This means:

- The element can use available width.
- It should not exceed 800px.
- It can shrink on smaller screens.

---

# 29. Responsive Images

Images should generally be prevented from overflowing their containers.

A common pattern is:

    img {
        max-width: 100%;
        height: auto;
    }

This allows the image to scale down when necessary while preserving its aspect ratio.

---

# 30. Width, Height and Overflow

If an element has a fixed size and its content becomes larger, the content may overflow.

Example:

    .box {
        width: 300px;
        height: 100px;
    }

Overflow can be controlled with:

    overflow: visible;
    overflow: hidden;
    overflow: scroll;
    overflow: auto;

For example:

    .box {
        max-height: 200px;
        overflow: auto;
    }

---

# 31. Practical Container

A commonly useful container is:

    .container {
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
        box-sizing: border-box;
    }

This pattern creates a flexible container with a maximum width and automatic horizontal centering.

---

# 32. Practical Card Layout

Example:

    .card {
        display: inline-block;
        width: 250px;
        min-height: 180px;
        max-width: 100%;
        padding: 20px;
        box-sizing: border-box;
    }

This allows cards to have controlled dimensions while remaining flexible within smaller containers.

---

# 33. Practical Button

Example:

    .button {
        display: inline-block;
        width: auto;
        padding: 10px 20px;
    }

`inline-block` allows the button-like element to have padding and controlled dimensions while remaining inline-level.

---

# 34. Block vs Inline vs Inline-Block

| Feature | Block | Inline | Inline-Block |
|---|---|---|---|
| New line | Yes | No | No |
| Width | Supported | Does not behave like block width | Supported |
| Height | Supported | Does not behave like block height | Supported |
| Padding | Yes | Yes | Yes |
| Border | Yes | Yes | Yes |
| Useful for | Sections/containers | Text-level content | Cards/buttons |

---

# 35. Common Mistakes

### Mistake 1: Using fixed width everywhere

    width: 1200px;

This may cause horizontal scrolling on smaller screens.

Better:

    width: 100%;
    max-width: 1200px;

---

### Mistake 2: Expecting width and height to work like block boxes on inline elements

    span {
        display: inline;
        width: 300px;
        height: 200px;
    }

Inline layout does not use width and height in the same way as block or inline-block layout.

Use:

    display: inline-block;

when appropriate.

---

### Mistake 3: Forgetting box-sizing

Padding and borders can make an element larger than its declared width when using `content-box`.

A common solution is:

    box-sizing: border-box;

---

### Mistake 4: Confusing hidden methods

    display: none;

and:

    visibility: hidden;

do not have the same layout behavior.

---

# 36. Best Practices

- Use `max-width` for responsive containers.
- Avoid unnecessary fixed widths.
- Use `width: 100%` carefully with `box-sizing: border-box`.
- Use `max-width: 100%` for responsive images.
- Understand the difference between block, inline, and inline-block.
- Use `display: none` when an element should not occupy layout space.
- Use `visibility: hidden` when layout space should remain.
- Prefer `box-sizing: border-box` for predictable component sizing.
- Test layouts at different viewport widths.

---

# 37. Quick Revision

    width
    → Controls horizontal size

    height
    → Controls vertical size

    min-width
    → Minimum allowed width

    max-width
    → Maximum allowed width

    min-height
    → Minimum allowed height

    max-height
    → Maximum allowed height

    display: block
    → Block-level behavior

    display: inline
    → Inline behavior

    display: inline-block
    → Inline placement + controllable dimensions

    display: none
    → Hidden and removed from layout

    visibility: hidden
    → Hidden but layout space remains

    box-sizing: border-box
    → Width/height includes padding and border

---

# 38. Key Takeaway

The combination of **width, height, min/max dimensions, display, and box-sizing** gives CSS control over how large elements are and how they participate in the page layout.

A strong understanding of these concepts is important before learning more advanced CSS positioning and layout techniques.

---

## 🔗 Navigation

Previous: Day 026 — CSS Margin, Padding and Border

Current: Day 027 — CSS Width, Height and Display

Next: Day 028 — CSS Positioning

---

**Happy Learning! 🚀**