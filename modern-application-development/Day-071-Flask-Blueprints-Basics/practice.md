# 📝 Day 071 — Flask Blueprints Basics Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 071  
**Topic:** Flask Blueprints Basics

---

## 🎯 Practice Goals

Practice creating, organizing, registering, and using Flask Blueprints.

---

## 🟢 Level 1 — Basic Questions

### Q1. What is a Flask Blueprint?

### Q2. Why are Blueprints useful?

### Q3. What is the difference between a Flask application and a Blueprint?

### Q4. Which class is used to create a Blueprint?

### Q5. How do you register a Blueprint?

### Q6. What is `url_prefix`?

### Q7. What is a Blueprint endpoint?

### Q8. Why does a Blueprint need to be registered?

---

## 🟡 Level 2 — Syntax Practice

### Q9. Create a Blueprint called:

    student_bp

### Q10. Add a route:

    /students

to the Blueprint.

### Q11. Register the Blueprint with a Flask application.

### Q12. Create a Blueprint with:

    url_prefix="/students"

### Q13. Create a route:

    /profile

inside that Blueprint.

What will the final URL be?

### Q14. Write the `url_for()` expression for the profile endpoint.

---

## 🟠 Level 3 — Student Blueprint

Create:

    students/
    ├── __init__.py
    └── routes.py

Inside `routes.py`:

1. Create `student_bp`.
2. Add `/`.
3. Add `/profile`.
4. Add `/courses`.
5. Use `url_prefix="/students"`.

Register it in `app.py`.

Expected URLs:

    /students/
    /students/profile
    /students/courses

---

## 🟠 Level 4 — Multiple Blueprints

Create:

    students/
    └── routes.py

    courses/
    └── routes.py

Create:

    student_bp
    course_bp

Student URLs:

    /students/
    /students/profile

Course URLs:

    /courses/
    /courses/python

Register both Blueprints in `app.py`.

---

## 🔴 Level 5 — Student Portal

Build a Flask Student Portal using Blueprints.

Create:

    project/
    ├── app.py
    ├── students/
    │   └── routes.py
    ├── courses/
    │   └── routes.py
    ├── templates/
    └── static/

### Student Blueprint

Routes:

    /students/
    /students/profile
    /students/progress

### Course Blueprint

Routes:

    /courses/
    /courses/python
    /courses/dbms

Requirements:

- Use separate Blueprints.
- Register both Blueprints.
- Use meaningful endpoint names.
- Use `url_for()` for navigation.

---

## ⭐ Challenge

Create three Blueprints:

    student_bp
    course_bp
    auth_bp

Use:

    /students
    /courses
    /auth

as URL prefixes.

Create:

### Student

    /students/
    /students/profile

### Course

    /courses/
    /courses/python

### Authentication

    /auth/login
    /auth/logout

Create a common navigation page using `url_for()`.

---

## 🧪 Debugging Practice

### Test 1

Create a Blueprint but do not register it.

What happens when you try to access its route?

### Test 2

Use:

    @app.route()

inside a Blueprint module.

Explain why using the Blueprint object is usually the correct approach.

### Test 3

Create:

    url_prefix="/students"

and:

    @student_bp.route("/students/profile")

What final URL does this create?

Why might this be undesirable?

### Test 4

Try:

    url_for("profile")

when the route belongs to the `student` Blueprint.

What endpoint should be used?

---

## 🧠 Revision Questions

1. What is a Blueprint?
2. Why do large Flask applications use Blueprints?
3. How do you create a Blueprint?
4. How do you add routes to a Blueprint?
5. How do you register a Blueprint?
6. What is `url_prefix`?
7. What is an endpoint?
8. How are Blueprint endpoints named?
9. How does `url_for()` work with Blueprints?
10. Can an application have multiple Blueprints?
11. Can a Blueprint exist without being registered?
12. Why are Blueprints useful for application organization?

---

## ✅ Completion Checklist

- [ ] I understand Flask Blueprints.
- [ ] I can create a Blueprint.
- [ ] I can add routes to a Blueprint.
- [ ] I can register a Blueprint.
- [ ] I understand URL prefixes.
- [ ] I understand Blueprint endpoints.
- [ ] I can use `url_for()` with Blueprints.
- [ ] I can create multiple Blueprints.
- [ ] I can organize Flask routes into modules.
- [ ] I can build a basic modular Flask application.