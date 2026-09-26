# 📚 Day 100 — Master Revision Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 100  
**Topic:** Master Revision and Portfolio Update

# 1. Complete MAD 1 Learning Path

The complete learning path follows:

HTML
    ↓
CSS
    ↓
JavaScript
    ↓
Flask
    ↓
SQLite / SQLAlchemy
    ↓
Full-Stack Application

Each layer has a different responsibility.

HTML provides structure.

CSS provides presentation and layout.

JavaScript provides client-side behavior.

Flask provides backend functionality.

SQLite stores relational data.

SQLAlchemy connects Python application code with the database.

# 2. HTML Master Revision

HTML defines webpage structure.

Important topics:

- HTML5 structure
- Elements
- Attributes
- Headings
- Paragraphs
- Links
- Images
- Lists
- Tables
- Forms
- Input types
- Validation
- Semantic elements
- Audio
- Video
- iFrames
- Accessibility
- Best practices

Important semantic elements:

- header
- nav
- main
- section
- article
- aside
- footer
- figure
- figcaption

# 3. CSS Master Revision

CSS controls the appearance and layout of HTML.

Major concepts:

- Selectors
- Specificity
- Colors
- Backgrounds
- Fonts
- Text styling
- Box model
- Margin
- Padding
- Border
- Width
- Height
- Display
- Position
- Z-index
- Units
- Overflow
- Flexbox
- Grid
- Responsive design
- Media queries
- Transitions
- Animations

Flexbox is mainly useful for one-dimensional layouts.

Grid is mainly useful for two-dimensional layouts.

Media queries allow layouts to respond to screen conditions.

# 4. JavaScript Master Revision

JavaScript adds behavior and interactivity.

Important progression:

Variables
    ↓
Data Types
    ↓
Operators
    ↓
Conditions
    ↓
Loops
    ↓
Functions
    ↓
Arrays
    ↓
Objects
    ↓
Array Methods
    ↓
DOM
    ↓
Events
    ↓
Storage

Important ES6 features:

- let
- const
- Arrow functions
- Template literals
- Default parameters
- Destructuring
- Spread
- Rest
- Optional chaining
- Nullish coalescing
- Classes
- Modules

# 5. DOM Revision

DOM means Document Object Model.

It represents the HTML document as a tree of objects.

Common selection methods:

- `getElementById()`
- `querySelector()`
- `querySelectorAll()`
- `getElementsByClassName()`
- `getElementsByTagName()`

Common manipulation:

- `textContent`
- `innerHTML`
- `style`
- `classList`
- `setAttribute()`
- `removeAttribute()`
- `createElement()`
- `append()`
- `remove()`

# 6. JavaScript Events

Events allow JavaScript to respond to user actions.

Common events:

- click
- input
- change
- submit
- focus
- blur
- keydown
- keyup
- mouseover

Preferred event handling:

`addEventListener()`

Important methods:

- `preventDefault()`
- `stopPropagation()`

# 7. Browser Storage

Local Storage:

- Data generally remains until removed.
- Useful for preferences and persistent client-side data.

Session Storage:

- Data is associated with the current page session.
- Useful for temporary client-side data.

Important methods:

- `setItem()`
- `getItem()`
- `removeItem()`
- `clear()`

Objects and arrays can be converted using:

- `JSON.stringify()`
- `JSON.parse()`

# 8. Flask Revision

Flask is a Python web framework.

Basic application flow:

Browser
    ↓
HTTP Request
    ↓
Flask
    ↓
Route
    ↓
View Function
    ↓
Response
    ↓
Browser

A route connects a URL with a Python function.

Dynamic routes allow values to be passed through URLs.

# 9. Jinja2 Revision

Jinja2 is Flask's template engine.

It allows Python data to be displayed inside HTML.

Important syntax concepts:

- Variables
- Conditions
- Loops
- Filters
- Template inheritance

Template inheritance uses:

- `extends`
- `block`
- `endblock`
- `super()`

# 10. Forms and Request Methods

HTML forms send user data to the server.

GET is mainly used to retrieve data.

POST is mainly used to submit or change data.

Flask commonly reads:

`request.args`

for query parameters.

`request.form`

for submitted form data.

The `name` attribute of a form control is important for server-side form processing.

# 11. Redirects

Flask provides:

`redirect()`

and:

`url_for()`

Using `url_for()` avoids hard-coding route URLs.

A common form workflow is:

GET
    ↓
Form
    ↓
POST
    ↓
Validation
    ↓
Database Operation
    ↓
Redirect
    ↓
GET

This is called Post/Redirect/Get.

# 12. Blueprints

Blueprints help divide a large Flask application into modules.

Example conceptual modules:

- Authentication
- Students
- Courses
- Admin
- Dashboard

Blueprints improve:

- Organization
- Maintainability
- Reusability
- Scalability

# 13. Error Handling

Important HTTP status codes:

- 200 — OK
- 201 — Created
- 301 — Permanent Redirect
- 302 — Temporary Redirect
- 400 — Bad Request
- 401 — Unauthorized
- 403 — Forbidden
- 404 — Not Found
- 405 — Method Not Allowed
- 500 — Internal Server Error

Flask can use:

`abort()`

and:

`@app.errorhandler()`

# 14. Configuration

Configuration contains application settings.

Examples include:

