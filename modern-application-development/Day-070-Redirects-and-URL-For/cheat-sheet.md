# ⚡ Day 070 — Redirects and `url_for()` Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 070  
**Topic:** Redirects and `url_for()`

---

## 🔹 `redirect()`

Tells the browser to navigate to another URL.

    from flask import redirect

    return redirect("/home")

---

## 🔹 `url_for()`

Generates a URL for a Flask endpoint.

    from flask import url_for

    url_for("home")

If:

    @app.route("/")
    def home():
        ...

Then:

    url_for("home")

returns:

    /

---

## 🔹 Most Important Pattern

    return redirect(url_for("home"))

Meaning:

    url_for() → Generate URL
    redirect() → Navigate browser

---

## 🔹 Endpoint

Example:

    @app.route("/about")
    def about():
        ...

Endpoint:

    about

Generate URL:

    url_for("about")

---

## 🔹 Dynamic Route

Route:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        ...

URL:

    url_for("student", student_id=101)

Result:

    /student/101

---

## 🔹 Multiple Parameters

    url_for(
        "course",
        student_id=101,
        course="Python"
    )

---

## 🔹 Query Parameters

    url_for("search", q="python")

Result:

    /search?q=python

Multiple:

    url_for("search", q="python", page=2)

---

## 🔹 Template Usage

    <a href="{{ url_for('home') }}">
        Home
    </a>

Dynamic:

    <a href="{{ url_for('student', student_id=101) }}">
        Student
    </a>

---

## 🔹 Static Files

    {{ url_for('static', filename='css/style.css') }}

---

## 🔹 POST → Redirect → GET

    POST
      ↓
    Process
      ↓
    Redirect
      ↓
    GET

Example:

    return redirect(url_for("success"))

---

## 🔹 Redirect Status Codes

| Code | Meaning |
|---|---|
| 301 | Permanent Redirect |
| 302 | Found |
| 303 | See Other |
| 307 | Temporary Redirect |
| 308 | Permanent Redirect |

Default Flask `redirect()` behavior uses a temporary redirect.

For explicit POST-to-GET:

    return redirect(url_for("success"), code=303)

---

## 🔹 `redirect()` vs `url_for()`

| Function | Purpose |
|---|---|
| `redirect()` | Redirect browser |
| `url_for()` | Generate URL |

Together:

    redirect(url_for("home"))

---

## 🔹 Common Errors

Wrong:

    url_for("/home")

Correct:

    url_for("home")

Wrong:

    url_for()

Correct:

    url_for("home")

Wrong:

    url_for("student")

when required parameter is missing.

Correct:

    url_for("student", student_id=101)

---

## 🧠 Remember

**`url_for()` → Generate URL**

**`redirect()` → Navigate**

**Endpoint → Usually view function name**

**Dynamic route → Pass required parameters**

**POST → Process → Redirect → GET**