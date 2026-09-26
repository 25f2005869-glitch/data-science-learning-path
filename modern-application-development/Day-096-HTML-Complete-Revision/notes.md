# 🌐 Day 096 — HTML Complete Revision Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 096  
**Topic:** HTML Complete Revision

---

# 1. What is HTML?

HTML stands for **HyperText Markup Language**.

HTML is used to structure content on webpages.

HTML defines:

- Headings
- Paragraphs
- Links
- Images
- Lists
- Tables
- Forms
- Semantic sections
- Multimedia

HTML provides structure, while CSS provides presentation and JavaScript provides behavior.

---

# 2. Basic HTML Structure

A basic HTML5 document contains:

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

Important parts:

- `<!DOCTYPE html>` declares HTML5.
- `<html>` is the root element.
- `<head>` contains metadata.
- `<title>` defines the page title.
- `<body>` contains visible content.

---

# 3. HTML Elements

An HTML element generally contains:

    Opening tag
    Content
    Closing tag

Example:

    <p>Hello World</p>

Some elements are empty elements.

Examples:

    <br>
    <hr>
    <img>

---

# 4. Attributes

Attributes provide additional information about elements.

Example:

    <img src="profile.jpg" alt="Profile image">

Common attributes:

- `id`
- `class`
- `title`
- `href`
- `src`
- `alt`
- `width`
- `height`
- `required`
- `placeholder`

---

# 5. Headings

HTML provides six heading levels:

    <h1>
    <h2>
    <h3>
    <h4>
    <h5>
    <h6>

Use headings in a meaningful hierarchy.

The `<h1>` generally represents the main page heading.

---

# 6. Paragraphs and Text

Important elements:

- `<p>` — paragraph
- `<br>` — line break
- `<hr>` — thematic break
- `<strong>` — strong importance
- `<em>` — emphasis

Prefer semantic elements instead of using HTML only for visual appearance.

---

# 7. Links

Links use the `<a>` element.

Example:

    <a href="https://example.com">Visit Website</a>

Important attributes:

- `href`
- `target`
- `rel`

For links opening a new tab, use an appropriate `rel` value such as:

    rel="noopener noreferrer"

---

# 8. Images

Images use the `<img>` element.

Example:

    <img src="images/student.jpg"
         alt="Student studying"
         width="400">

Important attributes:

- `src`
- `alt`
- `width`
- `height`

The `alt` attribute is important for accessibility.

---

# 9. Lists

HTML supports three major list types.

## Ordered List

    <ol>
        <li>HTML</li>
        <li>CSS</li>
    </ol>

## Unordered List

    <ul>
        <li>Python</li>
        <li>JavaScript</li>
    </ul>

## Description List

    <dl>
        <dt>HTML</dt>
        <dd>Markup language for web structure.</dd>
    </dl>

---

# 10. Tables

Important table elements:

- `<table>`
- `<caption>`
- `<thead>`
- `<tbody>`
- `<tfoot>`
- `<tr>`
- `<th>`
- `<td>`

Example structure:

    <table>
        <caption>Student Marks</caption>
        <thead>
            <tr>
                <th scope="col">Subject</th>
                <th scope="col">Marks</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>PDSA</td>
                <td>85</td>
            </tr>
        </tbody>
    </table>

Use tables for tabular data, not for page layout.

---

# 11. Colspan and Rowspan

`colspan` allows a cell to span multiple columns.

    <td colspan="2">Total</td>

`rowspan` allows a cell to span multiple rows.

    <td rowspan="2">Student</td>

---

# 12. Forms

Forms collect user input.

Basic structure:

    <form action="/submit" method="post">
        ...
    </form>

Important attributes:

- `action`
- `method`
- `name`
- `id`
- `value`
- `placeholder`
- `required`

---

# 13. Input Types

Common input types include:

- text
- email
- password
- number
- date
- time
- datetime-local
- month
- week
- url
- tel
- search
- radio
- checkbox
- file
- color
- range
- hidden
- submit
- reset
- button

Choose the input type according to the data being collected.

---

# 14. Labels

Use `<label>` with form controls.

Example:

    <label for="email">Email</label>
    <input type="email" id="email" name="email">

Labels improve usability and accessibility.

---

# 15. Select and Textarea

Dropdown:

    <select name="course">
        <option value="ds">Data Science</option>
        <option value="programming">Programming</option>
    </select>

Multiline input:

    <textarea name="message"></textarea>

---

