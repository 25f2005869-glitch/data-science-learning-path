# ⚡ Day 068 — HTML Forms and Request Methods Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 068  
**Topic:** HTML Forms and Request Methods

---

## 🔹 HTML Form

    <form action="/register" method="POST">
        ...
    </form>

`action` → destination route

`method` → HTTP request method

---

## 🔹 GET

Used commonly for retrieving data.

    <form action="/search" method="GET">

Flask:

    request.args.get("q")

Example URL:

    /search?q=Python

---

## 🔹 POST

Used commonly for submitting or changing data.

    <form action="/register" method="POST">

Flask:

    request.form.get("name")

---

## 🔹 Flask Imports

    from flask import Flask, request

---

## 🔹 Route Supporting GET and POST

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":
            name = request.form.get("name")
            return name

        return "Show form"

---

## 🔹 Important Request Properties

| Property | Purpose |
|---|---|
| `request.method` | HTTP method |
| `request.args` | Query parameters |
| `request.form` | Submitted form data |

---

## 🔹 GET Example

HTML:

    <form action="/search" method="GET">
        <input name="q">
        <button type="submit">Search</button>
    </form>

Flask:

    query = request.args.get("q", "")

---

## 🔹 POST Example

HTML:

    <form action="/register" method="POST">
        <input name="name">
        <button type="submit">Register</button>
    </form>

Flask:

    name = request.form.get("name", "")

---

## 🔹 `name` Attribute

Important:

    <input name="student_name">

Access:

    request.form.get("student_name")

---

## 🔹 Default Value

    name = request.form.get("name", "")

    page = request.args.get("page", "1")

---

## 🔹 Validation

    name = request.form.get("name", "").strip()

    if not name:
        return "Name is required", 400

---

## 🔹 Redirect

    from flask import redirect, url_for

    return redirect(url_for("home"))

---

## 🔹 GET vs POST

| Feature | GET | POST |
|---|---|---|
| Data | Query parameters | Request body |
| URL | Contains data | Normally does not contain form data |
| Search | Excellent choice | Usually unnecessary |
| Registration | Usually not | Common choice |
| Sensitive data | Avoid | Better choice, but HTTPS still required |
| Server-side change | Should not | May |

---

## 🔹 Request Flow

    HTML Form
        ↓
    Browser
        ↓
    HTTP Request
        ↓
    Flask Route
        ↓
    request.args / request.form
        ↓
    Validation
        ↓
    Processing
        ↓
    Response

---

## 🧠 Remember

**GET → request.args**

**POST → request.form**

**request.method → tells which method was used**

**action → where the form is submitted**

**name → identifies a form field**

**POST ≠ encryption**

**HTTPS → protects data in transit**