# 📝 Day 069 — GET and POST Methods Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 069  
**Topic:** GET and POST Methods

---

## 🎯 Practice Goals

Practice GET and POST requests using HTML forms and Flask routes.

---

## 🟢 Level 1 — Basic Questions

### Q1. What is an HTTP method?

### Q2. What is the GET method?

### Q3. What is the POST method?

### Q4. What is the main difference between GET and POST?

### Q5. What is a query parameter?

### Q6. What is a request body?

### Q7. What is `request.args`?

### Q8. What is `request.form`?

### Q9. What does `request.method` return?

### Q10. Why is the `name` attribute important in HTML forms?

---

## 🟡 Level 2 — Syntax Practice

### Q11. Create a GET search form.

Requirements:

- Action: `/search`
- Method: GET
- Input name: `q`
- Submit button

### Q12. Create a POST registration form.

Requirements:

- Action: `/register`
- Method: POST
- Name field
- Email field
- Submit button

### Q13. Write Flask code to read:

    q

from a GET request.

### Q14. Write Flask code to read:

    name

from a POST request.

### Q15. Write a route that accepts both GET and POST.

---

## 🟠 Level 3 — Flask Practice

Create:

    flask-get-post-practice/
    ├── app.py
    ├── templates/
    │   ├── home.html
    │   ├── search.html
    │   └── register.html
    └── static/
        └── css/
            └── style.css

Create these routes:

    /
    /search
    /register

Requirements:

1. `/` displays links to Search and Register.
2. Search uses GET.
3. Registration uses POST.
4. Use `request.args` for search.
5. Use `request.form` for registration.
6. Validate submitted values.
7. Return meaningful responses.

---

## 🔴 Level 4 — Student Search

Create a student search form.

Fields:

    student_id

Use GET.

Example:

    /student?id=101

Read the value using:

    request.args.get("id")

If the ID is missing, return an appropriate error response.

---

## 🔴 Level 5 — Student Registration

Create a student registration form.

Fields:

- Name
- Email
- Age
- Course

Use:

    method="POST"

The Flask route should:

1. Receive the POST request.
2. Read the submitted fields.
3. Remove unnecessary surrounding whitespace where appropriate.
4. Validate required fields.
5. Return a confirmation response.

---

## ⭐ Challenge — GET + POST Application

Build a small Flask application called:

**Student Portal**

### Home

Route:

    /

Display:

- Student Portal title
- Search link
- Registration link

### Search

Route:

    /search

Method:

    GET

Search for a course.

Example:

    /search?q=Python

### Registration

Route:

    /register

Methods:

    GET
    POST

GET displays the registration form.

POST processes the submitted data.

### Additional Requirements

- Use Jinja2 templates.
- Use template inheritance.
- Use static CSS.
- Use `url_for()`.
- Validate server-side input.
- Use Post/Redirect/Get after successful registration.

---

## 🧪 Debugging Practice

### Test 1

Send POST to a GET-only route.

Observe the HTTP response.

### Test 2

Use `request.form` for a GET query parameter.

Explain why it does not provide the expected value.

### Test 3

Remove the `name` attribute from an input.

Submit the form and inspect the result.

### Test 4

Try submitting an empty registration form.

Add server-side validation.

### Test 5

Try putting a password in a GET query parameter.

Explain why this is a bad design.

---

## 🧠 Revision Questions

1. What is GET?
2. What is POST?
3. When should GET be used?
4. When should POST be used?
5. What is a query parameter?
6. Where is GET data normally visible?
7. Where is POST form data normally sent?
8. What does `request.args` contain?
9. What does `request.form` contain?
10. What does `request.method` contain?
11. What happens when an unsupported method is sent to a Flask route?
12. Why is POST not the same as encryption?
13. Why should HTTPS be used?
14. What is Post/Redirect/Get?
15. Why is server-side validation required?

---

## ✅ Completion Checklist

- [ ] I understand HTTP methods.
- [ ] I understand GET.
- [ ] I understand POST.
- [ ] I can create GET forms.
- [ ] I can create POST forms.
- [ ] I can read `request.args`.
- [ ] I can read `request.form`.
- [ ] I can check `request.method`.
- [ ] I understand query parameters.
- [ ] I understand request body data.
- [ ] I can validate submitted data.
- [ ] I understand Post/Redirect/Get.
- [ ] I can build a Flask GET/POST application.