# ⚡ Day 081 — User Authentication Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 081  
**Topic:** User Authentication  

---

## 🔹 Authentication

    Authentication = Who are you?

    Authorization = What can you access?

---

## 🔹 Password Hashing

Import:

    from werkzeug.security import generate_password_hash

Hash:

    password_hash = generate_password_hash(
        password
    )

Store:

    password_hash

Never store the original password.

---

## 🔹 Password Verification

    from werkzeug.security import check_password_hash

    valid = check_password_hash(
        stored_hash,
        entered_password
    )

Result:

    True  → Correct password
    False → Incorrect password

---

## 🔹 User Model

    class User(db.Model):

        id = db.Column(
            db.Integer,
            primary_key=True
        )

        email = db.Column(
            db.String(120),
            unique=True,
            nullable=False
        )

        password_hash = db.Column(
            db.String(255),
            nullable=False
        )

---

## 🔹 Flask Session

Import:

    from flask import session

Login state:

    session["user_id"] = user.id

Read:

    user_id = session.get("user_id")

Logout:

    session.pop("user_id", None)

---

## 🔹 Secret Key

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY"
    )

Do not expose production secret keys.

---

## 🔹 Manual Protected Route

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            return redirect(
                url_for("login")
            )

        return "Dashboard"

---

## 🔹 Flask-Login Installation

    pip install flask-login

---

## 🔹 Flask-Login Setup

    from flask_login import LoginManager

    login_manager = LoginManager()

    login_manager.init_app(app)

---

## 🔹 UserMixin

    from flask_login import UserMixin

    class User(UserMixin, db.Model):
        ...

---

## 🔹 Login

    from flask_login import login_user

    login_user(user)

---

## 🔹 Current User

    from flask_login import current_user

Check authentication:

    current_user.is_authenticated

User ID:

    current_user.id

---

## 🔹 Protected Route

    from flask_login import login_required

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return "Dashboard"

---

## 🔹 Logout

    from flask_login import logout_user

    @app.route("/logout")
    def logout():

        logout_user()

        return redirect(
            url_for("login")
        )

---

## 🔹 Registration Flow

    Form
      ↓
    Validate
      ↓
    Hash Password
      ↓
    Create User
      ↓
    Commit
      ↓
    Account Created

---

## 🔹 Login Flow

    Email + Password
          ↓
    Find User
          ↓
    Verify Password
          ↓
    Login User
          ↓
    Protected Access

---

## 🔹 Authentication Security

| Practice | Purpose |
|---|---|
| Password hashing | Protect stored passwords |
| HTTPS | Protect data in transit |
| Strong secret key | Protect Flask session signing |
| Input validation | Reject invalid data |
| CSRF protection | Protect state-changing requests |
| Rate limiting | Reduce brute-force attempts |
| Protected routes | Restrict private resources |
| Generic login errors | Reduce information leakage |

---

## ⭐ Most Important Functions

    generate_password_hash()
            ↓
       Create hash

    check_password_hash()
            ↓
      Verify password

    login_user()
            ↓
      Log user in

    logout_user()
            ↓
     Log user out

    login_required
            ↓
     Protect route

    current_user
            ↓
     Current user