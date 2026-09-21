# 📚 Day 070 — Redirects and `url_for()`

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 070  
**Topic:** Redirects and `url_for()`

---

## 1. What Is a Redirect?

A redirect tells the browser to navigate to another URL.

For example:

    /login

may redirect the user to:

    /dashboard

The server sends a redirect response, and the browser makes a new request to the target URL.

---

## 2. Flask `redirect()`

Flask provides the `redirect()` function.

Import it using:

    from flask import redirect

Basic example:

    @app.route("/old")
    def old():
        return redirect("/new")

The browser is instructed to navigate to `/new`.

---

## 3. Why Use Redirects?

Redirects are useful when:

- A user logs in.
- A form is successfully submitted.
- A record is created.
- A page has moved.
- A user should be sent to another route.
- The Post/Redirect/Get pattern is needed.

---

## 4. What Is `url_for()`?

`url_for()` generates a URL for a Flask endpoint.

Example:

    @app.route("/")
    def home():
        return "Home"

The endpoint is normally:

    home

You can generate its URL using:

    url_for("home")

The result is:

    /

---

## 5. Why Use `url_for()`?

Instead of manually writing:

    "/dashboard"

you can use:

    url_for("dashboard")

Benefits:

- Avoids hard-coded route URLs.
- Automatically builds URLs.
- Works well with dynamic routes.
- Makes refactoring easier.
- Clearly connects a URL to a Flask endpoint.

---

## 6. Importing `url_for()`

Use:

    from flask import url_for

Example:

    @app.route("/")
    def home():
        return url_for("about")

If `/about` belongs to the `about()` endpoint, Flask generates:

    /about

---

## 7. `redirect()` + `url_for()`

A very common Flask pattern is:

    return redirect(url_for("home"))

Here:

1. `url_for("home")` generates the URL.
2. `redirect()` tells the browser to navigate there.

---

## 8. Why Not Hard-Code URLs?

You can write:

    return redirect("/home")

But this directly depends on the current URL path.

Using:

    return redirect(url_for("home"))

connects the redirect to the endpoint instead.

If the route changes later:

    @app.route("/homepage")
    def home():

`url_for("home")` can generate the updated URL.

---

## 9. Endpoint

An endpoint is the name Flask uses to identify a route.

Example:

    @app.route("/about")
    def about():
        return "About"

The endpoint is:

    about

Therefore:

    url_for("about")

generates:

    /about

By default, the endpoint name is usually the view function name.

---

## 10. Custom Endpoint

An endpoint can be explicitly specified.

Example:

    @app.route("/profile", endpoint="student_profile")
    def profile():
        return "Student Profile"

Now:

    url_for("student_profile")

generates:

    /profile

---

## 11. Dynamic Route

Consider:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student {student_id}"

To generate a URL:

    url_for("student", student_id=101)

Result:

    /student/101

---

## 12. Multiple Route Parameters

Example:

    @app.route("/student/<int:student_id>/course/<course>")
    def course(student_id, course):
        return f"{student_id}: {course}"

Generate the URL:

    url_for(
        "course",
        student_id=101,
        course="Python"
    )

Result:

    /student/101/course/Python

---

## 13. Query Parameters with `url_for()`

Extra keyword arguments that do not correspond to route variables can become query parameters.

Example:

    url_for("search", q="python")

If the route is:

    @app.route("/search")
    def search():
        ...

The generated URL is conceptually:

    /search?q=python

Another example:

    url_for("search", q="python", page=2)

Result:

    /search?q=python&page=2

---

## 14. Redirect with Dynamic URL

Example:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        ...

Another route can redirect to it:

    return redirect(
        url_for("student", student_id=101)
    )

The browser is redirected to:

    /student/101

---

## 15. Redirect After POST

Suppose a registration form submits data.

A common pattern is:

    POST
      ↓
    Validate
      ↓
    Process
      ↓
    Redirect
      ↓
    GET

Example:

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":
            name = request.form.get("name", "").strip()

            if not name:
                return "Name is required", 400

            return redirect(url_for("success"))

        return "Registration Form"

---

## 16. Post/Redirect/Get

The above pattern is called:

**Post/Redirect/Get (PRG)**

The sequence is:

    POST
      ↓
    Process
      ↓
    Redirect
      ↓
    GET

The browser's final page is reached through GET.

This helps reduce accidental duplicate form submissions caused by refreshing the result page.

---

## 17. Why PRG Is Useful

Imagine a user submits:

    POST /register

