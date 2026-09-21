# ⚡ Day 061 — Flask Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 061  
**Topic:** Introduction to Flask

---

## 🐍 Flask Basics

| Concept | Meaning |
|---|---|
| Flask | Python web framework |
| `Flask` | Flask application class |
| `app` | Application object |
| Route | URL mapped to a function |
| View Function | Function handling a request |
| Response | Data returned to browser |
| Development Server | Local server for development |

---

## 📦 Installation

    pip install flask

Or:

    python -m pip install flask

---

## 🚀 Basic Flask Application

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        app.run(debug=True)

---

## 🔗 Route

    @app.route("/about")
    def about():
        return "About Page"

URL:

    /about

---

## 🏠 Root Route

    @app.route("/")
    def home():
        return "Home Page"

---

## 📄 Multiple Routes

    @app.route("/")
    def home():
        return "Home"

    @app.route("/about")
    def about():
        return "About"

    @app.route("/contact")
    def contact():
        return "Contact"

---

## 🐞 Debug Mode

    app.run(debug=True)

Useful during development.

Do not expose development debug mode in production.

---

## ▶️ Run Flask

    python app.py

Then open the local Flask server address shown in the terminal, commonly:

    http://127.0.0.1:5000/

---

## 🔄 Request Flow

    Browser
        ↓
    HTTP Request
        ↓
    Flask
        ↓
    Route
        ↓
    View Function
        ↓
    Response
        ↓
    Browser

---

## 📁 Basic Structure

    project/
    │
    ├── app.py
    ├── templates/
    └── static/

---

## 🧠 Remember

    URL
      ↓
    Route
      ↓
    Function
      ↓
    Response

---

## ⚠️ Common Errors

- Flask not installed
- Incorrect Python command
- Wrong project directory
- Missing `@app.route()`
- Incorrect route URL
- Application not running
- Debug mode used carelessly

---

## ⭐ Most Important Syntax

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        app.run()