# 🎨 Day 097 — CSS Complete Revision Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 097  
**Topic:** CSS Complete Revision

---

# 1. What is CSS?

CSS stands for **Cascading Style Sheets**.

CSS controls the presentation and visual layout of HTML content.

CSS can control:

- Colors
- Fonts
- Spacing
- Borders
- Sizes
- Layout
- Positioning
- Responsive behavior
- Transitions
- Animations

Basic mental model:

    HTML → Structure
    CSS → Presentation
    JavaScript → Behavior

---

# 2. CSS Syntax

Basic CSS syntax:

    selector {
        property: value;
    }

Example:

    p {
        color: blue;
        font-size: 18px;
    }

A CSS declaration consists of:

    property + value

A declaration block contains one or more declarations.

---

# 3. Ways to Add CSS

## Inline CSS

    <p style="color: blue;">Hello</p>

## Internal CSS

    <style>
        p {
            color: blue;
        }
    </style>

## External CSS

    <link rel="stylesheet" href="style.css">

External CSS is generally preferred for larger projects because it improves organization and reuse.

---

# 4. CSS Selectors

Selectors determine which HTML elements receive styles.

## Universal Selector

    *

Selects all elements.

## Element Selector

    p

Selects all paragraphs.

## Class Selector

    .student

Selects elements with the class `student`.

## ID Selector

    #profile

Selects the element with the specified ID.

## Grouping Selector

    h1, h2, h3

Styles multiple selectors together.

---

# 5. Combinators

## Descendant

    section p

Selects paragraphs inside a section.

## Child

    section > p

Selects direct child paragraphs.

## Adjacent Sibling

    h2 + p

Selects the paragraph immediately following an `h2`.

## General Sibling

    h2 ~ p

Selects following sibling paragraphs.

---

# 6. Attribute Selectors

Examples:

    [required]

    [type="email"]

    [href^="https"]

    [src$=".png"]

    [href*="github"]

Attribute selectors are useful when styles depend on attributes.

---

# 7. Pseudo-Classes

Common pseudo-classes:

    :hover
    :focus
    :focus-visible
    :first-child
    :last-child
    :nth-child()
    :checked
    :disabled

Example:

    button:hover {
        ...
    }

Pseudo-classes represent a state or condition of an element.

---

# 8. Specificity

When multiple rules target the same element, specificity helps determine which rule has greater priority.

General order:

    Inline styles
    ID selectors
    Class / attribute / pseudo-class selectors
    Element / pseudo-element selectors

Specificity is not the only factor. Cascade order and `!important` also affect the final result.

Avoid unnecessary `!important`.

---

# 9. Colors

CSS supports multiple color formats.

Examples:

    color: red;

    color: #2563eb;

    color: rgb(37, 99, 235);

    color: rgba(37, 99, 235, 0.8);

    color: hsl(217, 83%, 53%);

Choose colors with sufficient contrast for readability and accessibility.

---

# 10. Backgrounds

Important properties:

    background-color
    background-image
    background-repeat
    background-position
    background-size
    background-attachment

Example:

    background-size: cover;

Gradients can also be used.

