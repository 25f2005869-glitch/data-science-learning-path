# 📚 Day 069 — GET and POST Methods

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 069  
**Topic:** GET and POST Methods

---

## 1. What Is an HTTP Method?

An HTTP method tells the server what kind of operation the client is requesting.

Common HTTP methods include:

- GET
- POST
- PUT
- PATCH
- DELETE

This day focuses on:

- GET
- POST

---

## 2. GET Method

GET is commonly used to request or retrieve data from a server.

Examples:

- Opening a webpage
- Searching
- Filtering information
- Reading a resource

Example:

    GET /courses

The browser asks the server for the `/courses` resource.

---

## 3. GET Request

A GET request can contain query parameters in the URL.

Example:

    /search?q=python

Here:

    /search

is the route.

And:

    q=python

is a query parameter.

---

## 4. Query Parameters

Query parameters are values added to a URL after `?`.

Example:

    /search?q=python

Multiple parameters can be separated using `&`.

Example:

    /search?q=python&page=2

Parameters:

    q = python
    page = 2

---

## 5. Reading GET Data in Flask

Flask provides `request.args`.

Example:

    from flask import Flask, request

    app = Flask(__name__)

    @app.route("/search")
    def search():
        query = request.args.get("q", "")
        return f"Search: {query}"

---

## 6. POST Method

POST is commonly used to submit data to a server.

Examples:

- Registration
- Login
- Creating a record
- Submitting feedback
- Uploading data
- Sending a form

Example:

    POST /register

The submitted form data is normally carried in the request body.

---

## 7. POST Request Body

Unlike a typical GET query, form data submitted using POST is normally sent in the request body.

Example HTML:

    <form action="/register" method="POST">
        <input type="text" name="name">
        <button type="submit">Register</button>
    </form>

The browser sends the value associated with `name` in the request body.

---

## 8. Reading POST Data in Flask

Flask provides `request.form` for normal submitted form fields.

Example:

    @app.route("/register", methods=["POST"])
    def register():
        name = request.form.get("name", "")
        return f"Registered: {name}"

---

## 9. `request.method`

Flask provides:

    request.method

It tells us which HTTP method was used.

Example:

    if request.method == "GET":
        ...

Or:

    if request.method == "POST":
        ...

---

## 10. One Route for GET and POST

A route can support both methods.

Example:

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":
            name = request.form.get("name", "")
            return f"Hello, {name}"

        return "Registration Form"

The route behaves differently depending on the request method.

---

## 11. GET Form

Example:

    <form action="/search" method="GET">
        <input type="search" name="q">
        <button type="submit">Search</button>
    </form>

If the user enters:

    Flask

The URL can become:

    /search?q=Flask

Flask reads it using:

    request.args.get("q")

---

## 12. POST Form

Example:

    <form action="/register" method="POST">
        <input type="text" name="name">
        <input type="email" name="email">
        <button type="submit">Register</button>
    </form>

Flask can read the submitted values:

    name = request.form.get("name")
    email = request.form.get("email")

---

## 13. GET Request Flow

The general flow is:

    Browser
        ↓
    GET Request
        ↓
    Flask Route
        ↓
    request.args
        ↓
    Processing
        ↓
    Response
        ↓
    Browser

---

## 14. POST Request Flow

The general flow is:

    Browser
        ↓
    POST Request
        ↓
    Flask Route
        ↓
    request.form
        ↓
    Validation
        ↓
    Processing
        ↓
    Response
        ↓
    Browser

---

## 15. GET vs POST

| Feature | GET | POST |
|---|---|---|
| Main purpose | Retrieve data | Submit/process data |
| Typical data location | URL query string | Request body |
| Data visible in URL | Yes | Normally no |
| Bookmarkable | Usually yes | Usually no |
| Search | Common | Uncommon |
| Registration | Usually not appropriate | Common |
| State-changing operation | Should not | May |
| Sensitive information | Avoid | Better choice, but still needs HTTPS |

---

## 16. GET Is Not "Less Secure" by Itself

GET data can appear in the URL.

For example:

    /search?q=python

URLs can be stored in:

- Browser history
- Server logs
- Analytics systems
- Referrer information in some situations

Therefore, sensitive information should not be placed in GET query parameters.

---

## 17. POST Does Not Mean Encryption

POST data is not automatically encrypted.

For example:

    POST /login

does not itself provide encryption.

HTTPS is what protects HTTP communication during transmission.

