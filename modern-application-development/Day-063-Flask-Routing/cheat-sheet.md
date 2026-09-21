# ⚡ Day 063 — Flask Routing Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 063  
**Topic:** Flask Routing

---

## 🔗 Basic Route

    @app.route("/")
    def home():
        return "Home Page"

---

## 📄 Multiple Routes

    @app.route("/")
    def home():
        return "Home"

    @app.route("/about")
    def about():
        return "About"

    @app.route("/contact")
    def contact():
        return "Contact"

---

## 🎯 Dynamic Route

    @app.route("/student/<name>")
    def student(name):
        return f"Student: {name}"

Example:

    /student/Saloni

---

## 🔢 Integer Parameter

    @app.route("/student/<int:id>")
    def student(id):
        return f"Student ID: {id}"

Example:

    /student/101

---

## 🔢 Float Parameter

    @app.route("/price/<float:amount>")
    def price(amount):
        return f"Price: {amount}"

---

## 📁 Path Parameter

    @app.route("/files/<path:filename>")
    def files(filename):
        return filename

---

## 🧩 Route Converters

| Converter | Accepts |
|---|---|
| `string` | Text |
| `int` | Integer |
| `float` | Decimal number |
| `path` | Text containing `/` |
| `uuid` | UUID |

---

## 🌐 HTTP Methods

    @app.route("/login", methods=["GET", "POST"])
    def login():
        return "Login"

Common methods:

- GET
- POST
- PUT
- PATCH
- DELETE

---

## 🔗 `url_for()`

    from flask import url_for

    url_for("home")

The argument is normally the endpoint/view function name.

---

## 🏷️ Endpoint

    @app.route("/about")
    def about():
        return "About"

Endpoint:

    about

URL generation:

    url_for("about")

---

## 🏷️ Custom Endpoint

    @app.route("/profile", endpoint="student_profile")
    def profile():
        return "Profile"

Use:

    url_for("student_profile")

---

## ❌ 404

A 404 occurs when Flask cannot find a matching route.

Example:

    /unknown

when `/unknown` has not been defined.

---

## 🔄 Routing Flow

    Browser
       ↓
    HTTP Request
       ↓
    Flask
       ↓
    Route Matching
       ↓
    View Function
       ↓
    Response
       ↓
    Browser

---

## 🧠 Remember

    URL → Route → Function → Response

Dynamic:

    URL → Parameter → Function

---

## ⚠️ Common Errors

- Missing `@app.route()`
- Wrong URL
- Parameter mismatch
- Wrong HTTP method
- Confusing URL with endpoint