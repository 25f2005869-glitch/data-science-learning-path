# 📘 Day 029 — CSS Units and Overflow — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 029  
**Topic:** CSS Units and Overflow

---

## 1. Introduction

CSS units define the size of elements, spacing, fonts, and other properties.

CSS overflow controls what happens when content becomes larger than the available space.

---

# 📏 2. CSS Units

CSS units are mainly divided into:

- Absolute units
- Relative units

---

## 3. Absolute Units

Absolute units represent fixed physical or screen-related sizes.

Common units:

    px
    cm
    mm
    in
    pt
    pc

The most commonly used absolute unit in web development is:

    px

Example:

    .box {
        width: 300px;
    }

---

# 4. Relative Units

Relative units depend on another value such as the parent element, root font size, or viewport.

Common relative units:

    %
    em
    rem
    vw
    vh
    vmin
    vmax
    ch

Relative units are especially useful for responsive designs.

---

# 5. Pixels — px

`px` represents CSS pixels.

Example:

    .box {
        width: 300px;
        padding: 20px;
    }

Advantages:

- Easy to understand
- Useful for borders and precise component sizes

Limitation:

- Fixed values may be less flexible for responsive layouts.

---

# 6. Percentage — %

Percentage values are generally calculated relative to a relevant containing value.

Example:

    .container {
        width: 80%;
    }

If the containing block is 1000px wide, an 80% width is approximately 800px.

Percentages are commonly used for:

- Width
- Layouts
- Flexible containers

---

# 7. em

`em` is relative to the font size of the relevant element or its inherited context, depending on the property.

Example:

    .text {
        font-size: 2em;
    }

For font sizing, `em` can compound when nested elements inherit and multiply relative font sizes.

`em` is also commonly used for spacing relative to an element's font size.

---

# 8. rem

`rem` means "root em".

It is relative to the root element's font size, usually the `<html>` element.

Example:

    html {
        font-size: 16px;
    }

    .text {
        font-size: 2rem;
    }

The resulting font size is 32px.

Because `rem` is based on the root font size, it is generally easier to manage consistently than deeply nested `em` values.

---

# 9. em vs rem

| Unit | Relative To |
|---|---|
| `em` | Relevant element's font size/context |
| `rem` | Root element's font size |

Quick memory:

    em
    → Element/context based

    rem
    → Root based

---

# 10. Viewport Units

Viewport units are based on the browser viewport.

Main viewport units:

    vw
    vh
    vmin
    vmax

---

## 11. vw

`vw` means viewport width.

    1vw = 1% of the viewport width

Example:

    .box {
        width: 50vw;
    }

The width changes as the viewport width changes.

---

# 12. vh

`vh` means viewport height.

    1vh = 1% of the viewport height

Example:

    .hero {
        min-height: 50vh;
    }

This can make a section adapt to the viewport height.

---

# 13. vmin

`vmin` represents 1% of the smaller viewport dimension.

It uses the smaller value between viewport width and viewport height.

Example:

    width: 50vmin;

---

# 14. vmax

`vmax` represents 1% of the larger viewport dimension.

Example:

    width: 50vmax;

---

# 15. ch

`ch` is approximately based on the width of the `0` character of the element's font.

Example:

    .paragraph {
        max-width: 65ch;
    }

It is commonly useful for controlling readable text line lengths.

---

# 16. Unitless Values

Some CSS properties can accept values without units.

Example:

    line-height: 1.5;

Unitless values are especially useful for properties such as:

    line-height
    z-index
    font-weight

---

# 17. Zero Values

The value `0` normally does not require a unit.

Example:

    margin: 0;
    padding: 0;
    top: 0;

Instead of:

    margin: 0px;

you can normally write:

    margin: 0;

---

# 18. Choosing CSS Units

Use units according to the requirement.

### `px`

Useful for:

- Borders
- Small fixed dimensions
- Precise component details

### `%`

Useful for:

- Flexible widths
- Parent-relative layouts

### `rem`

Useful for:

- Font sizes
- Consistent spacing
- Scalable layouts

### `em`

Useful when sizing should relate to an element's font size.

### `vw` and `vh`

Useful for:

- Viewport-based sections
- Responsive sizing

---

# 🌊 19. CSS Overflow

Overflow occurs when content is larger than the available space of an element.

Example:

    .box {
        width: 200px;
        height: 100px;
    }

If the content is larger than this area, it can overflow.

---

# 20. The Overflow Property

The `overflow` property controls how overflowing content is handled.

Common values:

    overflow: visible;
    overflow: hidden;
    overflow: scroll;
    overflow: auto;

---

# 21. Overflow Visible

`visible` is the default behavior.

Example:

    .box {
        overflow: visible;
    }

Content can extend outside the element's box.

---

# 22. Overflow Hidden

Example:

    .box {
        overflow: hidden;
    }

Overflowing content is clipped and does not extend outside the element's box.

This can be useful for:

- Cropping images
- Hiding unwanted overflow
- Rounded containers

---

# 23. Overflow Scroll

Example:

    .box {
        overflow: scroll;
    }

The element provides scrolling mechanisms for overflowing content.

Depending on the browser and content, scrollbars may be shown even when they are not strictly needed.

---

# 24. Overflow Auto

Example:

    .box {
        overflow: auto;
    }

