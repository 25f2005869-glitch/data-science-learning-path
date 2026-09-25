# 📚 Day 093 — Project Deployment Basics Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 093  
**Topic:** Project Deployment Basics  

---

# 1. What is Deployment?

Deployment is the process of making an application available for users outside the development environment.

During development:

    Developer
        ↓
    Local Computer
        ↓
    Flask Development Server
        ↓
    Browser

After deployment:

    User
        ↓
    Internet
        ↓
    Production Server
        ↓
    Flask Application
        ↓
    Database

---

# 2. Local Development vs Deployment

A local application may run at:

    http://127.0.0.1:5000

This address is normally accessible only from the local machine.

A deployed application is hosted on infrastructure that users can access over a network.

---

# 3. Development Environment

The development environment is used to build and test the application.

Typical characteristics:

- Debugging enabled when appropriate
- Development database
- Local environment variables
- Detailed error information
- Frequent code changes

Example:

    app.run(debug=True)

Debug mode should not be used as the production deployment configuration.

---

# 4. Production Environment

Production is the environment used by real users.

Important characteristics:

- Debug mode disabled
- Secure configuration
- Production server
- Proper logging
- HTTPS
- Production database
- Environment variables
- Monitoring
- Backups

---

# 5. Deployment Preparation

Before deployment:

    1. Test the application.
    2. Remove development-only settings.
    3. Protect secrets.
    4. Create requirements.txt.
    5. Configure environment variables.
    6. Configure the database.
    7. Configure the production server.
    8. Test production behavior.
    9. Configure HTTPS.
    10. Monitor the application.

---

# 6. Virtual Environment

A virtual environment isolates project dependencies.

Create one:

    python -m venv .venv

Activate on Windows:

    .venv\Scripts\activate

Activate on macOS/Linux:

    source .venv/bin/activate

Deactivate:

    deactivate

The virtual environment itself should normally not be committed to Git.

---

# 7. requirements.txt

`requirements.txt` records Python dependencies.

Example:

    Flask
    Flask-SQLAlchemy
    Werkzeug

Install dependencies:

    pip install -r requirements.txt

A more reproducible project usually records tested dependency versions.

Example:

    Flask==3.x.x

The exact versions should match the versions tested by the project.

---

# 8. Creating requirements.txt

A common command is:

    pip freeze > requirements.txt

This records installed packages and versions from the active environment.

Review the generated file before committing it.

---

# 9. Environment Variables

Environment variables store configuration outside the source code.

Examples:

    SECRET_KEY
    DATABASE_URL
    FLASK_ENV
    API_KEY

Python can read them using:

    import os

    secret_key = os.environ.get(
        "SECRET_KEY"
    )

---

# 10. Why Environment Variables?

Sensitive values should not be hard-coded in source code.

Avoid:

    SECRET_KEY = "my-real-secret"

Prefer:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY"
    )

This makes configuration safer and easier to change between environments.

---

# 11. `.env`

During local development, a `.env` file can store environment variables.

Example:

    SECRET_KEY=development-secret
    DATABASE_URL=sqlite:///app.db

The `.env` file should normally be excluded from Git when it contains secrets.

Example `.gitignore`:

    .env
    .venv/
    __pycache__/
    *.pyc

---

# 12. Never Commit Secrets

Do not commit:

    Passwords
    API keys
    Secret keys
    Database credentials
    Private tokens

If a real secret is accidentally exposed, it should be rotated/revoked and replaced.

---

# 13. Flask Configuration

A Flask application can load configuration from environment variables.

Example:

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY"
    )

Database:

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL"
    )

Configuration should be different for development, testing, and production when necessary.

---

# 14. WSGI

WSGI stands for:

    Web Server Gateway Interface

It defines a standard interface between Python web applications and web servers.

A Flask application can be served by a WSGI-compatible production server.

Conceptually:

    Web Server
        ↓
    WSGI Server
        ↓
    Flask Application

---

# 15. Development Server vs Production Server

Flask's development server is designed for development.

It is not intended to be the production serving solution.

Production deployments commonly use a dedicated WSGI server or a platform that provides equivalent production serving infrastructure.

---

# 16. Gunicorn

Gunicorn is a commonly used WSGI HTTP server for Python applications.

A conceptual command is:

    gunicorn app:app

Here:

    app.py
        ↓
    app

The first `app` refers to the Python module and the second `app` refers to the Flask application object.

The exact command depends on the project's structure.

---

# 17. Application Factory

Larger Flask projects may use an application factory.

Example:

    def create_app():
        app = Flask(__name__)

        return app

A WSGI entry point can then expose the application created by the factory.

This structure is useful for testing and different configurations.

---

# 18. Host and Port

A deployed application needs a network interface and port.

Development example:

    app.run(
        host="127.0.0.1",
        port=5000
    )

Production infrastructure typically manages the externally exposed port and routing.

Do not blindly expose development settings to production.

---

# 19. HTTPS

HTTPS encrypts communication between the client and server.

Production applications should use HTTPS.

Benefits include:

- Encryption
- Data integrity
- Protection against network interception
- Better protection for authentication sessions

HTTPS is especially important for login and other sensitive operations.

---

# 20. Database Deployment

A local Flask project may use SQLite:

    sqlite:///students.db

SQLite is useful for learning and smaller applications.

For production, database requirements depend on:

- Traffic
- Concurrent users
- Data size
- Reliability requirements
- Hosting platform

A managed relational database such as PostgreSQL may be appropriate for many production applications.

