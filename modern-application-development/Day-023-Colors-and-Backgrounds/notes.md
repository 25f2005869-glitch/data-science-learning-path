
## `notes.md`

```markdown
# 📚 Day 023 — CSS Colors and Backgrounds Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. Introduction

Colors are used to control the visual appearance of text, borders, backgrounds, and other elements.

CSS provides several ways to represent colors.

The most common formats are:

- Named colors
- HEX
- RGB
- RGBA
- HSL
- HSLA

---

# 2. The color Property

The `color` property changes the foreground color, usually the text color.

Example:

    p {
        color: blue;
    }

This makes the paragraph text blue.

---

# 3. Named Colors

CSS provides predefined color names.

Examples:

    color: red;

    color: blue;

    color: green;

    color: black;

    color: white;

    color: orange;

Named colors are easy to understand but provide limited choices compared with other color formats.

---

# 4. HEX Colors

HEX stands for hexadecimal.

A common HEX color uses six hexadecimal digits after `#`.

Example:

    color: #ff0000;

This represents red.

Another example:

    color: #0000ff;

This represents blue.

Another example:

    color: #00ff00;

This represents green.

---

# 5. HEX Structure

A six-digit HEX color can be understood as:

    #RRGGBB

Where:

    RR → Red

    GG → Green

    BB → Blue

Each pair represents the intensity of that color component.

---

# 6. RGB Colors

RGB stands for:

    Red
    Green
    Blue

Example:

    color: rgb(255, 0, 0);

This represents red.

Another example:

    color: rgb(0, 0, 255);

This represents blue.

RGB values normally range from 0 to 255.

---

# 7. RGBA Colors

RGBA adds an alpha channel to RGB.

RGBA means:

    Red
    Green
    Blue
    Alpha

Example:

    color: rgba(255, 0, 0, 0.5);

The alpha value controls transparency.

An alpha value of:

    1

means fully opaque.

An alpha value of:

    0

means fully transparent.

A value such as:

    0.5

means partially transparent.

---

# 8. HSL Colors

HSL stands for:

    Hue
    Saturation
    Lightness

Example:

    color: hsl(0, 100%, 50%);

This represents a red color.

HSL can be useful when working with color variations based on hue, saturation, and lightness.

---

# 9. HSLA Colors

HSLA adds an alpha channel to HSL.

Example:

    color: hsla(0, 100%, 50%, 0.5);

The final value controls transparency.

---

# 10. Color Format Comparison

| Format | Example |
|---|---|
| Named | `red` |
| HEX | `#ff0000` |
| RGB | `rgb(255, 0, 0)` |
| RGBA | `rgba(255, 0, 0, 0.5)` |
| HSL | `hsl(0, 100%, 50%)` |
| HSLA | `hsla(0, 100%, 50%, 0.5)` |

---

# 11. Background Color

The `background-color` property changes the background color of an element.

Example:

    body {
        background-color: #f4f6f8;
    }

Another example:

    section {
        background-color: lightblue;
    }

---

# 12. Background Image

The `background-image` property adds an image as an element's background.

Example:

    body {
        background-image: url("background.jpg");
    }

The image becomes part of the element's background.

---

# 13. Background Repeat

By default, background images may repeat depending on the image and CSS settings.

The `background-repeat` property controls repetition.

Example:

    body {
        background-repeat: no-repeat;
    }

Common values:

    repeat

    repeat-x

    repeat-y

    no-repeat

---

# 14. Background Position

The `background-position` property controls where the background image appears.

Example:

    body {
        background-position: center;
    }

Other common values include:

    top

    bottom

    left

    right

    center

---

# 15. Background Size

The `background-size` property controls the size of a background image.

Example:

    body {
        background-size: cover;
    }

Important values:

### cover

The image covers the entire element.

Some parts of the image may be cropped.

### contain

The complete image fits inside the element.

Empty space may remain.

