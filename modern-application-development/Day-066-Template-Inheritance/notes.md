# 🧩 Day 066 — Template Inheritance Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 066  
**Topic:** Jinja2 Template Inheritance

---

## 1. What is Template Inheritance?

Template inheritance is a Jinja2 feature that allows one template to reuse the structure of another template.

It helps us avoid repeating common HTML.

For example, many pages may have:

- Same header
- Same navigation bar
- Same footer
- Same CSS
- Different page content

Instead of writing the common HTML repeatedly, we create a **base template**.

---

## 2. Base Template

A base template contains the common structure of a website.

Example structure:

    templates/
    ├── base.html
    ├── home.html
    ├── about.html
    └── contact.html

`base.html` can contain:

- HTML document structure
- Header
- Navigation
- Main container
- Footer
- CSS links

---

## 3. The `{% block %}` Tag

A block defines an area that child templates can replace.

Example:

    {% block content %}
    {% endblock %}

The child template can put its own content inside this block.

---

## 4. The `{% extends %}` Tag

The `{% extends %}` tag allows a child template to inherit a base template.

Example:

    {% extends "base.html" %}

This tells Jinja2 that the current template should use the structure of `base.html`.

---

## 5. Child Template

A child template provides page-specific content.

Example:

    {% extends "base.html" %}

    {% block content %}
        <h1>Home Page</h1>
        <p>Welcome to my website.</p>
    {% endblock %}

The common layout comes from `base.html`.

---

## 6. How Inheritance Works

The process is:

1. Flask receives a request.
2. Flask calls `render_template()`.
3. Jinja2 loads the requested child template.
4. The child template extends the base template.
5. Jinja2 finds the blocks.
6. Child content is inserted into the corresponding blocks.
7. The final HTML is sent to the browser.

---

## 7. Example Base Template

A simple base template can look like:

    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}My Website{% endblock %}</title>
    </head>
    <body>

        <header>
            <h1>My Website</h1>
        </header>

        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>

        <main>
            {% block content %}
            {% endblock %}
        </main>

        <footer>
            <p>My Website</p>
        </footer>

    </body>
    </html>

---

## 8. Example Child Template

    {% extends "base.html" %}

    {% block title %}
        Home
    {% endblock %}

    {% block content %}
        <h2>Welcome</h2>
        <p>This is the home page.</p>
    {% endblock %}

The child template does not need to repeat the complete HTML structure.

---

## 9. Multiple Blocks

A base template can contain multiple blocks.

Example:

    {% block title %}{% endblock %}

    {% block styles %}{% endblock %}

    {% block content %}{% endblock %}

    {% block scripts %}{% endblock %}

Each child template can override the blocks it needs.

---

## 10. `{{ super() }}`

`super()` allows a child template to keep the parent block content and add more content.

Example:

    {% block content %}
        {{ super() }}
        <p>Additional content.</p>
    {% endblock %}

Without `super()`, the parent block content is replaced.

---

## 11. Important Difference

Jinja2 uses different syntax for different purposes.

Variable output:

    {{ variable }}

Template statements:

    {% statement %}

Comments:

    {# comment #}

Examples:

    {{ name }}

    {% extends "base.html" %}

    {# This is a Jinja2 comment #}

---

## 12. Flask Example

Python:

    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    if __name__ == "__main__":
        app.run(debug=True)

---

## 13. Recommended Project Structure

A Flask project can be organized as:

    project/
    ├── app.py
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── about.html
    │   └── contact.html
    └── static/
        ├── css/
        ├── js/
        └── images/

---

## 14. Why Template Inheritance is Useful

Without inheritance:

- Header is repeated.
- Navigation is repeated.
- Footer is repeated.
- CSS references may be repeated.
- Updating the layout becomes difficult.

With inheritance:

- Common structure is written once.
- Child templates contain only page-specific content.
- Maintenance becomes easier.
- Code becomes cleaner.
- The DRY principle is followed.

DRY means:

**Don't Repeat Yourself.**

---

## 15. Parent and Child Relationship

Think of:

    base.html

as the parent.

And:

    home.html
    about.html
    contact.html

as children.

The child receives the common layout from the parent and fills the defined blocks.

---

## 16. Common Mistakes

### Mistake 1: Wrong template name

    {% extends "bases.html" %}

when the file is actually:

    base.html

### Mistake 2: Missing block

The child may define:

    {% block content %}

but the base template may not contain a matching block.

### Mistake 3: Incorrect block closing

Always close the block:

    {% block content %}
    ...
    {% endblock %}

### Mistake 4: Putting content outside the inheritance structure

Keep child-specific content inside appropriate blocks.

### Mistake 5: Incorrect template folder

Flask normally searches for templates inside:

    templates/

---

## 17. Best Practices

- Create one reusable `base.html`.
- Keep common layout in the base template.
- Use meaningful block names.
- Keep child templates short.
- Use `{{ super() }}` when parent content should be preserved.
- Keep CSS and JavaScript in appropriate static files.
- Avoid unnecessary duplication.
- Keep templates readable.
- Follow a consistent project structure.

---

## 18. Mental Model

Remember:

**Base Template = Common Layout**

**Child Template = Page-Specific Content**

**extends = Inherit**

**block = Replaceable Area**

**super() = Keep Parent Content**

---

## 19. Summary

Jinja2 Template Inheritance is one of the most important features for building multi-page Flask applications.

The main syntax is:

    {% extends "base.html" %}

    {% block content %}
        Page-specific content
    {% endblock %}

It allows Flask applications to use reusable layouts and reduces repeated HTML.