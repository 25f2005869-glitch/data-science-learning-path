# 📝 Day 040 — CSS Final Project and Revision Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 040  
**Topic:** CSS Final Project and Revision

---

## 1. CSS Basics

CSS controls the presentation and layout of HTML documents.

Basic syntax:

    selector {
        property: value;
    }

Example:

    p {
        color: blue;
        font-size: 18px;
    }

---

## 2. CSS Selectors

Important selectors:

- Universal selector: `*`
- Element selector: `p`
- Class selector: `.card`
- ID selector: `#header`
- Grouping selector: `h1, h2`
- Descendant selector: `section p`
- Child selector: `section > p`
- Attribute selector: `input[type="email"]`
- Pseudo-class: `a:hover`

### Specificity

Generally:

    Inline style > ID > Class/attribute/pseudo-class > Element

Avoid unnecessary use of `!important`.

---

## 3. Colors and Backgrounds

Common color formats:

- Named colors
- HEX
- RGB
- RGBA
- HSL
- HSLA

Important properties:

    color
    background-color
    background-image
    background-size
    background-position
    background-repeat
    background

Gradients can be created using:

    linear-gradient()
    radial-gradient()

---

## 4. Fonts and Text

Important font properties:

    font-family
    font-size
    font-weight
    font-style
    line-height

Important text properties:

    text-align
    text-decoration
    text-transform
    text-indent
    letter-spacing
    word-spacing
    text-shadow

Readable typography should use appropriate font sizes, spacing and contrast.

---

## 5. CSS Box Model

Every normal element consists of:

    Content
    Padding
    Border
    Margin

The most useful setting is:

    box-sizing: border-box;

With `border-box`, declared width and height include padding and border.

---

## 6. Margin, Padding and Border

### Margin

Creates space outside an element.

    margin: 20px;

### Padding

Creates space inside an element.

    padding: 20px;

### Border

Creates a visible boundary.

    border: 1px solid black;

Common shorthand:

    margin: 10px 20px;
    padding: 10px 20px;
    border-radius: 10px;

---

## 7. Width, Height and Display

Important sizing properties:

    width
    height
    min-width
    max-width
    min-height
    max-height

Important display values:

- `block`
- `inline`
- `inline-block`
- `none`

Difference:

- `display: none` removes the element from layout.
- `visibility: hidden` hides the element but keeps its layout space.

---

## 8. Position

Main position values:

- `static`
- `relative`
- `absolute`
- `fixed`
- `sticky`

Offset properties:

    top
    right
    bottom
    left

`z-index` controls stacking order when elements overlap.

A common pattern:

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
    }

---

## 9. CSS Units

### Absolute

    px
    cm
    mm
    in
    pt
    pc

### Relative

    %
    em
    rem
    vw
    vh
    vmin
    vmax
    ch

`rem` is relative to the root font size.

`em` is generally relative to the current element's font context.

Viewport units are useful for viewport-based sizing.

---

## 10. Overflow

Overflow occurs when content exceeds the available space.

Important properties:

    overflow
    overflow-x
    overflow-y

Values:

    visible
    hidden
    scroll
    auto

Text overflow can use:

    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

---

## 11. Flexbox

Flexbox is mainly useful for one-dimensional layouts.

Container:

    display: flex;

Important properties:

    flex-direction
    flex-wrap
    justify-content
    align-items
    align-content
    gap

Item properties:

    flex-grow
    flex-shrink
    flex-basis
    flex
    order

Common centering:

    display: flex;
    justify-content: center;
    align-items: center;

---

## 12. CSS Grid

Grid is useful for two-dimensional layouts.

Basic setup:

    display: grid;

Useful properties:

    grid-template-columns
    grid-template-rows
    gap
    grid-column
    grid-row

Responsive grid pattern:

    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));

---

## 13. Responsive Web Design

Responsive design allows a website to adapt to different screen sizes.

Important techniques:

- Flexible widths
- Relative units
- Flexbox
- Grid
- Media queries
- Responsive images
- Mobile-first design

A common image rule:

    img {
        max-width: 100%;
        height: auto;
    }

---

## 14. Media Queries

Media queries apply CSS based on device or viewport conditions.

Example:

    @media (min-width: 768px) {
        .container {
            max-width: 1100px;
        }
    }

Mobile-first design starts with the small-screen layout and adds styles for larger screens.

---

## 15. Transitions

Transitions create smooth changes between CSS states.

Important properties:

    transition-property
    transition-duration
    transition-timing-function
    transition-delay

Shorthand:

    transition: transform 0.3s ease;

---

## 16. Transforms

Common transforms:

    translate()
    scale()
    rotate()

Example:

    transform: translateY(-5px);

Transforms are commonly combined with transitions for hover effects.

---

## 17. Animations

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

Important properties:

    animation-name
    animation-duration
    animation-delay
    animation-iteration-count
    animation-direction
    animation-fill-mode
    animation-play-state

---

## 18. Responsive Navbar

A responsive navbar commonly contains:

- Logo
- Navigation links
- Flexbox
- Media queries
- Hover states
- Focus states

On small screens, navigation links can be arranged vertically.

---

## 19. Responsive Cards

Cards should avoid unnecessary fixed dimensions.

Useful pattern:

    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;

Cards can use Flexbox internally for consistent alignment.

---

## 20. CSS Best Practices

- Use meaningful class names.
- Prefer reusable classes.
- Use semantic HTML.
- Keep CSS organized.
- Avoid excessive `!important`.
- Avoid unnecessary fixed widths.
- Use responsive units where appropriate.
- Maintain readable spacing.
- Ensure sufficient color contrast.
- Include visible focus states.
- Test different screen sizes.
- Respect reduced-motion preferences.

---

## 21. Final CSS Mental Model

Think of CSS in layers:

1. Select the element.
2. Set colors and typography.
3. Apply the box model.
4. Control display and sizing.
5. Choose layout using Flexbox or Grid.
6. Position special elements when necessary.
7. Make the layout responsive.
8. Add transitions and animations.
9. Test accessibility and responsiveness.

---

## 22. Final Project Architecture

The final project combines:

    HTML
      ↓
    CSS selectors
      ↓
    Box model
      ↓
    Flexbox + Grid
      ↓
    Responsive design
      ↓
    Media queries
      ↓
    Transitions + animations
      ↓
    Accessible responsive interface

---

## 📌 Final Revision Goal

By the end of Day 040, I should be able to create a responsive webpage from scratch using CSS without depending completely on copied code.