# 📝 Day 065 — Jinja2 Templates

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 065  
**Topic:** Jinja2 Templates

---

## 1. What is Jinja2?

Jinja2 is a template engine used with Flask to generate dynamic HTML.

It allows Python data to be inserted into HTML templates.

Basic flow:

    Python Data
         ↓
       Flask
         ↓
      Jinja2
         ↓
    HTML Template
         ↓
      Browser

---

## 2. Why Use Templates?

HTML can technically be returned directly from a Flask function.

Example:

    @app.route("/")
    def home():
        return "<h1>Welcome</h1>"

For large pages, this becomes difficult to maintain.

Instead, HTML can be placed inside:

    templates/index.html

and Flask can render it:

    @app.route("/")
    def home():
        return render_template("index.html")

This keeps Python and HTML separate.

---

## 3. The `templates` Folder

Flask conventionally searches for templates inside:

    templates/

Example:

    flask-project/
    │
    ├── app.py
    │
    └── templates/
        ├── index.html
        ├── about.html
        └── student.html

---

## 4. `render_template()`

Import it from Flask:

    from flask import Flask, render_template

Then:

    @app.route("/")
    def home():
        return render_template("index.html")

Flask finds `index.html` inside the `templates` folder.

---

## 5. Passing Variables

Python data can be passed to a template.

Example:

    @app.route("/")
    def home():
        name = "Saloni"
        return render_template("index.html", name=name)

The template can display it using:

    {{ name }}

---

## 6. Multiple Variables

Example:

    @app.route("/")
    def home():
        name = "Saloni"
        course = "MAD 1"
        score = 95

        return render_template(
            "index.html",
            name=name,
            course=course,
            score=score
        )

Template:

    <h1>{{ name }}</h1>
    <p>Course: {{ course }}</p>
    <p>Score: {{ score }}</p>

---

## 7. Jinja2 Expression Syntax

Jinja2 expressions use:

    {{ }}

Examples:

    {{ name }}

    {{ score + 5 }}

    {{ 10 * 2 }}

    {{ name.upper() }}

The expression is evaluated during template rendering.

---

## 8. Conditions

Jinja2 supports conditional statements.

Example:

    {% if score >= 50 %}
        <p>Pass</p>
    {% else %}
        <p>Fail</p>
    {% endif %}

The `{% %}` syntax is used for template statements.

---

## 9. `if`, `elif`, and `else`

Example:

    {% if score >= 90 %}
        <p>Grade: A+</p>
    {% elif score >= 80 %}
        <p>Grade: A</p>
    {% elif score >= 70 %}
        <p>Grade: B</p>
    {% else %}
        <p>Grade: C or below</p>
    {% endif %}

---

## 10. Jinja2 `for` Loop

Jinja2 supports loops for displaying lists.

Python:

    courses = ["DBMS", "PDSA", "MLF"]

Template:

    <ul>
        {% for course in courses %}
            <li>{{ course }}</li>
        {% endfor %}
    </ul>

The template generates one list item for each course.

---

## 11. Loop Index

Jinja2 provides useful loop information.

Example:

    {% for course in courses %}
        <p>{{ loop.index }}. {{ course }}</p>
    {% endfor %}

`loop.index` starts from 1.

Other useful loop properties include:

- `loop.index`
- `loop.index0`
- `loop.first`
- `loop.last`
- `loop.length`

---

## 12. Dictionary Data

Python:

    student = {
        "name": "Saloni",
        "course": "MAD 1",
        "score": 95
    }

Pass it:

    return render_template(
        "student.html",
        student=student
    )

Access values using:

    {{ student.name }}

or:

    {{ student["name"] }}

---

## 13. List of Dictionaries

Example:

    students = [
        {"name": "Saloni", "score": 95},
        {"name": "Aman", "score": 82},
        {"name": "Riya", "score": 91}
    ]

Template:

    {% for student in students %}
        <p>{{ student.name }} - {{ student.score }}</p>
    {% endfor %}

This pattern is useful for displaying database records.

---

## 14. Jinja2 Filters

Filters modify or format values.

Syntax:

    {{ value | filter }}

Examples:

    {{ name | upper }}

    {{ name | lower }}

    {{ name | title }}

    {{ courses | length }}

---

## 15. Common Filters

