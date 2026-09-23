# ⚡ Day 082 — Sessions and Cookies Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 082  
**Topic:** Sessions and Cookies  

---

## 🔹 HTTP

    HTTP = Stateless

Each request is independent.

Sessions and cookies help maintain state.

---

## 🔹 Flask Session

Import:

    from flask import session

Set:

    session["user_id"] = user.id

Read:

    user_id = session.get("user_id")

Check:

    if "user_id" in session:
        ...

Remove one:

    session.pop("user_id", None)

Clear all:

    session.clear()

---

## 🔹 Secret Key

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY"
    )

Keep the production secret key private.

---

## 🔹 Protected Route

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            return redirect(
                url_for("login")
            )

        return "Dashboard"

---

## 🔹 Logout

    session.pop("user_id", None)

or, when appropriate:

    session.clear()

---

## 🔹 Set Cookie

    from flask import make_response

    response = make_response("Cookie set")

    response.set_cookie(
        "username",
        "Saloni"
    )

    return response

---

## 🔹 Read Cookie

    from flask import request

    username = request.cookies.get(
        "username"
    )

---

## 🔹 Delete Cookie

    response = make_response(
        "Cookie deleted"
    )

    response.delete_cookie(
        "username"
    )

    return response

---

## 🔹 Cookie Attributes

| Attribute | Purpose |
|---|---|
| `max_age` | Cookie lifetime in seconds |
| `expires` | Cookie expiration date/time |
| `path` | URL path scope |
| `domain` | Domain scope |
| `secure` | Send over HTTPS |
| `httponly` | Prevent normal JavaScript access |
| `samesite` | Control cross-site sending |

---

## 🔹 Secure Cookie

    response.set_cookie(
        "session_id",
        value,
        secure=True,
        httponly=True,
        samesite="Lax"
    )

Use settings appropriate for the application and deployment.

---

## 🔹 Session Cookie

Generally has no persistent expiration.

It is associated with the browser session.

---

## 🔹 Persistent Cookie

Uses an expiration configuration.

Example:

    response.set_cookie(
        "theme",
        "dark",
        max_age=86400
    )

Approximately one day.

---

## 🔹 Sessions vs Cookies

    Session
    → Application state

    Cookie
    → Browser-stored data

---

## 🔹 Flask Default Session

Important:

    Flask default session
          ↓
    Cookie-based
          ↓
    Cryptographically signed

Signed does not mean encrypted.

Do not store passwords or sensitive secrets directly in it.

---

## 🔹 Authentication Flow

    Login
      ↓
    Verify Credentials
      ↓
    Create Session/Login State
      ↓
    Cookie
      ↓
    Future Requests
      ↓
    Protected Route
      ↓
    Logout

---

## 🔹 Session Operations

| Operation | Code |
|---|---|
| Set | `session["key"] = value` |
| Get | `session.get("key")` |
| Remove | `session.pop("key", None)` |
| Clear | `session.clear()` |

---

## 🔹 Cookie Operations

| Operation | Flask |
|---|---|
| Set | `response.set_cookie()` |
| Read | `request.cookies.get()` |
| Delete | `response.delete_cookie()` |

---

## 🔐 Security

    HTTPS
       +
    Secure
       +
    HttpOnly
       +
    SameSite
       +
    Strong Secret Key
       +
    No Passwords in Cookies/Sessions

---

## ⭐ Remember

    HTTP → Stateless

    Session → Maintains application state

    Cookie → Small browser-stored data

    session.get() → Read safely

    session.pop() → Remove one

    session.clear() → Remove all