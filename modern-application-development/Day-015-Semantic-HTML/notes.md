
## 2. `notes.md`

```markdown
# 📝 Day 015 — Semantic HTML

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. What is Semantic HTML?

Semantic HTML means using HTML elements that clearly describe the meaning and purpose of their content.

The word "semantic" means "related to meaning."

For example:

    <header>

clearly tells us that the content belongs to the header area.

Similarly:

    <footer>

clearly represents footer content.

---

# 2. Why Use Semantic HTML?

Semantic HTML provides a clear structure for webpages.

It helps:

- Developers understand the code
- Browsers understand document structure
- Search engines understand content
- Screen readers navigate webpages
- Users with accessibility needs
- Developers maintain the project

---

# 3. Semantic Elements

Important semantic elements include:

- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<article>`
- `<aside>`
- `<footer>`
- `<figure>`
- `<figcaption>`

---

# 4. `<header>`

The `<header>` element represents introductory content for a page or a section.

It can contain:

- Logo
- Heading
- Introduction
- Navigation
- Other introductory information

Example:

    <header>
        <h1>My Portfolio</h1>
        <p>Welcome to my website.</p>
    </header>

A page can have a header, and individual sections can also have their own headers.

---

# 5. `<nav>`

The `<nav>` element represents a section containing navigation links.

Example:

    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Projects</a>
        <a href="#">Contact</a>
    </nav>

The `<nav>` element tells browsers and assistive technologies that these links are part of navigation.

---

# 6. `<main>`

The `<main>` element contains the primary content of the webpage.

Example:

    <main>
        <h2>About Me</h2>
        <p>This is the main content of my webpage.</p>
    </main>

A document should normally have one main content area.

The main content should be different from repeated content such as navigation, sidebars, and footers.

---

# 7. `<section>`

The `<section>` element represents a meaningful standalone section of content.

Example:

    <section>
        <h2>Education</h2>
        <p>I am studying Data Science.</p>
    </section>

A section generally has a heading that describes its content.

Examples:

- Education
- Skills
- Projects
- Experience
- Contact

---

# 8. `<article>`

The `<article>` element represents independent or self-contained content.

Examples include:

- Blog post
- News article
- Forum post
- Product review
- Independent publication

Example:

    <article>
        <h2>My First Web Project</h2>
        <p>I created my first HTML project.</p>
    </article>

An article should make sense as a separate piece of content.

---

# 9. `<aside>`

The `<aside>` element represents content related to the surrounding content but not part of its main flow.

Examples:

- Sidebar
- Related links
- Author information
- Additional resources
- Advertisements

Example:

    <aside>
        <h2>Related Topics</h2>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </aside>

---

# 10. `<footer>`

The `<footer>` element represents footer information for a page or section.

It may contain:

- Copyright information
- Contact information
- Related links
- Author information
- Additional navigation

Example:

    <footer>
        <p>© 2026 My Portfolio</p>
    </footer>

---

# 11. `<figure>`

The `<figure>` element represents self-contained content such as:

- Image
- Diagram
- Illustration
- Code example
- Chart

Example:

    <figure>
        <img src="html-logo.png" alt="HTML5 Logo">
    </figure>

---

# 12. `<figcaption>`

The `<figcaption>` element provides a caption for content inside a `<figure>`.

Example:

    <figure>
        <img src="html-logo.png" alt="HTML5 Logo">
        <figcaption>HTML5 Logo</figcaption>
    </figure>

The caption explains or describes the figure.

---

# 13. Semantic vs Non-Semantic Elements

## Semantic Elements

Semantic elements communicate meaning.

Examples:

    <header>
    <nav>
    <main>
    <section>
    <article>
    <aside>
    <footer>

## Non-Semantic Elements

Non-semantic elements do not describe the meaning of their content.

Examples:

    <div>
    <span>

These elements are useful for grouping and styling content, but they do not tell us what the content represents.

---

# 14. `<div>` vs `<section>`

`<div>` is a generic container.

Example:

    <div>
        <h2>Projects</h2>
        <p>My projects are listed here.</p>
    </div>

`<section>` represents a meaningful section.

Example:

    <section>
        <h2>Projects</h2>
        <p>My projects are listed here.</p>
    </section>

Use `<section>` when the content represents a meaningful section.

Use `<div>` when a generic container is needed and no semantic element is appropriate.

