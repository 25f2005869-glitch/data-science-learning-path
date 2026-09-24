# 🗄️ Day 085 — Database Integration Project — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 085  
**Topic:** Database Integration Project

---

## 1. Stack

    Flask
      ↓
    SQLAlchemy
      ↓
    SQLite

---

## 2. Database URI

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

---

## 3. Initialize

    db = SQLAlchemy()

    db.init_app(app)

---

## 4. Model

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        age = db.Column(db.Integer, nullable=False)
        course = db.Column(db.String(100), nullable=False)
        marks = db.Column(db.Integer, nullable=False)

---

## 5. Create

    student = Student(
        name=name,
        email=email,
        age=age,
        course=course,
        marks=marks
    )

    db.session.add(student)
    db.session.commit()

---

## 6. Read All

    students = db.session.execute(
        db.select(Student)
    ).scalars().all()

---

## 7. Read One

    student = db.get_or_404(Student, student_id)

---

## 8. Update

    student.name = name
    student.marks = marks

    db.session.commit()

---

## 9. Delete

    db.session.delete(student)
    db.session.commit()

---

## 10. Search

    search = request.args.get("search", "").strip()

    statement = db.select(Student)

    if search:
        statement = statement.where(
            Student.name.ilike(f"%{search}%")
        )

---

## 11. Filter

    statement = statement.where(
        Student.course == course
    )

---

## 12. Marks Filter

    statement = statement.where(
        Student.marks >= 80
    )

---

## 13. Sorting

    statement = statement.order_by(
        Student.marks.desc()
    )

---

## 14. Execute Query

    students = db.session.execute(
        statement
    ).scalars().all()

---

## 15. Form Data

    name = request.form.get("name", "").strip()

---

## 16. Query Data

    search = request.args.get("search", "").strip()

---

## 17. Validation

    if not name:
        flash("Name is required.", "error")

---

## 18. Flash

    flash("Student added successfully.", "success")

---

## 19. Redirect

    return redirect(url_for("students"))

---

## 20. Transaction

    try:
        db.session.add(student)
        db.session.commit()
    except Exception:
        db.session.rollback()

---

## 21. CRUD

    CREATE → Add
    READ   → Retrieve
    UPDATE → Modify
    DELETE → Remove

---

## 22. Search Flow

    GET
      ↓
    request.args
      ↓
    where()
      ↓
    Database
      ↓
    Results

---

## 23. Form Flow

    POST
      ↓
    request.form
      ↓
    Validate
      ↓
    Database
      ↓
    flash()
      ↓
    redirect()
      ↓
    GET

---

## 24. Jinja2

    {% for student in students %}
        {{ student.name }}
        {{ student.course }}
        {{ student.marks }}
    {% endfor %}

---

## 25. No Results

    {% if students %}
        <!-- results -->
    {% else %}
        <p>No students found.</p>
    {% endif %}

---

## 26. Important Security Rules

- Never trust user input.
- Validate on the server.
- Use ORM expressions or parameterized SQL.
- Never store plaintext passwords.
- Protect state-changing forms against CSRF.
- Do not expose secrets.
- Do not show internal database errors to users.

---

## ⭐ Final Formula

    Flask
    + SQLAlchemy
    + SQLite
    + CRUD
    + Search
    + Filtering
    + Validation
    + Flash Messages
    + Jinja2
    = Database-Driven Flask Application