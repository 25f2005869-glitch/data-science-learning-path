# ⚡ Day 088 — Dashboard Development Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 088  
**Topic:** Dashboard Development  

---

## 🔹 Dashboard Flow

    User
      ↓
    Flask Route
      ↓
    Database Query
      ↓
    Python Data
      ↓
    Jinja2 Template
      ↓
    HTML/CSS/JS
      ↓
    Browser

---

## 🔹 Basic Dashboard Route

    @app.route("/dashboard")
    @login_required
    def dashboard():
        students = Student.query.all()
        return render_template(
            "dashboard.html",
            students=students
        )

---

## 🔹 Jinja2 Variable

    {{ student.name }}

---

## 🔹 Jinja2 Loop

    {% for student in students %}
        {{ student.name }}
    {% endfor %}

---

## 🔹 Jinja2 Condition

    {% if student.marks >= 50 %}
        Passed
    {% else %}
        Failed
    {% endif %}

---

## 🔹 Empty Data

    {% if students %}
        Display records
    {% else %}
        No records found
    {% endif %}

---

## 🔹 Summary Card

    total_students = Student.query.count()

    return render_template(
        "dashboard.html",
        total_students=total_students
    )

Template:

    {{ total_students }}

---

## 🔹 Search

    search = request.args.get("search", "").strip()

---

## 🔹 Flash Message

    flash("Student added successfully.", "success")

---

## 🔹 URL Navigation

    {{ url_for("dashboard") }}

---

## 🔹 Dashboard Components

    Header
    Sidebar
    Navigation
    Summary Cards
    Tables
    Search
    Filters
    Actions
    Footer

---

## 🔹 CRUD

    Create → Add record
    Read   → Display record
    Update → Edit record
    Delete → Remove record

---

## 🔹 Authentication vs Authorization

    Authentication
    = Who are you?

    Authorization
    = What are you allowed to do?

---

## 🔹 Responsive Grid

    .dashboard-grid {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
    }

---

## 🔹 Security Checklist

    ✓ Protect private routes
    ✓ Verify authorization
    ✓ Hash passwords
    ✓ Validate input
    ✓ Use ORM/parameterized queries
    ✓ Use CSRF protection
    ✓ Escape untrusted output
    ✓ Protect SECRET_KEY
    ✓ Never trust client-side authorization

---

## 🔹 Dashboard Golden Rule

    Fetch → Process → Pass → Render → Protect

---

## 🔹 Important Flask/Jinja2 Tools

    render_template()
    request.args
    request.form
    redirect()
    url_for()
    flash()
    login_required()
    session