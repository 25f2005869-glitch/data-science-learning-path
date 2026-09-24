# 📚 Day 088 — Dashboard Development Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 088  
**Topic:** Dashboard Development  

---

## 1. What is a Dashboard?

A dashboard is a web page that displays important information in a structured and easy-to-understand format.

A typical dashboard can contain:

- Summary cards
- Tables
- Charts
- Recent records
- User information
- Search and filters
- Navigation
- CRUD actions

Example:

A Student Dashboard may show:

- Total Students
- Average Marks
- Passed Students
- Failed Students
- Student Records

---

## 2. Dashboard Architecture

A Flask dashboard generally follows this flow:

User → Flask Route → Database → Query → Jinja2 Template → Browser

Example:

    @app.route("/dashboard")
    def dashboard():
        students = Student.query.all()
        return render_template("dashboard.html", students=students)

The database provides the data and Jinja2 displays it in HTML.

---

## 3. Dashboard Layout

A common dashboard layout contains:

- Header
- Sidebar
- Main content
- Summary cards
- Data tables
- Footer

Example structure:

    Dashboard
    ├── Header
    ├── Sidebar
    │   ├── Dashboard
    │   ├── Students
    │   ├── Courses
    │   └── Logout
    └── Main Content
        ├── Summary Cards
        ├── Recent Students
        └── Quick Actions

---

## 4. Dashboard Route

A dashboard normally has a dedicated Flask route.

Example:

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

For an authenticated application, the route should be protected.

Example:

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return render_template("dashboard.html")

---

## 5. Authentication and Dashboard

A dashboard often contains private information.

Therefore, authentication should be checked before allowing access.

Example:

    @login_required
    def dashboard():
        return render_template("dashboard.html")

Authentication answers:

    "Who is the user?"

Authorization answers:

    "What is the user allowed to do?"

---

## 6. Passing Data to a Dashboard

Flask can pass Python variables to Jinja2.

Example:

    students = Student.query.all()

    return render_template(
        "dashboard.html",
        students=students
    )

Jinja2 can then display the records.

Example:

    {% for student in students %}
        <p>{{ student.name }}</p>
    {% endfor %}

---

## 7. Summary Cards

Summary cards provide quick information.

Example:

    total_students = Student.query.count()

    return render_template(
        "dashboard.html",
        total_students=total_students
    )

Jinja2:

    <h2>{{ total_students }}</h2>

Possible dashboard cards:

- Total Students
- Total Courses
- Average Marks
- Passed Students
- Failed Students

---

## 8. Tables

Tables are useful for displaying database records.

Example:

    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Marks</th>
            </tr>
        </thead>

        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.name }}</td>
                <td>{{ student.email }}</td>
                <td>{{ student.marks }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

---

## 9. Conditional Display

Jinja2 conditions can change dashboard content.

Example:

    {% if students %}
        <p>Students are available.</p>
    {% else %}
        <p>No students found.</p>
    {% endif %}

This prevents an empty dashboard from looking broken.

---

## 10. Student Status

A dashboard can display different status values.

Example:

    {% if student.marks >= 50 %}
        <span>Passed</span>
    {% else %}
        <span>Failed</span>
    {% endif %}

The condition is evaluated on the server while rendering the template.

---

## 11. Search and Filtering

A dashboard may provide search and filtering.

Example route:

    @app.route("/dashboard")
    def dashboard():
        search = request.args.get("search", "").strip()

        if search:
            students = Student.query.filter(
                Student.name.ilike(f"%{search}%")
            ).all()
        else:
            students = Student.query.all()

        return render_template(
            "dashboard.html",
            students=students,
            search=search
        )

GET is commonly useful for search because the search term can be represented in the URL.

---

## 12. Dashboard CRUD Actions

A database dashboard may provide:

- Create
- Read
- Update
- Delete

Example actions:

    Add Student
    View Student
    Edit Student
    Delete Student

Destructive actions such as deletion should require appropriate authorization and confirmation.

---

## 13. Flash Messages

Flash messages provide feedback after an action.

Examples:

- Student added successfully.
- Student updated successfully.
- Student deleted successfully.
- Invalid form data.
- Unauthorized action.

Example:

    flash("Student added successfully.", "success")

The dashboard can display the message using:

    get_flashed_messages(with_categories=true)

---

## 14. Dashboard Navigation

A dashboard should have clear navigation.

Typical links:

- Dashboard
- Students
- Courses
- Profile
- Settings
- Logout

Flask's `url_for()` should be preferred instead of hard-coded application URLs.

Example:

    <a href="{{ url_for('dashboard') }}">Dashboard</a>

---

## 15. User-Specific Dashboard

Different users may see different information.

Example:

    Admin Dashboard
    - Manage students
    - Manage courses
    - View statistics

    Student Dashboard
    - View profile
    - View courses
    - View marks

Authorization should be enforced on the server, not only by hiding buttons in HTML.

---

## 16. Responsive Dashboard

A dashboard should work on:

- Desktop
- Laptop
- Tablet
- Mobile

CSS Grid and Flexbox are useful for dashboard layouts.

Example:

    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(
            auto-fit,
            minmax(220px, 1fr)
        );
        gap: 20px;
    }

---

## 17. Reusable Dashboard Components

Common components should be reusable.

Examples:

- Navbar
- Sidebar
- Card
- Table
- Alert
- Footer

Jinja2 template inheritance can help.

Example:

    {% extends "base.html" %}

    {% block content %}
        Dashboard content
    {% endblock %}

---

## 18. Dashboard Security

Important security practices:

- Protect private routes.
- Check authorization on the server.
- Hash passwords.
- Never expose passwords.
- Validate user input.
- Use parameterized queries or ORM queries.
- Protect forms against CSRF.
- Escape untrusted output.
- Do not expose secret keys.
- Do not trust hidden HTML fields for authorization.

---

## 19. Dashboard Development Workflow

A practical workflow:

1. Define dashboard users.
2. Identify required information.
3. Design the page structure.
4. Design database queries.
5. Create Flask routes.
6. Fetch database data.
7. Pass data to Jinja2.
8. Build reusable templates.
9. Add CRUD actions.
10. Add validation and flash messages.
11. Apply authentication and authorization.
12. Make the dashboard responsive.
13. Test all user flows.

---

## 20. Key Takeaway

A Flask dashboard is not only a frontend page.

It is a combination of:

    Authentication
    +
    Authorization
    +
    Flask Routes
    +
    Database Queries
    +
    Jinja2 Templates
    +
    HTML/CSS
    +
    JavaScript
    +
    Validation
    +
    Security

The goal is to present useful application data in a clear, secure, and responsive interface.