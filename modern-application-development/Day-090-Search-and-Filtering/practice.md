# 📝 Day 090 — Search and Filtering Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 090  
**Topic:** Search and Filtering  

---

# 🎯 Practice Objectives

Practice implementing search, filtering, sorting, and database queries in a Flask application.

---

# 🟢 Level 1 — Concepts

### Q1. What is search?

### Q2. What is filtering?

### Q3. What is the difference between search and filtering?

### Q4. What are query parameters?

### Q5. Why is GET commonly used for search?

### Q6. What does `request.args` contain?

### Q7. What is the purpose of `ilike()`?

### Q8. What is the difference between ascending and descending sorting?

---

# 🟡 Level 2 — Flask

### Q9. Read a query parameter named `search`.

### Q10. Remove unnecessary spaces from the search value.

### Q11. Create a GET route `/students` that accepts a search parameter.

### Q12. Display the search value again in the HTML input.

---

# 🟠 Level 3 — SQLAlchemy

Assume:

    Student
        id
        name
        email
        course
        marks

### Q13. Find students whose names contain `"Saloni"`.

### Q14. Find students with marks greater than or equal to 80.

### Q15. Find students enrolled in Data Science.

### Q16. Find students with marks >= 80 AND course = Data Science.

### Q17. Find students whose name OR email contains the search keyword.

### Q18. Sort students by marks in ascending order.

### Q19. Sort students by marks in descending order.

---

# 🔵 Level 4 — Search Form

Create a form containing:

    Search
    Course
    Minimum Marks
    Sort

Use:

    method="GET"

Example URL:

    /students?search=saloni&course=Data%20Science&min_marks=70

---

# 🟣 Level 5 — Student Dashboard

Build a searchable student table.

Columns:

    ID
    Name
    Email
    Course
    Marks
    Status
    Actions

Required features:

- Search by name
- Search by email
- Filter by course
- Filter by minimum marks
- Sort by name
- Sort by marks
- Display result count
- Display "No students found" when appropriate

---

# 🔴 Level 6 — Advanced Challenge

Create a combined query.

Requirements:

### Search

Search:

    Name
    Email
    Course

### Filters

    Course
    Minimum Marks

### Sorting

Allow only:

    name
    marks
    course

Do not allow arbitrary database column names from the user.

---

# ⭐ Final Challenge

Integrate search and filtering into the Day 089 CRUD module.

Complete flow:

    Dashboard
       ↓
    Search / Filter
       ↓
    Student Records
       ↓
    View
       ↓
    Edit
       ↓
    Delete

---

# ✅ Definition of Done

    [ ] GET search works
    [ ] request.args works
    [ ] Search works
    [ ] Course filter works
    [ ] Marks filter works
    [ ] Multiple conditions work
    [ ] Sorting works
    [ ] Sort fields are allowlisted
    [ ] Empty results are handled
    [ ] Search values are preserved
    [ ] CRUD actions remain available
    [ ] Input is validated
    [ ] SQLAlchemy queries are used safely
    [ ] Pagination is considered for large datasets