# 🧪 Day 062 — Flask Installation and Project Structure Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 062  
**Topic:** Installing Flask and Project Structure

---

## 🎯 Practice Goals

Practice:

- Python verification
- pip
- virtual environments
- Flask installation
- dependency management
- project structure
- `app.py`
- templates
- static files

---

## 📝 Concept Questions

### Q1. What is pip?

Explain its purpose in Python development.

### Q2. Why do we use a virtual environment?

### Q3. What is the purpose of `.venv`?

### Q4. How do you create a virtual environment?

### Q5. How do you activate a virtual environment on Windows?

### Q6. How do you install Flask?

### Q7. What is `requirements.txt`?

### Q8. Why should `.venv` generally not be committed to Git?

### Q9. What is the purpose of the `templates` folder?

### Q10. What is the purpose of the `static` folder?

### Q11. What is the purpose of `.gitignore`?

### Q12. Why should secrets not be stored directly in source code?

---

## 💻 Coding Practice

### Task 1 — Create a Flask Project

Create:

    flask-project/

Inside it create:

    app.py
    templates/
    static/
    requirements.txt
    .gitignore

---

### Task 2 — Create a Virtual Environment

Create:

    .venv/

Activate it and verify that it is working.

---

### Task 3 — Install Flask

Install Flask inside the virtual environment.

Then verify the installation.

---

### Task 4 — Create `app.py`

Create a Flask application with a root route:

    /

The page should display:

    Welcome to My Flask Application

---

### Task 5 — Add an About Route

Create:

    /about

Return:

    About My Flask Project

---

### Task 6 — Create an HTML Template

Create:

    templates/index.html

Add a heading:

    My Flask Website

For this task, practice organizing the HTML separately from the Python application.

---

### Task 7 — Create Static Folders

Create:

    static/
    ├── css/
    ├── js/
    └── images/

Add placeholder files where appropriate.

---

### Task 8 — Create `.gitignore`

Include common entries such as:

    .venv/
    __pycache__/
    *.pyc
    .env

---

### Task 9 — Generate Requirements

Generate:

    requirements.txt

using:

    python -m pip freeze > requirements.txt

---

## 🧩 Structure Challenge

Build this structure:

    student-flask-app/
    │
    ├── .venv/
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    │
    ├── templates/
    │   ├── index.html
    │   └── about.html
    │
    └── static/
        ├── css/
        │   └── style.css
        ├── js/
        │   └── script.js
        └── images/

---

## 🔍 Troubleshooting Practice

For each problem, write the likely reason and solution.

### Problem 1

`ModuleNotFoundError: No module named 'flask'`

### Problem 2

The virtual environment cannot be activated.

### Problem 3

`requirements.txt` is missing.

### Problem 4

The browser shows `404 Not Found`.

### Problem 5

The application starts but changes are not automatically reflected.

---

## 🚀 Mini Challenge

Create a Flask project called:

    student-portfolio

Requirements:

- Create a virtual environment
- Install Flask
- Create `app.py`
- Create `templates/`
- Create `static/`
- Create `requirements.txt`
- Create `.gitignore`
- Add `/`
- Add `/about`
- Run the application locally

---

## ✅ Self-Check

Before moving to Day 063:

- [ ] Python is installed
- [ ] pip is working
- [ ] Virtual environment can be created
- [ ] Virtual environment can be activated
- [ ] Flask can be installed
- [ ] Flask installation can be verified
- [ ] `app.py` is understood
- [ ] `templates/` is understood
- [ ] `static/` is understood
- [ ] `requirements.txt` is understood
- [ ] `.gitignore` is understood
- [ ] Flask application can be run