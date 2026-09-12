
## 2. `notes.md`

```markdown
# 📝 Day 018 — HTML Mini Project: Personal Portfolio

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. Project Introduction

A personal portfolio is a webpage that introduces a person, their education, skills, projects, achievements, and contact information.

In this project, we create a portfolio using HTML5 only.

The purpose is to combine previously learned HTML concepts.

---

# 2. Project Structure

The portfolio follows this general structure:

    Header
        ↓
    Navigation
        ↓
    Main
        ↓
    About
        ↓
    Education
        ↓
    Skills
        ↓
    Projects
        ↓
    Learning Journey
        ↓
    Multimedia
        ↓
    Contact
        ↓
    Footer

---

# 3. Header

The header introduces the portfolio.

Example:

    <header>
        <h1>Personal Portfolio</h1>
        <p>Welcome to my portfolio.</p>
    </header>

The header can contain:

- Name
- Portfolio title
- Short introduction

---

# 4. Navigation

The navigation allows users to move between sections.

Example:

    <nav>
        <a href="#about">About</a>
        <a href="#education">Education</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </nav>

The `href` values point to section IDs.

---

# 5. About Me

The About section introduces the student.

It can contain:

- Introduction
- Learning interests
- Career goals
- Short personal description

Example:

    <section id="about">
        <h2>About Me</h2>
        <p>I am learning web development.</p>
    </section>

---

# 6. Profile Image

A portfolio can contain a profile image.

Example:

    <figure>

        <img
            src="profile.jpg"
            alt="Student profile photograph"
            width="200">

        <figcaption>
            Personal Portfolio Profile
        </figcaption>

    </figure>

The `alt` attribute is important for accessibility.

---

# 7. Education Section

Education information can be displayed using a table.

Example structure:

    <table>

        <caption>Education Details</caption>

        <thead>
            ...
        </thead>

        <tbody>
            ...
        </tbody>

    </table>

Tables are appropriate when information naturally belongs in rows and columns.

---

# 8. Skills Section

Skills can be displayed using an unordered list.

Example:

    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
        <li>Python</li>
        <li>SQL</li>
    </ul>

---

# 9. Projects Section

Each project can be represented using an `<article>`.

Example:

    <article>

        <h3>Student Performance Dashboard</h3>

        <p>
            A project for analyzing student performance.
        </p>

    </article>

Multiple projects can exist inside a projects section.

---

# 10. Learning Journey

A portfolio can include a learning journey section.

Example:

    <ol>
        <li>HTML Fundamentals</li>
        <li>CSS Fundamentals</li>
        <li>JavaScript</li>
        <li>Flask</li>
    </ol>

An ordered list is useful when the sequence matters.

---

# 11. External Links

The portfolio can link to external profiles.

Example:

    <a
        href="https://github.com/"
        target="_blank"
        rel="noopener noreferrer">
        GitHub Profile
    </a>

Descriptive link text is better than vague text such as "Click Here."

---

# 12. Contact Form

A contact form allows visitors to submit information.

Basic structure:

    <form action="#" method="post">

        <label for="name">Name:</label>

        <input
            type="text"
            id="name"
            name="name"
            required>

        <button type="submit">
            Send Message
        </button>

    </form>

---

# 13. Form Validation

HTML5 validation can be used without JavaScript.

Examples:

    required

    minlength="3"

    maxlength="50"

    type="email"

    pattern="[0-9]{10}"

These attributes provide basic browser-side validation.

---

# 14. Email Field

Use the email input type for email addresses.

Example:

    <input
        type="email"
        id="email"
        name="email"
        required>

The browser provides basic email-format validation.

---

# 15. Phone Field

Use `tel` for telephone numbers.

Example:

    <input
        type="tel"
        id="phone"
        name="phone"
        pattern="[0-9]{10}"
        required>

The pattern requires exactly 10 digits.

---

# 16. Message Field

Use `<textarea>` for longer text.

Example:

    <textarea
        id="message"
        name="message"
        rows="5"
        cols="40"
        required></textarea>

---

# 17. Multimedia

HTML5 allows audio and video to be embedded.

Example:

    <audio controls>
        <source
            src="audio/sample.mp3"
            type="audio/mpeg">
    </audio>

Video:

    <video controls width="640">
        <source
            src="video/sample.mp4"
            type="video/mp4">
    </video>

For the portfolio project, multimedia is included as a demonstration of HTML5 capabilities.

---

# 18. iFrame

An iframe can embed suitable external content.

Example:

    <iframe
        src="https://www.example.com"
        title="Example Website"
        width="600"
        height="300"
        loading="lazy">
    </iframe>

Not every external website permits iframe embedding.

---

# 19. Accessibility

The portfolio should follow basic accessibility practices.

Important points:

- Use semantic HTML
- Use meaningful headings
- Use labels for form inputs
- Use useful `alt` text
- Use descriptive links
- Give iframes meaningful titles
- Maintain logical structure

---

# 20. Semantic Structure

The portfolio uses:

    <header>
    <nav>
    <main>
    <section>
    <article>
    <aside>
    <footer>

This makes the document easier to understand.

---

# 21. Unique IDs

Each major section receives a unique ID.

Example:

    <section id="about">

    <section id="education">

    <section id="projects">

Navigation can then target these sections.

Example:

    <a href="#projects">Projects</a>

---

# 22. HTML and CSS Separation

This project intentionally uses HTML only.

HTML is responsible for:

- Structure
- Meaning
- Content

CSS will later be responsible for:

- Colors
- Fonts
- Spacing
- Layout
- Visual design

---

# 23. Why Build HTML First?

Building HTML before CSS helps understand the actual document structure.

A strong structure makes later CSS development easier.

The workflow becomes:

    HTML
      ↓
    CSS
      ↓
    JavaScript
      ↓
    Backend

---

# 24. Project Best Practices

The portfolio should:

1. Use valid HTML5 structure.
2. Use semantic elements.
3. Use meaningful headings.
4. Use unique IDs.
5. Use labels for forms.
6. Use appropriate input types.
7. Use useful `alt` text.
8. Use descriptive links.
9. Use tables only for tabular data.
10. Avoid deprecated HTML.
11. Keep indentation consistent.
12. Keep HTML readable.
13. Test the webpage in a browser.

---

# 25. Project Testing

After creating the webpage:

1. Save `index.html`.
2. Open it using Live Server.
3. Check every navigation link.
4. Test form validation.
5. Test the email field.
6. Test the phone field.
7. Check the image.
8. Check the table.
9. Check multimedia elements.
10. Check the iframe.
11. Inspect the page for HTML errors.

---

# 26. Final Project Architecture

The final page follows:

    <!DOCTYPE html>
        ↓
    html
        ↓
    head
        ↓
    body
        ↓
    header
        ↓
    nav
        ↓
    main
        ↓
    sections
        ↓
    footer

This is a practical application of the HTML fundamentals learned so far.

---

# 27. Key Takeaways

- A portfolio is a practical HTML project.
- Semantic HTML provides the page structure.
- Tables are useful for structured education data.
- Lists are useful for skills and learning journeys.
- Articles are useful for individual projects.
- Forms can collect contact information.
- HTML5 provides basic validation.
- Multimedia can be embedded using HTML elements.
- iFrames can embed supported external content.
- Accessibility should be considered while building the page.
- HTML provides structure; CSS will later provide presentation.

---

# 28. Project Outcome

After completing Day 018, the goal is to have a complete HTML-only personal portfolio that can later be enhanced with CSS and JavaScript.