# 📝 Day 072 — Flask Error Handling and Debugging Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 072  
**Topic:** Flask Error Handling and Debugging

---

# 🎯 Practice Objectives

Practice:

- Flask HTTP errors
- `abort()`
- Custom error handlers
- `try-except`
- `raise`
- Debugging
- Tracebacks
- Logging

---

# 🟢 Level 1 — Basic Questions

### Q1. What is error handling?

Write a short explanation.

### Q2. What is the difference between a syntax error and a runtime error?

### Q3. What does HTTP status code 404 mean?

### Q4. What does HTTP status code 500 mean?

### Q5. What is the purpose of `abort()` in Flask?

### Q6. Why should debug mode not be used in production?

---

# 🟡 Level 2 — Code Practice

### Q7. Create a Flask route `/student/<int:student_id>`.

If the student ID is not `1`, return a 404 error using `abort()`.

### Q8. Create a custom 404 error handler.

Return:

    Page not found

with status code `404`.

### Q9. Create a custom 500 error handler.

Return a user-friendly server error message.

### Q10. Write a Python example using `try-except` to handle division by zero.

### Q11. Write an example that raises `ValueError` when marks are outside the range 0–100.

---

# 🟠 Level 3 — Debugging Practice

### Q12. Find the error:

    number = 10
    result = number / 0

Identify:

- Error type
- Reason
- Solution

### Q13. Find the logical error:

    marks = 80

    if marks >= 50:
        result = "Fail"
    else:
        result = "Pass"

Correct the logic.

### Q14. Create a route that accepts a student ID and handles an invalid ID safely.

---

# 🔴 Level 4 — Mini Challenge

## Student Error Handling System

Create a Flask application with:

- `/`
- `/student/<int:student_id>`
- Custom 404 page
- Custom 500 page
- `abort()`
- `try-except`
- Input validation
- Logging

### Requirements

1. Student ID `1` should display student information.
2. Other IDs should return 404.
3. Invalid input should be handled safely.
4. Errors should be logged.
5. Users should receive friendly error messages.
6. Debug mode should be used only during development.

---

# 🧠 Revision Questions

1. What is a traceback?
2. What is the purpose of `try-except`?
3. When is `finally` executed?
4. What does `raise` do?
5. What is `abort(403)`?
6. How do you create a custom Flask error handler?
7. Why should production applications hide tracebacks?
8. What is the difference between a 404 and a 500 error?
9. What is Flask debug mode?
10. Why is logging useful?

---

# ✅ Self-Check

Before moving to Day 073, make sure you can:

- [ ] Explain common error types.
- [ ] Explain HTTP error codes.
- [ ] Use `abort()`.
- [ ] Create a 404 handler.
- [ ] Create a 500 handler.
- [ ] Use `try-except`.
- [ ] Use `raise`.
- [ ] Read a traceback.
- [ ] Use Flask logging.
- [ ] Explain why debug mode is unsafe in production.