# ⚡ Day 078 — SQLAlchemy Basics Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 078  
**Topic:** SQLAlchemy Basics  

---

## 🔹 Installation

    pip install sqlalchemy

For Flask:

    pip install flask-sqlalchemy

---

## 🔹 Import

    from sqlalchemy import create_engine
    from sqlalchemy import String, select
    from sqlalchemy.orm import DeclarativeBase
    from sqlalchemy.orm import Mapped, mapped_column, Session

---

## 🔹 Engine

    engine = create_engine("sqlite:///students.db")

---

## 🔹 Base Class

    class Base(DeclarativeBase):
        pass

---

## 🔹 Model

    class Student(Base):
        __tablename__ = "students"

        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(100))
        email: Mapped[str] = mapped_column(String(120))

---

## 🔹 Create Tables

    Base.metadata.create_all(engine)

---

## 🔹 Session

    with Session(engine) as session:
        ...

---

## 🔹 Create

    student = Student(
        name="Saloni",
        email="saloni@example.com"
    )

    session.add(student)
    session.commit()

---

## 🔹 Create Multiple

    session.add_all([
        Student(name="Saloni", email="saloni@example.com"),
        Student(name="Rahul", email="rahul@example.com")
    ])

    session.commit()

---

## 🔹 Read All

    statement = select(Student)

    students = session.scalars(statement).all()

---

## 🔹 Read One

    student = session.get(Student, 1)

---

## 🔹 Filter

    statement = select(Student).where(
        Student.name == "Saloni"
    )

    student = session.scalars(statement).first()

---

## 🔹 Update

    student = session.get(Student, 1)

    student.name = "Saloni Tiwari"

    session.commit()

---

## 🔹 Delete

    student = session.get(Student, 1)

    session.delete(student)
    session.commit()

---

## 🔹 Rollback

    session.rollback()

---

## 🔹 Common Data Types

| SQLAlchemy Type | Python Type |
|---|---|
| `Integer` | `int` |
| `String` | `str` |
| `Text` | `str` |
| `Float` | `float` |
| `Boolean` | `bool` |
| `Date` | `date` |
| `DateTime` | `datetime` |

---

## 🔹 Important Methods

| Method | Purpose |
|---|---|
| `create_engine()` | Create database engine |
| `create_all()` | Create tables |
| `add()` | Add one object |
| `add_all()` | Add multiple objects |
| `select()` | Build SELECT query |
| `scalars()` | Get ORM objects |
| `get()` | Find by primary key |
| `commit()` | Save transaction |
| `rollback()` | Cancel uncommitted changes |
| `delete()` | Delete object |

---

## 🔹 ORM Mapping

    Python Class
          ↓
       Model
          ↓
    Database Table
          ↓
       Row/Object

---

## 🔹 CRUD

    CREATE → session.add()
    READ   → select()
    UPDATE → modify object
    DELETE → session.delete()

---

## 🔹 Flask-SQLAlchemy

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

    db = SQLAlchemy(app)

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))

    with app.app_context():
        db.create_all()

---

## ⭐ Remember

    Engine → connects to database
    Model → represents table
    Column → represents field
    Session → manages database work
    Commit → saves changes
    Rollback → cancels uncommitted changes