If the server directly returns the success page, refreshing that page can potentially repeat the browser's form-submission workflow.

With PRG:

    POST /register
          ↓
    redirect
          ↓
    GET /success

Refreshing the final page performs GET again instead of resubmitting the original POST form.

---

## 18. Redirect Status Codes

A redirect is represented by an HTTP 3xx response.

Common redirect statuses include:

- 301 — Permanent Redirect
- 302 — Found
- 303 — See Other
- 307 — Temporary Redirect
- 308 — Permanent Redirect

Flask's `redirect()` uses a temporary redirect by default.

For many POST-to-GET workflows, a `303 See Other` response can explicitly communicate that the follow-up request should use GET.

Example:

    return redirect(url_for("success"), code=303)

---

## 19. `redirect()` vs `url_for()`

These functions have different jobs.

### `redirect()`

Tells the browser to navigate to another URL.

Example:

    redirect("/home")

### `url_for()`

Generates a URL for a Flask endpoint.

Example:

    url_for("home")

Together:

    redirect(url_for("home"))

---

## 20. Jinja2 `url_for()`

`url_for()` can also be used inside templates.

Example:

    <a href="{{ url_for('home') }}">
        Home
    </a>

For a dynamic route:

    <a href="{{ url_for('student', student_id=101) }}">
        Student
    </a>

This avoids manually constructing URLs.

---

## 21. `url_for()` with Static Files

`url_for()` is also used for Flask static assets.

Example:

    {{ url_for('static', filename='css/style.css') }}

Here:

    static

is the endpoint.

The filename identifies the asset.

---

## 22. Endpoint Names Matter

Suppose:

    @app.route("/dashboard")
    def dashboard():
        return "Dashboard"

Then:

    url_for("dashboard")

is correct.

Do not use:

    url_for("/dashboard")

`url_for()` expects an endpoint name, not a URL path.

---

## 23. Blueprint Note

In larger Flask applications, routes may belong to Blueprints.

Blueprint endpoints are commonly referenced using:

    blueprint_name.endpoint_name

For example:

    url_for("admin.dashboard")

This helps organize routes in larger applications.

---

## 24. Common Mistakes

### Mistake 1: Passing a URL to `url_for()`

Incorrect:

    url_for("/home")

Correct:

    url_for("home")

---

### Mistake 2: Forgetting the endpoint

Incorrect:

    redirect(url_for())

Correct:

    redirect(url_for("home"))

---

### Mistake 3: Wrong endpoint name

If the function is:

    def dashboard():

Use:

    url_for("dashboard")

not:

    url_for("home")

unless the endpoint was explicitly configured as `home`.

---

### Mistake 4: Missing dynamic parameter

For:

    @app.route("/student/<int:student_id>")

You need:

    url_for("student", student_id=101)

---

### Mistake 5: Forgetting POST support

If a form uses POST:

    method="POST"

the route must allow POST.

Example:

    @app.route("/register", methods=["GET", "POST"])

---

## 25. Best Practices

- Prefer `url_for()` over hard-coded internal URLs.
- Use endpoint names correctly.
- Use `redirect(url_for(...))` for route-based redirects.
- Use PRG after successful form submissions where appropriate.
- Pass all required dynamic route parameters.
- Use meaningful endpoint names.
- Keep navigation URLs generated through Flask.
- Use HTTPS for sensitive applications.
- Validate user input before processing it.

---

## 26. Mental Model

Think of:

    url_for()
        ↓
    "Which URL belongs to this Flask endpoint?"

And:

    redirect()
        ↓
    "Tell the browser to go to this URL."

Together:

    redirect(url_for("home"))

means:

**Generate the home URL, then redirect the browser there.**

---

## 27. Complete Example

    from flask import Flask, request, redirect, url_for

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Home"

    @app.route("/success")
    def success():
        return "Registration successful"

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":
            name = request.form.get("name", "").strip()

            if not name:
                return "Name is required", 400

            return redirect(url_for("success"))

        return "Registration Form"

    if __name__ == "__main__":
        app.run(debug=True)

---

## 28. Summary

`redirect()` and `url_for()` are fundamental Flask tools.

`url_for()` generates a URL from an endpoint.

`redirect()` tells the browser to navigate to another URL.

The most important pattern is:

    return redirect(url_for("home"))

For dynamic routes:

    url_for("student", student_id=101)

For query parameters:

    url_for("search", q="python")

For form submission:

    POST → Process → Redirect → GET

This combination is essential for clean Flask navigation and form workflows.