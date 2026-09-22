# ⚡ Day 072 — Flask Error Handling and Debugging Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 072  
**Topic:** Flask Error Handling and Debugging

---

## 🔹 Error Types

| Error | Meaning |
|---|---|
| Syntax Error | Invalid Python syntax |
| Runtime Error | Error during execution |
| Logical Error | Program runs but gives wrong result |

---

## 🔹 Important HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 500 | Internal Server Error |

---

## 🔹 `abort()`

    from flask import abort

    abort(404)

Used to immediately return an HTTP error.

---

## 🔹 Custom Error Handler

    @app.errorhandler(404)
    def page_not_found(error):
        return "Page not found", 404

---

## 🔹 Custom 500 Handler

    @app.errorhandler(500)
    def server_error(error):
        return "Internal server error", 500

---

## 🔹 Try-Except

    try:
        result = 10 / 0
    except ZeroDivisionError:
        result = 0

---

## 🔹 Finally

    try:
        operation()
    except Exception:
        handle_error()
    finally:
        cleanup()

---

## 🔹 Raise

    raise ValueError("Invalid value")

---

## 🔹 Debug Mode

    app.run(debug=True)

Use only during development.

---

## 🔹 Logging

    app.logger.debug("Debug message")
    app.logger.info("Information")
    app.logger.warning("Warning")
    app.logger.error("Error")
    app.logger.critical("Critical error")

---

## 🔹 Debugging Workflow

    Reproduce
        ↓
    Read error
        ↓
    Check traceback
        ↓
    Find file + line
        ↓
    Inspect variables
        ↓
    Fix
        ↓
    Test again

---

## 🔹 Production Rules

- Disable debug mode.
- Do not expose tracebacks.
- Log errors securely.
- Show friendly error pages.
- Validate user input.
- Use correct HTTP status codes.

---

## ⭐ Remember

`404` → Resource not found

`403` → Access forbidden

`400` → Bad request

`500` → Server-side error

`abort()` → Stop request with an HTTP error

`@app.errorhandler()` → Customize error response

`try-except` → Handle Python exceptions

`debug=True` → Development only