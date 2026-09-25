# 📚 Day 090 — Search and Filtering Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 090  
**Topic:** Search and Filtering  

---

# 1. What is Search?

Search allows a user to find records matching a specific keyword or value.

Example:

A Student Management System may allow users to search:

    Saloni
    Data Science
    saloni@example.com

Instead of displaying every record, the application returns matching records.

---

# 2. What is Filtering?

Filtering means selecting records according to specific conditions.

Examples:

    Course = Data Science
    Marks >= 80
    Age >= 18
    Status = Passed

Search usually focuses on keywords, while filtering focuses on conditions.

---

# 3. Search and Filtering Flow

A typical Flask flow is:

    User enters search/filter
              ↓
        Browser sends GET
              ↓
        Flask reads request.args
              ↓
        SQLAlchemy builds query
              ↓
        Database returns records
              ↓
        Jinja2 renders results

---

# 4. Query Parameters

Query parameters are values added to a URL.

Example:

    /students?search=saloni

Here:

    search = saloni

Another example:

    /students?course=Data%20Science

Multiple parameters:

    /students?search=saloni&course=Data%20Science

---

# 5. Flask request.args

Flask provides query parameters through `request.args`.

Example:

    search = request.args.get("search", "")

The second argument provides a default value.

---

# 6. Removing Extra Spaces

User input may contain unnecessary spaces.

Example:

    search = request.args.get(
        "search",
        ""
    ).strip()

This converts:

    "  Saloni  "

into:

    "Saloni"

---

# 7. Basic Search Route

Example:

    @app.route("/students")
    def students():

        search = request.args.get(
            "search",
            ""
        ).strip()

        if search:
            students = db.session.execute(
                db.select(Student).where(
                    Student.name.ilike(f"%{search}%")
                )
            ).scalars().all()
        else:
            students = db.session.execute(
                db.select(Student)
            ).scalars().all()

        return render_template(
            "students.html",
            students=students,
            search=search
        )

---

# 8. SQL LIKE

SQL `LIKE` is commonly used for pattern matching.

Conceptually:

    WHERE name LIKE '%saloni%'

The `%` wildcard means that other characters can appear before or after the search text.

For example:

    %saloni%

can match:

    Saloni
    Saloni Tiwari
    Student Saloni

---

# 9. SQLAlchemy ilike()

SQLAlchemy provides `ilike()` for case-insensitive pattern matching on databases that support it.

Example:

    Student.name.ilike("%saloni%")

This can match different capitalization forms such as:

    Saloni
    saloni
    SALONI

Database behavior can vary, so portability should be considered.

---

# 10. Search Multiple Fields

A search box may search multiple columns.

Example:

    from sqlalchemy import or_

    query = db.select(Student).where(
        or_(
            Student.name.ilike(f"%{search}%"),
            Student.email.ilike(f"%{search}%"),
            Student.course.ilike(f"%{search}%")
        )
    )

This searches:

    Name
    Email
    Course

---

# 11. OR Condition

`or_()` means at least one condition should match.

Example:

    from sqlalchemy import or_

    query = db.select(Student).where(
        or_(
            Student.name == "Saloni",
            Student.course == "Data Science"
        )
    )

---

# 12. AND Condition

`and_()` requires multiple conditions to be true.

Example:

    from sqlalchemy import and_

    query = db.select(Student).where(
        and_(
            Student.marks >= 80,
            Student.course == "Data Science"
        )
    )

---

# 13. Multiple Conditions

SQLAlchemy can combine conditions.

Example:

    query = db.select(Student).where(
        Student.marks >= 50,
        Student.course == "Data Science"
    )

This represents an AND-style condition.

---

# 14. Filtering by Course

Example:

    course = request.args.get(
        "course",
        ""
    ).strip()

    if course:
        query = query.where(
            Student.course == course
        )

This returns students belonging to the selected course.

---

# 15. Filtering by Marks

Example:

    min_marks = request.args.get(
        "min_marks",
        type=int
    )

    if min_marks is not None:
        query = query.where(
            Student.marks >= min_marks
        )

---

# 16. Filtering Passed Students

Example:

    query = query.where(
        Student.marks >= 50
    )

This returns students who have passed according to the selected rule.

---

# 17. Combining Search and Filters

A dashboard may support:

    Search = Saloni
    Course = Data Science
    Minimum Marks = 70

The application can construct one database query containing all applicable conditions.

Example:

    query = db.select(Student)

    if search:
        query = query.where(
            Student.name.ilike(f"%{search}%")
        )

    if course:
        query = query.where(
            Student.course == course
        )

    if min_marks is not None:
        query = query.where(
            Student.marks >= min_marks
        )

