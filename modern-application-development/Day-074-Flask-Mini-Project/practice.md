# 📝 Day 074 — Flask Mini Project Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 074  
**Topic:** Flask Mini Project

---

# 🎯 Practice Objective

Build a complete Flask mini project by combining the concepts learned from Day 061 to Day 073.

---

# 🟢 Level 1 — Planning

### Q1. What is the purpose of the Student Learning Portal?

### Q2. List five routes that the project should contain.

### Q3. Which routes should use dynamic URL parameters?

### Q4. Which request should be used for student registration: GET or POST?

Explain why.

### Q5. Why should `url_for()` be preferred over manually writing URLs?

---

# 🟡 Level 2 — Flask Implementation

### Q6. Create a Flask application.

Requirements:

- Create the Flask app.
- Add a home route.
- Return a welcome message.

### Q7. Create a dynamic course route.

Example:

    /course/python

The route should display the selected course.

### Q8. Create a student profile route.

Display:

- Name
- Programme
- Current course

### Q9. Create a registration form.

Fields:

- Name
- Email
- Course
- Submit button

Use POST for submission.

---

# 🟠 Level 3 — Jinja2

### Q10. Create a template that displays a student's name dynamically.

### Q11. Create a course list using a Jinja2 loop.

### Q12. Use an `if` condition to display:

    Passed

or:

    Needs Improvement

depending on marks.

### Q13. Create `base.html` and extend it from another template.

---

# 🟠 Level 4 — Flask Features

### Q14. Add a Blueprint for student-related routes.

### Q15. Add a custom 404 error handler.

### Q16. Use `abort(404)` when a requested course does not exist.

### Q17. Add a redirect after successful registration.

### Q18. Use `url_for()` for the success-page URL.

---

# 🔴 Level 5 — Configuration

### Q19. Create a `Config` class.

Include:

- `DEBUG`
- `APP_NAME`
- `SECRET_KEY`

### Q20. Read `SECRET_KEY` from an environment variable.

### Q21. Create a `.gitignore` file that ignores:

- `.env`
- `.venv/`
- `__pycache__/`

---

# 🚀 Final Mini Project Challenge

## Student Learning Portal

Build the complete application.

### Required Pages

1. Home
2. Student Profile
3. Courses
4. Course Details
5. Student Registration
6. Registration Success
7. 404 Error
8. 500 Error

### Required Flask Features

- [ ] Flask application
- [ ] Basic routes
- [ ] Dynamic routes
- [ ] URL parameters
- [ ] Jinja2 templates
- [ ] Template inheritance
- [ ] Forms
- [ ] GET
- [ ] POST
- [ ] Request data
- [ ] Redirects
- [ ] `url_for()`
- [ ] Blueprint
- [ ] Error handling
- [ ] Configuration
- [ ] Environment variable

---

# 🧪 Testing Checklist

Test the following:

- [ ] Home page works.
- [ ] Student page works.
- [ ] Course page works.
- [ ] Dynamic URL works.
- [ ] Registration form opens.
- [ ] Form submission works.
- [ ] Invalid form data is handled.
- [ ] Redirect works.
- [ ] `url_for()` generates correct URLs.
- [ ] Invalid URL shows 404 page.
- [ ] Blueprint routes work.
- [ ] Configuration loads correctly.
- [ ] Environment variable is read correctly.
- [ ] Debug mode is disabled for production.

---

# 🧠 Final Revision Questions

1. How does a browser request reach a Flask route?
2. What is the purpose of `render_template()`?
3. How does Flask read form data?
4. What is the difference between `request.form` and `request.args`?
5. Why use POST for form submission?
6. What is Post/Redirect/Get?
7. What does `url_for()` do?
8. Why are Blueprints useful?
9. How do custom error handlers work?
10. Why should configuration be separated from application code?
11. Why use environment variables?
12. Why should secrets not be committed to Git?

---

# ✅ Project Completion Checklist

Before moving to Day 075:

- [ ] Application structure understood.
- [ ] All major Flask concepts connected.
- [ ] Routes tested.
- [ ] Forms tested.
- [ ] Templates tested.
- [ ] Blueprint tested.
- [ ] Error handling tested.
- [ ] Configuration tested.
- [ ] Environment variables understood.
- [ ] Project runs successfully.