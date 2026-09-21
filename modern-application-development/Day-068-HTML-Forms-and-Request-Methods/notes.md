# 📚 Day 068 — HTML Forms and Request Methods

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 068  
**Topic:** HTML Forms and Request Methods

---

## 1. What Is an HTML Form?

An HTML form is used to collect information from a user.

Examples:

- Student registration
- Login
- Search
- Contact form
- Feedback
- Course enrollment

Basic structure:

    <form action="/submit" method="POST">
        <input type="text" name="student_name">
        <button type="submit">Submit</button>
    </form>

---

## 2. Important Form Attributes

The two most important attributes are:

    action
    method

### `action`

Specifies where the form data should be sent.

Example:

    <form action="/register" method="POST">

The data is sent to the `/register` route.

### `method`

Specifies the HTTP method used for submitting the form.

Common methods:

    GET
    POST

---

## 3. GET Request

GET is commonly used when the request is intended to retrieve data.

Example:

    <form action="/search" method="GET">

If the user enters:

    Python

The browser may generate a URL similar to:

    /search?q=Python

The submitted values become query parameters.

---

## 4. POST Request

POST is commonly used when data is submitted to the server for processing.

Example:

    <form action="/register" method="POST">

The submitted data is sent in the request body instead of being placed in the URL.

POST is commonly used for:

- Registration
- Login
- Creating records
- Updating data
- Sending larger form submissions

---

## 5. GET vs POST

| Feature | GET | POST |
|---|---|---|
| Main purpose | Retrieve data | Submit/process data |
| Data location | URL query string | Request body |
| Visible in URL | Yes | No |
| Bookmarkable | Usually yes | Usually no |
| Suitable for passwords | No | Better choice |
| Common use | Search/filter | Registration/login |
| Changes server state | Should not | May |

Important:

**POST does not automatically make data secure.**

HTTPS is still required to protect data during transmission.

---

## 6. Flask Request Object

Flask provides the `request` object for accessing incoming request information.

Import it:

    from flask import request

Example:

    @app.route("/search")
    def search():
        query = request.args.get("q")
        return query

---

## 7. `request.args`

`request.args` is used to access query parameters.

For example:

    /search?q=Python

Python:

    query = request.args.get("q")

The value of `query` becomes:

    Python

---

## 8. Multiple Query Parameters

URL:

    /search?q=Python&page=2

Flask:

    query = request.args.get("q")
    page = request.args.get("page")

The values are:

    query = "Python"
    page = "2"

---

## 9. `request.form`

`request.form` is used to access data submitted through a form using POST.

HTML:

    <form action="/register" method="POST">
        <input type="text" name="name">
        <input type="email" name="email">
        <button type="submit">Register</button>
    </form>

Flask:

    name = request.form.get("name")
    email = request.form.get("email")

---

## 10. Why Is the `name` Attribute Important?

The `name` attribute identifies form data.

Example:

    <input type="text" name="student_name">

Flask can access it using:

    request.form.get("student_name")

An input without a meaningful `name` generally will not provide the expected form field name during normal form submission.

---

## 11. `request.method`

Flask provides:

    request.method

to determine the HTTP method.

Example:

    if request.method == "POST":
        ...

A route can support both GET and POST:

    @app.route("/register", methods=["GET", "POST"])
    def register():

---

## 12. GET and POST in One Route

Example:

    from flask import Flask, request

    app = Flask(__name__)

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":
            name = request.form.get("name")
            return f"Hello, {name}"

        return "Registration Form"

This route behaves differently depending on the request method.

---

## 13. Typical Form Flow

The complete flow is:

1. User opens a page.
2. Flask sends an HTML form.
3. User fills in the form.
4. User clicks Submit.
5. Browser creates an HTTP request.
6. The request is sent to the form `action`.
7. Flask receives the request.
8. Flask checks the request method.
9. Flask reads the submitted data.
10. Flask validates and processes the data.
11. Flask returns a response.

---

## 14. GET Form Example

HTML:

    <form action="/search" method="GET">
        <input type="text" name="q">
        <button type="submit">Search</button>
    </form>

Flask:

    @app.route("/search")
    def search():
        query = request.args.get("q", "")
        return f"Search: {query}"

