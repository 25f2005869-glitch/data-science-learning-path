# ⚡ Day 079 — CRUD: Create and Read Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 079  
**Topic:** CRUD: Create and Read  

---

## 🔹 CRUD

    C → Create
    R → Read
    U → Update
    D → Delete

Day 079:

    CREATE + READ

---

## 🔹 Create a Model Object

    student = Student(
        name="Saloni",
        email="saloni@example.com",
        age=17
    )

---

## 🔹 Add One Record

    session.add(student)

---

## 🔹 Save Record

    session.commit()

---

## 🔹 Add Multiple Records

    session.add_all([
        Student(
            name="Saloni",
            email="saloni@example.com"
        ),
        Student(
            name="Rahul",
            email="rahul@example.com"
        )
    ])

    session.commit()

---

## 🔹 Read All

    from sqlalchemy import select

    students = session.scalars(
        select(Student)
    ).all()

---

## 🔹 Read First

    student = session.scalars(
        select(Student)
    ).first()

---

## 🔹 Read One or None

    student = session.scalars(
        select(Student)
        .where(Student.email == "saloni@example.com")
    ).one_or_none()

---

## 🔹 Read by Primary Key

    student = session.get(Student, 1)

---

## 🔹 Filter

    statement = select(Student).where(
        Student.age >= 18
    )

    students = session.scalars(
        statement
    ).all()

---

## 🔹 Multiple Conditions

    statement = select(Student).where(
        Student.age >= 18,
        Student.course == "Data Science"
    )

---

## 🔹 Select a Column

    names = session.scalars(
        select(Student.name)
    ).all()

---

## 🔹 Order Results

    statement = select(Student).order_by(
        Student.name
    )

---

## 🔹 Limit Results

    statement = select(Student).limit(5)

---

## 🔹 Check for Missing Record

    student = session.get(Student, 100)

    if student is None:
        print("Student not found")

---

## 🔹 Rollback

    try:
        session.add(student)
        session.commit()

    except Exception:
        session.rollback()
        raise

---

## 🔹 Important Methods

| Method | Purpose |
|---|---|
| `add()` | Add one object |
| `add_all()` | Add multiple objects |
| `commit()` | Save transaction |
| `select()` | Build SELECT query |
| `scalars()` | Return ORM objects |
| `all()` | Return all results |
| `first()` | Return first result |
| `one_or_none()` | Return one result or None |
| `get()` | Find by primary key |
| `where()` | Add filtering condition |
| `order_by()` | Sort results |
| `limit()` | Limit result count |
| `rollback()` | Cancel uncommitted changes |

---

## 🔹 Create Flow

    Model(...)
        ↓
    session.add()
        ↓
    session.commit()
        ↓
    Database

---

## 🔹 Read Flow

    select(Model)
        ↓
    session.scalars()
        ↓
    all() / first()
        ↓
    Python Objects

---

## ⭐ Remember

    CREATE = add() + commit()

    READ = select() + scalars()

    PRIMARY KEY = session.get()