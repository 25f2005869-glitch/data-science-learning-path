# 🚀 Day 095 — Final MAD 1 Project Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 095  
**Topic:** Final MAD 1 Project

---

## 🎓 Project

**Student Academic Management System**

---

## 🧱 Technology Stack

    HTML
    CSS
    JavaScript
    Python
    Flask
    Jinja2
    SQLAlchemy
    SQLite

---

## 🌐 Application Flow

    Browser
       ↓
    Flask Route
       ↓
    Business Logic
       ↓
    SQLAlchemy
       ↓
    SQLite
       ↓
    Jinja2
       ↓
    Browser

---

## 🔐 Authentication

    Register
       ↓
    Validate
       ↓
    Hash Password
       ↓
    Save User

    Login
       ↓
    Verify Password
       ↓
    Create Session
       ↓
    Protected Dashboard

---

## 🗄️ CRUD

| Operation | Purpose |
|---|---|
| Create | Add data |
| Read | Retrieve data |
| Update | Modify data |
| Delete | Remove data |

---

## 🔎 Search

    GET
     ↓
    request.args
     ↓
    SQLAlchemy filter
     ↓
    Results

---

## 📝 Forms

Important:

    request.form
    validation
    flash()
    redirect()
    url_for()

---

## 🧩 Jinja2

    {{ variable }}

    {% if condition %}
    {% endif %}

    {% for item in items %}
    {% endfor %}

    {% extends "base.html" %}

    {% block content %}
    {% endblock %}

---

## 🛡️ Security

- Password hashing
- HTTPS
- CSRF protection
- Input validation
- Authorization
- Secure secret key
- Environment variables
- Safe error pages
- No plaintext passwords

---

## 📱 Responsive UI

Use:

    Flexbox
    CSS Grid
    Media Queries
    Responsive Units
    Mobile-first Design

---

## 🧪 Testing

Test:

    Authentication
    CRUD
    Search
    Filtering
    Validation
    Authorization
    Error handling

---

## ⚡ Optimization

    Measure
       ↓
    Find bottleneck
       ↓
    Optimize
       ↓
    Test
       ↓
    Measure again

Focus on:

- Database queries
- Pagination
- Indexes
- Images
- CSS
- JavaScript
- Code duplication

---

## 🚀 Deployment

Before deployment:

    requirements.txt
    Environment variables
    Production configuration
    Debug disabled
    Production server
    HTTPS
    Database configuration
    Security review

---

## ⭐ Final Formula

**Plan → Build → Test → Secure → Optimize → Deploy → Document**