# 16. Radio Buttons

Radio buttons are normally grouped using the same `name`.

Example:

    <input type="radio" name="level" value="foundation">
    <input type="radio" name="level" value="diploma">

This allows the user to select one option from the group.

---

# 17. Checkboxes

Checkboxes are useful when multiple options can be selected.

Example:

    <input type="checkbox" name="skill" value="python">
    <input type="checkbox" name="skill" value="sql">

---

# 18. HTML Validation

Important validation attributes:

- `required`
- `minlength`
- `maxlength`
- `min`
- `max`
- `pattern`

Example:

    <input
        type="text"
        name="username"
        minlength="3"
        maxlength="30"
        required>

HTML validation improves the user experience, but server-side validation is still required in real applications.

---

# 19. Semantic HTML

Semantic elements communicate the meaning of content.

Important elements:

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
        ...
    </header>

    <nav>
        ...
    </nav>

    <main>
        <section>
            ...
        </section>
    </main>

    <footer>
        ...
    </footer>

---

# 20. Semantic vs Non-Semantic Elements

Semantic:

    <article>
    <nav>
    <main>
    <section>

Non-semantic:

    <div>
    <span>

`div` and `span` are useful, but semantic elements should be preferred when they accurately describe the content.

---

# 21. Audio

Use `<audio>` for audio content.

Example:

    <audio controls>
        <source src="audio/sample.mp3" type="audio/mpeg">
        Your browser does not support audio.
    </audio>

Useful attributes:

- `controls`
- `autoplay`
- `muted`
- `loop`
- `preload`

---

# 22. Video

Use `<video>` for video content.

Example:

    <video controls width="600">
        <source src="video/sample.mp4" type="video/mp4">
        Your browser does not support video.
    </video>

Useful attributes:

- `controls`
- `autoplay`
- `muted`
- `loop`
- `poster`
- `preload`

---

# 23. Captions

Video captions can be added using `<track>`.

Example:

    <track
        kind="captions"
        src="captions.vtt"
        srclang="en"
        label="English">

Captions improve accessibility.

---

# 24. iFrames

The `<iframe>` element can embed another webpage or supported external content.

Example:

    <iframe
        src="https://example.com"
        title="Example website"
        loading="lazy">
    </iframe>

Always provide a meaningful `title`.

External sites may prevent embedding.

---

# 25. Accessibility

Important HTML accessibility practices:

- Use semantic elements.
- Use meaningful headings.
- Add `alt` text to meaningful images.
- Use labels for form controls.
- Use descriptive link text.
- Maintain logical document structure.
- Do not rely only on color.
- Make interactive elements keyboard accessible.

---

# 26. HTML Comments

HTML comments:

    <!-- This is a comment -->

Comments are not displayed as normal page content.

Do not put passwords, API keys, or other secrets in HTML comments.

---

# 27. Meta Tags

Important metadata includes:

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

Metadata helps browsers interpret and display webpages correctly.

---

# 28. HTML Best Practices

Follow these practices:

- Use HTML5.
- Use a proper document structure.
- Use semantic HTML.
- Keep indentation consistent.
- Use meaningful names.
- Use lowercase element names.
- Quote attribute values.
- Add useful `alt` text.
- Associate labels with inputs.
- Use appropriate input types.
- Keep HTML, CSS, and JavaScript responsibilities separate.
- Avoid deprecated elements.
- Validate HTML.
- Consider accessibility.

---

# 29. Deprecated Elements to Avoid

Avoid outdated presentation elements such as:

    <center>
    <font>
    <marquee>

Use CSS for presentation instead.

---

# 30. HTML, CSS and JavaScript

Think of a webpage as:

    HTML
      ↓
    Structure

    CSS
      ↓
    Presentation

    JavaScript
      ↓
    Behavior

Together they create interactive web interfaces.

---

# 31. Final HTML Revision Checklist

- [ ] HTML5 structure
- [ ] Elements
- [ ] Attributes
- [ ] Headings
- [ ] Paragraphs
- [ ] Links
- [ ] Images
- [ ] Lists
- [ ] Tables
- [ ] Forms
- [ ] Input types
- [ ] Validation
- [ ] Semantic HTML
- [ ] Audio
- [ ] Video
- [ ] iFrames
- [ ] Accessibility
- [ ] Best practices

---

# 32. Final Takeaway

HTML is the foundation of web development.

A strong HTML document should be:

**Structured + Semantic + Accessible + Valid + Maintainable**