# 🗄️ Day 085 — Database Integration Project — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 085  
**Topic:** Database Integration Project

---

# 1. Project Overview

The goal is to build a database-driven Student Management System using:

- Flask
- SQLAlchemy
- SQLite
- Jinja2
- HTML
- CSS
- JavaScript

The application stores student information permanently in a database.

---

# 2. Why Database Integration?

Without a database, application data may disappear when the application stops.

A database provides persistent storage.

Example student record:

    ID: 1
    Name: Saloni Tiwari
    Email: saloni@example.com
    Age: 18
    Course: Data Science
    Marks: 92

---

# 3. Project Architecture

A simple architecture is:

    Browser
        ↓
    Flask
        ↓
    SQLAlchemy
        ↓
    SQLite

The browser sends a request.

Flask handles the request.

SQLAlchemy communicates with the database.

SQLite stores the data.

---

# 4. Database Model

A Student model can represent the students table.

Conceptual model:

    Student
    ├── id
    ├── name
    ├── email
    ├── age
    ├── course
    └── marks

Example SQLAlchemy model:

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        age = db.Column(db.Integer, nullable=False)
        course = db.Column(db.String(100), nullable=False)
        marks = db.Column(db.Integer, nullable=False)

---

# 5. Database Configuration

A Flask application needs a database URI.

Example with Flask-SQLAlchemy:

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

The database file stores the SQLite data.

---

# 6. Initializing SQLAlchemy

Example:

    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy()

    db.init_app(app)

The application factory pattern can also initialize the database.

---

# 7. Creating Tables

Tables can be created using:

    with app.app_context():
        db.create_all()

In a real project, database migrations are preferable when the schema needs to evolve safely.

---

# 8. CREATE — Add Student

A new student object can be created:

    student = Student(
        name="Saloni Tiwari",
        email="saloni@example.com",
        age=18,
        course="Data Science",
        marks=92
    )

Then:

    db.session.add(student)
    db.session.commit()

The record is stored in the database.

---

# 9. READ — Display Students

Retrieve records:

    students = db.session.execute(
        db.select(Student)
    ).scalars().all()

The returned students can be passed to a Jinja2 template.

Example:

    return render_template(
        "students.html",
        students=students
    )

---

# 10. READ — Find One Student

Using the primary key:

    student = db.get_or_404(Student, student_id)

This retrieves a student or returns a 404 response if the record does not exist.

---

# 11. UPDATE — Modify Student

First retrieve the student:

    student = db.get_or_404(Student, student_id)

Then update attributes:

    student.name = name
    student.course = course
    student.marks = marks

Commit the transaction:

    db.session.commit()

---

# 12. DELETE — Remove Student

Retrieve the student:

    student = db.get_or_404(Student, student_id)

Delete:

    db.session.delete(student)
    db.session.commit()

The record is removed from the database.

---

# 13. CRUD Summary

    CREATE → Add record
    READ   → Retrieve record
    UPDATE → Modify record
    DELETE → Remove record

---

# 14. Search

Search can use a query parameter.

Example:

    /students?search=saloni

Read it using:

    search = request.args.get("search", "").strip()

Then construct a filtered query.

Example:

    statement = db.select(Student)

    if search:
        statement = statement.where(
            Student.name.ilike(f"%{search}%")
        )

    students = db.session.execute(statement).scalars().all()

---

# 15. Filtering

Example:

    /students?course=Data%20Science

Read the course:

    course = request.args.get("course", "").strip()

Apply the filter:

    if course:
        statement = statement.where(
            Student.course == course
        )

---

# 16. Multiple Filters

The application can combine filters.

Examples:

- Search by name
- Course
- Minimum marks
- Maximum marks

Conceptual URL:

    /students?search=saloni&course=Data%20Science&min_marks=70

---

# 17. Sorting

Example:

    statement = statement.order_by(
        Student.marks.desc()
    )

This returns students with higher marks first.

---

# 18. Form Handling

A POST form can submit student information.

Example:

    @app.route("/students/add", methods=["GET", "POST"])
    def add_student():

        if request.method == "POST":
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()

            # Validate and save data.

        return render_template("add_student.html")

---

# 19. Validation

Before storing data, validate it.

Example:

    if not name:
        flash("Name is required.", "error")
        return redirect(url_for("add_student"))

