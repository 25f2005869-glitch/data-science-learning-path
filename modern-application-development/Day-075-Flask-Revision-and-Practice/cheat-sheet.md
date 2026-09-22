# ⚡ Day 075 — Flask Revision Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 075  
**Topic:** Flask Revision and Practice

---

## 🔹 Create Flask App

    from flask import Flask

    app = Flask(__name__)

---

## 🔹 Basic Route

    @app.route("/")
    def home():
        return "Home"

---

## 🔹 Dynamic Route

    @app.route("/student/<student_name>")
    def student(student_name):
        return student_name

---

## 🔹 Route Converter

    @app.route("/student/<int:student_id>")

---

## 🔹 Render Template

    from flask import render_template

    return render_template(
        "index.html"
    )

---

## 🔹 Pass Data

    return render_template(
        "student.html",
        name="Saloni"
    )

Template:

    {{ name }}

---

## 🔹 Jinja2 Condition

    {% if marks >= 50 %}
        Passed
    {% else %}
        Failed
    {% endif %}

---

## 🔹 Jinja2 Loop

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

## 🔹 Static File

    {{ url_for(
        "static",
        filename="css/style.css"
    ) }}

---

## 🔹 GET / POST

    @app.route(
        "/register",
        methods=["GET", "POST"]
    )

---

## 🔹 Request Method

    request.method

---

## 🔹 Form Data

    request.form.get("name")

---

## 🔹 Query Parameter

    request.args.get("course")

---

## 🔹 Redirect

    return redirect(
        url_for("success")
    )

---

## 🔹 Dynamic URL

    url_for(
        "student",
        student_name="Saloni"
    )

---

## 🔹 Blueprint

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
        return "Not Found", 404

---

## 🔹 Abort

    abort(404)

---

## 🔹 Exception Handling

    try:
        operation()
    except ValueError:
        handle_error()
    finally:
        cleanup()

---

## 🔹 Debug Mode

    app.run(debug=True)

Development only.

---

## 🔹 Logging

    app.logger.info("Information")
    app.logger.warning("Warning")
    app.logger.error("Error")

---

## 🔹 Configuration

    app.config["APP_NAME"] = "Student Portal"

---

## 🔹 Configuration Class

    class Config:
        DEBUG = False
        TESTING = False

    app.config.from_object(Config)

---

## 🔹 Environment Variable

    import os

    value = os.environ.get("APP_NAME")

---

## 🔹 Secret Key

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY"
    )

---

## 🔹 PRG Pattern

    POST
      ↓
    Process
      ↓
    Redirect
      ↓
    GET

---

## 🔹 HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 500 | Internal Server Error |

---

## 🔹 Core Flask Objects

`Flask` → Creates application

`request` → Reads request data

`render_template()` → Renders HTML

`redirect()` → Redirects request

`url_for()` → Generates URLs

`Blueprint` → Organizes routes

`abort()` → Returns HTTP error

`app.config` → Stores configuration

---

## ⭐ Flask Mental Model

    Request
       ↓
    Route
       ↓
    Logic
       ↓
    Template
       ↓
    Response