# ⚡ Day 092 — Testing and Debugging Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 092  
**Topic:** Testing and Debugging  

---

## 🔹 Testing

    Testing
    = Checking expected behavior

---

## 🔹 Debugging

    Debugging
    = Finding and fixing the cause of a problem

---

## 🔹 Error Types

    Syntax
    Runtime
    Logical

---

## 🔹 Testing Types

    Unit
    Integration
    Functional
    System
    Acceptance
    Regression

---

## 🔹 Assertion

    assert result == expected

---

## 🔹 unittest

    import unittest

    class TestExample(unittest.TestCase):

        def test_total(self):
            self.assertEqual(
                80 + 90,
                170
            )

---

## 🔹 pytest

    pip install pytest

Run:

    pytest

---

## 🔹 Flask Test Client

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

---

## 🔹 GET Test

    response = client.get("/dashboard")

    assert response.status_code == 200

---

## 🔹 404 Test

    response = client.get("/unknown")

    assert response.status_code == 404

---

## 🔹 POST Test

    response = client.post(
        "/students/add",
        data={
            "name": "Saloni",
            "email": "saloni@example.com",
            "marks": "85"
        }
    )

---

## 🔹 CRUD Testing

    Create → Verify
    Read   → Verify
    Update → Verify
    Delete → Verify

---

## 🔹 Validation Tests

    Empty input
    Invalid email
    Invalid marks
    Duplicate email
    Missing field

---

## 🔹 Authentication Tests

    Valid Login
    Invalid Login
    Protected Route
    Logout
    Post-Logout Access

---

## 🔹 Authorization

    Authentication
    = Who are you?

    Authorization
    = What can you do?

---

## 🔹 HTTP Codes

    200 → OK
    201 → Created
    302 → Redirect
    400 → Bad Request
    401 → Unauthorized
    403 → Forbidden
    404 → Not Found
    405 → Method Not Allowed
    500 → Server Error

---

## 🔹 Debugging Workflow

    Reproduce
       ↓
    Read Error
       ↓
    Traceback
       ↓
    Isolate
       ↓
    Fix
       ↓
    Test
       ↓
    Regression Test

---

## 🔹 Flask Debug Mode

    app.run(debug=True)

Use only during development.

---

## 🔹 Logging

    app.logger.debug()
    app.logger.info()
    app.logger.warning()
    app.logger.error()
    app.logger.critical()

---

## 🔹 Browser DevTools

    Elements → HTML/CSS
    Console  → JavaScript errors
    Network  → HTTP requests
    Sources  → Debugging

---

## 🔹 TDD

    Red
      ↓
    Green
      ↓
    Refactor

---

## 🔹 Golden Rule

    Test → Diagnose → Fix → Retest