---

## 15. POST Form Example

HTML:

    <form action="/register" method="POST">
        <input type="text" name="name">
        <button type="submit">Register</button>
    </form>

Flask:

    @app.route("/register", methods=["POST"])
    def register():
        name = request.form.get("name", "")
        return f"Registered: {name}"

---

## 16. Default Values

You can provide a default value when using `.get()`.

Example:

    name = request.form.get("name", "")

If `name` is missing, an empty string is returned.

Another example:

    page = request.args.get("page", "1")

If `page` is missing, the value becomes `"1"`.

---

## 17. Basic Validation

Never assume that submitted data is valid.

Example:

    name = request.form.get("name", "").strip()

    if not name:
        return "Name is required", 400

Validation should happen on the server even if HTML validation is already present.

---

## 18. HTML Validation

HTML can provide basic client-side validation.

Example:

    <input
        type="email"
        name="email"
        required
    >

Another example:

    <input
        type="number"
        name="age"
        min="1"
        max="100"
        required
    >

Client-side validation improves user experience.

Server-side validation is still necessary.

---

## 19. Redirect After POST

A common Flask pattern is:

**POST → Process → Redirect → GET**

Example:

    from flask import redirect, url_for

    return redirect(url_for("home"))

This pattern is commonly called **Post/Redirect/Get (PRG)**.

It helps prevent accidental form resubmission when the user refreshes the resulting page.

---

## 20. Form Data vs Query Parameters

### Query Parameters

Example:

    /search?q=python

Access with:

    request.args.get("q")

### Form Data

Usually submitted through POST:

    <form method="POST">

Access with:

    request.form.get("q")

---

## 21. Why GET Is Useful for Search

Search forms often use GET.

Example:

    <form action="/search" method="GET">
        <input name="q">
        <button type="submit">Search</button>
    </form>

The URL can represent the search.

For example:

    /search?q=flask

This makes the result easier to bookmark and share.

---

## 22. Why POST Is Useful for Registration

Registration usually changes server-side data.

Example:

    <form action="/register" method="POST">

The registration information is submitted in the request body.

The server can then:

1. Validate the data.
2. Process the data.
3. Store the data if appropriate.
4. Return or redirect to another page.

---

## 23. Common Mistakes

### Mistake 1: Forgetting `name`

Incorrect:

    <input type="text">

Better:

    <input type="text" name="name">

### Mistake 2: Reading POST data with `request.args`

For normal POST form fields, use:

    request.form

### Mistake 3: Reading GET query parameters with `request.form`

For query parameters, use:

    request.args

### Mistake 4: Not allowing POST

If the route only supports GET:

    @app.route("/register")

but the form sends POST, Flask can return:

    405 Method Not Allowed

Use:

    @app.route("/register", methods=["GET", "POST"])

when the route should support both.

### Mistake 5: Trusting browser validation

Client-side validation can be bypassed.

Always validate important data on the server.

---

## 24. Security Considerations

Form data is user-controlled input.

Never blindly trust it.

Important practices:

- Validate input.
- Normalize input where appropriate.
- Escape output.
- Use parameterized database queries.
- Use HTTPS.
- Protect sensitive forms against CSRF where applicable.
- Never store passwords as plain text.
- Do not assume POST means encrypted.

---

## 25. Best Practices

- Give every form control a meaningful `name`.
- Choose GET or POST based on the purpose of the operation.
- Use `request.args` for query parameters.
- Use `request.form` for submitted form fields.
- Validate data on the server.
- Use `url_for()` for Flask route URLs.
- Use PRG after successful POST operations when appropriate.
- Use HTTPS for sensitive data.
- Keep form handling logic organized.

---

## 26. Mental Model

Remember:

    GET
    ↓
    URL + Query Parameters
    ↓
    request.args

And:

    POST
    ↓
    Request Body
    ↓
    request.form

---

## 27. Summary

HTML forms provide a way for users to send data to Flask.

The two fundamental methods are:

    GET
    POST

For GET query parameters:

    request.args.get("name")

For POST form data:

    request.form.get("name")

A Flask route can support both methods:

    @app.route("/form", methods=["GET", "POST"])

Understanding this request flow is essential before learning more advanced Flask request handling.