# 📝 Day 088 — Dashboard Development Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 088  
**Topic:** Dashboard Development  

---

# 🎯 Practice Objectives

Practice building a database-driven Flask dashboard using authentication, Jinja2, CRUD, and responsive UI concepts.

---

## 🟢 Level 1 — Conceptual Questions

### Q1. What is a dashboard?

Write a short definition.

### Q2. Why are dashboards useful in web applications?

### Q3. What is the difference between authentication and authorization?

### Q4. Why should a private dashboard be protected?

### Q5. What is the role of Jinja2 in a Flask dashboard?

### Q6. Why is `url_for()` preferred over hard-coded URLs?

### Q7. Why is server-side authorization necessary?

### Q8. What is the purpose of summary cards?

---

# 🟡 Level 2 — Flask and Jinja2

### Q9. Write a Flask route for `/dashboard`.

Requirements:

- Use `render_template()`.
- Pass a variable named `students`.

### Q10. Write a Jinja2 loop that displays student names.

### Q11. Write a Jinja2 condition that displays:

- `Passed` for marks >= 50
- `Failed` otherwise

### Q12. Write a Jinja2 condition for an empty student list.

### Q13. Write a Flask route that reads a GET search parameter named `search`.

### Q14. Write a flash message for successful student creation.

---

# 🟠 Level 3 — Database Dashboard

Create a dashboard for a Student Management System.

Student fields:

    id
    name
    email
    course
    marks

Display:

- Total students
- Average marks
- Passed students
- Failed students
- Student table

---

# 🔵 Level 4 — Dashboard Features

Add the following:

### Feature 1 — Search

Search students by name.

### Feature 2 — Filtering

Filter students by course.

### Feature 3 — Sorting

Allow sorting by marks.

### Feature 4 — CRUD

Add buttons for:

    Add
    View
    Edit
    Delete

### Feature 5 — Flash Messages

Show success/error messages after actions.

---

# 🟣 Level 5 — Authentication

Create two roles:

    Admin
    Student

Admin:

- View students
- Add students
- Edit students
- Delete students

Student:

- View own information
- View courses
- View marks

Make sure authorization is checked on the server.

---

# 🔴 Level 6 — Mini Dashboard Challenge

Build a complete **Student Academic Dashboard**.

## Required Sections

### Header

Display:

    Student Academic Dashboard

### Sidebar

Include:

    Dashboard
    Students
    Courses
    Profile
    Logout

### Summary Cards

Display:

    Total Students
    Total Courses
    Average Marks
    Passed Students

### Student Table

Columns:

    ID
    Name
    Email
    Course
    Marks
    Status
    Actions

### Search

Add a search box for student names.

### Filter

Add a course filter.

### Actions

Provide:

    View
    Edit
    Delete

### Feedback

Use flash messages for successful or failed operations.

---

# ⭐ Final Challenge

Build the dashboard using:

- Flask
- Jinja2
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- JavaScript
- Authentication
- Authorization
- CRUD
- Validation
- Flash messages

## Definition of Done

    [ ] Dashboard route works
    [ ] Authentication works
    [ ] Authorization works
    [ ] Database data displays
    [ ] Summary cards work
    [ ] Student table works
    [ ] Search works
    [ ] Filtering works
    [ ] CRUD actions work
    [ ] Flash messages work
    [ ] Validation works
    [ ] Responsive layout works
    [ ] Security checks are implemented