| Filter | Purpose |
|---|---|
| `upper` | Converts text to uppercase |
| `lower` | Converts text to lowercase |
| `title` | Converts text to title case |
| `length` | Returns length |
| `trim` | Removes surrounding whitespace |
| `replace` | Replaces text |
| `default` | Provides a default value |

---

## 16. Filter Chaining

Multiple filters can be used together.

Example:

    {{ name | trim | title }}

The result of one filter is passed to the next filter.

---

## 17. Jinja2 Comments

Jinja2 comments use:

    {# This is a Jinja2 comment #}

They are template comments and are not rendered as normal HTML content.

---

## 18. HTML Comments vs Jinja2 Comments

HTML:

    <!-- HTML comment -->

Jinja2:

    {# Jinja2 comment #}

Jinja2 comments are useful for template-specific notes.

---

## 19. Template Inheritance

Jinja2 allows templates to inherit from a common base template.

Example structure:

    templates/
    ├── base.html
    ├── index.html
    └── about.html

Child template:

    {% extends "base.html" %}

    {% block content %}
        <h1>Home Page</h1>
    {% endblock %}

---

## 20. Blocks

A base template can define a block:

    {% block content %}
    {% endblock %}

Child templates can replace that block with their own content.

This avoids repeating the same header, navigation, and footer.

---

## 21. Template Inheritance Flow

    base.html
         ↓
    ┌───────────────┐
    │ Header        │
    │ Navigation    │
    │ Content Block │
    │ Footer        │
    └───────────────┘
         ↑
    Child Template

---

## 22. Dynamic Routes with Templates

Dynamic routes and Jinja2 can work together.

Example:

    @app.route("/student/<int:student_id>")
    def student(student_id):
        return render_template(
            "student.html",
            student_id=student_id
        )

For:

    /student/101

the template can display:

    {{ student_id }}

Result:

    Student ID: 101

---

## 23. Jinja2 and Flask

Flask handles:

- HTTP requests
- Routing
- Python backend logic
- Responses

Jinja2 handles:

- Dynamic HTML
- Variables
- Conditions
- Loops
- Filters
- Template inheritance

---

## 24. Jinja2 and Security

Jinja2 normally performs automatic HTML escaping for values rendered into templates.

This helps protect against certain forms of HTML injection and XSS.

However, developers must still validate user input and should not mark untrusted content as safe without understanding the security implications.

---

## 25. Important Jinja2 Syntax

Expression:

    {{ variable }}

Statement:

    {% statement %}

Comment:

    {# comment #}

Condition:

    {% if condition %}
        ...
    {% endif %}

Loop:

    {% for item in items %}
        ...
    {% endfor %}

Inheritance:

    {% extends "base.html" %}

Block:

    {% block content %}
        ...
    {% endblock %}

---

## 26. Complete Example

Python:

    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route("/")
    def home():
        student = {
            "name": "Saloni",
            "course": "MAD 1",
            "score": 95
        }

        courses = [
            "DBMS",
            "PDSA",
            "MLF"
        ]

        return render_template(
            "index.html",
            student=student,
            courses=courses
        )

    if __name__ == "__main__":
        app.run(debug=True)

Template:

    <h1>Welcome, {{ student.name }}</h1>

    <p>Course: {{ student.course }}</p>

    <p>Score: {{ student.score }}</p>

    <h2>Courses</h2>

    <ul>
        {% for course in courses %}
            <li>{{ course }}</li>
        {% endfor %}
    </ul>

---

## 27. Common Mistakes

### Mistake 1: Wrong template folder

Use:

    templates/

### Mistake 2: Forgetting `render_template`

Import:

    from flask import render_template

### Mistake 3: Incorrect variable syntax

Correct:

    {{ name }}

### Mistake 4: Missing `endif`

Every Jinja2 `if` block should be closed.

### Mistake 5: Missing `endfor`

Every Jinja2 `for` block should be closed.

### Mistake 6: Mixing Python and Jinja2 syntax

Python runs in the Flask application.

Jinja2 syntax is processed while the template is rendered.

---

## 28. Key Takeaway

Jinja2 connects Flask backend data with HTML templates.

Remember:

    Python Data
        ↓
    Flask
        ↓
    render_template()
        ↓
    Jinja2
        ↓
    HTML
        ↓
    Browser

Most important syntax:

    {{ variable }}

    {% if condition %}
    {% endif %}

    {% for item in items %}
    {% endfor %}

    {# comment #}

Jinja2 is an important foundation for building dynamic Flask applications.