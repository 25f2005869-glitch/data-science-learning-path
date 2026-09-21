# ⚡ Day 067 — Static Files Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 067  
**Topic:** Flask Static Files — CSS, JavaScript & Images

---

## 🔹 Static Files

Static files are frontend assets such as:

- CSS
- JavaScript
- Images
- Fonts
- Icons
- Documents

---

## 🔹 Standard Structure

    project/
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

---

## 🔹 CSS

File:

    static/css/style.css

Template:

    <link rel="stylesheet"
          href="{{ url_for('static', filename='css/style.css') }}">

---

## 🔹 JavaScript

File:

    static/js/script.js

Template:

    <script
        src="{{ url_for('static', filename='js/script.js') }}">
    </script>

---

## 🔹 Image

File:

    static/images/logo.png

Template:

    <img
        src="{{ url_for('static', filename='images/logo.png') }}"
        alt="Website Logo"
    >

---

## 🔹 `url_for()`

Basic pattern:

    {{ url_for('static', filename='PATH') }}

Examples:

    {{ url_for('static', filename='css/style.css') }}

    {{ url_for('static', filename='js/script.js') }}

    {{ url_for('static', filename='images/logo.png') }}

---

## 🔹 Static vs Templates

| Directory | Purpose |
|---|---|
| `templates/` | Jinja2 HTML templates |
| `static/` | CSS, JS, images and assets |

---

## 🔹 Flask Application

    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html")

---

## 🔹 Template Inheritance

Base template:

    {% block styles %}
    {% endblock %}

Child template:

    {% block styles %}
        <link rel="stylesheet"
              href="{{ url_for('static', filename='css/page.css') }}">
    {% endblock %}

---

## 🔹 Important Rule

Do not normally put CSS, JavaScript, or images inside:

    templates/

Put them inside:

    static/

---

## 🔹 Common Errors

Wrong:

    {{ url_for('css/style.css') }}

Correct:

    {{ url_for('static', filename='css/style.css') }}

Wrong:

    static/style.css

when the actual file is:

    static/css/style.css

Correct filename:

    css/style.css

---

## 🔹 Security

Do not store secrets in:

    static/

Never put passwords, API keys, or private credentials in static files.

---

## 🧠 Remember

**templates → Jinja2**

**static → Assets**

**url_for() → Generate URLs**

**css/ → CSS**

**js/ → JavaScript**

**images/ → Images**