# 📝 Day 099 — Flask and SQLite Revision Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 099  
**Topic:** Flask and SQLite Revision

---

# Part A — Flask Fundamentals

## Q1. Short Answer

What is Flask?

## Q2. Short Answer

What is the purpose of `@app.route()`?

## Q3. Short Answer

What is the difference between a route and a view function?

## Q4. Practice

Create a Flask route:

    /about

It should return an About page message.

## Q5. Practice

Create a dynamic route:

    /student/<student_id>

Return the student ID.

---

# Part B — Request and Forms

## Q6. Concept

What is the difference between:

- `request.args`
- `request.form`

## Q7. Practice

Create a POST registration form with:

- name
- email
- course

Read the submitted values in Flask.

## Q8. Concept

Why is the `name` attribute important in an HTML form?

## Q9. Concept

Explain Post/Redirect/Get.

---

# Part C — Jinja2

## Q10. Practice

Pass a student name from Flask to a template and display it using Jinja2.

## Q11. Practice

Display a student's result using an `if-else` condition.

## Q12. Practice

Use a Jinja2 loop to display five courses.

## Q13. Concept

What is template inheritance?

## Q14. Practice

Create:

- `base.html`
- `dashboard.html`

Make `dashboard.html` extend `base.html`.

---

# Part D — SQLite

## Q15. SQL Practice

Create a `students` table with:

- id
- name
- email
- course
- marks

Use suitable constraints.

## Q16. SQL Practice

Insert three students.

## Q17. SQL Practice

Select students who scored at least 50 marks.

## Q18. SQL Practice

Update one student's marks.

## Q19. SQL Practice

Delete one student using the student ID.

---

# Part E — SQLAlchemy

## Q20. Concept

What is ORM?

## Q21. Concept

What is the purpose of a SQLAlchemy model?

## Q22. Practice

Create a `Student` model with:

- id
- name
- email
- marks

## Q23. Practice

Write the SQLAlchemy steps to create a student and commit it.

## Q24. Practice

Write the SQLAlchemy operation to retrieve a student by primary key.

## Q25. Practice

Update a student's marks and commit the transaction.

## Q26. Practice

Delete a student.

---

# Part F — Search and Filtering

## Q27. Practice

Create a search form using GET.

Search students by name.

## Q28. Concept

Why is `LIKE` or `ilike()` useful for search?

## Q29. Practice

Filter students whose marks are greater than or equal to 50.

## Q30. Practice

Sort students by marks in descending order.

---

# Part G — Authentication

## Q31. Concept

Differentiate:

- Authentication
- Authorization

## Q32. Concept

Why should passwords be hashed?

## Q33. Practice

Describe the complete login flow.

## Q34. Concept

What is the purpose of Flask's `session`?

## Q35. Practice

Create a protected-route logic where a user must be logged in.

---

# Part H — Validation and Flash Messages

## Q36. Practice

Validate a student registration form for:

- name required
- valid email
- marks between 0 and 100
- course required

## Q37. Concept

Why is server-side validation required even if HTML validation exists?

## Q38. Practice

Show a success flash message after successfully creating a student.

---

# Part I — Error Handling

## Q39. Concept

What is the difference between:

- 400
- 401
- 403
- 404
- 500

## Q40. Practice

Create a custom 404 error handler.

## Q41. Concept

Why should Flask debug mode not be used in production?

---

# Part J — Mini Revision Task

Build a conceptual **Student Management Application** containing:

### Authentication

- Register
- Login
- Logout
- Protected dashboard

### Student Module

- Add student
- View students
- Edit student
- Delete student

### Search

- Search by name
- Filter by course
- Filter by marks
- Sort results

### Database

Use:

- Flask
- SQLAlchemy
- SQLite

### UI

Use:

- Jinja2
- Template inheritance
- Static CSS
- Forms
- Flash messages

### Security

Implement concepts for:

- Password hashing
- Authorization
- CSRF protection
- Server-side validation
- Secure configuration

---

# ✅ Final Self-Assessment

Mark each concept after revision:

- [ ] Flask fundamentals
- [ ] Routing
- [ ] Dynamic routes
- [ ] Request data
- [ ] Forms
- [ ] GET/POST
- [ ] Jinja2
- [ ] Template inheritance
- [ ] Static files
- [ ] Redirects
- [ ] `url_for()`
- [ ] Blueprints
- [ ] Error handling
- [ ] Configuration
- [ ] SQLite
- [ ] SQL
- [ ] SQLAlchemy
- [ ] Database design
- [ ] CRUD
- [ ] Authentication
- [ ] Sessions
- [ ] Cookies
- [ ] Search/filtering
- [ ] Flash messages
- [ ] Validation
- [ ] Testing
- [ ] Security
- [ ] Deployment

---

# ⭐ Final Challenge

Explain this complete flow without looking at your notes:

**Browser → Flask → Route → Validation → SQLAlchemy → SQLite → Jinja2 → Browser**

If you can explain every step clearly, your Flask and SQLite fundamentals are ready for the final MAD 1 revision.