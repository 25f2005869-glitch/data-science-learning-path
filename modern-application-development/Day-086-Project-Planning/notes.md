# 📋 Day 086 — Project Planning — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 086  
**Topic:** Project Planning

---

# 1. What Is Project Planning?

Project planning means deciding:

- What to build
- Why to build it
- Who will use it
- What features are required
- What technologies will be used
- How data will be stored
- How the application will be developed
- How the application will be tested

Planning reduces confusion during development.

---

# 2. Project Idea

The first step is selecting a practical problem.

Example:

    Student Management System

The application manages student information and provides CRUD, search, filtering, authentication, and dashboard functionality.

---

# 3. Problem Statement

A problem statement describes the problem that the application will solve.

Example:

    Managing student records manually can make it difficult
    to add, search, update, and organize student information.

The application provides a centralized web-based system for managing student records.

---

# 4. Target Users

Identify who will use the application.

Example:

- Students
- Administrators

Different users may require different permissions.

---

# 5. Requirements

Requirements describe what the application needs to provide.

There are two major categories:

- Functional requirements
- Non-functional requirements

---

# 6. Functional Requirements

Functional requirements describe what the system should do.

Examples:

- Register users
- Login users
- Logout users
- Add students
- View students
- Update students
- Delete students
- Search students
- Filter students
- Validate forms
- Display messages

---

# 7. Non-Functional Requirements

Non-functional requirements describe qualities of the system.

Examples:

- Security
- Performance
- Usability
- Reliability
- Maintainability
- Accessibility
- Responsiveness

Example:

    The application should provide a responsive interface
    that works on desktop and mobile screens.

---

# 8. Features

Features are user-visible capabilities.

Example Student Management System:

    Authentication
    Student Management
    Search
    Filtering
    Dashboard
    Validation
    Flash Messages

---

# 9. Modules

Large applications can be divided into modules.

Example:

    Authentication Module
    Student Module
    Course Module
    Search Module
    Dashboard Module

Modules make development easier to organize.

---

# 10. User Roles

A role determines what a user is allowed to do.

Example:

### Student

Can:

- View own profile
- View courses
- View marks

### Admin

Can:

- Add students
- Update students
- Delete students
- View all students

This introduces authorization.

---

# 11. User Flow

User flow describes the path followed by a user.

Example:

    Login
      ↓
    Dashboard
      ↓
    Student List
      ↓
    Search / Filter
      ↓
    View Student
      ↓
    Edit Student

---

# 12. Application Flow

A Flask application generally follows:

    Browser
       ↓
    Route
       ↓
    View Function
       ↓
    Validation
       ↓
    Business Logic
       ↓
    Database
       ↓
    Template
       ↓
    Browser

---

# 13. Technology Stack

A technology stack is the collection of technologies used to build the application.

For the MAD 1 project:

### Frontend

    HTML
    CSS
    JavaScript

### Backend

    Python
    Flask

### Database

    SQLite

### ORM

    SQLAlchemy

### Template Engine

    Jinja2

---

# 14. Database Planning

Before coding database operations, identify the entities.

Example:

    User
    Student
    Course
    Enrollment

For a simple project, the initial database can start with:

    User
    Student

---

# 15. Student Table

Possible fields:

    id
    name
    email
    age
    course
    marks

---

# 16. User Table

Possible fields:

    id
    username
    email
    password_hash
    role

Passwords should never be stored as plaintext.

---

# 17. Relationships

If students can enroll in multiple courses and courses can contain multiple students, this is a many-to-many relationship.

A junction table can represent the relationship.

Conceptually:

    Student
       ↕
    Enrollment
       ↕
    Course

---

# 18. Route Planning

Plan routes before implementing them.

Example:

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

# 19. GET Routes

GET is generally used for retrieving resources or displaying pages.

Examples:

    GET /students

    GET /students/10

    GET /students/add

---

# 20. POST Routes

POST is commonly used for submitting data or performing state-changing operations.

Examples:

    POST /login

    POST /students/add

    POST /students/10/edit

---

# 21. Search Route

Search can use query parameters.

Example:

    /students?search=saloni

Flask:

    search = request.args.get("search", "").strip()

---

# 22. Filtering

Example:

    /students?course=Data%20Science

Multiple filters can be combined:

    /students?course=Data%20Science&min_marks=70

---

# 23. Authentication Planning

Authentication answers:

    "Who are you?"

Possible flow:

    Register
       ↓
    Login
       ↓
    Verify Password
       ↓
    Create Session
       ↓
    Protected Dashboard

---

# 24. Authorization Planning

Authorization answers:

    "What are you allowed to do?"

Example:

    Student → View own information

    Admin → Manage student records

Authentication and authorization are different concepts.

---

# 25. Form Planning

For every form, identify:

- Fields
- Input types
- Required fields
- Validation rules
- Success message
- Error messages
- Destination after submission

Example:

    Student Registration

    Name → required
    Email → required and valid
    Age → numeric
    Course → allowed value
    Marks → 0–100

---

# 26. Validation Planning

Validation should happen before database operations.

