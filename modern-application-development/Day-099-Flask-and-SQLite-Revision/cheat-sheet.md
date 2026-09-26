# ⚡ Day 099 — Flask and SQLite Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 099  
**Topic:** Flask and SQLite Revision

---

# 🐍 Flask Quick Reference

## Basic Flask App

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello"

    if __name__ == "__main__":
        app.run(debug=True)

---

## Route

    @app.route("/students")
    def students():
        return "Students"

## Dynamic Route

    @app.route("/student/<int:id>")
    def student(id):
        return str(id)

---

## HTTP Methods

    @app.route("/student", methods=["GET", "POST"])

- GET → retrieve
- POST → submit/create
- PUT → replace
- PATCH → partially update
- DELETE → delete

---

## Request Data

Query parameter:

    request.args.get("name")

Form data:

    request.form.get("name")

Method:

    request.method

---

## Render Template

    from flask import render_template

    return render_template(
        "student.html",
        name="Saloni"
    )

---

## Jinja2

Variable:

    {{ name }}

Condition:

    {% if marks >= 50 %}
        Pass
    {% endif %}

Loop:

    {% for student in students %}
        {{ student.name }}
    {% endfor %}

Inheritance:

    {% extends "base.html" %}

    {% block content %}
    {% endblock %}

---

## Static Files

    {{ url_for(
        'static',
        filename='css/style.css'
    ) }}

---

## Redirect

    return redirect(url_for("home"))

---

## Flash

    flash("Saved successfully.", "success")

---

## Error

    abort(404)

Custom handler:

    @app.errorhandler(404)

---

# 🗄️ SQLite Quick Reference

## Connection

    import sqlite3

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    conn.commit()
    conn.close()

---

## Create Table

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        marks REAL
    );

---

## CRUD

Create:

    INSERT INTO students
    (name, email, marks)
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

---

# 🔧 SQLAlchemy

## Model

    class Student(db.Model):
        id = db.Column(
            db.Integer,
            primary_key=True
        )

        name = db.Column(
            db.String(100),
            nullable=False
        )

---

## Create

    student = Student(name="Saloni")

    db.session.add(student)
    db.session.commit()

---

## Read

    students = db.session.execute(
        db.select(Student)
    ).scalars().all()

---

## Get One

    student = db.session.get(Student, 1)

---

## Update

    student.marks = 95
    db.session.commit()

---

## Delete

    db.session.delete(student)
    db.session.commit()

---

## Rollback

    db.session.rollback()

---

# 🔍 Search

    search = request.args.get("search", "")

Concept:

    Student.name.ilike(f"%{search}%")

---

# 🔐 Authentication

Hash:

    generate_password_hash(password)

Verify:

    check_password_hash(
        password_hash,
        password
    )

Session:

    session["user_id"] = user.id

Read:

    session.get("user_id")

Logout:

    session.clear()

---

# 🍪 Cookies

Set:

    response.set_cookie("theme", "dark")

Read:

    request.cookies.get("theme")

Delete:

    response.delete_cookie("theme")

Security:

- Secure
- HttpOnly
- SameSite

---

# ✅ Validation

Validate:

- Required fields
- Data type
- Length
- Range
- Format
- Uniqueness
- Business rules

Server-side validation is mandatory.

---

# 🔄 CRUD Lifecycle

    CREATE
       ↓
    READ
       ↓
    UPDATE
       ↓
    DELETE

---

# 🌐 Application Flow

    Browser
       ↓
    Flask Route
       ↓
    Request Validation
       ↓
    SQLAlchemy
       ↓
    SQLite
       ↓
    Jinja2
       ↓
    HTML Response

---

# 🛡️ Security Checklist

- Password hashing
- HTTPS
- CSRF protection
- Server-side validation
- Parameterized queries
- Authorization
- Secure cookies
- Secret environment variables
- No sensitive logs
- Production error handling