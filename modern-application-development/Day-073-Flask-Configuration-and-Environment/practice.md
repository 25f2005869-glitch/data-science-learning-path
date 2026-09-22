# 📝 Day 073 — Flask Configuration and Environment Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 073  
**Topic:** Flask Configuration and Environment

---

# 🎯 Practice Objectives

Practice:

- `app.config`
- Configuration classes
- `from_mapping()`
- `from_object()`
- Environment variables
- `.env`
- `SECRET_KEY`
- Development configuration
- Production configuration
- Configuration security

---

# 🟢 Level 1 — Basic Questions

### Q1. What is Flask configuration?

### Q2. What is `app.config`?

### Q3. How can you read a configuration value?

### Q4. What is an environment variable?

### Q5. Why are environment variables useful?

### Q6. What is the purpose of `SECRET_KEY`?

### Q7. Why should real secrets not be hard-coded?

---

# 🟡 Level 2 — Code Practice

### Q8. Create a Flask application and configure:

- `DEBUG`
- `APP_NAME`
- `MAX_STUDENTS`

Use `app.config`.

### Q9. Create a configuration class containing:

- `DEBUG = False`
- `TESTING = False`
- `APP_NAME = "Student Portal"`

Load it using `from_object()`.

### Q10. Use `from_mapping()` to configure:

- Application name
- Testing mode
- Maximum content length

### Q11. Read a `SECRET_KEY` from an environment variable.

### Q12. Create a `.env` example containing:

- `SECRET_KEY`
- `DATABASE_URL`
- `APP_NAME`

Do not use real secrets.

---

# 🟠 Level 3 — Environment Practice

### Q13. Create three configuration classes:

- `DevelopmentConfig`
- `TestingConfig`
- `ProductionConfig`

Give each environment appropriate settings.

### Q14. Write code that raises `RuntimeError` if `SECRET_KEY` is missing.

### Q15. Create a `.gitignore` containing common Python and environment files.

---

# 🔴 Level 4 — Mini Challenge

## Student Portal Configuration System

Create a Flask application with separate configurations for:

- Development
- Testing
- Production

### Requirements

1. Create a base configuration.
2. Create development configuration.
3. Create testing configuration.
4. Create production configuration.
5. Read `SECRET_KEY` from an environment variable.
6. Keep `.env` out of Git.
7. Disable debug mode in production.
8. Display the application name on the home page.
9. Raise an error if required configuration is missing.

---

# 🧠 Revision Questions

1. What is configuration?
2. What does `app.config` do?
3. What is `from_mapping()`?
4. What is `from_object()`?
5. What is an environment variable?
6. Why use `.env`?
7. Why should `.env` usually be ignored by Git?
8. What is `SECRET_KEY`?
9. Why should debug mode be disabled in production?
10. Why separate development and production configuration?

---

# ✅ Self-Check

Before moving to Day 074, make sure you can:

- [ ] Explain Flask configuration.
- [ ] Use `app.config`.
- [ ] Use `from_mapping()`.
- [ ] Use `from_object()`.
- [ ] Create configuration classes.
- [ ] Read environment variables.
- [ ] Explain `.env`.
- [ ] Explain `SECRET_KEY`.
- [ ] Configure development and production.
- [ ] Protect sensitive configuration.