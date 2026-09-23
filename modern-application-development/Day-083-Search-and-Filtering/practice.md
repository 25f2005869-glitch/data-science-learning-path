# 📝 Day 083 — Search and Filtering — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 083  
**Topic:** Search and Filtering

---

## 🎯 Practice Goals

Practice:

- Query parameters
- `request.args`
- SQL `WHERE`
- SQLAlchemy `where()`
- `LIKE` and `ILIKE`
- Multiple conditions
- Sorting
- Search forms
- Safe database queries

---

# Part A — Concept Questions

### 1. What is search?

Write a short definition of search in a web application.

### 2. What is filtering?

Explain filtering with one student-related example.

### 3. What is a query parameter?

Explain the URL:

    /students?search=saloni

Identify the route, parameter name, and value.

### 4. What is `request.args`?

Explain what information Flask provides through `request.args`.

### 5. Why is GET commonly used for search?

Give two reasons.

### 6. What does SQL `WHERE` do?

Write one example.

### 7. What does `LIKE` do?

Explain the meaning of:

    '%python%'

### 8. What is the purpose of `ilike()`?

Explain how it differs from ordinary `like()` behavior.

### 9. What is `order_by()` used for?

Give an example using student marks.

### 10. What is SQL injection?

Explain why directly concatenating user input into SQL is dangerous.

---

# Part B — Code Reading

Consider:

    search = request.args.get("search", "").strip()

Answer:

1. What happens if `search` is not provided?
2. Why is `strip()` useful?
3. What type of value is normally returned?

---

# Part C — SQL Practice

Assume this table:

    students(id, name, course, marks)

### Task 1

Find students whose marks are at least 80.

### Task 2

Find students whose name contains "an".

### Task 3

Find students belonging to Data Science.

### Task 4

Find students with marks between 60 and 90.

### Task 5

Sort students by marks from highest to lowest.

---

# Part D — SQLAlchemy Practice

Assume:

    class Student:
        id
        name
        course
        marks

### Task 1

Write a SQLAlchemy query for:

    marks >= 80

### Task 2

Write a query that searches for a name containing "saloni".

### Task 3

Write a query for:

    course == "Data Science"
    AND marks >= 70

### Task 4

Write a query for students from either:

    Data Science
    Programming

### Task 5

Sort students by marks in descending order.

---

# Part E — Flask Practice

Create a route:

    /students

It should:

1. Read `search` using `request.args`.
2. Remove surrounding whitespace.
3. Create a SQLAlchemy query.
4. Search the student's name.
5. Return matching records.
6. Display a message when no records are found.

---

# Part F — Search Form

Create a GET form containing:

- Search input
- Search button
- Clear link

Example URL after searching:

    /students?search=saloni

---

# Part G — Multiple Filters

Build a student search system supporting:

- Search by name
- Filter by course
- Minimum marks
- Maximum marks
- Sort by marks

Example:

    /students?search=saloni&course=Data%20Science&min_marks=70

---

# Part H — Mini Challenge

Build a Flask + SQLAlchemy student search page.

Requirements:

- Student database
- Search by name
- Search by email
- Course filter
- Minimum marks filter
- Maximum marks filter
- Sort by marks
- GET request
- `request.args`
- SQLAlchemy `where()`
- `ilike()`
- Empty-result message
- Safe query construction

---

# ⭐ Challenge Questions

### 1.

Why should search usually use GET instead of POST?

### 2.

Why should user input not be directly concatenated into SQL?

### 3.

How would you search both `name` and `email` using one keyword?

### 4.

How can search and pagination work together?

### 5.

Why should allowed sorting fields be controlled by the application?

---

# ✅ Self-Check

Before moving to Day 084, make sure you can explain:

- [ ] Search
- [ ] Filtering
- [ ] Query parameters
- [ ] `request.args`
- [ ] SQL `WHERE`
- [ ] `LIKE`
- [ ] `ILIKE`
- [ ] SQLAlchemy `where()`
- [ ] Multiple conditions
- [ ] `and_()`
- [ ] `or_()`
- [ ] `order_by()`
- [ ] GET search forms
- [ ] SQL injection prevention
- [ ] Flask + SQLAlchemy search workflow