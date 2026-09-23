# 📝 Day 082 — Sessions and Cookies

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 082  
**Topic:** Sessions and Cookies  

---

# 1. Why Do We Need Sessions and Cookies?

HTTP is fundamentally **stateless**.

Suppose a user makes three requests:

    Request 1 → Login
    Request 2 → Dashboard
    Request 3 → Profile

The server does not automatically know that all three requests belong to the same logged-in user.

Sessions and cookies provide mechanisms for maintaining state.

---

# 2. What Does Stateless Mean?

Stateless means that each HTTP request is treated independently.

Example:

    Request 1
        ↓
      Server
        ↓
    Response 1

    Request 2
        ↓
      Server
        ↓
    Response 2

The server does not automatically retain the complete context of Request 1 when processing Request 2.

Applications therefore use additional mechanisms to maintain state.

---

# 3. What is a Session?

A session is a mechanism used by a web application to maintain information associated with a user's interaction across requests.

Typical session information may include:

    user_id
    login status
    preferences
    temporary workflow data

For example:

    Login
      ↓
    user_id stored in session
      ↓
    Dashboard
      ↓
    Application knows which user is logged in

---

# 4. Flask Session

Flask provides a session object:

    from flask import session

Example:

    session["user_id"] = 101

Now the application can retrieve it in a later request.

    user_id = session.get("user_id")

---

# 5. Flask Secret Key

Flask's default session mechanism uses a secret key to cryptographically sign session data.

Example:

    app.config["SECRET_KEY"] = "development-secret"

For production, use a strong secret value and keep it outside source code.

Example:

    import os

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY"
    )

---

# 6. Setting Session Data

Example:

    session["username"] = "Saloni"

Another value:

    session["user_id"] = 101

Multiple session values can exist at the same time.

Example:

    session["username"] = "Saloni"
    session["course"] = "Data Science"

---

# 7. Reading Session Data

Use dictionary-style access:

    username = session["username"]

Or safer access:

    username = session.get("username")

`get()` returns `None` if the key does not exist.

---

# 8. Why Use `session.get()`?

Consider:

    username = session["username"]

If the key does not exist, accessing it directly can raise an error.

Instead:

    username = session.get("username")

If the key does not exist:

    username → None

You can then check:

    if username is None:
        print("User not logged in")

---

# 9. Removing One Session Value

Use:

    session.pop("username", None)

This removes the `username` value.

The second argument prevents an error if the key does not exist.

---

# 10. Clearing the Session

Use:

    session.clear()

This removes all session data.

Example:

    session.clear()

This is commonly useful during logout when the application uses the Flask session directly.

---

# 11. Session Authentication Example

A simple login flow can be:

    if valid_credentials:
        session["user_id"] = user.id

Later:

    user_id = session.get("user_id")

If there is no user ID:

    if "user_id" not in session:
        redirect to login

---

# 12. Protected Route Using Session

Example:

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            return redirect(
                url_for("login")
            )

        return "Dashboard"

The route checks whether the user has a login session.

---

# 13. Logout Using Flask Session

Example:

    @app.route("/logout")
    def logout():

        session.pop("user_id", None)

        return redirect(
            url_for("login")
        )

For applications where the session contains only authentication state, `session.clear()` may also be appropriate.

---

# 14. What is a Cookie?

A cookie is a small piece of data stored by a browser for a website.

Cookies can be sent with subsequent HTTP requests to the relevant website.

Conceptually:

    Server
       ↓
    Set-Cookie
       ↓
    Browser
       ↓
    Stores Cookie
       ↓
    Later Request
       ↓
    Cookie sent to Server

---

# 15. Why Are Cookies Used?

Cookies can be used for:

- Session identifiers
- Preferences
- Remembering choices
- Analytics
- Authentication-related mechanisms
- Shopping-cart identifiers

The exact use depends on the application.

---

# 16. Setting a Cookie in Flask

Flask can set cookies on a response.

Example:

    from flask import make_response

    response = make_response("Cookie set")

    response.set_cookie(
        "username",
        "Saloni"
    )

    return response

The browser stores the cookie according to the cookie attributes.

---

# 17. Reading a Cookie

Use:

    from flask import request

    username = request.cookies.get(
        "username"
    )

If the cookie does not exist:

    username → None

---