---

# 15. `<span>`

`<span>` is a generic inline container.

Example:

    <p>
        My favourite language is
        <span>Python</span>.
    </p>

It is commonly used when a small piece of inline content needs styling or scripting.

---

# 16. Basic Semantic Page Structure

A typical semantic webpage can look like:

    <header>
        Website Header
    </header>

    <nav>
        Navigation Links
    </nav>

    <main>

        <section>
            Main Section
        </section>

        <article>
            Independent Article
        </article>

        <aside>
            Related Information
        </aside>

    </main>

    <footer>
        Footer Information
    </footer>

---

# 17. Semantic HTML and Accessibility

Semantic HTML helps assistive technologies understand the structure of a webpage.

For example, a screen reader can recognize:

- Navigation
- Main content
- Sections
- Articles
- Footer

This makes navigation easier for users who rely on assistive technologies.

Semantic HTML does not automatically make every webpage fully accessible, but it provides a strong foundation.

---

# 18. Semantic HTML and SEO

Search engines need to understand webpage content.

Meaningful HTML structure can help search engines understand:

- Main content
- Sections
- Articles
- Navigation
- Supporting information

Semantic HTML is therefore useful for creating well-structured webpages.

However, semantic HTML alone does not guarantee higher search rankings.

---

# 19. Multiple Semantic Elements

A webpage can contain multiple sections and articles.

Example:

    <main>

        <section>
            <h2>Projects</h2>

            <article>
                <h3>Student Dashboard</h3>
                <p>Project description.</p>
            </article>

            <article>
                <h3>Economic Dashboard</h3>
                <p>Project description.</p>
            </article>

        </section>

    </main>

Here:

- `<main>` contains the primary page content.
- `<section>` groups project content.
- Each `<article>` represents an individual project.

---

# 20. Semantic HTML Best Practices

1. Use elements according to their meaning.
2. Use `<main>` for the primary page content.
3. Use `<nav>` for major navigation links.
4. Give sections meaningful headings.
5. Use `<article>` for independent content.
6. Use `<aside>` for related content.
7. Use `<figure>` and `<figcaption>` for figures with captions.
8. Use `<div>` when no suitable semantic element exists.
9. Do not use semantic elements only for styling.
10. Use meaningful `alt` text for informative images.

---

# 21. Complete Semantic Example

Example:

    <header>
        <h1>Student Portfolio</h1>
    </header>

    <nav>
        <a href="#">Home</a>
        <a href="#">Projects</a>
        <a href="#">Contact</a>
    </nav>

    <main>

        <section>
            <h2>About Me</h2>
            <p>I am learning web development.</p>
        </section>

        <section>
            <h2>Projects</h2>

            <article>
                <h3>Student Dashboard</h3>
                <p>A dashboard project using web technologies.</p>
            </article>

        </section>

        <aside>
            <h2>Skills</h2>
            <p>HTML, CSS and JavaScript.</p>
        </aside>

    </main>

    <footer>
        <p>© 2026 Student Portfolio</p>
    </footer>

---

# 22. Important Differences

## `<section>` vs `<article>`

`<section>`:

- Groups related content
- Usually has a heading
- Represents a meaningful section

`<article>`:

- Represents independent content
- Can make sense by itself
- Useful for posts, reviews, news, projects, etc.

---

## `<header>` vs `<footer>`

`<header>`:

- Introductory content
- Heading
- Logo
- Navigation or introduction

`<footer>`:

- Closing information
- Copyright
- Contact details
- Related links

---

## `<div>` vs Semantic Elements

`<div>`:

- Generic container
- Does not communicate meaning

Semantic element:

- Communicates meaning
- Gives the document clearer structure

---

# 23. Key Takeaways

- Semantic HTML uses elements according to their meaning.
- `<header>` represents introductory content.
- `<nav>` represents navigation.
- `<main>` contains primary content.
- `<section>` groups related content.
- `<article>` represents independent content.
- `<aside>` contains related or supplementary content.
- `<footer>` represents footer information.
- `<figure>` represents self-contained content.
- `<figcaption>` provides a figure caption.
- `<div>` and `<span>` are generic containers.
- Semantic HTML improves structure and accessibility.
- Semantic HTML can help search engines understand content.
- Semantic HTML should be used for meaning, not simply for styling.