# ⚡ Day 019 — HTML Revision Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 📌 Basic Structure

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page Title</title>
    </head>
    <body>
    </body>
    </html>

---

## 📝 Text

    <h1>Heading</h1>
    <h2>Heading</h2>
    <p>Paragraph</p>
    <br>
    <hr>

---

## 🔗 Link

    <a href="https://example.com">
        Visit Website
    </a>

New tab:

    <a href="https://example.com"
       target="_blank"
       rel="noopener noreferrer">
        Visit Website
    </a>

---

## 🖼 Image

    <img src="image.jpg"
         alt="Description"
         width="200">

---

## 📋 Lists

### Ordered

    <ol>
        <li>HTML</li>
        <li>CSS</li>
    </ol>

### Unordered

    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>

### Description

    <dl>
        <dt>HTML</dt>
        <dd>Markup language</dd>
    </dl>

---

## 📊 Table

    <table>

        <caption>Student Details</caption>

        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Course</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>Saloni</td>
                <td>MAD</td>
            </tr>
        </tbody>

    </table>

### colspan

    <td colspan="2">Data</td>

### rowspan

    <td rowspan="2">Data</td>

---

## 📝 Form

    <form action="#" method="post">

        <label for="name">Name:</label>

        <input type="text"
               id="name"
               name="name"
               required>

        <button type="submit">
            Submit
        </button>

    </form>

---

## ⌨ Input Types

    text
    email
    password
    number
    date
    time
    tel
    url
    search
    radio
    checkbox
    file
    color
    range
    submit
    reset
    button

---

## ✅ Validation

    required
    minlength
    maxlength
    min
    max
    pattern

Example:

    <input type="number"
           min="18"
           max="60"
           required>

---

## 🔘 Radio

    <input type="radio"
           name="gender"
           value="female">

---

## ☑ Checkbox

    <input type="checkbox"
           name="skills"
           value="html">

---

## 🔽 Dropdown

    <select name="course">

        <option value="mad">
            MAD
        </option>

        <option value="mlt">
            MLT
        </option>

    </select>

---

## 📝 Textarea

    <textarea
        name="message"
        rows="5"
        cols="40">
    </textarea>

---

## 🏗 Semantic HTML

    <header>
    <nav>
    <main>
    <section>
    <article>
    <aside>
    <footer>
    <figure>
    <figcaption>

---

## 🎵 Audio

    <audio controls>
        <source src="audio.mp3"
                type="audio/mpeg">
    </audio>

---

## 🎬 Video

    <video controls width="640">
        <source src="video.mp4"
                type="video/mp4">
    </video>

---

## 🌐 iframe

    <iframe
        src="https://example.com"
        title="Example Website"
        width="600"
        height="300">
    </iframe>

---

## ♿ Accessibility

- Use semantic HTML.
- Use meaningful headings.
- Add `alt` text.
- Use `<label>` with form controls.
- Use descriptive links.
- Use `<caption>` for tables.
- Use `scope` for table headers.
- Provide captions for videos when appropriate.

---

## ⭐ Most Important Revision

Remember:

    HTML = Structure

    CSS = Presentation

    JavaScript = Behaviour

---

## 🔑 Essential Elements

    html
    head
    body
    h1-h6
    p
    a
    img
    ol
    ul
    li
    table
    tr
    th
    td
    form
    label
    input
    textarea
    select
    option
    button
    header
    nav
    main
    section
    article
    aside
    footer
    audio
    video
    iframe