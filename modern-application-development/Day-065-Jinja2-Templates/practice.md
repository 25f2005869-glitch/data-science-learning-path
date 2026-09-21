# 🧪 Day 065 — Jinja2 Templates Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 065  
**Topic:** Jinja2 Templates

---

## 🎯 Practice Goals

Practice:

- `render_template()`
- Variables
- Expressions
- Conditions
- Loops
- Filters
- Dictionaries
- Lists
- Template inheritance

---

## 📝 Concept Questions

### Q1. What is Jinja2?

### Q2. Why are templates used in Flask?

### Q3. What does `render_template()` do?

### Q4. Where are Flask templates normally stored?

### Q5. What does `{{ variable }}` mean?

### Q6. What is the purpose of `{% ... %}`?

### Q7. What is a Jinja2 filter?

### Q8. What is template inheritance?

### Q9. What is the difference between an HTML comment and a Jinja2 comment?

### Q10. How does Flask pass Python data to a template?

---

## 💻 Coding Practice

### Task 1 — First Template

Create:

    templates/index.html

Display:

    Welcome to My Flask Website

Render the template using `render_template()`.

---

### Task 2 — Student Name

Pass a student name from Flask.

Display:

    Welcome, Saloni!

Use:

    {{ name }}

---

### Task 3 — Multiple Variables

Pass:

    name
    course
    score

Display all three values.

---

### Task 4 — Student Dictionary

Create:

    student = {
        "name": "Saloni",
        "course": "MAD1",
        "score": 95
    }

Display the dictionary values in the template.

---

### Task 5 — Grade Condition

Pass a student's score.

Display:

- A+ for 90 or above
- A for 80–89
- B for 70–79
- C for 60–69
- F below 60

Use Jinja2 `if`, `elif`, and `else`.

---

### Task 6 — Course List

Create:

    courses = [
        "DBMS",
        "PDSA",
        "MLF",
        "MAD1"
    ]

Display all courses using a Jinja2 loop.

---

### Task 7 — Loop Index

Display courses as:

    1. DBMS
    2. PDSA
    3. MLF
    4. MAD1

Use `loop.index`.

---

### Task 8 — Filters

Demonstrate:

    upper
    lower
    title
    length
    trim

---

### Task 9 — Multiple Students

Create:

    students = [
        {"name": "Saloni", "score": 95},
        {"name": "Aman", "score": 82},
        {"name": "Riya", "score": 91}
    ]

Display every student's name and score using a loop.

---

## 🧬 Template Inheritance

### Task 10

Create:

    templates/
    ├── base.html
    ├── index.html
    └── about.html

Use `base.html` for common page structure.

Use:

    {% extends "base.html" %}

in the child templates.

---

## 🔗 Dynamic Route + Jinja2

### Task 11

Create:

    /student/<int:student_id>

Pass the student ID to a template.

For:

    /student/101

Display:

    Student ID: 101

---

## 🧩 Mini Challenge

Create a Flask Student Dashboard.

Display:

- Student name
- Student ID
- Programme
- Courses
- Marks
- Grade
- Pass/fail status

Requirements:

- Use Jinja2 variables
- Use a dictionary
- Use a list
- Use a loop
- Use a condition
- Use at least two filters

---

## 🔍 Debugging Practice

### Problem 1

Flask says that the template cannot be found.

Check the folder structure.

### Problem 2

The browser displays:

    {{ name }}

instead of the actual name.

Check whether the variable was passed correctly.

### Problem 3

The `for` loop does not work.

Check for:

    {% endfor %}

### Problem 4

The `if` condition does not work.

Check for:

    {% endif %}

---

## 🚀 Final Challenge

Build a dynamic Student Profile page using:

- Flask
- Jinja2
- Dynamic route
- Variables
- Dictionary
- List
- Conditions
- Loops
- Filters

Example:

    /student/101

The same template should be reusable for different students.

---

## ✅ Self-Check

Before moving to Day 066:

- [ ] I understand Jinja2
- [ ] I understand Flask templates
- [ ] I can use `render_template()`
- [ ] I can pass variables
- [ ] I can use dictionaries
- [ ] I can use conditions
- [ ] I can use loops
- [ ] I can use filters
- [ ] I understand Jinja2 comments
- [ ] I understand template inheritance
- [ ] I can combine dynamic routes with templates