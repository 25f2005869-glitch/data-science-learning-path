# 📚 Day 019 — HTML Revision Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 1. HTML Overview

HTML stands for HyperText Markup Language.

HTML is used to create the structure of webpages.

HTML is not a programming language. It is a markup language.

A webpage can contain:

- Headings
- Paragraphs
- Links
- Images
- Lists
- Tables
- Forms
- Audio
- Video
- Embedded content

---

# 2. Basic HTML Structure

A standard HTML5 document contains:

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page Title</title>
    </head>
    <body>
        Page content
    </body>
    </html>

### Important Parts

`<!DOCTYPE html>` tells the browser that the document uses HTML5.

`<html>` is the root element.

`<head>` contains metadata and information about the document.

`<title>` defines the browser tab title.

`<body>` contains visible webpage content.

---

# 3. Headings

HTML provides six heading levels:

    <h1>Main Heading</h1>
    <h2>Section Heading</h2>
    <h3>Subsection Heading</h3>
    <h4>Heading Level 4</h4>
    <h5>Heading Level 5</h5>
    <h6>Heading Level 6</h6>

`<h1>` represents the highest-level heading.

Headings should follow a logical hierarchy.

---

# 4. Paragraphs

The `<p>` element is used for paragraphs.

Example:

    <p>
        HTML is used to create the structure of webpages.
    </p>

Use paragraphs for normal blocks of text.

---

# 5. Line Break and Horizontal Rule

The `<br>` element creates a line break.

Example:

    HTML<br>
    CSS<br>
    JavaScript

The `<hr>` element represents a thematic break.

Example:

    <hr>

---

# 6. HTML Comments

Comments are ignored by the browser.

Example:

    <!-- This is an HTML comment -->

Comments are useful for explaining sections of code.

---

# 7. Links

The `<a>` element creates hyperlinks.

Example:

    <a href="https://example.com">
        Visit Website
    </a>

Important attributes:

- `href` — destination of the link
- `target` — controls where the link opens
- `rel` — provides relationship/security information

For an external link opened in a new tab:

    <a href="https://example.com"
       target="_blank"
       rel="noopener noreferrer">
        Visit Website
    </a>

---

# 8. Images

The `<img>` element displays an image.

Example:

    <img src="images/profile.jpg"
         alt="Profile image"
         width="200">

Important attributes:

- `src` — image location
- `alt` — alternative text
- `width` — image width
- `height` — image height

The `alt` attribute is important for accessibility.

---

# 9. Lists

## Ordered List

An ordered list uses `<ol>`.

Example:

    <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ol>

## Unordered List

An unordered list uses `<ul>`.

Example:

    <ul>
        <li>Python</li>
        <li>SQL</li>
        <li>HTML</li>
    </ul>

## Description List

A description list uses `<dl>`, `<dt>`, and `<dd>`.

Example:

    <dl>
        <dt>HTML</dt>
        <dd>Markup language used to structure webpages.</dd>

        <dt>CSS</dt>
        <dd>Language used to style webpages.</dd>
    </dl>

---

# 10. Tables

Tables are used for tabular data.

Basic structure:

    <table>

        <tr>
            <th>Name</th>
            <th>Course</th>
        </tr>

        <tr>
            <td>Saloni</td>
            <td>MAD</td>
        </tr>

    </table>

Important elements:

- `<table>` — table
- `<caption>` — table title
- `<thead>` — table header section
- `<tbody>` — table body
- `<tfoot>` — table footer
- `<tr>` — table row
- `<th>` — header cell
- `<td>` — data cell

---

# 11. Colspan

`colspan` allows a cell to span multiple columns.

Example:

    <th colspan="3">
        Student Information
    </th>

---

# 12. Rowspan

`rowspan` allows a cell to span multiple rows.

Example:

    <td rowspan="2">
        Saloni
    </td>

---

# 13. Table Accessibility

The `scope` attribute helps identify the purpose of table headers.

Example:

    <th scope="col">Name</th>

For row headers:

    <th scope="row">Student 1</th>

Tables should be used for data, not for webpage layout.

---

# 14. Forms

Forms collect information from users.

Basic structure:

    <form action="#" method="post">

        <label for="name">Name:</label>

        <input type="text"
               id="name"
               name="name">

        <button type="submit">
            Submit
        </button>

    </form>

---

# 15. Labels

The `<label>` element identifies a form control.

Example:

    <label for="email">
        Email:
    </label>

    <input type="email"
           id="email"
           name="email">

The `for` value should match the input's `id`.

---

# 16. Common Input Types

Common HTML input types include:

- `text`
- `email`
- `password`
- `number`
- `date`
- `time`
- `tel`
- `url`
- `search`
- `radio`
- `checkbox`
- `file`
- `color`
- `range`
- `submit`
- `reset`
- `button`

Example:

    <input type="email"
           name="email"
           required>

---

# 17. Radio Buttons

Radio buttons allow the user to select one option from a group.