Example:

    background-size: contain;

---

# 16. Background Attachment

The `background-attachment` property controls how the background behaves when the page scrolls.

Example:

    body {
        background-attachment: fixed;
    }

Common values:

    scroll

    fixed

---

# 17. Background Shorthand

Multiple background properties can be combined using the `background` shorthand.

Example:

    body {
        background:
            #f4f6f8
            url("background.jpg")
            no-repeat
            center
            / cover;
    }

This can define multiple background settings in one declaration.

---

# 18. Linear Gradient

A linear gradient creates a gradual transition between colors.

Example:

    background: linear-gradient(
        to right,
        blue,
        purple
    );

The gradient changes from one color to another along a direction.

---

# 19. Linear Gradient Direction

Example:

    background: linear-gradient(
        to bottom,
        blue,
        white
    );

Other directions include:

    to right

    to left

    to top

    to bottom

Angles can also be used.

Example:

    background: linear-gradient(
        45deg,
        blue,
        purple
    );

---

# 20. Multiple Gradient Colors

A gradient can contain multiple colors.

Example:

    background: linear-gradient(
        to right,
        blue,
        purple,
        pink
    );

---

# 21. Radial Gradient

A radial gradient spreads outward from a central point.

Example:

    background: radial-gradient(
        circle,
        blue,
        white
    );

---

# 22. Transparency

Transparency allows the background behind an element to remain partially visible.

RGBA can be used for transparency.

Example:

    background-color: rgba(0, 0, 0, 0.5);

The final value controls the transparency level.

---

# 23. Color Contrast

Text should have sufficient contrast with its background.

Poor contrast makes text difficult to read.

Example of poor design:

    color: lightgray;
    background-color: white;

A darker text color is generally easier to read.

---

# 24. Background Image and Readability

When text is placed over a background image, readability must be considered.

A background image with high visual complexity can make text difficult to read.

Possible solutions include:

- Choosing a simpler image.
- Using a suitable overlay.
- Using a solid background.
- Using sufficient contrast.

---

# 25. Multiple Backgrounds

CSS can use multiple background layers.

Example:

    background-image:
        url("foreground.png"),
        url("background.jpg");

The first background is generally placed above the next background layer.

---

# 26. Background vs Image Element

There is an important difference between:

    <img>

and:

    background-image

Use `<img>` when the image is meaningful content.

Use `background-image` when the image is primarily decorative.

---

# 27. Color Best Practices

Follow these practices:

1. Use consistent colors.
2. Maintain good text contrast.
3. Avoid excessive colors.
4. Use readable text.
5. Use semantic HTML.
6. Use meaningful images as `<img>` elements.
7. Use background images for decorative purposes.
8. Test the page on different screen sizes.

---

# 28. Example CSS

    h1 {
        color: #1f4e79;
        background-color: #dbeafe;
    }

    section {
        background-color: white;
    }

    .gradient {
        background: linear-gradient(
            to right,
            #2563eb,
            #7c3aed
        );
    }

---

# 29. Important Properties

| Property | Purpose |
|---|---|
| `color` | Text/foreground color |
| `background-color` | Background color |
| `background-image` | Background image |
| `background-repeat` | Image repetition |
| `background-position` | Image position |
| `background-size` | Image size |
| `background-attachment` | Background scrolling behavior |
| `background` | Shorthand |

---

# 30. Final Mental Model

Think of CSS backgrounds like layers:

    Element
       ↓
    Background Color
       ↓
    Background Image
       ↓
    Gradient / Additional Background
       ↓
    Content

---

# 31. Final Revision

Remember:

    color
        → text/foreground color

    background-color
        → background color

    background-image
        → background image

    background-repeat
        → repetition

    background-position
        → position

    background-size
        → size

    background-attachment
        → scrolling behavior

    linear-gradient()
        → linear color transition

    radial-gradient()
        → radial color transition

---

**End of Day 023 Notes**