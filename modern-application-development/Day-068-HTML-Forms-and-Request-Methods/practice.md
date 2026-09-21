# 📝 Day 068 — HTML Forms and Request Methods Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 068  
**Topic:** HTML Forms and Request Methods

---

## 🎯 Practice Goals

Practice connecting HTML forms with Flask routes and understand GET and POST request handling.

---

## 🟢 Level 1 — Basic Questions

### Q1. What is an HTML form?

Explain its purpose.

### Q2. What is the purpose of the `action` attribute?

### Q3. What is the purpose of the `method` attribute?

### Q4. What is a GET request?

### Q5. What is a POST request?

### Q6. What is the difference between GET and POST?

### Q7. What is `request.args`?

### Q8. What is `request.form`?

### Q9. What is `request.method`?

### Q10. Why is the `name` attribute important in form inputs?

---

## 🟡 Level 2 — Syntax Practice

### Q11. Create a GET search form.

Requirements:

- Text input
- `name="q"`
- Submit button
- Action `/search`

### Q12. Create a POST registration form.

Requirements:

- Name
- Email
- Password
- Submit button
- Action `/register`

### Q13. Write Flask code to read:

    q

from GET query parameters.

### Q14. Write Flask code to read:

    name

from POST form data.

---

## 🟠 Level 3 — Flask Practice

Create:

    flask-form-practice/
    ├── app.py
    ├── templates/
    │   ├── search.html
    │   └── register.html
    └── static/

Create these routes:

    /
    /search
    /register

Requirements:

1. `/` displays links to Search and Register.
2. Search uses GET.
3. Registration uses POST.
4. Read GET data using `request.args`.
5. Read POST data using `request.form`.
6. Validate required fields.
7. Return meaningful responses.

---

## 🔴 Level 4 — Student Registration

Create a Flask Student Registration form.

Fields:

- Student Name
- Email
- Age
- Course
- Phone
- Submit button

Use:

    method="POST"

The Flask route should:

1. Receive the data.
2. Read the form fields.
3. Validate the data.
4. Display a confirmation response.

---

## ⭐ Challenge — Search + Registration

Build a small Flask application containing:

### Search

Use:

    GET

Allow the user to search for a course.

Example:

    /search?q=Python

Read the query using:

    request.args.get("q")

### Registration

Use:

    POST

Collect:

- Name
- Email
- Course

Read the data using:

    request.form.get(...)

### Additional Requirements

- Use `url_for()`.
- Validate input.
- Use meaningful `name` attributes.
- Use a reusable base template.
- Load CSS from the static directory.
- Redirect after successful registration.

---

## 🧠 Revision Questions

1. What is an HTML form?
2. What does `action` specify?
3. What does `method` specify?
4. When should GET be used?
5. When should POST be used?
6. What is `request.args`?
7. What is `request.form`?
8. What does `request.method` return?
9. Why is `name` important?
10. What happens if a route does not allow the submitted method?
11. Why is server-side validation necessary?
12. What is Post/Redirect/Get?
13. Does POST automatically encrypt data?
14. Why is HTTPS important?

---

## 🧪 Debugging Practice

Try these mistakes intentionally and observe the result:

### Test 1

Remove the `name` attribute from an input.

What happens to the submitted data?

### Test 2

Use:

    request.args.get("name")

for POST form data.

What happens?

### Test 3

Submit POST to a route that only accepts GET.

What HTTP status do you receive?

### Test 4

Remove server-side validation.

Try submitting an empty value.

Why is server-side validation still important?

---

## ✅ Completion Checklist

- [ ] I understand HTML forms.
- [ ] I understand `action`.
- [ ] I understand `method`.
- [ ] I understand GET.
- [ ] I understand POST.
- [ ] I can use `request.args`.
- [ ] I can use `request.form`.
- [ ] I can use `request.method`.
- [ ] I understand the `name` attribute.
- [ ] I can validate submitted data.
- [ ] I understand form submission flow.
- [ ] I can build a Flask form application.