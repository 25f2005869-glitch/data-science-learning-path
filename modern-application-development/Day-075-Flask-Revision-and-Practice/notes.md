# 📚 Day 075 — Flask Revision and Practice Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 075  
**Topic:** Flask Revision and Practice

---

# 1. What Is Flask?

Flask is a lightweight Python web framework used to build web applications and APIs.

A Flask application receives HTTP requests, processes them through routes and application logic, and returns HTTP responses.

Basic application:

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello Flask"

---

# 2. Flask Application Structure

A simple Flask project can contain:

    project/
    │
    ├── app.py
    ├── templates/
    ├── static/
    ├── .env
    ├── .gitignore
    └── requirements.txt

Larger applications can use Blueprints and an application factory.

---

# 3. Flask Installation

A virtual environment is recommended.

Create:

    python -m venv .venv

Activate on Windows:

    .venv\Scripts\activate

Install Flask:

    pip install flask

Check installation:

    flask --version

---

# 4. Routing

Routing connects a URL to a Python function.

Example:

    @app.route("/about")
    def about():
        return "About Page"

When the browser requests `/about`, Flask executes the `about()` function.

---

# 5. Dynamic Routes

Dynamic routes contain variable parts.

Example:

    @app.route("/student/<student_name>")
    def student(student_name):
        return f"Student: {student_name}"

The URL:

    /student/Saloni

produces:

    Student: Saloni

---

# 6. Route Converters

Flask supports route converters.

Examples:

    /student/<int:student_id>

    /price/<float:amount>

    /files/<path:file_path>

The converter controls what kind of value can be accepted.

---

# 7. URL Parameters vs Query Parameters

URL parameter:

    /student/10

Route:

    /student/<int:student_id>

Query parameter:

    /students?course=python

Read query parameters using:

    request.args.get("course")

---

# 8. HTTP Methods

Common HTTP methods include:

- GET
- POST
- PUT
- PATCH
- DELETE

In beginner Flask applications, GET and POST are especially important.

GET is commonly used to retrieve information.

POST is commonly used to submit data.

---

# 9. Request Object

Flask provides the `request` object.

Example:

    from flask import request

Form data:

    request.form.get("name")

Query parameter:

    request.args.get("course")

HTTP method:

    request.method

---

# 10. HTML Forms

A form collects user input.

Example:

    <form method="POST">
        <input type="text" name="name" required>
        <button type="submit">Submit</button>
    </form>

The `name` attribute identifies the submitted field.

---

# 11. GET and POST Form Flow

A registration page often works like this:

    GET
     ↓
    Display Form
     ↓
    User Enters Data
     ↓
    POST
     ↓
    Validate Data
     ↓
    Process Data
     ↓
    Redirect
     ↓
    Success Page

---

# 12. Jinja2

Jinja2 is Flask's template engine.

It allows Python data to be inserted into HTML.

Example:

    return render_template(
        "student.html",
        name="Saloni"
    )

Template:

    <h1>Welcome, {{ name }}</h1>

---

# 13. Jinja2 Expressions

Variables:

    {{ student_name }}

Expression:

    {{ marks + 5 }}

Condition:

    {% if marks >= 50 %}
        Passed
    {% endif %}

Loop:

    {% for course in courses %}
        {{ course }}
    {% endfor %}

---

# 14. Template Inheritance

A common layout can be placed in `base.html`.

Child template:

    {% extends "base.html" %}

    {% block content %}
        Student Dashboard
    {% endblock %}

This avoids repeating common HTML.

---

# 15. Static Files

Static files include:

- CSS
- JavaScript
- Images
- Fonts

They are commonly stored inside:

    static/

Flask can generate a static URL using:

    url_for("static", filename="css/style.css")

---

# 16. Redirects

Flask provides `redirect()`.

Example:

    from flask import redirect

    return redirect("/success")

A better approach is:

    return redirect(url_for("success"))

---

# 17. `url_for()`

`url_for()` generates URLs using endpoint names.

Example:

    @app.route("/success")
    def success():
        return "Success"

Then:

    url_for("success")

For dynamic routes:

    url_for(
        "student",
        student_name="Saloni"
    )

---

# 18. Post/Redirect/Get

Post/Redirect/Get, or PRG, is a useful form-processing pattern.

Flow:

    POST
     ↓
    Process Data
     ↓
    Redirect
     ↓
    GET Success Page

It helps prevent accidental form resubmission when a user refreshes the success page.

---

# 19. Blueprints

