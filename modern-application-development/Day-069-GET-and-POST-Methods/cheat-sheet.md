# ⚡ Day 069 — GET and POST Methods Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 069  
**Topic:** GET and POST Methods

---

## 🔹 GET

Commonly used to retrieve data.

Example:

    GET /courses

Query parameters:

    /search?q=python&page=2

Flask:

    request.args.get("q")

---

## 🔹 POST

Commonly used to submit or process data.

Example:

    POST /register

Flask:

    request.form.get("name")

---

## 🔹 Flask Request Import

    from flask import request

---

## 🔹 Check Method

    if request.method == "GET":
        ...

    if request.method == "POST":
        ...

---

## 🔹 Route Methods

GET only:

    @app.route("/search", methods=["GET"])

POST only:

    @app.route("/register", methods=["POST"])

Both:

    @app.route("/form", methods=["GET", "POST"])

---

## 🔹 GET Form

    <form action="/search" method="GET">
        <input name="q">
        <button type="submit">Search</button>
    </form>

Read:

    request.args.get("q")

---

## 🔹 POST Form

    <form action="/register" method="POST">
        <input name="name">
        <button type="submit">Register</button>
    </form>

Read:

    request.form.get("name")

---

## 🔹 Important Flask Objects

| Object | Purpose |
|---|---|
| `request.method` | HTTP method |
| `request.args` | URL query parameters |
| `request.form` | Submitted form fields |

---

## 🔹 GET Example

URL:

    /search?q=Flask

Flask:

    query = request.args.get("q", "")

Result:

    Flask

---

## 🔹 POST Example

Form:

    <input name="name">

Flask:

    name = request.form.get("name", "")

---

## 🔹 GET vs POST

| Feature | GET | POST |
|---|---|---|
| Main purpose | Retrieve | Submit/process |
| Query string | Yes | Not normally used for form body |
| Form data | URL | Request body |
| Search | Common | Uncommon |
| Registration | Usually no | Common |
| State change | Should not | May |
| Sensitive data | Avoid | Use HTTPS |

---

## 🔹 `name` Attribute

HTML:

    <input name="email">

Flask:

    email = request.form.get("email")

---

## 🔹 Validation

    value = request.form.get("name", "").strip()

    if not value:
        return "Required", 400

---

## 🔹 Redirect

    from flask import redirect, url_for

    return redirect(url_for("home"))

---

## 🔹 Post/Redirect/Get

    POST
      ↓
    Process
      ↓
    Redirect
      ↓
    GET

---

## 🔹 Important Security Rule

**POST is not encryption.**

Use:

    HTTPS

to protect data during transmission.

---

## 🧠 Remember

**GET → Retrieve → URL → `request.args`**

**POST → Submit → Body → `request.form`**

**`request.method` → tells the method**

**`action` → destination**

**`name` → identifies the form field**