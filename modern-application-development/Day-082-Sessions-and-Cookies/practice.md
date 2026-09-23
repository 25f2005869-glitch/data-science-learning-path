# 🧠 Day 082 — Sessions and Cookies Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 082  
**Topic:** Sessions and Cookies  

---

## 🎯 Practice Goals

Practice:

- HTTP statelessness
- Flask sessions
- Cookies
- Session management
- Login state
- Cookie attributes
- Authentication security

---

# 🟢 Level 1 — Conceptual Questions

### Q1. What does stateless mean in HTTP?

### Q2. Why do web applications need state management?

### Q3. What is a session?

### Q4. What is a cookie?

### Q5. What is the difference between a session and a cookie?

### Q6. What is the purpose of Flask's `session` object?

### Q7. Why is `SECRET_KEY` important?

### Q8. What does `session.get()` do?

### Q9. What does `session.pop()` do?

### Q10. What does `session.clear()` do?

---

# 🟡 Level 2 — Flask Session Practice

## Q11. Set a Session Value

Store:

    user_id = 101

inside the Flask session.

---

## Q12. Read the Session Value

Retrieve:

    user_id

using `session.get()`.

---

## Q13. Check Login

Write code that checks whether:

    user_id

exists in the session.

---

## Q14. Remove Login State

Remove:

    user_id

from the session.

---

## Q15. Clear Session

Write the statement that clears all session values.

---

# 🟡 Level 3 — Cookie Practice

## Q16. Set a Cookie

Create a Flask response that sets:

    username = Saloni

as a cookie.

---

## Q17. Read a Cookie

Read:

    username

from the incoming request.

---

## Q18. Delete a Cookie

Delete:

    username

from a response.

---

## Q19. Persistent Cookie

Create a cookie with:

    max_age = 86400

Explain what this means.

---

## Q20. Secure Cookie

Create a cookie using:

    secure=True
    httponly=True
    samesite="Lax"

Explain the purpose of each setting.

---

# 🟠 Level 4 — Authentication Exercises

## Exercise 1 — Login Session

Create a Flask login route.

After successful authentication:

    session["user_id"] = user.id

Redirect the user to:

    /dashboard

---

## Exercise 2 — Protected Dashboard

Create:

    /dashboard

The route should:

1. Check the session.
2. Allow authenticated users.
3. Redirect unauthenticated users to login.

---

## Exercise 3 — Logout

Create:

    /logout

Remove the user's authentication state.

---

## Exercise 4 — User Preference

Use a cookie to store:

    theme = dark

Read the cookie on a later request.

---

# 🔴 Level 5 — Student Portal Challenge

Build a simple **Student Portal Authentication System**.

## Login

Fields:

    Email
    Password

After successful login:

    session["user_id"] = user.id

## Dashboard

Display:

    Welcome, Student

Only authenticated users should access it.

## Logout

Remove the authentication state.

## Preference Cookie

Store:

    theme = dark

as a cookie.

---

# 🔐 Security Practice

For each item, explain why it matters:

### Q21.

    HTTPS

### Q22.

    secure=True

### Q23.

    httponly=True

### Q24.

    samesite="Lax"

### Q25.

Strong `SECRET_KEY`

---

# 🧩 Scenario Questions

### Scenario 1

A user logs in successfully.

How can the application remember the login during later requests?

---

### Scenario 2

A user visits `/dashboard` without logging in.

What should the application do?

---

### Scenario 3

A developer stores:

    password = "mypassword123"

inside a cookie.

Is this safe?

Explain why.

---

### Scenario 4

A developer stores an API secret inside the default Flask session.

Is this a good practice?

Explain why.

---

# 🧠 Difference Practice

Complete the table:

| Feature | Session | Cookie |
|---|---|---|
| Maintains application state | ? | ? |
| Stored in browser | ? | ? |
| Can be sent with HTTP requests | ? | ? |
| Has `HttpOnly` attribute | ? | ? |
| Used for login state | ? | ? |

---

# 🧪 Debugging Practice

Consider:

    username = session["username"]

What can happen if `"username"` does not exist?

Rewrite it using:

    session.get()

---

# 🧪 Security Debugging

Consider:

    response.set_cookie(
        "password",
        password
    )

What is wrong with this approach?

Explain how the design should be changed.

---

# ⭐ Final Challenge

Build a Flask application with:

    Register
       ↓
    Login
       ↓
    Session
       ↓
    Dashboard
       ↓
    Cookie Preference
       ↓
    Logout

Requirements:

- SQLite
- SQLAlchemy
- Flask
- Password hashing
- Flask session
- Cookie
- Protected dashboard
- Logout
- Secure cookie configuration

---

# ✅ Self-Assessment

- [ ] I understand HTTP statelessness.
- [ ] I understand sessions.
- [ ] I understand cookies.
- [ ] I can set session values.
- [ ] I can read session values.
- [ ] I can remove session values.
- [ ] I can clear a session.
- [ ] I can set a cookie.
- [ ] I can read a cookie.
- [ ] I can delete a cookie.
- [ ] I understand cookie attributes.
- [ ] I understand `Secure`.
- [ ] I understand `HttpOnly`.
- [ ] I understand `SameSite`.
- [ ] I understand Flask's default cookie-based session.
- [ ] I understand why passwords should never be stored in cookies.
- [ ] I can protect a Flask route using session state.

---

# 📌 Final Revision

Remember:

    HTTP
      ↓
    Stateless
      ↓
    Session + Cookie
      ↓
    Maintain State
      ↓
    Authentication
      ↓
    Protected Resources