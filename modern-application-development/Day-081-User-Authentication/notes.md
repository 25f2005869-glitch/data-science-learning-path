# 📝 Day 081 — User Authentication

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 081  
**Topic:** User Authentication  

---

# 1. What is Authentication?

Authentication is the process of verifying **who a user is**.

For example, when a user logs into a website using:

    Email
    Password

the application verifies whether those credentials belong to a registered user.

Simple idea:

    User
      ↓
    Provides credentials
      ↓
    Application verifies credentials
      ↓
    User authenticated

---

# 2. What is Authorization?

Authorization determines **what an authenticated user is allowed to do**.

Example:

    Authentication:
    "Who are you?"

    Authorization:
    "What are you allowed to access?"

A user may successfully log in but still not have permission to access an administrator page.

---

# 3. Authentication vs Authorization

| Concept | Question |
|---|---|
| Authentication | Who are you? |
| Authorization | What can you access? |

Example:

    Login → Authentication

    Admin dashboard access → Authorization

---

# 4. Typical Authentication System

A basic web authentication system can contain:

    Registration
        ↓
    Password Hashing
        ↓
    Store User
        ↓
    Login
        ↓
    Verify Password
        ↓
    Create Session
        ↓
    Access Protected Pages
        ↓
    Logout

---

# 5. User Registration

Registration allows a new user to create an account.

Typical fields:

    Name
    Email
    Password

Example form:

    <form method="POST">

        <input
            type="email"
            name="email"
        >

        <input
            type="password"
            name="password"
        >

        <button type="submit">
            Register
        </button>

    </form>

The server receives the submitted data.

---

# 6. Never Store Plain-Text Passwords

A major security rule:

**Do not store user passwords as plain text.**

Bad approach:

    email: saloni@example.com
    password: mypassword123

If the database is compromised, the actual password is exposed.

Instead, store a password hash.

---

# 7. Password Hashing

Hashing converts a password into a one-way representation.

Conceptually:

    Password
        ↓
    Hash Function
        ↓
    Password Hash

Example:

    "mypassword123"

may become something similar to:

    $hash$....

The exact hash depends on the algorithm and parameters.

---

# 8. Hashing vs Encryption

These concepts are different.

### Hashing

Generally one-way.

    Password
       ↓
     Hash

The original password should not be recovered from the stored hash.

### Encryption

Designed to be reversible when the correct key is available.

    Plain Data
       ↓
    Encryption
       ↓
    Encrypted Data
       ↓
    Decryption
       ↓
    Plain Data

Passwords should normally be stored using password hashing, not reversible encryption.

---

# 9. Password Hashing in Flask

Werkzeug provides password hashing helpers.

Example:

    from werkzeug.security import generate_password_hash

    password_hash = generate_password_hash(
        password
    )

The resulting hash can be stored in the database.

---

# 10. Password Verification

During login, the user provides a password.

The application compares it with the stored password hash.

Use:

    from werkzeug.security import check_password_hash

    check_password_hash(
        stored_hash,
        entered_password
    )

It returns:

    True

if the password is correct.

Otherwise:

    False

---

# 11. Registration Flow

A registration process can work like this:

    User submits registration form
                ↓
        Validate input
                ↓
       Check existing email
                ↓
        Hash password
                ↓
        Create User object
                ↓
          Save database
                ↓
        Registration complete

---

# 12. User Model

A basic SQLAlchemy model might contain:

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

The database stores the hash, not the original password.

---

# 13. Login Flow

A login process can work like this:

    User enters email/password
                ↓
          Find user
                ↓
       User exists?
          ↓       ↓
         No      Yes
          ↓       ↓
        Error   Verify hash
                    ↓
              Password correct?
                 ↓       ↓
                No      Yes
                 ↓       ↓
               Error   Login
                          ↓
                       Session

---

# 14. Finding the User

Example:

    user = User.query.filter_by(
        email=email
    ).first()

With modern SQLAlchemy-style querying:

    statement = db.select(User).where(
        User.email == email
    )

    user = db.session.execute(
        statement
    ).scalar_one_or_none()

The exact approach depends on the Flask-SQLAlchemy/SQLAlchemy version and project style.

---

# 15. Verifying the Password

Example:

    if user and check_password_hash(
        user.password_hash,
        password
    ):
        print("Login successful")

Otherwise:

    print("Invalid email or password")

A generic login error is often preferable to revealing whether a particular email exists.

---

# 16. What is a Session?

A session can maintain information across multiple HTTP requests.

HTTP itself is stateless.

For example:

    Request 1 → Login
    Request 2 → Dashboard
    Request 3 → Profile

The application needs a mechanism to remember that the user has logged in.

A Flask session can help maintain login state.

---

# 17. Flask Session

Flask provides:

    from flask import session

Example:

    session["user_id"] = user.id

This stores an identifier associated with the authenticated user.

Later:

    user_id = session.get("user_id")

can be used to determine whether a user is logged in.

---

# 18. Secret Key

Flask sessions require a secret key.

Example:

    app.config["SECRET_KEY"] = "development-secret"

For real applications, do not hard-code a sensitive production secret in source code.

Use secure configuration such as an environment variable.

Example:

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY"
    )

---

# 19. Login State

A simple application can determine login state using:

    if "user_id" in session:
        print("User is logged in")

Otherwise:

    print("User is not logged in")

---

# 20. Protected Routes

A protected route is a route that requires authentication.

For example:

    /dashboard

should only be accessible to logged-in users.

Conceptual flow:

    Request /dashboard
            ↓
       User logged in?
          ↓     ↓
         Yes    No
          ↓     ↓
      Dashboard Login

