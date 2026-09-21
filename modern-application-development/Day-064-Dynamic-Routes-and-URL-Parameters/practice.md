# 🧪 Day 064 — Dynamic Routes and URL Parameters Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 064  
**Topic:** Dynamic Routes and URL Parameters

---

## 🎯 Practice Goals

Practice:

- Dynamic routes
- URL parameters
- Route converters
- Multiple parameters
- `url_for()`
- Dynamic URL design

---

## 📝 Concept Questions

### Q1. What is a dynamic route?

### Q2. What is a URL parameter?

### Q3. What is the difference between a static route and a dynamic route?

### Q4. What does `<int:id>` mean?

### Q5. What does `<float:price>` mean?

### Q6. What is the purpose of the `path` converter?

### Q7. What happens if a non-integer value is supplied to an integer route?

### Q8. Can a Flask route contain multiple parameters?

### Q9. What is `url_for()`?

### Q10. What is the difference between a URL parameter and a query parameter?

---

## 💻 Coding Practice

### Task 1 — Name Route

Create:

    /hello/<name>

For:

    /hello/Saloni

Return:

    Hello, Saloni!

---

### Task 2 — Student ID

Create:

    /student/<int:student_id>

Display the received student ID.

---

### Task 3 — Course Route

Create:

    /course/<course_name>

Display the course name.

---

### Task 4 — Marks Route

Create:

    /marks/<int:marks>

Display the student's marks.

---

### Task 5 — Price Route

Create:

    /price/<float:amount>

Display the price.

---

### Task 6 — Multiple Parameters

Create:

    /student/<int:id>/course/<course>

Display both the student ID and course name.

---

### Task 7 — Project Route

Create:

    /project/<int:project_id>

Display the project ID.

---

### Task 8 — File Path

Create a route using:

    /files/<path:filename>

Test it with a path containing multiple directories.

---

## 🔗 `url_for()` Practice

### Task 9

Create:

    /student/<int:student_id>

Then generate the URL for student 101 using:

    url_for()

---

### Task 10

Create:

    /student/<int:id>/course/<course>

Generate a URL for:

    Student ID: 101
    Course: DBMS

using `url_for()`.

---

## 🔍 Debugging Practice

### Problem 1

Route:

    @app.route("/student/<int:id>")

Function:

    def student(student_id):

Identify the problem.

---

### Problem 2

Route:

    @app.route("/marks/<int:marks>")

Request:

    /marks/abc

Why does the route not match?

---

### Problem 3

The developer writes:

    /student/id

instead of:

    /student/<id>

What is the difference?

---

### Problem 4

A developer manually constructs every Flask URL using string concatenation.

What Flask feature should be preferred?

---

## 🧩 Mini Challenge

Build a dynamic student portal.

Create these routes:

    /
    /student/<int:student_id>
    /student/<int:student_id>/course/<course>
    /student/<int:student_id>/marks/<int:marks>
    /project/<int:project_id>

Requirements:

- Use dynamic routes
- Use integer converters
- Use a string parameter
- Use multiple parameters
- Use `url_for()`
- Test valid URLs
- Test invalid URLs

---

## 🚀 Real-World Challenge

Design dynamic routes for:

- Students
- Courses
- Projects
- Blog posts

Example patterns:

    /student/101
    /course/DBMS
    /project/5
    /post/10

Explain what resource each URL represents.

---

## ✅ Self-Check

Before moving to Day 065:

- [ ] I understand dynamic routes
- [ ] I understand URL parameters
- [ ] I can create string parameters
- [ ] I can create integer parameters
- [ ] I can create float parameters
- [ ] I understand the path converter
- [ ] I can use multiple parameters
- [ ] I can use `url_for()`
- [ ] I understand parameter type conversion
- [ ] I can design meaningful dynamic URLs