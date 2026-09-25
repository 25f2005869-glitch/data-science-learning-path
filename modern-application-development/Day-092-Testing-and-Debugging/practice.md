# 📝 Day 092 — Testing and Debugging Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 092  
**Topic:** Testing and Debugging  

---

# 🎯 Practice Objectives

Practice testing and debugging a Flask-based Student Management System.

---

# 🟢 Level 1 — Concepts

### Q1. What is software testing?

### Q2. What is debugging?

### Q3. What is the difference between testing and debugging?

### Q4. Explain syntax, runtime, and logical errors.

### Q5. What is unit testing?

### Q6. What is integration testing?

### Q7. What is regression testing?

### Q8. What is an assertion?

---

# 🟡 Level 2 — Python Testing

### Q9. Write a function that returns whether a student has passed.

Rule:

    marks >= 50 → True
    marks < 50  → False

Write tests for:

    50
    49
    100
    0

### Q10. Write a test for a grade calculation function.

Test at least:

    95
    85
    75
    65
    40

---

# 🟠 Level 3 — Flask Testing

Create a Flask test client.

Test:

### Q11

    GET /

Expected:

    200

### Q12

    GET /dashboard

Expected:

    200

when authenticated.

### Q13

    GET /unknown

Expected:

    404

### Q14

Test the student creation route using POST.

Verify that valid form data is accepted.

---

# 🔵 Level 4 — Validation Testing

Test the student form with:

    Valid name
    Empty name
    Valid email
    Invalid email
    Marks = 100
    Marks = 0
    Marks = -1
    Marks = 101
    Missing course
    Duplicate email

For every test, write:

    Input
    Expected Result
    Actual Result
    PASS/FAIL

---

# 🟣 Level 5 — CRUD Testing

Test the complete lifecycle:

    Create Student
         ↓
    Read Student
         ↓
    Update Student
         ↓
    Read Again
         ↓
    Delete Student
         ↓
    Verify Deleted

Make sure each database operation produces the expected result.

---

# 🔴 Level 6 — Authentication Testing

Test:

### Test 1

Valid username + valid password.

Expected:

    Login successful

### Test 2

Valid username + invalid password.

Expected:

    Login rejected

### Test 3

Unauthenticated user visits dashboard.

Expected:

    Access denied or redirect to login

### Test 4

User logs out and visits dashboard.

Expected:

    Access denied or redirect to login

---

# 🟤 Level 7 — Authorization Testing

Create:

    Admin
    Student

Test:

    Admin → Add Student
    Admin → Edit Student
    Admin → Delete Student

Student should not be allowed to perform unauthorized administrative actions.

---

# 🟧 Level 8 — Search and Filtering Tests

Test:

    Search by name
    Search by email
    Partial search
    Empty search
    No results
    Course filter
    Marks filter
    Combined filters
    Sorting

---

# ⭐ Final Debugging Challenge

Suppose the dashboard shows:

    500 Internal Server Error

Follow this workflow:

    1. Reproduce the problem.
    2. Read the traceback.
    3. Identify the exception.
    4. Locate the relevant file and line.
    5. Check the input.
    6. Check the database query.
    7. Fix the root cause.
    8. Run the failing test again.
    9. Run related tests.
    10. Check for regression.

---

# 🧪 Final Test Plan

Create a test plan containing at least:

    5 Authentication tests
    5 CRUD tests
    5 Validation tests
    5 Search/Filtering tests
    3 Error-handling tests

For each test record:

    Test ID
    Feature
    Input
    Expected Result
    Actual Result
    Status

---

# ✅ Definition of Done

    [ ] Unit tests created
    [ ] Flask routes tested
    [ ] GET tested
    [ ] POST tested
    [ ] CRUD tested
    [ ] Validation tested
    [ ] Authentication tested
    [ ] Authorization tested
    [ ] Search tested
    [ ] Filtering tested
    [ ] Error handling tested
    [ ] 404 tested
    [ ] Database tests isolated
    [ ] Debugging workflow practiced
    [ ] Regression tests run