---

# 21. Manual Route Protection

A simple Flask approach:

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            return redirect(
                url_for("login")
            )

        return "Dashboard"

This checks whether the user has a session identifier.

---

# 22. Flask-Login

For larger Flask applications, Flask-Login can simplify authentication-related session management.

Install:

    pip install flask-login

Typical components include:

    LoginManager
    UserMixin
    login_user()
    logout_user()
    login_required
    current_user

---

# 23. LoginManager

Example:

    from flask_login import LoginManager

    login_manager = LoginManager()

    login_manager.init_app(app)

It manages login state for the application.

---

# 24. UserMixin

A User model can use:

    from flask_login import UserMixin

Example:

    class User(UserMixin, db.Model):
        ...

`UserMixin` provides common Flask-Login user functionality.

---

# 25. `login_user()`

After successful authentication:

    login_user(user)

This tells Flask-Login that the user is authenticated.

---

# 26. `current_user`

Flask-Login provides:

    current_user

It represents the currently authenticated user.

Example:

    current_user.id

The user can also be checked:

    current_user.is_authenticated

---

# 27. `login_required`

A protected route can use:

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return "Dashboard"

Only authenticated users can access this route.

---

# 28. Logout

To log out with Flask-Login:

    from flask_login import logout_user

    @app.route("/logout")
    def logout():
        logout_user()

        return redirect(
            url_for("login")
        )

Logout removes the authenticated login state.

---

# 29. Manual Session Logout

If using Flask's session directly:

    session.pop("user_id", None)

This removes the user identifier from the session.

---

# 30. Authentication with Database

A typical architecture is:

    Browser
       ↓
    Flask
       ↓
    Authentication Logic
       ↓
    SQLAlchemy
       ↓
    User Table

Example User table:

    users
    --------------------------------
    id | email | password_hash
    --------------------------------
     1 | ...   | ...
     2 | ...   | ...

---

# 31. Complete Authentication Flow

### Registration

    Form
      ↓
    Validate
      ↓
    Hash Password
      ↓
    User Model
      ↓
    Database
      ↓
    Account Created

### Login

    Form
      ↓
    Find User
      ↓
    Verify Hash
      ↓
    Create Login State
      ↓
    Protected Access

### Logout

    Logout Request
          ↓
    Remove Login State
          ↓
    User Logged Out

---

# 32. Authentication and CRUD

User authentication commonly works together with database CRUD.

Registration:

    CREATE User

Login:

    READ User

Profile update:

    UPDATE User

Account deletion:

    DELETE User

Therefore, the CRUD knowledge from previous days is important.

---

# 33. Authentication vs User Management

Authentication is primarily about verifying identity.

User management may include:

- Registration
- Profile
- Password change
- Account deletion
- Roles
- Permissions
- Email verification
- Password reset

These are related but not exactly the same thing.

---

# 34. Security Best Practices

### 1. Hash passwords

Never store plain-text passwords.

### 2. Use HTTPS

Credentials should be transmitted over HTTPS in production.

### 3. Use strong secret keys

Do not expose Flask's production secret key.

### 4. Validate input

Validate email and other user input.

### 5. Avoid revealing account existence

Prefer:

    Invalid email or password

over detailed login errors that reveal whether an email is registered.

### 6. Protect sensitive routes

Use authentication checks.

### 7. Use secure session configuration

Configure cookies appropriately for production.

### 8. Use CSRF protection

State-changing forms should have appropriate CSRF protection.

### 9. Rate-limit authentication attempts

This can help reduce brute-force attacks.

### 10. Never log passwords

Passwords should never appear in application logs.

---

# 35. Authentication vs Authorization Example

Suppose Saloni logs into a student portal.

Authentication:

    Email + Password
           ↓
    Identity verified

Authorization:

    Student role
           ↓
    Student dashboard allowed

An administrator may have:

    Admin role
           ↓
    Admin dashboard allowed

---

# 36. Common Mistakes

## Mistake 1 — Plain-text passwords

Never store:

    password = "mypassword"

in the database.

---

## Mistake 2 — Comparing hashes incorrectly

Use a password verification function such as:

    check_password_hash()

Do not simply compare a newly generated salted password hash as a plain string to the stored hash.

---

## Mistake 3 — Missing secret key

Flask session functionality requires appropriate secret-key configuration.

---

## Mistake 4 — Forgetting route protection

A dashboard containing private information should not be publicly accessible.

---

## Mistake 5 — Trusting the browser

Authentication decisions must be made on the server.

---

# 37. Important Mental Model

Remember:

    Registration
         ↓
    Hash Password
         ↓
    Store User
         ↓
    Login
         ↓
    Find User
         ↓
    Verify Password
         ↓
    Create Session
         ↓
    Protected Routes
         ↓
    Logout

---

# 38. Key Takeaways

- Authentication verifies identity.
- Authorization controls permissions.
- Passwords should be hashed.
- Never store plain-text passwords.
- `generate_password_hash()` creates a password hash.
- `check_password_hash()` verifies a password.
- Flask sessions can maintain login state.
- `SECRET_KEY` is important for Flask sessions.
- Flask-Login provides convenient authentication helpers.
- `login_required` protects routes.
- `current_user` represents the logged-in user.
- `logout_user()` logs the user out.

---

# ⭐ Final Summary

A secure basic authentication system follows:

    Register
       ↓
    Validate
       ↓
    Hash Password
       ↓
    Save User
       ↓
    Login
       ↓
    Verify Password
       ↓
    Create Session
       ↓
    Access Protected Routes
       ↓
    Logout

This is the foundation for authentication in Flask-based web applications.