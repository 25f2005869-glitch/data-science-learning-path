# 📝 Day 095 — Final MAD 1 Project Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 095  
**Topic:** Final MAD 1 Project

---

# Part A — Project Planning

## Task 1

Write the problem statement for a Student Academic Management System.

## Task 2

Identify the target users.

## Task 3

List at least 10 functional requirements.

## Task 4

List at least 5 non-functional requirements.

## Task 5

Design the main application modules.

---

# Part B — Database

## Task 6

Design a `User` table.

Include:

    id
    username
    email
    password_hash
    role

## Task 7

Design a `Student` table.

Include:

    id
    name
    email
    age
    course
    marks

## Task 8

Design a `Course` table.

## Task 9

Explain the relationship between Student and Course.

## Task 10

Explain why an Enrollment table can be useful.

---

# Part C — Flask

## Task 11

Create a Flask application.

## Task 12

Create routes for:

    /
    /login
    /logout
    /dashboard
    /students

## Task 13

Create a dynamic student route.

Example concept:

    /students/<int:student_id>

## Task 14

Use `url_for()` to generate application URLs.

---

# Part D — Authentication

## Task 15

Implement registration.

Requirements:

- Validate input.
- Hash passwords.
- Store the password hash.
- Prevent duplicate usernames/emails.

## Task 16

Implement login.

## Task 17

Implement logout.

## Task 18

Protect the dashboard from unauthorized users.

---

# Part E — CRUD

## Task 19

Implement Create Student.

## Task 20

Implement Read Students.

## Task 21

Implement Update Student.

## Task 22

Implement Delete Student.

## Task 23

Use Post/Redirect/Get after successful form submissions.

---

# Part F — Search and Filtering

## Task 24

Create a GET search form.

Search by student name.

## Task 25

Add course filtering.

## Task 26

Add minimum marks filtering.

## Task 27

Add sorting.

## Task 28

Handle the no-results situation.

---

# Part G — UI

## Task 29

Create a dashboard containing:

- Total students
- Total courses
- Average marks
- Passed students

## Task 30

Create a responsive student table.

## Task 31

Create a responsive navigation bar.

## Task 32

Create reusable templates using template inheritance.

---

# Part H — Validation and Errors

## Task 33

Validate:

- Name
- Email
- Age
- Marks
- Course

## Task 34

Add flash messages for successful and unsuccessful operations.

## Task 35

Create custom 404 and 500 pages.

---

# Part I — Testing

## Task 36

Write tests for:

- Home page
- Login
- Logout
- Dashboard
- Student creation
- Student update
- Student deletion
- Search
- Invalid input

---

# Part J — Optimization

## Task 37

Review the database queries.

## Task 38

Identify queries that can be optimized.

## Task 39

Consider pagination.

## Task 40

Review image sizes.

## Task 41

Review unused CSS and JavaScript.

## Task 42

Find duplicated code and refactor it.

---

# Part K — Security Review

Complete the following checklist:

- [ ] Passwords are hashed.
- [ ] Secrets are protected.
- [ ] Environment variables are used.
- [ ] Server-side validation exists.
- [ ] CSRF protection is considered.
- [ ] Authorization checks exist.
- [ ] Debug mode is disabled for production.
- [ ] HTTPS is used in production.
- [ ] Sensitive errors are not exposed.
- [ ] Passwords are not logged.

---

# Part L — Final Project Review

Answer these questions:

### Q43. What problem does your application solve?

### Q44. What technologies did you use?

### Q45. What database did you use?

### Q46. How does authentication work?

### Q47. How does CRUD work?

### Q48. How does search work?

### Q49. How did you make the UI responsive?

### Q50. How did you test the application?

### Q51. What optimizations did you perform?

### Q52. How did you prepare the application for deployment?

---

# 🏆 Final Challenge

Build the complete Student Academic Management System from scratch.

The project should contain:

    Authentication
    Authorization
    Dashboard
    Student CRUD
    Search
    Filtering
    Validation
    Flash Messages
    Jinja2 Templates
    Template Inheritance
    Responsive UI
    Error Handling
    Testing
    Optimization
    Security
    Deployment Preparation

---

# ⭐ Definition of Done

The project is considered complete when:

- [ ] Core functionality works.
- [ ] Database operations work.
- [ ] Authentication works.
- [ ] CRUD works.
- [ ] Search works.
- [ ] Validation works.
- [ ] Error handling works.
- [ ] UI is responsive.
- [ ] Tests pass.
- [ ] Security has been reviewed.
- [ ] Performance has been reviewed.
- [ ] Documentation is complete.
- [ ] Deployment requirements are prepared.