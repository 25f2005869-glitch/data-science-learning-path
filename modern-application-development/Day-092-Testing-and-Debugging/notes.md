# 📚 Day 092 — Testing and Debugging Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 092  
**Topic:** Testing and Debugging  

---

# 1. What is Testing?

Testing is the process of checking whether software behaves according to its requirements.

Example:

If a student registration form requires marks between 0 and 100, testing should verify:

    50 → Valid
    100 → Valid
    0 → Valid
    -5 → Invalid
    150 → Invalid

Testing helps discover problems before users encounter them.

---

# 2. What is Debugging?

Debugging is the process of finding the cause of a software problem and fixing it.

Basic workflow:

    Problem
       ↓
    Reproduce
       ↓
    Investigate
       ↓
    Find Cause
       ↓
    Fix
       ↓
    Test Again

---

# 3. Testing vs Debugging

### Testing

Asks:

    "Does the application work correctly?"

### Debugging

Asks:

    "Why is the application not working correctly?"

Testing discovers problems.

Debugging investigates and fixes them.

---

# 4. Types of Software Errors

## Syntax Error

The code does not follow the language syntax.

Example:

    if student:
        print(student.name

A closing parenthesis is missing.

---

## Runtime Error

The program starts but fails while executing.

Example:

    student = None
    print(student.name)

This can produce an error because `student` is `None`.

---

## Logical Error

The program runs but produces an incorrect result.

Example:

    marks = 80

    if marks >= 90:
        grade = "A"
    elif marks >= 70:
        grade = "C"

The program runs, but the grading logic may be incorrect for the intended grading system.

---

# 5. Testing Levels

Common testing levels include:

    Unit Testing
    Integration Testing
    System Testing
    Acceptance Testing

---

# 6. Unit Testing

Unit testing tests a small unit of code independently.

Examples:

- Function
- Class method
- Validation function
- Grade calculation function

Example:

    def calculate_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        return "C"

A unit test can check whether:

    calculate_grade(95) == "A"

---

# 7. Integration Testing

Integration testing checks whether multiple components work together.

Example:

    Flask Route
        ↓
    SQLAlchemy
        ↓
    SQLite
        ↓
    Response

A CRUD application should test that a route can correctly interact with the database.

---

# 8. Functional Testing

Functional testing checks application features from the user's perspective.

Examples:

    Login
    Logout
    Add Student
    Edit Student
    Delete Student
    Search Student
    Filter Student

---

# 9. Regression Testing

Regression testing checks whether a change has broken functionality that previously worked.

Example:

You change the student search module.

After the change, you should also verify:

    Login
    Dashboard
    CRUD
    Search
    Logout

---

# 10. Assertions

An assertion checks whether an expected condition is true.

Example:

    assert total == 5

If the condition is false, the test fails.

Assertions are fundamental to automated testing.

---

# 11. Python unittest

Python includes the `unittest` framework.

Example:

    import unittest

    class TestStudent(unittest.TestCase):

        def test_total(self):
            total = 80 + 90
            self.assertEqual(total, 170)

    if __name__ == "__main__":
        unittest.main()

---

# 12. pytest

`pytest` is another popular Python testing framework.

Installation:

    pip install pytest

Simple test:

    def test_total():
        total = 80 + 90
        assert total == 170

Run tests:

    pytest

---

# 13. Flask Testing

Flask provides a test client for sending requests to an application without manually using a browser.

Conceptual example:

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

---

# 14. Testing a Route

Example:

    response = client.get("/dashboard")

    assert response.status_code == 200

A status code of 200 normally indicates a successful response.

---

# 15. Testing a 404 Route

Example:

    response = client.get("/does-not-exist")

    assert response.status_code == 404

This checks that an unknown route is handled correctly.

---

# 16. Testing POST

A test client can send form data.

Example:

    response = client.post(
        "/students/add",
        data={
            "name": "Saloni",
            "email": "saloni@example.com",
            "marks": "85"
        }
    )

The test can then verify the response or redirect.

---

# 17. Testing Redirects

Example:

    response = client.post(
        "/students/add",
        data={
            "name": "Saloni",
            "email": "saloni@example.com",
            "marks": "85"
        }
    )

    assert response.status_code == 302

Depending on the application, a different redirect status may be intentionally used.

---

# 18. Testing CRUD

A CRUD module should test all four operations.

### Create

Verify that a new record is added.

### Read

Verify that the record can be retrieved.

### Update

Verify that the record changes correctly.

### Delete

Verify that the record is removed.

Flow:

    Create
      ↓
    Read
      ↓
    Update
      ↓
    Read Again
      ↓
    Delete
      ↓
    Verify Removal

---

# 19. Testing Validation

Test both valid and invalid input.

Example:

    Valid:
    marks = 85

    Invalid:
    marks = 150

Also test:

    Empty name
    Invalid email
    Duplicate email
    Missing course
    Negative marks

---

# 20. Testing Authentication

Authentication tests can include:

    Login with valid credentials
    Login with invalid credentials
    Access dashboard while logged in
    Access dashboard while logged out
    Logout
    Access protected route after logout

---

# 21. Testing Authorization

Authentication and authorization are different.

Test that:

    Admin → Can delete students

and:

    Student → Cannot delete students

Authorization must be checked on the server.

---

# 22. Testing Search

Test:

    Exact search
    Partial search
    Case variations
    Empty search
    No matching results
    Search by multiple fields

Example:

    Search: Saloni

Expected:

    Saloni Tiwari

---

# 23. Testing Filtering

Test:

    Course = Data Science
    Marks >= 80
    Course + Marks

Also test when no records match the filters.

---

# 24. Testing Database Operations

Database tests should verify:

    Insert
    Select
    Update
    Delete
    Constraints
    Rollback

For example, a unique email constraint should reject duplicate email values.

---

# 25. Test Database

Testing should generally use a separate test database or isolated test environment.

Avoid accidentally modifying important development or production data.

A test database can be:

    Created before tests
    Used during tests
    Reset after tests

---

# 26. Fixtures

Testing frameworks can provide reusable setup data.

Conceptually:

    Create test database
       ↓
    Insert test student
       ↓
    Run test
       ↓
    Clean database

This avoids repeating setup code.

---

# 27. Debugging with Tracebacks

When Python encounters an unhandled exception, it provides a traceback.

A traceback helps identify:

- Error type
- Error message
- File
- Line number
- Call sequence

Read the traceback from the bottom upward to find the final exception and its message, while also checking the earlier frames for the source of the problem.

---

# 28. Debug Mode

Flask development applications can use debug mode.

Example:

    app.run(debug=True)

Debug mode can provide useful development information.

However:

    Never use Flask debug mode as a production deployment setting.

---

# 29. Logging

Logging records information about application execution.

Example:

    app.logger.info("Student created")

Other useful levels include:

    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL

Logs are useful when diagnosing application behavior.

---

# 30. Debugging with Print Statements

Simple debugging:

    print(student)

This can help during early development.

However, structured logging and a debugger are generally better for larger applications.

---

# 31. Browser Developer Tools

For frontend problems, use browser developer tools.

Useful tabs:

    Elements
    Console
    Network
    Sources

Examples:

### Console

Find JavaScript errors.

### Network

Inspect:

    Request
    Response
    Status Code
    Headers

### Elements

Inspect HTML and CSS.

---

# 32. HTTP Status Codes

Important testing codes:

    200 → OK
    201 → Created
    302 → Redirect
    400 → Bad Request
    401 → Unauthorized
    403 → Forbidden
    404 → Not Found
    405 → Method Not Allowed
    500 → Internal Server Error

Testing should verify that routes return appropriate responses.

---

# 33. Testing Forms

Test:

    Empty fields
    Invalid email
    Invalid number
    Out-of-range marks
    Duplicate values
    Valid submission

Also verify that server-side validation exists.

Client-side validation alone is not sufficient.

---

# 34. Testing Error Handling

Test expected failures.

Examples:

    Invalid ID
    Missing record
    Invalid form
    Unauthorized access
    Database constraint failure

The application should fail safely and provide an appropriate response.

---

# 35. Test Case Structure

A useful test case contains:

    Test ID
    Feature
    Input
    Expected Result
    Actual Result
    Status

Example:

    Test ID: TC-001
    Feature: Login
    Input: Valid credentials
    Expected: Dashboard displayed
    Actual: Dashboard displayed
    Status: PASS

---

# 36. Test-Driven Development Basics

Test-driven development (TDD) commonly follows:

    Red
      ↓
    Green
      ↓
    Refactor

### Red

Write a test that fails.

### Green

Write the minimum code needed to pass it.

### Refactor

Improve the code while keeping tests passing.

TDD is a development approach; it is not required for every project.

---

# 37. Debugging Workflow

Use this process:

    1. Reproduce the problem.
    2. Read the error message.
    3. Inspect the traceback.
    4. Identify the failing component.
    5. Check input and output.
    6. Isolate the problem.
    7. Fix the root cause.
    8. Run the test again.
    9. Run related tests.
    10. Check for regression.

---

# 38. Common Debugging Mistakes

### Mistake 1

Changing many things at once.

### Mistake 2

Ignoring the actual error message.

### Mistake 3

Testing only successful cases.

### Mistake 4

Using debug mode in production.

### Mistake 5

Testing against production data.

### Mistake 6

Fixing symptoms instead of the root cause.

### Mistake 7

Not retesting after a fix.

---

# 39. Testing Strategy for MAD 1 Project

For the Student Management System:

    Authentication
        ↓
    Dashboard
        ↓
    CRUD
        ↓
    Search
        ↓
    Filtering
        ↓
    Validation
        ↓
    Error Handling
        ↓
    Responsive UI

Each module should be tested individually and then together.

---

# 40. Final Testing Checklist

    [ ] Routes tested
    [ ] GET requests tested
    [ ] POST requests tested
    [ ] Forms tested
    [ ] Validation tested
    [ ] CRUD tested
    [ ] Database tested
    [ ] Authentication tested
    [ ] Authorization tested
    [ ] Search tested
    [ ] Filtering tested
    [ ] Error handling tested
    [ ] 404 tested
    [ ] Invalid input tested
    [ ] Responsive UI tested
    [ ] Browser console checked
    [ ] Logs checked
    [ ] Regression tests run

---

# 41. Key Takeaway

Testing asks:

    "Does it work?"

Debugging asks:

    "Why does it not work?"

A reliable Flask application needs both.

    Build
      ↓
    Test
      ↓
    Find Problem
      ↓
    Debug
      ↓
    Fix
      ↓
    Test Again
      ↓
    Deploy Safely