# 📝 Day 087 — Authentication System — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 087  
**Topic:** Authentication System

---

# 🎯 Practice Goals

Practice:

- Authentication
- Authorization
- Registration
- Password hashing
- Password verification
- Sessions
- Protected routes
- Flask-Login
- Role-based access
- Authentication security

---

# Part A — Concept Questions

### 1.

What is authentication?

### 2.

What is authorization?

### 3.

What is the difference between authentication and authorization?

### 4.

Why should passwords never be stored as plaintext?

### 5.

What is password hashing?

### 6.

What is the purpose of `generate_password_hash()`?

### 7.

What is the purpose of `check_password_hash()`?

### 8.

Why is Flask `SECRET_KEY` important?

### 9.

What is a session?

### 10.

What is a protected route?

---

# Part B — Password Hashing

Write Python code that:

1. Receives a password.
2. Generates a password hash.
3. Verifies the original password against the hash.
4. Verifies an incorrect password.

Do not print or store the plaintext password in a real application.

---

# Part C — User Model

Create a SQLAlchemy `User` model with:

- `id`
- `username`
- `email`
- `password_hash`
- `role`

Requirements:

- `id` is the primary key.
- Username is unique.
- Email is unique.
- Password is stored as a hash.
- Role has a default value.

---

# Part D — Registration

Design a registration route.

Requirements:

    GET  /register
    POST /register

The route should:

1. Display the form.
2. Receive form data.
3. Validate the data.
4. Check username/email uniqueness.
5. Hash the password.
6. Create the user.
7. Commit the transaction.
8. Flash success.
9. Redirect to login.

---

# Part E — Login

Design:

    GET  /login
    POST /login

The login should:

1. Receive email and password.
2. Find the user.
3. Verify the password hash.
4. Create an authenticated session.
5. Flash success.
6. Redirect to dashboard.

Invalid credentials should produce a generic message.

---

# Part F — Logout

Implement:

    POST /logout

The operation should:

1. End the authenticated session.
2. Flash a message.
3. Redirect to login or home.

---

# Part G — Protected Route

Create:

    /dashboard

Only authenticated users should be able to access it.

Unauthenticated users should be redirected to login.

---

# Part H — Role-Based Authorization

Create two roles:

    student
    admin

Rules:

### Student

Can:

- View dashboard
- View own profile

### Admin

Can:

- View dashboard
- View students
- Add students
- Edit students
- Delete students

Create a server-side authorization check for admin-only operations.

---

# Part I — Flask-Login

Repeat the authentication implementation using Flask-Login.

Practice:

    LoginManager
    UserMixin
    user_loader
    login_user()
    logout_user()
    login_required
    current_user

---

# Part J — Authentication Security

Write how your application will protect against:

1. Plaintext password storage
2. Weak secret keys
3. CSRF
4. Session attacks
5. User enumeration
6. Brute-force login attempts
7. Unauthorized access
8. SQL injection

---

# Part K — Debugging

Identify the problem:

    user.password = password

Why is this unsafe?

Write the corrected concept.

---

# Part L — Authentication Flow

Complete this flow:

    Register
       ↓
    ________
       ↓
    Store User
       ↓
    Login
       ↓
    ________
       ↓
    Create Session
       ↓
    Protected Route
       ↓
    ________
       ↓
    Logout

---

# Part M — Database + Authentication

Build the following flow:

    Registration Form
          ↓
    Validation
          ↓
    Password Hashing
          ↓
    User Table
          ↓
    Login
          ↓
    Password Verification
          ↓
    Session
          ↓
    Dashboard

---

# ⭐ Final Mini Challenge

Build an authentication module for the MAD 1 Student Management System.

## Required Features

### Registration

- [ ] Username
- [ ] Email
- [ ] Password
- [ ] Password confirmation
- [ ] Server-side validation
- [ ] Unique email
- [ ] Password hashing

### Login

- [ ] Email
- [ ] Password
- [ ] Password verification
- [ ] Generic authentication error
- [ ] Session creation

### Logout

- [ ] End session
- [ ] Redirect
- [ ] Flash message

### Authorization

- [ ] Student role
- [ ] Admin role
- [ ] Protected routes
- [ ] Admin-only operations

### Security

- [ ] Strong secret key
- [ ] Password hashing
- [ ] CSRF protection
- [ ] HTTPS in production
- [ ] Server-side validation
- [ ] No password logging

---

# 🧠 Challenge Questions

### 1.

Why is hashing appropriate for passwords?

### 2.

Why should the application use a generic "Invalid email or password" message?

### 3.

What happens if an attacker modifies a client-side role value from `student` to `admin`?

### 4.

Why must authorization be checked on the server?

### 5.

What is the difference between a session and authentication?

### 6.

Why should authentication and authorization be treated as separate concepts?

---

# ✅ Self-Check

Before moving forward:

- [ ] I understand authentication.
- [ ] I understand authorization.
- [ ] I can hash passwords.
- [ ] I can verify password hashes.
- [ ] I understand Flask sessions.
- [ ] I understand `SECRET_KEY`.
- [ ] I can design registration.
- [ ] I can design login.
- [ ] I can implement logout.
- [ ] I can protect routes.
- [ ] I understand Flask-Login.
- [ ] I understand roles.
- [ ] I understand server-side authorization.
- [ ] I know basic authentication security practices.

Happy Learning! 🔐