# 📝 Day 085 — Database Integration Project — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 085  
**Topic:** Database Integration Project

---

# 🎯 Project Goal

Build a Student Management System using:

- Flask
- SQLAlchemy
- SQLite
- Jinja2
- HTML
- CSS
- JavaScript

---

# Part A — Database Design

Create a `Student` model with:

- `id`
- `name`
- `email`
- `age`
- `course`
- `marks`

Requirements:

- `id` should be the primary key.
- `name` should not be empty.
- `email` should be unique.
- `age` should be an integer.
- `marks` should be between 0 and 100.

---

# Part B — CRUD

## Task 1 — Create

Create a route that adds a new student.

Requirements:

- Read form data.
- Validate the data.
- Create a Student object.
- Add it to the session.
- Commit the transaction.
- Flash a success message.
- Redirect to the student list.

---

## Task 2 — Read

Create a route:

    /students

Display all students.

---

## Task 3 — Read One

Create:

    /students/<id>

Display information about one student.

Return a 404 response if the student does not exist.

---

## Task 4 — Update

Create an edit form.

Update:

- Name
- Email
- Age
- Course
- Marks

Commit the changes.

Display a success flash message.

---

## Task 5 — Delete

Create a delete operation.

Requirements:

- Find the student.
- Delete the record.
- Commit.
- Flash a success message.
- Redirect to the student list.

---

# Part C — Search

Add a search box.

Search URL:

    /students?search=saloni

Requirements:

- Use GET.
- Read `request.args`.
- Strip whitespace.
- Search student names.
- Use SQLAlchemy filtering.
- Handle no results.

---

# Part D — Multiple-Field Search

Modify search so one keyword can search:

- Name
- Email
- Course

Example:

    /students?search=data

---

# Part E — Filtering

Add a course filter.

Allowed courses:

    Data Science
    Programming
    Mathematics

Example:

    /students?course=Data%20Science

---

# Part F — Marks Filter

Add:

- Minimum marks
- Maximum marks

Example:

    /students?min_marks=70&max_marks=95

Validate the values before using them in the query.

---

# Part G — Sorting

Allow users to sort by:

- Name
- Marks

Support:

- Ascending
- Descending

Do not blindly insert a user-provided column name into SQL.

Create an allowlist of supported fields.

---

# Part H — Flash Messages

Implement messages for:

### Success

    Student added successfully.

    Student updated successfully.

    Student deleted successfully.

### Errors

    Name is required.

    Invalid email address.

    Marks must be between 0 and 100.

    Student not found.

---

# Part I — Validation

Implement server-side validation for:

### Name

- Required
- Minimum 3 characters
- Maximum 50 characters

### Email

- Required
- Valid expected format
- Unique

### Age

- Required
- Numeric
- Positive
- Appropriate application range

### Course

Must be one of the allowed courses.

### Marks

Must be between:

    0 and 100

---

# Part J — Transaction Handling

Handle database failures.

Workflow:

    Try
      ↓
    Database Operation
      ↓
    Commit
      ↓
    Success

If an appropriate database exception occurs:

    Rollback
      ↓
    Flash Error
      ↓
    Redirect

---

# Part K — Jinja2

Create a student list template.

Display:

- ID
- Name
- Email
- Course
- Marks
- Edit action
- Delete action

Use a loop to display records.

---

# Part L — Search Form

Create:

    <form method="GET">

Include:

- Search input
- Course filter
- Minimum marks
- Maximum marks
- Sort option
- Submit button

Preserve submitted values when rendering the results page.

---

# Part M — Complete Application Flow

Implement:

    Home
      ↓
    Student List
      ↓
    Add Student
      ↓
    Validate
      ↓
    Database
      ↓
    Flash
      ↓
    Redirect
      ↓
    Student List

Also implement:

    Student List
      ↓
    Search / Filter
      ↓
    Database
      ↓
    Results

And:

    Student List
      ↓
    Edit
      ↓
    Validate
      ↓
    Update
      ↓
    Flash
      ↓
    Redirect

---

# ⭐ Final Mini Project Challenge

Build a complete:

# Student Management System

## Required Features

- [ ] Flask application
- [ ] SQLite database
- [ ] SQLAlchemy
- [ ] Student model
- [ ] Add student
- [ ] View students
- [ ] View one student
- [ ] Edit student
- [ ] Delete student
- [ ] Search
- [ ] Course filtering
- [ ] Marks filtering
- [ ] Sorting
- [ ] Form validation
- [ ] Flash messages
- [ ] Redirects
- [ ] Jinja2 templates
- [ ] Error handling
- [ ] Transaction rollback
- [ ] Basic security review

---

# 🧠 Questions

### 1.

Why is SQLAlchemy useful instead of manually constructing SQL strings?

### 2.

Why should validation happen before `db.session.commit()`?

### 3.

Why is GET suitable for search?

### 4.

What is the difference between `request.args` and `request.form`?

### 5.

Why should `db.session.rollback()` be used after a failed transaction?

### 6.

Why should email uniqueness be enforced at the database level as well as checked in application code?

### 7.

Why should sorting fields be restricted to an allowlist?

### 8.

Why should flash messages usually be followed by a redirect after a successful POST?

---

# ✅ Final Checklist

Before completing Day 085, make sure you understand:

- [ ] Flask + SQLite
- [ ] SQLAlchemy
- [ ] Models
- [ ] Tables
- [ ] CRUD
- [ ] Search
- [ ] Filtering
- [ ] Sorting
- [ ] Forms
- [ ] Validation
- [ ] Flash messages
- [ ] Redirects
- [ ] Jinja2
- [ ] Transactions
- [ ] Rollback
- [ ] Database security
- [ ] Complete request-to-database flow

Happy Building! 🚀