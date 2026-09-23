# 🔎 Day 083 — Search and Filtering — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 083  
**Topic:** Search and Filtering

---

## 1. What is Search?

Search allows a user to find specific records based on a keyword or value.

Example:

A student portal may contain:

- Saloni
- Rahul
- Priya
- Aman

If the user searches for `Saloni`, the application should return the matching student.

---

## 2. What is Filtering?

Filtering means selecting records that satisfy one or more conditions.

Examples:

- Students with marks greater than 80
- Students from a particular course
- Products under ₹1000
- Students whose name contains "an"

Search usually focuses on finding matching text, while filtering can use many types of conditions.

---

## 3. Query Parameters

A query parameter is additional information sent through a URL.

Example:

    /students?search=saloni

Here:

- `/students` → route
- `search` → parameter name
- `saloni` → parameter value

Multiple parameters can be used:

    /students?search=saloni&course=data-science

---

## 4. `request.args`

Flask provides query parameters through `request.args`.

Example:

    from flask import request

    search = request.args.get("search", "")

The default value `""` is useful when no search parameter is supplied.

---

## 5. Basic Search Flow

A typical search operation follows these steps:

1. User enters a keyword.
2. Browser sends the keyword as a query parameter.
3. Flask receives it using `request.args`.
4. The application builds a database query.
5. Database returns matching records.
6. Flask sends the results to the template.
7. Template displays the results.

---

## 6. SQL `WHERE`

SQL uses `WHERE` to filter records.

Example:

    SELECT * FROM students
    WHERE marks >= 80;

Only students with marks greater than or equal to 80 are returned.

---

## 7. SQL `LIKE`

`LIKE` is commonly used for text searching.

Example:

    SELECT * FROM students
    WHERE name LIKE '%saloni%';

The `%` symbol represents any sequence of characters.

Examples:

    'Saloni%'

Matches values beginning with Saloni.

    '%Saloni'

Matches values ending with Saloni.

    '%Saloni%'

Matches values containing Saloni.

---

## 8. SQLAlchemy `where()`

SQLAlchemy provides `where()` for filtering queries.

Example:

    from sqlalchemy import select

    statement = select(Student).where(Student.marks >= 80)

    students = session.scalars(statement).all()

---

## 9. Text Search with SQLAlchemy

Example:

    search = request.args.get("search", "").strip()

    statement = select(Student)

    if search:
        statement = statement.where(Student.name.ilike(f"%{search}%"))

    students = session.scalars(statement).all()

`ilike()` is useful for case-insensitive text matching on databases that support it appropriately.

---

## 10. `LIKE` vs `ILIKE`

`LIKE` performs pattern matching.

`ILIKE` is commonly used for case-insensitive pattern matching where supported.

Example:

    Student.name.like("%Saloni%")

    Student.name.ilike("%saloni%")

Database behavior can vary, so understand how the selected database handles case sensitivity.

---

## 11. Filtering by Number

Example:

    statement = select(Student).where(Student.marks >= 80)

Other examples:

    Student.age == 18

    Student.marks < 50

    Student.marks.between(60, 90)

---

## 12. Multiple Conditions

Conditions can be combined.

Example:

    from sqlalchemy import and_

    statement = select(Student).where(
        and_(
            Student.marks >= 80,
            Student.course == "Data Science"
        )
    )

SQLAlchemy also supports expressions such as:

    Student.marks >= 80

    Student.course == "Data Science"

These expressions can be combined using appropriate SQLAlchemy operators.

---

## 13. OR Conditions

Example:

    from sqlalchemy import or_

    statement = select(Student).where(
        or_(
            Student.course == "Data Science",
            Student.course == "Programming"
        )
    )

This returns students belonging to either course.

---

## 14. Search with Multiple Fields

A search box can search more than one field.

Example:

    statement = select(Student).where(
        or_(
            Student.name.ilike("%saloni%"),
            Student.email.ilike("%saloni%")
        )
    )

This can find the keyword in either the name or email.

---

## 15. Combining Search and Filters

Suppose the user wants:

- Name containing "saloni"
- Marks at least 70
- Course = Data Science

The query can combine all conditions.

Example:

    statement = select(Student).where(
        Student.name.ilike("%saloni%"),
        Student.marks >= 70,
        Student.course == "Data Science"
    )

---

## 16. Sorting Results

Search results can also be sorted.

Example:

    statement = (
        select(Student)
        .where(Student.marks >= 60)
        .order_by(Student.marks.desc())
    )

`desc()` sorts from highest to lowest.

`asc()` sorts from lowest to highest.

---

## 17. Empty Search

The application should handle an empty search safely.

Example:

    search = request.args.get("search", "").strip()

    if search:
        # Apply search condition
        pass
    else:
        # Show all records
        pass

An empty search can either display all records or show a message asking the user to enter a keyword.

---

## 18. Search Form

Example:

    <form method="GET" action="/students">
        <input type="search" name="search">
        <button type="submit">Search</button>
    </form>

Using GET is appropriate for search because the search criteria can be represented in the URL.

---

## 19. Search Route

Example:

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

## 20. Search + Filtering Workflow

    Browser
        ↓
    Search Form
        ↓
    GET /students?search=saloni
        ↓
    Flask request.args
        ↓
    SQLAlchemy Query
        ↓
    Database
        ↓
    Matching Records
        ↓
    Jinja2 Template
        ↓
    Results

---

## 21. SQL Injection

Never directly build SQL queries by concatenating untrusted user input.

Unsafe idea:

    query = "SELECT * FROM students WHERE name = '" + search + "'"

This can create SQL injection vulnerabilities.

Use SQLAlchemy expressions or parameterized SQL instead.

Example:

    statement = select(Student).where(
        Student.name.ilike(f"%{search}%")
    )

The ORM handles query parameters safely at the database layer.

---

## 22. Whitelisting Sort Fields

Do not blindly insert a user-provided column name into SQL.

Instead, map allowed values.

Example:

    allowed_sort = {
        "name": Student.name,
        "marks": Student.marks
    }

    sort = request.args.get("sort", "name")

    column = allowed_sort.get(sort, Student.name)

This prevents users from choosing arbitrary SQL expressions.

---

## 23. Search vs Filtering

| Search | Filtering |
|---|---|
| Usually keyword-based | Condition-based |
| Often uses text | Can use text, numbers, dates |
| Commonly uses `LIKE`/`ILIKE` | Commonly uses comparisons |
| Example: name contains "saloni" | marks >= 80 |
| Usually user-entered | Often dropdowns/sliders/forms |

---

## 24. Search vs Query Parameter

A search is a feature.

A query parameter is a mechanism used to send information.

Example:

    /students?search=saloni

Here:

- `search` is the query parameter.
- Searching for `saloni` is the feature.

---

## 25. Best Practices

- Use GET for normal search forms.
- Strip unnecessary whitespace.
- Handle empty searches.
- Validate filter values.
- Use SQLAlchemy expressions or parameterized SQL.
- Avoid SQL string concatenation.
- Restrict allowed sorting fields.
- Use indexes for frequently searched columns when appropriate.
- Keep queries efficient.
- Display useful "no results" messages.
- Preserve search/filter values in the UI.
- Combine search with pagination for large datasets.
- Do not expose sensitive database information.

---

## 26. Key Takeaway

Search and filtering connect the user interface with database queries.

The most important concepts are:

    request.args
    select()
    where()
    like()
    ilike()
    and_()
    or_()
    order_by()

A strong Flask developer should understand how user input travels from a search form to a safe database query and finally back to the results page.