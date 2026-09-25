# ⚡ Day 090 — Search and Filtering Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 090  
**Topic:** Search and Filtering  

---

## 🔹 Query Parameter

    /students?search=saloni

---

## 🔹 Flask

    search = request.args.get(
        "search",
        ""
    ).strip()

---

## 🔹 Basic Search

    query = db.select(Student).where(
        Student.name.ilike(f"%{search}%")
    )

---

## 🔹 Execute Query

    students = db.session.execute(
        query
    ).scalars().all()

---

## 🔹 Multiple Fields

    from sqlalchemy import or_

    query = db.select(Student).where(
        or_(
            Student.name.ilike(f"%{search}%"),
            Student.email.ilike(f"%{search}%"),
            Student.course.ilike(f"%{search}%")
        )
    )

---

## 🔹 AND Conditions

    query = query.where(
        Student.marks >= 50,
        Student.course == "Data Science"
    )

---

## 🔹 OR Conditions

    from sqlalchemy import or_

    query = query.where(
        or_(
            Student.course == "Data Science",
            Student.course == "Mathematics"
        )
    )

---

## 🔹 Course Filter

    query = query.where(
        Student.course == course
    )

---

## 🔹 Minimum Marks

    min_marks = request.args.get(
        "min_marks",
        type=int
    )

    if min_marks is not None:
        query = query.where(
            Student.marks >= min_marks
        )

---

## 🔹 Ascending

    query = query.order_by(
        Student.marks.asc()
    )

---

## 🔹 Descending

    query = query.order_by(
        Student.marks.desc()
    )

---

## 🔹 Allowlisted Sorting

    sort_options = {
        "name": Student.name,
        "marks": Student.marks,
        "course": Student.course
    }

    sort_column = sort_options.get(
        sort,
        Student.name
    )

---

## 🔹 Search Form

    <form method="GET" action="/students">
        <input
            type="search"
            name="search"
        >
        <button type="submit">
            Search
        </button>
    </form>

---

## 🔹 No Results

    {% if students %}
        Display results
    {% else %}
        No students found.
    {% endif %}

---

## 🔹 Search Concepts

    Search
    ↓
    request.args
    ↓
    Validate
    ↓
    SQLAlchemy WHERE
    ↓
    Database
    ↓
    Jinja2
    ↓
    Results

---

## 🔹 Security

    ✓ Validate input
    ✓ Use SQLAlchemy
    ✓ Avoid raw SQL concatenation
    ✓ Allowlist sorting
    ✓ Authenticate private data
    ✓ Authorize access
    ✓ Use pagination for large datasets

---

## 🔹 Search vs Filter

    Search  → Keyword matching
    Filter  → Condition matching
    Sort    → Ordering results

---

## 🔹 Golden Rule

    GET → Validate → Query → Filter → Sort → Render