Blueprints divide a Flask application into logical modules.

Example:

    from flask import Blueprint

    student_bp = Blueprint(
        "students",
        __name__,
        url_prefix="/students"
    )

Route:

    @student_bp.route("/profile")
    def profile():
        return "Student Profile"

Register:

    app.register_blueprint(student_bp)

---

# 20. Error Handling

Flask can handle HTTP errors using custom error handlers.

Example:

    @app.errorhandler(404)
    def not_found(error):
        return "Page not found", 404

Common errors:

- 400 Bad Request
- 403 Forbidden
- 404 Not Found
- 405 Method Not Allowed
- 500 Internal Server Error

---

# 21. `abort()`

`abort()` immediately returns an HTTP error.

Example:

    from flask import abort

    if student_not_found:
        abort(404)

---

# 22. Python Exception Handling

Expected Python exceptions can be handled with:

    try:
        result = 10 / 0
    except ZeroDivisionError:
        result = 0

The `finally` block runs whether an exception occurs or not.

---

# 23. Debugging

During development, Flask can provide detailed debugging information.

Example:

    app.run(debug=True)

Debug mode is useful during development but should not be exposed in production.

---

# 24. Tracebacks

A traceback helps locate the source of a Python error.

It can show:

- File
- Line number
- Function
- Exception type
- Error message

A good debugging process is:

    Reproduce
       ↓
    Read error
       ↓
    Check traceback
       ↓
    Locate problem
       ↓
    Fix
       ↓
    Test

---

# 25. Logging

Flask provides application logging.

Examples:

    app.logger.debug("Debug information")
    app.logger.info("Student requested")
    app.logger.warning("Invalid input")
    app.logger.error("Operation failed")

Logging helps developers understand application behavior.

---

# 26. Flask Configuration

Flask provides:

    app.config

Example:

    app.config["APP_NAME"] = "Student Portal"

Multiple values:

    app.config.from_mapping(
        DEBUG=True,
        APP_NAME="Student Portal"
    )

---

# 27. Configuration Classes

Configuration can be organized into classes.

Example:

    class Config:
        DEBUG = False
        TESTING = False
        APP_NAME = "Student Portal"

Load it:

    app.config.from_object(Config)

Different environments can have different configuration classes.

---

# 28. Environment Variables

Environment variables allow configuration to be supplied outside the source code.

Example:

    import os

    secret_key = os.environ.get("SECRET_KEY")

This is especially useful for secrets and deployment-specific settings.

---

# 29. `.env`

A local `.env` file may contain:

    SECRET_KEY=development-secret
    DATABASE_URL=sqlite:///students.db

Sensitive `.env` files should not be committed to a public repository.

Example `.gitignore`:

    .env
    .venv/
    __pycache__/
    *.pyc

---

# 30. SECRET_KEY

Flask uses `SECRET_KEY` for security-related features such as signing session-related data.

Example:

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY"
    )

The value should be strong and private.

---

# 31. Development vs Production

Development:

- Debugging enabled when needed.
- Detailed errors useful.
- Local configuration.
- Frequent testing.

Production:

- Debug mode disabled.
- Secrets securely configured.
- Friendly error pages.
- Secure logging.
- Production server/deployment setup.

---

# 32. Complete Flask Mental Model

The most important Flask flow is:

    Browser
       ↓
    HTTP Request
       ↓
    Flask Application
       ↓
    Route
       ↓
    View Function
       ↓
    Application Logic
       ↓
    Template / Response
       ↓
    HTTP Response
       ↓
    Browser

---

# 33. Flask Section Summary

| Day | Topic |
|---|---|
| 061 | Introduction to Flask |
| 062 | Installation and Project Structure |
| 063 | Flask Routing |
| 064 | Dynamic Routes and URL Parameters |
| 065 | Jinja2 Templates |
| 066 | Template Inheritance |
| 067 | Static Files |
| 068 | HTML Forms and Request Methods |
| 069 | GET and POST |
| 070 | Redirects and `url_for()` |
| 071 | Flask Blueprints |
| 072 | Error Handling and Debugging |
| 073 | Configuration and Environment |
| 074 | Flask Mini Project |
| 075 | Revision and Practice |

---

# ⭐ Final Takeaway

Flask development can be understood as a sequence:

    Request
       ↓
    Route
       ↓
    Request Data
       ↓
    Application Logic
       ↓
    Template
       ↓
    Response

Supporting features such as Blueprints, error handling, configuration, and environment variables help make the application organized, maintainable, and safer.