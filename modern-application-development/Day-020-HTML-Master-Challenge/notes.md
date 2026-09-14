# 📚 Day 020 — HTML Master Challenge Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. Challenge Overview

Day 020 combines the major HTML concepts learned during Day 001 to Day 019.

The objective is not to learn a large number of new elements.

The objective is to demonstrate practical understanding by combining existing HTML concepts into one complete webpage.

---

# 2. Project Structure

The project uses the following structure:

    <!DOCTYPE html>
    <html>
        <head>
        </head>

        <body>

            <header>
            </header>

            <nav>
            </nav>

            <main>

                <section>
                </section>

            </main>

            <footer>
            </footer>

        </body>
    </html>

---

# 3. Header

The header introduces the webpage or a particular section.

Example:

    <header>

        <h1>Student Learning Hub</h1>

        <p>
            Welcome to my learning journey.
        </p>

    </header>

---

# 4. Navigation

Navigation provides links to different sections of the webpage.

Example:

    <nav aria-label="Main Navigation">

        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>

    </nav>

Using fragment identifiers such as `#about` allows navigation to a section with the matching `id`.

---

# 5. Main Content

The `<main>` element contains the primary content of the webpage.

Example:

    <main>

        <section id="about">
            About content
        </section>

        <section id="skills">
            Skills content
        </section>

    </main>

A page should have one primary `<main>` element.

---

# 6. Sections

A section groups related content.

Example:

    <section id="education">

        <h2>Education</h2>

        <p>
            Education information goes here.
        </p>

    </section>

A section should generally have a meaningful heading.

---

# 7. Articles

An article represents a self-contained piece of content.

Example:

    <article>

        <h3>Student Performance Dashboard</h3>

        <p>
            A project for analyzing student performance data.
        </p>

    </article>

Multiple articles can be placed inside a projects section.

---

# 8. Aside

An aside contains related or supplementary information.

Example:

    <aside>

        <h2>Quick Resources</h2>

        <ul>
            <li>HTML Documentation</li>
            <li>Practice Exercises</li>
        </ul>

    </aside>

---

# 9. Images

Images can be included using `<img>`.

Example:

    <img
        src="https://example.com/image.jpg"
        alt="Description of the image"
        width="200">

The `alt` attribute provides alternative text.

---

# 10. Figure

A figure groups an image or other media with its caption.

Example:

    <figure>

        <img
            src="image.jpg"
            alt="HTML logo"
            width="180">

        <figcaption>
            HTML5 Logo
        </figcaption>

    </figure>

---

# 11. Education Table

Tables are useful for structured data.

Example:

    <table border="1">

        <caption>
            Education Details
        </caption>

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

Use tables for data, not page layout.

---

# 12. Colspan and Rowspan

`colspan` allows a cell to cover multiple columns.

Example:

    <th colspan="2">
        Project Information
    </th>

`rowspan` allows a cell to cover multiple rows.

Example:

    <td rowspan="2">
        Web Development
    </td>

---

# 13. Lists

Use an unordered list when order does not matter.

Example:

    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ul>

Use an ordered list when sequence matters.

Example:

    <ol>
        <li>Learn HTML</li>
        <li>Learn CSS</li>
        <li>Learn JavaScript</li>
    </ol>

Use description lists for terms and definitions.

Example:

    <dl>

        <dt>HTML</dt>
        <dd>Markup language for webpage structure.</dd>

        <dt>CSS</dt>
        <dd>Language for webpage presentation.</dd>

    </dl>

---

# 14. Contact Form

A contact form can collect information from the user.

Example:

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

# 15. Input Types

Choose input types according to the data.

Examples:

    <input type="text">

    <input type="email">

    <input type="password">

    <input type="number">

    <input type="date">

    <input type="tel">

    <input type="url">

    <input type="file">

---

# 16. Radio Buttons

Radio buttons are useful when one option should be selected.