Marks should also be checked:

    if marks < 0 or marks > 100:
        flash("Marks must be between 0 and 100.", "error")
        return redirect(url_for("add_student"))

---

# 20. Flash Messages

Successful operation:

    flash("Student added successfully.", "success")

Failed operation:

    flash("Unable to add student.", "error")

The template displays these messages using:

    get_flashed_messages()

---

# 21. Post/Redirect/Get

After successful POST processing:

    flash("Student added successfully.", "success")
    return redirect(url_for("students"))

The flow becomes:

    POST
      ↓
    Validate
      ↓
    Database Operation
      ↓
    Flash
      ↓
    Redirect
      ↓
    GET

---

# 22. Transactions

A transaction groups database changes into an operation.

If an operation fails, rollback may be required.

Example:

    try:
        db.session.add(student)
        db.session.commit()
    except Exception:
        db.session.rollback()
        flash("Database operation failed.", "error")

In production applications, catch appropriate database exceptions and log useful diagnostic information securely.

---

# 23. Unique Email

The email field can be unique.

Example:

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

The application should still handle duplicate email attempts gracefully.

---

# 24. Complete Student Lifecycle

    CREATE
       ↓
    READ
       ↓
    SEARCH
       ↓
    FILTER
       ↓
    UPDATE
       ↓
    DELETE

All operations use the same database.

---

# 25. Recommended Routes

A simple application can use:

    GET  /students
    GET  /students/add
    POST /students/add
    GET  /students/<id>
    GET  /students/<id>/edit
    POST /students/<id>/edit
    POST /students/<id>/delete

Using POST for destructive browser form actions can be appropriate when the application is designed around HTML forms.

---

# 26. Jinja2 Student List

Conceptual template:

    {% for student in students %}
        <h3>{{ student.name }}</h3>
        <p>{{ student.course }}</p>
        <p>{{ student.marks }}</p>
    {% endfor %}

Jinja2 receives database records from Flask.

---

# 27. Search Form

Example:

    <form method="GET" action="{{ url_for('students') }}">
        <input
            type="search"
            name="search"
            value="{{ search }}"
        >
        <button type="submit">Search</button>
    </form>

---

# 28. No Results

The application should handle empty results.

Example:

    {% if students %}
        <!-- Display students -->
    {% else %}
        <p>No students found.</p>
    {% endif %}

---

# 29. Security

Important rules:

- Validate all user input.
- Use parameterized database queries or ORM expressions.
- Do not store plaintext passwords.
- Do not expose database credentials.
- Protect sensitive routes with authentication and authorization.
- Use CSRF protection for state-changing browser forms.
- Escape untrusted output.
- Do not reveal internal database errors to users.
- Use secure configuration values.

---

# 30. Project Workflow

### Add Student

    Form
      ↓
    POST
      ↓
    Validate
      ↓
    SQLAlchemy
      ↓
    SQLite
      ↓
    Commit
      ↓
    Flash
      ↓
    Redirect

### Search Student

    Search Form
      ↓
    GET
      ↓
    request.args
      ↓
    SQLAlchemy WHERE
      ↓
    SQLite
      ↓
    Results
      ↓
    Jinja2

### Update Student

    Edit Form
      ↓
    POST
      ↓
    Validate
      ↓
    Update Object
      ↓
    Commit
      ↓
    Flash
      ↓
    Redirect

### Delete Student

    Delete Request
      ↓
    Find Student
      ↓
    Delete
      ↓
    Commit
      ↓
    Flash
      ↓
    Redirect

---

# 31. Project Checklist

- [ ] Flask application configured
- [ ] SQLite database configured
- [ ] SQLAlchemy initialized
- [ ] Student model created
- [ ] Table created
- [ ] Create implemented
- [ ] Read implemented
- [ ] Update implemented
- [ ] Delete implemented
- [ ] Search implemented
- [ ] Filtering implemented
- [ ] Sorting implemented
- [ ] Forms implemented
- [ ] Validation implemented
- [ ] Flash messages implemented
- [ ] Redirects implemented
- [ ] Jinja2 templates connected
- [ ] Error handling added
- [ ] Security reviewed

---

# 32. Key Takeaway

Database integration connects Flask application logic with persistent data.

The complete concept is:

    Flask
      +
    SQLAlchemy
      +
    SQLite
      +
    Forms
      +
    Validation
      +
    CRUD
      +
    Search
      +
    Flash Messages
      =
    Database-Driven Web Application