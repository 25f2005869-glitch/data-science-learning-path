# 📝 Day 093 — Project Deployment Basics Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 093  
**Topic:** Project Deployment Basics  

---

# 🎯 Practice Objectives

Practice preparing the Student Management System for deployment.

---

# 🟢 Level 1 — Concepts

### Q1. What is deployment?

### Q2. What is the difference between development and production?

### Q3. Why should Flask debug mode not be used in production?

### Q4. What is WSGI?

### Q5. What is the purpose of `requirements.txt`?

### Q6. Why are environment variables useful?

### Q7. Why should secrets not be committed to Git?

### Q8. Why is HTTPS important?

---

# 🟡 Level 2 — Environment Setup

### Q9

Create a virtual environment.

Use:

    python -m venv .venv

### Q10

Activate the environment on your operating system.

### Q11

Install the application's dependencies.

### Q12

Create a `requirements.txt` file.

---

# 🟠 Level 3 — Configuration

Create environment variables for:

    SECRET_KEY
    DATABASE_URL

Do not place real secrets directly in source code.

Create an appropriate `.gitignore` containing:

    .env
    .venv/
    __pycache__/
    *.pyc

---

# 🔵 Level 4 — Flask Deployment Preparation

Prepare the Student Management System so that it has:

    ✓ Production configuration
    ✓ Debug mode disabled
    ✓ Environment-based SECRET_KEY
    ✓ Database configuration
    ✓ Error pages
    ✓ Health endpoint
    ✓ Logging
    ✓ Requirements file

---

# 🟣 Level 5 — Production Testing

After deployment, test:

### Application

    Home
    Login
    Logout
    Dashboard

### CRUD

    Create
    Read
    Update
    Delete

### Search

    Search
    Filter
    Sort

### Security

    Authentication
    Authorization
    Invalid input
    Protected routes

### UI

    Desktop
    Tablet
    Mobile

---

# 🔴 Level 6 — Deployment Failure Challenge

Suppose the application works locally but gives:

    500 Internal Server Error

Create a debugging checklist.

Check:

    [ ] Production logs
    [ ] Python dependencies
    [ ] Environment variables
    [ ] Database URL
    [ ] Database availability
    [ ] Flask configuration
    [ ] Static files
    [ ] Route configuration
    [ ] Production server
    [ ] File paths

---

# ⭐ Final Project Challenge

Prepare the Student Management System for deployment.

Required structure:

    project/
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes/
    │   ├── templates/
    │   └── static/
    ├── tests/
    ├── requirements.txt
    ├── .gitignore
    └── run.py

Add:

    Authentication
    Dashboard
    CRUD
    Search
    Filtering
    Validation
    Error Handling
    Responsive UI
    Production Configuration

---

# 🚀 Deployment Checklist

    [ ] Application tested
    [ ] Dependencies recorded
    [ ] Environment variables configured
    [ ] Secrets protected
    [ ] Debug mode disabled
    [ ] Database configured
    [ ] Production server configured
    [ ] Static files verified
    [ ] HTTPS configured
    [ ] Error pages verified
    [ ] Logs checked
    [ ] Health endpoint tested
    [ ] Authentication tested
    [ ] Authorization tested
    [ ] CRUD tested
    [ ] Search tested
    [ ] Mobile UI tested

---

# ✅ Definition of Done

The application is deployment-ready when it can be run in a production-like environment without relying on development-only settings or exposed secrets, and its major features have been tested after deployment.