Example:

    <input
        type="radio"
        id="online"
        name="mode"
        value="online">

    <label for="online">
        Online
    </label>

All radio buttons in the same group should normally share the same `name`.

---

# 17. Checkboxes

Checkboxes are useful when multiple choices can be selected.

Example:

    <input
        type="checkbox"
        id="html"
        name="skills"
        value="html">

    <label for="html">
        HTML
    </label>

---

# 18. Form Validation

HTML provides built-in client-side validation.

Example:

    <input
        type="text"
        name="name"
        minlength="3"
        maxlength="50"
        required>

Email:

    <input
        type="email"
        name="email"
        required>

Phone:

    <input
        type="tel"
        name="phone"
        pattern="[0-9]{10}"
        required>

---

# 19. Select Element

A dropdown can be created using `<select>`.

Example:

    <select name="topic" required>

        <option value="">
            Select a topic
        </option>

        <option value="html">
            HTML
        </option>

        <option value="css">
            CSS
        </option>

    </select>

---

# 20. Textarea

Use `<textarea>` for multi-line text.

Example:

    <textarea
        name="message"
        rows="5"
        cols="40"
        placeholder="Write your message"
        required>
    </textarea>

---

# 21. Multimedia

HTML supports audio and video.

Audio:

    <audio controls>

        <source
            src="audio/sample.mp3"
            type="audio/mpeg">

        Your browser does not support audio.

    </audio>

Video:

    <video controls width="640">

        <source
            src="video/sample.mp4"
            type="video/mp4">

        Your browser does not support video.

    </video>

---

# 22. iframe

An iframe can embed external content.

Example:

    <iframe
        src="https://www.example.com"
        title="Example Website"
        width="600"
        height="300">
    </iframe>

A meaningful `title` should be provided for accessibility.

---

# 23. Accessibility Checklist

Important accessibility practices:

- Use semantic elements.
- Use logical heading hierarchy.
- Add `alt` text to informative images.
- Connect labels to form controls.
- Use descriptive link text.
- Use table headers.
- Use `scope` where appropriate.
- Provide captions or transcripts for media when appropriate.
- Do not depend only on visual presentation.

---

# 24. HTML Best Practices

Follow these rules:

1. Use HTML5 doctype.
2. Set the document language.
3. Use proper indentation.
4. Use semantic elements.
5. Use meaningful headings.
6. Use meaningful attributes.
7. Add alternative text to images.
8. Use labels for form controls.
9. Use appropriate input types.
10. Use tables only for data.
11. Avoid deprecated elements.
12. Keep HTML structure clean.
13. Use lowercase element names.
14. Quote attribute values.
15. Close elements correctly.
16. Keep HTML, CSS, and JavaScript responsibilities separate.

---

# 25. Master Challenge Strategy

When creating a webpage from scratch, follow this order:

1. Create the HTML5 document structure.
2. Add the page title.
3. Create the header.
4. Add navigation.
5. Create the main content.
6. Divide content into semantic sections.
7. Add text.
8. Add lists.
9. Add tables.
10. Add project articles.
11. Add multimedia.
12. Add the contact form.
13. Add an aside.
14. Add the footer.
15. Test every section.

---

# 26. Final HTML Mental Model

Think of a webpage as a structured document:

    HTML
    │
    ├── HEAD
    │   ├── META
    │   └── TITLE
    │
    └── BODY
        ├── HEADER
        ├── NAV
        ├── MAIN
        │   ├── SECTION
        │   ├── ARTICLE
        │   ├── TABLE
        │   ├── FORM
        │   └── ASIDE
        └── FOOTER

---

# 27. Final Goal

The real goal of Day 020 is independence.

You should now be able to open a blank `index.html` file and create a structured webpage without needing to copy a complete template.

After this challenge, the HTML foundation is ready for the next stage:

**CSS Fundamentals.**

---

**End of Day 020 Notes**