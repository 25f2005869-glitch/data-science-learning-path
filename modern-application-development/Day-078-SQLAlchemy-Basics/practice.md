# 🧠 Day 078 — SQLAlchemy Basics Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 078  
**Topic:** SQLAlchemy Basics  

---

## 🎯 Practice Goals

Practice the fundamentals of SQLAlchemy:

- ORM
- Engine
- Models
- Columns
- Primary keys
- Sessions
- CRUD basics
- Transactions
- Flask integration

---

# 🟢 Level 1 — Conceptual Questions

### Q1. What does ORM stand for?

Write the full form and explain it in your own words.

### Q2. What is SQLAlchemy?

Explain its purpose in Python applications.

### Q3. What is an Engine?

Explain the role of the SQLAlchemy Engine.

### Q4. What is a Model?

Explain how a model relates to a database table.

### Q5. What is a primary key?

Why is it important?

### Q6. What is a Session?

Explain why SQLAlchemy uses sessions.

### Q7. What does `commit()` do?

### Q8. What does `rollback()` do?

### Q9. What is the difference between SQLAlchemy and `sqlite3`?

### Q10. What is Flask-SQLAlchemy?

---

# 🟡 Level 2 — Syntax Practice

### Q11. Create a SQLite engine

Create an engine for:

    students.db

### Q12. Create a Base class

Write the SQLAlchemy declarative Base class.

### Q13. Create a Student model

Create a model containing:

- id
- name
- email
- age

Make `id` the primary key.

### Q14. Create the database tables

Write the required statement.

### Q15. Add a student

Create a student object and add it to a session.

### Q16. Add multiple students

Use `add_all()`.

### Q17. Read all students

Use `select()` and `scalars()`.

### Q18. Find a student by ID

Use `session.get()`.

### Q19. Update a student

Change the student's name and commit the change.

### Q20. Delete a student

Delete a student and commit the transaction.

---

# 🟠 Level 3 — Practical Exercises

## Exercise 1 — Student Database

Create a SQLite database called:

    students.db

Create a `Student` model with:

- id
- name
- email
- age
- course

Insert at least five students.

---

## Exercise 2 — Student Search

Write a query to find students whose course is:

    Data Science

---

## Exercise 3 — Student Update

Find a student using their primary key and update their course.

---

## Exercise 4 — Student Delete

Find a student using their primary key and delete the record.

---

## Exercise 5 — Transaction Handling

Perform an insert operation.

Then intentionally create an error before committing.

Use:

    session.rollback()

Explain what happened.

---

# 🔴 Level 4 — Flask Practice

Create a simple Flask application using Flask-SQLAlchemy.

Requirements:

- Flask application
- SQLite database
- Student model
- Home route
- Student creation route
- Student listing route
- Student database table

Suggested structure:

    project/
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   └── students.html
    └── instance/
        └── students.db

---

# 🧩 Challenge

Create a **Student Management Database**.

The application should support:

1. Add student
2. View students
3. Search student
4. Update student
5. Delete student

Student fields:

- ID
- Name
- Email
- Age
- Course

Use:

- Flask
- Flask-SQLAlchemy
- SQLite
- HTML forms
- Jinja2

---

# ✅ Self-Assessment

After completing this day, check:

- [ ] I understand ORM.
- [ ] I understand SQLAlchemy.
- [ ] I can create an Engine.
- [ ] I can create a Model.
- [ ] I can define Columns.
- [ ] I understand Primary Keys.
- [ ] I can create database tables.
- [ ] I understand Sessions.
- [ ] I can add records.
- [ ] I can query records.
- [ ] I can update records.
- [ ] I can delete records.
- [ ] I understand `commit()`.
- [ ] I understand `rollback()`.
- [ ] I understand basic Flask-SQLAlchemy integration.

---

## ⭐ Revision Task

Without looking at the notes, explain this flow:

    Model
      ↓
    Engine
      ↓
    Session
      ↓
    Database
      ↓
    CRUD