Flow:

    User Input
       ↓
    Normalize
       ↓
    Validate
       ↓
    Valid?
      ↙ ↘
    No   Yes
    ↓      ↓
    Error  Database
    ↓      ↓
    Flash  Commit
           ↓
         Success

---

# 27. Flash Message Planning

Examples:

    Student added successfully.

    Student updated successfully.

    Student deleted successfully.

    Invalid email address.

    Student not found.

Use appropriate message categories.

---

# 28. UI Planning

Before writing HTML and CSS, identify the main pages.

Example:

    Home
    Login
    Register
    Dashboard
    Student List
    Add Student
    Edit Student
    Student Details
    Profile

---

# 29. Navigation Planning

A common navigation structure:

    Home
    Dashboard
    Students
    Profile
    Logout

The visible navigation can depend on the user's authentication state and role.

---

# 30. Project Structure

A scalable Flask project can use:

    project/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes/
    │   ├── templates/
    │   └── static/
    │
    ├── instance/
    │   └── database.db
    │
    ├── tests/
    │
    ├── requirements.txt
    ├── .gitignore
    └── run.py

The exact structure can be simplified for a smaller MAD 1 project.

---

# 31. Development Phases

Break the project into phases.

### Phase 1 — Planning

- Problem statement
- Requirements
- Features
- Database design
- Routes

### Phase 2 — Setup

- Flask
- Virtual environment
- SQLAlchemy
- Project structure

### Phase 3 — Database

- Models
- Tables
- Relationships

### Phase 4 — Authentication

- Registration
- Login
- Logout
- Protected routes

### Phase 5 — CRUD

- Create
- Read
- Update
- Delete

### Phase 6 — Search

- Search
- Filtering
- Sorting

### Phase 7 — UI

- Templates
- CSS
- JavaScript
- Responsive design

### Phase 8 — Validation

- Form validation
- Error handling
- Flash messages

### Phase 9 — Testing

- Functional testing
- Validation testing
- Authentication testing
- Security testing

### Phase 10 — Documentation

- README
- Screenshots
- Features
- Setup instructions
- Database description

---

# 32. MVP

MVP means Minimum Viable Product.

It is the smallest useful version of the project.

For a Student Management System:

    Login
    Student CRUD
    Database
    Search
    Validation

can form the initial MVP.

Additional features can be added after the core system works.

---

# 33. Prioritizing Features

Use three categories:

### Must Have

Features required for the project.

### Should Have

Important but not absolutely required.

### Could Have

Optional enhancements.

Example:

    Must Have:
    CRUD
    Database
    Authentication

    Should Have:
    Search
    Filtering
    Dashboard

    Could Have:
    Advanced analytics
    Export
    Additional themes

---

# 34. Testing Plan

Test:

### Authentication

- Correct login
- Incorrect password
- Logout
- Unauthorized access

### Forms

- Empty values
- Invalid email
- Invalid marks
- Invalid course

### CRUD

- Add
- View
- Edit
- Delete

### Search

- Matching keyword
- No result
- Empty search
- Multiple filters

---

# 35. Security Planning

Important security areas:

- Password hashing
- Authentication
- Authorization
- CSRF protection
- Input validation
- SQL injection prevention
- Secure session configuration
- Secret management
- Output escaping
- Secure error messages

---

# 36. Deployment Planning

Before deployment:

- Disable debug mode.
- Configure production secrets.
- Use a production WSGI server.
- Configure the database appropriately.
- Review security settings.
- Test production configuration.

---

# 37. Documentation Planning

The final README should explain:

- Project name
- Problem statement
- Features
- Technology stack
- Project structure
- Database design
- Installation
- Running instructions
- Routes
- Screenshots
- Testing
- Future improvements

---

# 38. Task Breakdown

Do not treat the project as one huge task.

Break it into smaller tasks.

Example:

    [ ] Create Flask application
    [ ] Configure database
    [ ] Create User model
    [ ] Create Student model
    [ ] Create registration
    [ ] Create login
    [ ] Create student CRUD
    [ ] Add search
    [ ] Add filtering
    [ ] Add validation
    [ ] Add flash messages
    [ ] Build dashboard
    [ ] Test application
    [ ] Write README

---

# 39. Definition of Done

A feature can be considered complete when:

- It works correctly.
- Input is validated.
- Errors are handled.
- Database operations work.
- UI is usable.
- Security considerations are addressed.
- The feature has been tested.
- Documentation is updated.

---

# 40. Final Planning Checklist

Before coding:

- [ ] Problem defined
- [ ] Users identified
- [ ] Requirements written
- [ ] Features selected
- [ ] Modules identified
- [ ] Database designed
- [ ] Routes planned
- [ ] Pages planned
- [ ] Technology stack selected
- [ ] Tasks divided
- [ ] Testing planned
- [ ] Security considered
- [ ] Documentation planned

---

# ⭐ Key Takeaway

Good project planning turns:

    Big Project

into:

    Small Tasks
       ↓
    Modules
       ↓
    Features
       ↓
    Routes
       ↓
    Database
       ↓
    Implementation
       ↓
    Testing
       ↓
    Final Application

Plan first, then implement systematically.