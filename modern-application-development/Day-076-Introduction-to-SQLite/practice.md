# 📝 Day 076 — Introduction to SQLite Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 076  
**Topic:** Introduction to SQLite

---

# 🎯 Practice Objectives

Practice:

- Database fundamentals
- SQLite
- SQL
- Tables
- Rows and columns
- Primary keys
- CRUD
- Python `sqlite3`
- SQLite connections
- Parameterized queries
- Flask + SQLite basics

---

# 🟢 Level 1 — Basic Questions

### Q1. What is a database?

### Q2. What is a DBMS?

### Q3. What is a relational database?

### Q4. What is SQLite?

### Q5. Why is SQLite called serverless?

### Q6. Where is an SQLite database commonly stored?

### Q7. What is SQL?

### Q8. What does CRUD stand for?

---

# 🟡 Level 2 — SQL Practice

### Q9. Create a table named `students`.

Columns:

- `id`
- `name`
- `email`
- `course`

Make `id` the primary key.

### Q10. Insert three students.

### Q11. Select all students.

### Q12. Select only student names and courses.

### Q13. Find students enrolled in Python.

### Q14. Update a student's course.

### Q15. Delete a student using their ID.

---

# 🟠 Level 3 — Python SQLite Practice

### Q16. Import the SQLite module.

### Q17. Connect Python to:

    students.db

### Q18. Create a cursor.

### Q19. Create the `students` table using Python.

### Q20. Insert a student using a parameterized query.

### Q21. Retrieve all students using `fetchall()`.

### Q22. Commit the changes.

### Q23. Close the database connection.

---

# 🟠 Level 4 — Query Practice

### Q24. Write a parameterized query to find a student by name.

### Q25. Write a query to find students whose marks are greater than 70.

### Q26. Write a query to update marks using a student ID.

### Q27. Write a query to delete a student using a student ID.

### Q28. Explain why parameterized queries are preferred.

---

# 🔵 Level 5 — Flask + SQLite

### Q29. Create a Flask route:

    /students

The route should connect to SQLite and retrieve all students.

### Q30. Pass the retrieved students to a Jinja2 template.

### Q31. Display the students in an HTML table.

### Q32. Create a route to add a new student.

### Q33. Use POST to submit student data.

### Q34. Redirect to `/students` after successful insertion.

---

# 🔴 Level 6 — Mini Challenge

## Student Database Application

Build a small Flask + SQLite application.

### Database

Create:

    students.db

Table:

    students

Columns:

- `id`
- `name`
- `email`
- `course`
- `marks`

### Required Pages

1. Home
2. Student List
3. Add Student
4. Student Details

### Required Operations

- [ ] Create student
- [ ] Read students
- [ ] Update student
- [ ] Delete student

### Required Flask Concepts

- [ ] Routing
- [ ] Jinja2
- [ ] Forms
- [ ] GET
- [ ] POST
- [ ] Redirect
- [ ] `url_for()`
- [ ] SQLite
- [ ] Parameterized SQL

---

# 🧪 Testing Checklist

### Database

- [ ] Database file is created.
- [ ] Table is created.
- [ ] Primary key works.
- [ ] Student records can be inserted.
- [ ] Records can be selected.
- [ ] Records can be updated.
- [ ] Records can be deleted.

### Flask

- [ ] Student list page works.
- [ ] Add form works.
- [ ] POST request works.
- [ ] Data is stored in SQLite.
- [ ] Redirect works.
- [ ] Jinja2 displays database records.

---

# 🧠 Revision Questions

1. What is SQLite?
2. What is the difference between SQLite and a server-based database?
3. What is a table?
4. What is a row?
5. What is a column?
6. What is a primary key?
7. What is CRUD?
8. What does `sqlite3.connect()` do?
9. What is a cursor?
10. What does `execute()` do?
11. What does `fetchall()` do?
12. Why is `commit()` important?
13. Why should connections be closed?
14. What is a parameterized query?
15. Why should user input not be directly concatenated into SQL?
16. How does Flask communicate with SQLite?

---

# ⭐ Self-Check

Before moving to Day 077, make sure you can:

- [ ] Explain SQLite.
- [ ] Explain relational databases.
- [ ] Create a table.
- [ ] Insert data.
- [ ] Select data.
- [ ] Update data.
- [ ] Delete data.
- [ ] Use Python `sqlite3`.
- [ ] Use parameterized queries.
- [ ] Explain CRUD.
- [ ] Explain Flask + SQLite request flow.