# 📝 Day 062 — Installing Flask and Project Structure

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 062  
**Topic:** Installing Flask and Project Structure

---

## 1. Check Python Installation

Before installing Flask, verify Python:

    python --version

If the system uses `python3`:

    python3 --version

Python is required because Flask is a Python web framework.

---

## 2. Check pip

`pip` is the Python package installer.

Check pip:

    pip --version

Or:

    python -m pip --version

It is often safer to use:

    python -m pip

because it makes it clear which Python installation is being used.

---

## 3. What is a Virtual Environment?

A virtual environment creates an isolated Python environment for a project.

It allows each project to have its own packages and package versions.

Without virtual environments, packages from different projects can interfere with each other.

---

## 4. Create a Virtual Environment

Inside the project directory:

    python -m venv .venv

This creates a `.venv` directory.

Example:

    flask-project/
    └── .venv/

---

## 5. Activate the Virtual Environment

### Windows

    .venv\Scripts\activate

### macOS/Linux

    source .venv/bin/activate

After activation, the terminal usually shows the environment name.

---

## 6. Deactivate the Environment

To leave the virtual environment:

    deactivate

---

## 7. Install Flask

After activating the virtual environment:

    python -m pip install flask

Flask and its required dependencies are installed into the environment.

---

## 8. Verify Flask

One simple verification method is:

    python -c "import flask; print(flask.__version__)"

The command should successfully import Flask.

---

## 9. Why Use `requirements.txt`?

`requirements.txt` records project dependencies.

Example:

    Flask==3.x.x

The exact version depends on the version installed in your environment.

Generate the dependency list using:

    python -m pip freeze > requirements.txt

Another developer can install the recorded dependencies with:

    python -m pip install -r requirements.txt

---

## 10. Basic Flask Project Structure

A beginner Flask project can be organized as:

    flask-project/
    │
    ├── .venv/
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    │
    ├── templates/
    │   └── index.html
    │
    └── static/
        ├── css/
        │   └── style.css
        ├── js/
        │   └── script.js
        └── images/

---

## 11. `.venv`

`.venv` contains the project's virtual environment.

It normally should not be committed to Git.

Instead, recreate the environment using the dependency file.

---

## 12. `app.py`

`app.py` is commonly used as the main Flask application file in a simple project.

Example:

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        app.run(debug=True)

---

## 13. `templates/`

The `templates` directory is conventionally used for HTML templates.

Example:

    templates/
    └── index.html

Later, Flask's `render_template()` function will be used to render these HTML files.

Example:

    from flask import render_template

    @app.route("/")
    def home():
        return render_template("index.html")

---

## 14. `static/`

The `static` directory is conventionally used for files that are served as static assets.

Common contents:

- CSS
- JavaScript
- Images
- Fonts

Example:

    static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/

---

## 15. `.gitignore`

`.gitignore` tells Git which files or directories should not be tracked.

A basic Flask `.gitignore` may include:

    .venv/
    __pycache__/
    *.pyc
    .env

The exact contents can vary depending on the project.

---

## 16. Environment Variables

Sensitive configuration should not normally be hard-coded into source code.

Examples of sensitive configuration include:

- Secret keys
- Database credentials
- API keys

Environment variables can be used for configuration.

Do not commit secrets to Git repositories.

---

## 17. Running the Application

Activate the virtual environment and run:

    python app.py

The Flask development server will start.

The terminal will provide the local server address.

A common development address is:

    http://127.0.0.1:5000/

---

## 18. Development vs Production

The Flask development server is intended for local development and testing.

It is not a replacement for a production deployment server.

Debug mode is useful during development but should not be exposed carelessly in production.

---

## 19. Common Installation Problems

### Flask is not found

Check whether the virtual environment is activated.

Then install Flask:

    python -m pip install flask

### `python` command does not work

Try:

    python3 --version

### Wrong package environment

Check:

    python -m pip --version

This helps identify which Python installation is being used.

### Application does not start

Check:

- Python syntax
- Flask installation
- Correct project directory
- Correct filename
- Route definition

---

## 20. Recommended Workflow

A clean workflow is:

    Create project
          ↓
    Create virtual environment
          ↓
    Activate environment
          ↓
    Install Flask
          ↓
    Create app.py
          ↓
    Create templates/
          ↓
    Create static/
          ↓
    Create requirements.txt
          ↓
    Create .gitignore
          ↓
    Run application

---

## 21. Key Takeaway

A Flask project should be organized so that application code, HTML templates, static assets, dependencies, and environment configuration are easy to manage.

Remember:

    .venv/          → isolated Python environment
    app.py          → Flask application
    templates/      → HTML templates
    static/         → CSS, JS, images
    requirements.txt → dependencies
    .gitignore      → files ignored by Git