---

# 18. Sorting

Sorting changes the order of returned records.

Ascending:

    query = query.order_by(
        Student.marks.asc()
    )

Descending:

    query = query.order_by(
        Student.marks.desc()
    )

---

# 19. Sorting by Name

Example:

    query = query.order_by(
        Student.name.asc()
    )

---

# 20. Allowlisted Sorting

Never blindly use arbitrary user input as a database field.

Instead, create an allowlist.

Example:

    sort_options = {
        "name": Student.name,
        "marks": Student.marks,
        "course": Student.course
    }

    sort = request.args.get(
        "sort",
        "name"
    )

    sort_column = sort_options.get(
        sort,
        Student.name
    )

    query = query.order_by(sort_column.asc())

This ensures that users can choose only supported sorting fields.

---

# 21. Search Form

A GET search form may look like:

    <form method="GET" action="/students">

        <input
            type="search"
            name="search"
            placeholder="Search students"
        >

        <button type="submit">
            Search
        </button>

    </form>

The browser may generate:

    /students?search=saloni

---

# 22. Preserving Search Values

The entered search term can be displayed again.

Jinja2:

    <input
        type="search"
        name="search"
        value="{{ search }}"
    >

This improves user experience.

---

# 23. Empty Search

If no search term is provided, the application can display all records.

Example:

    if search:
        # Apply search
    else:
        # Return all records

---

# 24. No Results

A dashboard should handle empty results.

Jinja2:

    {% if students %}
        {% for student in students %}
            {{ student.name }}
        {% endfor %}
    {% else %}
        <p>No students found.</p>
    {% endif %}

---

# 25. Search Result Count

The application can show how many records were found.

Python:

    result_count = len(students)

Template:

    <p>{{ result_count }} students found.</p>

For very large datasets, database-side counting is generally preferable to loading all rows just to count them.

---

# 26. Search vs Client-Side Filtering

### Client-Side Filtering

JavaScript filters data already loaded into the browser.

Advantages:

- Fast for small datasets
- No additional server request

Disadvantages:

- Requires all data to be loaded
- Not suitable for large datasets
- Cannot protect private data by itself

### Server-Side Filtering

Flask and the database perform the filtering.

Advantages:

- Better for large datasets
- Less data sent to the browser
- Works naturally with database queries

For database applications, server-side filtering is generally preferred.

---

# 27. Search and Security

User input must not be trusted.

Use:

- SQLAlchemy queries
- Parameterized SQL
- Input validation
- Allowlisted sort fields
- Authentication
- Authorization

Avoid constructing raw SQL by directly concatenating user input.

Unsafe conceptual example:

    "SELECT * FROM students WHERE name = '" + search + "'"

Prefer SQLAlchemy or parameterized queries.

---

# 28. Search + CRUD

Search and filtering work naturally with CRUD.

Example:

    Search
       ↓
    Find record
       ↓
    View
       ↓
    Edit
       ↓
    Delete

The filtered result table can contain CRUD action buttons.

---

# 29. Dashboard Search Architecture

A complete dashboard can contain:

    Search box
    Course filter
    Marks filter
    Sort dropdown
    Result count
    Student table
    Pagination

This creates a powerful database-driven interface.

---

# 30. Pagination

When a database contains many records, loading everything at once may be inefficient.

Pagination divides results into pages.

Example:

    Page 1 → Students 1–20
    Page 2 → Students 21–40
    Page 3 → Students 41–60

Pagination can be combined with search, filtering, and sorting.

---

# 31. Best Practices

- Use GET for search/filter parameters.
- Strip unnecessary whitespace.
- Validate filter values.
- Use SQLAlchemy/parameterized queries.
- Allowlist sort fields.
- Handle empty results.
- Preserve filter values in the UI.
- Use pagination for large datasets.
- Keep queries readable.
- Add database indexes when appropriate for frequently searched fields.
- Protect private records with authentication and authorization.

---

# 32. Complete Search Workflow

    User enters search
            ↓
    GET /students?search=saloni
            ↓
    request.args.get("search")
            ↓
    Validate / normalize input
            ↓
    SQLAlchemy WHERE condition
            ↓
    Database query
            ↓
    Results
            ↓
    Jinja2 template
            ↓
    Filtered table

---

# 33. Key Takeaway

Search answers:

    "Which records match this keyword?"

Filtering answers:

    "Which records satisfy these conditions?"

Sorting answers:

    "In what order should the records appear?"

Together they make database-driven dashboards much easier to use.