# 📚 Day 072 — Flask Error Handling and Debugging

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 072  
**Topic:** Flask Error Handling and Debugging

---

## 1. What Is Error Handling?

Error handling is the process of detecting errors and responding to them properly.

A Flask application can encounter errors because of:

- Invalid URLs
- Missing resources
- Invalid user input
- Programming mistakes
- Database problems
- Server-side exceptions
- Configuration problems

Good error handling prevents the application from showing confusing or sensitive information to users.

---

## 2. Types of Programming Errors

### Syntax Error

A syntax error occurs when Python code does not follow Python's syntax rules.

Example:

    if student_name
        print(student_name)

The missing colon causes a syntax error.

### Runtime Error

A runtime error occurs while the program is executing.

Example:

    number = 10 / 0

This produces a `ZeroDivisionError`.

### Logical Error

A logical error occurs when the program runs but produces an incorrect result.

Example:

    marks = 40
    if marks >= 50:
        result = "Pass"
    else:
        result = "Pass"

The program runs, but the logic is incorrect.

---

## 3. HTTP Errors in Flask

Flask applications commonly use HTTP status codes to describe the result of a request.

Important status codes:

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 301 | Permanent Redirect |
| 302 | Temporary Redirect |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 500 | Internal Server Error |

---

## 4. 404 Not Found

A `404` error occurs when the requested resource does not exist.

Example:

    @app.route("/students/<int:student_id>")
    def student(student_id):
        if student_id != 1:
            abort(404)

If the student does not exist, Flask can return a 404 response.

---

## 5. The `abort()` Function

Flask provides `abort()` to stop request processing and return an HTTP error.

Example:

    from flask import abort

    @app.route("/admin")
    def admin():
        is_admin = False

        if not is_admin:
            abort(403)

        return "Admin Dashboard"

Here, Flask returns a `403 Forbidden` response.

---

## 6. Custom Error Handlers

Flask allows us to define custom responses for HTTP errors.

Example:

    @app.errorhandler(404)
    def page_not_found(error):
        return "Page not found", 404

Now Flask uses this function whenever a 404 error occurs.

---

## 7. Custom 500 Error

A 500 error means that an unexpected server-side error occurred.

Example:

    @app.errorhandler(500)
    def internal_server_error(error):
        return "Something went wrong on the server.", 500

The application should not expose technical details to normal users.

---

## 8. Custom Error Pages

Instead of returning plain text, we can render an HTML template.

Example:

    from flask import render_template

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

A project can have:

    templates/
    ├── 404.html
    └── 500.html

This provides a better user experience.

---

## 9. Exception Handling with `try-except`

Python's `try-except` can handle expected exceptions.

Example:

    @app.route("/calculate")
    def calculate():
        try:
            result = 10 / 0
            return str(result)
        except ZeroDivisionError:
            return "Cannot divide by zero.", 400

The exception is caught instead of crashing the request.

---

## 10. `finally`

The `finally` block executes whether an exception occurs or not.

Example:

    try:
        result = 10 / 2
    except ZeroDivisionError:
        result = 0
    finally:
        print("Calculation completed")

`finally` is useful for cleanup operations.

---

## 11. Raising Exceptions

Python allows us to raise an exception explicitly.

Example:

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

This is useful for enforcing application rules.

---

## 12. Debug Mode

During development, Flask can run in debug mode.

Example:

    app.run(debug=True)

Debug mode provides detailed error information and automatically reloads the application when code changes.

### Important

Debug mode should NOT be enabled in production.

Detailed debugging information can expose sensitive application information.

---

## 13. Traceback

A traceback shows where an error occurred.

It can help identify:

- File name
- Line number
- Function
- Exception type
- Error message
- Execution path

A traceback is one of the most useful debugging tools in Python.

---

## 14. Flask Debugging Workflow

A simple debugging workflow is:

1. Reproduce the problem.
2. Read the error message.
3. Check the traceback.
4. Identify the file and line number.
5. Inspect variables.
6. Check the request data.
7. Fix the problem.
8. Test the application again.

---

## 15. Logging Basics

Logging helps developers understand what is happening inside an application.

Example:

    app.logger.info("Student page requested")
    app.logger.warning("Invalid student ID")
    app.logger.error("Database operation failed")

Common logging levels include:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

## 16. Development vs Production

### Development

During development:

- Debugging tools can be enabled.
- Detailed errors are useful.
- Tracebacks help identify problems.
- Developers can use logs extensively.

### Production

In production:

- Debug mode should be disabled.
- Users should see friendly error pages.
- Detailed technical information should stay private.
- Errors should be logged securely.
- A production WSGI server should be used.

---

## 17. Error Handling Flow

A simplified Flask flow is:

    Browser
        ↓
    Request
        ↓
    Flask Route
        ↓
    Application Logic
        ↓
    Error?
       / \
     No   Yes
     ↓      ↓
  Response  Error Handler
              ↓
         Error Response

---

## 18. Common Mistakes

### Mistake 1 — Exposing Debug Information

Do not expose detailed tracebacks to normal users in production.

### Mistake 2 — Catching Every Exception

Avoid unnecessarily broad exception handling.

Example to avoid:

    try:
        some_operation()
    except Exception:
        pass

This can hide important problems.

### Mistake 3 — Returning the Wrong Status Code

If a page is missing, return `404`, not `200`.

### Mistake 4 — Ignoring Validation

Always validate user input before processing it.

### Mistake 5 — Using Debug Mode in Production

Never use:

    app.run(debug=True)

for a production deployment.

---

## 19. Best Practices

- Validate user input.
- Use meaningful HTTP status codes.
- Create custom error pages.
- Handle expected exceptions.
- Log useful information.
- Avoid exposing sensitive details.
- Use debug mode only during development.
- Test error scenarios.
- Keep error messages user-friendly.
- Do not silently ignore exceptions.

---

## 20. Key Takeaway

Flask error handling combines Python exception handling with HTTP error handling.

The most important tools are:

- `try`
- `except`
- `finally`
- `raise`
- `abort()`
- `@app.errorhandler()`
- Flask debug mode
- Tracebacks
- Logging

Good error handling makes a Flask application more reliable, secure, and easier to maintain.