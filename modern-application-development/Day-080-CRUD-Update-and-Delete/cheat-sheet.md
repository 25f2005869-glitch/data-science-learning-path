# ⚡ Day 080 — CRUD: Update and Delete Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 080  
**Topic:** CRUD: Update and Delete  

---

## 🔹 CRUD

    C → Create
    R → Read
    U → Update
    D → Delete

Day 080:

    U → Update
    D → Delete

---

## 🔹 Update by Primary Key

    student = session.get(Student, 1)

    if student:
        student.name = "Saloni Tiwari"
        session.commit()

---

## 🔹 Update Multiple Fields

    student = session.get(Student, 1)

    if student:
        student.name = "Saloni Tiwari"
        student.age = 18
        student.course = "Data Science"

        session.commit()

---

## 🔹 Update Using a Condition

    statement = select(Student).where(
        Student.email == "saloni@example.com"
    )

    student = session.scalars(
        statement
    ).one_or_none()

    if student:
        student.course = "Data Science"
        session.commit()

---

## 🔹 Delete by Primary Key

    student = session.get(Student, 1)

    if student:
        session.delete(student)
        session.commit()

---

## 🔹 Delete Using a Condition

    statement = select(Student).where(
        Student.email == "old@example.com"
    )

    student = session.scalars(
        statement
    ).one_or_none()

    if student:
        session.delete(student)
        session.commit()

---

## 🔹 Rollback

    try:
        student.name = "New Name"
        session.commit()

    except Exception:
        session.rollback()
        raise

---

## 🔹 Missing Record

    student = session.get(Student, 100)

    if student is None:
        print("Student not found")

---

## 🔹 Update Flow

    Find
      ↓
    Modify
      ↓
    Commit
      ↓
    Database Updated

---

## 🔹 Delete Flow

    Find
      ↓
    session.delete()
      ↓
    Commit
      ↓
    Record Removed

---

## 🔹 Important Methods

| Method | Purpose |
|---|---|
| `get()` | Find by primary key |
| `select()` | Build query |
| `where()` | Filter records |
| `one_or_none()` | Get one or no result |
| `delete()` | Mark object for deletion |
| `commit()` | Save transaction |
| `rollback()` | Cancel uncommitted changes |

---

## 🔹 Complete CRUD

    CREATE → add() → commit()

    READ → select() → scalars()

    UPDATE → modify object → commit()

    DELETE → delete() → commit()

---

## 🔹 Flask-SQLAlchemy

Update:

    student = db.session.get(Student, 1)

    if student:
        student.course = "Data Science"
        db.session.commit()

Delete:

    student = db.session.get(Student, 1)

    if student:
        db.session.delete(student)
        db.session.commit()

---

## ⭐ Remember

    UPDATE = Find + Modify + Commit

    DELETE = Find + Delete + Commit