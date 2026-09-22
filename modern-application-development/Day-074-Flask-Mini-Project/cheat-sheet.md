# ⚡ Day 074 — Flask Mini Project Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 074  
**Topic:** Flask Mini Project

---

## 🔹 Create Flask App

    from flask import Flask

    app = Flask(__name__)

---

## 🔹 Route

    @app.route("/")
    def home():
        return "Home Page"

---

## 🔹 Dynamic Route

    @app.route("/course/<course_name>")
    def course(course_name):
        return course_name

---

## 🔹 Render Template

    from flask import render_template

    return render_template("index.html")

---

## 🔹 Pass Data

    return render_template(
        "student.html",
        name="Saloni"
    )

---

## 🔹 Jinja2

    {{ name }}

    {% if condition %}
        Content
    {% endif %}

    {% for course in courses %}
        {{ course }}
    {% endfor %}

---

## 🔹 Template Inheritance

    {% extends "base.html" %}

    {% block content %}
        Page Content
    {% endblock %}

---

## 🔹 GET / POST

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            pass

        return render_template("register.html")

---

## 🔹 Form Data

    name = request.form.get("name")

---

## 🔹 Query Parameter

    search = request.args.get("search")

---

## 🔹 Redirect

    return redirect(url_for("success"))

---

## 🔹 URL Generation

    url_for("home")

    url_for("course", course_name="python")

---

## 🔹 Blueprint

    from flask import Blueprint

    student_bp = Blueprint(
        "students",
        __name__,
        url_prefix="/students"
    )

---

## 🔹 Register Blueprint

    app.register_blueprint(student_bp)

---

## 🔹 Error Handler

    @app.errorhandler(404)
    def not_found(error):
        return "Page not found", 404

---

## 🔹 Abort

    from flask import abort

    abort(404)

---

## 🔹 Configuration

    app.config["APP_NAME"] = "Student Portal"

---

## 🔹 Configuration Class

    class Config:
        DEBUG = False
        APP_NAME = "Student Portal"

    app.config.from_object(Config)

---

## 🔹 Environment Variable

    import os

    secret_key = os.environ.get("SECRET_KEY")

---

## 🔹 Secret Key

    app.config["SECRET_KEY"] = secret_key

---

## 🔹 Project Flow

    Browser
       ↓
    Request
       ↓
    Route
       ↓
    View Function
       ↓
    Logic
       ↓
    Jinja2 Template
       ↓
    Response

---

## 🔐 Important Security Rules

- Validate server-side input.
- Never expose real secrets.
- Keep `.env` out of Git.
- Disable debug mode in production.
- Use HTTPS in production.
- Do not trust client-side validation alone.

---

## ⭐ Core Flask Concepts

`route()` → Connect URL to function

`render_template()` → Render HTML template

`request.form` → Read form data

`request.args` → Read query parameters

`redirect()` → Redirect request

`url_for()` → Generate URL

`Blueprint` → Organize routes

`abort()` → Return HTTP error

`errorhandler()` → Customize error handling

`app.config` → Store configuration