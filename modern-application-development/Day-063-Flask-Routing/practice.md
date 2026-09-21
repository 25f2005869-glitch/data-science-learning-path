# 🧪 Day 063 — Flask Routing Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 063  
**Topic:** Flask Routing

---

## 🎯 Practice Goals

Practice:

- Basic routes
- Multiple routes
- View functions
- Dynamic routes
- Route converters
- HTTP methods
- `url_for()`
- 404 errors

---

## 📝 Concept Questions

### Q1. What is routing in Flask?

### Q2. What does `@app.route()` do?

### Q3. What is a view function?

### Q4. What is a dynamic route?

### Q5. What is the purpose of `<int:id>`?

### Q6. What is the difference between `<name>` and `<int:id>`?

### Q7. What is `url_for()`?

### Q8. What is an endpoint?

### Q9. What causes a 404 error?

### Q10. What are GET and POST methods?

---

## 💻 Coding Practice

### Task 1 — Home Route

Create:

    /

Return:

    Welcome to My Flask Website

---

### Task 2 — About Route

Create:

    /about

Return:

    About Me

---

### Task 3 — Skills Route

Create:

    /skills

Return a list of your skills.

---

### Task 4 — Project Route

Create:

    /projects

Return information about your projects.

---

### Task 5 — Dynamic Name Route

Create:

    /hello/<name>

For:

    /hello/Saloni

Return:

    Hello, Saloni!

---

### Task 6 — Integer Route

Create:

    /student/<int:id>

For:

    /student/101

Return:

    Student ID: 101

---

### Task 7 — Marks Route

Create:

    /marks/<int:score>

Display the received score.

---

### Task 8 — Float Route

Create:

    /price/<float:amount>

Display the received price.

---

### Task 9 — Multiple HTTP Methods

Create a route:

    /login

Allow:

    GET
    POST

Return an appropriate message.

---

### Task 10 — `url_for()`

Create routes:

    /
    /about
    /contact

Use `url_for()` to generate URLs for the three view functions.

---

## 🧩 Routing Challenge

Create a student portfolio backend with:

    /
    /about
    /education
    /skills
    /projects
    /student/<int:id>

Each route should have a meaningful response.

---

## 🔍 Debugging Practice

### Problem 1

The browser returns 404.

Find the possible cause.

### Problem 2

This route is defined:

    @app.route("/student/<int:id>")

but the function is:

    def student(student_id):

Identify the problem.

### Problem 3

A POST request is sent to a route that only accepts GET.

What should be changed?

### Problem 4

The wrong endpoint is passed to `url_for()`.

What happens?

---

## 🚀 Mini Challenge

Build a Flask application with:

    /
    /about
    /skills
    /projects
    /student/<int:student_id>
    /course/<course_name>

Requirements:

- Use meaningful view function names
- Use at least one dynamic route
- Use an integer converter
- Use `url_for()`
- Test valid and invalid URLs
- Test the application in the browser

---

## ✅ Self-Check

Before moving to Day 064:

- [ ] I understand Flask routing
- [ ] I can create a basic route
- [ ] I can create multiple routes
- [ ] I understand view functions
- [ ] I can create dynamic routes
- [ ] I understand route converters
- [ ] I understand GET and POST
- [ ] I can use `url_for()`
- [ ] I understand endpoints
- [ ] I understand 404 errors