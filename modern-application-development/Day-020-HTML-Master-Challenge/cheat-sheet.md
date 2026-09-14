# ⚡ Day 020 — HTML Master Challenge Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🏗️ Basic Structure

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

## 🧱 Semantic Structure

    <header></header>
    <nav></nav>

    <main>

        <section></section>

        <article></article>

        <aside></aside>

    </main>

    <footer></footer>

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

    <img
        src="image.jpg"
        alt="Image description"
        width="200">

---

## 📋 Lists

Ordered:

    <ol>
        <li>HTML</li>
        <li>CSS</li>
    </ol>

Unordered:

    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>

Description:

    <dl>
        <dt>HTML</dt>
        <dd>Markup language</dd>
    </dl>

---

## 📊 Table

    <table border="1">

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

---

## ↔️ Colspan

    <td colspan="2">
        Data
    </td>

---

## ↕️ Rowspan

    <td rowspan="2">
        Data
    </td>

---

## 📝 Form

    <form action="#" method="post">

        <label for="name">
            Name:
        </label>

        <input
            type="text"
            id="name"
            name="name"
            required>

        <button type="submit">
            Submit
        </button>

    </form>

---

## ⌨️ Input Types

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

    <input
        type="number"
        min="1"
        max="100"
        required>

---

## 🔘 Radio

    <input
        type="radio"
        name="mode"
        value="online">

---

## ☑️ Checkbox

    <input
        type="checkbox"
        name="skills"
        value="html">

---

## 🔽 Select

    <select name="course">

        <option value="html">
            HTML
        </option>

        <option value="css">
            CSS
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

## 🖼️ Figure

    <figure>

        <img
            src="image.jpg"
            alt="Description">

        <figcaption>
            Image Caption
        </figcaption>

    </figure>

---

## 🎵 Audio

    <audio controls>

        <source
            src="audio.mp3"
            type="audio/mpeg">

    </audio>

---

## 🎬 Video

    <video controls width="640">

        <source
            src="video.mp4"
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
- Use logical headings.
- Add `alt` text.
- Use labels.
- Use descriptive links.
- Use table headers.
- Use `scope`.
- Provide appropriate media alternatives.

---

## 🔑 Important Attributes

| Attribute | Purpose |
|---|---|
| `id` | Unique identifier |
| `class` | Groups elements |
| `href` | Link destination |
| `src` | Resource location |
| `alt` | Alternative text |
| `name` | Form field name |
| `value` | Form value |
| `required` | Mandatory field |
| `placeholder` | Input hint |
| `target` | Link target |
| `rel` | Link relationship |
| `scope` | Table header meaning |
| `action` | Form destination |
| `method` | Form submission method |

---

## 🧠 Final Mental Model

    HTML = Structure
    CSS = Presentation
    JavaScript = Behaviour

---

## 🏆 Master Challenge Checklist

    ✓ Structure
    ✓ Semantic HTML
    ✓ Headings
    ✓ Paragraphs
    ✓ Links
    ✓ Images
    ✓ Lists
    ✓ Tables
    ✓ Forms
    ✓ Validation
    ✓ Multimedia
    ✓ Accessibility

---

**HTML Foundation Complete! 🏆**