Therefore:

**POST + HTTPS** is appropriate for many sensitive form submissions.

---

## 18. GET Should Be Safe

GET requests should generally be used for operations that do not change server-side state.

Good example:

    GET /courses

Potentially problematic design:

    GET /delete-student/10

Deleting data should normally use a method intended for state-changing operations, such as DELETE, or an appropriate POST workflow when working with HTML forms.

---

## 19. POST Can Change State

POST can be used for operations such as:

    POST /register

    POST /students

    POST /feedback

The server may create or modify data as a result.

---

## 20. Form `action`

The `action` attribute specifies where the form is submitted.

Example:

    <form action="/register" method="POST">

The request is sent to:

    /register

---

## 21. Form `method`

The `method` attribute specifies the HTTP method.

Example:

    <form method="GET">

or:

    <form method="POST">

If the method is omitted, the default form submission method is GET.

---

## 22. The `name` Attribute

The `name` attribute identifies the submitted field.

Example:

    <input type="text" name="student_name">

Flask:

    student_name = request.form.get("student_name")

Without a meaningful `name`, the expected field data will not be submitted under that field name.

---

## 23. Default Values

Using `.get()` with a default value is useful.

Example:

    name = request.form.get("name", "")

For GET:

    page = request.args.get("page", "1")

---

## 24. Basic Server-Side Validation

Never trust user input.

Example:

    name = request.form.get("name", "").strip()

    if not name:
        return "Name is required", 400

Server-side validation is necessary even when HTML validation is present.

---

## 25. Post/Redirect/Get

A common web pattern is:

    POST
      ↓
    Process
      ↓
    Redirect
      ↓
    GET

Example:

    from flask import redirect, url_for

    return redirect(url_for("home"))

This is called **Post/Redirect/Get (PRG)**.

It helps avoid accidental duplicate form submissions when the user refreshes the resulting page.

---

## 26. GET Example in Flask

    from flask import Flask, request

    app = Flask(__name__)

    @app.route("/search", methods=["GET"])
    def search():
        query = request.args.get("q", "").strip()

        if not query:
            return "Search query is required", 400

        return f"Searching for: {query}"

---

## 27. POST Example in Flask

    from flask import Flask, request

    app = Flask(__name__)

    @app.route("/register", methods=["POST"])
    def register():
        name = request.form.get("name", "").strip()

        if not name:
            return "Name is required", 400

        return f"Student registered: {name}"

---

## 28. GET and POST Together

Example:

    @app.route("/student", methods=["GET", "POST"])
    def student():

        if request.method == "POST":
            name = request.form.get("name", "").strip()

            if not name:
                return "Name is required", 400

            return f"Submitted: {name}"

        return "Student Form"

The GET request can display the form.

The POST request can process the submitted form.

---

## 29. Common Mistakes

### Mistake 1: Using `request.form` for GET query parameters

For:

    /search?q=python

Use:

    request.args.get("q")

### Mistake 2: Using `request.args` for POST form fields

For a POST form:

    request.form.get("name")

is normally used.

### Mistake 3: Forgetting the route method

If a route only allows GET:

    @app.route("/register")

and the browser sends POST, Flask can return:

    405 Method Not Allowed

### Mistake 4: Forgetting `name`

Incorrect:

    <input type="text">

Better:

    <input type="text" name="name">

### Mistake 5: Trusting client-side validation

Browser validation can be bypassed.

Always validate important data on the server.

---

## 30. Security Best Practices

- Use HTTPS.
- Validate server-side input.
- Never put passwords in GET query parameters.
- Escape output appropriately.
- Use parameterized SQL queries.
- Protect state-changing forms against CSRF where applicable.
- Never store plaintext passwords.
- Do not treat POST as encryption.
- Avoid exposing sensitive data in URLs.

---

## 31. Mental Model

Remember:

    GET
    ↓
    Retrieve
    ↓
    Query String
    ↓
    request.args

And:

    POST
    ↓
    Submit
    ↓
    Request Body
    ↓
    request.form

---

## 32. Summary

GET and POST are fundamental HTTP methods.

GET is commonly used to retrieve data.

POST is commonly used to submit or process data.

In Flask:

    request.args

reads query parameters.

    request.form

reads normal form fields submitted through POST.

    request.method

identifies the HTTP method.

A good Flask developer should understand not only the syntax but also why a particular HTTP method is appropriate for an operation.