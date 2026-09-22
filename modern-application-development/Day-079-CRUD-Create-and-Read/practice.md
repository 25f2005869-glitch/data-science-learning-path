# 🧠 Day 079 — CRUD: Create and Read Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 079  
**Topic:** CRUD: Create and Read  

---

## 🎯 Practice Goals

Practice:

- Create operations
- Read operations
- SQLAlchemy models
- Sessions
- `add()`
- `add_all()`
- `commit()`
- `select()`
- `scalars()`
- `all()`
- `first()`
- `one_or_none()`
- `where()`
- `session.get()`

---

# 🟢 Level 1 — Conceptual Questions

### Q1. What does CRUD stand for?

Explain all four operations.

### Q2. What is the Create operation?

### Q3. What is the Read operation?

### Q4. Why is `session.commit()` required?

### Q5. What is the purpose of `session.add()`?

### Q6. What is the difference between `add()` and `add_all()`?

### Q7. What does `select()` do?

### Q8. What is the purpose of `scalars()`?

### Q9. What does `all()` return?

### Q10. What does `first()` return when there are no matching records?

---

# 🟡 Level 2 — Syntax Practice

## Q11. Create a Student object

Create a Student with:

- Name: Saloni
- Email: saloni@example.com
- Age: 17

---

## Q12. Add the Student

Add the object to a SQLAlchemy session.

---

## Q13. Commit the Student

Write the statement that permanently saves the transaction.

---

## Q14. Add Multiple Students

Create and add three Student objects using `add_all()`.

---

## Q15. Read All Students

Write a query that retrieves all Student records.

---

## Q16. Read the First Student

Use `first()`.

---

## Q17. Find a Student by ID

Use:

    session.get(Student, id)

---

## Q18. Search by Name

Retrieve students whose name is:

    Saloni

---

## Q19. Search by Age

Retrieve students whose age is greater than or equal to 18.

---

## Q20. Search by Email

Retrieve the student whose email is:

    saloni@example.com

Use `one_or_none()`.

---

# 🟠 Level 3 — Practical Exercises

## Exercise 1 — Student Database

Create a database:

    students.db

Create a Student model containing:

- id
- name
- email
- age
- course

Insert at least five students.

---

## Exercise 2 — Display Students

Read all students and print:

    ID
    Name
    Email
    Age
    Course

---

## Exercise 3 — Search Students

Write queries to find:

1. Students older than 18
2. Students in Data Science
3. Students named Saloni
4. Student with a particular email

---

## Exercise 4 — First Record

Retrieve only the first Student record.

Handle the case where the table is empty.

---

## Exercise 5 — Primary-Key Search

Search for:

    ID = 3

If the student does not exist, display:

    Student not found

---

# 🔴 Level 4 — Challenge

Create a **Student Registration Database** using SQLAlchemy.

The program should:

1. Create the database.
2. Create the Student table.
3. Insert students.
4. Read all students.
5. Search by name.
6. Search by course.
7. Search by email.
8. Search by ID.

Student fields:

    id
    name
    email
    age
    course

---

# 🌐 Flask Challenge

Create a Flask application using Flask-SQLAlchemy.

Required routes:

    /
    /students
    /students/add

Requirements:

- `/` displays a home page.
- `/students` displays all students.
- `/students/add` provides a form.
- Form submission creates a new student.
- Use SQLite as the database.
- Use SQLAlchemy ORM.
- Use Jinja2 for displaying records.

---

# 🧩 Debugging Practice

Consider:

    student = session.get(Student, 100)

What should your program do if student ID 100 does not exist?

Write code using:

    if student is None:

---

# ✅ Self-Assessment

- [ ] I understand CRUD.
- [ ] I understand Create.
- [ ] I understand Read.
- [ ] I can create model objects.
- [ ] I can use `session.add()`.
- [ ] I can use `session.add_all()`.
- [ ] I understand `commit()`.
- [ ] I can use `select()`.
- [ ] I understand `scalars()`.
- [ ] I can use `all()`.
- [ ] I can use `first()`.
- [ ] I can use `one_or_none()`.
- [ ] I can filter using `where()`.
- [ ] I can find a record using `session.get()`.
- [ ] I can handle a missing record.
- [ ] I understand the Create → Commit → Read workflow.

---

# ⭐ Final Challenge

Without looking at your notes, write a complete program that:

1. Creates a Student model.
2. Creates the SQLite database.
3. Inserts three students.
4. Commits the transaction.
5. Reads all students.
6. Prints their details.
7. Searches for one student by ID.
8. Handles the case where the student does not exist.