# 📘 Day 005 - HTML Headings and Paragraphs

Welcome to **Day 005**.

Today, we will learn how to structure text on a webpage using headings and paragraphs.

---

# What are HTML Headings?

HTML provides **six levels of headings**.

They are:

```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

- `<h1>` is the largest and most important heading.
- `<h6>` is the smallest heading.

---

# Best Practice

Use only **one `<h1>`** per webpage.

Organize content like this:

```
h1
 ├── h2
 │    ├── h3
 │    └── h3
 └── h2
```

---

# What is a Paragraph?

The `<p>` tag is used to write paragraphs.

Example

```html
<p>This is a paragraph.</p>
```

The browser automatically adds space before and after each paragraph.

---

# Line Break

The `<br>` tag moves text to the next line.

Example

```html
HTML<br>
CSS<br>
JavaScript
```

Output

```
HTML
CSS
JavaScript
```

---

# Horizontal Rule

The `<hr>` tag creates a horizontal line.

Example

```html
<hr>
```

It is commonly used to separate sections.

---

# Difference

Paragraph

```html
<p>Hello World</p>
```

Line Break

```html
Hello<br>World
```

Horizontal Rule

```html
<hr>
```

---

# Heading Hierarchy

Correct

```html
<h1>Main Title</h1>

<h2>Section</h2>

<h3>Subsection</h3>
```

Avoid

```html
<h1>Main Title</h1>

<h4>Section</h4>
```

Always maintain the correct hierarchy.

---

# Summary

Today you learned

- h1 to h6
- Paragraph
- br
- hr
- Heading Hierarchy
- Best Practices

Congratulations!