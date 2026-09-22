# 📝 Day 075 — Flask Revision and Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 075  
**Topic:** Flask Revision and Practice

---

# 🎯 Practice Objectives

Revise and practice:

- Flask application creation
- Project structure
- Routing
- Dynamic routes
- Jinja2
- Forms
- GET / POST
- Redirects
- `url_for()`
- Blueprints
- Error handling
- Debugging
- Configuration
- Environment variables

---

# 🟢 Level 1 — Concept Revision

### Q1. What is Flask?

### Q2. What is a route?

### Q3. What is a dynamic route?

### Q4. What is the difference between a URL parameter and a query parameter?

### Q5. What is Jinja2?

### Q6. What is the purpose of `render_template()`?

### Q7. What is the difference between GET and POST?

### Q8. What is `request.form`?

### Q9. What is `request.args`?

### Q10. What is the purpose of `url_for()`?

---

# 🟡 Level 2 — Flask Code Practice

### Q11. Create a Flask application with a home route.

The home page should display:

    Welcome to My Flask Application

### Q12. Create an `/about` route.

Display:

- Application name
- Author
- Programme

### Q13. Create a dynamic route:

    /student/<student_name>

Display the student's name.

### Q14. Create a dynamic route:

    /marks/<int:marks>

Display the marks.

If marks are outside 0–100, handle the situation appropriately.

### Q15. Create a `/courses` route.

Pass a list of courses to a Jinja2 template and display them using a loop.

---

# 🟠 Level 3 — Forms

### Q16. Create a student registration form.

Fields:

- Name
- Email
- Course
- Marks
- Submit button

### Q17. Process the form using POST.

Read the submitted values using:

    request.form.get()

### Q18. Validate the marks.

Marks must be between 0 and 100.

### Q19. After successful registration, redirect to a success page.

Use:

    redirect()
    url_for()

### Q20. Explain why PRG is useful after form submission.

---

# 🟠 Level 4 — Jinja2 Practice

### Q21. Display a student's name dynamically.

### Q22. Display a list of courses using a loop.

### Q23. Display:

    Passed

when marks are at least 50.

Otherwise display:

    Failed

### Q24. Create a base template with:

- Header
- Navigation
- Main content
- Footer

Create a child template that extends it.

---

# 🔵 Level 5 — Blueprints

### Q25. Create a student Blueprint.

Use:

    url_prefix="/students"

### Q26. Add these routes:

    /students/profile
    /students/courses

### Q27. Register the Blueprint with the Flask application.

---

# 🔴 Level 6 — Error Handling

### Q28. Create a custom 404 error handler.

### Q29. Create a custom 500 error handler.

### Q30. Use `abort(404)` when a requested student does not exist.

### Q31. Handle a `ZeroDivisionError` using `try-except`.

### Q32. Explain why debug mode should not be enabled in production.

---

# 🟣 Level 7 — Configuration

### Q33. Create a configuration class containing:

- `DEBUG`
- `TESTING`
- `APP_NAME`

### Q34. Load the configuration using `from_object()`.

### Q35. Read `SECRET_KEY` from an environment variable.

### Q36. Write a `.gitignore` that ignores:

    .env
    .venv/
    __pycache__/
    *.pyc

---

# 🚀 Final Master Challenge

## Student Learning Management System

Build a complete Flask application.

### Required Pages

1. Home
2. About
3. Student Profile
4. Courses
5. Course Details
6. Registration
7. Success
8. 404 Error
9. 500 Error

### Required Routes

    /
    /about
    /student
    /courses
    /course/<course_name>
    /register
    /success

### Required Flask Features

- [ ] Flask application
- [ ] Basic routes
- [ ] Dynamic route
- [ ] Jinja2
- [ ] Template inheritance
- [ ] Static files
- [ ] HTML form
- [ ] GET
- [ ] POST
- [ ] `request.form`
- [ ] `request.args`
- [ ] Redirect
- [ ] `url_for()`
- [ ] Blueprint
- [ ] 404 handler
- [ ] 500 handler
- [ ] `abort()`
- [ ] Configuration
- [ ] Environment variable

---

# 🧪 Testing Checklist

### Routing

- [ ] Home route works.
- [ ] About route works.
- [ ] Dynamic route works.
- [ ] Invalid route returns 404.

### Templates

- [ ] Jinja2 variables display correctly.
- [ ] Jinja2 loops work.
- [ ] Jinja2 conditions work.
- [ ] Template inheritance works.

### Forms

- [ ] Form opens.
- [ ] POST request works.
- [ ] Form data is received.
- [ ] Validation works.
- [ ] Redirect works.

### Blueprints

- [ ] Blueprint imports correctly.
- [ ] Blueprint routes work.
- [ ] URL prefix works.

### Errors

- [ ] Custom 404 page works.
- [ ] Custom 500 page works.
- [ ] `abort()` works.
- [ ] Exceptions are handled appropriately.

### Configuration

- [ ] Configuration loads.
- [ ] Environment variable is read.
- [ ] `.env` is ignored by Git.
- [ ] Debug mode is disabled for production.

---

# 🧠 Final Revision Questions

1. What happens when a browser sends a request to Flask?
2. How does Flask select a route?
3. What is a view function?
4. What is a dynamic route?
5. What is a route converter?
6. What is Jinja2?
7. Why use template inheritance?
8. What is the difference between `request.form` and `request.args`?
9. Why is POST commonly used for form submission?
10. What is PRG?
11. What does `url_for()` do?
12. Why are Blueprints useful?
13. What does `abort()` do?
14. How are 404 errors handled?
15. Why is debug mode dangerous in production?
16. What is `app.config`?
17. Why use environment variables?
18. Why should secrets not be committed to Git?

---

# ⭐ Self-Assessment

Give yourself a score from 1–5:

| Skill | Score |
|---|---|
| Flask Basics | /5 |
| Routing | /5 |
| Dynamic Routes | /5 |
| Jinja2 | /5 |
| Forms | /5 |
| GET / POST | /5 |
| Redirects | /5 |
| Blueprints | /5 |
| Error Handling | /5 |
| Configuration | /5 |

---

# ✅ Final Checklist

Before moving to the next section:

- [ ] I can create a Flask application.
- [ ] I can create routes.
- [ ] I understand dynamic routes.
- [ ] I can use Jinja2.
- [ ] I can process forms.
- [ ] I understand GET and POST.
- [ ] I can use redirects and `url_for()`.
- [ ] I understand Blueprints.
- [ ] I can handle common errors.
- [ ] I understand Flask configuration.
- [ ] I understand environment variables.
- [ ] I can explain the complete Flask request flow.