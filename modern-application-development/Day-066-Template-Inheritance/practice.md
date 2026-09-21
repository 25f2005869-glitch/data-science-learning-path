# 📝 Day 066 — Template Inheritance Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 066  
**Topic:** Jinja2 Template Inheritance

---

## 🎯 Practice Goals

Practice creating reusable Flask layouts using Jinja2 Template Inheritance.

---

## 🟢 Level 1 — Basic Questions

### Q1. What is Jinja2 Template Inheritance?

Explain the concept in your own words.

### Q2. What is a base template?

Explain its purpose.

### Q3. What is a child template?

Explain its purpose.

### Q4. What does `{% extends %}` do?

Write one example.

### Q5. What is the purpose of `{% block %}`?

Explain with an example.

### Q6. What is `{{ super() }}` used for?

---

## 🟡 Level 2 — Syntax Practice

### Q7. Create a base template containing:

- Header
- Navigation
- Main section
- Footer

Create a `content` block inside the main section.

### Q8. Create a child template that extends `base.html`.

Add:

- Page title
- Heading
- Paragraph

### Q9. Create three blocks in `base.html`:

- `title`
- `content`
- `scripts`

### Q10. Use `super()` in a child template.

Explain what happens when `super()` is used.

---

## 🟠 Level 3 — Flask Practice

Create the following project:

    flask-template-practice/
    ├── app.py
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── about.html
    │   └── contact.html
    └── static/

Create these routes:

    /
    /about
    /contact

Each route should render its corresponding child template.

All child templates must extend:

    base.html

---

## 🔴 Level 4 — Mini Project

### Student Learning Website

Build a small Flask website using template inheritance.

Create:

- `base.html`
- `home.html`
- `courses.html`
- `projects.html`
- `contact.html`

The base template should contain:

- Website title
- Navigation
- Header
- Main content block
- Footer

Each child template should contain different page-specific content.

---

## ⭐ Challenge

Add these blocks to `base.html`:

    title
    styles
    content
    scripts

Then create a child template that:

1. Extends `base.html`.
2. Changes the page title.
3. Adds page-specific content.
4. Adds extra CSS.
5. Adds page-specific JavaScript.
6. Uses `{{ super() }}` at least once.

---

## 🧠 Revision Questions

1. What is template inheritance?
2. Why do we use `base.html`?
3. What does `extends` mean?
4. What does `block` mean?
5. What is `super()`?
6. What is the difference between `{{ }}` and `{% %}`?
7. Where does Flask normally search for templates?
8. Why is template inheritance better than repeating HTML?
9. What is the DRY principle?
10. How does Flask render a child template?

---

## ✅ Completion Checklist

- [ ] I understand base templates.
- [ ] I understand child templates.
- [ ] I can use `{% extends %}`.
- [ ] I can create `{% block %}` sections.
- [ ] I understand `{{ super() }}`.
- [ ] I can organize Flask templates.
- [ ] I can create multiple child pages.
- [ ] I understand the DRY principle.
- [ ] I can build a reusable Flask layout.