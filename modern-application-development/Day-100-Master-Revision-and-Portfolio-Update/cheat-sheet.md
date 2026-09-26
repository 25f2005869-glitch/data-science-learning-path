# ⚡ Day 100 — MAD 1 Master Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 100  
**Topic:** Master Revision and Portfolio Update

# 🌐 HTML

Structure:

<!DOCTYPE html>
<html>
<head>
    <title>Page</title>
</head>
<body>
    Content
</body>
</html>

Important elements:

h1-h6
p
a
img
ul
ol
table
form
input
textarea
select
button

Semantic elements:

header
nav
main
section
article
aside
footer
figure
figcaption

# 🎨 CSS

Selectors:

element
.class
#id
*
[attribute]

Box Model:

Content
Padding
Border
Margin

Layouts:

display: flex;
display: grid;

Position:

static
relative
absolute
fixed
sticky

Responsive:

@media (max-width: 768px) {
    ...
}

# ⚙️ JavaScript

Variables:

let score = 90;
const name = "Saloni";

Condition:

if (score >= 50) {
    console.log("Pass");
}

Loop:

for (let i = 0; i < 5; i++) {
    console.log(i);
}

Function:

function add(a, b) {
    return a + b;
}

Array:

const courses = ["DBMS", "PDSA", "MLF"];

Object:

const student = {
    name: "Saloni",
    marks: 90
};

DOM:

document.querySelector("#title");

Event:

button.addEventListener("click", function () {
    console.log("Clicked");
});

Storage:

localStorage.setItem("name", "Saloni");

# 🐍 Flask

Basic:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

Dynamic route:

@app.route("/student/<int:id>")
def student(id):
    return str(id)

Template:

return render_template(
    "index.html",
    name="Saloni"
)

GET:

request.args.get("name")

POST:

request.form.get("name")

Redirect:

return redirect(url_for("home"))

Error:

abort(404)

# 🎨 Jinja2

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

# 🗄️ SQLite

Create table:

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    marks REAL
);

Insert:

INSERT INTO students
(name, email, marks)
VALUES (?, ?, ?);

Read:

SELECT * FROM students;

Update:

UPDATE students
SET marks = ?
WHERE id = ?;

Delete:

DELETE FROM students
WHERE id = ?;

# 🔧 SQLAlchemy

Create:

student = Student(
    name="Saloni",
    marks=90
)

db.session.add(student)
db.session.commit()

Read:

students = db.session.execute(
    db.select(Student)
).scalars().all()

Get:

student = db.session.get(Student, 1)

Update:

student.marks = 95
db.session.commit()

Delete:

db.session.delete(student)
db.session.commit()

Rollback:

db.session.rollback()

# 🔄 CRUD

CREATE → Add
READ → View
UPDATE → Edit
DELETE → Remove

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

# 🔍 Search

Example:

/students?search=Saloni

Flask:

request.args.get("search")

SQLAlchemy concept:

Student.name.ilike("%Saloni%")

# 🍪 Cookies

Set:

response.set_cookie("theme", "dark")

Read:

request.cookies.get("theme")

Delete:

response.delete_cookie("theme")

Security:

Secure
HttpOnly
SameSite

# ✅ Validation

Check:

Required
Type
Length
Range
Format
Uniqueness
Business Rules

Server-side validation is mandatory.

# 🛡️ Security

Password Hashing
HTTPS
CSRF Protection
Server Validation
Authorization
Parameterized Queries
Secure Cookies
Environment Variables
No Secrets in Git

# 🧪 Testing

Test:

Routes
Forms
CRUD
Authentication
Authorization
Search
Validation
Errors

# 🚀 Deployment

Before deployment:

requirements.txt
Environment variables
Production configuration
WSGI server
HTTPS
Database configuration
Logging
Error handling
Security review

# 🏗️ Full-Stack Flow

HTML
    ↓
CSS
    ↓
JavaScript
    ↓
HTTP
    ↓
Flask
    ↓
Jinja2
    ↓
SQLAlchemy
    ↓
SQLite

# 💼 Portfolio Formula

Project
    +
README
    +
GitHub
    +
Screenshots
    +
Tech Stack
    +
Features
    +
Testing
    +
Security
    =
Professional Portfolio Project

# 🎯 Final Rule

Do not only memorize syntax.

Understand:

What?
Why?
How?
When?
Where?

Then build it.