The browser provides scrolling when the content actually overflows.

This is often more convenient than always forcing scrollbars.

---

# 25. Overflow-X

`overflow-x` controls horizontal overflow.

Example:

    .container {
        overflow-x: auto;
    }

This is useful for wide content such as tables or code-like content.

---

# 26. Overflow-Y

`overflow-y` controls vertical overflow.

Example:

    .container {
        overflow-y: auto;
    }

This can create a vertically scrollable area.

---

# 27. Horizontal and Vertical Overflow Together

Example:

    .container {
        width: 300px;
        height: 200px;
        overflow-x: auto;
        overflow-y: auto;
    }

Both horizontal and vertical overflow can be handled independently.

---

# 28. Text Overflow

Long text can exceed the available width.

CSS provides:

    text-overflow

It is commonly combined with:

    overflow: hidden;
    white-space: nowrap;

Example:

    .title {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

This can display truncated text with an ellipsis when the necessary conditions are met.

---

# 29. White Space

The `white-space` property controls how spaces and line breaks are handled.

Example:

    white-space: nowrap;

`nowrap` prevents normal text wrapping.

This is often used with `text-overflow: ellipsis`.

---

# 30. Overflow Wrap

`overflow-wrap` allows long words or strings to break when necessary.

Example:

    .text {
        overflow-wrap: break-word;
    }

This can help prevent long URLs or unbroken strings from causing horizontal overflow.

---

# 31. Word Break

`word-break` controls how words can break across lines.

Example:

    .text {
        word-break: break-word;
    }

Use appropriate values according to the text and language requirements.

---

# 32. Scrollable Container

A common pattern is:

    .content {
        width: 300px;
        height: 200px;
        overflow: auto;
    }

When content becomes larger than the available area, scrolling can be used to access it.

---

# 33. Responsive Container

A responsive container can combine relative units and maximum dimensions.

Example:

    .container {
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
        box-sizing: border-box;
    }

This allows the container to adapt to different screen sizes.

---

# 34. Responsive Image

A common responsive image pattern is:

    img {
        max-width: 100%;
        height: auto;
    }

This prevents the image from becoming wider than its containing area while maintaining its aspect ratio.

---

# 35. Common Overflow Problem

A fixed-width element can cause horizontal scrolling.

Example:

    .box {
        width: 1200px;
    }

On a smaller screen, this may exceed the viewport.

A more flexible approach is:

    .box {
        width: 100%;
        max-width: 1200px;
    }

---

# 36. Overflow and Border Radius

When content or images should stay inside rounded corners, this pattern is often useful:

    .card {
        border-radius: 12px;
        overflow: hidden;
    }

The overflow is clipped to the element's box.

---

# 37. Common Mistakes

### Mistake 1: Using fixed widths everywhere

    width: 1200px;

This can cause horizontal overflow on small screens.

Prefer flexible sizing where appropriate.

---

### Mistake 2: Forgetting long text

Very long URLs or strings can create unexpected horizontal overflow.

Useful properties include:

    overflow-wrap
    word-break

---

### Mistake 3: Using `overflow: hidden` without understanding its effect

It clips overflowing content and can hide content that users need to access.

Use it intentionally.

---

### Mistake 4: Using viewport units for everything

`vw` and `vh` are useful, but excessive use can produce awkward sizing across different screens.

Choose units based on the component's purpose.

---

# 38. Best Practices

- Use relative units for flexible layouts.
- Use `rem` when consistent root-based sizing is useful.
- Use `%` for parent-relative dimensions.
- Use `vw` and `vh` when viewport-based sizing is appropriate.
- Use `max-width` to prevent oversized containers.
- Use `overflow: auto` for content that may need scrolling.
- Handle long text and URLs carefully.
- Use responsive image rules.
- Test layouts on different screen sizes.

---

# 39. Quick Comparison

| Unit | Based On | Common Use |
|---|---|---|
| `px` | CSS pixel | Borders, precise sizes |
| `%` | Relevant containing value | Flexible layouts |
| `em` | Element/context font size | Relative component sizing |
| `rem` | Root font size | Scalable typography/spacing |
| `vw` | Viewport width | Viewport-based sizing |
| `vh` | Viewport height | Viewport-based sizing |
| `vmin` | Smaller viewport dimension | Responsive sizing |
| `vmax` | Larger viewport dimension | Responsive sizing |
| `ch` | Character width approximation | Text line length |

---

# 40. Overflow Quick Reference

    overflow: visible;
    → Content can extend outside

    overflow: hidden;
    → Overflow is clipped

    overflow: scroll;
    → Scrolling mechanism is provided

    overflow: auto;
    → Scrolling is provided when needed

    overflow-x
    → Horizontal overflow

    overflow-y
    → Vertical overflow

---

# 41. Key Takeaway

CSS units control **how large elements are**, while overflow properties control **what happens when content does not fit**.

For responsive web development, commonly useful choices include:

    %
    rem
    em
    vw
    vh
    max-width
    overflow: auto

Choosing the correct unit and overflow behavior helps create flexible and user-friendly layouts.

---

## 🔗 Navigation

Previous: Day 028 — CSS Position and Z-Index

Current: Day 029 — CSS Units and Overflow

Next: Day 030 — CSS Flexbox Basics

---

**Happy Learning! 🚀**