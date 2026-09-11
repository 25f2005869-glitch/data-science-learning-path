# 📘 Day 009 - Semantic HTML

## What is Semantic HTML?

Semantic HTML means using HTML elements that clearly describe the meaning and purpose of their content.

For example:

```html
<header>
    Website Header
</header>
```

The `<header>` element tells us that this content is the header of the webpage.

---

# Why Use Semantic HTML?

Semantic HTML helps:

- Developers understand the code
- Browsers understand page structure
- Search engines understand content
- Screen readers navigate the page
- Maintain clean and organized code

---

# Common Semantic Elements

## 1. `<header>`

Represents introductory content or the header of a webpage or section.

```html
<header>
    <h1>My Website</h1>
</header>
```

---

## 2. `<nav>`

Contains navigation links.

```html
<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Contact</a>
</nav>
```

---

## 3. `<main>`

Contains the main content of the webpage.

```html
<main>
    <h2>Main Content</h2>
    <p>This is the main content.</p>
</main>
```

A page should normally have one main content area.

---

## 4. `<section>`

Represents a thematic section of content.

```html
<section>
    <h2>About Me</h2>
    <p>This section contains information about me.</p>
</section>
```

---

## 5. `<article>`

Represents independent content that can stand on its own.

Examples:

- Blog post
- News article
- Forum post
- Product review

```html
<article>
    <h2>My First Blog Post</h2>
    <p>This is my article.</p>
</article>
```

---

## 6. `<aside>`

Contains related or secondary content.

Examples:

- Sidebar
- Related links
- Advertisements
- Additional information

```html
<aside>
    <h3>Related Links</h3>
    <a href="#">HTML Tutorial</a>
</aside>
```

---

## 7. `<footer>`

Represents the footer of a webpage or section.

```html
<footer>
    <p>© 2026 My Website</p>
</footer>
```

---

# Figure and Figcaption

## `<figure>`

Used for self-contained content such as images, diagrams, or illustrations.

```html
<figure>
    <img src="image.jpg" alt="Example">
</figure>
```

## `<figcaption>`

Provides a caption for the figure.

```html
<figure>

    <img src="image.jpg" alt="HTML Logo">

    <figcaption>
        HTML5 Logo
    </figcaption>

</figure>
```

---

# Semantic Page Structure

A common webpage structure looks like this:

```text
<header>
    Website Header
</header>

<nav>
    Navigation
</nav>

<main>

    <section>
        Main Section

        <article>
            Article
        </article>

    </section>

    <aside>
        Sidebar
    </aside>

</main>

<footer>
    Footer
</footer>
```

---

# Semantic vs Non-Semantic

## Non-Semantic

```html
<div>
    Header
</div>

<div>
    Content
</div>

<div>
    Footer
</div>
```

`<div>` does not describe what the content means.

---

## Semantic

```html
<header>
    Header
</header>

<main>
    Content
</main>

<footer>
    Footer
</footer>
```

These elements clearly describe their purpose.

---

# `<div>` vs Semantic Elements

`<div>` is still useful.

Use semantic elements when the content has a clear meaning.

Use `<div>` when there is no more appropriate semantic element.

---

# Accessibility

Semantic HTML helps assistive technologies such as screen readers understand the structure of a webpage.

For example:

```html
<nav>
    ...
</nav>
```

allows a screen reader to recognize that the content is navigation.

---

# SEO

Semantic HTML can also help search engines better understand the structure and meaning of webpage content.

Semantic HTML is therefore useful for:

- Accessibility
- Maintainability
- SEO
- Code readability

---

# Summary

Today you learned:

- Semantic HTML
- Header
- Navigation
- Main
- Section
- Article
- Aside
- Footer
- Figure
- Figcaption
- Semantic vs Non-Semantic HTML

Congratulations! 🎉