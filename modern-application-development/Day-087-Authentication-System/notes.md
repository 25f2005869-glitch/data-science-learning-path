# 🔐 Day 087 — Authentication System — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 087  
**Topic:** Authentication System

---

# 1. What Is Authentication?

Authentication is the process of verifying the identity of a user.

The basic question is:

    "Who are you?"

Examples:

- Login with email and password
- Login with username and password
- Multi-factor authentication

---

# 2. What Is Authorization?

Authorization determines what an authenticated user is allowed to do.

The question is:

    "What are you allowed to do?"

Example:

    Student → View own profile

    Admin → Manage all students

Authentication and authorization are different concepts.

---

# 3. Authentication Flow

A typical authentication system works like this:

    Register
       ↓
    Store User
       ↓
    Login
       ↓
    Verify Credentials
       ↓
    Create Session
       ↓
    Access Protected Pages
       ↓
    Logout

---

# 4. User Registration

Registration creates a new user account.

Typical fields:

    username
    email
    password

The application should validate these fields before creating the account.

---

# 5. Registration Validation

Example rules:

- Username is required.
- Email is required.
- Email should have an appropriate format.
- Password should meet minimum security requirements.
- Username/email should be unique where required.

Validation must happen on the server.

---

# 6. Never Store Plaintext Passwords

Never store:

    password = "mypassword123"

in the database as plaintext.

Instead, store a password hash.

Example:

    password_hash = generate_password_hash(password)

---

# 7. Password Hashing

Hashing transforms a password into a one-way representation.

Example:

    from werkzeug.security import generate_password_hash

    password_hash = generate_password_hash(password)

The original password is not stored directly.

A password hash is designed for password verification rather than for recovering the original password.

---

# 8. Password Verification

During login, the submitted password must be checked against the stored hash.

Example:

    from werkzeug.security import check_password_hash

    valid = check_password_hash(
        stored_hash,
        submitted_password
    )

If the result is true, the credentials are valid.

---

# 9. Hashing vs Encryption

Hashing:

    Password
       ↓
    Hash

It is intended to be one-way.

Encryption:

    Data
       ↓
    Encrypted Data
       ↓
    Decryption
       ↓
    Original Data

Passwords should normally be stored using a password hashing function, not reversible encryption.

---

# 10. User Model

A user table can contain:

    id
    username
    email
    password_hash
    role

Example SQLAlchemy model:

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password_hash = db.Column(db.String(255), nullable=False)
        role = db.Column(db.String(20), nullable=False, default="student")

---

# 11. Registration Workflow

    User enters registration form
             ↓
    Flask receives POST
             ↓
    Validate input
             ↓
    Check uniqueness
             ↓
    Hash password
             ↓
    Create User object
             ↓
    Commit database transaction
             ↓
    Flash success
             ↓
    Redirect to login

---

# 12. Login

Login verifies an existing user's credentials.

Typical flow:

    Email/Username
          +
    Password
          ↓
    Find User
          ↓
    Verify Password
          ↓
    Create Session
          ↓
    Dashboard

---

# 13. Login Example

Conceptual Flask code:

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(
        user.password_hash,
        password
    ):
        session["user_id"] = user.id
        session["role"] = user.role

        flash("Login successful.", "success")
        return redirect(url_for("dashboard"))

    flash("Invalid email or password.", "error")

For modern SQLAlchemy usage, the query can also be constructed with `select()`.

---

# 14. Generic Login Errors

Avoid messages such as:

    "Email exists but password is incorrect."

This can reveal whether an account exists.

A safer user-facing message is:

    "Invalid email or password."

---

# 15. Flask Session

Flask sessions can remember information between requests.

Example:

    session["user_id"] = user.id

Later:

    user_id = session.get("user_id")

The session can be used to determine whether a user is logged in.

---

# 16. SECRET_KEY

Flask requires a secret key for securely signing its session data.

Example:

    app.config["SECRET_KEY"] = "strong-secret"

For production:

- Use a strong random value.
- Keep it outside source control.
- Prefer environment-based configuration.

---

# 17. Logout

Logout removes the authentication information from the session.

Example:

    session.clear()

Then:

    flash("Logged out successfully.", "success")
    return redirect(url_for("login"))

Only clear the session if the application intends to remove all session data.

---

# 18. Protected Routes

A protected route should only be accessible to authenticated users.

Example:

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            flash("Please log in first.", "error")
            return redirect(url_for("login"))

        return render_template("dashboard.html")

---

# 19. Authentication Decorator

Instead of repeating authentication logic, create a decorator.

Conceptually:

    @login_required
    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

