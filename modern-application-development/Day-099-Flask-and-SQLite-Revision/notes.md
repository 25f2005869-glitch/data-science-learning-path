# 📚 Day 099 — Flask and SQLite Revision Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 099  
**Topic:** Flask and SQLite Revision

---

## 1. Flask Fundamentals

Flask is a lightweight Python web framework used to build web applications and APIs.

Basic application:

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        app.run(debug=True)

Important concepts:

- `Flask(__name__)` creates the application object.
- `@app.route()` connects a URL to a function.
- The function is called a view function.
- `app.run()` starts the development server.
- Debug mode helps during development.

---

## 2. Flask Project Structure

A typical project can contain:

    project/
    ├── app.py
    ├── templates/
    ├── static/
    ├── instance/
    ├── tests/
    ├── requirements.txt
    ├── .env
    └── .gitignore

`templates/` stores Jinja2 HTML templates.

`static/` stores CSS, JavaScript, and images.

`instance/` can store instance-specific data such as a local SQLite database.

---

## 3. Routing

Routes map URLs to Python functions.

Example:

    @app.route("/students")
    def students():
        return "Student List"

Dynamic route:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student ID: {student_id}"

Common converters:

- `string`
- `int`
- `float`
- `path`
- `uuid`

---

## 4. URL Parameters and Query Parameters

URL parameter:

    /student/25

Flask:

    @app.route("/student/<int:id>")
    def student(id):
        return str(id)

Query parameter:

    /students?course=Data%20Science

Flask:

    request.args.get("course")

URL parameters are part of the route.

Query parameters are supplied after `?`.

---

## 5. Jinja2 Templates

Jinja2 allows dynamic data to be inserted into HTML.

Python:

    return render_template("student.html", name="Saloni")

Template:

    <h1>{{ name }}</h1>

Condition:

    {% if marks >= 50 %}
        Passed
    {% else %}
        Failed
    {% endif %}

Loop:

    {% for student in students %}
        {{ student.name }}
    {% endfor %}

---

## 6. Template Inheritance

Template inheritance avoids repeating common HTML.

Base template:

    {% block content %}
    {% endblock %}

Child template:

    {% extends "base.html" %}

    {% block content %}
        <h1>Student Dashboard</h1>
    {% endblock %}

Important keywords:

- `extends`
- `block`
- `endblock`
- `super()`

---

## 7. Static Files

Flask normally uses the `static/` directory.

Example:

    <link rel="stylesheet"
          href="{{ url_for('static', filename='css/style.css') }}">

JavaScript:

    <script src="{{ url_for('static', filename='js/app.js') }}"></script>

Image:

    <img src="{{ url_for('static', filename='images/logo.png') }}"
         alt="Logo">

Never store passwords or secret keys in static files.

---

## 8. Forms

HTML form:

    <form action="/register" method="POST">
        <input type="text" name="name">
        <input type="email" name="email">
        <button type="submit">Register</button>
    </form>

Flask:

    from flask import request

    @app.route("/register", methods=["POST"])
    def register():
        name = request.form.get("name")
        email = request.form.get("email")
        return "Registered"

The `name` attribute is important because Flask uses it to retrieve submitted form data.

---

## 9. GET and POST

GET is generally used to retrieve data.

Example:

    /students?course=DataScience

Flask:

    request.args

POST is generally used to submit or modify data.

Flask:

    request.form

Important difference:

- GET data is normally visible in the URL.
- POST data is sent in the request body.
- POST should be used for state-changing operations.

---

## 10. Redirects and `url_for()`

Redirect:

    return redirect(url_for("students"))

Dynamic URL:

    url_for("student", student_id=10)

Query parameters can also be generated:

    url_for("students", course="Data Science")

Using `url_for()` is preferred over hard-coding URLs because route changes are easier to manage.

---

## 11. Post/Redirect/Get

A common form workflow is:

    GET form
       ↓
    POST form
       ↓
    Validate
       ↓
    Save data
       ↓
    Redirect
       ↓
    GET result page

This prevents accidental duplicate form submissions when the page is refreshed.

---

## 12. Blueprints

Blueprints divide large Flask applications into modules.

Example:

    student_bp = Blueprint("student", __name__)

    @student_bp.route("/students")
    def students():
        return "Students"

Register:

    app.register_blueprint(student_bp, url_prefix="/student")

Blueprints improve organization and maintainability.

---

## 13. Error Handling

Common HTTP errors:

- 400 — Bad Request
- 401 — Unauthorized
- 403 — Forbidden
- 404 — Not Found
- 405 — Method Not Allowed
- 500 — Internal Server Error

Example:

    abort(404)

Custom handler:

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

---

## 14. Configuration

Configuration stores application settings.

Example:

    app.config["SECRET_KEY"] = "development-key"

Environment variables should be used for sensitive configuration.

Example:

    import os

    secret_key = os.environ.get("SECRET_KEY")

Never commit real secrets to GitHub.

---

# 🗄️ SQLite Revision

## 15. SQLite

SQLite is a lightweight relational database.

Important characteristics:

- Serverless
- File-based
- Relational
- Lightweight
- Supports SQL
- Easy to use with Python
- Useful for small applications and development

Python provides the built-in `sqlite3` module.

---

## 16. Database Connection

Basic SQLite connection:

    import sqlite3

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

After database operations:

    connection.commit()
    connection.close()

---

## 17. Creating Tables

Example:

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        marks REAL
    );

Important constraints:

- PRIMARY KEY
- FOREIGN KEY
- NOT NULL
- UNIQUE
- DEFAULT
- CHECK

---

## 18. CRUD

CRUD means:

- Create
- Read
- Update
- Delete