Example:

    background: linear-gradient(to right, #111827, #2563eb);

---

# 11. Fonts

Important font properties:

    font-family
    font-size
    font-weight
    font-style
    font-variant
    line-height

Example:

    body {
        font-family: Arial, sans-serif;
    }

Use fallback fonts when defining a font stack.

---

# 12. Text Styling

Important properties:

    text-align
    text-decoration
    text-transform
    text-indent
    letter-spacing
    word-spacing
    text-shadow

Readable text should have:

- Appropriate font size
- Suitable line height
- Good contrast
- Reasonable line length

---

# 13. CSS Box Model

Every normal CSS box consists conceptually of:

    Content
       ↓
    Padding
       ↓
    Border
       ↓
    Margin

The box model is fundamental to understanding spacing and dimensions.

---

# 14. Padding

Padding is the space between the content and border.

Example:

    padding: 20px;

Four-side shorthand:

    padding: 10px 20px 15px 25px;

Order:

    top
    right
    bottom
    left

---

# 15. Margin

Margin creates space outside an element's border.

Example:

    margin: 20px;

Centering a block with a defined or constrained width:

    margin: 0 auto;

Margins can sometimes collapse vertically between block elements.

---

# 16. Border

Important properties:

    border-width
    border-style
    border-color
    border-radius

Shorthand:

    border: 1px solid black;

Rounded corners:

    border-radius: 10px;

A circle can be created for a square element using:

    border-radius: 50%;

---

# 17. Box Sizing

Default behavior is generally:

    box-sizing: content-box;

A common project-wide approach is:

    *,
    *::before,
    *::after {
        box-sizing: border-box;
    }

With `border-box`, declared width and height include padding and border.

---

# 18. Width and Height

Important properties:

    width
    height
    min-width
    max-width
    min-height
    max-height

Responsive designs commonly use:

    max-width: 100%;

for images and other content that should not overflow their container.

---

# 19. Display

Common values:

    block
    inline
    inline-block
    none

### Block

Usually starts on a new line and can accept width and height.

### Inline

Usually remains within the text flow and does not behave like a block for width and height.

### Inline-block

Combines characteristics of inline flow with the ability to set dimensions.

### None

Removes the element from the layout.

---

# 20. Visibility

    visibility: hidden;

The element becomes invisible but continues to occupy layout space.

Difference:

    display: none;
    → removed from layout

    visibility: hidden;
    → hidden but layout space remains

---

# 21. CSS Units

## Absolute Units

Examples:

    px
    cm
    mm
    in
    pt
    pc

## Relative Units

Examples:

    %
    em
    rem
    vw
    vh
    vmin
    vmax
    ch

### rem

Relative to the root element's font size.

### em

Generally relative to the font size of the relevant element or inherited context.

### vw

One percent of viewport width.

### vh

One percent of viewport height.

Use units according to the design requirement.

---

# 22. Overflow

Overflow occurs when content is larger than its containing box.

Properties:

    overflow
    overflow-x
    overflow-y

Values:

    visible
    hidden
    scroll
    auto

For text truncation, common properties include:

    white-space
    overflow
    text-overflow

---

# 23. Position

The main position values are:

    static
    relative
    absolute
    fixed
    sticky

### Static

Normal positioning.

### Relative

Remains in normal flow but can be visually offset.

### Absolute

Removed from normal flow and positioned relative to a suitable containing block.

### Fixed

Positioned relative to the viewport in typical cases.

### Sticky

Behaves relatively until a threshold is reached, then sticks within its scrolling context.

---

# 24. Positioning Properties

Common properties:

    top
    right
    bottom
    left

These are generally used with positioned elements.

---

# 25. Z-Index

`z-index` controls stacking order when elements overlap and the relevant stacking contexts permit comparison.

Example:

    .card {
        position: relative;
        z-index: 2;
    }

A higher value does not automatically escape a different stacking context.

---

# 26. Flexbox

Flexbox is primarily a one-dimensional layout system.

Enable it:

    display: flex;

Important properties for the flex container:

    flex-direction
    justify-content
    align-items
    align-content
    flex-wrap
    gap

Important properties for flex items:

    flex
    flex-grow
    flex-shrink
    flex-basis
    order
    align-self

---

# 27. Main Axis and Cross Axis

Flexbox has:

    Main Axis
    Cross Axis

For:

    flex-direction: row;

the main axis is horizontal.

For:

    flex-direction: column;

the main axis is vertical.

---

# 28. justify-content and align-items

`justify-content` distributes items along the main axis.

Examples:

    center
    space-between
    space-around
    space-evenly

`align-items` aligns items along the cross axis.

Example:

    align-items: center;

---

# 29. Flex Wrapping

Use:

    flex-wrap: wrap;

when items should move onto additional lines when necessary.

Use:

    gap: 20px;

to create consistent spacing between flex items.

---

# 30. CSS Grid

CSS Grid is a two-dimensional layout system.

Enable it:

    display: grid;

Important properties:

    grid-template-columns
    grid-template-rows
    gap
    column-gap
    row-gap
    grid-column
    grid-row

---

# 31. Responsive Grid

A useful pattern is:

    grid-template-columns:
        repeat(auto-fit, minmax(250px, 1fr));

This allows columns to adapt to available space.

Other useful values:

    auto-fit
    auto-fill
    minmax()

---

# 32. Grid Placement

An item can span columns:

    grid-column: span 2;

Or rows:

    grid-row: span 2;

Grid is useful for dashboards, card layouts, galleries, and page structures.

---

# 33. Responsive Web Design

Responsive design means the interface adapts to different screen sizes and devices.

Important techniques:

- Flexible layouts
- Relative units
- Flexbox
- Grid
- Media queries
- Responsive images
- Mobile-first design

---

# 34. Viewport Meta Tag

Responsive webpages should include:

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

This helps browsers use the device viewport appropriately.

---

# 35. Mobile-First Design

Mobile-first means designing the base layout for smaller screens first and progressively enhancing it for larger screens.

Example:

    Base → Mobile
    Media query → Tablet
    Media query → Desktop

This approach often keeps responsive CSS easier to manage.

---

# 36. Media Queries

Media queries apply CSS based on conditions.

Example:

    @media (max-width: 600px) {
        ...
    }

Common features:

    min-width
    max-width
    min-height
    max-height
    orientation

Media queries can also target print and user preferences.

---

# 37. Breakpoints

Breakpoints are screen sizes where the layout changes.

Do not choose breakpoints only because a particular device has that width.

Choose breakpoints based on where the content or layout needs adjustment.

---

# 38. Transitions

Transitions create smooth changes between property values.

Important properties:

    transition-property
    transition-duration
    transition-timing-function
    transition-delay

Shorthand:

    transition: transform 0.3s ease;

---

# 39. Transform

Common transforms:

    translate()
    scale()
    rotate()

Example:

    transform: scale(1.05);

Transforms can often be animated efficiently without changing document layout.

---

# 40. Animations

CSS animations use `@keyframes`.

Example structure:

    @keyframes slide {
        from {
            transform: translateX(0);
        }

        to {
            transform: translateX(100px);
        }
    }

Important animation properties:

    animation-name
    animation-duration
    animation-delay
    animation-iteration-count
    animation-direction
    animation-fill-mode
    animation-play-state

---

# 41. Transition vs Animation

### Transition

Usually occurs between two states.

Example:

    normal → hover

### Animation

Can contain multiple stages defined with keyframes.

Example:

    0% → 50% → 100%

---

# 42. Responsive Navigation

A responsive navigation system commonly uses:

- Semantic `<nav>`
- Flexbox
- Media queries
- Accessible links
- Hover/focus states
- Mobile layout

Always ensure navigation remains usable with keyboard interaction.

---

# 43. Responsive Cards

Cards can be arranged with Grid or Flexbox.

A responsive grid can use:

    repeat(auto-fit, minmax(250px, 1fr))

Avoid unnecessarily fixed widths that cause horizontal scrolling.

---

# 44. Accessibility and CSS

Good CSS should support accessibility.

Important practices:

- Maintain sufficient contrast.
- Keep focus indicators visible.
- Do not rely only on hover.
- Make controls touch-friendly.
- Support keyboard navigation.
- Respect reduced-motion preferences.

Example:

    @media (prefers-reduced-motion: reduce) {
        * {
            animation-duration: 0.01ms;
            transition-duration: 0.01ms;
        }
    }

---

# 45. CSS Best Practices

- Use external stylesheets for larger projects.
- Prefer classes for reusable styling.
- Avoid unnecessary IDs for styling.
- Keep specificity manageable.
- Use meaningful class names.
- Group related styles.
- Use responsive layouts.
- Avoid excessive `!important`.
- Avoid unnecessary fixed dimensions.
- Keep CSS organized.
- Remove unused styles.
- Test different screen sizes.
- Consider accessibility.

---

# 46. Final CSS Revision Checklist

- [ ] CSS syntax
- [ ] Selectors
- [ ] Specificity
- [ ] Colors
- [ ] Backgrounds
- [ ] Fonts
- [ ] Text styling
- [ ] Box model
- [ ] Margin
- [ ] Padding
- [ ] Border
- [ ] Width and height
- [ ] Display
- [ ] Units
- [ ] Overflow
- [ ] Position
- [ ] Z-index
- [ ] Flexbox
- [ ] Grid
- [ ] Responsive design
- [ ] Media queries
- [ ] Transitions
- [ ] Animations
- [ ] Responsive navigation
- [ ] Responsive cards
- [ ] Accessibility
- [ ] Best practices

---

# 47. Final Takeaway

CSS controls how structured HTML content looks, behaves spatially, and adapts to different screen sizes.

A strong CSS implementation should be:

**Clean + Responsive + Maintainable + Accessible + Consistent**