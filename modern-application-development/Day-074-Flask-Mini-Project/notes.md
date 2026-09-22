# 📚 Day 074 — Flask Mini Project Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 074  
**Topic:** Flask Mini Project

---

## 1. Project Overview

The **Student Learning Portal** is a small Flask application that combines the concepts learned during the Flask section.

The application allows students to:

- View the home page.
- View courses.
- Open individual course pages.
- Register as a student.
- Submit form data.
- Receive a success response.
- Navigate between pages.
- Handle invalid URLs.

---

## 2. Flask Application

A basic Flask application starts with:

    from flask import Flask

    app = Flask(__name__)

The Flask object represents the application.

---

## 3. Basic Route

The home page can be created with:

    @app.route("/")
    def home():
        return "Student Learning Portal"

The browser sends a request to `/`, and Flask executes the `home()` function.

---

## 4. Dynamic Route

A dynamic route can display a specific course.

Example:

    @app.route("/course/<course_name>")
    def course(course_name):
        return f"Course: {course_name}"

A URL such as:

    /course/python

can produce:

    Course: python

---

## 5. Jinja2 Templates

Instead of writing HTML directly inside Python, Flask can render templates.

Example:

    from flask import render_template

    @app.route("/")
    def home():
        return render_template("index.html")

The HTML file is stored inside the `templates/` directory.

---

## 6. Passing Data to Templates

Python can send data to a Jinja2 template.

Example:

    @app.route("/student")
    def student():
        name = "Saloni"
        course = "Data Science"

        return render_template(
            "student.html",
            name=name,
            course=course
        )

The template can display the values.

---

## 7. Template Inheritance

A common layout can be stored in:

    base.html

Child templates can extend it.

Example:

    {% extends "base.html" %}

    {% block content %}
    Student Learning Portal
    {% endblock %}

This avoids repeating common HTML.

---

## 8. Forms

The project contains a student registration form.

Example:

    <form method="POST">
        <input type="text" name="name" required>
        <input type="email" name="email" required>
        <button type="submit">Register</button>
    </form>

The `name` attribute is important because Flask uses it to identify submitted fields.

---

## 9. GET and POST

GET is commonly used for retrieving information.

POST is commonly used for submitting data.

Example:

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            name = request.form.get("name")

            return "Registration successful"

        return render_template("register.html")

---

## 10. Request Data

Flask provides the `request` object.

Form data:

    request.form

Query parameters:

    request.args

Request method:

    request.method

Example:

    name = request.form.get("name")

Using `.get()` helps avoid an exception when a key is missing.

---

## 11. Redirects

After successful form submission, redirecting to another page is useful.

Example:

    return redirect(url_for("success"))

This separates the submission request from the success page.

---

## 12. Post/Redirect/Get

The common form workflow is:

    User opens form
            ↓
        GET request
            ↓
       Form displayed
            ↓
      User submits form
            ↓
        POST request
            ↓
       Process the data
            ↓
        Redirect
            ↓
       Success page

This pattern is called **Post/Redirect/Get (PRG)**.

---

## 13. `url_for()`

`url_for()` generates URLs using endpoint names.

Example:

    @app.route("/success")
    def success():
        return "Success"

A redirect can use:

    redirect(url_for("success"))

This is better than manually writing URLs throughout the application.

---

## 14. Blueprints

A Blueprint helps organize routes into modules.

Example:

    from flask import Blueprint

    student_bp = Blueprint(
        "students",
        __name__,
        url_prefix="/students"
    )

Then a route can be created:

    @student_bp.route("/profile")
    def profile():
        return "Student Profile"

The Blueprint is registered with the application.

---

## 15. Error Handling

The project can define custom 404 and 500 handlers.

Example:

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

This gives users a friendly error page.

---

## 16. `abort()`

A route can intentionally return an HTTP error.

Example:

    from flask import abort

    @app.route("/course/<int:course_id>")
    def course(course_id):
        if course_id not in [1, 2, 3]:
            abort(404)

        return f"Course ID: {course_id}"

---

## 17. Configuration

The application can have configuration values.

Example:

    class Config:
        APP_NAME = "Student Learning Portal"
        DEBUG = False

Load the configuration:

    app.config.from_object(Config)

---

## 18. Environment Variables

Sensitive or environment-specific values should be outside the source code.

Example:

    import os

    secret_key = os.environ.get("SECRET_KEY")

Then:

    app.config["SECRET_KEY"] = secret_key

---

## 19. `.env`

For local development, environment variables may be stored in a `.env` file.

Example:

    SECRET_KEY=development-secret
    APP_NAME=Student Learning Portal

Real secrets should never be committed to a public repository.

---

## 20. Project Request Flow

A typical request flow is:

    Browser
       ↓
    Flask Application
       ↓
    Route
       ↓
    View Function
       ↓
    Application Logic
       ↓
    Jinja2 Template
       ↓
    HTML Response
       ↓
    Browser

---

## 21. Project Architecture

A clean Flask project separates responsibilities.

### Routes

Handle incoming requests.

### Templates

Handle HTML presentation.

### Static Files

Contain CSS, JavaScript, and images.

### Configuration

Controls application settings.

### Blueprints

Organize related routes.

### Error Handlers

Handle HTTP errors.

---

## 22. Validation

Forms should validate user input.

Examples:

- Name should not be empty.
- Email should have a valid format.
- Course should be selected.
- Marks should be within a valid range.

Validation should happen on the server even when browser-side validation exists.

---

## 23. Security Considerations

The mini project should:

- Validate submitted data.
- Avoid exposing secrets.
- Avoid debug mode in production.
- Keep `.env` out of Git.
- Escape template output appropriately.
- Use HTTPS in production.
- Avoid trusting client-side validation alone.

---

## 24. What This Project Combines

| Previous Day | Concept |
|---|---|
| Day 061 | Flask Introduction |
| Day 062 | Installation and Structure |
| Day 063 | Routing |
| Day 064 | Dynamic Routes |
| Day 065 | Jinja2 |
| Day 066 | Template Inheritance |
| Day 067 | Static Files |
| Day 068 | Forms and Request Methods |
| Day 069 | GET and POST |
| Day 070 | Redirects and `url_for()` |
| Day 071 | Blueprints |
| Day 072 | Error Handling |
| Day 073 | Configuration |

---

## ⭐ Key Takeaway

This mini project is important because it connects individual Flask concepts into one application.

The main idea is:

    Request
       ↓
    Route
       ↓
    Logic
       ↓
    Template
       ↓
    Response

A well-structured Flask application keeps routing, templates, configuration, static files, and error handling organized.