- SECRET_KEY
- Database URI
- Debug configuration
- Testing configuration

Sensitive values should be stored through environment variables.

Never commit secrets to GitHub.

# 15. SQLite Revision

SQLite is a lightweight relational database.

Important characteristics:

- File-based
- Serverless
- Lightweight
- Relational
- SQL support
- Easy local development

Important database concepts:

- Database
- Table
- Row
- Column
- Primary key
- Foreign key
- Constraint
- Relationship

# 16. Database Constraints

Important constraints:

- PRIMARY KEY
- FOREIGN KEY
- NOT NULL
- UNIQUE
- DEFAULT
- CHECK

Constraints improve data integrity.

# 17. SQL Revision

CRUD:

Create
    ↓
Read
    ↓
Update
    ↓
Delete

SQL examples:

INSERT → Create data

SELECT → Read data

UPDATE → Modify data

DELETE → Remove data

Parameterized queries should be used when working with raw SQL.

# 18. SQLAlchemy Revision

SQLAlchemy is a Python SQL toolkit and ORM.

ORM means Object-Relational Mapping.

It allows Python classes and objects to represent database tables and rows.

Common operations:

- Create model
- Add object
- Commit
- Select
- Update
- Delete
- Rollback

# 19. CRUD Revision

Create:

Add a new record.

Read:

Retrieve existing records.

Update:

Modify existing records.

Delete:

Remove records.

Complete student management flow:

Add Student
    ↓
View Student
    ↓
Edit Student
    ↓
Delete Student

# 20. Search and Filtering

Search can use GET query parameters.

Example concept:

`/students?search=Saloni`

Flask reads:

`request.args`

Database filtering can use SQLAlchemy conditions.

Common concepts:

- WHERE
- LIKE
- `ilike()`
- `and_()`
- `or_()`
- `order_by()`
- `asc()`
- `desc()`

# 21. Authentication

Authentication asks:

Who are you?

Authorization asks:

What are you allowed to do?

Typical authentication flow:

Register
    ↓
Validate
    ↓
Hash Password
    ↓
Store User
    ↓
Login
    ↓
Verify Password
    ↓
Create Session
    ↓
Protected Route
    ↓
Logout

Passwords should never be stored as plain text.

# 22. Sessions and Cookies

HTTP is stateless.

Sessions help applications maintain user state across requests.

Cookies are stored by the browser and sent with matching requests.

Important cookie security concepts:

- Secure
- HttpOnly
- SameSite

Flask's default session mechanism uses a signed cookie.

Signed does not mean encrypted.

# 23. Flash Messages

Flash messages provide temporary feedback to users.

Common categories:

- success
- error
- warning
- info

Typical workflow:

POST
    ↓
Validate
    ↓
Database Operation
    ↓
Flash Message
    ↓
Redirect

# 24. Validation

Validation checks whether input is acceptable.

Examples:

- Required fields
- Correct type
- Correct format
- Valid range
- Length
- Uniqueness
- Business rules

Client-side validation improves user experience.

Server-side validation is required for security and data integrity.

# 25. Testing

Important tests:

- Route tests
- GET tests
- POST tests
- Form validation
- CRUD tests
- Authentication tests
- Authorization tests
- Search tests
- Error tests

Testing should include both valid and invalid cases.

# 26. Debugging

Basic debugging process:

1. Reproduce the problem.
2. Read the error message.
3. Inspect the traceback.
4. Find the failing line.
5. Check input values.
6. Check database operations.
7. Fix the root cause.
8. Test again.

Debug mode should not be enabled in production.

# 27. Security

Important practices:

- Password hashing
- HTTPS
- CSRF protection
- Server-side validation
- Authorization
- Safe database queries
- Secure cookies
- Environment variables
- Secure configuration
- No secrets in repositories

# 28. Deployment

Before deployment:

- Install dependencies
- Create requirements.txt
- Configure environment variables
- Disable debug mode
- Configure production server
- Configure database
- Enable HTTPS
- Test application
- Review security
- Configure logging

# 29. Optimization

Optimization areas:

- Database queries
- Indexes
- Pagination
- Static files
- Images
- HTML
- CSS
- JavaScript
- Caching
- Code structure

Optimization should improve both performance and maintainability.

# 30. Portfolio Update

A strong portfolio should clearly answer:

Who are you?

What have you learned?

What can you build?

How did you build it?

Where can someone see your work?

Each project should have:

- Overview
- Problem statement
- Features
- Tech stack
- Project structure
- Database design
- Screenshots
- Installation
- Usage
- Testing
- Security
- Future improvements
- GitHub repository

# 31. Final Full-Stack Architecture

User
    ↓
Frontend
    ↓
HTTP Request
    ↓
Flask
    ↓
Authentication
    ↓
Validation
    ↓
Business Logic
    ↓
SQLAlchemy
    ↓
SQLite
    ↓
Database Result
    ↓
Jinja2
    ↓
HTML Response
    ↓
User

# 32. Final Learning Formula

Learn
    ↓
Practice
    ↓
Build
    ↓
Debug
    ↓
Test
    ↓
Document
    ↓
Deploy
    ↓
Improve

# 🎉 Final Milestone

Day 001 → Day 100 Complete

The 100-day MAD 1 foundation is complete.

The next objective is practical application development rather than only studying concepts.