The exact decorator implementation depends on whether the application uses Flask-Login or a custom session system.

---

# 20. Flask-Login

Flask-Login is a popular extension for managing user sessions.

Common components include:

    LoginManager
    UserMixin
    login_user()
    logout_user()
    login_required
    current_user

---

# 21. Flask-Login Setup

Conceptual setup:

    from flask_login import LoginManager

    login_manager = LoginManager()
    login_manager.init_app(app)

Then configure the login view as appropriate for the application.

---

# 22. User Model with Flask-Login

A model can inherit from `UserMixin`.

Example:

    from flask_login import UserMixin

    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(
            db.String(120),
            unique=True,
            nullable=False
        )
        password_hash = db.Column(
            db.String(255),
            nullable=False
        )

`UserMixin` provides common methods and properties expected by Flask-Login.

---

# 23. User Loader

Flask-Login needs a way to load a user from the stored user ID.

Conceptual example:

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

---

# 24. Login with Flask-Login

After verifying credentials:

    login_user(user)

Then redirect:

    return redirect(url_for("dashboard"))

---

# 25. Logout with Flask-Login

Example:

    logout_user()

Then:

    return redirect(url_for("login"))

---

# 26. Protected Route with Flask-Login

Example:

    @login_required
    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

The route requires an authenticated user.

---

# 27. Current User

Flask-Login provides:

    current_user

It represents the currently authenticated user.

Example:

    current_user.email

---

# 28. Role-Based Authorization

Suppose users have:

    student
    admin

A student should not automatically receive administrator permissions.

Example conceptual check:

    if current_user.role != "admin":
        abort(403)

Authentication establishes identity.

Authorization checks permissions.

---

# 29. Registration Security

During registration:

1. Validate input.
2. Normalize appropriate values.
3. Check uniqueness.
4. Hash the password.
5. Store only the hash.
6. Commit the database transaction.
7. Provide user feedback.

---

# 30. Login Security

During login:

- Validate input.
- Look up the user.
- Verify the password hash.
- Use generic failure messages.
- Establish a secure authenticated session.
- Consider rate limiting or account protection.
- Do not log passwords.

---

# 31. Session Security

Authentication sessions should be protected.

Important considerations include:

- Strong secret key
- HTTPS in production
- Secure cookie settings
- Appropriate `HttpOnly`
- Appropriate `SameSite`
- Session expiration policies
- Session fixation protection

Exact settings depend on the deployment environment.

---

# 32. CSRF Protection

State-changing browser forms should be protected against Cross-Site Request Forgery.

Examples:

- Login-related state changes
- Profile updates
- Student creation
- Student deletion

A Flask application can use an appropriate CSRF protection extension or framework integration.

---

# 33. Authentication vs Session

Authentication:

    Verifies identity.

Session:

    Helps maintain login state across requests.

They work together but are not identical concepts.

---

# 34. Authentication vs Authorization

| Concept | Question |
|---|---|
| Authentication | Who are you? |
| Authorization | What can you access? |

Example:

    Login → Authentication

    Admin-only delete → Authorization

---

# 35. Complete Authentication Architecture

    Registration
          ↓
    User Database
          ↓
    Login
          ↓
    Password Verification
          ↓
    Authentication Session
          ↓
    Protected Route
          ↓
    Authorization
          ↓
    Resource

---

# 36. Common Mistakes

### Mistake 1

Storing plaintext passwords.

### Mistake 2

Using a weak or exposed secret key.

### Mistake 3

Trusting client-side validation.

### Mistake 4

Protecting the page but not the underlying operation.

### Mistake 5

Confusing authentication with authorization.

### Mistake 6

Returning detailed login errors.

### Mistake 7

Not handling duplicate usernames/emails.

### Mistake 8

Logging passwords.

---

# 37. Authentication Checklist

    [ ] Registration
    [ ] Server-side validation
    [ ] Password hashing
    [ ] Unique username/email
    [ ] Login
    [ ] Password verification
    [ ] Session
    [ ] Protected routes
    [ ] Logout
    [ ] Authorization
    [ ] CSRF protection
    [ ] Secure configuration
    [ ] Generic authentication errors
    [ ] HTTPS in production

---

# 38. Key Takeaway

A secure authentication system follows:

    Register
       ↓
    Validate
       ↓
    Hash Password
       ↓
    Store User
       ↓
    Login
       ↓
    Verify Hash
       ↓
    Create Session
       ↓
    Protect Routes
       ↓
    Authorize Actions
       ↓
    Logout

Authentication is not just a login form.

It is a complete security workflow.