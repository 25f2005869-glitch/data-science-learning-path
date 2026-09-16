
## 2. `notes.md`

```markdown
# ✍️ Day 024 — Fonts and Text Styling Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 1. Introduction

Typography is an important part of web design.

CSS provides several properties that control how text looks and how easily users can read it.

Two major groups are:

1. Font properties
2. Text properties

---

# 2. Font Properties

## 2.1 `font-family`

The `font-family` property specifies the font used for text.

Example:

    p {
        font-family: Arial, sans-serif;
    }

A list of fonts can be provided as a fallback.

Example:

    font-family: "Trebuchet MS", Arial, sans-serif;

The browser tries the first available font.

---

## 2.2 Generic Font Families

CSS provides generic font families.

### Serif

Serif fonts have small decorative strokes.

Example:

    font-family: Georgia, serif;

### Sans-serif

Sans-serif fonts do not have decorative strokes.

Example:

    font-family: Arial, sans-serif;

### Monospace

Every character has approximately the same width.

Example:

    font-family: "Courier New", monospace;

### Cursive

Designed to resemble handwriting.

Example:

    font-family: cursive;

### Fantasy

Decorative fonts.

Example:

    font-family: fantasy;

---

# 3. Font Size

The `font-size` property controls the size of text.

Example:

    p {
        font-size: 18px;
    }

Common units:

- `px`
- `em`
- `rem`
- `%`
- `vw`

Example:

    h1 {
        font-size: 2rem;
    }

`rem` is commonly useful for scalable typography.

---

# 4. Font Weight

The `font-weight` property controls how thick the characters appear.

Examples:

    font-weight: normal;
    font-weight: bold;

Numeric values can also be used:

    font-weight: 400;
    font-weight: 500;
    font-weight: 700;

Typical values:

| Value | Meaning |
|---|---|
| 100 | Very thin |
| 400 | Normal |
| 500 | Medium |
| 700 | Bold |
| 900 | Very bold |

Not every font supports every weight.

---

# 5. Font Style

The `font-style` property controls whether text is normal, italic, or oblique.

Example:

    font-style: italic;

Common values:

- `normal`
- `italic`
- `oblique`

---

# 6. Font Variant

The `font-variant` property can display text using small capitals.

Example:

    font-variant: small-caps;

---

# 7. Line Height

The `line-height` property controls the vertical space between lines.

Example:

    p {
        line-height: 1.6;
    }

A larger line height can improve readability.

For normal body text, a value around `1.4` to `1.8` is often comfortable.

---

# 8. Text Alignment

The `text-align` property controls horizontal alignment.

Examples:

    text-align: left;
    text-align: center;
    text-align: right;
    text-align: justify;

Example:

    h1 {
        text-align: center;
    }

---

# 9. Text Decoration

The `text-decoration` property adds decoration to text.

Examples:

    text-decoration: underline;
    text-decoration: overline;
    text-decoration: line-through;
    text-decoration: none;

Links commonly use:

    text-decoration: none;

---

# 10. Text Transformation

The `text-transform` property changes the visual capitalization of text.

Examples:

    text-transform: uppercase;
    text-transform: lowercase;
    text-transform: capitalize;
    text-transform: none;

Important:

`text-transform` changes presentation, not the actual HTML text content.

---

# 11. Text Indentation

The `text-indent` property adds indentation to the first line of a paragraph.

Example:

    p {
        text-indent: 30px;
    }

---

# 12. Letter Spacing

The `letter-spacing` property controls the space between characters.

Example:

    h2 {
        letter-spacing: 2px;
    }

Negative values are also possible:

    letter-spacing: -0.5px;

Use excessive letter spacing carefully because it can reduce readability.

---

# 13. Word Spacing

The `word-spacing` property controls the space between words.

Example:

    p {
        word-spacing: 8px;
    }

---

# 14. Text Shadow

The `text-shadow` property adds a shadow behind text.

Syntax:

    text-shadow: horizontal vertical blur color;

Example:

    h1 {
        text-shadow: 2px 2px 4px gray;
    }

The values represent:

- Horizontal offset
- Vertical offset
- Blur radius
- Shadow color

---

# 15. Font Shorthand

CSS provides the `font` shorthand property.

Example:

    font: italic bold 20px Arial, sans-serif;

The shorthand can combine properties such as:

- `font-style`
- `font-weight`
- `font-size`
- `line-height`
- `font-family`

Example:

    font: 700 18px/1.6 Arial, sans-serif;

Here:

- `700` = font weight
- `18px` = font size
- `1.6` = line height
- `Arial, sans-serif` = font family

---

# 16. Font Stack

A font stack provides multiple font choices.

Example:

    font-family: Arial, Helvetica, sans-serif;

The browser uses the first available font.

This provides a fallback mechanism.

---

# 17. Web-Safe Fonts

Web-safe fonts are fonts that are commonly available across operating systems.

Examples include:

- Arial
- Helvetica
- Georgia
- Times New Roman
- Courier New
- Verdana
- Tahoma

Using fallback fonts is still important.

Example:

    font-family: Arial, Helvetica, sans-serif;

---

# 18. Readability

Good typography should be easy to read.

Important considerations:

- Use an appropriate font size.
- Maintain sufficient line height.
- Avoid excessive letter spacing.
- Use good color contrast.
- Avoid decorative fonts for long paragraphs.
- Maintain a clear heading hierarchy.
- Avoid unnecessary text effects.

---

# 19. Accessibility

Typography should support accessibility.

Good practices include:

- Use readable font sizes.
- Maintain sufficient contrast.
- Do not communicate information only through font style.
- Keep headings structured.
- Avoid excessive uppercase text.
- Use semantic HTML headings.

---

# 20. Font vs Text Properties

### Font Properties

These primarily control the appearance of characters.

Examples:

- `font-family`
- `font-size`
- `font-weight`
- `font-style`
- `font-variant`

### Text Properties

These primarily control text layout and decoration.

Examples:

- `text-align`
- `text-decoration`
- `text-transform`
- `text-indent`
- `letter-spacing`
- `word-spacing`
- `text-shadow`
- `line-height`

---

# 21. Example

    h1 {
        font-family: Georgia, serif;
        font-size: 36px;
        font-weight: 700;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px gray;
    }

---

# 22. Key Takeaways

- `font-family` selects the font.
- `font-size` controls text size.
- `font-weight` controls thickness.
- `font-style` controls italic/oblique appearance.
- `line-height` controls vertical spacing.
- `text-align` controls horizontal alignment.
- `text-decoration` adds or removes decoration.
- `text-transform` controls capitalization.
- `text-indent` indents the first line.
- `letter-spacing` controls character spacing.
- `word-spacing` controls word spacing.
- `text-shadow` creates text shadows.
- `font` provides shorthand notation.
- Readability and accessibility should always be considered.