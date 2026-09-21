# ⚡ Day 064 — Dynamic Routes and URL Parameters

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 064  
**Topic:** Dynamic Routes and URL Parameters

---

## 🔗 Basic Dynamic Route

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

Example:

    /price/499.50

---

## 📁 Path Parameter

    @app.route("/files/<path:filename>")
    def files(filename):
        return filename

Example:

    /files/docs/mad1/notes.pdf

---

## 🧩 Route Converters

| Converter | Meaning |
|---|---|
| `string` | Text |
| `int` | Integer |
| `float` | Decimal number |
| `path` | Text containing `/` |
| `uuid` | UUID |

---

## 🔀 Multiple Parameters

    @app.route("/student/<int:id>/course/<course>")
    def student_course(id, course):
        return f"{id} - {course}"

Example:

    /student/101/course/DBMS

---

## 🔗 `url_for()`

    url_for("student", student_id=101)

Generates the URL for the dynamic route.

---

## 🏷️ Parameter Matching

Route:

    @app.route("/student/<int:student_id>")

Function:

    def student(student_id):

The names should match.

---

## ❌ Invalid Parameter

Route:

    /student/<int:id>

Request:

    /student/abc

`abc` does not satisfy the integer converter.

If no other route matches, Flask returns 404.

---

## 🔄 Dynamic Route Flow

    URL
     ↓
    Parameter
     ↓
    Flask Route
     ↓
    View Function
     ↓
    Response

---

## 📌 URL Parameter vs Query Parameter

Path parameter:

    /student/101

Query parameter:

    /students?page=2

They are different concepts.

---

## 🧠 Remember

    <name>       → String
    <int:id>     → Integer
    <float:value> → Float
    <path:file>  → Path

---

## ⭐ Most Important Pattern

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student: {student_id}"