Create:

    INSERT INTO students (name, email, marks)
    VALUES (?, ?, ?)

Read:

    SELECT * FROM students

Update:

    UPDATE students
    SET marks = ?
    WHERE id = ?

Delete:

    DELETE FROM students
    WHERE id = ?

Parameterized queries should be used instead of building SQL with string concatenation.

---

## 19. SQLAlchemy

SQLAlchemy is a Python SQL toolkit and ORM.

ORM means Object-Relational Mapping.

It allows Python classes to represent database tables.

Example:

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

A Python object can represent a database row.

---

## 20. Database Operations with SQLAlchemy

Create:

    student = Student(
        name="Saloni",
        email="saloni@example.com",
        marks=90
    )

    db.session.add(student)
    db.session.commit()

Read:

    students = db.session.execute(
        db.select(Student)
    ).scalars().all()

Get by primary key:

    student = db.session.get(Student, 1)

Update:

    student.marks = 95
    db.session.commit()

Delete:

    db.session.delete(student)
    db.session.commit()

Rollback:

    db.session.rollback()

---

## 21. Database Relationships

Common relationship types:

### One-to-One

One record is associated with one record.

### One-to-Many

One student can have many records.

### Many-to-Many

Students can enroll in multiple courses and courses can contain multiple students.

Many-to-many relationships commonly use a junction table.

---

## 22. Search and Filtering

Query parameters can be used for search.

Example:

    /students?search=Saloni

Flask:

    search = request.args.get("search", "")

SQLAlchemy concept:

    Student.name.ilike(f"%{search}%")

Filtering:

    Student.marks >= 50

Sorting:

    Student.marks.desc()

Always validate or allowlist fields used for dynamic sorting.

---

## 23. Authentication

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to do?

Typical authentication flow:

    Register
       ↓
    Hash password
       ↓
    Store user
       ↓
    Login
       ↓
    Verify password
       ↓
    Create session
       ↓
    Access protected pages
       ↓
    Logout

Passwords must never be stored as plain text.

Useful Werkzeug functions:

    generate_password_hash()
    check_password_hash()

---

## 24. Sessions and Cookies

Flask sessions can remember information between requests.

Example:

    session["user_id"] = user.id

Retrieve:

    user_id = session.get("user_id")

Remove:

    session.pop("user_id", None)

Clear:

    session.clear()

Flask requires a secret key for its default session mechanism.

Cookies are stored by the browser and sent with matching requests.

Important cookie security attributes:

- `Secure`
- `HttpOnly`
- `SameSite`

---

## 25. Flash Messages

Flash messages provide temporary feedback.

Example:

    flash("Student added successfully.", "success")

Template:

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% for category, message in messages %}
            {{ message }}
        {% endfor %}
    {% endwith %}

Common categories:

- success
- error
- warning
- info

---

## 26. Validation

Validation should happen on the server even when client-side validation exists.

Examples:

- Required fields
- Correct email format
- Valid age
- Valid marks
- Unique email
- Allowed course
- Password requirements

Validation protects both data quality and application behavior.

---

## 27. Authentication vs Authorization

Authentication:

    Is the user logged in?

Authorization:

    Does the logged-in user have permission?

Example:

- Student → view own profile
- Teacher → manage students
- Admin → manage users and system settings

---

## 28. Testing

Important Flask tests include:

- Route tests
- GET tests
- POST tests
- Form validation tests
- Authentication tests
- Authorization tests
- CRUD tests
- Search tests
- Error tests

Flask provides a test client for testing application routes.

---

## 29. Debugging

Basic debugging workflow:

1. Reproduce the problem.
2. Read the traceback.
3. Identify the failing line.
4. Check input values.
5. Check database queries.
6. Check route and template names.
7. Fix the root cause.
8. Test again.

Debug mode should not be enabled in production.

---

## 30. Security Revision

Important security practices:

- Hash passwords.
- Keep secrets outside source code.
- Use HTTPS in production.
- Validate server-side input.
- Use parameterized SQL or ORM queries.
- Protect state-changing forms against CSRF.
- Use authorization checks.
- Do not expose sensitive errors.
- Avoid logging passwords or secrets.
- Use secure cookie settings.
- Keep dependencies updated.

---

## 31. Complete Application Flow

A Flask + SQLite application can follow this flow:

    Browser
       ↓
    HTTP Request
       ↓
    Flask Route
       ↓
    Authentication / Validation
       ↓
    Business Logic
       ↓
    SQLAlchemy
       ↓
    SQLite Database
       ↓
    Query Result
       ↓
    Jinja2 Template
       ↓
    HTML Response
       ↓
    Browser

---

## 32. Final Revision Checklist

- [ ] Flask basics
- [ ] Project structure
- [ ] Routing
- [ ] Dynamic routes
- [ ] URL parameters
- [ ] Jinja2
- [ ] Template inheritance
- [ ] Static files
- [ ] Forms
- [ ] GET and POST
- [ ] Request data
- [ ] Redirects
- [ ] `url_for()`
- [ ] Blueprints
- [ ] Error handling
- [ ] Configuration
- [ ] Environment variables
- [ ] SQLite
- [ ] Database design
- [ ] SQLAlchemy
- [ ] CRUD
- [ ] Authentication
- [ ] Sessions
- [ ] Cookies
- [ ] Search and filtering
- [ ] Flash messages
- [ ] Validation
- [ ] Testing
- [ ] Security
- [ ] Deployment basics

---

## 📌 Key Idea

Flask handles the web application layer, while SQLite stores relational data.

SQLAlchemy connects Python application code with the database using ORM concepts.

Together:

**Flask + Jinja2 + SQLAlchemy + SQLite = A complete foundation for MAD 1 web applications.**