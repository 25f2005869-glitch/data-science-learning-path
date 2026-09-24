# 📝 Day 086 — Project Planning — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 086  
**Topic:** Project Planning

---

# 🎯 Practice Goal

Create a complete technical plan before starting the final MAD 1 project implementation.

---

# Part A — Project Idea

Choose a web application idea.

Write:

1. Project name
2. Problem statement
3. Target users
4. Main objective

Example:

    Project: Student Management System

---

# Part B — Requirements

Write at least:

### 5 Functional Requirements

Example:

    User can register.
    User can login.

### 5 Non-Functional Requirements

Example:

    Application should be responsive.

---

# Part C — Features

Divide your features into:

### Must Have

Write at least 5.

### Should Have

Write at least 3.

### Could Have

Write at least 3.

---

# Part D — User Roles

Identify the roles in your application.

For each role, write:

- What can the user view?
- What can the user create?
- What can the user update?
- What can the user delete?

---

# Part E — Database Planning

Identify the entities.

For a Student Management System, consider:

    User
    Student
    Course
    Enrollment

For each table, write:

- Primary key
- Important fields
- Constraints
- Relationships

---

# Part F — Route Planning

Design the routes before writing Flask code.

Include routes for:

- Home
- Login
- Register
- Logout
- Dashboard
- Student list
- Add student
- Student details
- Edit student
- Delete student

For every route, identify:

- HTTP method
- URL
- Purpose
- Authentication requirement

---

# Part G — Search and Filtering

Design a student search page.

Support:

- Name search
- Email search
- Course filter
- Minimum marks
- Maximum marks
- Sorting

Example:

    /students?search=saloni&course=Data%20Science

---

# Part H — Form Planning

Create a student form.

Fields:

    Name
    Email
    Age
    Course
    Marks

For every field define:

- Input type
- Required?
- Minimum value
- Maximum value
- Validation rule

---

# Part I — Flash Messages

Plan messages for:

### Success

    Student added successfully.
    Student updated successfully.
    Student deleted successfully.

### Error

    Invalid student information.
    Student not found.
    Unable to complete the operation.

---

# Part J — Page Planning

List all pages required by the project.

Example:

    Home
    Login
    Register
    Dashboard
    Student List
    Student Details
    Add Student
    Edit Student
    Profile

---

# Part K — User Flow

Draw the complete user flow.

Example:

    Home
      ↓
    Login
      ↓
    Dashboard
      ↓
    Student List
      ↓
    Search / Filter
      ↓
    Student Details

---

# Part L — Development Plan

Divide the project into phases.

Example:

    Phase 1 → Setup
    Phase 2 → Database
    Phase 3 → Authentication
    Phase 4 → CRUD
    Phase 5 → Search
    Phase 6 → UI
    Phase 7 → Validation
    Phase 8 → Testing
    Phase 9 → Documentation

---

# Part M — Task Breakdown

Create a checklist of at least 20 small tasks.

Example:

    [ ] Create virtual environment
    [ ] Install Flask
    [ ] Configure application
    [ ] Configure SQLite
    [ ] Create models
    [ ] Create authentication
    [ ] Create CRUD
    [ ] Add search
    [ ] Add filtering

Continue until the entire project is covered.

---

# Part N — Testing Plan

Write test cases for:

### Authentication

- Correct login
- Incorrect password
- Logout
- Unauthorized access

### CRUD

- Create
- Read
- Update
- Delete

### Forms

- Empty fields
- Invalid email
- Invalid age
- Invalid marks
- Invalid course

### Search

- Matching result
- No result
- Empty search
- Multiple filters

---

# Part O — Security Plan

Identify how your project will handle:

- Password hashing
- Authentication
- Authorization
- CSRF
- Input validation
- SQL injection
- Sessions
- Secrets
- Error messages
- Output escaping

---

# ⭐ Final Challenge

Create a complete one-page project specification containing:

1. Project name
2. Problem statement
3. Target users
4. Functional requirements
5. Non-functional requirements
6. Features
7. User roles
8. Database entities
9. Routes
10. Pages
11. User flow
12. Technology stack
13. Development phases
14. Testing strategy
15. Security strategy
16. Future improvements

---

# ✅ Self-Check

Before moving to the next day:

- [ ] I can define a project problem.
- [ ] I can identify target users.
- [ ] I can write requirements.
- [ ] I can separate functional and non-functional requirements.
- [ ] I can identify features and modules.
- [ ] I can design database entities.
- [ ] I can plan Flask routes.
- [ ] I can plan forms.
- [ ] I can plan search and filtering.
- [ ] I can define validation rules.
- [ ] I can plan flash messages.
- [ ] I can divide the project into phases.
- [ ] I can create a testing plan.
- [ ] I can identify basic security requirements.

Happy Planning! 🚀