# ⚡ Day 093 — Project Deployment Basics Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 093  
**Topic:** Project Deployment Basics  

---

## 🔹 Deployment

    Local Application
          ↓
    Production Environment
          ↓
    Users

---

## 🔹 Development

    Debugging
    Local Database
    Development Server

---

## 🔹 Production

    Debug OFF
    Secure Configuration
    Production Server
    HTTPS
    Logging
    Database
    Monitoring

---

## 🔹 Virtual Environment

    python -m venv .venv

Windows:

    .venv\Scripts\activate

macOS/Linux:

    source .venv/bin/activate

---

## 🔹 Dependencies

Create:

    requirements.txt

Install:

    pip install -r requirements.txt

---

## 🔹 Environment Variable

    import os

    SECRET_KEY = os.environ.get(
        "SECRET_KEY"
    )

---

## 🔹 `.gitignore`

    .env
    .venv/
    __pycache__/
    *.pyc

---

## 🔹 WSGI

    Web Server
        ↓
    WSGI Server
        ↓
    Flask

---

## 🔹 Gunicorn

Conceptual command:

    gunicorn app:app

---

## 🔹 Debug Mode

Development:

    app.run(debug=True)

Production:

    Debug OFF

---

## 🔹 HTTPS

    HTTP
      ↓
    HTTPS

Provides encrypted communication.

---

## 🔹 Database

Development:

    SQLite

Production choice depends on:

    Traffic
    Concurrency
    Data size
    Hosting
    Reliability

---

## 🔹 Health Check

    @app.route("/health")
    def health():
        return {"status": "ok"}

---

## 🔹 Logging

    app.logger.info()
    app.logger.warning()
    app.logger.error()

Never log passwords.

---

## 🔹 Deployment Flow

    Develop
      ↓
    Test
      ↓
    Configure
      ↓
    Commit
      ↓
    Deploy
      ↓
    Verify
      ↓
    Monitor

---

## 🔹 Security

    ✓ HTTPS
    ✓ Secret management
    ✓ Password hashing
    ✓ CSRF protection
    ✓ Validation
    ✓ Authorization
    ✓ Secure cookies
    ✓ Debug OFF
    ✓ No secrets in Git

---

## 🔹 CI/CD

    Push
      ↓
    Test
      ↓
    Build
      ↓
    Deploy
      ↓
    Verify

---

## 🔹 Final Rule

    Test → Secure → Deploy → Verify → Monitor