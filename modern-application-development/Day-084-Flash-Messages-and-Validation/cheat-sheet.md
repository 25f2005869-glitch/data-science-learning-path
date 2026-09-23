# 💬 Day 084 — Flash Messages and Validation — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 084  
**Topic:** Flash Messages and Validation

---

## 1. Import Flash

    from flask import flash

---

## 2. Create Message

    flash("Registration successful.")

With category:

    flash("Registration successful.", "success")

---

## 3. Display Messages

    {% with messages = get_flashed_messages() %}
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    {% endwith %}

---

## 4. Display Categories

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% for category, message in messages %}
            <div class="{{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endwith %}

---

## 5. SECRET_KEY

    app.config["SECRET_KEY"] = "strong-secret-value"

Use a secure secret in real applications and do not commit it to source control.

---

## 6. Read Form Data

    name = request.form.get("name", "").strip()

---

## 7. Required Validation

    if not name:
        flash("Name is required.", "error")
        return redirect(url_for("register"))

---

## 8. Length Validation

    if len(name) < 3:
        flash("Name is too short.", "error")

    if len(name) > 50:
        flash("Name is too long.", "error")

---

## 9. Numeric Validation

    age_text = request.form.get("age", "").strip()

    try:
        age = int(age_text)
    except ValueError:
        flash("Age must be a number.", "error")

---

## 10. Range Validation

    if marks < 0 or marks > 100:
        flash("Marks must be between 0 and 100.", "error")

---

## 11. Choice Validation

    allowed_courses = {
        "Data Science",
        "Programming",
        "Mathematics"
    }

    if course not in allowed_courses:
        flash("Invalid course.", "error")

---

## 12. HTML Validation

    <input type="text" required>

    <input type="email" required>

    <input type="text" minlength="3" maxlength="50">

    <input type="number" min="0" max="100">

---

## 13. POST → Validate → Redirect

    POST
      ↓
    Validate
      ↓
    Process
      ↓
    flash()
      ↓
    redirect()
      ↓
    GET

This is the Post/Redirect/Get pattern.

---

## 14. Common Categories

| Category | Purpose |
|---|---|
| `success` | Successful operation |
| `error` | Failed operation |
| `warning` | Warning |
| `info` | General information |

These are application conventions; Flask does not require these exact names.

---

## 15. Client vs Server Validation

**Client-side:**
Browser-based, fast feedback, can be bypassed.

**Server-side:**
Runs on server, must always be performed.

Remember:

**Never rely only on client-side validation.**

---

## 16. Common Functions

| Function | Purpose |
|---|---|
| `flash()` | Store temporary message |
| `get_flashed_messages()` | Retrieve messages |
| `request.form` | Read POST form data |
| `request.args` | Read query parameters |
| `redirect()` | Send browser to another URL |
| `url_for()` | Generate URL |
| `render_template()` | Render HTML template |

---

## 17. Database Safety

Validate before:

    INSERT
    UPDATE

For failed transactions:

    db.session.rollback()

---

## 18. Secure Workflow

    User Input
        ↓
    Normalize
        ↓
    Validate
        ↓
    Authorize
        ↓
    Database Operation
        ↓
    Flash Feedback
        ↓
    Redirect

---

## 19. Remember

**Flash = temporary user feedback**

**Validation = check input**

**`flash()` = create message**

**`get_flashed_messages()` = display messages**

**`SECRET_KEY` = required for Flask's session-backed flash mechanism**

**Server-side validation = mandatory**