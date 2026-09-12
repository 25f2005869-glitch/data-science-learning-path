
## 2. `notes.md`

```markdown
# 📝 Day 017 — HTML Best Practices

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. What are HTML Best Practices?

HTML best practices are recommended ways of writing HTML that make webpages:

- Easy to understand
- Easy to maintain
- Accessible
- Consistent
- Reliable
- Easier to debug

A webpage can work correctly and still contain poorly written HTML.

Good HTML focuses on both functionality and code quality.

---

# 2. Use the HTML5 Document Structure

Start webpages with a standard HTML5 structure.

Example:

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Webpage</title>
    </head>

    <body>

        <h1>Hello World</h1>

    </body>

    </html>

This gives the browser the basic information it needs to interpret the document.

---

# 3. Always Use `<!DOCTYPE html>`

The `<!DOCTYPE html>` declaration tells the browser that the document should be interpreted using modern HTML standards.

Example:

    <!DOCTYPE html>

It should appear at the beginning of the HTML document.

---

# 4. Use the `lang` Attribute

Specify the primary language of the webpage.

Example:

    <html lang="en">

The language attribute helps:

- Screen readers
- Browsers
- Search engines
- Translation tools

---

# 5. Use Proper Indentation

Indent nested elements consistently.

Good example:

    <main>

        <section>

            <h2>Projects</h2>

            <p>
                My project information.
            </p>

        </section>

    </main>

Poor indentation makes code harder to read and maintain.

---

# 6. Use Semantic HTML

Prefer semantic elements when they accurately describe the content.

Examples:

- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<article>`
- `<aside>`
- `<footer>`

Example:

    <header>
        <h1>My Portfolio</h1>
    </header>

Instead of using generic containers everywhere:

    <div>
        <h1>My Portfolio</h1>
    </div>

Semantic HTML provides more meaning to the document structure.

---

# 7. Use Meaningful Headings

Headings should describe the content that follows them.

Example:

    <h1>Student Portfolio</h1>

    <h2>Education</h2>

    <h2>Skills</h2>

    <h2>Projects</h2>

Do not select heading levels only because of their visual size.

Heading levels represent document structure.

---

# 8. Maintain Heading Hierarchy

A logical hierarchy makes content easier to understand.

Example:

    <h1>My Portfolio</h1>

    <h2>Education</h2>

    <h3>Degree</h3>

    <h2>Projects</h2>

    <h3>Project 1</h3>

    <h3>Project 2</h3>

Avoid randomly jumping between heading levels when there is no structural reason.

---

# 9. Use Meaningful Attributes

Attributes should provide useful information.

Example:

    <img
        src="profile.jpg"
        alt="Student profile photograph">

Use meaningful values for:

- `id`
- `class`
- `alt`
- `title`
- `name`

Avoid confusing names such as:

    <div id="x123">

when a meaningful identifier would be more appropriate.

---

# 10. Use Classes for Reusable Styling

Classes are useful when multiple elements need the same styling or behavior.

Example:

    <p class="important">Important information.</p>

    <p class="important">Another important message.</p>

The same class can be reused.

An `id` should identify a unique element within a document.

---

# 11. Use IDs Carefully

An `id` should normally be unique within the document.

Example:

    <section id="projects">
        <h2>Projects</h2>
    </section>

A link can point to it:

    <a href="#projects">Projects</a>

Do not assign the same `id` to multiple elements.

---

# 12. Write Useful `alt` Text

Images should have appropriate alternative text.

Example:

    <img
        src="html-logo.png"
        alt="HTML5 logo">

The `alt` text describes the image when appropriate.

For a decorative image, an empty `alt` can be used:

    <img src="decorative-line.png" alt="">

Do not write unnecessary descriptions such as:

    alt="image"

when a meaningful description is available.

---

# 13. Use Labels for Form Inputs

Forms should have associated labels.

Good example:

    <label for="email">Email Address:</label>

    <input
        type="email"
        id="email"
        name="email">

The `for` value of the label matches the input's `id`.

This improves usability and accessibility.

---

# 14. Use Appropriate Input Types

Choose the input type according to the data.

Examples:

    <input type="email">

    <input type="number">

    <input type="date">

    <input type="url">

    <input type="tel">

Using the correct input type can provide better browser behavior and user experience.

---

# 15. Use `required` Carefully

Use `required` when a field genuinely needs a value.

Example:

    <input
        type="email"
        name="email"
        required>

Do not make every field required without a reason.

---

# 16. Use Descriptive Link Text

Links should describe their destination.

Good:

    <a href="projects.html">
        View My Projects
    </a>

Less useful:

    <a href="projects.html">
        Click Here
    </a>

Descriptive link text is better for users and accessibility.

---

# 17. Use `target="_blank"` Carefully

When opening a link in a new tab:

    <a
        href="https://example.com"
        target="_blank"
        rel="noopener noreferrer">

        Visit Website

    </a>

Using `rel="noopener noreferrer"` is a useful security and privacy practice when opening external pages in a new browsing context.

---

# 18. Use Tables for Tabular Data

Tables should represent data that naturally belongs in rows and columns.

Good examples:

- Student marks
- Product prices
- Exam schedules
- Financial data

Do not use tables to create the layout of a webpage.

Use CSS for webpage layout.

---

# 19. Use Table Headers

Use `<th>` for table headings.

Example:

    <table>

        <tr>
            <th>Name</th>
            <th>Marks</th>
        </tr>

        <tr>
            <td>Saloni</td>
            <td>95</td>
        </tr>

    </table>

Headers make tables easier to understand.

---

# 20. Use `<caption>` for Tables When Appropriate

A table can have a meaningful caption.

