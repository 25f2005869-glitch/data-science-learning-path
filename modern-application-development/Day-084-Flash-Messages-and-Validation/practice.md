# 📝 Day 084 — Flash Messages and Validation — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 084  
**Topic:** Flash Messages and Validation

---

## 🎯 Practice Goals

Practice:

- Flash messages
- Message categories
- Form validation
- Server-side validation
- Client-side validation
- `request.form`
- `redirect()`
- `url_for()`
- Post/Redirect/Get
- Validation before database operations

---

# Part A — Concept Questions

### 1.

What is a flash message?

### 2.

Why are flash messages useful in Flask applications?

### 3.

What does `flash()` do?

### 4.

What does `get_flashed_messages()` do?

### 5.

Why is `SECRET_KEY` important when using Flask's default session-backed flash mechanism?

### 6.

What are message categories?

Give three examples.

### 7.

What is validation?

### 8.

What is the difference between client-side and server-side validation?

### 9.

Why can client-side validation not be trusted as the only validation layer?

### 10.

What is the Post/Redirect/Get pattern?

---

# Part B — Flash Message Practice

Write Flask code to display:

    "Student created successfully."

Use the category:

    success

---

Write another flash message for:

    "Invalid email address."

Use the category:

    error

---

# Part C — Template Practice

Write a Jinja2 block that displays all flash messages together with their categories.

Expected variables:

    category
    message

---

# Part D — Form Validation

Create a registration form with:

- Name
- Email
- Age
- Course
- Password

Validate:

1. Name is required.
2. Name must contain at least 3 characters.
3. Email is required.
4. Age must be a number.
5. Age must be at least 18.
6. Course must belong to an allowed list.
7. Password must have at least 8 characters.

---

# Part E — Flash + Validation

Create a route:

    /register

Requirements:

- Accept GET and POST.
- Read form data.
- Validate the submitted data.
- Flash errors.
- Redirect when validation fails.
- Flash success when registration succeeds.
- Redirect after successful registration.

---

# Part F — Marks Validation

Assume a student submits marks.

Write validation so that:

- Marks cannot be empty.
- Marks must be numeric.
- Marks must be between 0 and 100.

Example invalid input:

    120

Expected result:

    "Marks must be between 0 and 100."

---

# Part G — Course Validation

Allowed courses:

    Data Science
    Programming
    Mathematics

If the user submits another value, display:

    "Invalid course selected."

---

# Part H — Database Practice

Assume a `Student` model.

Create a workflow:

    Form
      ↓
    Validation
      ↓
    Create Student
      ↓
    Commit
      ↓
    Flash Success
      ↓
    Redirect

If the database operation fails:

    rollback()
    flash error
    redirect

---

# Part I — Debugging

Find the problems in this conceptual workflow:

    Receive POST
      ↓
    Save directly to database
      ↓
    Validate after saving
      ↓
    Show success message
      ↓
    Stay on POST page

Write a corrected workflow.

---

# ⭐ Mini Challenge

Build a Flask Student Registration application.

Requirements:

### Form

- Name
- Email
- Age
- Course
- Marks

### Validation

- Name required
- Name length 3–50
- Email required
- Age must be valid
- Age must be at least 18
- Course must be allowed
- Marks must be 0–100

### Flash Messages

Success:

    Student registered successfully.

Errors:

    Please correct the form.
    Invalid course.
    Marks must be between 0 and 100.

### Application Flow

    GET /register
          ↓
    Registration Form
          ↓
    POST /register
          ↓
    Validate
          ↓
    Save
          ↓
    flash()
          ↓
    redirect()
          ↓
    Success Page

---

# 🧠 Challenge Questions

### 1.

Why should validation happen before a database insert?

### 2.

Why should a server validate values from a dropdown even when the HTML contains predefined options?

### 3.

Why is `strip()` useful when processing text input?

### 4.

Why should internal error details not be shown directly to users?

### 5.

How do flash messages and redirects work together?

---

# ✅ Self-Check

Before moving forward, make sure you can explain:

- [ ] `flash()`
- [ ] `get_flashed_messages()`
- [ ] Message categories
- [ ] `SECRET_KEY`
- [ ] Client-side validation
- [ ] Server-side validation
- [ ] Required validation
- [ ] Length validation
- [ ] Numeric validation
- [ ] Range validation
- [ ] Choice validation
- [ ] Business-rule validation
- [ ] `request.form`
- [ ] `redirect()`
- [ ] `url_for()`
- [ ] Post/Redirect/Get
- [ ] Validation before database operations