# 18. Deleting a Cookie

Use `delete_cookie()` on a response.

Example:

    response = make_response(
        "Cookie deleted"
    )

    response.delete_cookie(
        "username"
    )

    return response

The browser will receive an instruction to remove the cookie.

---

# 19. Cookie Attributes

Important cookie attributes include:

- `expires`
- `max_age`
- `domain`
- `path`
- `secure`
- `httponly`
- `samesite`

These attributes affect cookie lifetime, scope and security.

---

# 20. `max_age`

`max_age` specifies how long the cookie should remain valid in seconds.

Example:

    response.set_cookie(
        "theme",
        "dark",
        max_age=3600
    )

The cookie is configured to last for approximately one hour.

---

# 21. `expires`

`expires` specifies a date/time after which the cookie should no longer be considered valid.

It can be used when a specific expiration time is needed.

---

# 22. `path`

The `path` attribute controls which URL paths receive the cookie.

Example:

    response.set_cookie(
        "preference",
        "dark",
        path="/"
    )

A root path generally makes the cookie available to the site's paths under that scope.

---

# 23. `secure`

A cookie with:

    secure=True

is sent by the browser only over HTTPS.

This is important for production applications.

---

# 24. `httponly`

A cookie with:

    httponly=True

cannot normally be read by JavaScript through `document.cookie`.

This can reduce exposure to some client-side script attacks.

It does not make a cookie completely immune to attacks.

---

# 25. `samesite`

The `SameSite` attribute controls when browsers send cookies in cross-site contexts.

Common values include:

    Strict
    Lax
    None

For `SameSite=None`, browsers generally require:

    Secure

This setting is important for controlling cross-site cookie behavior.

---

# 26. Session Cookie vs Persistent Cookie

### Session Cookie

A cookie without a persistent expiration configuration is generally treated as a session cookie.

It is typically removed when the browser session ends, subject to browser behavior.

### Persistent Cookie

A cookie with an expiration or `max_age` can persist beyond the current browser session.

Example:

    max_age=86400

means approximately one day.

---

# 27. Sessions vs Cookies

| Feature | Session | Cookie |
|---|---|---|
| Purpose | Maintain application state | Store/send small browser data |
| Location | Depends on session implementation | Browser |
| Sent with requests | Session identifier or session data depending on implementation | Matching cookies are sent |
| Size | Depends on implementation | Limited |
| Common use | Login state | Preferences/session identifiers |
| Security | Depends on implementation | Requires secure attributes and careful data choices |

---

# 28. Important Flask Session Detail

Flask's default session implementation is **cookie-based**.

This is important.

When you write:

    session["user_id"] = 101

Flask normally serializes and signs the session data into a cookie rather than automatically storing the session data in a server-side session database.

Therefore:

- Do not store sensitive secrets directly in the Flask session.
- Keep the secret key secure.
- Use an appropriate server-side session solution when your application's requirements call for it.

---

# 29. Signed Does Not Mean Encrypted

Flask's default session cookie is cryptographically signed.

Signing helps detect tampering.

It does not mean that arbitrary session contents should be treated as confidential encrypted storage.

Therefore, do not put passwords, API keys or other sensitive secrets into the session.

---

# 30. Session and Cookie Authentication

A common authentication design is:

    User Login
        ↓
    Server verifies password
        ↓
    Login state created
        ↓
    Browser receives session cookie
        ↓
    Browser sends cookie with later requests
        ↓
    Application identifies session/user
        ↓
    Protected resource

The exact mechanism depends on the authentication library and session configuration.

---

# 31. Cookie vs Local Storage

Cookies and `localStorage` are different.

### Cookies

- Automatically sent with matching HTTP requests.
- Can use `HttpOnly`.
- Have attributes such as `Secure` and `SameSite`.

### localStorage

- Accessible through JavaScript.
- Not automatically included in HTTP requests.
- Does not support the `HttpOnly` cookie protection mechanism.

Sensitive authentication designs should be chosen carefully rather than simply storing tokens in browser-accessible storage.

---

# 32. Session vs localStorage

### Session

Used by the server/application to maintain request-to-request state.

### localStorage

Browser-side storage controlled through JavaScript.

Example:

    localStorage.setItem(
        "theme",
        "dark"
    )

These mechanisms solve different problems.

---

