# ⚡ Day 017 — HTML Best Practices Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🔹 Basic Structure

    <!DOCTYPE html>

    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>Page Title</title>
    </head>

    <body>
        Content
    </body>

    </html>

---

## 🔹 Semantic HTML

Prefer:

    <header>
    <nav>
    <main>
    <section>
    <article>
    <aside>
    <footer>

Use `<div>` when no appropriate semantic element exists.

---

## 🔹 Headings

Recommended hierarchy:

    <h1>Main Page Title</h1>

    <h2>Major Section</h2>

    <h3>Subsection</h3>

    <h2>Another Major Section</h2>

Do not choose headings only for visual size.

---

## 🔹 Images

    <img
        src="profile.jpg"
        alt="Student profile photograph">

Remember:

`alt` describes the image when appropriate.

Decorative image:

    <img src="decoration.png" alt="">

---

## 🔹 Forms

Good:

    <label for="email">Email:</label>

    <input
        type="email"
        id="email"
        name="email"
        required>

Remember:

`label` → Accessibility

`type` → Appropriate input behavior

`required` → Required field

---

## 🔹 Links

Prefer descriptive text:

    <a href="projects.html">
        View My Projects
    </a>

Avoid vague text such as:

    Click Here

For a new tab:

    <a
        href="https://example.com"
        target="_blank"
        rel="noopener noreferrer">
        Visit Website
    </a>

---

## 🔹 Tables

Use tables for data.

    <table>

        <caption>Student Results</caption>

        <tr>
            <th>Name</th>
            <th>Marks</th>
        </tr>

        <tr>
            <td>Saloni</td>
            <td>95</td>
        </tr>

    </table>

Do not use tables for webpage layout.

---

## 🔹 IDs and Classes

`id` → Unique element

    <section id="projects">

`class` → Reusable group

    <p class="important">

---

## 🔹 Naming

Prefer meaningful names:

    id="projects"

    class="student-card"

Avoid unclear names:

    id="x123"

---

## 🔹 Formatting

Use:

- Consistent indentation
- Lowercase elements
- Quoted attribute values
- Proper nesting
- Meaningful comments

---

## 🔹 Avoid

Do not rely on outdated presentation elements:

    <center>
    <font>
    <marquee>

Use CSS for presentation.

---

## 🔹 Page Title

    <title>Student Portfolio</title>

Every webpage should have a meaningful title.

---

## 🔹 Viewport

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

Useful for responsive webpages.

---

## 🔹 Accessibility

Remember:

    Semantic HTML
    +
    Proper labels
    +
    Useful alt text
    +
    Logical headings
    +
    Descriptive links

---

## 🔹 HTML Quality Checklist

    ✓ DOCTYPE
    ✓ lang
    ✓ charset
    ✓ viewport
    ✓ title
    ✓ semantic structure
    ✓ logical headings
    ✓ alt text
    ✓ form labels
    ✓ correct input types
    ✓ descriptive links
    ✓ unique IDs
    ✓ proper nesting
    ✓ consistent indentation
    ✓ no deprecated elements

---

## ⭐ Golden Rule

HTML = Structure + Meaning

CSS = Presentation

JavaScript = Behavior