# 🧠 Day 080 — CRUD: Update and Delete Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 080  
**Topic:** CRUD: Update and Delete  

---

## 🎯 Practice Goals

Practice:

- Update operations
- Delete operations
- `session.get()`
- `select()`
- `where()`
- Object modification
- `session.delete()`
- `commit()`
- `rollback()`
- Missing-record handling

---

# 🟢 Level 1 — Conceptual Questions

### Q1. What does CRUD stand for?

Explain all four operations.

### Q2. What is an Update operation?

### Q3. What is a Delete operation?

### Q4. Why do we retrieve a record before updating it?

### Q5. What does `session.delete()` do?

### Q6. Why is `commit()` required after an update?

### Q7. Why is `commit()` required after a delete?

### Q8. What happens if `session.get()` cannot find a record?

### Q9. What is the purpose of `rollback()`?

### Q10. What is the difference between Update and Delete?

---

# 🟡 Level 2 — Syntax Practice

## Q11. Update a Name

Find Student ID 1 and change the name to:

    Saloni Tiwari

Commit the change.

---

## Q12. Update Multiple Fields

Find Student ID 2 and change:

    age → 18
    course → Data Science

Commit the changes.

---

## Q13. Update Using Email

Find the student with:

    saloni@example.com

Change their course to:

    Data Science

---

## Q14. Delete a Student

Find Student ID 3 and delete the record.

Commit the transaction.

---

## Q15. Delete Using Email

Find the student with:

    old@example.com

Delete the student.

---

## Q16. Handle Missing Student

Find Student ID 100.

If the student does not exist, display:

    Student not found

---

## Q17. Rollback

Write a try-except block that:

1. Updates a student.
2. Attempts to commit.
3. Rolls back if an exception occurs.

---

# 🟠 Level 3 — Practical Exercises

## Exercise 1 — Student Update

Create a Student database containing:

- id
- name
- email
- age
- course

Insert five students.

Then update at least two records.

---

## Exercise 2 — Course Change

Find all students studying:

    Mathematics

Change their course to:

    Data Science

Commit the transaction.

---

## Exercise 3 — Delete Student

Delete a student using their primary key.

Display:

    Student deleted successfully

if the operation succeeds.

---

## Exercise 4 — Safe Delete

Ask for a student ID.

Before deleting:

1. Find the student.
2. Check whether the student exists.
3. Delete only if found.
4. Commit the transaction.
5. Display an appropriate message.

---

## Exercise 5 — Update by Email

Ask for an email address.

Find the student.

If found:

    update course

If not found:

    Student not found

---

# 🔴 Level 4 — Complete CRUD Challenge

Build a Student Management application supporting:

### Create

Add a student.

### Read

Display all students.

### Update

Update:

- Name
- Email
- Age
- Course

### Delete

Delete a student by ID.

---

# 🌐 Flask Challenge

Create a Flask application using Flask-SQLAlchemy.

Required routes:

    /
    /students
    /students/add
    /students/<int:id>/edit
    /students/<int:id>/delete

Requirements:

- Display students.
- Add students.
- Edit students.
- Delete students.
- Use SQLite.
- Use SQLAlchemy ORM.
- Use Jinja2 templates.
- Validate form data.
- Handle missing student IDs.

---

# 🧩 Debugging Questions

### Problem 1

What is wrong with this code?

    student = session.get(Student, 100)
    student.name = "New Name"

What happens if ID 100 does not exist?

---

### Problem 2

What happens if this is executed without `commit()`?

    student.course = "Data Science"

---

### Problem 3

Why should you be careful with a condition such as:

    Student.age < 18

when deleting multiple records?

---

# 🧠 Scenario Practice

A student changes their email and course.

Write the steps required to update both fields.

Expected flow:

    Find
      ↓
    Modify
      ↓
    Commit

---

# 🧠 Scenario 2

A student leaves the course and must be removed from the database.

Write the correct flow:

    Find
      ↓
    Delete
      ↓
    Commit

---

# ✅ Self-Assessment

- [ ] I understand Update.
- [ ] I understand Delete.
- [ ] I can find a record using `session.get()`.
- [ ] I can modify model attributes.
- [ ] I can update multiple fields.
- [ ] I can use `session.delete()`.
- [ ] I understand `commit()`.
- [ ] I understand `rollback()`.
- [ ] I can handle missing records.
- [ ] I can update using a condition.
- [ ] I can delete using a condition.
- [ ] I understand the complete CRUD lifecycle.

---

# ⭐ Final Challenge

Without looking at your notes, write a SQLAlchemy program that:

1. Creates a Student model.
2. Inserts three students.
3. Reads all students.
4. Updates one student.
5. Deletes another student.
6. Commits each successful transaction.
7. Handles a missing student.
8. Uses rollback for transaction errors.

Final CRUD flow:

    CREATE
       ↓
    READ
       ↓
    UPDATE
       ↓
    DELETE