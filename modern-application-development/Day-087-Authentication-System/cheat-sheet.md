# 🔐 Day 087 — Authentication System — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 087  
**Topic:** Authentication System

---

## 1. Authentication

    "Who are you?"

Verifies user identity.

---

## 2. Authorization

    "What are you allowed to do?"

Controls permissions.

---

## 3. Password Hashing

    from werkzeug.security import generate_password_hash

    password_hash = generate_password_hash(password)

---

## 4. Password Verification

    from werkzeug.security import check_password_hash

    check_password_hash(
        stored_hash,
        submitted_password
    )

---

## 5. Never Store

    password = "mypassword123"

Never store plaintext passwords.

Store:

    password_hash

---

## 6. User Model

    id
    username
    email
    password_hash
    role

---

## 7. Flask Session

    session["user_id"] = user.id

Read:

    user_id = session.get("user_id")

---

## 8. SECRET_KEY

    app.config["SECRET_KEY"] = "strong-secret"

Keep production secrets outside source control.

---

## 9. Logout

Custom session approach:

    session.clear()

Flask-Login:

    logout_user()

---

## 10. Login

Concept:

    Find User
       ↓
    Check Password
       ↓
    Create Session
       ↓
    Redirect

---

## 11. Protected Route

Concept:

    if "user_id" not in session:
        return redirect(url_for("login"))

---

## 12. Flask-Login

Important components:

    LoginManager
    UserMixin
    login_user()
    logout_user()
    login_required
    current_user

---

## 13. Flask-Login Setup

    login_manager = LoginManager()
    login_manager.init_app(app)

---

## 14. User Loader

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

---

## 15. Login

    login_user(user)

---

## 16. Protected Route

    @login_required
    @app.route("/dashboard")
    def dashboard():
        ...

---

## 17. Current User

    current_user

Example:

    current_user.email

---

## 18. Role Check

    if current_user.role != "admin":
        abort(403)

---

## 19. Authentication Flow

    Register
       ↓
    Hash Password
       ↓
    Store User
       ↓
    Login
       ↓
    Verify Hash
       ↓
    Session
       ↓
    Protected Route

---

## 20. Security

    Password hashing
    HTTPS
    Strong SECRET_KEY
    CSRF protection
    Server-side validation
    Generic login errors
    Rate limiting
    Secure session cookies
    Authorization

---

## 21. Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Who are you? | What can you do? |
| Login | Permission |
| Identity | Access control |

---

## ⭐ Remember

**Hash passwords.**

**Never store plaintext passwords.**

**Authenticate first. Authorize second.**

**Protect server-side operations, not just UI pages.**