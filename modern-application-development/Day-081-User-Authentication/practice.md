# 🧠 Day 081 — User Authentication Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 081  
**Topic:** User Authentication  

---

## 🎯 Practice Goals

Practice:

- Authentication
- Authorization
- Registration
- Login
- Logout
- Password hashing
- Password verification
- Flask sessions
- Protected routes
- Flask-Login
- Authentication security

---

# 🟢 Level 1 — Conceptual Questions

### Q1. What is authentication?

Explain it in your own words.

### Q2. What is authorization?

### Q3. What is the difference between authentication and authorization?

### Q4. Why should passwords not be stored as plain text?

### Q5. What is password hashing?

### Q6. What is the difference between hashing and encryption?

### Q7. What does `generate_password_hash()` do?

### Q8. What does `check_password_hash()` do?

### Q9. Why are sessions useful for authentication?

### Q10. What is a protected route?

---

# 🟡 Level 2 — Syntax Practice

## Q11. Hash a Password

Write Python code that creates a password hash using:

    generate_password_hash()

---

## Q12. Verify a Password

Write code using:

    check_password_hash()

to verify a password.

---

## Q13. Create a User Model

Create a SQLAlchemy User model containing:

- id
- email
- password_hash

Make:

- id → primary key
- email → unique
- email → required
- password_hash → required

---

## Q14. Store User ID in Session

Write the Flask statement that stores a user's ID in the session.

---

## Q15. Read User ID

Write code that retrieves the user ID from the session.

---

## Q16. Logout with Session

Write code that removes the user ID from the Flask session.

---

# 🟠 Level 3 — Authentication Exercises

## Exercise 1 — Registration

Create a Flask registration form with:

- Email
- Password
- Confirm Password

Requirements:

1. Validate the form.
2. Check whether passwords match.
3. Check whether email already exists.
4. Hash the password.
5. Create a User object.
6. Save it to the database.

---

## Exercise 2 — Login

Create a login form with:

- Email
- Password

Requirements:

1. Find the user.
2. Verify the password.
3. Log the user in.
4. Redirect to dashboard.
5. Show an appropriate error for invalid credentials.

---

## Exercise 3 — Protected Dashboard

Create:

    /dashboard

Only logged-in users should access it.

Unauthenticated users should be redirected to:

    /login

---

## Exercise 4 — Logout

Create:

    /logout

The route should:

1. Log the user out.
2. Redirect to the login page.

---

# 🔴 Level 4 — Flask-Login Practice

Install:

    pip install flask-login

Create an application using:

- Flask
- Flask-SQLAlchemy
- SQLite
- Flask-Login

Implement:

- User model
- Registration
- Login
- Logout
- Protected dashboard

Use:

    UserMixin
    LoginManager
    login_user()
    logout_user()
    login_required
    current_user

---

# 🧩 Complete Authentication Challenge

Build a **Student Portal Authentication System**.

## Registration

Fields:

    Name
    Email
    Password
    Confirm Password

## Login

Fields:

    Email
    Password

## Dashboard

Display:

    Welcome, <student name>

## Logout

Provide a logout button.

---

# 🔐 Security Requirements

Your application must:

- [ ] Never store plain-text passwords.
- [ ] Hash passwords.
- [ ] Verify passwords securely.
- [ ] Validate input.
- [ ] Use a secret key.
- [ ] Protect private routes.
- [ ] Avoid exposing sensitive information.
- [ ] Use HTTPS in production.
- [ ] Avoid logging passwords.

---

# 🧠 Scenario Questions

### Scenario 1

A user enters the wrong password.

Should the application:

A. Log them in anyway  
B. Show a successful login  
C. Reject the login  
D. Store the password

Choose the correct answer and explain why.

---

### Scenario 2

A user visits:

    /dashboard

without logging in.

What should happen?

---

### Scenario 3

A database contains:

    email
    password_hash

Why is storing `password_hash` safer than storing the original password?

---

# 🧪 Debugging Practice

Consider:

    user = User.query.filter_by(
        email=email
    ).first()

    if user.password_hash == password:
        login_user(user)

What is wrong with this approach?

Rewrite it using secure password verification.

---

# ⭐ Final Challenge

Build a complete authentication flow:

    Register
       ↓
    Hash Password
       ↓
    Save User
       ↓
    Login
       ↓
    Verify Password
       ↓
    Create Login State
       ↓
    Protected Dashboard
       ↓
    Logout

---

# ✅ Self-Assessment

- [ ] I understand authentication.
- [ ] I understand authorization.
- [ ] I understand password hashing.
- [ ] I can hash a password.
- [ ] I can verify a password.
- [ ] I understand Flask sessions.
- [ ] I can protect a route.
- [ ] I understand Flask-Login.
- [ ] I understand `login_user()`.
- [ ] I understand `logout_user()`.
- [ ] I understand `login_required`.
- [ ] I understand `current_user`.
- [ ] I can design a basic registration flow.
- [ ] I can design a basic login flow.
- [ ] I understand authentication security.

---

# 📌 Revision

Remember:

    Authentication
          ↓
    Verify Identity
          ↓
    Password Hash
          ↓
    Login State
          ↓
    Protected Route
          ↓
    Logout