Example:

    <table>

        <caption>
            Student Examination Results
        </caption>

    </table>

The caption describes what the table represents.

---

# 21. Avoid Deprecated HTML

Avoid old HTML elements and presentation attributes that are no longer recommended.

Examples to avoid:

    <center>
    <font>
    <marquee>

Also avoid using HTML attributes for presentation when CSS should be used.

For example, prefer CSS rather than:

    <body bgcolor="yellow">

HTML should describe structure and meaning.

CSS should handle presentation and styling.

---

# 22. Keep HTML and CSS Separate

HTML should primarily describe structure.

CSS should handle visual presentation.

HTML:

    <h1>Student Portfolio</h1>

CSS can control:

- Color
- Font
- Spacing
- Layout
- Borders
- Background

This separation makes projects easier to maintain.

---

# 23. Avoid Unnecessary `<div>` Elements

Do not create large numbers of meaningless containers.

Instead of:

    <div>
        <div>
            <div>
                <h2>Projects</h2>
            </div>
        </div>
    </div>

Prefer meaningful structure:

    <section>
        <h2>Projects</h2>
    </section>

Use `<div>` when a generic container is actually needed.

---

# 24. Write Comments Carefully

Comments can explain important parts of code.

Example:

    <!-- Projects Section -->

    <section id="projects">
        ...
    </section>

Avoid comments that simply repeat obvious code.

Good comments explain intent or important decisions.

---

# 25. Use Lowercase HTML

HTML is generally written using lowercase element and attribute names.

Recommended:

    <h1>My Website</h1>

    <p class="intro">Welcome.</p>

Avoid inconsistent casing such as:

    <H1>My Website</H1>

Consistent formatting improves readability.

---

# 26. Quote Attribute Values

Use quotes around attribute values.

Recommended:

    <input type="text" id="name">

Avoid:

    <input type=text id=name>

Quoted values are clearer and follow common HTML coding conventions.

---

# 27. Close Elements Correctly

Normal HTML elements should have proper opening and closing tags.

Example:

    <p>
        This is a paragraph.
    </p>

Void elements such as `<img>` and `<input>` do not need closing tags.

Examples:

    <img src="photo.jpg" alt="Profile photo">

    <input type="text">

---

# 28. Use Meaningful Page Titles

Every webpage should have a useful `<title>`.

Example:

    <title>Student Portfolio | Saloni Tiwari</title>

The title appears in places such as the browser tab and can help users and search engines understand the page.

---

# 29. Use Meta Viewport

For responsive webpages, include:

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

This helps webpages behave properly on different device sizes.

---

# 30. Validate HTML

HTML validation can help find:

- Missing attributes
- Incorrect nesting
- Invalid markup
- Structural problems

Validation is useful during development.

However, a validator is a tool for finding problems; it does not replace understanding HTML semantics and accessibility.

---

# 31. Check HTML Nesting

Elements should be nested logically.

Correct:

    <p>
        This is <strong>important</strong>.
    </p>

Incorrect nesting can create unexpected browser behavior.

Always keep opening and closing relationships clear.

---

# 32. Avoid Duplicate IDs

Incorrect:

    <p id="student">Student One</p>

    <p id="student">Student Two</p>

The same ID should not be reused within the same document.

Use a class if multiple elements share the same category.

Example:

    <p class="student">Student One</p>

    <p class="student">Student Two</p>

---

# 33. Use External Resources Carefully

When using external:

- Images
- Audio
- Video
- iFrames
- Scripts

make sure the source is trustworthy and appropriate.

External resources can affect:

- Performance
- Privacy
- Security
- Availability

---

# 34. Optimize Multimedia

Large multimedia files can slow down webpages.

Good practices include:

- Use appropriate file formats
- Compress large files
- Avoid unnecessary autoplay
- Use suitable image dimensions
- Lazy-load suitable off-screen content

---

# 35. Accessibility Should Be Considered From the Beginning

Accessibility should not be added only at the end.

Start with:

- Semantic HTML
- Proper labels
- Useful `alt` text
- Logical headings
- Descriptive links
- Keyboard-friendly controls

Good HTML provides a strong accessibility foundation.

---

# 36. HTML Best Practices Checklist

Before considering an HTML page complete, check:

    ✓ DOCTYPE is present
    ✓ lang attribute is present
    ✓ Character encoding is defined
    ✓ Viewport meta tag is included
    ✓ Page has a meaningful title
    ✓ Semantic elements are used
    ✓ Headings follow a logical structure
    ✓ Images have appropriate alt text
    ✓ Forms have labels
    ✓ Correct input types are used
    ✓ Links have descriptive text
    ✓ Tables are used for tabular data
    ✓ IDs are unique
    ✓ HTML is properly nested
    ✓ Indentation is consistent
    ✓ Deprecated elements are avoided
    ✓ HTML and CSS responsibilities are separated
    ✓ Code is validated and tested

---

# 37. Golden Rules

Remember these rules:

1. Write HTML for structure and meaning.
2. Use semantic elements whenever appropriate.
3. Keep the code readable.
4. Use meaningful names.
5. Use proper heading hierarchy.
6. Make forms accessible.
7. Provide useful alternative text for informative images.
8. Use descriptive link text.
9. Use tables only for tabular data.
10. Avoid deprecated HTML.
11. Keep IDs unique.
12. Use CSS for presentation.
13. Validate and test your HTML.
14. Think about accessibility while writing the page.

---

# 38. Key Takeaways

Good HTML is not just HTML that works.

Professional HTML should be:

- Semantic
- Accessible
- Readable
- Maintainable
- Valid
- Meaningful
- Consistent

Following these practices creates a strong foundation for CSS, JavaScript, and later web application development.