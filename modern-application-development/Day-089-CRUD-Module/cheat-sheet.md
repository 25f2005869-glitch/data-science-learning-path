# ⚡ Day 089 — CRUD Module Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 089  
**Topic:** CRUD Module  

---

## 🔹 CRUD Meaning

    C → Create
    R → Read
    U → Update
    D → Delete

---

## 🔹 Create

    student = Student(
        name="Saloni",
        email="saloni@example.com",
        marks=85
    )

    db.session.add(student)
    db.session.commit()

---

## 🔹 Read All

    students = db.session.execute(
        db.select(Student)
    ).scalars().all()

---

## 🔹 Read One

    student = db.session.get(Student, student_id)

---

## 🔹 Update

    student = db.session.get(Student, student_id)

    student.name = "New Name"
    student.marks = 90

    db.session.commit()

---

## 🔹 Delete

    student = db.session.get(Student, student_id)

    db.session.delete(student)
    db.session.commit()

---

## 🔹 Basic Routes

    GET  /students
    GET  /students/add
    POST /students/add
    GET  /students/<id>
    GET  /students/<id>/edit
    POST /students/<id>/edit
    POST /students/<id>/delete

---

## 🔹 Jinja2 Loop

    {% for student in students %}
        {{ student.name }}
    {% endfor %}

---

## 🔹 URL Generation

    {{ url_for("edit_student", student_id=student.id) }}

---

## 🔹 Flash

    flash("Student added successfully.", "success")

---

## 🔹 Redirect

    return redirect(url_for("students"))

---

## 🔹 Record Not Found

    student = db.session.get(Student, student_id)

    if student is None:
        abort(404)

---

## 🔹 Rollback

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

---

## 🔹 CRUD + HTTP

    Create → POST
    Read   → GET
    Update → POST
    Delete → POST

---

## 🔹 PRG

    POST
      ↓
    Database Operation
      ↓
    Flash
      ↓
    Redirect
      ↓
    GET

---

## 🔹 Validation Checklist

    ✓ Required fields
    ✓ Correct data type
    ✓ Valid ranges
    ✓ Valid email
    ✓ Unique values
    ✓ Record existence

---

## 🔹 Security Checklist

    ✓ Authentication
    ✓ Authorization
    ✓ CSRF protection
    ✓ Input validation
    ✓ ORM/parameterized queries
    ✓ POST for deletion
    ✓ Password hashing
    ✓ Safe error handling

---

## 🔹 CRUD Golden Rule

    Validate → Operate → Commit → Flash → Redirect