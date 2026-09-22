# 📚 Day 073 — Flask Configuration and Environment

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 073  
**Topic:** Flask Configuration and Environment

---

## 1. What Is Configuration?

Configuration means the settings that control how an application behaves.

Examples include:

- Debug mode
- Secret keys
- Database URL
- Testing mode
- Session settings
- File upload limits
- External service configuration

Instead of writing these values directly throughout the application, configuration keeps them organized.

---

## 2. Flask Configuration

Flask provides a configuration object through:

    app.config

It behaves similarly to a dictionary.

Example:

    from flask import Flask

    app = Flask(__name__)

    app.config["DEBUG"] = True
    app.config["APP_NAME"] = "Student Portal"

---

## 3. Reading Configuration

A configuration value can be accessed using its key.

Example:

    app.config["APP_NAME"]

Inside a route:

    @app.route("/")
    def home():
        return app.config["APP_NAME"]

---

## 4. `from_mapping()`

`from_mapping()` allows multiple configuration values to be loaded.

Example:

    app.config.from_mapping(
        DEBUG=True,
        APP_NAME="Student Portal",
        MAX_STUDENTS=100
    )

This is useful when configuration values are known directly in Python.

---

## 5. Configuration Class

A common approach is to create configuration classes.

Example:

    class Config:
        APP_NAME = "Student Portal"
        DEBUG = False

Then:

    app.config.from_object(Config)

This keeps configuration separate from application logic.

---

## 6. Development Configuration

Development configuration is designed for local development.

Example:

    class DevelopmentConfig:
        DEBUG = True
        TESTING = False

Development can provide:

- Debugging
- Automatic reloading
- Detailed development information

---

## 7. Production Configuration

Production configuration is used when the application is deployed.

Example:

    class ProductionConfig:
        DEBUG = False
        TESTING = False

Production should prioritize:

- Security
- Reliability
- Performance
- Safe error handling

---

## 8. Testing Configuration

A separate testing configuration can be useful.

Example:

    class TestingConfig:
        TESTING = True
        DEBUG = False

This allows application behavior to be controlled specifically for tests.

---

## 9. Environment Variables

Environment variables are values provided by the operating system or execution environment.

Examples:

    SECRET_KEY
    DATABASE_URL
    FLASK_ENV

Environment variables are useful for values that should not be hard-coded.

---

## 10. Reading Environment Variables in Python

Python provides the `os` module.

Example:

    import os

    secret_key = os.environ.get("SECRET_KEY")

A default value can also be provided:

    secret_key = os.environ.get(
        "SECRET_KEY",
        "development-key"
    )

For production secrets, a secure environment variable should be provided rather than relying on a weak default.

---

## 11. Why Use Environment Variables?

Environment variables allow the same application code to work in different environments.

For example:

    Development
        ↓
    Local database

    Production
        ↓
    Production database

The application code does not need to be rewritten.

---

## 12. `.env` Files

A `.env` file can be used during local development to store environment variables.

Example:

    SECRET_KEY=development-secret
    DATABASE_URL=sqlite:///students.db

The `.env` file should generally NOT be committed to Git when it contains secrets.

---

## 13. `python-dotenv`

Flask commonly works with environment variables and can use `python-dotenv` for loading variables from `.env` files during development.

Installation:

    pip install python-dotenv

A `.env` file may contain:

    SECRET_KEY=my-development-secret

The application can then read:

    import os

    secret_key = os.environ.get("SECRET_KEY")

---

## 14. `SECRET_KEY`

`SECRET_KEY` is an important Flask configuration value.

Example:

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

It is used by Flask features such as securely signing session-related data.

The secret should:

- Be difficult to guess.
- Be kept private.
- Not be committed to a public repository.
- Be different across environments when appropriate.

---

## 15. Never Hard-Code Real Secrets

Avoid storing real credentials directly in source code.

Bad practice:

    DATABASE_PASSWORD = "my-real-password"

Better approach:

    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

This keeps sensitive configuration outside the source code.

---

## 16. `.gitignore`

