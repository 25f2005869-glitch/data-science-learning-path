# ⚡ Day 071 — Flask Blueprints Basics Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 071  
**Topic:** Flask Blueprints Basics

---

## 🔹 Import

    from flask import Blueprint

---

## 🔹 Create Blueprint

    student_bp = Blueprint(
        "student",
        __name__
    )

---

## 🔹 Blueprint Route

    @student_bp.route("/students")
    def students():
        return "Students"

---

## 🔹 Register Blueprint

    app.register_blueprint(student_bp)

---

## 🔹 URL Prefix

    student_bp = Blueprint(
        "student",
        __name__,
        url_prefix="/students"
    )

Route:

    @student_bp.route("/")

Final URL:

    /students/

---

## 🔹 Blueprint Endpoint

Blueprint:

    student_bp = Blueprint("student", __name__)

Function:

    def profile():

Endpoint:

    student.profile

Generate URL:

    url_for("student.profile")

---

## 🔹 Dynamic Route

    @student_bp.route("/<int:student_id>")
    def profile(student_id):
        ...

URL:

    url_for("student.profile", student_id=101)

---

## 🔹 Multiple Blueprints

    app.register_blueprint(student_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(auth_bp)

---

## 🔹 Example Structure

    project/
    ├── app.py
    ├── students/
    │   ├── __init__.py
    │   └── routes.py
    ├── courses/
    │   └── routes.py
    ├── templates/
    └── static/

---

## 🔹 Blueprint vs App

| Flask App | Blueprint |
|---|---|
| Main application | Modular component |
| Created with `Flask()` | Created with `Blueprint()` |
| Runs application | Does not run by itself |
| Registers Blueprints | Gets registered |
| `app.route()` | `blueprint.route()` |

---

## 🔹 Most Important Functions

| Function | Purpose |
|---|---|
| `Blueprint()` | Create Blueprint |
| `register_blueprint()` | Register Blueprint |
| `url_for()` | Generate endpoint URL |
| `render_template()` | Render template |

---

## 🔹 Blueprint Flow

    Create Blueprint
          ↓
    Add Routes
          ↓
    Register Blueprint
          ↓
    Flask Application
          ↓
    Routes Available

---

## 🔹 Common Mistakes

Wrong inside Blueprint module:

    @app.route("/students")

Correct:

    @student_bp.route("/students")

Wrong:

    app.register_blueprint()

Correct:

    app.register_blueprint(student_bp)

Wrong endpoint:

    url_for("profile")

Correct for Blueprint:

    url_for("student.profile")

---

## 🧠 Remember

**Blueprint = Module**

**`Blueprint()` = Create**

**`@bp.route()` = Add route**

**`register_blueprint()` = Connect to app**

**`url_for("bp.endpoint")` = Generate Blueprint URL**

**`url_prefix` = Common URL prefix**