Example:

    <input type="radio"
           id="html"
           name="course"
           value="html">

    <label for="html">
        HTML
    </label>

Radio buttons belonging to the same group should use the same `name`.

---

# 18. Checkboxes

Checkboxes allow multiple selections.

Example:

    <input type="checkbox"
           id="html"
           name="skills"
           value="html">

    <label for="html">
        HTML
    </label>

Multiple checkboxes can be selected.

---

# 19. Select Dropdown

A dropdown can be created using `<select>`.

Example:

    <select name="course">

        <option value="mad">
            Modern Application Development
        </option>

        <option value="mlt">
            Machine Learning Techniques
        </option>

    </select>

---

# 20. Textarea

`<textarea>` is used for multi-line text.

Example:

    <textarea
        name="message"
        rows="5"
        cols="40"
        placeholder="Write your message">
    </textarea>

---

# 21. Form Validation

HTML provides built-in client-side validation.

Important attributes:

- `required`
- `minlength`
- `maxlength`
- `min`
- `max`
- `pattern`
- `type`

Example:

    <input type="text"
           name="username"
           minlength="3"
           maxlength="30"
           required>

Email validation:

    <input type="email"
           name="email"
           required>

Number validation:

    <input type="number"
           name="age"
           min="18"
           max="60">

---

# 22. Semantic HTML

Semantic HTML uses elements that describe the meaning of their content.

Important semantic elements:

- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<article>`
- `<aside>`
- `<footer>`
- `<figure>`
- `<figcaption>`

Example structure:

    <header>
        Header content
    </header>

    <nav>
        Navigation
    </nav>

    <main>

        <section>
            Section content
        </section>

        <article>
            Article content
        </article>

        <aside>
            Related content
        </aside>

    </main>

    <footer>
        Footer content
    </footer>

Semantic HTML improves readability, accessibility, and document structure.

---

# 23. Figure and Figcaption

`<figure>` groups media content.

`<figcaption>` provides a caption.

Example:

    <figure>

        <img src="image.jpg"
             alt="HTML logo">

        <figcaption>
            HTML5 Logo
        </figcaption>

    </figure>

---

# 24. Audio

Audio can be added using `<audio>`.

Example:

    <audio controls>

        <source src="audio/sample.mp3"
                type="audio/mpeg">

        Your browser does not support audio.

    </audio>

The `controls` attribute displays playback controls.

---

# 25. Video

Video can be added using `<video>`.

Example:

    <video controls
           width="640">

        <source src="video/sample.mp4"
                type="video/mp4">

        Your browser does not support video.

    </video>

Common attributes:

- `controls`
- `autoplay`
- `muted`
- `loop`
- `poster`
- `preload`

---

# 26. iframe

The `<iframe>` element embeds another webpage or external content.

Example:

    <iframe
        src="https://www.example.com"
        title="Example Website"
        width="600"
        height="300">
    </iframe>

Always provide a meaningful `title` for accessibility.

---

# 27. Important HTML Attributes

Common attributes include:

| Attribute | Purpose |
|---|---|
| `id` | Unique identifier |
| `class` | Groups elements |
| `href` | Link destination |
| `src` | Resource location |
| `alt` | Alternative text |
| `title` | Additional information |
| `name` | Form field name |
| `value` | Form value |
| `placeholder` | Input hint |
| `required` | Makes field mandatory |
| `disabled` | Disables control |
| `readonly` | Prevents editing |
| `target` | Link target |
| `rel` | Link relationship |

---

# 28. Accessibility

Good HTML should be accessible.

Important practices:

- Use semantic elements.
- Use meaningful headings.
- Add `alt` text to informative images.
- Associate labels with form controls.
- Use descriptive link text.
- Use table headers correctly.
- Provide captions for multimedia when appropriate.
- Use logical document structure.

---

# 29. HTML Best Practices

Follow these practices:

1. Use `<!DOCTYPE html>`.
2. Set the correct `lang` attribute.
3. Use proper indentation.
4. Use semantic HTML.
5. Keep heading hierarchy logical.
6. Use meaningful names.
7. Add `alt` text to images.
8. Use labels for forms.
9. Use tables only for tabular data.
10. Keep HTML, CSS, and JavaScript responsibilities separate.
11. Avoid deprecated HTML elements.
12. Close elements correctly.
13. Use lowercase element names.
14. Quote attribute values.
15. Validate the HTML when necessary.

---

# 30. HTML Revision Checklist

Before moving to CSS, make sure you understand:

- Document structure
- Elements
- Attributes
- Headings
- Paragraphs
- Links
- Images
- Lists
- Tables
- Forms
- Input types
- Validation
- Semantic HTML
- Multimedia
- Accessibility
- HTML best practices

---

# 31. Final Revision Goal

The purpose of Day 019 is not to learn many new HTML elements.

The main goal is to become comfortable combining the concepts already learned.

You should be able to create a complete HTML webpage from an empty file without copying a template.

---

**End of Day 019 Notes**