A `.gitignore` file can prevent sensitive local files from being committed.

Example:

    .env
    .venv/
    __pycache__/
    *.pyc

This is especially important when using Git and GitHub.

---

## 17. Configuration and Application Factory

Larger Flask applications often use an application factory.

Example:

    def create_app():
        app = Flask(__name__)

        app.config.from_object(Config)

        return app

This makes it easier to create applications with different configurations.

---

## 18. Configuration Order

Configuration values can be loaded from different sources.

A simplified approach is:

    Default configuration
            ↓
    Python configuration
            ↓
    Environment-specific configuration
            ↓
    Environment variables
            ↓
    Final application configuration

The exact loading strategy depends on the application's design.

---

## 19. Configuration in Templates

Configuration values can be made available to templates.

For example, a route can pass configuration:

    @app.route("/")
    def home():
        return render_template(
            "index.html",
            app_name=app.config["APP_NAME"]
        )

The template can then display the value.

---

## 20. Common Configuration Values

Some commonly encountered Flask configuration keys include:

| Key | Purpose |
|---|---|
| `DEBUG` | Development debugging |
| `TESTING` | Testing mode |
| `SECRET_KEY` | Secret used by Flask security-related features |
| `SESSION_COOKIE_NAME` | Session cookie name |
| `MAX_CONTENT_LENGTH` | Maximum request content size |
| `APPLICATION_ROOT` | Application root path |

---

## 21. Debug Configuration

During development, debug mode can be enabled.

Example:

    app.config["DEBUG"] = True

However, debug mode should never be exposed to untrusted users in production.

---

## 22. Configuration vs Code

Configuration answers:

> "How should the application behave?"

Application code answers:

> "What should the application do?"

Keeping these responsibilities separate makes applications easier to maintain.

---

## 23. Security Best Practices

- Never commit real secrets.
- Use environment variables for sensitive values.
- Keep `.env` out of Git when appropriate.
- Use strong secret keys.
- Disable debug mode in production.
- Use different configurations for different environments.
- Avoid printing secrets in logs.
- Validate required environment variables.
- Rotate compromised secrets.

---

## 24. Missing Environment Variables

Applications should detect required configuration early.

Example:

    secret_key = os.environ.get("SECRET_KEY")

    if not secret_key:
        raise RuntimeError("SECRET_KEY is not configured")

This is better than allowing the application to fail later in an unexpected way.

---

## 25. Development and Production

| Development | Production |
|---|---|
| Debug enabled when needed | Debug disabled |
| Local database | Production database |
| Development secrets | Secure production secrets |
| Detailed debugging | Safe error pages |
| Local configuration | Deployment configuration |

---

## 26. Configuration Flow

A simple mental model:

    Environment
          ↓
    Configuration
          ↓
    Flask Application
          ↓
    Routes / Extensions / Templates
          ↓
    Response

---

## 27. Common Mistakes

### Mistake 1 — Hard-Coding Secrets

Do not put passwords or real API keys in source code.

### Mistake 2 — Committing `.env`

Do not accidentally upload secret configuration to GitHub.

### Mistake 3 — Production Debug Mode

Do not run a public production application with debug mode enabled.

### Mistake 4 — One Configuration for Everything

Development, testing, and production often need different settings.

### Mistake 5 — Weak Secret Keys

Use strong, unpredictable secret values.

---

## 28. Best Practices

- Keep configuration organized.
- Use environment variables for deployment-specific values.
- Separate development and production settings.
- Protect secrets.
- Use `.gitignore`.
- Validate required configuration.
- Keep configuration names descriptive.
- Avoid unnecessary configuration values.
- Never expose secrets in responses or logs.

---

## ⭐ Key Takeaway

Flask configuration controls how an application behaves.

The most important concepts are:

- `app.config`
- `from_mapping()`
- `from_object()`
- Configuration classes
- Environment variables
- `.env`
- `SECRET_KEY`
- Development configuration
- Production configuration
- Secure secret management

Good configuration management makes Flask applications portable, maintainable, and safer.