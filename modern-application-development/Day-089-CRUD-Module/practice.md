# 📝 Day 089 — CRUD Module Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 089  
**Topic:** CRUD Module  

---

# 🎯 Practice Objectives

Practice implementing a complete CRUD module using Flask, SQLAlchemy, SQLite, Jinja2, forms, validation, and authentication.

---

# 🟢 Level 1 — Concepts

### Q1. What does CRUD stand for?

### Q2. What is the purpose of the Create operation?

### Q3. What is the difference between Read and Update?

### Q4. Why should Delete normally use POST instead of GET?

### Q5. What is the purpose of `db.session.commit()`?

### Q6. What does `db.session.rollback()` do?

### Q7. What is Post/Redirect/Get?

### Q8. Why is server-side validation necessary?

---

# 🟡 Level 2 — SQLAlchemy

Assume a model named `Student`.

Fields:

    id
    name
    email
    course
    marks

### Q9. Write code to create a new student.

### Q10. Write code to retrieve all students.

### Q11. Write code to retrieve one student using an ID.

### Q12. Write code to update a student's marks.

### Q13. Write code to delete a student.

---

# 🟠 Level 3 — Flask Routes

Create these routes:

    GET  /students
    GET  /students/add
    POST /students/add
    GET  /students/<id>/edit
    POST /students/<id>/edit
    POST /students/<id>/delete

For every route, identify:

- HTTP method
- Database operation
- Template or redirect

---

# 🔵 Level 4 — Forms

Create an Add Student form containing:

    Name
    Email
    Course
    Marks

Validation requirements:

- Name is required.
- Email is required.
- Email must be unique.
- Course is required.
- Marks must be between 0 and 100.

---

# 🟣 Level 5 — Jinja2

Create a student table.

Columns:

    ID
    Name
    Email
    Course
    Marks
    Status
    Actions

Display:

    Passed

when marks are at least 50.

Otherwise display:

    Failed

Add:

    View
    Edit
    Delete

actions.

---

# 🔴 Level 6 — Complete CRUD Challenge

Build a **Student Management CRUD Module**.

## Required Features

### Create

Admin can add students.

### Read

Display all students in a table.

### Update

Admin can edit student information.

### Delete

Admin can delete a student.

### Validation

Validate every submitted field on the server.

### Feedback

Use flash messages after successful or failed operations.

### Authentication

Only logged-in users can access the module.

### Authorization

Only authorized users can modify or delete records.

### Error Handling

Handle:

- Missing student
- Duplicate email
- Invalid marks
- Database errors

---

# ⭐ Final Challenge

Implement this complete flow:

    Login
      ↓
    Dashboard
      ↓
    Student List
      ↓
    Add Student
      ↓
    Save to Database
      ↓
    Redirect to Student List
      ↓
    Edit Student
      ↓
    Update Database
      ↓
    Redirect
      ↓
    Delete Student
      ↓
    Redirect

---

# ✅ Definition of Done

    [ ] Create works
    [ ] Read works
    [ ] Update works
    [ ] Delete works
    [ ] Forms work
    [ ] Validation works
    [ ] Jinja2 displays data
    [ ] Flash messages work
    [ ] Redirects work
    [ ] 404 handling works
    [ ] Authentication works
    [ ] Authorization works
    [ ] CSRF protection is considered
    [ ] Database errors are handled
    [ ] Delete uses POST
    [ ] CRUD interface is responsive