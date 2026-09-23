# 💬 Day 084 — Flash Messages and Validation — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 084  
**Topic:** Flash Messages and Validation

---

## 1. What Are Flash Messages?

Flash messages are temporary messages displayed to users after an action.

Examples:

- "Registration successful."
- "Invalid password."
- "Student deleted successfully."
- "Please correct the form."

They are useful for communicating the result of an operation.

---

## 2. Flask `flash()`

Flask provides the `flash()` function.

Example:

    from flask import flash

    flash("Registration successful.")

The message is stored temporarily and can be displayed on a later request.

---

## 3. Why Is `SECRET_KEY` Required?

Flask's default session mechanism is used to store flash messages.

Therefore, the application needs a secret key.

Example:

    app.config["SECRET_KEY"] = "change-this-in-production"

For a real application, use a strong secret value and keep it outside source control.

---

## 4. Displaying Flash Messages

Jinja2 provides `get_flashed_messages()`.

Example:

    {% with messages = get_flashed_messages() %}
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    {% endwith %}

The messages can then be displayed in the template.

---

## 5. Flash Message Categories

Flash messages can have categories.

Example:

    flash("Student created successfully.", "success")

Another example:

    flash("Invalid email address.", "error")

Common application-level categories include:

- success
- error
- warning
- info

The category is a label used by the application to decide how the message should be presented.

---

## 6. Reading Categories

Use `with_categories=True`.

Example:

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% for category, message in messages %}
            <div class="{{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endwith %}

This allows CSS or frontend code to style different message types.

---

## 7. Flash Message Lifecycle

A typical flow is:

    User submits form
            ↓
    Flask receives POST
            ↓
    Validate input
            ↓
    Operation succeeds/fails
            ↓
    flash(message, category)
            ↓
    redirect()
            ↓
    New request
            ↓
    get_flashed_messages()
            ↓
    Message displayed

---

## 8. Why Use Redirect?

A common pattern is:

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

This is called the Post/Redirect/Get pattern.

It helps prevent accidental form resubmission when the user refreshes the result page.

---

# VALIDATION

## 9. What Is Validation?

Validation checks whether input satisfies expected rules.

Example:

A registration form may require:

- Name is not empty
- Email has a valid format
- Age is within an allowed range
- Password has sufficient length

---

## 10. Client-Side Validation

Client-side validation happens in the browser.

HTML provides attributes such as:

    required
    minlength
    maxlength
    min
    max
    pattern
    type="email"

JavaScript can also perform validation.

Client-side validation provides fast feedback.

However, it must not be the only validation layer.

---

## 11. Server-Side Validation

Server-side validation happens in Flask after the request reaches the server.

Example:

    name = request.form.get("name", "").strip()

    if not name:
        flash("Name is required.", "error")
        return redirect(url_for("register"))

The server must validate data because users can bypass browser-side validation.

---

## 12. Client-Side vs Server-Side

| Client-Side | Server-Side |
|---|---|
| Runs in browser | Runs on server |
| Fast feedback | Trusted validation layer |
| Improves user experience | Protects application logic |
| Can be bypassed | Must always be performed |
| HTML/JavaScript | Flask/Python |

Best practice:

**Use both, but always trust server-side validation.**

---

## 13. Required Field Validation

Example:

    name = request.form.get("name", "").strip()

    if not name:
        flash("Name is required.", "error")

Using `.strip()` removes unnecessary whitespace from the beginning and end.

---

## 14. Length Validation

Example:

    if len(name) < 3:
        flash("Name must contain at least 3 characters.", "error")

For a maximum length:

    if len(name) > 50:
        flash("Name is too long.", "error")

---

## 15. Email Validation

A server should validate that an email value follows the application's expected format.

For more robust applications, use a well-tested validation library or appropriate validation logic rather than relying only on a simple regular expression.

Example basic check:

    email = request.form.get("email", "").strip()

    if "@" not in email:
        flash("Enter a valid email address.", "error")

This is only a basic demonstration and is not a complete email validator.

---

## 16. Numeric Validation

Example:

    age_text = request.form.get("age", "").strip()

    try:
        age = int(age_text)
    except ValueError:
        flash("Age must be a number.", "error")

