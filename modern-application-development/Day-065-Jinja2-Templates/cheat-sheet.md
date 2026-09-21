# ⚡ Day 065 — Jinja2 Templates Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 065  
**Topic:** Jinja2 Templates

---

## 📦 Import

    from flask import Flask, render_template

---

## 📁 Template Folder

    project/
    │
    ├── app.py
    └── templates/
        └── index.html

---

## 🖥️ Render Template

    @app.route("/")
    def home():
        return render_template("index.html")

---

## 📤 Pass Variable

Python:

    return render_template(
        "index.html",
        name="Saloni"
    )

Jinja2:

    {{ name }}

---

## 📚 Multiple Variables

    return render_template(
        "index.html",
        name="Saloni",
        course="MAD1",
        score=95
    )

Template:

    {{ name }}
    {{ course }}
    {{ score }}

---

## 🧩 Dictionary

Python:

    student = {
        "name": "Saloni",
        "score": 95
    }

Template:

    {{ student.name }}

or:

    {{ student["name"] }}

---

## 🔢 Expression

    {{ 10 + 5 }}

    {{ score * 2 }}

---

## 🔀 Condition

    {% if score >= 50 %}
        Pass
    {% else %}
        Fail
    {% endif %}

---

## 🔁 Loop

    {% for course in courses %}
        <p>{{ course }}</p>
    {% endfor %}

---

## 🔢 Loop Index

    {% for course in courses %}
        {{ loop.index }}. {{ course }}
    {% endfor %}

---

## 🎨 Filters

    {{ name | upper }}

    {{ name | lower }}

    {{ name | title }}

    {{ courses | length }}

    {{ name | trim }}

---

## 💬 Comment

    {# This is a Jinja2 comment #}

---

## 🧬 Template Inheritance

    {% extends "base.html" %}

    {% block content %}
        <h1>Home Page</h1>
    {% endblock %}

---

## 🧠 Jinja2 Syntax

    {{ ... }}     → Expression

    {% ... %}     → Statement

    {# ... #}     → Comment

---

## 🔄 Flow

    Python Data
        ↓
    Flask
        ↓
    render_template()
        ↓
    Jinja2
        ↓
    HTML
        ↓
    Browser

---

## ⚠️ Common Errors

- Wrong `templates/` directory
- Missing `render_template`
- Incorrect `{{ }}` syntax
- Missing `{% endif %}`
- Missing `{% endfor %}`
- Mixing Python and Jinja2 syntax

---

## ⭐ Remember

    @app.route("/")
    def home():
        return render_template(
            "index.html",
            name="Saloni"
        )

Template:

    <h1>Hello, {{ name }}!</h1>