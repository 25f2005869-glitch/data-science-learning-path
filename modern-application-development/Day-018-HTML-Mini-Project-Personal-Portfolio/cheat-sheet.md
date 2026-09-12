# ⚡ Day 018 — Personal Portfolio Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🔹 Main Structure

    <header>
        Portfolio Header
    </header>

    <nav>
        Navigation
    </nav>

    <main>

        <section>
            Section
        </section>

        <article>
            Project
        </article>

    </main>

    <footer>
        Footer
    </footer>

---

## 🔹 Navigation

    <a href="#about">About</a>

    <a href="#projects">Projects</a>

The `href` points to an element's `id`.

---

## 🔹 About

    <section id="about">

        <h2>About Me</h2>

        <p>
            About information.
        </p>

    </section>

---

## 🔹 Image

    <img
        src="profile.jpg"
        alt="Student profile photograph"
        width="200">

Always provide appropriate `alt` text.

---

## 🔹 Figure

    <figure>

        <img
            src="profile.jpg"
            alt="Student profile photograph">

        <figcaption>
            Portfolio Profile
        </figcaption>

    </figure>

---

## 🔹 Education Table

    <table>

        <caption>Education Details</caption>

        <thead>
            <tr>
                <th scope="col">Programme</th>
                <th scope="col">Institution</th>
                <th scope="col">Status</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>BS Degree</td>
                <td>IIT Madras</td>
                <td>In Progress</td>
            </tr>
        </tbody>

    </table>

---

## 🔹 Skills

    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
        <li>Python</li>
    </ul>

---

## 🔹 Projects

    <article>

        <h3>Project Name</h3>

        <p>
            Project description.
        </p>

    </article>

---

## 🔹 External Link

    <a
        href="https://github.com/"
        target="_blank"
        rel="noopener noreferrer">
        GitHub Profile
    </a>

---

## 🔹 Contact Form

    <form action="#" method="post">

        <label for="name">Name:</label>

        <input
            type="text"
            id="name"
            name="name"
            required>

        <button type="submit">
            Send
        </button>

    </form>

---

## 🔹 Validation

    required

    minlength="3"

    maxlength="50"

    type="email"

    pattern="[0-9]{10}"

---

## 🔹 Audio

    <audio controls>

        <source
            src="audio/sample.mp3"
            type="audio/mpeg">

    </audio>

---

## 🔹 Video

    <video controls width="640">

        <source
            src="video/sample.mp4"
            type="video/mp4">

    </video>

---

## 🔹 iFrame

    <iframe
        src="https://www.example.com"
        title="Example Website"
        width="600"
        height="300"
        loading="lazy">
    </iframe>

---

## 🔹 Accessibility Checklist

    ✓ Semantic HTML
    ✓ Logical headings
    ✓ Image alt text
    ✓ Form labels
    ✓ Appropriate input types
    ✓ Descriptive links
    ✓ iframe title
    ✓ Table headers

---

## 🔹 Portfolio Sections

    Header
    Navigation
    About
    Education
    Skills
    Projects
    Learning Journey
    Multimedia
    Contact
    Footer

---

## ⭐ Remember

HTML = Structure + Meaning

CSS = Presentation

JavaScript = Behaviour