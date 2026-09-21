# 📝 Day 067 — Static Files Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 067  
**Topic:** Flask Static Files — CSS, JavaScript & Images

---

## 🎯 Practice Goals

Practice serving and organizing CSS, JavaScript, and images in a Flask application.

---

## 🟢 Level 1 — Basic Questions

### Q1. What are static files?

Give three examples.

### Q2. What is the purpose of Flask's `static/` directory?

### Q3. What is the difference between `templates/` and `static/`?

### Q4. Where should CSS files normally be stored?

### Q5. Where should JavaScript files normally be stored?

### Q6. Where should images normally be stored?

---

## 🟡 Level 2 — Syntax Practice

### Q7. Write the Jinja2 syntax for loading:

- `style.css`
- `script.js`
- `profile.jpg`

Assume the following structure:

    static/
    ├── css/style.css
    ├── js/script.js
    └── images/profile.jpg

### Q8. Write the `url_for()` expression for:

    static/css/responsive.css

### Q9. Write an HTML `<img>` element that loads:

    static/images/logo.png

Use an appropriate `alt` attribute.

---

## 🟠 Level 3 — Flask Practice

Create this project:

    flask-static-practice/
    ├── app.py
    ├── templates/
    │   └── home.html
    └── static/
        ├── css/
        │   └── style.css
        ├── js/
        │   └── script.js
        └── images/
            └── logo.png

Create a Flask route:

    /

Render:

    home.html

Load the CSS and JavaScript using `url_for()`.

Display the image from the static directory.

---

## 🔴 Level 4 — Mini Project

### Student Learning Portal

Build a Flask page containing:

- Website header
- Navigation
- Student profile
- Course cards
- Learning progress
- Footer

Use:

    static/css/style.css

for styling.

Use:

    static/js/script.js

for an interactive button.

Use:

    static/images/

for at least one image.

---

## ⭐ Challenge

Combine Day 066 and Day 067.

Create:

    templates/
    ├── base.html
    ├── home.html
    ├── about.html
    └── courses.html

And:

    static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png

Requirements:

1. `base.html` contains the common layout.
2. All child templates extend `base.html`.
3. CSS is loaded from the static directory.
4. JavaScript is loaded from the static directory.
5. The logo is loaded from the static directory.
6. Use `url_for()` for all static assets.
7. Create a navigation bar.
8. Create at least three Flask routes.

---

## 🧠 Revision Questions

1. What is a static file?
2. What is the `static/` directory?
3. What is `url_for()`?
4. Why should static URLs use `url_for()`?
5. Where should CSS files be stored?
6. Where should JavaScript files be stored?
7. Where should images be stored?
8. What is the difference between `templates/` and `static/`?
9. Can sensitive information be stored in static files?
10. How do static files work with template inheritance?

---

## ✅ Completion Checklist

- [ ] I understand static files.
- [ ] I understand the `static/` directory.
- [ ] I can organize CSS files.
- [ ] I can organize JavaScript files.
- [ ] I can organize images.
- [ ] I understand `url_for()`.
- [ ] I can load CSS using Jinja2.
- [ ] I can load JavaScript using Jinja2.
- [ ] I can load images using Jinja2.
- [ ] I can combine static files with template inheritance.