After conversion, business rules can be applied:

    if age < 13:
        flash("Age must be at least 13.", "error")

---

## 17. Business Rule Validation

Not every validation rule is about data type.

Examples:

- Marks must be between 0 and 100.
- Course must be one of the allowed courses.
- Username must be unique.
- Password confirmation must match.
- A user cannot delete another user's record.

These are application or business rules.

---

## 18. Validating Choice Values

Do not blindly trust values from dropdowns.

Example:

    allowed_courses = {
        "Data Science",
        "Programming",
        "Mathematics"
    }

    course = request.form.get("course", "").strip()

    if course not in allowed_courses:
        flash("Invalid course selected.", "error")

The server checks the submitted value against the allowed choices.

---

## 19. Validation Workflow

A good server-side validation workflow is:

1. Receive the request.
2. Read submitted values.
3. Normalize appropriate values.
4. Check required fields.
5. Check data types.
6. Check length/range.
7. Check business rules.
8. If invalid, show an error.
9. If valid, process the operation.
10. Flash success feedback.
11. Redirect to the appropriate page.

---

## 20. Multiple Validation Errors

A form can contain several invalid fields.

Example:

    errors = []

    if not name:
        errors.append("Name is required.")

    if not email:
        errors.append("Email is required.")

    if age < 18:
        errors.append("Age must be at least 18.")

Then display the errors appropriately.

For simple applications, flash messages can also be generated individually.

---

## 21. Validation Before Database Operations

Always validate data before inserting or updating database records.

Flow:

    Form
      ↓
    Validation
      ↓
    Valid?
      ↓
    Yes → Database operation
      ↓
    No → Error message

Do not save invalid data simply because the browser accepted it.

---

## 22. Flash Messages with CRUD

### Create

    db.session.add(student)
    db.session.commit()

    flash("Student created successfully.", "success")
    return redirect(url_for("students"))

### Update

    student.name = name
    db.session.commit()

    flash("Student updated successfully.", "success")

### Delete

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully.", "success")

---

## 23. Error Handling During Database Operations

Database operations can fail.

A transaction can be rolled back when necessary.

Example:

    try:
        db.session.add(student)
        db.session.commit()
    except Exception:
        db.session.rollback()
        flash("Unable to save the student.", "error")

In production applications, catch appropriate exceptions rather than using overly broad exception handling everywhere.

---

## 24. User-Friendly Messages

Good message:

    "Please enter a valid email address."

Poor message:

    "ValidationError: invalid field email."

User-facing messages should be understandable without exposing internal implementation details.

---

## 25. Security Principles

Never trust user input.

Always validate:

- Form data
- Query parameters
- URL parameters
- Uploaded files
- JSON data
- Cookies where relevant

Validation is not a replacement for:

- Authentication
- Authorization
- CSRF protection
- Output escaping
- Parameterized database queries

Each security layer solves a different problem.

---

## 26. Flash Messages and Authentication

Example:

    if not valid_password:
        flash("Invalid email or password.", "error")
        return redirect(url_for("login"))

Avoid revealing whether an account exists when that information could help attackers enumerate users.

---

## 27. Flash Messages and `url_for()`

A common pattern is:

    flash("Profile updated successfully.", "success")
    return redirect(url_for("profile"))

`url_for()` generates the URL from the Flask endpoint.

This is preferable to hardcoding URLs throughout the application.

---

## 28. Important Flask Functions

    flash()
    get_flashed_messages()
    redirect()
    url_for()
    request.form
    request.args

Together, these functions are frequently used in form workflows.

---

## 29. Complete Conceptual Example

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":

            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()

            if not name:
                flash("Name is required.", "error")
                return redirect(url_for("register"))

            if not email:
                flash("Email is required.", "error")
                return redirect(url_for("register"))

            # Save validated data here.

            flash("Registration successful.", "success")
            return redirect(url_for("login"))

        return render_template("register.html")

---

## 30. Key Takeaway

**Flash messages communicate temporary feedback.**

**Validation checks whether input is acceptable.**

A reliable Flask form workflow is:

    Receive
       ↓
    Validate
       ↓
    Process
       ↓
    Flash
       ↓
    Redirect
       ↓
    Display

Always perform validation on the server before trusting or storing user input.