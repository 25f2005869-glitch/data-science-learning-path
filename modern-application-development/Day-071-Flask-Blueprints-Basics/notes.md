# 📚 Day 071 — Flask Blueprints Basics

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 071  
**Topic:** Flask Blueprints Basics

---

## 1. What Is a Flask Blueprint?

A Blueprint is a way to organize related Flask routes and other application components into a separate module.

It helps divide a large Flask application into smaller parts.

For example, a student application might have:

    students
    courses
    authentication
    admin

Each area can have its own Blueprint.

---

## 2. Why Do We Need Blueprints?

A small Flask application may contain everything in:

    app.py

For example:

    @app.route("/")
    def home():
        ...

    @app.route("/students")
    def students():
        ...

    @app.route("/courses")
    def courses():
        ...

As the application grows, this file can become difficult to maintain.

Blueprints allow us to organize these routes into separate modules.

---

## 3. Without Blueprint

A simple application might look like:

    project/
    ├── app.py
    ├── templates/
    └── static/

All routes are defined inside `app.py`.

This is acceptable for small applications.

---

## 4. With Blueprint

A larger application can be organized as:

    project/
    ├── app.py
    ├── students/
    │   ├── __init__.py
    │   └── routes.py
    ├── courses/
    │   ├── __init__.py
    │   └── routes.py
    ├── templates/
    └── static/

Now related functionality can be separated.

---

## 5. Import Blueprint

Flask provides the `Blueprint` class.

Example:

    from flask import Blueprint

---

## 6. Creating a Blueprint

Basic syntax:

    student_bp = Blueprint(
        "student",
        __name__
    )

The first argument is the Blueprint name.

The second argument is usually:

    __name__

---

## 7. Adding Routes to a Blueprint

Instead of:

    @app.route("/students")

use the Blueprint object:

    @student_bp.route("/students")
    def students():
        return "Students"

The route belongs to the Blueprint.

---

## 8. Registering a Blueprint

Creating a Blueprint is not enough.

It must be registered with the Flask application.

Example:

    app.register_blueprint(student_bp)

After registration, the Blueprint's routes become part of the application.

---

## 9. Complete Basic Example

### `students/routes.py`

    from flask import Blueprint

    student_bp = Blueprint(
        "student",
        __name__
    )

    @student_bp.route("/students")
    def students():
        return "Student List"

### `app.py`

    from flask import Flask
    from students.routes import student_bp

    app = Flask(__name__)

    app.register_blueprint(student_bp)

    if __name__ == "__main__":
        app.run(debug=True)

The application now has:

    /students

---

## 10. URL Prefix

A Blueprint can have a common URL prefix.

Example:

    student_bp = Blueprint(
        "student",
        __name__,
        url_prefix="/students"
    )

Then the route can be:

    @student_bp.route("/")
    def students():
        return "Student List"

The final URL becomes:

    /students/

---

## 11. Why Use URL Prefixes?

Suppose a Blueprint contains:

    /
    /profile
    /courses

With:

    url_prefix="/student"

the final URLs become:

    /student/
    /student/profile
    /student/courses

This makes the URL structure easier to understand.

---

## 12. Multiple Blueprints

A Flask application can have multiple Blueprints.

Example:

    student_bp
    course_bp
    admin_bp

