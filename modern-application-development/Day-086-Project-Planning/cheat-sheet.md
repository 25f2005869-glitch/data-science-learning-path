# 📋 Day 086 — Project Planning — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 086  
**Topic:** Project Planning

---

## 1. Planning Formula

    Problem
      ↓
    Requirements
      ↓
    Features
      ↓
    Modules
      ↓
    Database
      ↓
    Routes
      ↓
    UI
      ↓
    Development
      ↓
    Testing
      ↓
    Deployment

---

## 2. Requirements

### Functional

What the application does.

Examples:

    Login
    CRUD
    Search
    Filtering

### Non-Functional

How the application should behave.

Examples:

    Security
    Performance
    Usability
    Responsiveness

---

## 3. MAD 1 Stack

    HTML
    CSS
    JavaScript
        ↓
    Flask
        ↓
    SQLAlchemy
        ↓
    SQLite

---

## 4. CRUD

    CREATE → Add
    READ   → View
    UPDATE → Edit
    DELETE → Remove

---

## 5. Authentication vs Authorization

**Authentication**

    Who are you?

**Authorization**

    What are you allowed to do?

---

## 6. Student Management System

Possible entities:

    User
    Student
    Course
    Enrollment

---

## 7. Student Fields

    id
    name
    email
    age
    course
    marks

---

## 8. Basic Routes

    GET  /
    GET  /login
    POST /login
    POST /logout

    GET  /students
    GET  /students/add
    POST /students/add

    GET  /students/<id>
    GET  /students/<id>/edit
    POST /students/<id>/edit
    POST /students/<id>/delete

---

## 9. Search

URL:

    /students?search=saloni

Flask:

    request.args.get("search", "")

---

## 10. Validation

    Receive
      ↓
    Validate
      ↓
    Database
      ↓
    Commit
      ↓
    Flash
      ↓
    Redirect

---

## 11. Project Phases

    1. Planning
    2. Setup
    3. Database
    4. Authentication
    5. CRUD
    6. Search
    7. UI
    8. Validation
    9. Testing
    10. Documentation

---

## 12. MVP

Minimum Viable Product:

    Authentication
    +
    Database
    +
    CRUD

Then add:

    Search
    Filtering
    Dashboard
    Other enhancements

---

## 13. Feature Priority

**Must Have**

Required for core application.

**Should Have**

Important improvements.

**Could Have**

Optional enhancements.

---

## 14. Security Checklist

    Password hashing
    Authentication
    Authorization
    CSRF protection
    Input validation
    SQL injection prevention
    Secret management
    Output escaping
    Secure sessions

---

## 15. Testing

Test:

    Authentication
    Forms
    CRUD
    Search
    Filtering
    Authorization
    Error handling

---

## 16. Definition of Done

A feature is complete when:

    Works
    +
    Validated
    +
    Tested
    +
    Secure
    +
    Documented

---

## ⭐ Remember

**Plan → Build → Test → Document**

Do not start a large project by writing code randomly.