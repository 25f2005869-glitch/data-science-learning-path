# ⚡ Day 053 — Error Handling — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 053  
**Topic:** Error Handling

---

# 🔹 Error

An error is a problem encountered during parsing or execution.

---

# 🔹 Three Common Error Categories

| Type | Meaning |
|---|---|
| Syntax Error | Invalid JavaScript syntax |
| Runtime Error | Error while executing |
| Logical Error | Program runs but gives wrong result |

---

# 🔹 try...catch

    try {
        riskyCode();
    } catch (error) {
        console.error(error);
    }

Use it to handle exceptions.

---

# 🔹 finally

    try {
        // code
    } catch (error) {
        // handle error
    } finally {
        // cleanup
    }

`finally` runs after the `try`/`catch` process.

---

# 🔹 throw

Create your own exception:

    throw new Error("Invalid input");

---

# 🔹 Error Object

    try {
        throw new Error("Something went wrong");
    } catch (error) {
        console.log(error.name);
        console.log(error.message);
        console.log(error.stack);
    }

Important properties:

- `name`
- `message`
- `stack`

---

# 🔹 Common Error Types

| Error | Typical Cause |
|---|---|
| `Error` | General error |
| `SyntaxError` | Invalid syntax / invalid JSON parsing |
| `ReferenceError` | Unknown variable or binding |
| `TypeError` | Invalid operation for a value's type |
| `RangeError` | Value outside valid range |
| `URIError` | Invalid URI operation |

---

# 🔹 ReferenceError

    console.log(unknownVariable);

Unknown identifier → `ReferenceError`

---

# 🔹 TypeError

    const value = null;

    console.log(value.name);

Invalid property operation → `TypeError`

---

# 🔹 RangeError

    new Array(-1);

Invalid range → `RangeError`

---

# 🔹 JSON Error

    JSON.parse("invalid");

Invalid JSON can produce a `SyntaxError`.

---

# 🔹 Custom Validation

    function checkScore(score) {
        if (score < 0 || score > 100) {
            throw new Error("Invalid score");
        }
    }

---

# 🔹 Catch Without Error Variable

    try {
        JSON.parse("invalid");
    } catch {
        console.log("Invalid data");
    }

---

# 🔹 Error Propagation

    function test() {
        throw new Error("Problem");
    }

    try {
        test();
    } catch (error) {
        console.log(error.message);
    }

An exception can propagate to an outer handler.

---

# 🔹 console.error()

    console.error("Operation failed");

Useful for reporting errors in the developer console.

---

# 🧠 Golden Rules

1. Use `try...catch` when exceptions are expected.
2. Validate input.
3. Throw meaningful errors.
4. Use `finally` for cleanup.
5. Never silently ignore important errors.
6. Keep user-facing messages simple.
7. Log useful technical information for debugging.
8. Do not use exceptions for normal control flow.
9. Fix the underlying cause of errors.
10. Avoid exposing sensitive internal details.

---

# ⭐ Remember

    try
      ↓
    Attempt code

    catch
      ↓
    Handle exception

    finally
      ↓
    Cleanup

    throw
      ↓
    Create/raise exception