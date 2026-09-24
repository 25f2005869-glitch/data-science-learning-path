# 📚 Day 089 — CRUD Module Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 089  
**Topic:** CRUD Module  

---

## 1. What is CRUD?

CRUD represents four basic database operations:

    C → Create
    R → Read
    U → Update
    D → Delete

Almost every database-driven application uses some form of CRUD.

Examples:

- Student Management System
- Course Management System
- Blog
- Inventory System
- Employee Management System

---

## 2. CRUD Architecture

A typical Flask CRUD flow is:

    Browser
       ↓
    Flask Route
       ↓
    Validation
       ↓
    SQLAlchemy
       ↓
    SQLite Database
       ↓
    Response / Redirect
       ↓
    Jinja2 Template

---

# 3. Create

Create means adding a new record to the database.

Example model:

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        marks = db.Column(db.Integer, nullable=False)

Creating an object:

    student = Student(
        name="Saloni",
        email="saloni@example.com",
        marks=85
    )

Adding it:

    db.session.add(student)
    db.session.commit()

---

## 4. Create Route

A Flask route can process a POST form.

    @app.route("/students/add", methods=["GET", "POST"])
    def add_student():

        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            marks = request.form["marks"]

            student = Student(
                name=name,
                email=email,
                marks=marks
            )

            db.session.add(student)
            db.session.commit()

            flash("Student added successfully.", "success")

            return redirect(url_for("students"))

        return render_template("add_student.html")

---

# 5. Read

Read means retrieving records from the database.

All records:

    students = db.session.execute(
        db.select(Student)
    ).scalars().all()

A single record:

    student = db.session.get(Student, student_id)

---

## 6. Read Route

Example:

    @app.route("/students")
    def students():
        students = db.session.execute(
            db.select(Student)
        ).scalars().all()

        return render_template(
            "students.html",
            students=students
        )

---

## 7. Display Data with Jinja2

Example:

    {% for student in students %}
        <p>{{ student.name }}</p>
        <p>{{ student.email }}</p>
        <p>{{ student.marks }}</p>
    {% endfor %}

Jinja2 converts database data into HTML.

---

# 8. Update

Update means modifying an existing record.

First retrieve the record:

    student = db.session.get(Student, student_id)

Modify its attributes:

    student.name = "New Name"
    student.marks = 90

Save:

    db.session.commit()

---

## 9. Update Route

Example:

    @app.route("/students/<int:student_id>/edit",
               methods=["GET", "POST"])
    def edit_student(student_id):

        student = db.session.get(Student, student_id)

        if student is None:
            abort(404)

        if request.method == "POST":
            student.name = request.form["name"]
            student.email = request.form["email"]
            student.marks = request.form["marks"]

            db.session.commit()

            flash("Student updated successfully.", "success")

            return redirect(url_for("students"))

        return render_template(
            "edit_student.html",
            student=student
        )

---

# 10. Delete

Delete removes an existing record.

Example:

    student = db.session.get(Student, student_id)

    if student:
        db.session.delete(student)
        db.session.commit()

---

## 11. Delete Route

Example:

    @app.route("/students/<int:student_id>/delete",
               methods=["POST"])
    def delete_student(student_id):

        student = db.session.get(Student, student_id)

        if student is None:
            abort(404)

        db.session.delete(student)
        db.session.commit()

        flash("Student deleted successfully.", "success")

        return redirect(url_for("students"))

Delete operations should normally use POST rather than a simple GET link.

---

# 12. Why GET Should Not Delete Data

GET should generally retrieve information.

POST is appropriate for state-changing operations such as:

    Create
    Update
    Delete

Using GET for deletion can cause accidental destructive actions.

---

# 13. CRUD Route Design

A common route design is:

    GET  /students
         → Display students

    GET  /students/add
         → Display create form

    POST /students/add
         → Create student

    GET  /students/<id>
         → Display one student

    GET  /students/<id>/edit
         → Display edit form

    POST /students/<id>/edit
         → Update student

    POST /students/<id>/delete
         → Delete student

---

# 14. Validation

Never assume that form data is valid.

Example:

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    marks = request.form.get("marks", "").strip()

Check:

- Required fields
- Valid email
- Valid numeric value
- Marks range
- Unique email
- Valid record ID

---

# 15. Database Transactions

A database operation should be committed only after validation succeeds.

Example:

    try:
        db.session.add(student)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

`rollback()` restores the transaction state after a failed database operation.

---

# 16. Flash Messages

Flash messages provide feedback to users.

Examples:

    flash("Student created successfully.", "success")

    flash("Student updated successfully.", "success")

    flash("Student deleted successfully.", "success")

    flash("Invalid student data.", "error")

---

# 17. Post/Redirect/Get

After a successful POST operation, redirect to another page.

Flow:

    POST
      ↓
    Database Operation
      ↓
    Flash Message
      ↓
    Redirect
      ↓
    GET

This pattern is called Post/Redirect/Get (PRG).

It helps prevent accidental duplicate form submissions when a user refreshes the resulting page.

---

# 18. CRUD and Jinja2

Jinja2 can create action links.

Example:

    <a href="{{ url_for('edit_student', student_id=student.id) }}">
        Edit
    </a>

For delete, use a form:

    <form
        method="POST"
        action="{{ url_for('delete_student', student_id=student.id) }}"
    >
        <button type="submit">Delete</button>
    </form>

---

# 19. CRUD and Authentication

CRUD operations should be protected when they modify private application data.

Example:

    @login_required
    def add_student():
        ...

But authentication alone may not be enough.

Authorization should also be checked.

Example:

    Admin → Create, Update, Delete

    Student → View own records

---

# 20. Unique Constraints

A database can enforce important rules.

Example:

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

The database should not rely only on frontend validation to enforce uniqueness.

---

# 21. Error Handling

Possible errors include:

- Record not found
- Duplicate email
- Invalid form data
- Database failure
- Unauthorized action

Example:

    student = db.session.get(Student, student_id)

    if student is None:
        abort(404)

---

# 22. CRUD Security

Important practices:

- Authenticate users.
- Authorize operations.
- Validate input.
- Use CSRF protection for state-changing forms.
- Use SQLAlchemy/parameterized queries.
- Never trust hidden form fields.
- Do not expose sensitive data.
- Use POST for destructive operations.
- Confirm important deletions.
- Handle database errors.
- Use secure passwords.

---

# 23. Complete CRUD Lifecycle

The complete lifecycle is:

    CREATE
       ↓
    READ
       ↓
    UPDATE
       ↓
    DELETE

Example:

    Add Student
        ↓
    Display Student
        ↓
    Edit Student
        ↓
    Delete Student

---

# 24. CRUD Module Structure

A larger Flask application may organize CRUD functionality into modules.

Example:

    project/
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes/
    │   │   └── students.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── students.html
    │   │   ├── add_student.html
    │   │   └── edit_student.html
    │   └── static/
    │       └── css/
    └── run.py

This keeps the application maintainable.

---

# 25. Key Takeaway

CRUD is the foundation of database-driven web applications.

In Flask:

    Create → Form + POST + INSERT
    Read   → GET + SELECT
    Update → Form + POST + UPDATE
    Delete → POST + DELETE

A good CRUD module combines:

    Flask
    +
    SQLAlchemy
    +
    SQLite
    +
    Jinja2
    +
    Forms
    +
    Validation
    +
    Authentication
    +
    Authorization
    +
    Security