Register them:

    app.register_blueprint(student_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(admin_bp)

Each Blueprint can manage a different part of the application.

---

## 13. Example Application Structure

A student portal might use:

    project/
    ├── app.py
    │
    ├── students/
    │   └── routes.py
    │
    ├── courses/
    │   └── routes.py
    │
    ├── auth/
    │   └── routes.py
    │
    └── templates/

Possible URL structure:

    /students/
    /students/profile
    /courses/
    /courses/python
    /login
    /logout

---

## 14. Blueprint Endpoint Names

Blueprints affect endpoint naming.

Suppose:

    student_bp = Blueprint("student", __name__)

and:

    @student_bp.route("/")
    def home():
        ...

The endpoint is generally:

    student.home

Therefore:

    url_for("student.home")

can generate the URL.

---

## 15. Blueprint + `url_for()`

Example:

    url_for("student.home")

For another route:

    @student_bp.route("/profile")
    def profile():
        ...

Use:

    url_for("student.profile")

The Blueprint name and view function name form the endpoint.

---

## 16. Blueprint URL Prefix and `url_for()`

Suppose:

    student_bp = Blueprint(
        "student",
        __name__,
        url_prefix="/students"
    )

and:

    @student_bp.route("/profile")
    def profile():
        ...

Then:

    url_for("student.profile")

generates:

    /students/profile

---

## 17. Blueprint vs Flask Application

The Flask application is the main application object.

A Blueprint is a modular component that can be registered with the application.

Think of it as:

    Flask App
       │
       ├── Student Blueprint
       ├── Course Blueprint
       └── Admin Blueprint

---

## 18. Blueprint Does Not Run by Itself

A Blueprint is not the Flask application itself.

It needs to be registered:

    app.register_blueprint(student_bp)

Without registration, its routes are not available through the application.

---

## 19. Blueprint Registration

Example:

    from flask import Flask
    from students.routes import student_bp

    app = Flask(__name__)

    app.register_blueprint(student_bp)

The application imports the Blueprint and registers it.

---

## 20. `__init__.py`

In a package-based structure, `__init__.py` can be used to make a directory a Python package and organize imports.

Example:

    students/
    ├── __init__.py
    └── routes.py

The exact structure can vary depending on the application design.

---

## 21. Blueprint for Students

Example:

    from flask import Blueprint

    student_bp = Blueprint(
        "student",
        __name__,
        url_prefix="/students"
    )

    @student_bp.route("/")
    def list_students():
        return "Student List"

    @student_bp.route("/profile")
    def profile():
        return "Student Profile"

The Blueprint manages student-related routes.

---

## 22. Blueprint for Courses

Example:

    from flask import Blueprint

    course_bp = Blueprint(
        "course",
        __name__,
        url_prefix="/courses"
    )

    @course_bp.route("/")
    def list_courses():
        return "Course List"

    @course_bp.route("/python")
    def python():
        return "Python Course"

---

## 23. Registering Multiple Blueprints

In `app.py`:

    from flask import Flask

    from students.routes import student_bp
    from courses.routes import course_bp

    app = Flask(__name__)

    app.register_blueprint(student_bp)
    app.register_blueprint(course_bp)

Now the application can contain both:

    /students/
    /courses/

---

## 24. Advantages of Blueprints

### Organization

Related routes stay together.

### Maintainability

Smaller files are easier to understand.

### Reusability

A Blueprint can be designed as a reusable application component.

### Scalability

The structure works better as applications become larger.

### Team Development

Different developers can work on different modules.

---

## 25. Blueprint Naming

Use meaningful Blueprint names.

Good:

    student_bp
    course_bp
    auth_bp

Avoid unclear names such as:

    x
    temp
    thing

Clear names improve readability.

---

## 26. Common Mistakes

### Mistake 1: Creating but not registering the Blueprint

Creating:

    student_bp = Blueprint(...)

is not enough.

You also need:

    app.register_blueprint(student_bp)

---

### Mistake 2: Using `app.route()` inside a Blueprint module

Inside a Blueprint module, use:

    @student_bp.route(...)

not:

    @app.route(...)

---

### Mistake 3: Wrong endpoint in `url_for()`

For a Blueprint endpoint:

    student.profile

not simply:

    profile

---

### Mistake 4: Incorrect URL prefix

If:

    url_prefix="/students"

and:

    @student_bp.route("/profile")

the final URL is:

    /students/profile

Do not accidentally repeat the prefix inside the route.

---

## 27. Blueprint and Templates

A Blueprint can render templates.

Example:

    from flask import Blueprint, render_template

    student_bp = Blueprint(
        "student",
        __name__
    )

    @student_bp.route("/")
    def home():
        return render_template("students/home.html")

This allows templates to be organized by application module.

---

## 28. Blueprint and Static Files

Blueprints can also be configured with their own static resources.

A basic Blueprint can use:

    Blueprint(
        "student",
        __name__,
        static_folder="static"
    )

For simple Flask projects, a single application-level `static/` directory may be easier.

---

## 29. When Should You Use Blueprints?

Blueprints are especially useful when:

- The application has many routes.
- Different features need separate modules.
- The project has multiple developers.
- The application has clear functional areas.
- You want a scalable project structure.

For a very small Flask application, Blueprints may not be necessary.

---

## 30. Mental Model

Think of a Blueprint as a **module of Flask routes**.

    Blueprint
        ↓
    Group related routes
        ↓
    Register with Flask app
        ↓
    Routes become available

---

## 31. Complete Example

### `students/routes.py`

    from flask import Blueprint

    student_bp = Blueprint(
        "student",
        __name__,
        url_prefix="/students"
    )

    @student_bp.route("/")
    def list_students():
        return "Student List"

    @student_bp.route("/profile")
    def profile():
        return "Student Profile"

### `app.py`

    from flask import Flask
    from students.routes import student_bp

    app = Flask(__name__)

    app.register_blueprint(student_bp)

    if __name__ == "__main__":
        app.run(debug=True)

Routes:

    /students/
    /students/profile

Endpoints:

    student.list_students
    student.profile

---

## 32. Summary

Flask Blueprints help organize large applications into smaller modules.

The three most important steps are:

### Step 1 — Create

    student_bp = Blueprint(
        "student",
        __name__
    )

### Step 2 — Define Routes

    @student_bp.route("/students")
    def students():
        ...

### Step 3 — Register

    app.register_blueprint(student_bp)

For navigation:

    url_for("student.students")

Blueprints make Flask applications cleaner, modular, maintainable, and easier to scale.