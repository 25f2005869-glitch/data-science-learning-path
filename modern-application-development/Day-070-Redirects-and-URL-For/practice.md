# 📝 Day 070 — Redirects and `url_for()` Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 070  
**Topic:** Redirects and `url_for()`

---

## 🎯 Practice Goals

Practice Flask redirects, endpoint-based URL generation, dynamic routes, query parameters, and Post/Redirect/Get.

---

## 🟢 Level 1 — Basic Questions

### Q1. What is a redirect?

### Q2. What does Flask's `redirect()` function do?

### Q3. What does `url_for()` do?

### Q4. What is an endpoint?

### Q5. What is the default endpoint name of a Flask view function?

### Q6. Why is `url_for()` preferred over hard-coded internal URLs?

### Q7. What is the difference between `redirect()` and `url_for()`?

### Q8. What is Post/Redirect/Get?

---

## 🟡 Level 2 — Syntax Practice

### Q9. Create a Flask route called `home`.

Then generate its URL using `url_for()`.

### Q10. Redirect from `/old` to the `home` endpoint.

### Q11. Create a route:

    /student/<int:student_id>

Generate the URL for student ID `101`.

### Q12. Create a URL for:

    /search?q=Python

using `url_for()`.

### Q13. Create a redirect that sends the browser to a `success` endpoint.

---

## 🟠 Level 3 — Flask Practice

Create:

    flask-redirect-practice/
    ├── app.py
    ├── templates/
    │   ├── home.html
    │   ├── register.html
    │   └── success.html
    └── static/
        └── css/
            └── style.css

Create these routes:

    /
    /register
    /success

Requirements:

1. Home page links to registration.
2. Registration accepts GET and POST.
3. GET displays the form.
4. POST processes the form.
5. Successful POST redirects to `/success`.
6. Use `url_for()` for the redirect.
7. Use `url_for()` for navigation links.

---

## 🟠 Level 4 — Dynamic Routes

Create:

    /student/<int:student_id>

and:

    /course/<course_name>

Use `url_for()` to generate links to these routes.

Example student:

    101

Example course:

    Python

---

## 🔴 Level 5 — Post/Redirect/Get

Build a student registration application.

Requirements:

### GET

Display the registration form.

### POST

Receive:

- Name
- Email
- Course

Validate the data.

After successful processing:

    POST
      ↓
    Redirect
      ↓
    GET success page

Use:

    redirect(url_for("success"))

---

## ⭐ Challenge

Build a **Student Portal** using:

- Flask
- Jinja2
- Template inheritance
- Static CSS
- HTML forms
- GET
- POST
- Redirects
- `url_for()`

Routes:

    /
    /students
    /student/<int:student_id>
    /search
    /register
    /success

Requirements:

1. Use `base.html`.
2. All navigation links should use `url_for()`.
3. Student links should use dynamic `url_for()`.
4. Search should use GET.
5. Registration should use POST.
6. Successful registration should use PRG.
7. Validate submitted data.
8. Use a static CSS file.
9. Avoid hard-coded internal URLs where `url_for()` can be used.

---

## 🧪 Debugging Practice

### Test 1

Try:

    url_for("/home")

Explain why this is incorrect.

### Test 2

Try generating a dynamic URL without supplying the required parameter.

Observe the error.

### Test 3

Change the route path but keep the endpoint name the same.

Check what `url_for()` generates.

### Test 4

Submit a POST form and return the success page directly.

Then refresh the page.

Compare this with the Post/Redirect/Get pattern.

---

## 🧠 Revision Questions

1. What is `redirect()`?
2. What is `url_for()`?
3. What is an endpoint?
4. How is an endpoint normally named?
5. How do you generate a dynamic route URL?
6. How do you pass query parameters using `url_for()`?
7. Why should internal URLs usually use `url_for()`?
8. What is PRG?
9. Why is PRG useful after form submission?
10. What is a 302 redirect?
11. What is a 303 redirect?
12. Can `url_for()` be used inside Jinja2 templates?
13. Can `url_for()` be used for static files?
14. What happens when a required route parameter is missing?

---

## ✅ Completion Checklist

- [ ] I understand redirects.
- [ ] I can use `redirect()`.
- [ ] I understand endpoints.
- [ ] I can use `url_for()`.
- [ ] I can generate dynamic URLs.
- [ ] I can generate query parameters.
- [ ] I can use `url_for()` in templates.
- [ ] I can redirect after POST.
- [ ] I understand PRG.
- [ ] I can build Flask navigation without hard-coded internal URLs.