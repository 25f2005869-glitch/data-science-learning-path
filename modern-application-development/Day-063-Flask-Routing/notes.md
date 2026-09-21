# 📝 Day 063 — Flask Routing

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 063  
**Topic:** Flask Routing

---

## 1. What is Routing?

Routing means connecting a URL to a specific Python function.

For example:

    /about

can be connected to:

    def about():
        return "About Page"

When a browser requests `/about`, Flask executes the corresponding view function.

The basic idea is:

    URL → Route → View Function → Response

---

## 2. Basic Route

A basic Flask route looks like:

    @app.route("/")
    def home():
        return "Home Page"

Here:

- `@app.route("/")` defines the route.
- `/` is the URL path.
- `home()` is the view function.
- The returned string is the response.

---

## 3. Root Route

The root route represents the main URL of the application.

Example:

    @app.route("/")
    def home():
        return "Welcome to my website!"

When the user visits the root URL, Flask executes `home()`.

---

## 4. Multiple Routes

A Flask application can have multiple routes.

Example:

    @app.route("/")
    def home():
        return "Home"

    @app.route("/about")
    def about():
        return "About"

    @app.route("/contact")
    def contact():
        return "Contact"

Each URL has its own view function.

---

## 5. View Functions

A view function handles a request for a particular route.

Example:

    @app.route("/profile")
    def profile():
        return "Student Profile"

The function name can be chosen by the developer, but it should be meaningful.

---

## 6. Dynamic Routes

Sometimes the URL needs to contain a changing value.

Example:

    @app.route("/student/<name>")
    def student(name):
        return f"Student: {name}"

A request such as:

    /student/Saloni

passes `Saloni` to the `name` parameter.

The result becomes:

    Student: Saloni

---

## 7. URL Parameters

A variable can be placed inside angle brackets.

Example:

    @app.route("/user/<username>")
    def user(username):
        return f"Welcome, {username}"

The URL:

    /user/Saloni

produces:

    Welcome, Saloni

---

## 8. Integer Route Converter

Flask can restrict a dynamic value to an integer.

Example:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student ID: {student_id}"

Valid:

    /student/101

Invalid:

    /student/abc

The `int` converter converts the URL value into an integer.

---

## 9. Float Route Converter

A floating-point value can be accepted using:

    <float:value>

Example:

    @app.route("/price/<float:amount>")
    def price(amount):
        return f"Price: {amount}"

---

## 10. Path Route Converter

The `path` converter can accept a path containing slashes.

Example:

    @app.route("/files/<path:filename>")
    def files(filename):
        return f"File: {filename}"

A URL such as:

    /files/documents/mad1/notes.pdf

can be handled by this route.

---

## 11. Common Route Converters

| Converter | Purpose |
|---|---|
| `string` | Text without `/` |
| `int` | Integer |
| `float` | Floating-point number |
| `path` | Text including `/` |
| `uuid` | UUID value |

The default converter is `string`.

---

## 12. Route Parameters and Function Parameters

The variable in the route should match the function parameter.

Correct:

    @app.route("/student/<name>")
    def student(name):
        return f"Student: {name}"

The route variable is `name`, and the function receives `name`.

---

## 13. HTTP Methods

Routes can specify which HTTP methods they accept.

Example:

    @app.route("/login", methods=["GET", "POST"])
    def login():
        return "Login Page"

Common HTTP methods include:

- GET
- POST
- PUT
- PATCH
- DELETE

For basic Flask web applications, GET and POST are especially important.

---

## 14. GET

GET is commonly used to request or retrieve data.

Example:

    @app.route("/students", methods=["GET"])
    def students():
        return "Student List"

---

## 15. POST

POST is commonly used to submit data to the server.

Example:

    @app.route("/student", methods=["POST"])
    def create_student():
        return "Student Created"

Form handling and request data will be studied in greater detail later.

---

## 16. `url_for()`

`url_for()` generates a URL for a view function.

Example:

    from flask import Flask, url_for

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Home"

    @app.route("/about")
    def about():
        return "About"

Instead of manually writing a URL, Flask can generate it using the function name.

Example:

    url_for("about")

This produces the URL for the `about` endpoint.

---

## 17. Why Use `url_for()`?

Using `url_for()` helps avoid hard-coding URLs.

If a route changes from:

    /about

to:

    /about-me

links generated through `url_for("about")` can continue to use the updated route.

This becomes especially useful in larger applications and templates.

---

## 18. Endpoint

A Flask route has an endpoint.

By default, the endpoint is usually the name of the view function.

Example:

    @app.route("/about")
    def about():
        return "About"

The endpoint is:

    about

Therefore:

    url_for("about")

can generate the URL.

---

## 19. Custom Endpoint

An endpoint can also be explicitly specified.

Example:

    @app.route("/profile", endpoint="student_profile")
    def profile():
        return "Profile"

The endpoint is now:

    student_profile

It can be referenced using:

    url_for("student_profile")

---

## 20. Trailing Slash

Consider:

    @app.route("/about/")
    def about():
        return "About"

The trailing slash is part of the route design.

Flask can redirect between slash variants depending on the route definition and request.

The important point is to keep URL design consistent.

---

## 21. 404 Not Found

If no route matches the requested URL, Flask returns a 404 Not Found response.

For example, if only this route exists:

    @app.route("/")
    def home():
        return "Home"

and the user requests:

    /unknown

Flask cannot find a matching route and returns 404.

---

## 22. Route Order and Specificity

Routes should be designed carefully, especially when using dynamic paths.

For example:

    /student/profile

and:

    /student/<name>

should be considered together when designing URLs.

Clear and predictable URL structures make applications easier to maintain.

---

## 23. Route Naming Best Practices

Good route names are:

- Short
- Meaningful
- Consistent
- Easy to understand
- Usually lowercase

Examples:

    /about
    /contact
    /students
    /projects
    /profile

Avoid unnecessarily complicated URLs.

---

## 24. Practical Student Example

Example:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student ID: {student_id}"

A request:

    /student/101

produces:

    Student ID: 101

This pattern is useful for pages representing individual records.

---

## 25. Complete Basic Example

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Home Page"

    @app.route("/about")
    def about():
        return "About Page"

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student ID: {student_id}"

    if __name__ == "__main__":
        app.run(debug=True)

---

## 26. Request Flow

The routing process can be understood as:

    Browser
        ↓
    HTTP Request
        ↓
    Flask Application
        ↓
    Route Matching
        ↓
    View Function
        ↓
    Response
        ↓
    Browser

---

## 27. Common Mistakes

### Mistake 1: Missing `@app.route()`

A function does not automatically become a route.

### Mistake 2: Parameter mismatch

If the route uses:

    <student_id>

the function should receive:

    student_id

### Mistake 3: Wrong URL

The requested URL must match an available route.

### Mistake 4: Wrong HTTP method

A route configured for specific methods may reject other methods.

### Mistake 5: Confusing endpoint and URL

The endpoint is usually the view function name.

The URL is the path requested by the browser.

---

## 28. Key Takeaway

Flask routing connects URLs with Python functions.

Remember:

    @app.route("/path")
    def function():
        return response

For dynamic URLs:

    @app.route("/student/<int:id>")
    def student(id):
        return f"Student {id}"

Routing is the foundation for connecting the browser to Flask backend logic.