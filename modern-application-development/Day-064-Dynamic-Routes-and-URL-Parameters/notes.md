# 📝 Day 064 — Dynamic Routes and URL Parameters

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 064  
**Topic:** Dynamic Routes and URL Parameters

---

## 1. What is a Dynamic Route?

A dynamic route is a Flask route that contains a variable part.

Example:

    @app.route("/student/<name>")
    def student(name):
        return f"Student: {name}"

The `<name>` portion is dynamic.

The same route can handle:

    /student/Saloni
    /student/Aman
    /student/Riya

---

## 2. What is a URL Parameter?

A URL parameter is a value included in the URL and passed to a Flask view function.

Example:

    /student/101

Here:

    101

can be received by Flask as a parameter.

Example:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student ID: {student_id}"

---

## 3. Static vs Dynamic Route

### Static Route

    @app.route("/about")
    def about():
        return "About Page"

The URL is fixed.

### Dynamic Route

    @app.route("/student/<name>")
    def student(name):
        return f"Student: {name}"

The value of `name` can change.

---

## 4. String Parameter

The simplest dynamic parameter is a string.

Example:

    @app.route("/hello/<name>")
    def hello(name):
        return f"Hello, {name}!"

Request:

    /hello/Saloni

Response:

    Hello, Saloni!

The default converter is generally `string`.

A string parameter does not match a slash-separated path as one value.

---

## 5. Integer Parameter

Use the `int` converter when the value should be an integer.

Example:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student ID: {student_id}"

Valid:

    /student/101

Invalid for this route:

    /student/abc

Flask converts the matched value to an integer before passing it to the function.

---

## 6. Float Parameter

Use the `float` converter for decimal values.

Example:

    @app.route("/course/<float:price>")
    def course(price):
        return f"Course Price: {price}"

Example:

    /course/499.50

The value received by the function is a Python floating-point value.

---

## 7. Path Parameter

The `path` converter can accept a value containing slashes.

Example:

    @app.route("/files/<path:filename>")
    def files(filename):
        return f"File: {filename}"

Request:

    /files/notes/mad1/flask.txt

The `filename` value can contain:

    notes/mad1/flask.txt

---

## 8. Common Route Converters

| Converter | Purpose |
|---|---|
| `string` | Text without `/` |
| `int` | Integer |
| `float` | Floating-point number |
| `path` | Text containing `/` |
| `uuid` | UUID value |

---

## 9. Multiple URL Parameters

A route can contain more than one parameter.

Example:

    @app.route("/student/<int:student_id>/course/<course_name>")
    def student_course(student_id, course_name):
        return f"Student {student_id} is studying {course_name}"

Example URL:

    /student/101/course/MAD1

Flask passes:

    student_id = 101
    course_name = "MAD1"

---

## 10. Parameter Names Must Match

The parameter names in the route should correspond to the function parameters.

Correct:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"ID: {student_id}"

Incorrect:

    @app.route("/student/<int:student_id>")
    def student(id):
        return f"ID: {id}"

The route variable is `student_id`, while the function expects `id`.

---

## 11. Dynamic Route with a Student Name

Example:

    @app.route("/student/<name>")
    def student(name):
        return f"Welcome, {name}!"

Request:

    /student/Saloni

Response:

    Welcome, Saloni!

This is useful for learning the basic concept of URL parameters.

---

## 12. Dynamic Route with Student ID

For record identifiers, an integer parameter is often more appropriate.

Example:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student record: {student_id}"

Example:

    /student/25

---

## 13. Multiple Parameters in Practice

Example:

    @app.route("/student/<int:student_id>/course/<course>")
    def course(student_id, course):
        return f"Student {student_id}: {course}"

Example:

    /student/101/course/DBMS

Response:

    Student 101: DBMS

---

## 14. `url_for()` with Dynamic Parameters

`url_for()` can generate URLs for dynamic routes.

Example:

    from flask import url_for

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student {student_id}"

A URL can be generated using:

    url_for("student", student_id=101)

This produces the URL corresponding to:

    /student/101

---

## 15. Why Use `url_for()`?

Avoid manually constructing URLs whenever possible.

Instead of:

    "/student/" + str(student_id)

Flask can generate the URL using:

    url_for("student", student_id=student_id)

Advantages:

- Less hard-coding
- Easier route maintenance
- Fewer URL mistakes
- Works well with templates
- Useful when applications grow

---

## 16. Parameter Type Conversion

Consider:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return str(type(student_id))

For:

    /student/101

the parameter is received as an integer.

The converter performs the route-level conversion.

---

## 17. What Happens with an Invalid Type?

Suppose the route is:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student {student_id}"

Request:

    /student/abc

The URL does not satisfy the integer route pattern.

If there is no other matching route, Flask returns a 404 response.

---

## 18. URL Parameters vs Query Parameters

These are different concepts.

### URL Parameter

Example:

    /student/101

The `101` is part of the route path.

### Query Parameter

Example:

    /students?page=2

The `page=2` portion is part of the query string.

Query parameters will be studied more deeply when handling requests.

---

## 19. URL Design

Good dynamic URLs should be:

- Meaningful
- Predictable
- Consistent
- Easy to read

Good examples:

    /student/101
    /course/MLF
    /student/101/course/DBMS
    /project/5

Avoid unnecessarily complicated URL structures.

---

## 20. Practical Example

Consider a student application.

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student profile: {student_id}"

Then:

    /student/101

can represent student record 101.

Another route:

    @app.route("/student/<int:student_id>/course/<course>")
    def student_course(student_id, course):
        return f"Student {student_id} - Course: {course}"

can represent a specific student's course.

---

## 21. Dynamic Routes and Backend Applications

Dynamic routes are useful for:

- Student profiles
- Product pages
- Course pages
- Blog posts
- User profiles
- Project pages
- Database records

For example:

    /product/25

can represent product 25.

    /post/10

can represent blog post 10.

---

## 22. Complete Example

    from flask import Flask, url_for

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Student Portal"

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return f"Student ID: {student_id}"

    @app.route("/student/<int:student_id>/course/<course>")
    def student_course(student_id, course):
        return f"Student {student_id} is studying {course}"

    if __name__ == "__main__":
        app.run(debug=True)

---

## 23. Common Mistakes

### Mistake 1: Parameter mismatch

Route and function parameters do not correspond.

### Mistake 2: Wrong converter

Using `<int:id>` when the URL contains non-numeric data.

### Mistake 3: Forgetting angle brackets

Incorrect:

    /student/id

Dynamic:

    /student/<id>

### Mistake 4: Confusing path and query parameters

These are different parts of a URL.

### Mistake 5: Hard-coding dynamic URLs

Prefer `url_for()` for generating Flask URLs.

---

## 24. Key Takeaway

Dynamic routes allow one Flask route to handle many different URLs.

Remember:

    @app.route("/student/<int:student_id>")

means that `student_id` comes from the URL and Flask converts it to an integer.

The core pattern is:

    Dynamic URL
          ↓
    URL Parameter
          ↓
    View Function
          ↓
    Response

For multiple parameters:

    /student/<int:id>/course/<course>

For generated URLs:

    url_for("student", student_id=101)