# 33. Cookie Security

Cookies can contain or reference important information.

Security practices include:

### Use HTTPS

Protect data during transmission.

### Use Secure

For sensitive cookies in HTTPS deployments:

    secure=True

### Use HttpOnly

For cookies that do not need JavaScript access:

    httponly=True

### Configure SameSite

Choose an appropriate:

    samesite="Lax"

or other suitable policy.

### Avoid Sensitive Cookie Data

Do not place passwords or secrets in ordinary cookies.

---

# 34. Session Fixation

Session fixation is an authentication attack in which an attacker attempts to cause a victim to use a session identifier known to the attacker.

Authentication systems should ensure that session identifiers are appropriately rotated or regenerated when login state changes.

Well-designed authentication libraries help manage this correctly.

---

# 35. Session Expiration

Authentication sessions should have appropriate lifetime policies.

Possible strategies include:

- Session expiration
- Idle timeout
- Absolute timeout
- Logout
- Server-side session invalidation where applicable

The correct policy depends on the application's security requirements.

---

# 36. Cookie Size

Cookies are designed for small amounts of data.

Do not use cookies as a general-purpose database.

For larger data, use:

    Database
    Server-side storage
    Appropriate browser storage

depending on the use case.

---

# 37. Authentication Example

A simplified Flask session authentication flow:

    @app.route("/login", methods=["POST"])
    def login():

        user = find_user()

        if user and valid_password:
            session["user_id"] = user.id

            return redirect(
                url_for("dashboard")
            )

        return "Invalid credentials"

Dashboard:

    @app.route("/dashboard")
    def dashboard():

        user_id = session.get("user_id")

        if user_id is None:
            return redirect(
                url_for("login")
            )

        return "Dashboard"

Logout:

    @app.route("/logout")
    def logout():

        session.pop("user_id", None)

        return redirect(
            url_for("login")
        )

---

# 38. Common Mistakes

## Mistake 1 — Storing passwords in cookies

Never do this.

## Mistake 2 — Storing secrets in Flask sessions

Avoid storing sensitive secrets directly in the default client-side session.

## Mistake 3 — Hard-coding production secret keys

Use secure configuration.

## Mistake 4 — Ignoring HTTPS

Sensitive authentication traffic should use HTTPS.

## Mistake 5 — Making every cookie accessible to JavaScript

Use `HttpOnly` where JavaScript access is unnecessary.

## Mistake 6 — Ignoring SameSite

Choose a suitable SameSite policy.

## Mistake 7 — Treating cookies as a database

Cookies are small client-side data mechanisms.

---

# 39. Best Practices

- Use HTTPS in production.
- Keep Flask's secret key secure.
- Do not store passwords in cookies or sessions.
- Use `HttpOnly` for cookies that do not need JavaScript access.
- Use `Secure` for sensitive cookies over HTTPS.
- Configure `SameSite` appropriately.
- Use reasonable session expiration policies.
- Validate authentication state on the server.
- Avoid storing unnecessary data in sessions.
- Use a trusted authentication/session library when appropriate.

---

# 40. Important Mental Model

Remember:

    HTTP
      ↓
    Stateless
      ↓
    Need State
      ↓
    Sessions / Cookies
      ↓
    Login State
      ↓
    Protected Resources

---

# 41. Key Takeaways

- HTTP is stateless.
- Sessions help maintain application state.
- Cookies are small browser-stored pieces of data.
- Flask provides a `session` object.
- `session.get()` safely reads a value.
- `session.pop()` removes a session value.
- `session.clear()` removes all session values.
- Flask can set cookies using `set_cookie()`.
- Flask can read cookies through `request.cookies`.
- Cookies have security attributes such as `Secure`, `HttpOnly`, and `SameSite`.
- Flask's default session is cookie-based and signed.
- Signed does not mean encrypted.
- Never store passwords in sessions or cookies.
- Use HTTPS for production authentication.

---

# ⭐ Final Summary

The basic relationship is:

    Browser
       ↕
    Cookies
       ↕
    Flask Session
       ↕
    Flask Application
       ↕
    Database

For authentication:

    Login
      ↓
    Verify User
      ↓
    Create Login State
      ↓
    Session/Cookie
      ↓
    Future Requests
      ↓
    Protected Routes
      ↓
    Logout