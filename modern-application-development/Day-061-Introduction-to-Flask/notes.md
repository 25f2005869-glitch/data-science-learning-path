# 📝 Day 061 — Introduction to Flask

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 061  
**Topic:** Introduction to Flask

---

## 1. What is Flask?

Flask is a lightweight web framework written in Python.

It is used to build:

- Websites
- Web applications
- REST APIs
- Backend services

Flask provides the basic tools required to receive HTTP requests and return HTTP responses.

---

## 2. What is a Web Framework?

A web framework provides ready-made tools and structures for building web applications.

Without a framework, we would have to manually handle many backend tasks.

Examples of Python web frameworks:

- Flask
- Django
- FastAPI

Flask is known for being lightweight and flexible.

---

## 3. Why Use Flask?

Important advantages of Flask:

- Simple to learn
- Lightweight
- Python-based
- Flexible project structure
- Easy routing
- Useful for APIs
- Good for learning backend development
- Suitable for small and medium-sized applications

---

## 4. Flask and Python

Python is the programming language.

Flask is a framework built using Python.

Mental model:

Python → Programming Language

Flask → Python Web Framework

HTML → Page Structure

CSS → Page Styling

JavaScript → Browser-side Interactivity

Flask → Backend/Web Server

---

## 5. Installing Flask

First check whether Python is installed:

    python --version

Install Flask using pip:

    pip install flask

On some systems:

    python -m pip install flask

Verify the installation:

    python -c "import flask; print(flask.__version__)"

---

## 6. Creating a Flask Application

A basic Flask application can be created using:

    from flask import Flask

    app = Flask(__name__)

`Flask` is imported from the Flask package.

`app` is the Flask application object.

`__name__` helps Flask identify the current Python module.

---

## 7. What is a Route?

A route connects a URL to a Python function.

Example:

    @app.route("/")
    def home():
        return "Hello, Flask!"

When the browser requests:

    /

Flask executes:

    home()

This produces a response.

---

## 8. The `@app.route()` Decorator

`@app.route()` tells Flask which URL should be handled by a function.

Example:

    @app.route("/about")
    def about():
        return "About Page"

The `/about` URL is connected to the `about()` function.

---

## 9. View Function

A function that handles a web request is commonly called a view function.

Example:

    @app.route("/")
    def home():
        return "Welcome to my website!"

Here:

- `/` → route
- `home()` → view function
- Returned text → response

---

## 10. Running the Flask Application

A basic Flask application can be started with:

    if __name__ == "__main__":
        app.run()

Run the Python file:

    python app.py

Flask starts a development server.

The terminal usually displays a local address such as:

    http://127.0.0.1:5000/

Open this address in the browser.

---

## 11. Development Server

Flask provides a development server for testing applications locally.

Important:

The Flask development server is intended for development and testing.

It should not be treated as a production server.

---

## 12. Debug Mode

Debug mode helps during development.

Example:

    if __name__ == "__main__":
        app.run(debug=True)

Debug mode can provide:

- Detailed error information
- Automatic reloading when code changes

Do not enable debug mode carelessly in a production environment.

---

## 13. Returning a Response

A Flask route can return text:

    @app.route("/")
    def home():
        return "Hello World"

It can also return HTML:

    @app.route("/about")
    def about():
        return "<h1>About Me</h1><p>Welcome!</p>"

Flask converts the returned value into an HTTP response.

---

## 14. Multiple Routes

A Flask application can have multiple routes.

Example:

    @app.route("/")
    def home():
        return "Home Page"

    @app.route("/about")
    def about():
        return "About Page"

    @app.route("/contact")
    def contact():
        return "Contact Page"

Each URL is connected to a different view function.

---

## 15. Basic Flask Request Flow

The basic flow is:

Browser

↓

HTTP Request

↓

Flask Application

↓

Route Matching

↓

View Function

↓

HTTP Response

↓

Browser

---

## 16. Flask Project Structure

A simple project may look like:

    flask-project/
    │
    ├── app.py
    ├── templates/
    ├── static/
    └── README.md

`app.py` contains the Flask application.

`templates/` is commonly used for HTML templates.

`static/` is commonly used for CSS, JavaScript, and images.

These folders will become more important in later Flask days.

---

## 17. Flask vs HTML

HTML alone creates the structure of a webpage.

Flask runs on the server and can generate or serve web content dynamically.

Example:

HTML:

    <h1>Hello</h1>

Flask:

    @app.route("/")
    def home():
        return "<h1>Hello</h1>"

---

## 18. Flask vs JavaScript

JavaScript in the browser is primarily used for client-side behavior.

Flask runs on the server.

Typical architecture:

    Browser
       ↓
    JavaScript / HTML / CSS
       ↓
    HTTP Request
       ↓
    Flask Backend
       ↓
    Python Logic
       ↓
    HTTP Response
       ↓
    Browser

---

## 19. Common Mistakes

### Mistake 1: Forgetting the import

Incorrect:

    app = Flask(__name__)

Correct:

    from flask import Flask
    app = Flask(__name__)

### Mistake 2: Forgetting the route decorator

A URL needs a route definition.

### Mistake 3: Running the wrong Python file

Make sure the terminal is in the correct project directory.

### Mistake 4: Using production assumptions

The built-in development server is for development and testing.

### Mistake 5: Debug mode in production

Debug mode should not be exposed in a production deployment.

---

## 20. Key Takeaway

Flask provides a simple way to connect Python code with web requests.

The fundamental idea is:

    URL → Route → View Function → Response

This concept is the foundation for the Flask section of MAD 1.