# 🌐 Day 096 — HTML Complete Revision Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 096  
**Topic:** HTML Complete Revision

---

## 🧱 Basic Structure

    <!DOCTYPE html>
    <html>
    <head>
        <title>Page</title>
    </head>
    <body>
        Content
    </body>
    </html>

---

## 🏷️ Common Elements

| Element | Purpose |
|---|---|
| `h1`–`h6` | Headings |
| `p` | Paragraph |
| `a` | Link |
| `img` | Image |
| `br` | Line break |
| `hr` | Thematic break |
| `ul` | Unordered list |
| `ol` | Ordered list |
| `li` | List item |
| `table` | Table |
| `form` | Form |
| `input` | Input control |
| `button` | Button |

---

## 🔗 Link

    <a href="https://example.com">Visit</a>

New tab:

    target="_blank"
    rel="noopener noreferrer"

---

## 🖼️ Image

    <img src="image.jpg" alt="Description">

Remember:

**Always provide useful `alt` text for meaningful images.**

---

## 📋 Lists

Ordered:

    <ol>
        <li>HTML</li>
    </ol>

Unordered:

    <ul>
        <li>CSS</li>
    </ul>

Description:

    <dl>
        <dt>HTML</dt>
        <dd>Web markup language</dd>
    </dl>

---

## 📊 Table

    <table>
        <caption>Marks</caption>
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

---

## 📝 Form

    <form action="/submit" method="post">
        <label for="name">Name</label>
        <input id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>

---

## ⌨️ Important Input Types

    text
    email
    password
    number
    date
    time
    url
    tel
    search
    radio
    checkbox
    file
    color
    range
    submit
    reset

---

## ✅ Validation

    required
    minlength
    maxlength
    min
    max
    pattern

---

## 🧩 Semantic HTML

    header
    nav
    main
    section
    article
    aside
    footer
    figure
    figcaption

---

## 🎵 Multimedia

Audio:

    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
    </audio>

Video:

    <video controls>
        <source src="video.mp4" type="video/mp4">
    </video>

---

## 🖥️ iFrame

    <iframe
        src="https://example.com"
        title="Example website">
    </iframe>

---

## ♿ Accessibility

Remember:

    Semantic HTML
    Meaningful alt text
    Form labels
    Logical headings
    Descriptive links
    Keyboard accessibility

---

## 🧠 HTML + CSS + JS

    HTML → Structure
    CSS → Presentation
    JavaScript → Behavior

---

## ⭐ Final Rule

**Write HTML for meaning and structure, not merely for appearance.**