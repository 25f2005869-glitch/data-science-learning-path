# ⚡ Day 066 — Template Inheritance Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 066  
**Topic:** Jinja2 Template Inheritance

---

## 🔹 Core Concept

Template Inheritance allows child templates to reuse a common base template.

**Base → Common Layout**

**Child → Specific Content**

---

## 🔹 Important Syntax

### Extend a Template

    {% extends "base.html" %}

### Create a Block

    {% block content %}
    {% endblock %}

### Output a Variable

    {{ name }}

### Jinja2 Comment

    {# This is a comment #}

### Keep Parent Block Content

    {{ super() }}

---

## 🔹 Basic Base Template

    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}Website{% endblock %}</title>
    </head>
    <body>

        <header>Header</header>

        <nav>Navigation</nav>

        <main>
            {% block content %}
            {% endblock %}
        </main>

        <footer>Footer</footer>

    </body>
    </html>

---

## 🔹 Basic Child Template

    {% extends "base.html" %}

    {% block title %}
        Home
    {% endblock %}

    {% block content %}
        <h1>Home Page</h1>
        <p>Welcome.</p>
    {% endblock %}

---

## 🔹 Multiple Blocks

    {% block title %}{% endblock %}

    {% block styles %}{% endblock %}

    {% block content %}{% endblock %}

    {% block scripts %}{% endblock %}

---

## 🔹 `super()`

Use `super()` when the child should keep the parent's block content.

    {% block content %}
        {{ super() }}
        <p>Extra content.</p>
    {% endblock %}

---

## 🔹 Flask Rendering

    from flask import render_template

    @app.route("/")
    def home():
        return render_template("home.html")

---

## 🔹 Recommended Structure

    project/
    ├── app.py
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── about.html
    │   └── contact.html
    └── static/

---

## 🔹 Syntax Comparison

| Syntax | Purpose |
|---|---|
| `{{ }}` | Output |
| `{% %}` | Jinja2 statement |
| `{# #}` | Jinja2 comment |
| `extends` | Inherit template |
| `block` | Define/override section |
| `endblock` | Close block |
| `super()` | Keep parent content |

---

## 🔹 Remember

**extends → Parent**

**block → Replaceable Area**

**endblock → Close Area**

**super() → Parent + Child**

**render_template() → Flask renders template**

---

## 🔹 Golden Rule

Create common HTML once in `base.html` and reuse it through child templates.