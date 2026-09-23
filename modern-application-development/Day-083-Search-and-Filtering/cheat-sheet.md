# 🔎 Day 083 — Search and Filtering — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 083  
**Topic:** Search and Filtering

---

## 1. Query Parameter

    /students?search=saloni

---

## 2. Flask `request.args`

    search = request.args.get("search", "")

With whitespace removal:

    search = request.args.get("search", "").strip()

---

## 3. SQL WHERE

    SELECT * FROM students
    WHERE marks >= 80;

---

## 4. SQL LIKE

    SELECT * FROM students
    WHERE name LIKE '%saloni%';

Patterns:

    'saloni%'     → starts with
    '%saloni'     → ends with
    '%saloni%'    → contains

---

## 5. SQLAlchemy Basic Filter

    statement = select(Student).where(
        Student.marks >= 80
    )

---

## 6. Text Search

    statement = select(Student).where(
        Student.name.ilike("%saloni%")
    )

---

## 7. Multiple Conditions

    statement = select(Student).where(
        Student.marks >= 70,
        Student.course == "Data Science"
    )

---

## 8. OR Conditions

    from sqlalchemy import or_

    statement = select(Student).where(
        or_(
            Student.course == "Data Science",
            Student.course == "Programming"
        )
    )

---

## 9. Sorting

Ascending:

    statement = select(Student).order_by(
        Student.marks.asc()
    )

Descending:

    statement = select(Student).order_by(
        Student.marks.desc()
    )

---

## 10. Search Form

    <form method="GET" action="/students">
        <input type="search" name="search">
        <button type="submit">Search</button>
    </form>

---

## 11. Search Route Pattern

    @app.route("/students")
    def students():
        search = request.args.get("search", "").strip()

        statement = select(Student)

        if search:
            statement = statement.where(
                Student.name.ilike(f"%{search}%")
            )

        students = db.session.scalars(statement).all()

        return render_template(
            "students.html",
            students=students,
            search=search
        )

---

## 12. Search Multiple Fields

    statement = select(Student).where(
        or_(
            Student.name.ilike("%saloni%"),
            Student.email.ilike("%saloni%")
        )
    )

---

## 13. Important Methods

| Method | Purpose |
|---|---|
| `request.args` | Read query parameters |
| `select()` | Build SELECT query |
| `where()` | Add filtering |
| `like()` | Pattern matching |
| `ilike()` | Case-insensitive pattern matching where supported |
| `and_()` | Combine AND conditions |
| `or_()` | Combine OR conditions |
| `order_by()` | Sort results |
| `asc()` | Ascending order |
| `desc()` | Descending order |
| `strip()` | Remove surrounding whitespace |

---

## 14. Search Flow

    User Input
        ↓
    GET Request
        ↓
    request.args
        ↓
    SQLAlchemy Query
        ↓
    Database
        ↓
    Filtered Results
        ↓
    Jinja2
        ↓
    Browser

---

## 15. Security

Avoid:

    "SELECT ... WHERE name = '" + search + "'"

Prefer:

    SQLAlchemy expressions
    Parameterized queries

---

## 16. Remember

**Search = find matching records**

**Filtering = select records based on conditions**

**Sorting = arrange the returned records**

**GET = commonly used for search**

**`request.args` = query parameters**

**`where()` = database filtering**