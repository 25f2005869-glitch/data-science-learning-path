# ⚡ Day 073 — Flask Configuration and Environment Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 073  
**Topic:** Flask Configuration and Environment

---

## 🔹 Flask Configuration

    app.config["DEBUG"] = True

Read:

    app.config["DEBUG"]

---

## 🔹 `from_mapping()`

    app.config.from_mapping(
        DEBUG=True,
        APP_NAME="Student Portal"
    )

Useful for loading multiple values.

---

## 🔹 Configuration Class

    class Config:
        DEBUG = False
        APP_NAME = "Student Portal"

Load it:

    app.config.from_object(Config)

---

## 🔹 Environment Variable

    import os

    secret_key = os.environ.get("SECRET_KEY")

---

## 🔹 Environment Variable with Default

    value = os.environ.get(
        "APP_NAME",
        "Student Portal"
    )

Do not use weak defaults for real production secrets.

---

## 🔹 `.env`

Example:

    SECRET_KEY=development-secret
    DATABASE_URL=sqlite:///students.db

Keep sensitive `.env` files out of version control.

---

## 🔹 python-dotenv

Install:

    pip install python-dotenv

Use environment variables through:

    import os

    value = os.environ.get("SECRET_KEY")

---

## 🔹 SECRET_KEY

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

Used by Flask security-related features such as signed session data.

Keep it secret.

---

## 🔹 `.gitignore`

    .env
    .venv/
    __pycache__/
    *.pyc

---

## 🔹 Development Configuration

    class DevelopmentConfig:
        DEBUG = True
        TESTING = False

---

## 🔹 Production Configuration

    class ProductionConfig:
        DEBUG = False
        TESTING = False

---

## 🔹 Testing Configuration

    class TestingConfig:
        TESTING = True
        DEBUG = False

---

## 🔹 Application Factory

    def create_app():
        app = Flask(__name__)
        app.config.from_object(Config)
        return app

---

## 🔹 Required Configuration Check

    secret_key = os.environ.get("SECRET_KEY")

    if not secret_key:
        raise RuntimeError(
            "SECRET_KEY is not configured"
        )

---

## 🔐 Security Rules

- Never commit real passwords.
- Never expose API keys.
- Keep secrets outside source code.
- Use environment variables.
- Protect `.env`.
- Disable production debug mode.
- Do not print secrets in logs.
- Use strong secret keys.

---

## ⭐ Remember

`app.config` → Flask configuration object

`from_mapping()` → Load configuration values

`from_object()` → Load from a Python object/class

`os.environ.get()` → Read environment variable

`.env` → Local development environment file

`SECRET_KEY` → Important Flask secret configuration

`DEBUG=True` → Development only