---

# 21. SQLite Deployment Considerations

SQLite is a file-based database.

This is convenient because:

- Easy setup
- No separate database server
- Simple backups
- Good for learning and small applications

However, production hosting environments may have filesystem persistence limitations or concurrency requirements that make a server-based database more appropriate.

---

# 22. Static Files

A Flask application may contain:

    static/
        css/
        js/
        images/

Templates:

    templates/
        base.html
        dashboard.html

The deployment environment must correctly serve or otherwise handle static assets.

---

# 23. Project Structure

A deployment-ready project might look like:

    project/
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes/
    │   ├── templates/
    │   └── static/
    ├── tests/
    ├── .gitignore
    ├── requirements.txt
    ├── .env
    └── run.py

The exact structure depends on the application.

---

# 24. Git and Deployment

Git helps track project code.

Typical workflow:

    Local Changes
        ↓
    Test
        ↓
    git add
        ↓
    git commit
        ↓
    git push
        ↓
    Deployment Platform
        ↓
    Production Application

Do not push secrets to the repository.

---

# 25. Health Check

A health endpoint can help determine whether an application is running.

Example:

    @app.route("/health")
    def health():
        return {"status": "ok"}

A monitoring system can request this endpoint.

---

# 26. Logging in Production

Production applications should use appropriate logging.

Useful information includes:

- Request errors
- Database failures
- Authentication failures
- Application warnings
- Unexpected exceptions

Do not log sensitive information such as passwords.

---

# 27. Error Handling in Production

Production users should not receive detailed internal tracebacks.

Instead, provide user-friendly error pages.

Example:

    404 → Page not found

    500 → Something went wrong

Detailed diagnostic information should remain in secure server-side logs.

---

# 28. Database Migrations

When a production application's database schema changes, manually changing tables can become difficult.

Migration tools help manage schema changes.

For Flask applications using SQLAlchemy, Flask-Migrate is a commonly used option.

Conceptually:

    Model Change
        ↓
    Migration
        ↓
    Database Schema Update

---

# 29. Deployment Configuration

Configuration may include:

    SECRET_KEY
    DATABASE_URL
    Debug setting
    Host
    Port
    Environment
    External service credentials

Configuration should be separated from application logic where practical.

---

# 30. Basic Deployment Checklist

Before deployment:

    ✓ Tests pass
    ✓ requirements.txt exists
    ✓ Secrets are protected
    ✓ Debug mode is disabled
    ✓ Production configuration exists
    ✓ Database is configured
    ✓ Static files work
    ✓ Error pages work
    ✓ Authentication works
    ✓ Authorization works
    ✓ HTTPS is configured
    ✓ Logs are available

---

# 31. Deployment Platforms

A Flask application can be deployed using different infrastructure options.

Examples include:

- Cloud application platforms
- Virtual machines
- Containers
- Managed hosting services
- Platform-as-a-Service solutions

The exact deployment commands depend on the selected platform.

---

# 32. Containers

Containers package an application and its dependencies into a consistent environment.

A common tool is Docker.

Conceptually:

    Application
       +
    Dependencies
       +
    Runtime
       ↓
    Container

Containers can improve consistency between development and deployment environments.

---

# 33. CI/CD Basics

CI/CD stands for:

    Continuous Integration
    Continuous Delivery / Deployment

A simple workflow:

    Push Code
       ↓
    Run Tests
       ↓
    Build
       ↓
    Deploy
       ↓
    Verify

CI/CD reduces manual deployment work.

---

# 34. Deployment Testing

After deployment, test:

    Home page
    Login
    Logout
    Dashboard
    CRUD
    Search
    Filtering
    Forms
    Validation
    Database
    Error pages
    Static files
    Mobile UI

Deployment is not complete until the deployed application itself has been verified.

---

# 35. Common Deployment Problems

### Problem 1

Missing dependency.

Solution:

    Check requirements.txt.

### Problem 2

Missing environment variable.

Solution:

    Check production configuration.

### Problem 3

Database connection failure.

Solution:

    Check DATABASE_URL and database availability.

### Problem 4

Static files not loading.

Solution:

    Check static configuration and deployment setup.

### Problem 5

Application crashes.

Solution:

    Inspect secure server logs.

### Problem 6

Works locally but fails after deployment.

Possible causes:

- Environment differences
- Missing dependency
- Wrong configuration
- Database differences
- File path assumptions
- Production server configuration

---

# 36. Security Checklist

Production application:

    ✓ HTTPS
    ✓ Secure SECRET_KEY
    ✓ Password hashing
    ✓ CSRF protection
    ✓ Input validation
    ✓ Authorization
    ✓ Secure cookies
    ✓ No debug mode
    ✓ No secrets in Git
    ✓ Safe error pages
    ✓ Dependency updates
    ✓ Secure database credentials

---

# 37. Deployment Workflow

A practical Flask deployment workflow:

    Develop
       ↓
    Test
       ↓
    Debug
       ↓
    Configure
       ↓
    Freeze Dependencies
       ↓
    Commit Code
       ↓
    Deploy
       ↓
    Run Production Tests
       ↓
    Monitor

---

# 38. Key Takeaway

Deployment is more than uploading code.

A production application needs:

    Code
      +
    Dependencies
      +
    Configuration
      +
    Database
      +
    Production Server
      +
    Security
      +
    Testing
      +
    Monitoring

The goal is to make the Flask application reliable, secure, and accessible to users.